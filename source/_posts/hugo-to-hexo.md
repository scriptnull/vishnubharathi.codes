---
title: Hugo to Hexo
date: 2018-09-30 19:09:10
tags: ["blogging", "software"]
---
I have been using [Hugo](https://gohugo.io/) to blog for quite sometime. I recently pulled an all nighter to migrate from [Hugo](https://gohugo.io/) to [Hexo](https://hexo.io/).

## Old Look
I was using [cocoa-hugo-theme](https://github.com/nishanths/cocoa-hugo-theme). I loved its simplicity. I also contributed few things to the theme itself.

1. [Pull request for showing tags](https://github.com/nishanths/cocoa-hugo-theme/pull/127)
1. [Feature request - Dark mode](https://github.com/nishanths/cocoa-hugo-theme/issues/129)
1. [Feature request - Telegram Icon](https://github.com/nishanths/cocoa-hugo-theme/issues/128)

![Hugo home page](/images/hugo-cocoa-home-page.png)
![hugo quotes page](/images/hugo-cocoa-quotes-page.png)
![Hugo books page](/images/hugo-cocoa-books-page.png)
![Hugo blog post](/images/hugo-cocoa-blog-post.png)
![Hugo code syntax](/images/hugo-cocoa-code-syntax-theme.png)

## New Look
One of the things that strongly convinced me to move to hexo was this theme called [cactus](https://github.com/probberechts/hexo-theme-cactus). It is perfect and it is everything that I am expecting it to be.

![hexo home page](/images/hexo-cactus-home-page.png)
![hexo quotes page](/images/hexo-cactus-quotes-page.png)
![hexo books page](/images/hexo-cactus-books-page.png)
![hexo blog post](/images/hexo-cactus-blog-post.png)
![hexo code syntax](/images/hexo-cactus-code-syntax-theme.png)

## Reasons

Here are my reasons for this migration.

1. I find hexo to be simple and good enough for my needs.
1. Themes - [cocoa](https://github.com/nishanths/cocoa-hugo-theme) VS [cactus](https://github.com/probberechts/hexo-theme-cactus) :: Winner is cactus and I was having hard time porting cactus to Hugo!
1. Hugo's documentation felt complex with terms like `archetypes`. On the other hand, Hexo's documentation was simple and to the point. Hugo might have few features which comes with the complexity in the documentation. But I am sure that, I wouldn't need them at this point of time.

## Lessons

An important lesson I learnt is to avoid using pictures with transparent background in blog posts. Because, some parts of the pictures might become invisible when migrating the site from light to dark theme. (Example: black lines drawn with a transparent background render correctly on a site with white background and seems invisible when it is used in a site with black background)

## Other options

I started evaluating various tools when I started this site.

### Hosted Platforms
- [Medium](https://medium.com/) :: I felt Medium is not a place for posting something very personal and small. Because there weren't much of an audience for my personal posts and the upvote system kind of made my posts look like spam.
- [Posthaven](https://posthaven.com/) :: not free $5 + I think it has problem with rendering code snippets. It is suited more for saying personal experiences.
- [Tumblr](https://www.tumblr.com/) :: More suited for sharing personal experiences.
- [Wordpress](https://wordpress.com) :: Not free.
- [Notion](notion.so) :: This is not a blogging platform, but I use it to keep my private journals. It fits that space perfectly and I checked if it is possible to host a public blog with notion. I asked around and seems like it is not possible yet, but the notion team added my vote on this feature request.

![notion feature request](/images/notion-blog-feature-request.png)

### Static site generators
- [Jekyll](https://jekyllrb.com/) :: I don't want to fiddle with ruby, gem, bundler etc. So, nope!
- [Hugo](https://gohugo.io/) :: I have to confess something here. I did Hype-driven development while choosing Hugo and it satisfied my needs perfectly at that point of time.
- [Gatsby](https://www.gatsbyjs.org) :: This is new and has cool features (https://www.gatsbyjs.org/features/), which I won't need as of now. So I will say pass for now.

---

This is a very interesting topic. I am always on a look out for new blogging tools and platforms.
