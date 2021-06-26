export default {
  target: "static",

  generate: {
    crawler: true
  },

  head: {
    title: "hay-kot.dev",
    meta: [
      { charset: "utf-8" },
      { name: "viewport", content: "width=device-width, initial-scale=1" },
      {
        hid: "description",
        name: "description",
        content: process.env.npm_package_description || ""
      },
      {
        hid: "twitter:card",
        name: "twitter:card",
        content: "summary_large_image"
      }
    ],
    link: [
      { rel: "icon", type: "image/x-icon", href: "/favicon.ico" },
      {
        rel: "stylesheet",
        href: "https://fonts.googleapis.com/css?family=Nunito+Sans:400,700"
      }
    ]
  },

  css: [],

  plugins: [],
  plausible: {
    domain: "hay-kot.dev"
  },
  components: true,

  buildModules: [
    "nuxt-vite",
    "@nuxtjs/tailwindcss",
    "@aceforth/nuxt-optimized-images",
    "@nuxtjs/pwa"
  ],

  pwa: {
    manifest: {
      name: "hay-kot.dev",
      description: "hay-kot Portfolio",
      theme_color: "#30855A"
    }
  },

  optimizedImages: {
    optimizeImages: true
  },

  modules: [
    "vue-plausible",
    "@nuxt/content",
    "@nuxtjs/axios",
    ["vue-scrollto/nuxt", { duration: 500, easing: "ease" }]
  ],

  content: {
    markdown: {
      prism: {
        theme: "prism-themes/themes/prism-material-oceanic.css"
      }
    }
  },

  axios: {},

  build: {}
};
