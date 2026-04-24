---
title: Counting zeros
date: 2026-04-24 10:14:10
tags: ["systems-summer","mathematics","software","engineering"]
---
I have been giving myself the freedom and excuse to explore various software systems in my free time this summer. I am calling this: "Systems Summer", just so that I take it more seriously, and if anyone asks me what my current side project is, it would be this.

During that exploration, I realized that there is one underrated skill for an engineer: "counting the number of zeros in a number".

There is a cultural element to why I am calling this a skill. It is because all the software-related literature (books, RFCs, design docs, blog posts, papers, etc.) follows the International number system. I am from/in India, where we follow the Indian Number System. The international system is a 2-mark question in our grade/class 1. After that, I moved on to use the Indian number system for almost anything for the next 20 years - that includes all the numbers needed for my algebra, calculus, finance, economics, physics, and chemistry.

What does that mean?

Take a look at this number: 1000000 (That's six zeros if you are counting).

* A person practicing the International Number System
  * would write it as 1,000,000
  * would read it as 1 million
* A person practicing the Indian Number system
  * would write it as 10,00,000
  * would read it as 10 lakhs

I initially struggled to read software literature with numbers. If a blog post says we had 1 million users hit our servers at peak times, I would actually spend a few seconds in my mind trying to convert it and say, "Oh, they had 10 lakh users! That's great!"

Once, I was working at a startup where my primary task was to benchmark various KV stores to migrate the system to a store that could handle 10x load. That was my peak number struggling days. I was showing the numbers from a benchmark to the CTO. He sat down with me, and the first thing he started doing was counting zeros. (To my luck, he did it out loud)

> 1, 2, 3 - That is three zeros, that means a K. So this is 4K bytes.

And he goes,

> We have 3... 6 zeros. - That means a million. So this is 4M requests.

That is a turning point for me. Because you can understand things faster that way. I gave up on my "convert to Indian numerals to understand the impact" idea and instead embraced the idea that counting zeros is the way.

If you ask me how it looks in my brain now. It is as if there are two languages for mathematics. One I use to count money (this is the main use-case for the Indian number system for me), and another one I use to count numbers while working with computers.

Okay, so this is what you have to remember if you are coming from a similar cultural background:

* Count zeros
* 1000
  * 3 zeros
  * That is a thousand.
  * It has another name: Kilo - Kilobyte is one thousand bytes.
  * Instagram teenagers mean 4,000 when they say 4k
  * = 10<sup>3</sup>
* 1,000,000
  * 6 zeros
  * That is a million.
  * It has another name: Mega - Megabyte is one million bytes.
  * If an engineer says you have 1M rows in a table that is not indexed, you are in trouble.
  * = 10<sup>6</sup>
* 1,000,000,000
  * 9 zeros
  * That is a billion
  * It is denoted by Giga - Gigabyte is a thousand megabytes i.e., a billion bytes.
  * The world population is ~8.3 billion people as of mid-2026.
  * = 10<sup>9</sup>

~ ~ ~

That's enough zeros to get you a good mileage.

