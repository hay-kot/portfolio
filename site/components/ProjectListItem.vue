<template>
  <li class="checkmark">
    <div class="flex pr-6">
      <div class="w-full">{{ title }}</div>
      <div class="flex w-full">
        <div class="ml-auto mr-2 flex">
          <img
            v-if="pythonLogo"
            src="~assets/img/code/python-logo.svg"
            class="m-1 w-6 h-6"
            alt=""
          />
          <img
            v-if="vueLogo"
            src="~assets/img/code/vue-logo.svg"
            class="ml-auto m-1 w-6 h-6"
            alt=""
          />
          <img
            v-if="goLogo"
            src="~assets/img/code/go-logo.svg"
            class="ml-auto m-1 w-12 h-6"
            alt=""
          />
        </div>
        <p>
          <a v-if="docs" :href="docs">Docs</a> {{ docs ? "·" : "" }}
          <a v-if="source" :href="source">Source Code</a>
          <a v-if="!docs && !source"> Closed Source </a>
        </p>
      </div>
    </div>
    <div class="text-lg text-gray-600">
      {{ description }}
    </div>
  </li>
</template>

<script>
export default {
  props: {
    title: {
      default: "Mealie",
    },
    logos: {
      type: [Array],
    },
    source: {
      default: null,
    },
    docs: {
      default: null,
    },
    description: {
      default: "",
    },
    vueLogo: {
      type: Boolean,
      default: false,
    },
    pythonLogo: {
      type: Boolean,
      default: false,
    },
    goLogo: {
      type: Boolean,
      default: false,
    },
  },
};
</script>

<style lang="scss" scoped>
</style>