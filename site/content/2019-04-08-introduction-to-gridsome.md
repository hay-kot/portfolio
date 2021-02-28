---
title: Introduction to Gridsome
path: /introduction-to-gridsome
date: 2019-04-08
summary: Caddy is a simple, powerful, and extensible platform to serve your sites, services, and apps, written in Go. It's ability to split your SPA and API with a short and simple config makes it my favorite web-server for my projects. 
tags: ['frontend', 'coding', 'vue']
image: /caddy_v2.png
---

![background](/blog_bg_1.jpg)

As part of my on going development for Mealie, a self hosted recipe manager, I needed to split the static files from the API to simplify deployment and get some clunky code out of the FastAPI backend. Instead of using the traditional Nginx configuration I decided to use a newer web server Caddy to handle requests. Even though Caddy is a fairly simple and easy to use web server I found it difficult to quickly determine the correct way to use both a SPA and an API backend served on subpaths in the uri. This is my quick guide on getting a server up and running to server your SPA and the API on the same domain. 
Here's the final CaddyFile, we'll break it down below.

```
{
  auto_https off
}

:80 {
  @proxied path /api/* /docs /openapi.json

  root * /app/dist
  encode gzip
  uri strip_suffix /
  
  handle @proxied {
    reverse_proxy http://127.0.0.1:9000 
  }

  handle {
    try_files {path}.html {path} /
    file_server 
  }

}
```