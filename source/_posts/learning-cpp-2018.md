---
title: I learnt C++ in 2018 and have no regrets
date: 2019-01-04 02:08:00
tags: ["programming", "c++"]
---

My quest for relearning C++ started in November 2018. I have been reading + [blogging](https://vishnubharathi.codes/tags/c/) + writing C++ from then. I would like to reflect on my journey a bit.

Before I begin, I would like to state that this is not a language war blog post (although few parts of it might sound like). My intention and emphasis is on how all these beautiful languages converge and diverge to give healthy competition and chance for evolution.

## Background

I have been writing JavaScript code on Node.js for most of my time in the past 3 years. Around  November 2018, I started to get the feel that I am missing something in my toolbox.

One thing that I do easily is to get excited about programming - programming languages, tools, technologies and even the old things that I haven't experienced before. This leads me to be that kind of person who likes to explore more and learn from them.

During November 2018, I was basically having my mind fly around huge number of thoughts like let me read the source code of a open source software today... no let me do competitive programming and improve my DS and algorithm skills... no let me spend time learning about design patterns and learn Object Oriented Programming... no let me pick up functional programming... no let me read about linux and do Systems Programming...

I was equally excited for doing all of those. Before the confusion took over and make me do nothing, I decided to take initiative and progress somewhere. I can't do all at once but I could wisely choose a tool that will help me do most of them.

So what was that tool? You guessed it right. It was C++

NOTE: If you feel weird when I call out a programming language as a tool, become comfortable with it. Because I just bring that up wherever possible! - I feel that it is just a tool to instruct a machine to do something.

Ok! Here is my evaluation of what led me to study C++ in 2018 and I have no regrets about it now.

## C++11 is not the C++ I ran away from

I studied C++ in my college and I used to fear using it mainly because of the book I used to learn. It was a pretty scary book - a very big one portraying C++ to be full of complex concepts. Actually I was ok with it, but the real problem started to happen when I attempted to write C++ for building a Windows Store app for Windows 8 platform. 

I met with lot of outside the text book notations like the [Microsoft Visual C++ ^ operator](https://stackoverflow.com/questions/500580/in-c-cli-what-does-the-hat-character-do). I couldn't even manage to understand the sample codes properly. At the same time, I met C# which was easy to learn and understand + had friends who use it - so it was my time to blend with the local community and rebel against C++.

I heard about the new C++ standards here and there on the internet like C++11, C++14, C++17 and C++20. I was curious to know what changed in them. 

I chose to learn C++11 because it was the breaking point and a major release of what C++ was. After learning it and while learning it, I have to tell you that it is not the C++ I feared and ran away from few years back. It is something else. (nicer!)

## Tool from the past

C++ is hanging around for a long time ( 34 years till date according to Wikipedia). It is powering some of the world's oldest and stable piece of software written over all these years. So I thought there must be a secret sauce in there that is keeping it alive. 

## Tool to read C/C++ code bases

> Read more code than you write

I took this programming advice seriously and as a result I have been wanting to read more code. A good way to start this would be to read books that have code in them. Because you just can't start reading the source code of a code base from top to bottom (you can but not in most cases, because you might give up at some point without understanding something). Books are in between everything from documentation to source code to contributing guides.

I was very much interested in reading the source code of V8, Node.js, libuv, redis, electron etc. because they will help me to understand node.js or respective technologies in a better way and all of them are written in C or C++

C is not going to go away at least in the near future and so is C++. Because there are already great piece of software written in them and is being used extensively. So learning C++ would be helpful for me if I ever have to work with / debug / understand internals of any of those kind of software.

## Tool to solve puzzle questions

C++ is widely adopted amongst competitive programmers. I heard somewhere that all the finalists of Google code jam use C++ except 1 who used Java. Why so? It is mainly because of the STL which is providing nice functionality and clear abstraction. 

```cpp
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <bitset>
#include <algorithm>
```

If you ask me one favourite thing about C++, it would be the  presence of STL and it's organisation.

I don't want to compare any specific language here, but I obviously compared it with a lot of languages and I feel that C++ really got this right! 

## Object Oriented Programming

I read Head First Design Patterns book in October 2018 and I was interested in implementing and learning about these patterns more. So I obviously wanted to learn a language which has good OOPS background. For example, I learnt Go back in Jan 2018 for most of the reasons written down here, but it did not satisfy this particular criteria. It was filled with structs and it was [hard to or impossible](https://github.com/tmrts/go-patterns) to express the common patterns in it. I don't want to sail the same ship. This time I am taking the one which is deeply rooted and created in first place for Object Orientation.

## Tool to understand other languages

By the end of 2018, we are clearly seeing this emergence of newer Systems Programming languages being written (Go, Rust, Crystal, Zig). Most of them advertise to fix what C++'s shortcomings are. So I believe that learning C++ is a good way to get idea about those problems and using it will actually make me feel the real pain, that is causing the newer languages to emerge (and also how C++ is trying to solve with newer versions maintaining/breaking compatibility).

For example, after reading C++ for a while I took a break for a week to learn about Rust. I definitely attempted to read about Rust before, but gave up during those attempts. But this time the story is different. I was curious to know how the ownership model and lifetimes in Rust are reducing pain because I have already got enough taste of segmentation faults at this point. (If you are interested in C++ and read till this point, there is a good chance that you will enjoy learning Rust. Give it a go!)

## Paradigm

C++ has a nice merge of various programming paradigm embedded in it. From Object Oriented Programming to function programming, we have the batteries included!

Want to do systems programming? sit down and write code that is C like and get a good performance.

```cpp
// access a dynamically sized array like
vec[10];
 
// more efficient but unsafe than
vec.at(10);

// because .at() throws exception for out of bounds access
```

I personally use `.at()` at all times because my use cases demand safety over performance. Programming is all about trade offs. It is like they say, "you have to lose something to gain some other thing!"

One thing that I absolutely loved learning + using in C++ is generics. As I [tweeted](https://twitter.com/scriptnull/status/1063634792888115200) a while back, C++ is full of generics.

> There is a rich heritage of generic programming popping up everywhere, resulting in generalized ideas.

Regarding functional programming, C++ now includes lamda expressions and closures, functors, and [functional header](http://www.cplusplus.com/reference/functional/).

## Problems

There are definitely some problems that I faced in this land. These problems gave a sense of when to and when not to use C++ for solving a problem.

**I have to pay:** First and main concern being that the standard study materials for reading about C++ are not free. They are in book format ([The C++ Programming Language (4th Edition)](http://www.stroustrup.com/4th.html) and [A Tour of C++ (Second Edition)](http://www.stroustrup.com/tour2.html)) and you have to pay for them. Good work in the Rust community in this case because they have free and open books for all the standard study material. 

**Tooling:** Coming from a JS background, npm set high expectations in this area. I faced this problem in Go too (which I think is being actively solved). There is no standard tool for doing a particular thing — there are just a lot of tools and that basically gives you flexibility to use them and confusion of which one to use. There are lot of choices available for compilers (gcc, Microsoft Visual C++ compiler, clang), build tools (make, bazel, ninja etc.) and there is CMake which a lot of projects seem to use and again we have to pay for getting the standard material on it and even more is that there will be a lot of time spent learning and choosing. For formatting there is clang_format which seems to be a nice way but I am using gcc for compiling my code and to format my C++ I have to suddenly install clang tools. This just leads to more work and effort. Package management with Conan - I haven't given it a try. You know why! It is worth learning if it is being already used in a project that you are interested in or it is the standard/default way recommended of doing something. There are lot of test frameworks too — most common being gtest and catch2. Again more choices. On the other hand Rust has solved the tooling problem nicely with cargo, creates, tests, benchmarks etc. in a simpler way.

To round up, C++ does not dictate about its tooling, which basically gives lot of choices and flexibility. But at the same time it is making it complex for beginners to come in to projects and start projects with it.

![crazy](https://media.giphy.com/media/xUA7aSnSnSnrWWSTWE/giphy.gif)

Example: I just spent days learning about tools and coming up with [my own C++ setup](https://vishnubharathi.codes/blog/my-cpp-setup/)  for bootstrapping projects in C++ — when entering rust all I have to do was type `cargo new project —bin` 

Oh and I am not trying to advertise that Rust got everything right and you should use Rust because nothing is ever perfect and that is what make things interesting.

There are awesome efforts going on already to overcome the problems. One such notable effort being C++ Modules which is probably the most exciting thing if you ask me.

## No regrets

Despite all the problems I faced, I still don't have regrets learning and using C++ now and then. Because it gives this awesome base of knowledge about problems that programmers faced all these years and how they are being solved with respect to language design and tooling.

> "Within C++ is a smaller, simpler, safer language struggling to get out." - Bjarne Stroustrup

There surely is!

~ ~ ~

Woah! This post got posted on [Hacker News](https://news.ycombinator.com/item?id=18845476) and received very insightful comments. Thank you everyone for sharing this in your network and giving helpful feedback!

