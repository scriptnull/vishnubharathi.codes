---
title: First feedback
date: 2020-07-20 13:27:19
tags: ["interviewing"]
---

I just got off from a call where I gathered feedback about my interview with a company. I didn't pass the interview, but the feedback of why I failed is making have an immense smile in my face for the past hour.

This is the first company that I applied after I lost my job a few days back. So, this is the _first feedback_ that I got in that sense. I think writing it down here would give me a solid place to refer to on a regular basis to up my game!

The feedback call was between me and the CTO of the company. Whenever I find myself talking to CEOs, CTOs and VPs (and some Engineers), I seem to get immense amount of "You are playing a different game, so game on!" level of energy from the conversation. This is nonetheless different. The way things were put infront of me is actually something helpful that I could act upon.

## Background
To give background, here is how the interview process went. It is an early-stage startup, recently funded, super-interesting to me (as it is in the Reliability, Observability space). I saw their CTO's tweet that they are hiring.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">We (<a href="https://twitter.com/last9inc?ref_src=twsrc%5Etfw">@last9inc</a>) are looking for a Software Engineer who can _own_ our Reliability + Customer Integration pipeline. <br><br>Key requisites are: Strong *nix skills, and being able to think ahead and automate mundane / repetitive work.<br><br>If that&#39;s not you, help spread the word 🙏</p>&mdash; Piyush Verma (@realmeson10) <a href="https://twitter.com/realmeson10/status/1273551418448740352?ref_src=twsrc%5Etfw">June 18, 2020</a></blockquote>

After doing my homework on what they are trying to do, I arrived at one of their interesting projects which is open source - https://github.com/last9/k8stream

Now I am fully convinced that I should definitely apply to them! `k8stream` was written in Go, which I am currently focusing on. So I thought it might be good to contribute a feature to the project, that way I get a little bit better in Go programming and also it would help me break the ice with them while applying!

It is a project that uploads various kuberenetes events to AWS S3. It had this notion of Sink, which lets you store the data. For example, there was file sink and AWS sink. You can choose the sink in which your events should get stored. My initial idea was to add a GCS sink, which would enable storing events in Google Cloud storage. During the "exploring by reading the code" phase, I happened to notice a `TODO` comment in the code base and I felt it would be more valuable to address it rather than sending code for feature that I wasn't sure if they are interested in having in the software. So, here it is: https://github.com/last9/k8stream/pull/38 - a PR to validate input in file sink!

One of the other reasons for not going with GCS feature is that I didn't have clear idea about how to use `context` package in Go (this package was used extensively by the google cloud Go library). So, I did spin off understanding it parallely during the process and ended up [digging deep into the source code of context package and writing a blog post about it](/blog/go-contexts/)

After sending in a hello email with a pointer to my PR, I was able to get an interview from them. It involved a introduction/get-to-know-each-other call followed by a take home assignment.

The call went well. Then I wrote and submitted the take-home assignment in a week. I chose Go as my programming language (as I was learning it and I thought it would be a fun exercise).

I learnt that I was rejected in some days after the assignment and after a week, I was able to get the CTO on call for a feedback session. 

## Good things
Always start with the good things! A few things that they thought I was good at.

- Good hands on
