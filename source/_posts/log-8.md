---
title: log 8 = 0.9030
date: 2017-11-27 04:00:00
tags: ["blogging"]
---
This is my 8th weekly log.

### launchd + launchctl

I got the chance to learn about launchd and launchctl at [work](https://www.shippable.com/). They are responsible for loading and unloading daemons in macOS. If you need any of your programs to be run on background in macOS on startup, take a look at launchd and launchctl.

### Scaling Reddit
[**Scaling Reddit from 1 Million to 1 Billion-Pitfalls and Lessons**
*Summary Jeremy Edberg shares some of the lessons learned scaling Reddit, advising on pitfalls to avoid. Jeremy Edberg…*www.infoq.com](https://www.infoq.com/presentations/scaling-reddit)

One of the awesome points I noted in the talk is serving pre-rendered web pages from cache for logged out users. In that way, even if the site goes down, only the login users would notice. This technique could be used in sites which has more public users than logged in users (Example: Reddit had 80% as logged out users)

### tldr

<iframe src="https://medium.com/media/90c57da768755f74bd3b7cce8d47a0b6" frameborder=0></iframe>

### 2nd line

At work, I was trying to get the second line of the stdout. After searching a little, I came across this simple and elegant solution.

    MACOS_VERSION=$(sw_vers | head -2 | tail -1 | awk '{print $2}')

head -2 picks the first 2 lines and tail -1 picks the last one line in the first 2 lines.

### Moving fast

Days are moving really fast. I was thinking that it’s just Wednesday of the week, but surprisingly it was already Friday. I think, I just got busy with work and starting to forget days.

### Rainbow cake

<iframe src="https://medium.com/media/a0d3a0d85ba1137ec1282d4473b3e5a4" frameborder=0></iframe>

### 50+ days of logging

I just realised that I have been logging in medium for 50+ days. That is huge. I have been able to do something continuously for this much time. I am excited about where this is going.

I have been busy lately, but from analysing my logs, I could clearly arrive at the point that, “I am not spending much time for me and learning things”. I will try my best to change this situation. Because, the world is boring this way.

### Tickets

<iframe src="https://medium.com/media/6b17ff4265a94636f6235c7ff41141ed" frameborder=0></iframe>

### Scalable system design patterns

I read a crisp article about scalable system design patterns. It was good to know few new patterns, but still there is a long way to go. Because, I could not understand some patterns.
[**Scalable System Design Patterns**
*Looking back after 2.5 years since my previous post on scalable system design techniques, I've observed an emergence of…*horicky.blogspot.in](http://horicky.blogspot.in/2010/10/scalable-system-design-patterns.html)

The one below is very much detailed and a master piece!
[**The Architecture of Open Source Applications (Volume 2): Scalable Web Architecture and Distributed…**
*Open source software has become a fundamental building block for some of the biggest websites. And as those websites…*www.aosabook.org](http://www.aosabook.org/en/distsys.html)

And the following article introduced me to various types of [cache replacement policies](https://en.wikipedia.org/wiki/Cache_replacement_policies)
[**Introduction to Architecting Systems for Scale**
*Designing a system which scales to a high number of requests isn't critical for most applications, but you'll never…*lethain.com](https://lethain.com/introduction-to-architecting-systems-for-scale/)

I just watched [this talk](https://www.youtube.com/watch?v=srOgpXECblk), but could not understand it fully. Sometimes, I watch few things that I don’t understand. Because, they give us some model. Here and there, we will understand something and it will help us one day to learn some other thing. I learnt the following important lesson.

<iframe src="https://medium.com/media/f2065fbc716869021f60b7338c92b8fa" frameborder=0></iframe>

### Wishlist

1. Drink bubble gum shake

Thanks for reading. I quote verses from my favourite Tamil literature “[Tirukkuṛaḷ](https://en.wikipedia.org/wiki/Tirukku%E1%B9%9Ba%E1%B8%B7)” at the end of my blog posts.
> # “எண்ணிய எண்ணியாங்கு எய்துப எண்ணியார்
> # திண்ணிய ராகப் பெறின். ”
> # — திருக்குறள்

Translated meaning ( in my words ): Thoughts turn into action, when the thinker is strong enough to act.
