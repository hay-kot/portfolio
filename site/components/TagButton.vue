<template>
  <div>
    <nuxt-link :to="`/blog/tags/${tag}`" class="bg-primary-color rounded-full pr-3">
      {{ titleCase(tag) }}
    </nuxt-link>
  </div>
</template>

<script>
export default {
  props: {
    tag: String,
  },
  methods: {
    titleCase(str) {
      return str
        .toLowerCase()
        .split(" ")
        .map(function (word) {
          return word.charAt(0).toUpperCase() + word.slice(1);
        })
        .join(" ");
    },
  },
};
</script>

<style scoped>
</style>