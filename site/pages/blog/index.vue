<template>
  <div>
    <div class="mx-auto border-b border-t border-green-900 mb-10 pb-10">
      <div
        v-for="(post, index) in posts"
        :key="index"
        class="mx-auto container-inner"
      >
        <BlogCard
          class="my-2"
          :slug="post.slug"
          :title="post.title"
          :summary="post.summary"
          :date="formatDate(post.date)"
          :image="post.image"
          :tags="post.tags"
          :reading-time="post.reading_time"
        />
      </div>

      <!-- end post -->
    </div>
    <div class="flex justify-center align-center text-xl items-center mb-3">
      <a
        :href="previousPage"
        :class="{
          'text-gray-400 hover:text-gray-400 cursor-not-allowed':
            !showPreviousPage,
        }"
      >
        &larr; Prev
      </a>
      <div class="text-base mx-10">
        Page {{ currentPage }} of {{ totalPages }}
      </div>
      <a
        :href="nextPage"
        :class="{
          'text-gray-400 hover:text-gray-400 cursor-not-allowed': !showNextPage,
        }"
      >
        Next &rarr;
      </a>
    </div>
  </div>
</template>

<script>
import { format } from "date-fns";

export default {
  data() {
    return {
      currentPage: 1,
      base: "/blog",
      windowWidth: 0,
      menuOpen: false,
    };
  },
  watchQuery: ["page"],
  async asyncData({ $content, route }) {
    const allPosts = await $content("articles").fetch();
    let currentPage = parseInt(route.query.page)
      ? parseInt(route.query.page)
      : 1;

    const totalPages = Math.ceil(allPosts.length / 12);

    if (currentPage > totalPages) {
      route.query.page = 1;
    }

    const posts = await $content("articles")
      .sortBy("date", "desc")
      .limit(12)
      .skip((currentPage - 1) * 12)
      .fetch();

    return { posts, allPosts, currentPage, totalPages };
  },
  computed: {
    showPreviousPage() {
      return this.currentPage !== 1;
    },
    previousPage() {
      return [0, 1].includes(this.currentPage - 1)
        ? this.base
        : `${this.base}?page=${this.currentPage - 1}`;
    },
    showNextPage() {
      return this.currentPage !== this.totalPages;
    },
    nextPage(currentPage, totalPages) {
      return this.totalPages > this.currentPage
        ? `${this.base}?page=${this.currentPage + 1}`
        : null;
    },
  },
  mounted() {
    this.updateWindowSize();
    window.addEventListener("resize", this.updateWindowSize);
  },
  beforeDestroyed() {
    window.removeEventListener("resize", this.updateWindowSize);
  },
  methods: {
    updateWindowSize() {
      this.windowWidth = window.innerWidth;
    },
    formatDate(dateToFormat) {
      return format(new Date(dateToFormat), "MMM d, Y");
    },
  },
};
</script>
