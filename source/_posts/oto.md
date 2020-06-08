---
title: On top of
date: 2020-06-09 01:41:00
tags: ["ideas", "software", "want-to-build"]
---

This is a rough draft of thoughts on a tool that I would like to build. It is a simple command line tool named `oto`. It stands for `on top of`. I often hear and reaffirm to myself that

> We are built __on top of__ the giants.

By saying "giants", we mean anything that adds huge value! Try to hold your thoughts with respect to the business world where giants mean "Big corps". Think of this word in the context of open source / software developement in general. It means any project that adds massive value to your project.

Want a web-server? `npm install --save express`

Want a cache? `docker run redis`

You just stood on top of all these giants: npm, express, docker, redis

Want any piece of software? you download it, add it to your project and just forget about it! Just think of all those projects that help you with your project.

Don't you think we often take things for granted?

How about we give a little credits to them.

[There is a value in open source](https://www.youtube.com/watch?v=AdVQdXS6ooQ) or any kind of software. The least we can do is to give credits to them.

That's what `oto` is going to help you with!

## all-contributors

There is this awesome project called [all-contributors](https://github.com/all-contributors/all-contributors) that comes very close to the motives of this tool.

It helps in recognising and giving credits to all the contributors of a project. It does it by generating a table of contributors and adding it to the README of the project. Like this :point_down:

![all-contributors](https://raw.githubusercontent.com/all-contributors/all-contributors/master/docs/assets/contributors-table-small.png)

_Picture Credits: https://github.com/all-contributors/all-contributors/blob/master/README.md_

## backers & sponsors

Next thing where I find this kind of culture is with giving credits to backers and sponsors in a project. 

![backers](https://camo.githubusercontent.com/d1cc35572ae57f015e917614d0bf4661aa7d49d8/68747470733a2f2f636c2e6c792f33673256334d3230305532642f53637265656e25323053686f74253230323031362d30372d31382532306174253230342e33342e3438253230504d2e706e67)

_Picture Credits: https://github.com/opencollective/opencollective/wiki/Show-Backers-and-Sponsors_

## openring

There is this amazing project called [openring](https://git.sr.ht/~sircmpwn/openring). What this does is create a [webring](https://en.wikipedia.org/wiki/Webring) that could be embedded in blogs. It is kind of giving credits to other people on the idea with nice / related blog posts.

![openring](https://l.sr.ht/TRrJ.png)

_Picture Credits: https://git.sr.ht/~sircmpwn/openring_

## Meet oto

`oto` builds on the core of all the above tools: Giving credits!

I searched through the internet and discovered that there is no tool to give credits for the technologies, tools, libraries, frameworks etc. used within our project. `oto` aims to address that!

(Also if you happen to find a project that already does this, please drop me a [message](mailto:vishnubharathi04@gmail.com) / [tweet](https://twitter.com/scriptnull)

It is a really simple tool. It is aimed to do the following.

- Analyse source code of project and generate an embeddable credits with logos of technologies, tools, libraries, frameworks etc.
- Compatible for markdown, HTML and plain text. So that credits could be embedded anywhere.

## Contributors
By generating credits to the things used inside a project, we essentially put up a banner to the future contributors of the OSS project.

It gives a person an idea about what they might be learning by contributing to the project upfront!

I suspect that `oto` will encourage new-contributors to the project and also gives a nice space for people who are skimming/researching the project.

## Inside companies
lol, I don't know why I am including this passage here, but hear me out.

Whenever I joined a new company, I usually like to get an idea of all the technologies they are using. Then I start digging in the code at multiple repositories to figure out the things. Another way is talking to different people inside the org about it.

In this case `oto` could be run in the private code bases. This will help understanding what is being done in the code-base faster. 

You might tell, "oh! just read the package.json and be done with it".

I wish! What if I am a person that doesn't even know what `package.json` is? In this case having a bunch of logos in README will more likely trigger a person to gather knowledge about the dependencies of the project.

So, clear communication of what are being used and faster understanding by engineers who are on-boarding the company.

This might just be the first step to having some kind of docs on their technical architecture. Most likely helpful in startups where they don't have time to document their architecture and how things are being used.

## Basic Features
Enough of story, let me try to write out the basic feature set of `oto`

### Programming languages
Most of the programming languages have a logo these days. So it would be good to analyse the source tree for files with respective file extensions and create thumnails of all the programming languages used in the project.

### Configuration files and directories
Most of the projects have configuration files checked into the source tree. For example: a ruby project might have `.rubocop.yml` file which means that it is using the [Rubocop static analyser and formatter for ruby](https://github.com/rubocop-hq/rubocop). So, we add it's logo/name to the output generated by `oto`.

Another low hanging fruit. Check if `.git` folder exists and add the git logo to the output. :)

Also, people tend to give templates for configuration files: If the project is using redis, there might be a `example.redis.conf` or `redis.conf` or redis.template.conf` etc. file that denotes the redis config. So, `oto` needs to understand this and add the logo of redis to the output.

### Package managers
Files used for package management like `package.json`, `Gemfile` etc. needs to be understood and the logos of packages by the project could be rendered in the output.

### Manual gear
So far everything was automatic. But the user should be able to manually pass the name of some tools to `oto`, so that those get added automatically.

## Sign off
I think this is a pretty decent document on the rational behind `oto`. This obviously helped me to normalize my thoughts around it (probably made it one step closer to building this tool).

I hope `oto` gets built with the help of all the amazing technologies in computing at present.

After all, __we are built on top of the giants__!
