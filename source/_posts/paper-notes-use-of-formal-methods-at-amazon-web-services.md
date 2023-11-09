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

I have noticed this divergence between the reality and the design doc/diagrams in day-to-day engineering. What if we wrote something during that process of creating those beautiful diagrams and design docs - something that is more detailed and helps us down the line when we are trying to alter the system? That something turned out to be TLA+ for AWS.

> TLA+ is based on simple discrete math, i.e. basic set theory and predicates, with which all engineers are familiar. A TLA+ specification describes the set of all possible legal behaviors (execution traces) of a system.

> TLA+ is intended to make it as easy as possible to show that a system design correctly implements the desired correctness properties, either via conventional mathematical reasoning, or more easily and quickly by using tools such as the TLC model checker [5], a tool which takes a TLA+ specification and exhaustively checks the desired correctness properties across all of the possible execution traces.

> TLA+ is accompanied by a second language called PlusCal which is closer to a C-style programming language, but much more expressive as it uses TLA+ for expressions and values. In fact, PlusCal is intended to be a direct replacement for pseudo-code.

# The Value of Formal Methods for ‘Real-world Systems’

> In industry, formal methods have a reputation of requiring a huge amount of training and effort to verify a tiny piece of relatively straightforward code, so the return on investment is only justified in safety-critical domains such as medical systems and avionics. Our experience with TLA+ has shown that perception to be quite wrong.

Excellent, that is exactly what I needed to hear. They also provided this nice table of real world things:

![image](https://github.com/scriptnull/vishnubharathi.codes/assets/4211715/fc2e094e-f7b9-4e26-b139-c99d5cc7baf8)


# Side Benefit: A Better Way to Design Systems

> TLA+ has been helping us shift to a better way of designing systems. Engineers naturally focus on designing the ‘happy case’ for a system

and

> Once the design for the happy case is done, the engineer then tries to think of “what might go wrong?”, based on personal experience and that of colleagues and reviewers.
> .... Almost always, the engineer stops well short of handling ‘extremely rare’ combinations of events, as there are too many such scenarios to imagine.

and

> In contrast, when using formal specification we begin by precisely stating “what needs to go right?”
> ....
> - Safety properties: “what the system is allowed to do”
> - Liveness properties: “what the system must eventually do”

After we define those properties, we will need to see if those hold true for various kind of things that can happen in the system.

> Next, with the goal of confirming that our design correctly handles all of the dynamic events in the environment, we specify the effects of each of those possible events; e.g. network errors and repairs, disk errors, process crashes and restarts, data center failures and repairs, and actions by human operators.

So there should be a way to model these events in the system too. (The video that I mentioned at the top helped me digest this portion of the paper more easily)

> We have found this rigorous “what needs to go right?” approach to be significantly less error prone than the ad hoc “what might go wrong?” approach.

# More Side Benefits: Improved Understanding, Productivity and Innovation

> In several cases we have prevented subtle, serious bugs from reaching production. In other cases we have been able to make innovative performance optimizations – e.g. removing or narrowing locks, or weakening constraints on message ordering – which we would not have dared to do without having model checked those changes.

Awesome!

# What Formal Specification Is Not Good For

They are interested in two things

> 1) bugs and operator errors that cause a departure from the logical intent of the system, and
>
> 2) surprising ‘sustained emergent performance degradation’ of complex systems that inevitably contain feedback loops.

(1) is achievable via formal methods but not (2). They give a good example of what (2) would look like and they mention that they have other ways to mitigate those.

# First Steps To Formal Methods

This and the upcoming sections of the paper are well narrated and I felt like I was watching a documentary movie while reading these sections.

One another option that they were considering was [Alloy](https://en.wikipedia.org/wiki/Alloy_(specification_language)) as they found evidence of its usage.

> Zave used a language called Alloy to find serious bugs in the membership protocol of a distributed system called Chord. Chord was designed by a strong group at MIT and is certainly successful; it won a ’10-year test of time’ award at SIGCOMM 2011

But they chose TLA+ over Alloy as it was not as expressive as they needed it to be.

> Eventually C.N. stumbled across a language with those properties when he found a TLA+ specification in the appendix of a paper on a canonical algorithm in our problem domain: the Paxos consensus algorithm
>
> The fact that TLA+ was created by the designer of such a widely used algorithm gave us some confidence that TLA+ worked for real-world systems.

Yeah, TLA+ was invented by [Leslie Lamport](https://en.wikipedia.org/wiki/Leslie_Lamport) who given us with some of the coolest research that are getting used in a lot of stuff.

# First Big Success at Amazon

> T.R. says that, had he known about TLA+ before starting work on DynamoDB, he would have used it from the start. He believes that the investment he made in writing and checking the formal TLA+ specifications was both more reliable, and also less time consuming than the work he put into writing and checking his informal proofs.

# Persuading More Engineers Leads to Further Successes

Totally love this section. I would use the techniques mentioned here if I were to introduce formal methods and verification to other engineers.

> This raised a challenge; how to convey the purpose and benefits of formal methods to an audience of software engineers? Engineers think in terms of debugging rather than ‘verification’, so we called the presentation “Debugging Designs”

and

> Continuing that metaphor, we have found that software engineers more readily grasp the concept and practical value of TLA+ if we dub it:
>
> Exhaustively testable pseudo-code

One another thing that I saw that I didn't expect was

> Most recently we discovered that TLA+ is an excellent tool for data modeling, e.g. designing the schema for a relational or ‘No SQL’ database.

Wow, his helped them in coming up with a better schema!

# The Most Frequently Asked Question

> “How do we know that the executable code correctly implements the verified design?”

We don't, but

> Formal methods help engineers to get the design right, which is a necessary first step toward getting the code right. If the design is broken then the code is almost certainly broken, as mistakes during coding are extremely unlikely to compensate for mistakes in design. Worse, engineers will probably be deceived into believing that the code is ‘correct’ because it appears to correctly implement the (broken) design. Engineers are unlikely to realize that the design is incorrect while they are focusing on coding.

# Alternatives to TLA+

Seems like they published a whole other paper on this topic.

> When we found that TLA+ met those requirements, we stopped evaluating methods, as our goal was always practical engineering rather than an exhaustive survey.

# Conclusion

I hope you enjoyed this post and got the urge to explore and learn TLA+ - I feel this has the power to change the way we think and reason about our systems. I hope to write up more when I try to use it in real-world situations.

From here, I would like to read [this](https://brooker.co.za/blog/2013/01/20/two-phase.html) which was one of the references from that paper and try to learn and write TLA+ for something(s).

> Formal methods deal with models of systems, not the systems themselves, so the adage applies;
>
> “All models are wrong, some are useful.”

~ ~ ~

oh, and TLA is an acronym for [Temporal logic of actions](https://en.wikipedia.org/wiki/Temporal_logic_of_actions)
