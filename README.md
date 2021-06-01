# Nuxt Portfolio Starter

Deployed with Docker and Github Actions CI/CD

[See it Live!](https://hay-kot.dev)

![](./website.png)
Based on the [Gridsome Portfolio Starter](https://github.com/drehimself/gridsome-portfolio-starter).
## Article Processor

The Article Processor built in python, scans the drafts folder for drafts containing the `publish: true`. Any post containing `publish true` will be processed and imported into **Nuxt** for deployment. 

The Article Processor does the following: 

- Sets Metadata
  - slug: `slugify(title)`
  - path: `/{slug}`
  - date: `datetime.now()`
  - reading_time: `total_words += len(content_text) / 5`
  - image: transforms `./image.png` -> `/{slug}/image.png`
- Sets Image URLs in markdown from `./image.png` -> `/{slug}/image.png`
- Sets markdown file name to `YYYY-MM-DD-{slug}.md`
- Copies markdown file to `site/content`
- Copies non-markdown files to `site/static/{slug}/`

## Todo 

- [x] Metadata/FrontMatter Generator
- [x] Copy over Images
- [x] Image Optimization
- [x] Fix Domain Issues
- [x] Indicate Read Time for Posts
- [x] Custom Markdown Elements
- [x] Tags for posts
- [x] Response Pagination for blog posts
- [ ] Search posts with [Fuse.js](https://fusejs.io) and [vue-fuse](https://github.com/shayneo/vue-fuse)
