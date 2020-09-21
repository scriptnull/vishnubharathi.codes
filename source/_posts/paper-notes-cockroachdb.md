---
title: Paper notes - CockroachDB: The Resilient Geo-Distributed SQL Database
date: 2020-09-20 00:23:19
tags: ["databases"," recurse center"," research papers"]
---

CockroachDB published a [paper sometime back](https://www.cockroachlabs.com/blog/cockroachdb-sigmod-2020/). Since I am trying to learn about databases and trying to pick up Go programming, I thought this might be a good read.

These are my notes from reading that paper. Also, moving forward I will be referring CockroachDB as CRDB (like they do it in the paper) to save some key strokes.

## A simple intro

If you have never heard of or used CRDB before, here are some things that you might want to know.

- It is a SQL database. (compatible with postgres clients)
- It is horizontally scalable unlike conventional SQL databases.

## Paper intro

The paper introduces CRDB by telling about the following features which makes it suitable for usage in global companies.

- Fault tolerance and high availability
  > CRDB maintains at least three replicas of every partition in the database across diverse geographic zones.

- Geo-distributed partitioning and replica placement

- High-performance transactions
  > It provides serializable isolation using no specialized hardware; a standard clock synchronization mechanism such as NTP is sufficient.
  
## Architecture

Overall,

> A CRDB cluster consists of an arbitrary number of nodes, which may be colocated in the same datacenter or spread across the globe. Clients can connect to any node in the cluster.

### Layers

At a node level, CRDB has the following layers:
- SQL
- Transactional KV
- Distribution
- Replication
- Storage

All communication to CRDB is done with SQL. So there is a SQL parser, optimizer and execution engine. It is said that the SQL layer is responsible for converting SQL into low level read and write requests to the underlying KV store. This is a classic example of how SQL databases use Key-value engines as a underlying storage.

Among all the layers mentioned above, the most confusing part is the "Distribution" layer. I wonder what really happens there. The only thing I could understand here is the keys of the kv pair are getting partitioned and stored in ranges. Each range is ~64MiB of size (reason? low enough for quick movement of data between nodes and high-enough to store contiguous data which are accessed together)

To better understand ranges, I found this line in CRDB docs:

> CockroachDB splits rows of table data into ranges, and then replicates the ranges and distributes them to the individual nodes of the cluster.

Also, one interesting part is that CRDB used RocksDB in the storage layer as of writing the paper. So there is cgo in there. I was wondering why not use [Badger](https://github.com/dgraph-io/badger) (both are based on LSM trees, but badger is written in Go which would help us avoid cgo overhead) and found the answer [here](https://github.com/cockroachdb/cockroach/issues/17929)

### Replication using Raft

CRDB seems to use Raft consensus algorithm for replication.

> The unit of replication in CRDB is a command, which represents a sequence of low-level edits to be made to the storage engine.

This section also discusses about leases. CRDB uses Range-level leases. All writes go-through the leaseholder.

>  Leases for user Ranges are tied to the liveness of the node the leaseholder is on; to signal liveness, nodes heartbeat a special record in a system Range every 4.5 seconds. System Ranges in turn use expiration based leases which must be renewed every 9 seconds.

So, now we have the notion of User ranges and System ranges.

### Automatic load (re)balancing

> Nodes can be added to or removed from running CRDB clusters, and can fail temporarily or even permanently. CRDB treats all of these scenarios similarly: they all cause load to be redistributed across the new and/or remaining live nodes.

When the affected node rejoin, it seems like CRDB could choose to send full range data or just the raft log entries that went missing during the downtime. This decision is taken by looking at the number of writes that happened during the downtime of the node.

> The node liveness data and cluster metrics required to make this determination are disseminated across the cluster using a peer-to-peer gossip protocol.

Wait, so this gossip protocol is not the responsibility of raft? So raft is a consensus protocol - meaning a protocol to help multiple nodes aggree upon a value. Wheres gossip protocol is useful for informing nodes about discovery, metadata etc. - [read this](https://forum.cockroachlabs.com/t/the-different-roles-between-raft-and-gossip/957#:~:text=Gossip%20is%20how%20new%20nodes,through%20raft%20membership%20change%20operations.)

### Data placement

> CRDB has both manual and automatic mechanisms to control replica placement.

They way CRDB does this would be when you start the node, we are supposed to pass in a `--locality` flag which suggests the nodes about their locality. [Docs here](https://www.cockroachlabs.com/docs/v20.1/cockroach-start#locality). Apart from locality, I think CRDB should allow users to place data based on other parameters like RAM, disk type etc.)

The paper describes about the following data placement policies:

- Geo-Partitioned Replicas
- Geo-Partitioned Leaseholders
- Duplicated Indexes

It might be a bit more interesting to actually use them in a practical system.

## Transactions

> CRDB uses a variation of multi-version concurrency control (MVCC) to provide serializable isolation.

It seems like CRDB employs two approaches to optimize transactions: Write pipelining and parallel commits. There is a graph in the paper comparing parallel commits and two-phase commit. I am not sure how parallel commits work (something to dig up on), but it seems like it is helpful in reducing extra round of consensus.

One interesting stuff that I found here is that CRDB uses TLA+ to verify the safety properties of Parallel Commits - https://github.com/cockroachdb/cockroach/tree/master/docs/tla-plus

It is good to note that transaction deals with two things - a co-ordinator and a leaseholder. The SQL client that wants to perform a transaction actually connects to a node in the cluster (typically the one that is close to the client) and co-ordinates the transaction. Thus called the co-ordinator.

### Atomicity Guarantees

> An atomic commit for a transaction is achieved by considering all of its writes provisional until commit time. CRDB calls these provisional values write intents.

So, it does something like - write whatever data is involved in the transaction as a KV-pair. Use the metadata associated with it to actually commit the data. It seems like a transaction could be any of these states - pending, staging, committed or aborted.

### Conflicts

The core part of a transaction is its timestamp. The paper decribes the following conflicts occuring due to the ordering of the timestamps in the transactions:

#### Write-read conflict:
> A read running into an uncommitted intent with a lower timestamp will wait for the earlier transaction to finalize. Waiting is implemented using in-memory queue structures

#### Read-write conflict
> A write to a key at timestamp ta cannot be performed if there’s already been a read on the same key at a higher timestamp  tb >= ta . CRDB forces the writing transaction to advance its commit timestamp past tb

#### Write-write conflict
> A write running into an uncommitted intent with a lower timestamp will wait for the earlier transaction to finalize (similar to write-read conflicts)

Also it is good to know that,

> CRDB employs a distributed deadlock-detection algorithm to abort one transaction from a cycle of waiters.

