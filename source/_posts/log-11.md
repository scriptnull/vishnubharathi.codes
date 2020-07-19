---
title: log 11 = 1.0413
date: 2017-12-17 04:00:00
tags: ["blogging"]
---

This weekly log is a bit different. Because, I am writing the entire post in the last day of the week. Usually, I write down my logs throughout the week and launch it. But, this time I was very busy with a lot of stuff.

### At work

I have been spending a lot of time [at work](https://www.shippable.com/) lately. Good thing is, some of the things are open sourced and I could should show you what I was working on.

[This page](https://www.shippable.com/circleci-compare.html) got to my notice few days back. In particular the terms Q4 2017 for iOS builds and Windows Containers. I think, it means the feature is estimated around 4th quarter of 2017. Well, that’s right. Efforts have been going for it to happen and that too in the open.

This week, I got to work on enabling Shippable builds on Windows
[**Task executes a minimal dir command by scriptnull · Pull Request #131 · Shippable/execTemplates**
*Contribute to execTemplates development by creating an account on GitHub.*github.com](https://github.com/Shippable/execTemplates/pull/131)

I got to learn about PowerShell a bit. I am super amazed by the work that has been went into designing and developing PowerShell. Go check it out!
[**PowerShell/PowerShell**
*PowerShell for every system!*github.com](https://github.com/PowerShell/PowerShell)

### Coolest thing in PowerShell

Most of the time, I felt like I was on bash when using PowerShell. But there is this one functionality which I feel is very powerful.

PowerShell allows us to access the .NET Framework inside a PowerShell script.

I wanted to generate a UUID in [our PowerShell script](https://github.com/Shippable/execTemplates/pull/131/files#diff-83adc9a02f6213321116b3d9729ff8fbR6).

First, How do we do it in bash?

bash does not have access to some thing like a .NET framework in its scripts. So, as a work around we are expected to rely on a program that bash can access to get a uuid from stdout and use it.

That’s what we do exactly [here](https://github.com/Shippable/execTemplates/blob/master/Ubuntu_16.04/job/header.sh#L89). There is this file in the proc fs, ( /proc/sys/kernel/random/uuid ) giving us a uuid everytime we read it. ( I am curious to know why it exists in first place )

    group_uuid=$(cat /proc/sys/kernel/random/uuid)

Now, in PowerShell instead of calling an external program, all we need to do is to access [the Guid class in .NET Framework](https://msdn.microsoft.com/en-us/library/system.guid.newguid(v=vs.110).aspx).

    $group_uuid = [guid]::NewGuid().Guid

### Learning about Linux

I have been tweeting most of the interesting things that I learnt throughout the week.

<iframe src="https://medium.com/media/92ae93c041e2c11b45f608b3e2c4a622" frameborder=0></iframe>

<iframe src="https://medium.com/media/d16003a65a68b943f3ee00fd4bf82918" frameborder=0></iframe>

<iframe src="https://medium.com/media/fdeb9e5864193573659b6a67f64c8456" frameborder=0></iframe>

<iframe src="https://medium.com/media/afe93ad58880fd20ac2752a29ce0c1a6" frameborder=0></iframe>

<iframe src="https://medium.com/media/d8646c566f8a39081ce0f045d8aa10cd" frameborder=0></iframe>

<iframe src="https://medium.com/media/2aed0692bfe244631d62ad10b5d7cb44" frameborder=0></iframe>

<iframe src="https://medium.com/media/d72ac9687a29b60db356904023560b9e" frameborder=0></iframe>

<iframe src="https://medium.com/media/58643e190c4abed39b6d16945f4fbbb2" frameborder=0></iframe>

<iframe src="https://medium.com/media/593088cbe7ad93026d8586f705169a3c" frameborder=0></iframe>

<iframe src="https://medium.com/media/75e53284cc4050b8cf800c8de5782a10" frameborder=0></iframe>

<iframe src="https://medium.com/media/56ff8124a63d8ddcc545f50008f5bca2" frameborder=0></iframe>

Thanks for reading. I quote verses from my favourite Tamil literature “[Tirukkuṛaḷ](https://en.wikipedia.org/wiki/Tirukku%E1%B9%9Ba%E1%B8%B7)” at the end of my blog posts.
> # “கேடில் விழுச்செல்வம் கல்வி யொருவற்கு
> # மாடல்ல மற்றை யவை.”
> # — திருக்குறள்

Translated meaning ( in my words ): Education is the only wealth of a man that could not be destroyed. Any other wealth is not considered to be a wealth in front of a man’s knowledge through education.
