<template>
  <div class="w-full h-full">
    <div
      class="h-48 flex-none bg-cover rounded-t"
      :style="`background-image: url(${image})`"
      title="River"
    ></div>
    <div
      class="bg-background-primary border-r border-l border-b border-green-900 lg:border-green-900 rounded-b lg:rounded-b-none p-4"
    >
      <div class="mb-8">
        <h2 class="text-3xl font-bold">
          <nuxt-link :to="`/posts/${slug}`" class="text-copy-primary">{{
            title
          }}</nuxt-link>
        </h2>
        <p class="text-gray-500 text-md">
          {{ summary }}
        </p>
      </div>
      <div class="flex">
        <img
          class="w-10 h-10 rounded-full mr-4"
          src="~assets/img/avatar.jpg"
          alt="Avatar of Writer"
        />
        <div class="text-sm">
          <p class="text-gray-500 leading-none">{{ author }}</p>
          <p class="text-gray-600">{{ date }}</p>
        </div>
        <div class="ml-auto mt-auto">
          <nuxt-link :to="`/posts/${slug}`" class="font-bold uppercase"
            >Read More</nuxt-link
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    slug: String,
    title: String,
    summary: String,
    date: String,
    author: {
      default: "Hayden",
    },
    image: {
      default: "",
    },
  },
};
</script>

<style>
</style>