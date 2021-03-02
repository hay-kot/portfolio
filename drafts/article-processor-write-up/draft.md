---
# When Publish is set to true the article will be processed
publish: false
title: "Using Python to Generate Blog Frontmatter"
summary: "Using jinja2 templating as base, I was able to use python to create metadata for my blog posts and automate some of the borning parts about moving from a draft to published post"
tags: ['code', 'blogging', 'automation']
# Urls will be downloaded and inserted into the static folder
image: "./header.png"
---

![Test Image](./header.png)

I recently began the process of migrating my small blog from Ghost to a Static Site build with Nuxt. While there are some things I didn't like about Ghost, there were a few big things that really made me want to stick with the platform. Primarily the ease of use for generating metadata for posts and how easy it was to integrate images into posts. While I also loved the editor, unfortunately there's not great alternative for that at the moment. 

## The Goal
On the initial pass of what I'm calling the "Article Processor" I set out to accomplish a few things to bridge the gap of difficulty for moving a post from draft state to published. These are a few of the things I kept in mind while I was working

 - Easily draft posts with images in markdown
 - Automatically generate specific metadata such as 
   - reading time
   - slugs 
   - url-paths
 - Move, rename, and organize all files related to a post
 - Convert image paths in the markdown to what is expected by Nuxt
 - Create something flexible enough to expand upon.

## Defining the Data
As with most things these days I started by installing Pydantic, because why not! Pydantic is a great library that aids tremendously in data validation. It also comes with a few handy methods like `.dict()` that easily can convert nested classes into a friendly python dictionary that can be used directly in Jinja2 Templates. Here's the Pydantic class I came up with

```python
import datetime
from pathlib import Path
from typing import Optional

from pydantic import BaseModel

from frontmatter import Frontmatter


class MetaData(BaseModel):
    publish: bool
    title: str
    slug: Optional[str]
    path: Optional[str]
    date: Optional[datetime.date]
    summary: str
    reading_time: Optional[str]
    tags: list
    image: str


class Article(BaseModel):
    metadata: MetaData
    content: str
    dest: Optional[Path]

    @classmethod
    def from_file(cls, markdown_file: Path):
        raw_data = Frontmatter.read_file(markdown_file)
        frontmatter = raw_data.get("attributes")
        body = raw_data.get("body")
        return cls(metadata=MetaData(**frontmatter), content=body)

```

The Article class houses the entire markdown files contents where:

- metadata is the frontmatter content defined in the draft
- content is the markdown content of the file
- dest is the path that will be set as the destination in Nuxt

Note that the `Optional` parameters are ones that are set in the program while being processed. The `from_file` method uses the [frontmatters](https://github.com/jonbeebe/frontmatter) python library to get the data necessary from the draft posts markdown file. I didn't actually install the package, but did copy the code as it's a fairly small file. 

## Working with the Data
Now that the data has been defined, there are a few actions that need to be performed to get it ready to be published. The first of which is to determine if the post is to be published. I created a attribute in the frontmatter `published: bool` where true means to publish and false is to pass. A simple for loop through the files will determine what gets processed.

Once a article to be published is found, the script will do the following

### Sets Metadata
**slug:** Uses the python-slugify package to create a slug for the post with `slugify(title)`
**path:** defines the path URL for next as `/{slug}`
**Date:** Adds a published date the file with `datetime.now()`
**reading_time:** Creates a basic read time from the following equation `total_words += len(content_text) / 5`
**image:** transforms `./image.png` -> `/{slug}/image.png` for Nuxt to know where to find the images in the post

### Additional Processing
- Sets Image URLs in markdown from `./image.png` -> `/{slug}/image.png`
- Sets markdown file name to `YYYY-MM-DD-{slug}.md`
- Copies markdown file to `site/content`
- Copies non-markdown files to `site/static/{slug}/`

After settings the attributes on the Article and MetaData classes I can now pass that through a jinja2 template to render my markdown files. Which is where Pydantic comes in with a `.dict()` method that I can use with the jinja2 Template.

#### Function to create and write the processed markdown file
```python
def write_article(article: Article):
    with open(POST_TEMPLATE, "r") as f:
        template = Template(f.read())

    content = template.render(article=article.dict())

    with open(article.dest, "w") as f:
        f.write(content)
```

#### The Jinja2 Template used to render the final file
```jinja2
---
title: {{ article.metadata.title }}
path: /{{ article.metadata.slug }}
date: {{ article.metadata.date }}
summary: {{ article.metadata.summary }}
reading_time: {{ article.metadata.reading_time }}
tags: {{ article.metadata.tags }}
image: {{ article.metadata.image }}
---

{{ article.content }}
```

With that what may have taken me a few minutes per post now happens instantly! You can find the full source-code for this project and my whole website on [github](https://github.com/hay-kot/portfolio/tree/master/article-processor)