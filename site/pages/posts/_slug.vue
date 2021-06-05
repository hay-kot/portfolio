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
import { format } from "date-fns";

export default {
  async asyncData({ $content, params, $axios }) {
    const postInMarkdown = await $content(params.slug)
      .fetch()
      .catch((err) => {
        console.error(err);
      });

    ctx.seo({
      name: "Blog",
      title: postInMarkdown.title,
      templateTitle: "%name% | %title%",
      description: postInMarkdown.summary,
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
    dateFormatted() {
      return format(new Date(this.postInMarkdown.date), "MMMM d, Y");
    },
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
