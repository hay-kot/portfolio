<template>
  <div>
    <div class="text-lg ml-10 uppercase font-bold text-green-700">
      {{ tag }}
    </div>
    <div
      class="container mx-auto p-10 grid grid-cols-1 sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-2 xl:grid-cols-3 gap-10 items-stretch border-b border-t border-green-900 mb-10"
    >
      <div v-for="(post, index) in filteredPosts" :key="index" class="post">
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
          'text-gray-400 hover:text-gray-400 cursor-not-allowed': !showPreviousPage,
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
      return `/tag/${this.tag}`;
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
    nextPage(currentPage, totalPages) {
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
      this.allPosts = await this.$content().fetch();
      this.allPosts.filter((e) => {
        return e.tags.includes(this.tag);
      });

      this.currentPage = parseInt(this.$route.query.page)
        ? parseInt(this.$route.query.page)
        : 1;

      this.filteredPosts = await this.$content()
        .where({ tags: { $contains: this.tag } })
        .sortBy("date", "desc")
        .limit(this.pagination)
        .skip((this.currentPage - 1) * this.pagination)
        .fetch();

      if (!this.filteredPosts[0]) {
        this.$router.push("/404")
      }
    },
  },
};
</script>
