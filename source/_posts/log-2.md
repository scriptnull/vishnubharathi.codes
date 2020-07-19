---
title: log 2 = 0.3010
date: 2017-10-16 04:00:00
tags: ["blogging"]
---

# log 2 = 0.3010

This is my second weekly log.

### Language Servers

[Language Servers](https://code.visualstudio.com/blogs/2016/06/27/common-language-protocol) are awesome. In [one of my previous blog posts](https://medium.com/@scriptnull/understanding-ast-for-building-better-developer-tools-40a18bbbc87a), I have talked about Abstract Syntax Trees and how they play an important role in building developer tools.

I am super interested everything about Editors and IDEs. Plugins, Text Editing Algorithms, Text searching algorithms, UTF-8, and literally anything regarding text editing. You name it, I am ready to learn about it.

I wanted to know more about language servers, ever since hearing this talk.

<center><iframe width="560" height="315" src="https://www.youtube.com/embed/SwAhE5zgsbQ" frameborder="0" allowfullscreen></iframe></center>

So, I started this week by skimming through stuff about Language Servers, Lexers etc. The conversation [happening here](https://github.com/crystal-lang/crystal-book/issues/124) made me to get a idea about language server implementation of crystal language called [scry](https://github.com/crystal-lang-tools/scry).

Few things to note here are, Language server protocol could be read from it’s open source repository.
[**Microsoft/language-server-protocol**
*language-server-protocol - Defines a common protocol for language servers.*github.com](https://github.com/Microsoft/language-server-protocol)

It uses JSON-RPC to communicate back and forth.
[**JSON-RPC 2.0 Specification**
*JSON-RPC 2.0 Request objects and Response objects may not work with existing JSON-RPC 1.0 clients or servers. However…*www.jsonrpc.org](http://www.jsonrpc.org/specification)

Why JSON-RPC ? It’s probably lightweight and same reason why JSON is preferred over XML ( JSON’s size is much smaller compared to XML )

    {
      "name": {
        "first": "Vishnu",
        "last" : "Bharathi"
      }
    }

Vs

    <name>
      <first>Vishnu</first>
      <second>Bharathi</second>
    </name>

XML uses 66 characters and JSON uses 45 characters !

### Tired days

I was tired most of the week nights. I did long commutes in bus. Heavy rain is making these commutes more adventures and sometimes tired I guess. So this week is going in a more relaxed phase.

<iframe src="https://medium.com/media/2892ed5922093b8d363be960ebe201fa" frameborder=0></iframe>

### pv

I learnt about this amazing command utility called pv ( Pipeline Viewer )

    $ yes | pv > yes.txt

![pv intercepts writing yes command output to a file and shows its progress.](https://cdn-images-1.medium.com/max/2768/1*MdEciyVKwXymzkytGY_4YQ.gif)*pv intercepts writing yes command output to a file and shows its progress.*

### Trees

I happend to go through some really basic stuff about trees this week. Also tried to cartoon that stuff and will probably upload them to [pinterest](https://www.pinterest.com/scriptnull/data-structures/) later this week.

### linkedlist.cr

I wanted to build a production quality linked list in crystal and i started on it last week. I spent most of my weekend building it and i am close to completing singly linked list.
[**scriptnull/linkedlist.cr**
*linkedlist.cr - Linked List Implementation for Crystal Programming Language*github.com](https://github.com/scriptnull/linkedlist.cr)

I wrote a lot of tests ( 70+ ) for my code and actually felt the feeling of writing object oriented code after quite some time.

### Dream in code

I think I spent a good amount of time with linked lists and programming, that when I woke up the Monday morning i had a dream of rewriting a Unix command line utility in [rust](https://www.rust-lang.org/). Haha. Just like the good old days when I dream of making npm packages for every computer science problem I wanted to solve.

### What is a container?

I watched this amazing talk about containers. It’s really cool and i would definitely recommend it to people who are into containers.

<center><iframe width="560" height="315" src="https://www.youtube.com/embed/HPuvDm8IC-4" frameborder="0" allowfullscreen></iframe></center>

### DEF CON

I also love this conference named DEF CON. I take time to learn about computer and information security whenever possible. This weekend I watched and liked this talk on proxies and botnets.

<center><iframe width="560" height="315" src="https://www.youtube.com/embed/0QT4YJn7oVI" frameborder="0" allowfullscreen></iframe></center>

### This is helping me

This whole weekly log thing is very new to me and i already feel that it’s helping me by having notes on various things I learn and do. This is kind of fun, but I want to streamline the process more.

### Wish list

* [DONE] Upload the tree data structure cartoons to [pinterest](https://www.pinterest.com/scriptnull/data-structures/)

* Launch linkedlist.cr v1.0.0

* Contribute to a language server.

Thanks for reading. I quote verses from my favourite Tamil literature “[Tirukkuṛaḷ](https://en.wikipedia.org/wiki/Tirukku%E1%B9%9Ba%E1%B8%B7)” at the end of my blog posts.
> # “இன்பம் விழையான் இடும்பை இயல்பென்பான்
> # துன்பம் உறுதல் இலன்.”
> # — திருக்குறள்

Translated meaning ( in my words ): Problems are common. People who understand this simple truth will not be affected by their problems.
