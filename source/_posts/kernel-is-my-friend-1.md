---
title: Kernel is my friend — Part 1
date: 2018-03-01 04:00:00
tags: ["linux", "kernel", "software"]
---

Kernel is my friend — Part 1

### Fun with file descriptors

At the start of 2018, I wished to learn in general about [Linux](https://hackernoon.com/tagged/linux) and Systems [Programming](https://hackernoon.com/tagged/programming). That means, being friends with the Kernel! So, I started reading [The Linux Programming Interface](http://man7.org/tlpi/). This is the first part of the series of blog posts that I will be writing as I go through the book and unravel the mysteries of Linux.

This post is an attempt to understand some parts of the lesson “[File I/O: The Universal I/O Model](http://man7.org/tlpi/)” from [The Linux Programming Interface](http://man7.org/tlpi/).

### Types of files

I have heard of the statement that “everything in Linux is a file”. But, I got learn that there are different types of files in Linux.

<iframe src="https://medium.com/media/68f351b92069cf24265a45886692e11c" frameborder=0></iframe>

### System calls

System call is a way of asking the kernel to do some work for us. For example, these are the four basic system calls that help to work with files in Linux

* open — Hey kernel, could you open a file for me? So that the process could do something with it.

* read — Hey kernel, could you read this amazing piece of code that I saved in ~/cool/stuff/is/here.js ?

* write — Hey kernel, could you help me write my really long homework to this file?

* close — Hey kernel, I am done with my homework, please close the file. We will go hangout and do some other fun stuff.

### File Descriptors

File descriptor is a non-negative integer number that is used to reference a file.

When open() system call is being called by a process, a file descriptor is being returned from it, which could be used in other system calls like read, write, close.

One of the interesting thing that I missed out to observe closely when I read the lesson for the first time is (This is probably an important key take away)
> # Each process has its own set of file descriptors

Lets try to understand this in a step by step manner.

### One process, one file

Lets write a program that just opens a file and print its file descriptor value.

<iframe src="https://medium.com/media/733c0fc4f97ca12d53a8ee233b9112bb" frameborder=0></iframe>

I created a binary and executed it to read one file at a time. So, this is basically reading one file from one process at a time.

![The file always gets the file descriptor value of 3 always](https://cdn-images-1.medium.com/max/2084/1*7oWSG_RvSyUf003g_j4Nmw.png)*The file always gets the file descriptor value of 3 always*

### One process, multiple files

Now, lets try opening multiple files from one process at a time

<iframe src="https://medium.com/media/76da565e8ea3b5a2d75c61592e991e69" frameborder=0></iframe>

![files got allocated with sequential integer values](https://cdn-images-1.medium.com/max/2592/1*FEfd7Tu_MuJgCyqC_2Gv1g.png)*files got allocated with sequential integer values*

The way the files get the file descriptor number is based on this simple idea
> SUSv3 specifies that if open() succeeds, it is guaranteed to use the lowest-numbered unused file descriptor for the process.
> — Kerrisk, Michael. The Linux Programming Interface: A Linux and UNIX System Programming Handbook (p. 73). No Starch Press. Kindle Edition.

### Multiple processes, multiple files

This is the interesting part. What happens if same files are accessed by multiple processes at the same time. How is the file descriptor allocated then?

<iframe src="https://medium.com/media/916cbce74ea4b92e8b14aa4ee40cd2db" frameborder=0></iframe>

![Numbering is done at a process level](https://cdn-images-1.medium.com/max/2456/1*ba3qUr1QOBHMMJ5U69w9DQ.png)*Numbering is done at a process level*

This proves the statement that we started with,
> # Each process has its own set of file descriptors

Process 9012 opened 1.js assigning fd 3 and 2.js assigning fd 4. Process 9015 is no different, it did the same thing. Because those are the lowest numbered unused file descriptor value within those processes.

Now that we have come this long way, the interesting question in my mind is what will happen if two processes try to write to the opened files at the same time. (I guess, this is probably worth answering another time!)

### Standard File Descriptors

I have already heard of these names and to my surprise, they are just file descriptors.

<iframe src="https://medium.com/media/6205e5ec2f35cd59ea18a146d39ba522" frameborder=0></iframe>

When a process is created, it seems like it automatically opens the stdin, stdout and stderr files and allocate the fd numbers 0,1,2 respectively.

I went a step further and tried to see where these files are present. But I ended up with something that I don’t know yet. (Amazing! We have something to dwell about)

![character special? ¯\_(ツ)_/¯](https://cdn-images-1.medium.com/max/2184/1*DVuquAhjz3W3AtwMTQF0dg.png)*character special? ¯\_(ツ)_/¯*

### Mysteries

* What will happen if two processes try to read from an open file at the same time?

* What will happen if two processes try to write to an open file at the same time?

* What is /dev/pts/0?

* What is file type “character special” ?

(Please do comment, if you got the chance to solve these)

Thanks for reading. I quote verses from my favourite Tamil literature “[Tirukkuṛaḷ](https://en.wikipedia.org/wiki/Tirukku%E1%B9%9Ba%E1%B8%B7)” at the end of my blog posts.
> # செய்தக்க அல்ல செயக்கெடும் செய்தக்க
> # செய்யாமை யானும் கெடும்.
> # *— திருக்குறள்*

Translated meaning ( in my words ): Things go wrong for people who do the things that are not supposed to be done by them and also for the people who do not do what they are supposed to do.

<iframe src="https://medium.com/media/3c851dac986ab6dbb2d1aaa91205a8eb" frameborder=0></iframe>
