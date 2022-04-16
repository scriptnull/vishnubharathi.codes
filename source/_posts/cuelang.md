---
title: Exploring CUE
date: 2022-04-17 01:15:31
tags: ["programming"]
---

When I was working on [this project](https://hasura.io/blog/what-we-learnt-by-migrating-from-circleci-to-buildkite) at work, I wished to take a closer look at CUE. It seemed like a candidate for the project that we were undertaking. At the end, we ended up using golang for various reasons: turing completeness, familiarty for the team, good tooling, easy for other teams to understand, and a great deal of support from the compiler.

But tonight, I would like to give a deep look at CUE. The main reason for my curiosity is the recently released [dagger](https://dagger.io) project. CUE seems to be at the center of this project. I hope I could understand the reason for that preference during my exploration here.

