<script>
  import { X_API_ACCESS_HEADER, BACKEND_API } from "$lib/index";
  import { authToken } from "$lib/stores/auth";
  import { goto } from "$app/navigation";
  import Errorcomponent from "$lib/components/errorcomponent.svelte";
  import Successcomponent from "$lib/components/successcomponent.svelte";
  import Loader from "$lib/components/loader.svelte";
  import { onMount } from "svelte";
  onMount(() => {
    authToken.set(null); // or authToken.set('') if you prefer an empty string
  });
  let apiKey = "";
  let repoLink = "";
  let errorMessage = "";
  let showSuccess = false;
  let countdown = 3;
  let showModal = false;
  async function submitCredentials() {
    try {
      showModal = true;
      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), 20000); // 10 seconds timeout
      const response = await fetch(`${BACKEND_API}/repository`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-API-Key": X_API_ACCESS_HEADER,
        },
        body: JSON.stringify({ github_url: repoLink, openai_api_key: apiKey }),
        signal: controller.signal,
      });

      clearTimeout(timeoutId);

      if (response.ok) {
        const data = await response.json();
        if (data.api_key) {
          showSuccess = true;
          showModal = false;
          authToken.set(data.api_key);

          const interval = setInterval(() => {
            countdown--;
            if (countdown === 0) {
              clearInterval(interval);
              goto("/ask");
            }
          }, 1000);
        } else {
          throw new Error("API key not found in response");
        }
      } else {
        showModal = false;
        throw new Error(`HTTP error! status: ${response.status}`);
      }
    } catch (error) {
      console.error("There was a problem with the fetch operation:", error);
      if (error.name === "AbortError") {
        showModal = false;
        errorMessage = "Request timed out after 10 seconds. Please try again.";
      } else {
        showModal = false;
        errorMessage = `An error occurred: ${error.message}`;
      }
    }
  }
</script>

{#if showModal}
  <Loader />
{/if}
<div class="flex flex-col min-h-[100dvh] dark:bg-gray-900 dark:text-gray-50">
  <div class="flex-1 flex flex-col">
    <header
      class="px-4 lg:px-6 h-14 flex items-center bg-blue-900 text-gray-50 dark:bg-gray-800 dark:text-gray-50"
    >
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
      <section class="bg-gray-100 dark:bg-gray-800 p-4 md:p-6 flex-1">
        {#if showSuccess}
          <Successcomponent />
          <p>Redirecting in {countdown} seconds...</p>
        {/if}

        {#if errorMessage}
          <Errorcomponent {errorMessage} />
        {/if}
        <div class="container max-w-7xl">
          <h2 class="text-2xl font-bold mb-4">Connect to your Repository</h2>
          <form class="grid gap-4" on:submit|preventDefault={submitCredentials}>
            <div class="grid gap-2">
              <label
                class="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
                for="api-key"
              >
                OpenAI API Key
              </label>
              <input
                class="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
                id="api-key"
                placeholder="Enter your OpenAI API key"
                type="text"
                bind:value={apiKey}
              />
            </div>
            <div class="grid gap-2">
              <label
                class="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
                for="repo-link"
              >
                Repository Link
              </label>
              <input
                class="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
                id="repo-link"
                placeholder="Enter your repository link"
                type="text"
                bind:value={repoLink}
              />
            </div>
            <button
              type="submit"
              class="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 bg-black text-white hover:bg-black/90 h-10 px-4 py-2 justify-self-end"
            >
              Connect
            </button>
          </form>
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
</div>

<style>
  @tailwind base;
  @tailwind components;
  @tailwind utilities;
</style>
