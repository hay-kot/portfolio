const type = "website";
const url = "https://hay-kot.dev";
const title = "hay-kot";
const description =
  "Hayden is a Building Automation Engineer at Johnson Controls. While not a programmer by trade, Hayden spends his free time contributing to open source projects and building utility applications to support the community.";
const mainImage = "https://hay-kot.dev/_nuxt/img/39d706a.svg";
const twitterSite = "@kot_hay";
const twitterCard = "summary_large_image";

export const getSiteMeta = function (meta) {
  return [
    {
      hid: "description",
      name: "description",
      content: (meta && meta.description) || description,
    },
    {
      hid: "og:type",
      property: "og:type",
      content: (meta && meta.type) || type,
    },
    {
      hid: "og:url",
      property: "og:url",
      content: (meta && meta.url) || url,
    },
    {
      hid: "og:title",
      property: "og:title",
      content: (meta && meta.title) || title,
    },
    {
      hid: "og:description",
      property: "og:description",
      content: (meta && meta.description) || description,
    },
    {
      hid: "og:image",
      property: "og:image",
      content: (meta && meta.mainImage) || mainImage,
    },
    {
      hid: "twitter:card",
      name: "twitter:card",
      content: (meta && meta.twitterCard) || twitterCard,
    },
    {
      hid: "twitter:url",
      name: "twitter:url",
      content: (meta && meta.url) || url,
    },
    {
      hid: "twitter:title",
      name: "twitter:title",
      content: (meta && meta.title) || title,
    },
    {
      hid: "twitter:description",
      name: "twitter:description",
      content: (meta && meta.description) || description,
    },
    {
      hid: "twitter:image",
      name: "twitter:image",
      content: (meta && meta.mainImage) || mainImage,
    },
    {
      hid: "twitter:site",
      name: "twitter:site",
      content: (meta && meta.twitterSite) || twitterSite,
    },
  ];
};
