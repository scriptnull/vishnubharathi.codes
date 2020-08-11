---
title: "Paper notes: Key-Value Storage Engines"
date: 2020-08-11 08:48:16
tags: ["research papers","recurse center"," databases"]
---

These are my notes and thoughts that came up while reading this research paper called [Key-Value Storage Engines](https://stratos.seas.harvard.edu/files/stratos/files/keyvaluestorageengines.pdf).

I first came across this paper in [TiKV's slack](https://tikv-wg.slack.com/archives/CGQ6VFATU/p1589836557016600). I have been wanting to read it ever since! (and pulled it off early morning yesterday). I think the paper is a short one compared to any of the papers that I have read. It was published recently and so it contains notes about the latest key-value stores.

> we survey the state-of-the-art approaches on how the core storage engine of a key-value store system is designed.

On the side: I was wondering how to discover new research papers to read about in topics of interest. My current interest is in databases (more specifically key-value stores and hybrid stores). Seems like one efficient way is to take on an introductory paper (like the one we are going to discuss here), read it, and see how it aligns with the goals. If you got what you want, go and check the other works of the author(s) of the paper. I did the same for this and ended up amazed by the work [the authors](https://stratos.seas.harvard.edu/) of this paper.

Speaking of authors, let me put up the ACM reference format here to give credit to the authors and the paper

```
Stratos Idreos and Mark Callaghan. 2020. Key-Value Storage En-
gines. In Proceedings of the 2020 ACM SIGMOD International Con-
ference on Management of Data (SIGMOD’20), June 14–19, 2020,
Portland, OR, USA. ACM, New York, NY, USA, 6 pages. https://doi.
org/10.1145/3318464.3383133
```

## Contents
The main contents of the paper are divided into three parts

1. Key-value storage engines and applications
1. State of art engine design
1. Self-Designing NoSQL storage

## Key-value storage engines and applications

Key-value stores could be used in a lot of places.

> graph processing in social media [9, 14], to event log processing in cybersecurity [15], application data caching [51], NoSQL stores [57], flash translation layer design [21], time-series management [42, 43], and online transaction processing [26].

One interesting take in this section: __Key Value Stores are used in SQL systems__

I have mostly viewed tables in SQL systems as "tables" (you get me!). This paper lays the base work of thinking about SQL tables in terms of key-value stores.

> FoundationDB is a core part of Snowflake, while My-Rocks integrates RockDB in MySQL as its back-end storage.

It seems like modern databases seem to use a distributed key-value store as a building block. I have noticed this pattern recently in "TiKV being used as the underlying store as TiDB".

Apart from the applications, the section introduces properties like read, update, and memory amplification. Each key-value store has different properties and it is up to the users to choose a store based on their workloads.

By reading this section, I mostly understood this:

> There is no Perfect Design.

If we are trying to build a key-value store from scratch, we must first understand and accept the trade-offs. Ask questions and arrive at answers like

Q: What kind of workload will be suited the most for the store?

A: It suits the most for frequent reads and in-frequent bulk inserts.

An example mentioned in this paper is [sparkey](https://github.com/spotify/sparkey), a key-value storage library from Spotify which does that tradeoff.

## State of art engine design

Before this paper, I usually took the time to think about the outer-most layers of key-value stores like the communication protocols, how are we going to store data in-memory. This paper jumps right into the core - how data is stored on the disk? How data is first stored in memory and moved to disk afterward?

### Big three
The paper introduces about three data-structures to be at the core of the state of art storage designs.

1. B+ tree
2. Log-structures merge-tree (LSM tree)
3. Log and Index (LSH table)

That's it! If I just learn about them, then I should have a basic idea about what's going on in most databases.

#### B+ tree

> B+ tree is the backbone design of the BerkeleyDB key-value store [53], now owned by Oracle, and the backbone of the WiredTiger key-value store [66], now used as the primary storage engine in MongoDB [52]. FoundationDB [8] also relies on a B+ tree.

#### LSM tree

This is usually augmented with some-other things like:

> In-memory structures such as Bloom filters, fence pointers and Tries help filter queries to avoid disk I/O [19, 67].

In practice: 

>  This design has been adopted in numerous industrial settings including LevelDB [30] and BigTable [17] at Google, RocksDB [27] at Facebook, Cassandra [45], HBase [33] and Accumulo [7] at Apache, Voldemort [47] at LinkedIn, Dynamo [24] at Amazon, WiredTiger [66] at MongoDB, and bLSM [61] and cLSM [29] at Yahoo, and more designs in research such as SlimDB [58], WiscKey [49], Monkey [19, 20], Dostoevsky [22], and LSM-bush [23].

#### Log and index

> This Log and Index design is employed by BitCask [62] at Riak, Sparkey [64] at Spotify, FASTER [16] at Microsoft, and many more systems in research [2, 46, 59].

I guess that the concrete implementation of this technique is called Log-Structured Hash tables.

> Most systems use a hash table as the index over the log.

### Design Descisions

The remainder of this section deals with various design considerations that we need to be aware of while building a key-value store. 

1. Memory management
1. Compactions and Splits
1. Concurrency control
1. Time travel queries
1. CPU vs I/O Cost
1. Adaptive Indexing and layouts

#### Memory management

> One of the most critical decisions in key-value stores is how to distribute the available bits across the various in-memory components. For example, in an LSM-tree like design, it is common to have numerous Bloom-filters in memory and other helper structures to help skip disk reads.

#### Compaction and Splits

> Depending on the exact design a NoSQL engine will need to frequently reorganize data such as to maintain certain performance invariants. For example, an LSM-tree like design needs to perform compactions as new data arrives such as to maintain order and remove past invalid values that have been updated out of place.

Compactions can happen in two ways: in-place and out-of-place compactions. Out-of-place compaction allows queries to be served while the compaction is happening. The way it does it is by having a duplicated in-memory copy from which the query could be served while the actual data is undergoing compaction. For in-place compactions, the query will block.

So, we know one new thing about LSM trees from this section: They don't block queries while undergoing compactions.

#### Concurrency control

> LSM-trees are inherently more able to process concurrent requests compared to a typical B-tree design because they update data out of place. Similarly, a log-structured hash table design goes a step further by performing much fewer compactions and thus creating fewer conflicts for reads and writes (at the expense of read cost). B-tree designs can also adopt an out of place approach by stacking updates in leaf nodes like BW-tree or across any node like Bε tree.)

#### Time travel queries

Key-value stores might be designed to store timestamps along with key-value pairs. This choice opens up the possibility for implementation of features like

1. Multiple versions of the same key could be stored
1. TTL (Ability to automatically remove the key-value pair after certain amount of time)

> if timestamps are stored inline with the base date, then this can lead to significant overheads for all queries (since timestamps will need to be read along with the base data).

#### CPU vs I/O Cost

> using compression leads to increased CPU costs and the exact form of compression used defines the balance of I/O saved versus CPU sacrificed.

So if we are trying to build a database, we need to decide whether if we are going to support compression of data and have to get an idea about various types of compression.

#### Adaptive Indexing and Layouts

> Adaptive indexing [36] is a lightweight approach in self-tuning databases. Adaptive indexing addresses the limitations of offline and online indexing for dynamic workloads; it reacts to workload changes by building or refining indices partially and incrementally as part of query processing.

Before going on to adaptive indexing, we need to think about just "indexing". How are we going to store the index of keys in-memory? What if there are a lot of keys? Is it possible to index only a partial set of keys and swap out the partial to load the parts that we need? Things like these!

Now we are allowed to get excited about newer research on adaptive indexing - what if the key-value store automatically figures out what to index based on the access patterns of the workload? - exciting, huh?

## Self-Designing NoSQL storage

This section of the paper mostly deals with the special interest of the authors - Self-tuning databases. You can read up this section of the paper if you are interested. I didn't understand much, but in simple terms, they are trying to describe data systems that self-tune it's configuration _near instantly_ (ah, interesting!) on live workloads.

That leads me to a project written by one of the authors of this paper called CrimsonDB - https://demosubmitter.github.io/

If this sounds exciting, the next step for this is exploring the [Data Calculator](https://stratos.seas.harvard.edu/files/stratos/files/datacalculator.pdf) paper which gives an idea about "how we can synthesize more data structures than stars on the sky to pick the right one for a given problem".

## Questions to work on

Arrived at a list of questions by reading this paper: 

(I believe each one has the potential to become a blog post on its own)

1. What is a B+ tree?
1. What is an LSM tree?
1. What is an LSH table?
1. What is a B<sup>ε</sup> tree?
1. What is a BW-tree?
1. What is a Bloom filter? (probabilistic data structure)
1. What is a fence pointer? (I think it is something that supports an LSM tree)
1. What other ways of storing timestamps for KV pairs are there? (apart from storing it inline with the kv-pair itself)
1. What kind of compression techniques are employed by various key-value stores?

~ ~ ~

If you want to discuss about any of the above things, feel free to [say hi](https://twitter.com/scriptnull) to me!
