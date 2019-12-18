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
The recovery process involved converting html to markdown back again and stitching it together with the old backup I had. The site was down for a while (shame on me, can't keep a static site running 100% of time). It was running an older version for sometime and then now it is fully updated.

The entire recovery process took me working on the terminal for a quite while with html->markdown converters and copy-paste.

But wait, recovery does not stop here. True recovery is recovering from the root cause of the problem.

The root cause of the problem is that master branch was not force-push protected. I usually do this, but this got missed somehow. (What to do. We humans, right?)

I changed in Github Settings to restrict force push for master.

## A flow
I like hexo. [You can learn why here](https://vishnubharathi.codes/blog/hugo-to-hexo/#Reasons). But in order to get instant flow of editing and publishing, I want an environment like Wordpress or Medium. Sophistication is setting high expectations all the time. So I want to keep using Hexo, but publish Medium or Wordpress style.

First I was thinking of writing a fresh blogging platform that will try to address this. But I can't draw lines on what I should be building. So I wanted to see if there is a way to publish content from something more accessible (like a markdown editor on the web). How about Github's markdown editor. I am pretty familiar with it and like it.

In the spirit of exploring Github Actions again, I started writing yaml configurations for it that will build and generate the hexo site. The whole disaster I was speaking about before gave me the idea that you could push some code easily from your github action.

Here is my YAML config.

```yml
name: Deployment

on:
  push:
    branches:
      - master

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v1
    - name: Hexo Generate
      env:
        GITHUB_CONTEXT: ${{ toJson(github) }}
      run: |
        ls
        git status
        git remote -v 
        npm install
        pushd themes
        git clone https://github.com/scriptnull/hexo-theme-cactus.git cactus
        popd
        ./package.sh
        git status
        git add docs/
        git add package-lock.json
        git config --global user.email "vishnubharathi04@gmail.com"
        git config --global user.name "Vishnu Bharathi"
        git commit -m "Generated site :sparkles:"
    - name: Push changes
      if: startsWith(github.event.head_commit.message, '[deploy]')
      uses: ad-m/github-push-action@master
      with:
        github_token: ${{ secrets.GH_PAGES_TOKEN }}
```

It is bunch of git commands + this github action `ad-m/github-push-action@master` which helps us to push changes with Github token, rather than a private key.

![image](https://user-images.githubusercontent.com/4211715/71079967-3f699200-21b2-11ea-90ce-59b7a1efaa17.png)

## Auto

There are more things behind the story, which would have been fun if I had blogged it like a live journal. But I didn't have that setup before. But now I have it.

All I have to do is, open up the github repository and commit the changes with the commit message starting with `[deploy]` and it will automatically deploy the site.

The next level of automation would be to deploy a staging environment for each pull requests and see a live version of the site before merging the PR. But for now, I am just happy with this setup.

Oh and Github gives this cool badge,

![](https://github.com/scriptnull/vishnubharathi.codes/workflows/Deployment/badge.svg)

