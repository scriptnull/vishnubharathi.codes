---
title: A Slice of Redis - Part 2
date: 2018-10-12 20:19:00
tags: ["redis", "software"]
---

Perfect timing. The cake just arrived. Actually, cakes :P (Read [Part 1](/blog/A-Slice-of-Redis-Part-1/) where I actually ordered them.)

I cloned the [redis](https://github.com/antirez/redis) repository and built it using the instructions in the [README.md](http://readme.md)

    # very simple

    $ git clone git@github.com:antirez/redis.git

    $ cd redis

    $ make

    $ make test

I am reading over [Redis Internals](https://github.com/antirez/redis#redis-internals) section in the README and easily got to learn this new stuff called [Redis Sentinel](https://redis.io/topics/sentinel).

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">if you are planning on doing some cool <a href="https://twitter.com/hashtag/redis?src=hash&amp;ref_src=twsrc%5Etfw">#redis</a> stuff, especially high availability - take a look at Redis Sentinel. <a href="https://t.co/PsJe24Vl61">https://t.co/PsJe24Vl61</a></p>&mdash; Vishnu Bharathi (@scriptnull) <a href="https://twitter.com/scriptnull/status/1050774780255731713?ref_src=twsrc%5Etfw">October 12, 2018</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

If we are planning on sending some pull requests to Redis, we need to open it against their `unstable` branch.

Also, I just discovered that, redis is written in C and it's unit tests are written in [Tcl](https://en.wikipedia.org/wiki/Tcl).

> Tcl (pronounced "tickle" or tee cee ell /ˈtiː siː ɛl/) is a high-level, general-purpose, interpreted, dynamic programming language

---

One thing worth saying it here is redis has a event loop! I kind of had a prediction about this before. Now I just had the chance to read the actual source of the event loop that powers redis.

Ok! That is it for now. Saving the good parts for later.
