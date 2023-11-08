---
title: Paper notes: Use of Formal Methods at Amazon Web Services
date: 2023-11-09 03:56:53
tags: ["research papers"]
---

It has been a while that I posted paper notes or anything at all in this blog. Luckily, I got curious last night about "How are distributed systems tested?". My curiosity was evoked by these factors:
- I keep on hearing about "Deterministic Simulation Testing" used in the [TigerBeetle](https://github.com/tigerbeetle/tigerbeetle) project. I wonder what is it (haven't explored it yet) and what are the other methods to test distributed systems.
- I have been wanting to add "High Availability" modes in [my little side project](https://github.com/scriptnull/waymond) and I wanted to understand how to test the high availability of the system before declaring it to be highly available :D
- Maybe there are some lessons that I can take away for designing and implementing different testing strategies at [my current work](https://hasura.io/).

With those very good enough reasons, I stumbled upon [this awesome github repo](https://github.com/asatarin/testing-distributed-systems) which curates various testing strategies for distributed systems. One of the things that stood out for me in that list was "Formal methods", more specifically "TLA+". It then led me to watch [this awesome conference video](https://youtu.be/sPSPEgz3o9U?si=oyvODVhHCr5l7ZnQ) where they compare TLA+ and [Jepsen](https://jepsen.io/)/[maelstrom](https://github.com/jepsen-io/maelstrom) - the video made me feel excited about both the technologies. A quick lesson from the video: TLA+ is apples and Jepsen is oranges - we would ideally want to eat both.

I then decided to learn more about TLA+ since that comes in the earlier stages of the design process. I have previously attempted to learn TLA+ but couldn't succeed in it successfully - mainly due to a lack of motivation in the middle of the learning process. So, I wanted to be motivated enough this time before attempting to learn it again and try to use it in my side project or at work. This line of thinking made me remember that AWS had published a paper about TLA+ that I had heard of in the past. So I decided to pick it up and read it.

You can get a copy of it from [here](https://www.amazon.science/publications/how-amazon-web-services-uses-formal-methods).

# Intro

This paper is an experience report from the Engineers who spearheaded the moment of using formal methods to verify complex distributed systems that were getting built at AWS such as S3, Dynamodb, etc. At first, they didn't think of formal methods and were investing in other types of testing. Those tests helped but there were still edge cases that could cause serious bugs.

They open up with the scale that they are dealing with here.

> As an example of this growth; in 2006 we launched S3, our Simple Storage Service. In the 6 years after launch, S3 grew to store 1 trillion objects [1]. Less than a year later it had grown to 2 trillion objects, and was regularly handling 1.1 million requests per second [2].

Imagine that you were about to design a system for such a high scale and growth - how will you gain confidence about its design and correctness? If you are making any changes to the system at some point, how will you be confident about the effects of your changes?

The first line of defense in order to gain that confidence is using formal methods to specify and check your system design. Once we made sure that our design is correct, then we start to implement it and write "tests" which check the correctness of the code (this is the classic software testing bit that we are used to).

# Precise Designs

What do most of us do most of the time while designing systems?

> ... conventional design documents consist of prose, static diagrams, and perhaps pseudo-code in an ad hoc untestable language. Such descriptions are far from precise; they are often ambiguous, or omit critical aspects such as partial failure or the granularity of concurrency (i.e. which constructs are assumed to be atomic).

I have noticed this divergence of reality and the design doc/diagrams in day-to-day engineering. What if we wrote something during that process of creating those beautiful diagrams and design docs - something that is more detailed and helps us down the line when we are trying to alter the system. That something turned out to be TLA+ for AWS.

> TLA+ is based on simple discrete math, i.e. basic set theory and predicates, with which all engineers are familiar. A TLA+ specification describes the set of all possible legal behaviors (execution traces) of a system.

> TLA+ is intended to make it as easy as possible to show that a system design correctly implements the desired correctness properties, either via conventional mathematical reasoning, or more easily and quickly by using tools such as the TLC model checker [5], a tool which takes a TLA+ specification and exhaustively checks the desired correctness properties across all of the possible execution traces.

> TLA+ is accompanied by a second language called PlusCal which is closer to a C-style programming language, but much more expressive as it uses TLA+ for expressions and values. In fact, PlusCal is intended to be a direct replacement for pseudo-code.




