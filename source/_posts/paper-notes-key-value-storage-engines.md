---
title: Paper notes: Key-Value Storage Engines
date: 2020-08-11 08:48:16
tags: ["research papers","recurse center"," databases"]
---

These are my notes and and thoughts that came up while reading this research paper called [Key-Value Storage Engines](https://stratos.seas.harvard.edu/files/stratos/files/keyvaluestorageengines.pdf).

I first came across this paper in [TiKV's slack](https://tikv-wg.slack.com/archives/CGQ6VFATU/p1589836557016600). I have been wanting to read it eversince! (and pulled it off early morning yesterday). I think the paper is a short one compared to any of the papers that I have read. It was published recently and so it contains notes about latest key-value stores.

> we survey the state-of-the-art approaches on how the core storage engine of a key-value store system is designed.

On the side: I was wondering how to discover new research papers to read about in topics of interest. My current interest is in databases (more specifically key-value stores and hybrid stores). Seems like one efficient way is to take on a introductory paper (like the one we are going to discuss about here), read it and see how it aligns with the goals. If you got what you want, go and check the other works of the author(s) of the paper. I did the same for this and ended up amazed by the work [one of the authors](https://stratos.seas.harvard.edu/) of this paper.

Speaking of authors, let me put up the ACM reference format here to give credit to the authors and the paper

```
Stratos Idreos and Mark Callaghan. 2020. Key-Value Storage En-
gines. In Proceedings of the 2020 ACM SIGMOD International Con-
ference on Management of Data (SIGMOD’20), June 14–19, 2020,
Portland, OR, USA. ACM, New York, NY, USA, 6 pages. https://doi.
org/10.1145/3318464.3383133
```

## Contents
The main contents of the paper is divided into three parts

1. Key-value storage engines and applications
1. State of art engine design
1. Self-Designing NoSQL storage

## Key-value storage engines and applications

Key-value stores could be used in lot of places. I will summarize the interesting takes from the paper.

First take: __Key Value Stores are used in SQL systems__

I have mostly viewed tables in SQL systems as "tables" (you get me!). This paper lays the base work of thinking about SQL tables in terms of key-value stores.

> FoundationDB is a core part of Snowflake, while My-Rocks integrates RockDB in MySQL as its back-end storage.

It seems like modern databases seem to use a distributed key-value store as building block. I have noticed this pattern recently in "TiKV being used as a the underlying store as TiDB".

I will try to describe more about this in a while! 
