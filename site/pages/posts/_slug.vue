<template>
  <div>
    <div class="markdown-body">
      <h2 class="mb-0">{{ postInMarkdown.title }}</h2>
      <div>{{ dateFormatted }}</div>
      <div class="flex text-lg mt-3 mb-0">
        <TagButton
          v-for="(tag, index) in postInMarkdown.tags.slice(0, 3)"
          :key="`${index}-${tag}`"
          :tag="tag"
        />
      </div>

      <nuxt-content :document="postInMarkdown" />
      <nuxt-link to="/blog" class="font-bold uppercase">Back to Blog</nuxt-link>
    </div>
  </div>
</template>

<script>
import Vue from "vue";
import "~/assets/css/github-markdown.css";
import AppCopyButton from "~/components/AppCopyButton";
import { getSiteMeta } from "~/utils/getSiteMeta";
import { format } from "date-fns";

export default {
  async asyncData({ $content, params, $axios }) {
    const postInMarkdown = await $content(params.slug)
      .fetch()
      .catch((err) => {
        console.error(err);
      });

    return {
      postInMarkdown,
    };
  },
  mounted() {
    setTimeout(() => {
      const blocks = document.getElementsByClassName("nuxt-content-highlight");
      for (const block of blocks) {
        const CopyButton = Vue.extend(AppCopyButton);
        const component = new CopyButton().$mount();
        block.appendChild(component.$el);
      }
    }, 100);
  },
  computed: {
    meta() {
      const metaData = {
        type: "article",
        title: this.postInMarkdown.title,
        description: this.postInMarkdown.summary,
        url: `https://hay-kot.dev/posts/${this.$route.params.slug}`,
        mainImage: this.postInMarkdown.image,
      };
      return getSiteMeta(metaData);
    },
    dateFormatted() {
      return format(new Date(this.postInMarkdown.date), "MMMM d, Y");
    },
  },
  head() {
    return {
      title: this.postInMarkdown.title,
      meta: [
        ...this.meta,
        {
          property: "article:published_time",
          content: this.postInMarkdown.date,
        },
        {
          property: "article:tag",
          content: this.postInMarkdown.tags
            ? this.postInMarkdown.tags.toString()
            : "",
        },
        { name: "twitter:label1", content: "Written by" },
        { name: "twitter:data1", content: "hay-kot" },
        {
          name: "twitter:data2",
          content: this.postInMarkdown.tags
            ? this.postInMarkdown.tags.toString()
            : "",
        },
      ],
      link: [
        {
          hid: "canonical",
          rel: "canonical",
          href: `https://hay-kot.dev/posts/${this.$route.params.slug}`,
        },
      ],
    };
  },
};
</script>

<style>
.nuxt-content-highlight {
  position: relative;
}

.markdown-body {
  box-sizing: border-box;
  min-width: 200px;
  max-width: 980px;
  margin: 0 auto;
  padding: 45px;
}

@media (max-width: 767px) {
  .markdown-body {
    padding: 15px;
  }
}
</style>
