---
title: From Windows to M1
path: /the-best-laptop-ive-ever-used-from-windows-to-the-m1
date: 2021-02-12T06:08:42.000+00:00
summary: As a long time, diehard Windows fan it slightly pains me to say that the M1 MacBook Air is by far the greatest laptop I've ever used. I adamantly refused to buy into the MacOS ecosystem but after weeks of being undecided on a new laptop I finally caved and took the plunge into the MacBook Air.
reading_time: 
tags: ['frontend', 'coding', 'vue']
image: https://images.unsplash.com/photo-1537498425277-c283d32ef9db?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MXwxMTc3M3wwfDF8c2VhcmNofDF8fG1hY2Jvb2t8ZW58MHx8fA&ixlib=rb-1.2.1&q=80&w=2000
---

<br>

<test-component title="My Title ">

To my surprise, the experience of installing and updating applications felt very...linux-like? I was able to use [brew](https://brew.sh/) as a package manager with cask right out of the box, no rosetta nonsense. I opened terminal installed brew and away I went. The overall performance of applications was also a surprise.

</test-component>

----

As a long time, diehard Windows fan it slightly pains me to say that the M1 MacBook Air is by far the greatest laptop I've ever used. Over the past few weeks I've scoured the internet to find the perfect laptop for traveling and light development. I adamantly refused to buy into the MacOS ecosystem as I was raised by a diehard windows administrator. After weeks of being undecided I finally caved and took the plunge into the MacBook Air and boy oh boy was I wrong.

First Impressions
-----------------

Starting off, the boot up experience wasn't anything special. After fumbling a bit to get my icloud account setup I was a bit confused about having a local account and a icloud account and seemingly had to use both passwords at different times to authorize different items. I found my self using the wrong password multiple times. A small hurdle but a hurdle none the less. 

To my surprise, the experience of installing and updating applications felt very...linux-like? I was able to use [brew](https://brew.sh/) as a package manager with cask right out of the box, no rosetta nonsense. I opened terminal installed brew and away I went. The overall performance of applications was also a surprise.

As a "later adopter" of the M1 a lot of the major applications I use were already ported over to work natively on the M1 processor. Things like Word, Excel, and Powerpoint ran well and the performance of the *new* Outlook was excellent. Traditionally, I'm not a fan of using Outlook however the new Mac application has made some significant style changes that make Outlook feel so much more modern and accessible, something that was lacking in the outlook experience on Windows. 

A small tip, if you are interested in knowing what architecture your current application is running in there's a nifty app called [Silicone Info](https://apps.apple.com/us/app/silicon-info/id1542271266?mt=12) that adds a small icon to the top bar that you can check and see if it's Intel or Arm 

Basic Development Setup
-----------------------

Small Caveat: I am, by no means, a hardcore developer. My main use cases are web development with Javascript, Vue and Python so that may color my experiences with the M1. 

With any linux machine I have a few dot files with shortcuts and snippets that I like to include with a new install. The Mac being somewhat unix based, I pulled my dot files from GitHub and ran my setup script to see if it would run. Granted it's a small script that mostly just sets up zsh so I fully expected it to work and it did. I didn't need to change a single thing. 

Next thing I needed to do was actually get a project running. I installed VSCode with brew but wasn't super impressed with the performance of the intel version, not that it was bad, it just ran like it did on windows. Luckily the preview version support Apple Silicon! Setting up the preview version of VSCode was super simple, just download the zip file, extract it and you're off to the races. Running in preview was noticeably faster than the default install and well worth and bugs you may experience. I haven't had any problems using the preview version. Once VSCode was setup I pulled down my open source application [Mealie](https://github.com/hay-kot/mealie), ran npm install and poetry install , started the dev servers and was up and running in about 10 minutes without any clunk work arounds. 

Overall Impression
------------------

As a seasoned Windows user and someone who thought WSL2 would be the best developer environment in 2020, it's hard to admin but the M1 Macbook Air is easily the best computer I've ever used. Comparing it against my i9 gaming desktop with 48 gigs of ram, I still think I would rather develop on the M1. It just feels *that* much better of a machine. 

