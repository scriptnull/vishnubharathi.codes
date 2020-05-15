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
