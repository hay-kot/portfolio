---
title: Serving a Single Page Application and API With Caddy v2
path: /serving-spa-and-apis-with-caddy
date: 2021-02-13T03:27:05.000+00:00
summary: Caddy is a simple, powerful, and extensible platform to serve your sites, services, and apps, written in Go. It's ability to split your SPA and API with a short and simple config makes it my favorite web-server for my projects. 
reading_time: 
tags: ['frontend', 'coding', 'vue']
image: https://blog.hay-kot.dev/content/images/2021/02/Caddy-Document-2.png
---

<p>As part of my on going development for <a href="https://github.com/hay-kot/mealie">Mealie</a>, a self hosted recipe manager, I needed to split the static files from the API to simplify deployment and get some clunky code out of the FastAPI backend. Instead of using the traditional Nginx configuration I decided to use a newer web server Caddy to handle requests. Even though Caddy is a fairly simple and easy to use web server I found it difficult to quickly determine the correct way to use both a SPA and an API backend served on subpaths in the uri. This is my quick guide on getting a server up and running to server your SPA and the API on the same domain. </p><p>Here's the final CaddyFile, we'll break it down below.</p><pre><code class="language-CaddyFile">{
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

}</code></pre><p>The first part is the main configuration where you can use several options to customize the overall behavior of Caddy. In this case I did not need encryption via https as this is designed to sit behind another instance of a proxy server. Including <code>auto_https off</code> will disable the automatic https through lets encrypt. </p><pre><code>{
  auto_https off
}</code></pre><p><code>:80</code> refers to the port that Caddy will listen on, everything included in the <code>{}</code> will be associated with port 80. <code>@proxied</code> is a short-hand in Caddy to use a snippet somewhere else in the file. In this case we'll define our API routes here and pass them to a handler later in the file. Since I'm using FastAPI I needed to add a few additional routes besides <code>/api/*</code>. </p><p>Next we have the <code>encode gzip</code> and <code>uri strip_suffix /</code>  these are little helpers that enable gzip and strip trailing <code>/</code> on urls. This was extremely helpful as defining routes in FastAPI as I did not need to account for two paths, the proxy server will always strip the trailing <code>/</code>. </p><p>To deal with the API we're going to use the <code>handle</code> directive and pass the <code>@proxied</code> snippet as that matcher to pick up all our api routes. Then we're going to use the <code><a href="https://caddyserver.com/docs/caddyfile/directives/reverse_proxy">reverse_proxy</a></code> directive and pass it our API server. In this case I'm using a local server on port 9000</p><pre><code>  handle @proxied {
    reverse_proxy http://127.0.0.1:9000 
  }</code></pre><p>Finally we need to mount the static files. We'll again reuse the handle directive but this time we won't include a matcher and instead handle all requests that were not previously handled. The <a href="https://caddyserver.com/docs/caddyfile/directives/try_files"><code>try_files</code></a> directive is then used to match the requests against a file, if the request does not match any static files, rewrite to your index.html. Lastly you add the <a href="https://caddyserver.com/docs/caddyfile/directives/file_server"><code>file_server</code></a> directive to tell Caddy to server up static files</p><pre><code>  handle {
    try_files {path}.html {path} /
    file_server 
  }</code></pre>