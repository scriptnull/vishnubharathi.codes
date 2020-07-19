---
title: log 4 = 0.6020
date: 2017-10-30 04:00:00
tags: ["blogging"]
---

![steps](/images/steps.png)

hurray! I went out every morning and jogged/walked in the park.

I spent lot of time on relaxation last week. This week, I am positive that I could be more productive and I am planning to achieve one of the hardest goal for me “Do physical exercise everyday”

Lets start.

### Time and Task management

I have been experimenting a lot on managing time and getting stuff done. I want to take control of it. So badly.

One of the craziest things I did this year is, I managed my time and task by using a bug tracking board on Source Control Management platform called [Gitlab](https://gitlab.com/). I got this idea from work. I was able to do it for a month. But, eventually got bored, as I do the same thing at work for managing tasks.

So, I moved to [Trello](https://trello.com/) few months back. It’s actually good and I am using it in very minimal manner ( I open it once a day, to note down important backlogs ). However, I am still experimenting with it ( for months ).

This week, I am going to use a new setup of my Trello board and important principle to take control of my time back. The important principle is “Knowing what is right and doing it”

### Trees

I started to explore various kinds of trees and how they could be useful. Till now, I have come across the below tree types

* Binary tree

* Binary search tree

* 2–3 tree

* 2–3–4 tree or 2–4 tree

* AA tree

* Red Black tree

* Threaded Binary tree

Even though I did not spend more time in learning them in detail. I just grasped the basic ideas behind them.

### Tagged union and trees

I came across tagged unions long back. Interestingly, I just realised that it could be used to implement some complex tree structures in a very simple way. For example:

<iframe src="https://medium.com/media/03b3f7f0db2fbe576bff5fc0d76e00af" frameborder=0></iframe>

Child of a node could be expressed as a tagged union of nil or node containing two children or node containing three children

    @left : Nil | TwoNode(T) | ThreeNode(T)

### Power in my hands

<iframe src="https://medium.com/media/f6a0713c4faf9678d9aebc2304c1a1ad" frameborder=0></iframe>

### Query Plan Analysis

I saw this interesting tweet and boom! I happen to discover an interesting query in Postgres, that helps us to analyse other queries.

<iframe src="https://medium.com/media/c96d06dcf9aafb9017938e341c28c6c0" frameborder=0></iframe>

<iframe src="https://medium.com/media/b2c052264d82e3d4afa79fa51a5f3b4d" frameborder=0></iframe>

There is this query called [EXPLAIN](https://www.postgresql.org/docs/9.1/static/sql-explain.html) in postgres, which will helps in analysing the SQL query we write.

![Example query from [https://www.postgresql.org/docs/9.1/static/sql-explain.html](https://www.postgresql.org/docs/9.1/static/sql-explain.html)](https://cdn-images-1.medium.com/max/2000/1*1zp3qkEXaI82TOYDs7TALQ.png)*Example query from [https://www.postgresql.org/docs/9.1/static/sql-explain.html](https://www.postgresql.org/docs/9.1/static/sql-explain.html)*

### Rush

I don’t like doing things in a rush. I originally intended to write something about doing things in a rush and its after effects. But it’s a subject that needs to be written not in a rush. So, will try to note down some ideas about this topic in future, if I feel like to.

But for now, avoid doing things in a rush with an obscure plan.

### Suicide Linux

I tried out this fun project in a docker container. It’s fun and give it a try.
[**Suicide Linux @ Things Of Interest**
*As another, slightly more serious suggestion, if Suicide Linux randomly deleted a single file without telling you every…*qntm.org](https://qntm.org/suicide)

### Blog post on Trees

I am writing a blog post on some interesting things i happen to discover about the tree data structure and I have named this blog post as “Trees are green”. By far, it’s going pretty good. I hope to get it out soon.

### microplan

Back in the November of last year, I and my friends ( [Venkat](https://github.com/argonlaser) and [Vasanth](https://twitter.com/11cs103) ) started working on this project called microplan. It is a very simple command line tool for planning projects via issue trackers.
[**microplan-xyz/microplan**
*microplan - Plan your project from command line*github.com](https://github.com/microplan-xyz/microplan)

I happen to work on it a bit, this week. I use this tool a lot at work. We are very much excited to go for a 2.0.0 release of this tool.
[**Adhere to oss-checklist for proper major release · Issue #78 · microplan-xyz/microplan**
*OSS Project Checklist A copy of the below checklist could be obtained from oss-checklist (Help us make it better!) Pre…*github.com](https://github.com/microplan-xyz/microplan/issues/78)

### TODO for medium blogs

I happen to discover this super cool feature from medium this week. I always wanted the ability to have TODO markers in blog posts. It seems like it already exists in medium

<iframe src="https://medium.com/media/43bd7d7cdc7c8a487b48237f1490cb4d" frameborder=0></iframe>

### Goals

* [DONE 6/6] Go out and jog/walk early morning ( 6 days streak )

* [DONE 5/6] Learn one new data structure everyday ( 6 days streak )

### Overall

Overall this was a productive week for me. I hope to maintain the spirit over the next week too. However, I will be travelling in next week and might be a bit hard to maintain some things.

Thanks for reading. I quote verses from my favourite Tamil literature “[Tirukkuṛaḷ](https://en.wikipedia.org/wiki/Tirukku%E1%B9%9Ba%E1%B8%B7)” at the end of my blog posts.
> # “கேடில் விழுச்செல்வம் கல்வி யொருவற்கு
> # மாடல்ல மற்றை யவை.”
> # *— திருக்குறள்*

Translated meaning ( in my words ): Education is the only wealth of a man that could not be destroyed. Any other wealth is not considered to be a wealth in front of a man’s knowledge through education.
