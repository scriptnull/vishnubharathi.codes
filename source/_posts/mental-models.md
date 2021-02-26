---
title: Mental Models
date: 2021-02-26 05:19:27
tags: ["life"," career advice"]
---

This post is inspired by [Julian's Mental Models](https://www.julian.com/blog/mental-model-examples). I will use the explanation in that blog post to explain what it is: 

> Mental models do two things: they help you assess how things work and they help you make better decisions.

Good! Secretly I have been using mental models for a long long time. It's just that I have never formalized and called it a name and probably forget about a model and move on to using/experimenting with some other model periodically. If you have a set of a thoughts that you base your actions upon, then that is a mental model for you. I would like to think about Mental models as predicates in discrete mathematics (sorry for the math-y reference, but just couldn't resist myself from adding it here :D)

I used to not care about mental models when there was a trend on Twitter where people write threads about it. I think it was mostly due to the fact that it was theory that was hard for me to follow through. So, I am going to stop explaining what mental models and try to write about some mental models that I personally use/trying-to-use/like.

## Five Whys

This mental model even has a [Wikipedia page](https://en.wikipedia.org/wiki/Five_whys) that describes about it nicely.

> The technique was originally developed by Sakichi Toyoda and was used within the Toyota Motor Corporation during the evolution of its manufacturing methodologies. It is a critical component of problem-solving training, delivered as part of the induction into the Toyota Production System.

I learned this technique from when I was working for [shippable.com](https://www.shippable.com/) - a lot of work and how things operate inside the company was based on Toyoto's manufacturing process. They used to even refer the term "Software Manufacturing" for the vision of where they want the product to do for software development.

Often times I have found myself get to the answer of the problem in less than 5 whys. Sometimes going and fixing all the whys may not be in your control. So, chillax and fix what is within your control.

The technique is simple: Just ask the question "why" five times when you are faced with a problem to find out the root-cause/real problem.

I use this technique till date to debug software. Infact we used it just yesterday at work to debug [this issue](https://github.com/hasura/graphql-engine/issues/6600).

Why did the UI showed the wrong version number? Because the base docker image sets an older version number.

Why is the base docker image setting an older version number? Because the CI build failed but continued anyway with a cached older image.

Why did the CI build fail but continue anyway? (found the bug in CI script that does not short-circuit on failure.)

Also did a parallel why based on the second answer.

Why did the CI build fail? Because there a command-line program that we used in the script was not found.

Why was the command-line program not found? Because the base image of the build image in CI changed to not have it.

......

I can go all day asking why. haha - but I should say that I kind of abuse this technique most of the time like stopping with 3 whys in interest of time and control. But that is fine and we just have to find peace somewhere, so this might as well be.

## First Principles

This was mentioned in [Julian's post](https://www.julian.com/blog/mental-model-examples) and is famously used by Elon Musk. I am sure that there is a good chance that you might be using it too. Because I had been quite a while.

Remember those moments at work where you feel nothing is working out. Then this one of the models to be used at those times.

"What if nothing existed about this problem and you were to build a solution for it completely from scratch?" 

Example: This software library does not have a feature or does not have the extensibility to add this feature. Ok! What if you wrote this library from scratch? What are your design decisions like in that case? Will your design accomodate the extensibility for the feature that you are aiming for?

This will try to sink you in deep thoughts - I mean the ones that you think about in shower and make you "forget if you applied soap to your legs" level of thought.


