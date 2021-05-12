<template>
  <button ref="copy" class="absolute right-0 bottom-0 leading-none shadow-lg px-2 py-2 text-white bg-gray-800 text-sm uppercase rounded-md border border-white font-semibold mr-3 mb-3">
    <svg
      v-if="state === 'copied'"
      class="w-5 h-5"
      fill="none"
      stroke-linecap="round"
      stroke-linejoin="round"
      stroke-width="2"
      viewBox="0 0 24 24"
      stroke="currentColor"
    >
      <path
        d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"
      />
    </svg>
    <svg
      v-else
      class="w-5 h-5"
      fill="none"
      stroke-linecap="round"
      stroke-linejoin="round"
      stroke-width="2"
      viewBox="0 0 24 24"
      stroke="currentColor"
    >
      <path
        d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3"
      />
    </svg>
  </button>
</template>

<script>
import Clipboard from "clipboard";
export default {
  data() {
    return {
      state: "init",
    };
  },
  mounted() {
    const copyCode = new Clipboard(this.$refs.copy, {
      target(trigger) {
        return trigger.previousElementSibling;
      },
    });
    copyCode.on("success", (event) => {
      event.clearSelection();
      this.state = "copied";
      window.setTimeout(() => {
        this.state = "init";
      }, 2000);
    });
  },
};
</script>

<style lang="css">

</style>