<template>
  <div class="flex flex-wrap">
    <div class="w-full">
      <div class="flex flex-wrap flex-row justify-end mb-0 pt-2 pb-2">
        <button
          class="
            bg-green-700
            text-white text-xs
            font-bold
            uppercase
            px-3
            py-2
            ml-1
            shadow-sm
            hover:bg-green-500
            hover:shadow-lg
            border
            leading-normal
            rounded
            gab-1
            inline-flex
            items-center
          "
          @click="code = !code"
        >
          <svg
            v-if="!code"
            style="width: 24px; height: 24px"
            viewBox="0 0 24 24"
          >
            <path
              fill="currentColor"
              d="M14.6,16.6L19.2,12L14.6,7.4L16,6L22,12L16,18L14.6,16.6M9.4,16.6L4.8,12L9.4,7.4L8,6L2,12L8,18L9.4,16.6Z"
            />
          </svg>
          <svg v-else style="width: 24px; height: 24px" viewBox="0 0 24 24">
            <path
              fill="currentColor"
              d="M20,11V13H8L13.5,18.5L12.08,19.92L4.16,12L12.08,4.08L13.5,5.5L8,11H20Z"
            />
          </svg>
          <span class="ml-1">
            {{ code ? "Back" : "Code" }}
          </span>
        </button>
      </div>
      <div
        class="
          relative
          flex flex-col
          min-w-0
          break-words
          w-full
          mb-6
          shadow-md
          rounded
        "
      >
        <div class="px-4 flex-auto">
          <div class="tab-content tab-space">
            <div class="wrapper" v-if="!code">
              <slot> </slot>
            </div>
            <div class="wrapper" v-else>
              <slot name="code"> </slot>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "pink-tabs",
  data() {
    return {
      code: false,
      openTab: 1,
    };
  },
  methods: {},
};
</script>

<style lang="css">
.wrapper > * {
  margin-bottom: 1rem !important;
  margin-top: 1rem !important;
}
</style>

// <code-tab>

// Default Slot

// <template v-slot:code>

// ## Test Code
// ```js
// // testing 123
// ```
// </template>
// </code-tab>