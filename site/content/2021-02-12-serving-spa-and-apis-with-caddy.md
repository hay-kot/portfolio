---
title: Serving SPAs and API With Caddy v2
path: /serving-spa-and-apis-with-caddy
date: 2021-02-13T03:27:05.000+00:00
summary: Caddy is a simple, powerful, and extensible platform to serve your sites, services, and apps, written in Go. It's ability to split your SPA and API with a short and simple config makes it my favorite web-server for my projects. 
reading_time: 
tags: ['coding', 'vue', 'python']
image: /serving-spa-and-apis-with-caddy.png
---

As part of my on going development for [Mealie](https://github.com/hay-kot/mealie), a self hosted recipe manager, I needed to split the static files from the API to simplify deployment and get some clunky code out of the FastAPI backend. Instead of using the traditional Nginx configuration I decided to use a newer web server Caddy to handle requests. Even though Caddy is a fairly simple and easy to use web server I found it difficult to quickly determine the correct way to use both a SPA and an API backend served on subpaths in the uri. This is my quick guide on getting a server up and running to server your SPA and the API on the same domain. 

Here's the final CaddyFile, we'll break it down below.

```
{
 auto_https off
}

:80 {
 @proxied path /api/* /docs /openapi.json

 root * /app/dist
 encode gzip
 uri strip\_suffix /
 
 handle @proxied {
 reverse\_proxy http://127.0.0.1:9000 
 }

 handle {
 try\_files {path}.html {path} /
 file\_server 
 }

}
```

The first part is the main configuration where you can use several options to customize the overall behavior of Caddy. In this case I did not need encryption via https as this is designed to sit behind another instance of a proxy server. Including auto_https off will disable the automatic https through lets encrypt. `:80` refers to the port that Caddy will listen on, everything included in the `{}` will be associated with port 80. `@proxied` is a short-hand in Caddy to use a snippet somewhere else in the file. In this case we'll define our API routes here and pass them to a handler later in the file. Since I'm using FastAPI I needed to add a few additional routes besides /api/*. 

Next we have the encode gzip and uri strip_suffix these are little helpers that enable gzip and strip trailing on urls. This was extremely helpful as defining routes in FastAPI as I did not need to account for two paths, the proxy server will always strip the trailing. 

To deal with the API we're going to use the handle directive and pass the @proxied snippet as that matcher to pick up all our api routes. Then we're going to use the [reverse\_proxy](https://caddyserver.com/docs/caddyfile/directives/reverse_proxy) directive and pass it our API server. In this case I'm using a local server on port 9000

```
 handle @proxied {
 reverse\_proxy http://127.0.0.1:9000 
 }
 ```
 
 Finally we need to mount the static files. We'll again reuse the handle directive but this time we won't include a matcher and instead handle all requests that were not previously handled. The [try_files](https://caddyserver.com/docs/caddyfile/directives/try_files) directive is then used to match the requests against a file, if the request does not match any static files, rewrite to your index.html. Lastly you add the [file_server](https://caddyserver.com/docs/caddyfile/directives/file_server) directive to tell Caddy to server up static files

```
 handle {
 try\_files {path}.html {path} /
 file\_server 
 }
 ```