---
title: Paper notes: Use of Formal Methods at Amazon Web Services
date: 2023-11-09 03:56:53
tags: ["research papers"]
---

It has been a while that I posted paper notes or anything at all in this blog. Luckily, I got curious last night about "How are distributed systems tested?". My curiosity was evoked by these factors:
- I keep on hearing about "Deterministic Simulation Testing" used in the [TigerBeetle](https://github.com/tigerbeetle/tigerbeetle) project. I wonder what is it (haven't explored it yet) and what are the other methods to test distributed systems.
- I have been wanting to add "High Availability" modes in [my little side project](https://github.com/scriptnull/waymond) and I wanted to understand how to test the high availability of the system before declaring it to be highly available :D
- Maybe there are some lessons that I can take away for designing and implementing different testing strategies at [my current work](https://hasura.io/).

With those very good enough reasons, I stumbled upon [this awesome github repo](https://github.com/asatarin/testing-distributed-systems) which curates various testing strategies for distributed systems. One of the things that stood out for me in that list was "Formal methods", more specifically "TLA+". It then led me to watch [this awesome conference video](https://youtu.be/sPSPEgz3o9U?si=oyvODVhHCr5l7ZnQ) where they compare TLA+ and [Jepsen](https://jepsen.io/)/[maelstrom](https://github.com/jepsen-io/maelstrom) - the video made me feel excited about both the technologies. Quick lesson from the video: TLA+ is apples and Jepsen is oranges - we would ideally want to eat both.

I then decided to learn more about TLA+ since that comes in the earlier stages of the design process. I have previously attempted to learn TLA+ but couldn't succeed in it successfully - mainly due to a lack of motivation in the middle of the learning process. So, I wanted to be motivated enough this time before attempting to learn it again and try to use it in my side project or at work. This line of thinking made me remember that AWS had published a paper about TLA+ that I had heard of in the past. So I decided to pick it up and read it.

You can get a copy of it from [here](https://www.amazon.science/publications/how-amazon-web-services-uses-formal-methods)https://www.amazon.science/publications/how-amazon-web-services-uses-formal-methods.
