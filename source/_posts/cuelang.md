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

### Types

One of the cool things that CUE is doing which we don't see much in the wild is having "types" for the configuration. Like we mention types in a real programming language, we could use types in CUE to represent how the config should look like. I guess this in turn will be used by the tooling to validate the config.

Example config from the docs:

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

### Boilerplate and Inheritance

Copy pasting a hundrend lines of config (boilerplate) to add or edit one line of config - done that ✔️

Opening a random file with 2 lines of config and wondering "what does this even do 🤔" - done that ✔️ (because the actual config that contains most of the config is placed in a different file and is _inherited_ to this config file to reduce boilerplate)

CUE is a config language, so obivously there is a mechanism to avoid boilerplate but this point sounds particularly interesting:

> Like with other configuration languages, CUE can add complexity if values are organized to come from multiple places. However, as CUE disallows overrides, deep layerings are naturally prevented.

CUE disallows overrides - want to see a practical example of this. Forgetting to override values in an inherited config file is a great way to do something bad in production systems; if the default value is not good enough, then forgetting to override that default value might easily cause troubles. Example: default config setting of a container has memory limit as 256mb but the application running in the container needs 512mb of memory to function properly; if the author of that application forgets to override, then that would impact the application when it is trying to run - often silently after deploying to prod :D  Does CUE help us combat this problem? I will continue reading for now and wait to know.

> Inheritance, is not commutative and idempotent in the general case. In other words, order matters. This makes it hard to track where values are coming from. This is not only true for humans, but also machines.

### Other config languages

Some notes from the docs with comparison to other config languages:

> Like Jsonnet, CUE is a superset of JSON

> CUE’s focus is data validation whereas Jsonnet focuses on data templating (boilerplate removal). Jsonnet was not designed with validation in mind.

Here comes HCL (one of my favorite config languages):

> HCL has some striking similarities with GCL. But whether this was a coincidence or deliberate, it removes the core source of complexity of GCL: inheritance.

> Also, whether the removal of inheritance was a coincidence or great insight, there is no construct given in return that one might need for larger scale configuration management. This means the use of HCL may hit a ceiling for medium to larger setups.

## Data Validation

### Validating YAML and JSON

one of the neat things about CUE is that it tries to play a bit nice with YAML and JSON whenever possible. A great example is how CUE could be used as a way to validate already existing YAML or JSON configurations.

I installed `cue` tool on my machine at this point and thought of re-writing the example from docs to practice CUE.

```
$ cue vet --help 
vet validates CUE and other data files

By default it will only validate if there are no errors.
The -c validates that all regular fields are concrete.


Checking non-CUE files

Vet can also check non-CUE files. The following file formats are
currently supported:

  Format       Extensions
	JSON       .json .jsonl .ndjson
	YAML       .yaml .yml
	TEXT       .txt  (validate a single string value)

To activate this mode, the non-cue files must be explicitly mentioned on the
command line. There must also be at least one CUE file to hold the constraints.
```


Let us consider a YAML config that is absurd.

```yaml
min: 10
max: 5
```

Equivalent JSON file:

```json
{
  "min": 10,
  "max": 5
}
```

The above config is absurd because "min" is greater than "max" - what a contradiction! It seems like we could write a CUE file to check for these kind of mistakes:

```cue
min: *0 | number
max: number & >min
```

After writing the CUE check, we could vet it like this

```
$ cue vet check.cue range.json range.yaml 
max: invalid value 5 (out of bound >10):
    ./check.cue:2:15
    ./range.json:3:10
```

The above command first validates the JSON file and throws the error at that point and STOPs without showing the error for YAML file (Why so? Why can't it continue? - maybe I will discover it afterwards)

Fixing the error in JSON file and retrying `cue vet` shows the problem in the YAML file.

## Schema Definition

I have written JSON Schmema in the past to define the structure of how the configuration should look like. It also helps in validation of the configuration. JSON Schema becomes very complex at scale. When you are past some point, it becomes very difficult digest it.


CUE feels more readable than JSON Schema in the first look so far.

If we write Schema in CUE, there is a way to check if `v2` of schema is backwards-compatible with `v1` of the schema. [This example](https://cuelang.org/docs/usecases/datadef/#validating-backwards-compatibility) in the docs describes it very neatly. I guess there is a potential to use this to enhance tooling for all of us here.

