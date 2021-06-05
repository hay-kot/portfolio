---
# When Publish is set to true the article will be processed
publish: false
title: Working with Home Assistant and Mealie
summary: Get to know the Mealie API and learn how it can be used to integrate with/into Home Assistant to take full advantage of the restful API
tags: ['coding', 'automation', 'python']
# Urls will be downloaded and inserted into the static folder
image: ""
---

<call-out-box warning>

This blog post covers the BETA release of Mealie (v0.5.0). Some things may change after the official stable release has been posted.

</call-out-box>

To get started we'll assume that you've pulled down and deployed Mealie and already have a few recipes to work with. If you haven't you can review the documentation [here](https://hay-kot.github.io/mealie/) on how to get started. 

## Getting an API Token
First thing first, you'll need to get an API token. After you login, you can navigate to the profile/admin page at `/admin`. Scroll down until you see the API card and click the "Create" button. A dialog will appear, name the token something relevant to what will be consuming the API, in this case I'll name it 'Home Assistant.' Once it's been named hit the "Create" button in the dialog and you should see an API key appear. Highlight the API text and copy or hit the copy button and save this key somewhere, you won't be able to see it again. 

<call-out-box tip>

if you're not sure what API points are available visit `/docs` on your installed version or checkout the [demo site](https://mealie-demo.hay-kot.dev/docs) to see everything you have access to! 

</call-out-box>

