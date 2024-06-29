<script>
  import repoexplainer from "$lib/assets/repoexplainer.png"
  import ME from "$lib/assets/ME.jpeg"
</script>
<div class="flex flex-col min-h-[100dvh] dark:bg-gray-900 dark:text-gray-50">
  <header class="px-4 lg:px-6 h-14 flex items-center bg-blue-900 text-gray-50 dark:bg-gray-800 dark:text-gray-50">
    <a class="flex items-center justify-center" href="/">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="24"
        height="24"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        stroke-width="2"
        stroke-linecap="round"
        stroke-linejoin="round"
        class="h-6 w-6"
      >
        <path d="M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.403 5.403 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4"></path>
        <path d="M9 18c-4.51 2-5-2-7-2"></path>
      </svg>
      <span class="text-xl font-bold">RepoExplainer</span>
    </a>
    <nav class="ml-auto flex gap-4 sm:gap-6">
      <a class="text-sm font-medium hover:underline underline-offset-4" href="https://www.github.com/RepoExplainer-v2" target="_blank" rel="noopener noreferrer">
        Star us on Github🖤
      </a>
    </nav>
  </header>
  <main class="flex-1">
    <section class="w-full py-12 md:py-24 lg:py-32">
      <div class="container px-4 md:px-6">
        <div class="grid gap-6 lg:grid-cols-[1fr_400px] lg:gap-12 xl:grid-cols-[1fr_600px]">
          <div class="flex flex-col justify-center space-y-4">
            <div class="space-y-2">
              <h1 class="text-3xl font-bold tracking-tighter sm:text-5xl xl:text-6xl/none text-blue-900 dark:text-blue-400">
                Converse with GitHub Repositories
              </h1>
              <p class="max-w-[600px] text-gray-500 md:text-xl dark:text-gray-400">
                RepoGPT is a web application that allows you to have natural language conversations with GitHub
                repositories, enabling you to explore and understand code more effectively.
              </p>
            </div>
            <div class="flex flex-col gap-2 min-[400px]:flex-row">
              <a
                class="inline-flex h-10 items-center justify-center rounded-md bg-blue-900 px-8 text-sm font-medium text-gray-50 shadow transition-colors hover:bg-blue-900/90 focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-blue-950 disabled:pointer-events-none disabled:opacity-50 dark:bg-blue-400 dark:text-gray-900 dark:hover:bg-blue-400/90 dark:focus-visible:ring-blue-300"
                href="/credentials"
              >
                Try it Now
              </a>
            </div>
          </div>
          <img
            src={repoexplainer}
            width="550"
            height="550"
            alt="Hero"
            class="mx-auto aspect-video overflow-hidden rounded-xl object-cover sm:w-full lg:order-last lg:aspect-square"
          />
        </div>
      </div>
    </section>
    <section id="features" class="w-full py-12 md:py-24 lg:py-32 bg-gray-100 dark:bg-gray-800">
      <div class="container px-4 md:px-6">
        <div class="flex flex-col items-center justify-center space-y-4 text-center">
          <div class="space-y-2">
            <h2 class="text-3xl font-bold tracking-tighter sm:text-5xl text-blue-900 dark:text-blue-400">
              Key Features
            </h2>
            <p class="max-w-[900px] text-gray-500 md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed dark:text-gray-400">
              RepoGPT offers a range of features to help you explore and understand GitHub repositories more
              effectively.
            </p>
          </div>
        </div>
        <div class="mx-auto grid max-w-5xl items-start gap-6 py-12 lg:grid-cols-3 lg:gap-12">
          <div class="relative">
            <div class="grid gap-1">
              <h3 class="text-lg font-bold text-blue-900 dark:text-blue-400">Natural Language Queries</h3>
              <p class="text-sm text-gray-500 dark:text-gray-400">
                Ask questions about the repository in plain language and get relevant information.
              </p>
            </div>
            <span class="absolute top-0 right-0 bg-green-200 text-green-800 px-2 py-1 text-xs font-semibold rounded-md flex items-center">
              <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
              </svg>
              Available
            </span>
          </div>
          <div class="relative">
            <div class="grid gap-1">
              <h3 class="text-lg font-bold text-blue-900 dark:text-blue-400">Code Explanation</h3>
              <p class="text-sm text-gray-500 dark:text-gray-400">
                Understand complex code snippets by having them explained in simple terms.
              </p>
            </div>
            <span class="absolute top-0 right-0 bg-green-200 text-green-800 px-2 py-1 text-xs font-semibold rounded-md flex items-center">
              <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
              </svg>
              Available
            </span>
          </div>
          <div class="relative">
            <div class="grid gap-1">
              <h3 class="text-lg font-bold text-blue-900 dark:text-blue-400">Codebase Navigation</h3>
              <p class="text-sm text-gray-500 dark:text-gray-400">
                Easily navigate and explore the structure of a repository using natural language.
              </p>
            </div>
            <span class="absolute top-0 right-0 bg-green-200 text-green-800 px-2 py-1 text-xs font-semibold rounded-md flex items-center">
              <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
              </svg>
              Available
            </span>
          </div>
          <div class="relative">
            <div class="grid gap-1">
              <h3 class="text-lg font-bold text-blue-900 dark:text-blue-400">Code Generation</h3>
              <p class="text-sm text-gray-500 dark:text-gray-400">
                Generates code on how to use a complex library/sdk with little to no docs.
              </p>
            </div>
            <span class="absolute top-0 right-0 bg-green-200 text-green-800 px-2 py-1 text-xs font-semibold rounded-md flex items-center">
              <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
              </svg>
              Available
            </span>
          </div>
          <div class="flex items-center justify-between">
            <div class="grid gap-1">
              <h3 class="text-lg font-bold text-blue-900 dark:text-blue-400">Commit explanation</h3>
              <p class="text-sm text-gray-500 dark:text-gray-400">
                Understand the context and purpose of code changes by having commit messages explained.
              </p>
            </div>
            <span class="bg-yellow-200 text-yellow-800 px-2 py-1 text-xs font-semibold rounded-md">Coming Soon</span>
          </div>
          <div class="flex items-center justify-between">
            <div class="grid gap-1">
              <h3 class="text-lg font-bold text-blue-900 dark:text-blue-400">Issue Summarization</h3>
              <p class="text-sm text-gray-500 dark:text-gray-400">
                Get concise summaries of GitHub issues to quickly understand the problem and proposed solutions.
              </p>
            </div>
            <span class="bg-yellow-200 text-yellow-800 px-2 py-1 text-xs font-semibold rounded-md">Coming Soon</span>
          </div>
        </div>
      </div>
    </section>
    
    <section id="about" class="w-full py-12 md:py-24 lg:py-32">
      <div class="container px-4 md:px-6">
        <div class="flex flex-col items-center justify-center space-y-4 text-center">
          <div class="space-y-2">
            <h2 class="text-3xl font-bold tracking-tighter sm:text-5xl text-blue-900 dark:text-blue-400">
              About the Developer
            </h2>
            <p class="max-w-[900px] text-gray-500 md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed dark:text-gray-400">
              RepoGPT was created by a passionate developer who wanted to make it easier for developers to
              navigate and understand GitHub repositories.
            </p>
          </div>
        </div>
        <div class="mx-auto grid max-w-5xl items-center gap-6 py-12 lg:grid-cols-2 lg:gap-12">
          <img
            src={ME}
            width="550"
            height="310"
            alt="Team"
            class="mx-auto aspect-video overflow-hidden rounded-xl object-cover object-center sm:w-full lg:order-last"
          />
          <div class="flex flex-col justify-center space-y-4">
            <div class="grid gap-4">
              <div class="grid gap-1">
              </div>
              <div class="grid gap-1">
                <h3 class="text-xl font-bold text-blue-900 dark:text-blue-400">Feranmi Odugbemi</h3>
                <p class="text-gray-500 dark:text-gray-400">Backend and AI Engineer</p>
                <p class="text-sm text-gray-500 dark:text-gray-400">
                  Feranmi is a skilled Engineer, Blah Blah
                  Blud na demi god sha
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
  <footer class="bg-gray-100 p-6 md:py-12 w-full dark:bg-gray-800">
    <div class="container max-w-7xl flex items-center justify-between">
      <p class="text-sm text-gray-500 dark:text-gray-400">Built with love by <a class="text-sm hover:underline underline-offset-4" href="https://www.twitter.com/FeranmiOdugbemi/" target="_blank" rel="noopener noreferrer">
        Feranmi
      </a>, Inspiration from <a class="text-sm hover:underline underline-offset-4" href="https://www.github.com/cmoorelabs" target="_blank" rel="noopener noreferrer">
        Cmooredev
      </a></p>
      <div class="flex flex-col gap-4">
        <div class="flex items-center gap-2">
          <span class="text-sm text-gray-500">Powered by</span>
          <a class="text-sm hover:underline underline-offset-4" href="https://www.langchain.com/" target="_blank" rel="noopener noreferrer">
            Langchain
          </a>
          <a class="text-sm hover:underline underline-offset-4" href="https://www.openai.com/" target="_blank" rel="noopener noreferrer">
            OpenAI
          </a>
        </div>
      </div>
    </div>
  </footer>
</div>