<template>
  <div class="w-full h-full md:flex md:row mt-2 md:mt-0">
    <img
      class="m-auto rounded h-52 md:object-cover md:w-52"
      :src="image"
      alt=""
    />
    <div
      class="
        bg-background-primary
        border-green-900
        rounded-b
        lg:rounded-b-none
        p-4
      "
    >
      <div class="mb-4">
        <h2 class="text-2xl font-bold">
          <nuxt-link :to="`/blog/${slug}`" class="text-copy-primary">
            {{ title }}
          </nuxt-link>
        </h2>
        <p class="text-gray-600" v-if="readingTime">
          {{ readingTime }}
        </p>
        <div class="flex text-sm mb-1">
          <TagButton
            v-for="(tag, index) in tags.slice(0, 3)"
            :key="`${index}-${tag}`"
            :tag="tag"
          />
        </div>

        <p class="text-gray-500 text-md">
          {{ summary }}
        </p>
      </div>
      <!-- Read More Section -->
      <div class="flex">
        <img
          class="w-10 h-10 rounded-full mr-4"
          src="~assets/img/avatar.svg"
          alt="Avatar of Writer"
        />
        <div class="text-sm">
          <p class="text-gray-500 leading-none">{{ author }}</p>
          <p class="text-gray-600">{{ date }}</p>
        </div>
        <div class="ml-auto mt-auto">
          <nuxt-link :to="`/blog/${slug}`" class="font-bold uppercase">
            Read More
          </nuxt-link>
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
    readingTime: {
      default: false,
    },
    tags: {
      default: false,
    },
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

<style>
</style>