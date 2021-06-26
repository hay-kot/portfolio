<template>
  <div class="border-r-2">
    <div v-for="(value, key, index) in sidebar" :key="index" class="px-5">
      <h3 class="mt-3 font-bold">{{ key }}</h3>
      <ul v-for="(v, k) in value" :key="k">
        <nuxt-link class="my-1 ml-2" :to="`/wiki/${v}`">{{ k }}</nuxt-link>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      sidebar: {
        "Code Snippets": {
          Caddy: "snippets/caddy",
          Python: "snippets/python",
          "Item 3": "Testing 3",
          "Item 4": "Testing 4",
        },
        "Section 2": {
          "Item 1": "Testing 1",
          "Item 2": "Testing 2",
          "Item 3": "Testing 3",
          "Item 4": "Testing 4",
        },
      },
    };
  },
};
</script>

<style lang="scss" scoped>
</style>