---
title: Exploring CUE
date: 2022-04-17 01:15:31
tags: ["programming"]
---

When I was working on [this project](https://hasura.io/blog/what-we-learnt-by-migrating-from-circleci-to-buildkite) at work, I wished to take a closer look at CUE. It seemed like a candidate for the project that we were undertaking. But we didn't endup choosing it at that time. We ended up using golang for writing our CI config - reasons: turing completeness, familiarty for the team, good tooling, easy for other teams to understand, and a great deal of support from the compiler.

But tonight, I would like to give a deep look at CUE. The main reason for my curiosity is the recently released [dagger](https://dagger.io) project. CUE seems to be at the center of this project. I hope I could understand the reason for that preference during my exploration here.

Also, I have been dabbling in this problem space for a long while. I know that the pain is real - That 2000 lines CI config written as YAML file, that 1800 lines [JSON schema](https://json-schema.org) file - I have edited them all. They have all hurt me! It is good to see projects emerging that acknowledge that this problem exists.


# CUE and its history

Time to borrow some quotes from CUE docs:

> CUE is an open-source data validation language and inference engine with its roots in logic programming. Although the language is not a general-purpose programming language, it has many applications, such as data validation, data templating, configuration, querying, code generation and even scripting

And here is the gist of where it came from:

> Although it is a very different language, the roots of CUE lie in GCL, the dominant configuration language in use at Google as of this writing. It was originally designed to configure Borg, the predecessor of Kubernetes.

CUE has a set of philosophy and principles, which I hope to revisit at the end of this blog post to get a better idea of how they are practically applied.


# Use-cases

Starting by reading - https://cuelang.org/docs/usecases/

## Configuration

The first line in docs - I love it <3

> Arguably, validation should be the foremost task of any configuration language. Most configuration languages, however, focus on boilerplate removal. CUE is different in that it takes the validation first stance.

One more point that I want to highlight is this:

> CUE basic operation merges configurations in a way that the outcome is always the same regardless of the order in which it is carried out (it is associative, commutative and idempotent).

This means that the order in which we write a config in the config file does not matter - pretty much like other config formats.

One of the cool things that CUE is doing which we don't see much in the wild is having "types" for the configuration. Like we mention types in a real programming language, we could use types in CUE to represent how the config should look like.

Example config from the docs example:

```cue
#Spec: {
  kind: string

  name: {
    first:   !=""  // must be specified and non-empty
    middle?: !=""  // optional, but must be non-empty when specified
    last:    !=""
  }

  // The minimum must be strictly smaller than the maximum and vice versa.
  minimum?: int & <maximum
  maximum?: int & >minimum
}
```

Now the above type called "Spec" could be used by the actual config like this

```cue
spec: #Spec
spec: {
  knid: "Homo Sapiens" // error, misspelled field

  name: first: "Jane"
  name: last:  "Doe"
}
```

