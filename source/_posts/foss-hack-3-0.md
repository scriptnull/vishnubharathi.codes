---
title: FOSS Hack 3.0
date: 2023-03-05 21:24:07
tags: ["life"," hackathon"]
---

After a long long time, I managed to attend a hackathon - [FOSS Hack 3.0](https://fossunited.org/fosshack/2023)

## Confession

I have a confession to make.

I have had a secret hackathon burnout all these years. The last time I attended a hackathon might have been in 2016 or 2017.

But this hackathon is different. I didn't face any burnout or pressure.

Instead, I just kept working on what I wanted to work on.

One of the things that I did differently in this event compared to my previous hackathons is to work on a project that I would use in the real world.

In my previous hackathons, I used to work on some random app(s) or game(s) which was far out of my reach. This time: I had a well-scoped and practical idea.

Besides, this hackathon is very special to me - because it is for building Open-source software. How cool is it! (dreamed about something like this to happen in India around 2013-14-ish timeline)

## And my new project is

I worked on a new project called [waymond](https://github.com/scriptnull/waymond) which I had been looking to get started on for a long time. I used the hackathon as an excuse to work on it 😀

> waymond is
> 
> - An open-source autoscaler.
> - Aiming to provide autoscaling for a wide variety of infrastructure.
> - Modular and extensible.
> - Built with Go.

The project's [README](https://github.com/scriptnull/waymond#readme) contains a good deal of information about the project if you are interested. If you find it useful/interesting, consider giving a 🌟 on [GitHub](https://github.com/scriptnull/waymond) - helps with my dopamine levels 😅

I got the chance to learn some Go and explore some libraries while working on the project. I want to share all my learnings here in this blog. At the same time, I would love to keep working and maintaining the project moving forward.

## Progress

I was able to make [v0.1.0 release](https://github.com/scriptnull/waymond/releases/tag/v0.1.0):
- Helped me arrive at a design for the system
- Helped me in prototyping a very basic use case
- Helped me to write the "core" parts of the software. (of course, I might most probably need to refactor it once I have a better understanding)
- Gave me the chance to write an elaborate README for the project

I already prepared a thin milestone [v0.2.0](https://github.com/scriptnull/waymond/milestone/1) for the project. The aim is to deploy it on real-world workloads (yeah, I do have them and will talk about it in detail once I am there)

## Demo

I also recorded a [small demo](https://youtu.be/DuKksePAJ_o) to show my progress so far (also needed to submit it at the end of the hackathon)

<iframe width="560" height="315" src="https://www.youtube.com/embed/DuKksePAJ_o" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Online and solo this time

It was happening both in-person and online. I attended it online, as I couldn't travel to Bangalore at the moment.

Also, I had to do some solo hacking this time. Because the project that I have been working on is in its very early stages and it would have been hard to collaborate with a team. (so, I didn't want to disturb my friends with lot of unknowns at this point.)

But I wished the opposite in both cases:
- I wished to attend it online.
- I wished to work on it with a team.

maybe next time!

But the good thing is I was able to make some decent progress on the project and it is already at an ok-ish level to accept Open Source contributions for it. So, if you are looking to contribute to an OSS project written in Go, then this is your chance! Take a look at the issue tracker [here](https://github.com/scriptnull/waymond/issues).

~ ~ ~ ~

I am still very shy to show my code, but it's a hackathon project - so I hope you wouldn't mind my 222 lines long `main.go` file.
