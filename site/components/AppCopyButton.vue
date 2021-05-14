<template>
  <button
    ref="copy"
    class="transition transform hover:-translate-y-1 text-white hover:text-secondary absolute right-0 top-0 hover:transform leading-none px-2 py-2 bg-opacity-100 text-sm uppercase font-semibold mr-3 mt-3"
  >
    <svg
      v-if="state === 'copied'"
      class="w-5 h-5"
      fill="none"
      style="width: 24px; height: 24px"
      viewBox="0 0 24 24"
    >
      <path
        fill="currentColor"
        d="M10,17L6,13L7.41,11.59L10,14.17L16.59,7.58L18,9M12,3A1,1 0 0,1 13,4A1,1 0 0,1 12,5A1,1 0 0,1 11,4A1,1 0 0,1 12,3M19,3H14.82C14.4,1.84 13.3,1 12,1C10.7,1 9.6,1.84 9.18,3H5A2,2 0 0,0 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5A2,2 0 0,0 19,3Z"
      />
    </svg>
    <svg
      v-else
      class="w-5 h-5"
      fill="none"
      style="width: 24px; height: 24px"
      viewBox="0 0 24 24"
    >
      <path
        fill="currentColor"
        d="M19,21H8V7H19M19,5H8A2,2 0 0,0 6,7V21A2,2 0 0,0 8,23H19A2,2 0 0,0 21,21V7A2,2 0 0,0 19,5M16,1H4A2,2 0 0,0 2,3V17H4V3H16V1Z"
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