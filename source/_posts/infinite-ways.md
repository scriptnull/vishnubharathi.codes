---
title: Infinite ways
date: 2024-01-13 04:10:00
tags: ["mathematics"]
---

I was reading through the [Specifying systems](https://lamport.azurewebsites.net/tla/book-21-07-04.pdf) book few hours back where I came across this beautiful insight.

> Mathematics provides infinitely many ways of expressing the same thing

Take the number 12. There are infinite number of ways to express it.

expr 1) 6 + 6

expr 2) 3 * 4

expr 3) 141 - 129

expr 4) 4353475 - (4353462 + 1)

All the above expressions evaluate to 12. When options are infinte, how to express something?

The same question applies to writing formal specifications and programming.

The advice from the book is simple:

> ..., then you can choose the one that you feel makes the specification easiest to understand.

Yes, choose the one that makes it the easiest to READ it at a future point.

Example: Someone might find it OKAY to choose (expr 3) above to express 12. Reason behind it being, "come on, it is not that complex!". Especially it is not as complex as (expr 4). But when others (or the same person) read it at a future point in time, they might wonder, "why didn't we choose (expr 1) or (expr 2)".

I have seen the equivalent of this happening in programming.

My advice for anyone (especially if you are getting started with programming and are in that phase where you get excited about different programming languages and their features) would be:

If there are two ways to express something, choose the one that will be the easiest to read and understand at a future point in time by a human and not the compiler.

~ ~ ~ ~

Optimize for reads, when writing.
