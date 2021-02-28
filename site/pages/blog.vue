<template>
  <div>
    <div
      class="container mx-auto p-10 grid grid-cols-1 sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10 items-stretch"
    >
      <div v-for="(post, index) in posts" :key="index" class="post h-full mb-12">
        <BlogCard
          :slug="post.slug"
          :title="post.title"
          :summary="post.summary"
          :date="formatDate(post.date)"
          :image="post.image"
        />
      </div>
      <!-- end post -->
    </div>

    <div class="flex justify-center align-center text-xl items-center mb-3">
      <a
        :href="previousPage"
        :class="{
          'text-gray-400 hover:text-gray-400 cursor-not-allowed': !showPreviousPage,
        }"
        >&larr; Prev</a
      >
      <div class="text-base mx-10">
        Page {{ currentPage }} of {{ totalPages }}
      </div>
      <a
        :href="nextPage"
        :class="{
          'text-gray-400 hover:text-gray-400 cursor-not-allowed': !showNextPage,
        }"
        >Next &rarr;</a
      >
    </div>
  </div>
</template>

<script>
import { format } from "date-fns";

export default {
  data() {
    return {
      posts: [],
      currentPage: 1,
      pagination: 3,
      allPosts: [],
      base: "/blog",
    };
  },
  computed: {
    totalPages() {
      return Math.ceil(this.allPosts.length / this.pagination);
    },
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
        : `${this.base}?page=${this.currentPage}`;
    },
  },
  methods: {
    formatDate(dateToFormat) {
      return format(new Date(dateToFormat), "MMMM d, Y");
    },
  },
  async fetch() {
    this.allPosts = await this.$content().fetch();

    this.currentPage = parseInt(this.$route.query.page)
      ? parseInt(this.$route.query.page)
      : 1;

    if (this.currentPage > this.totalPages) {
      this.$router.push("/blog");
      window.location.href = "/blog";
    }

    this.posts = await this.$content()
      .sortBy("date", "desc")
      .limit(this.pagination)
      .skip((this.currentPage - 1) * this.pagination)
      .fetch();
  },
  fetchOnServer: false,
};
</script>
