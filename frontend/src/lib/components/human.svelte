<script>
    import human from "$lib/assets/human.png"
    export let humancontent;
</script>


<div class="flex items-start gap-4">
    <span class="relative flex shrink-0 overflow-hidden rounded-full border w-8 h-8">
      <img class="aspect-square h-full w-full" src={human} alt="" />
    </span>
    <div class="grid gap-1">
      <div class="font-bold">You</div>
      <div class="prose prose-stone">
        <p>
          {humancontent}
        </p>
      </div>
    </div>
  </div>

