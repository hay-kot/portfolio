export default {
  target: "static",
  ssr: true,
  generate: {
    crawler: true,
  },

  head: {
    title: "hay-kot.dev",
    meta: [
      { charset: "utf-8" },
      { name: "viewport", content: "width=device-width, initial-scale=1" },
      {
        hid: "description",
        name: "description",
        content: process.env.npm_package_description || "",
      },
      {
        hid: "twitter:card",
        name: "twitter:card",
        content: "summary_large_image",
      },
    ],
    link: [
      { rel: "icon", type: "image/x-icon", href: "/favicon.ico" },
      {
        rel: "stylesheet",
        href: "https://fonts.googleapis.com/css?family=Nunito+Sans:400,700",
      },
    ],
  },

  css: [],

  plugins: [],
  plausible: {
    domain: "hay-kot.dev",
  },
  components: true,

  buildModules: ["@nuxtjs/tailwindcss", "@aceforth/nuxt-optimized-images"],

  optimizedImages: {
    optimizeImages: true,
  },

  modules: [
    "vue-plausible",
    "@nuxtjs/axios",
    "@nuxt/content",
    ["vue-scrollto/nuxt", { duration: 500, easing: "ease" }],
  ],

  content: {
    markdown: {
      prism: {
        theme: "prism-themes/themes/prism-material-oceanic.css",
      },
    },
  },

  axios: {},

  build: {},
};
