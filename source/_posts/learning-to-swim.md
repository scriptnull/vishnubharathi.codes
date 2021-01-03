---
title: Learning to SWIM
date: 2021-01-03 09:22:20
tags: ["databases","research papers"]
---

I finished reading a research paper called "SWIM: Scalable Weakly-consistent Infection-style Process Group Membership Protocol" last night. This post is going to be about it. If you are here to read my experience about real-world swimming, I have disappointed you - I still don't know to swim in waters, haha.

First, I started by reading the Raft paper and was trying to go through a few open source RAft implementation libraries and see how those libraries are used in softwares that are currently used in production. The exploration included the following places:

- https://github.com/hashicorp/raft
- https://github.com/hashicorp/consul
- https://github.com/hashicorp/nomad
- https://github.com/hashicorp/raft-mdb


Halfway through my Raft journey, I understood that Raft is a consensus algorithm - It is about making a few machines (a cluster) agree on something. But it does not deal with how machines could be added/removed in the cluster. So we need to handle cluster membership outside it. While digging the above libraries, I arrived at how cluster membership is done in some of the practical systems (mostly the Hashicorp stack).

Hashicorp seem to have [Serf](https://github.com/hashicorp/serf) which could be used for performing cluster membership. More specifically it uses this [memberlist](https://github.com/hashicorp/memberlist) library to do it which is based on this awesome research paper.

```
A. Das, I. Gupta and A. Motivala, "SWIM: scalable weakly-consistent infection-style process group membership protocol," Proceedings International Conference on Dependable Systems and Networks, Washington, DC, USA, 2002, pp. 303-312, doi: 10.1109/DSN.2002.1028914.
```

Here are some of my notes on the SWIM paper. The SWIM paper starts with this nice quote:

> As you swim lazily through the milieu,
> 
> The secrets of the world will infect you.

## Motivation
The main motivation behind the SWIM paper is

> The SWIM effort is motivated by the unscalability of traditional heart-beating protocols, which either impose network loads that grow quadratically with group size, or compromise response times or false positive frequency w.r.t. detecting process crashes.

Before SWIM, the norm is to use a simple many-to-many heart-beating protocol to propogate cluster membership in the cluster. Consider this example:

If the cluster has n nodes, then it needs to send message to all the other (n-1) nodes. Hence we end up sending n*(n-1) messages across the network when we want to exchange the information about cluster membership. This means that our network load (number of communications that happen on the cluster network) grows quadratically (n<sup>2</sup>) for a group of n nodes in the cluster.

Example of what we are dealing with here:

When there are 5 nodes, we will end up making 5<sup>2</sup> = 25 network communications. For 10, it will be 100 and for 100, it will be 10,000 (just for sharing the knowledge of what nodes are in the cluster)
