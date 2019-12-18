---
title: Auto
date: 2019-12-18
tags: ["devops"]
---

Hi, it's me, blogging after a long time.

I was lazy to setup the local environment for updating anything on this site for all these days.

![lazy](https://media.giphy.com/media/f4SoNPj4otohG/giphy-downsized-large.gif)

Well, those days are gone. I just finished setting up a simple auto-deployment for this website.

So here will be my thoughts but more faster.

## A pain

The real pain for starting/editing blog posts is that I have to setup a local development environment. Bring up vagrant, install all prereqs and clone the source code and theme and ..... You get it, it needs work and needs a computer all the time, even just to do simple things like [adding a quote here](https://vishnubharathi.codes/quotes).

## A lesson learnt

I was wanting to give [Github Actions](https://github.com/features/actions) a try from when it was in beta. So I gave it a try during this process.

When I started looking at it, I came across it's marketplace and got very excited. Since I was using hexo blogging framework for the site, my natural intution was to [try any of these actions in the marketplace](https://github.com/marketplace?utf8=%E2%9C%93&type=actions&query=hexo). I went with [hexo-deploy-with-cname-enabled](https://github.com/marketplace/actions/hexo-deploy-with-cname-enabled).

That was a disastrous decision. After commiting the workflow yaml, the action ran and force pushed to master.

The action basically took all the source code and generated a hexo site (probably by running `hexo generate`) and force pushed to master.

I usually have the source files (markdown blog posts and other pages) in the root and have the generated hexo site in `/docs` folder. So, now all the markdown files are gone. Only the hexo generated html files are there. Boom! thankfully, it the data is still there, but just a different format.

At this point, I started searching for some local backup, which I didn't find at first. PANIC!

After a while, I found an old copy probably missing the last 3 blog posts I posted. LESS PANIC!

The hard lesson here is making a simple backup before being adventurous. Example, I could have been chill throughout this entire situation, if I had did a git clone before trying out the action or just used two mouse clicks to create a backup branch from Github.

> Always backup and ask the question if there is a backup somewhere

## A Recovery
The recovery process involved converting html to markdown back again and stitching it together with the old backup I had. 
