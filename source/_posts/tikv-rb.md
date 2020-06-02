---
title: Building a ruby client for TiKV
date: 2020-05-15 20:35:00
tags: ["programming"]
---

My recent interest in key-value stores and a few hours of fresh afternoon sleep is leading me to build something on this Friday night!

If you haven't heard of TiKV,

> TiKV : A distributed transactional key-value database

TiKV is a very exciting project to work on! It looks very promising. A lot to offer which means, there is also a lot to build around!

For example: I am very excited to see a new KV API in TiKV (VerKV - the one that lets MVCC + gives support for expire times on key values). This is happening at https://github.com/tikv/tikv/issues/7295

In my journey of understanding about key-value storages, I have been concentrating on studying the about the clients for a while. I am kind of into Ruby programming these days and I have been out of touch with open source for a while. I want to get back on it!

The current landscape of TiKV clients look like this

![tikv-clients](/images/tikv-clients.png)

With lots of good reasons, I have decided to work on a ruby client for TiKV and probably donate the implementation to the core TiKV project (if that is welcomed)

This is going to be a "blog as I do it thing"!

## Setup

After playing around with [various deployment methods](https://tikv.org/docs/3.0/tasks/deploy/introduction/) for TiKV, I decided to do an old-fashioned, "bring up software using binaries" style of bringing up a TiKV server for local development.

In order to verify the setup, I also created a simple demo app written using the Go client, as Go seems to be the stable client for TiKV (inferring from the docs)

So we got a placement driver and TiKV now. (In case of if you are wondering what a placement driver is, follow along)

## Architecture

Before we go further down the line, let us try to revise on the basics of TiKV.

Here is a beautiful architecture diagram of TiKV (from the [TiKV Architecture page](https://tikv.org/docs/3.0/concepts/architecture/))

![tikv-arch](https://tikv.org/img/basic-architecture.png)

In simple terms, TiKV is a distributed key-value store. That means it can store multiple copy of a key-value pair in multiple nodes. If you scale up/down nodes, the data gets distributed (balanced) among the available nodes again.

So, TiKV is architectured to run with the help of something called the placement driver. It is the component that is aware of the cluster topology of TiKV, helping in auto-sharding (the balancing stuff that I spoke about above)

A TiKV node has the actual KV whereas the placement driver contains information on which TiKV node is reponsible for having a KV.

So, our placement driver is the entry point of things. From what I understand, here is a guess of how these clients work.

- client speaks with placement driver over GRPC and asks "which TiKV node is suitable for performing this KV API call?"
- client gets back the address of a TiKV node from placement driver and does the actual KV operation on the TiKV node.

I am just guessing, but let us see. If we take a look at the method signature in Go client, we give a list of placement driver IP addresses to the constructor of the Client. So this kind of aligns towards my guess.

oh, here is some other thing we need to be aware of TiKV has two kinds of APIs currently ( A third one is in progress :) )
- Raw API : A lower-level key-value API for interacting directly with individual key-value pairs.
- Transactional API : A higher-level key-value API that provides ACID semantics

I think that is enough architecture.

## Help

After hours of trying to backtrack the code in the Go client and building the proto files present at https://github.com/pingcap/kvproto , I decided to ask for a little help!

![help](https://user-images.githubusercontent.com/4211715/82099608-5b536e80-9725-11ea-9941-ba11865b5b1d.png)

Lets see if someone responds!

Got back a response saying that I am on the right track. So will continue to get the code generation from proto files working and reverse engineering the implementation of other clients.


~ ~ ~

I tried again and again to get the proto files to generate code, but struck with some weird C++ header file errors. Also there is not enough documentation on building clients overall. With all these obscurity, I am pausing this project to focus on something more productive.
