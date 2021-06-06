<template>
  <div>
    <div class="container mx-auto text-lg uppercase font-bold text-green-700">
      {{ tag }}
    </div>
    <div class="mx-auto border-b border-t border-green-900 mb-10 pb-10">
      <div
        v-for="(post, index) in filteredPosts"
        :key="index"
        class="container-inner post max-w-3xl mx-auto"
      >
        <BlogCard
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
      posts: [],
      filteredPosts: [],
      currentPage: 1,
      allPosts: [],
      menuOpen: false,
      pagination: 3,
    };
  },
  mounted() {
    this.fetchData();
  },
  computed: {
    base() {
      return `blog/tags/${this.tag}`;
    },
    tag() {
      return this.$route.params.tag;
    },
    totalPages() {
      return Math.ceil(this.filteredPosts.length / this.pagination);
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
    nextPage() {
      return this.totalPages > this.currentPage
        ? `${this.base}?page=${this.currentPage + 1}`
        : `${this.base}?page=${this.currentPage}`;
    },
  },
  methods: {
    formatDate(dateToFormat) {
      return format(new Date(dateToFormat), "MMM d, Y");
    },
    async fetchData() {
      this.allPosts = await this.$content("articles").fetch();
      this.allPosts.filter((e) => {
        return e.tags.includes(this.tag);
      });

      this.currentPage = parseInt(this.$route.query.page)
        ? parseInt(this.$route.query.page)
        : 1;

      this.filteredPosts = await this.$content("articles")
        .where({ tags: { $contains: this.tag } })
        .sortBy("date", "desc")
        .limit(this.pagination)
        .skip((this.currentPage - 1) * this.pagination)
        .fetch();

      if (!this.filteredPosts[0]) {
        this.$router.push("/404");
      }
    },
  },
};
</script>
