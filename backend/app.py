from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import APIKeyHeader
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import tempfile
from dotenv import load_dotenv
from langchain import PromptTemplate, LLMChain
from langchain.llms import OpenAI
from config import model_name
from utils import format_user_question
from file_processing import clone_github_repo, load_and_index_files
from questions import ask_question, QuestionContext
import time
import uuid
from slowapi.errors import RateLimitExceeded
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address, Request


limiter = Limiter(key_func=get_remote_address)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "https://repoexplainer.vercel.app/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]   
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


# Use API key for simple "authentication"
API_KEY_HEADER = APIKeyHeader(name="X-API-Key")

# In-memory storage for user sessions
user_sessions = {}

# Session timeout (in seconds)
SESSION_TIMEOUT = 1200  # 20 mins

class Repository(BaseModel):
    github_url: str
    openai_api_key: str


class Question(BaseModel):
    question: str

class RepositoryContext:
    def __init__(self, repo_name, github_url, index, documents, file_type_counts, filenames, openai_api_key):
        self.repo_name = repo_name
        self.github_url = github_url
        self.index = index
        self.documents = documents
        self.file_type_counts = file_type_counts
        self.filenames = filenames
        self.conversation_history = ""
        self.llm = OpenAI(api_key=openai_api_key, temperature=0.2)
        self.llm_chain = self.create_llm_chain()
        self.last_accessed = time.time()

    def create_llm_chain(self):
        template = """
        Repo: {repo_name} ({github_url}) | Conv: {conversation_history} | Docs: {numbered_documents} | Q: {question} | FileCount: {file_type_counts} | FileNames: {filenames}
        Instr:
        1. Answer based on context/docs.
        2. Focus on repo/code.
        3. Consider:
        a. Purpose/features - describe.
        b. Functions/code - provide details/samples.
        c. Setup/usage - give instructions.
        4. Unsure? Say "I am not sure".
        Answer:
        """
        prompt = PromptTemplate(
            template=template,
            input_variables=["repo_name", "github_url", "conversation_history", "question", "numbered_documents", "file_type_counts", "filenames"]
        )
        return LLMChain(prompt=prompt, llm=self.llm)

def get_current_user(api_key: str = Depends(API_KEY_HEADER)):
    if api_key not in user_sessions:
        api_key = str(uuid.uuid4())
        user_sessions[api_key] = None
    return api_key

def clean_expired_sessions():
    current_time = time.time()
    expired_keys = [key for key, context in user_sessions.items() 
                    if context and current_time - context.last_accessed > SESSION_TIMEOUT]
    for key in expired_keys:
        del user_sessions[key]

@app.post("/repository")
@limiter.limit("100/minute")
async def set_repository(repo: Repository, request: Request, current_user: str = Depends(get_current_user)):
    clean_expired_sessions()
    github_url = repo.github_url
    openai_key = str(repo.openai_api_key)

    if not openai_key:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="OpenAI API key is required"
        )

    repo_name = github_url.split("/")[-1]
    
    with tempfile.TemporaryDirectory() as local_path:
        if clone_github_repo(github_url, local_path):
            index, documents, file_type_counts, filenames = load_and_index_files(local_path)
            if index is None:
                raise HTTPException(status_code=400, detail="No documents were found to index.")
            user_sessions[current_user] = RepositoryContext(repo_name, github_url, index, documents, file_type_counts, filenames, openai_api_key=openai_key)
            return {"message": "Repository cloned and indexed successfully", "api_key": current_user}
        else:
            raise HTTPException(status_code=400, detail="Failed to clone the repository")

@app.post("/question")
@limiter.limit("500/minute")
async def ask_repository_question(question: Question, request: Request, current_user: str = Depends(get_current_user)):
    clean_expired_sessions()
    if current_user not in user_sessions or user_sessions[current_user] is None:
        raise HTTPException(status_code=400, detail="Repository not set. Please set a repository first.")
    
    repo_context = user_sessions[current_user]
    repo_context.last_accessed = time.time()
    user_question = format_user_question(question.question)
    question_context = QuestionContext(
        repo_context.index,
        repo_context.documents,
        repo_context.llm_chain,
        model_name,
        repo_context.repo_name,
        repo_context.github_url,
        repo_context.conversation_history,
        repo_context.file_type_counts,
        repo_context.filenames
    )
    
    try:
        answer = ask_question(user_question, question_context)
        repo_context.conversation_history += f"Question: {user_question}\nAnswer: {answer}\n"
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)