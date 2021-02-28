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

I learned this technique from when I was working for [shippable.com](https://www.shippable.com/) - a lot of work and how things operate inside the company was based on Toyoto's manufacturing process. They used to even refer the term "Software Manufacturing" for the vision of what they want the product to do for software development.

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

## Last Principles

First of all, I made up this name "Last Principles" - because this is the opposite of the first principles mental model.

But very often useful. You are doing this when you are googling for something.

When faced with a problem, asking how will I solve it if I were to start from scratch is first principles. Instead, asking how has this problem been solved in various ways and using one of the ways is last principles.

Last principles are a very critical mental model to have. Because that's where the learning and experience happens. You get to see this awesome ways various people are solving the problem you have at hand. It might teach you the best practices and the knowledge that the field has accrued over time. 

oh! and probably save you a ton of time.

Reading a research paper is last principles. I love the way those papers build upon the knowledge from their reference papers. That reference section is last principles. Getting what I mean? :D 

## Regret Minimization

Popularised by Jeff Bezos - also has been mentioned in [Julian's post](https://www.julian.com/blog/mental-model-examples). 

Particularly helpful for taking big decisions. 

It is as simple as asking this question before undertaking big things:

"Will I regret not doing this when I am old?"

## Minus Five

This is a mental model that I learnt sometime back from [Sridhar Vembhu](https://en.wikipedia.org/wiki/Sridhar_Vembu). He has this advice for people wanting to bootstrap their own company, "Start from -5 years" - meaning start working for what you want to build 5 years before actually starting to build it. This includes saving up money for such a long period of time, gathering skillsets that you need for the business etc.

The core idea that I understand from the minus five mindset is that in-order to do anything substancially big in life, try to plan ahead and save up for those times. Because you don't want to enter the war zone unarmed.

## Measure them

Picked up this mental model from Vinod Khosla. Been using this for a few weeks now and I feel good about it.

I am linking the awesome talk below from where I learnt this.

<iframe width="560" height="315" src="https://www.youtube.com/embed/HZcXup7p5-8" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

The talk ends where he discusses about work-life balance. He firmly believes that it is achievable but we just have to be disciplined about it. Vinod Khosla seem to schedule his time into 15 minutes slots and even give appointments. Early on he had 20 main categories and each 15 minute time slot can belong to one of those categories. One of the important categories for him was "having dinner with family/kids" and he started by setting an impossible goal of 25 times per month and eventually achieved it in an year.

The key part is he had to do the tracking - measure how he spent his time in-order to make time.

So, if you are having this problem of "not finding enough time", start by measuring them. Once you measure how you spend time, it is way simpler to identify the fluff and be very self-aware about how you are spending time.

Bonus: I personally use 1 hour slots, as that is easy to track and gives me more focus by avoiding context switching often.
