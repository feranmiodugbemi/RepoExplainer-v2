<script>
  import Bot from "$lib/components/bot.svelte";
  import Human from "$lib/components/human.svelte";
  import Errorcomponent from "$lib/components/errorcomponent.svelte";
  let question = "";
  let answer = "";
  let errorMessage = "";
  let components = [
    {
      type: Bot,
      props: { aicontent: "Hello, how are you doing?", isError: false },
    },
  ];

  async function fetchAiResponse() {
    if (question.trim() === "") {
      alert("Message cannot be empty");
      return;
    }

    components = [
      ...components,
      { type: Human, props: { humancontent: question } },
    ];
    components = [
      ...components,
      { type: Bot, props: { aicontent: "", isError: false } },
    ];
    const currentQuestion = question;
    question = "";

    try {
      const response = await fetch(`${import.meta.env.VITE_BACKEND_API}/question`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ question: currentQuestion }),
      });

      if (response.ok) {
        const data = await response.json();
        components[components.length - 1] = {
          type: Bot,
          props: { aicontent: data.answer, isError: false },
        };
        components = [...components]; // Trigger reactivity
      } else {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
    } catch (error) {
      console.error("There was a problem with the fetch operation:", error);
      errorMessage = `An error occurred: ${error.message}`;
      components[components.length - 1] = {
        type: Bot,
        props: { aicontent: `An error occurred: ${error.message}`, isError: true },
      };
      components = [...components]; // Trigger reactivity
    }
  }
</script>

<div class="flex flex-col min-h-[100dvh] dark:bg-gray-900 dark:text-gray-50">
  <header
    class="px-4 lg:px-6 h-14 flex items-center bg-blue-900 text-gray-50 dark:bg-gray-800 dark:text-gray-50"
  >
    <a class="flex items-center justify-center" href="/" rel="ugc">
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
        <path
          d="M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.403 5.403 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4"
        ></path>
        <path d="M9 18c-4.51 2-5-2-7-2"></path>
      </svg>
      <span class="text-xl font-bold">RepoGPT</span>
    </a>
    <nav class="ml-auto flex gap-4 sm:gap-6">
      <a
        class="text-sm font-medium hover:underline underline-offset-4"
        href="https://www.github.com/feranmiodugbemi/RepoExplainer-v2"
        target="_blank"
        rel="noopener noreferrer"
      >
        Star us on Github🖤
      </a>
    </nav>
  </header>
  <main class="flex-1 flex flex-col">
    {#if errorMessage}
      <Errorcomponent {errorMessage} />
    {/if}
    <section class="flex-1 flex flex-col">
      <div class="flex-1 flex flex-col">
        <div class="flex-1 overflow-y-auto p-4 md:p-6">
          {#each components as { type, props } (props)}
            <svelte:component this={type} {...props} />
          {/each}
        </div>
        <div
          class="bg-white dark:bg-gray-950 p-4 md:p-6 border-t border-gray-200 dark:border-gray-800 flex-shrink-0"
        >
          <div class="relative">
            <form on:submit|preventDefault={fetchAiResponse}>
              <input
                class="flex w-full bg-background text-sm ring-offset-background placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 min-h-[48px] rounded-2xl resize-none p-4 border border-neutral-400 shadow-sm pr-16 dark:border-gray-800"
                placeholder="Message RepoGPT..."
                name="message"
                id="message"
                type="text"
                bind:value={question}
              />
              <button
                class="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 bg-primary text-primary-foreground hover:bg-primary/90 absolute top-3 right-3 w-8 h-8 bg-blue-900"
                type="submit"
                disabled=""
              >
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
                  class="w-4 h-4"
                >
                  <path d="m5 12 7-7 7 7"></path>
                  <path d="M12 19V5"></path>
                </svg>
                <span class="sr-only">Send</span>
              </button>
            </form>
          </div>
          <p
            class="text-xs text-center text-neutral-700 font-medium dark:text-neutral-400"
          >
            RepoGPT can make mistakes. Consider checking important information.
            Note: A session lasts for only 15 mins
          </p>
        </div>
      </div>
    </section>
  </main>
  <footer class="bg-gray-100 p-6 md:py-12 w-full dark:bg-gray-800">
    <div class="container max-w-7xl flex items-center justify-between">
      <p class="text-sm text-gray-500 dark:text-gray-400">
        Built with love by <a
          class="text-sm hover:underline underline-offset-4"
          href="https://www.twitter.com/FeranmiOdugbemi/"
          target="_blank"
          rel="noopener noreferrer"
        >
          Feranmi
        </a>, Inspiration from
        <a
          class="text-sm hover:underline underline-offset-4"
          href="https://www.github.com/cmoorelabs"
          target="_blank"
          rel="noopener noreferrer"
        >
          Cmooredev
        </a>
      </p>
      <div class="flex flex-col gap-4">
        <div class="flex items-center gap-2">
          <span class="text-sm text-gray-500">Powered by</span>
          <a
            class="text-sm hover:underline underline-offset-4"
            href="https://www.langchain.com/"
            target="_blank"
            rel="noopener noreferrer"
          >
            Langchain
          </a>
          <a
            class="text-sm hover:underline underline-offset-4"
            href="https://www.openai.com/"
            target="_blank"
            rel="noopener noreferrer"
          >
            OpenAI
          </a>
        </div>
      </div>
    </div>
  </footer>
</div>

<style>
  @tailwind base;
  @tailwind components;
  @tailwind utilities;
</style>
