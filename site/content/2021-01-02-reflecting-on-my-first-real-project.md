---
title: Mealie - Reflecting on my First "Real" Project
path: /reflecting-on-my-first-real-project
date: 2021-01-02T23:25:31.000+00:00
summary: This is short blog post on my first "real" programming project, and what I learned through the process.
reading_time: 
tags: ['coding', 'frontend', 'vue']
image: /reflecting-on-my-first-real-project.webp
---

The Project
-----------


When beginning a coding project, even just to learn, it's important to me to make something I find useful. It also matters, almost more so, for me to make things that others might find useful. If you take a look at the self hosted space there aren't many options in the Recipe Management realm. Specifically, I couldn't find anything that had an API which I could integrate into Home Assistant. To me, that was a perfect place to start for my first "real" project that would eventually be put out into the world for others.


With that in mind, I considered what a good recipe website would need:


* Automatic Web Scrapping / Import from URL
* UI Recipe Editor
* Custom Tags / Categories
* Adding Custom Notes
* Meal Planner with Randomized Meal Planning
* Backup Data with Easy Import/Export
* Restful API

With a baseline of what I wanted to create, I could actually get into the code. Because my primary language is Python, I decided to go with a FastAPI backend. This made it easy to create an API driven application that can be interacted with from many different places. For the frontend, I chose Vue. I'm fairly new to the world of Javascript, so this was the first framework I looked at which made sense to me. I liked that the framework made it easy to do the simple stuff, but it offered a rubust set of tools to do the more complicated stuff. I am looking forward to using it on a few more projects.


Lessons Learned
---------------


### WSL2 on Windows is a Pleasure


Being a long-time Windows user, I used to code directly in Windows with VSCode. This worked well most of the time. However, for this project I made the switch to using WSL2 on Windows for development and it was great for almost the entire project. I never ran into any issues getting setup, and docker worked straight out of the box. I previously used Docker on Windows, and it was a nightmare, but Microsoft made huge strides in improving the experience and making it feel like its running natively on Linux. The VSCode integration is also top-notch. If you're developing on Windows, I highly recommend moving your environment over to [WSL2](https://docs.microsoft.com/en-us/windows/wsl/install-win10).


### Docker is Awesome


The most useful experience I had in this project was working with Docker in development. For the first half of the project, I worked primarily with a terminal window having to constantly restart the app after it crashed, even with the auto reload. When I ran it through Docker, the web server would continue to restart no matter what. This was probably a small timer saver overall, but the convenience factor was huge. On top of that, [VSCode Tasks](https://code.visualstudio.com/docs/editor/tasks) made building for production and development as simple as a few keyboard shortcuts.


### Use VSCode Tasks!


Another important lesson I learned was the importance of automating my work-flow. Nobody wants to type the same commands into terminal every time they need to test their build, and I'm a sucker for automation. That's where [VSCode Tasks](https://code.visualstudio.com/docs/editor/tasks) came in. All I did was write a script for what I wanted to do and added it to the vscode task.json. The example below shows the two scripts I'm using to execute my docker-compose.dev.sh and my docker-compose.sh for both development and production stacks.

```json
# ./.vscode/tasks.json
{
 "version": "2.0.0",
 "tasks": [
 {
 "label": "DEV: Build and Start Docker Compose",
 "command": "./dev/scripts/docker-compose.dev.sh",
 "type": "shell",
 "args": [],
 "problemMatcher": ["$tsc"],
 "presentation": {
 "reveal": "always"
 },
 "group": "test"
 },
 {
 "label": "Production: Build and Start Docker Compose",
 "command": "./dev/scripts/docker-compose.sh",
 "type": "shell",
 "args": [],
 "problemMatcher": ["$tsc"],
 "presentation": {
 "reveal": "always"
 },
 "group": "test"
 }
 ]
}
```

I learned to use the command palette to access my tasks with ctrl + shift + p and type tasks to bring up a list of options. I made sure to commit my .vscode file to have those available in the repository.


### Use MKdocs Material Theme for Documentation


In the middle of the project, I was excited to discover Mkdocs, a framework/static site generator geared towards documentation. While it's default theme is not appealing to me, using the [Material Theme](https://squidfunk.github.io/mkdocs-material/), I discovered I could generate beautiful documentation with little to no effort. Most settings can be configured in yaml, users are able to add custom js/cs as needed, and it uses plain old markdown to generate the site in a way that makes sense. It also has single line gh-pages deployment. It's as easy as mkdocs gh-deploy and now any site has live documentation hosted for free on github. It feels like magic and was worth the 10 minute setup.


### A Crash Course in "Do it Right the First Time"



> 
> "Let me just write this little thing here, oh I'll just copy and paste, no big deal"
> 


But it was a big deal. As I went through the project, there were many times I had to stop and refactor code I had just written. I had either written sloppy code, or doubled up on things in too many places. One particular example was with unpacking documents from MongoDB. In nearly every class I had a step to unpack the document and turn it into a class object that I repeated slightly differently in each function. Instead of including that step in every function that retrieves from the database, I abstracted it into it's own function. After the creating the new function, I had go back and refactor how nearly all other functions worked. If I had started with a better idea on how to work with my data, I may have been able to see this coming before writing a bunch of code.


Final Thoughts
--------------


My biggest take away from making Mealie is to take more time to map out how data flows in the application. With a data driven application, even something as minor as JSON, I'm somewhat at the mercy of the data. In some instances one structurs their code to deal with data in a way that makes life easy for both the frontend and the backend. Sometimes, it only works for the backend. Before I create a class that represents data, I'm going to really take some time to map out how I want that data to be structured for both my frontend development and my backend.


Finally, after [publishing the project in a reddit thread](https://www.reddit.com/r/selfhosted/comments/kp3qih/mealie_a_self_hosted_recipe_manager_alpha_release/) I was overwhelmed with the support, kind words, and even the financial support from one very giving Redditor. It's hard to explain how good it feels to get so much positive feedback on something I spent close to a hundred hours on. The self-hosted community has provided me with a lot of support, projects, and time wasting endeavors. I can only hope that from the Alpha release of Mealie, it can be built into something that is supported by the community. It feels really good to be able to give something back.


