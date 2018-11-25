---
title: My C++ Setup
date: 2018-11-24 20:07:16
tags: ["programming", "devops", "c++"]
---
## Prelude

I have been trying to write some C++ for the past few days. I was just exploring the standard library and modern C++ features. It has been going good so far, as I have been using C++ just to solve some puzzle questions on some sites. Now, I want to level up the game. I would like to write and understand some real world code with C++.

There are some factors that need to be in check while writing OSS or some real-world project in any programming language like formatting, testing, building and packaging etc. JavaScript taught me this well. It is filled with a lot of things like npm, grunt, gulp, webpack, babel, yarn, standard, es-lint, js-hint etc. to help programmers.

Most of the modern languages are starting to understand these needs and are coming up with official tools. This leads to lesser time spent on making decisions about the development environment. Example: go gives go-fmt for formatting your code, rust comes with cargo for dependency management. (Reminds me of [Zuckerberg's answer to why he wears the same colored T-shirt everyday](https://www.businessinsider.in/Heres-The-Real-Reason-Mark-Zuckerberg-Wears-The-Same-T-Shirt-Every-Day/articleshow/45064550.cms))

Unfortunately if you are writing C++ you need to sit down and create a build environment that works for you. This involves time and in my guess, it is the reason why not-so-many projects are bootstrapped with C++. Example: `npm init` is all I need for convincing me to bootstrap a project in JavaScript and from there I know that I could easily pull in all the tools I need to achieve the development environment I need.

## What do I need?
- Format code
- Produce executable
- Add dependency
- Run test
- Produce library

## CMake
CMake is build system generator, which is popular and being recommended by a lot of people in 2018.

- [Effective CMake](https://www.youtube.com/watch?v=bsXLMQ6WgIk)
- [Introduction to CMake](https://www.youtube.com/watch?v=jt3meXdP-QI)
- [How to create slides about CMake with CMake?](https://www.youtube.com/watch?v=sFH8IvPfHx0) : This one is short and interesting.

I have problems with CMake and I am not going to be secretive about it.

Learning curve is high for me as I feel that getting started guides and documentation of it is not sufficient enough. When you are trying to read the documentation for cmake, you will end up hitting the [man page](https://cmake.org/cmake/help/v3.12/manual/cmake.1.html) of it.

The man page, seriously? come on.

So, how do I learn CMake properly? "Buy a book that just costs 59.00$"

No, thanks.

I could feel that CMake is a powerful tool - power being in [generators](https://cmake.org/cmake/help/v3.0/manual/cmake-generators.7.html). It is even [Open Sourced](https://gitlab.kitware.com/cmake/cmake).

Another point is you need to learn its DSL to write CMake configuration file.

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Day 6 of <a href="https://twitter.com/hashtag/100DaysOfCode?src=hash&amp;ref_src=twsrc%5Etfw">#100DaysOfCode</a> <br><br>Learning about CMake. Coming from a place where `npm ...` does wonders, CMake feels complex. My first impression is learning a language for writing another language adds more barriers.<br><br>I just wish we had something simple.</p>&mdash; Vishnu Bharathi (@scriptnull) <a href="https://twitter.com/scriptnull/status/1065292039439466496?ref_src=twsrc%5Etfw">November 21, 2018</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

My take on this is "I don't need CMake now, but I might need it in future."

## Bazel
I met [Bazel](https://www.bazel.build/) while exploring [envoy](https://github.com/envoyproxy/envoy).

> {Fast, Correct} - Choose two
>
> Build and test software of any size, quickly and reliably

It is open sourced and has good OPEN documentation and getting started guides. Another interesting feature for me is ["One tool, multiple languages"](https://www.bazel.build/#one-tool-multiple-languages).

Check out [this](https://blog.envoyproxy.io/external-c-dependency-management-in-bazel-dd37477422f5) cool blog post from envoy talking about how they use bazel.

I am going to give it a try.

### Install
I am on macOS. So going with brew.

```sh
brew tap bazelbuild/tap
brew tap-pin bazelbuild/tap
brew install bazel
```

### WORKSPACE and BUILD
A bazel project makes use of two files WORKSPACE and BUILD.

To start a bazel workspace,

```sh
touch WORKSPACE
```

Empty file, huh? not much use? nope. To my surprise this WORKSPACE file could be super powerful. I just realized it after seeing the [workspace rules](https://docs.bazel.build/versions/master/be/workspace.html)

The project could have one or more BUILD files inside, helping bazel to figure out how to build the particular directory.

> Each instance of a build rule in the BUILD file is called a target

```
cc_binary(
    name = "hello-world",
    srcs = ["hello-world.cc"],
)
```

`cc_binary` is the rule and `hello-world` is the target. For the full list of available rules check out [this bazel docs page](https://docs.bazel.build/versions/master/be/c-cpp.html).


To run the `hello-world` target,
```sh
# run from WORKSPACE root
bazel build //main:hello-world
```

This outputs the binary in `bazel-bin` folder.

I recommended following [this tutorial about bazel](https://docs.bazel.build/versions/master/tutorial/cpp.html) if you are interested in learning more about it.

## Format code
After investigating, I came across `clang-format` - a tool to format C++ code. There are also other interesting tools and ideas for tools on [this Clang documentation page](https://clang.llvm.org/docs/ClangTools.html).

Some open source projects that use `clang-format` are envoy and electron. In fact, electron even has this [nice documentation](https://electronjs.org/docs/development/clang-format) on getting started with it.

```sh
npm install -g clang-format

# run this to format
clang-format -i **/*.cpp

# run clang-format on git added files
git-clang-format
```

## Produce executable
Since we are using bazel, this is as simple as adding a new package called main and using `cc_binary` rule in it.

```
.
├── README.md
├── WORKSPACE
└── main
    ├── BUILD
    └── app.cpp
```

Add the following rule to `main/BUILD`

```
cc_binary(
    name = "app",
    srcs = ["app.cpp"]
)
```

To build the package and run the app
```sh
bazel build //main:app

./bazel-bin/main/app
```

## Add dependency
This page about [managing external dependencies](https://docs.bazel.build/external.html) with bazel is quite useful. My best guess is that I will be trying to add non-bazel projects as third party-dependencies most of the time.

Let me try adding a testing library called catch2. First step is adding the git repository as needed artifact in the WORKSPACE file.

```
load("@bazel_tools//tools/build_defs/repo:git.bzl", "new_git_repository")
new_git_repository(
    name = "catch2",
    remote = "https://github.com/catchorg/catch2.git",
    tag = "v2.4.2",
    build_file_content="""
cc_library(
    name = "catch2",
    hdrs = ["single_include/catch2/catch.hpp"],
    visibility = ["//visibility:public"],
)
"""
)
```

Next step is adding catch2 as dependency in the tests target.

```
cc_test(
    name = "factorial",
    srcs = [
        "factorial.cpp"
    ],
    copts = ["-Iexternal/catch2/single_include/catch2"],
    deps = [
        "@catch2//:catch2"
    ],
)
```

And our test file would look like

```cpp
#define CATCH_CONFIG_MAIN
#include "catch.hpp"

unsigned int Factorial( unsigned int number ) {
    return number <= 1 ? number : Factorial(number-1)*number;
}

TEST_CASE( "Factorials are computed", "[factorial]" ) {
    REQUIRE( Factorial(1) == 1 );
    REQUIRE( Factorial(2) == 2 );
    REQUIRE( Factorial(3) == 6 );
    REQUIRE( Factorial(10) == 3628800 );
}
```

woof! I spend quite few hours trying to figure this out! But finally, I got it working.

My first iteration made me to specify the header file like this

```cpp
#include "external/catch2/single_include/catch2/catch.hpp"
```

`copts` to the rescue and now the header is accessible just as

```cpp
#include "catch.hpp"
```

Now that we have added a library as dependency for `cc_test`, the process would be same for `cc_binary` and `cc_library`.

## Run test

`bazel test` command is used to run tests.

```sh
# Run tests
bazel test //test:factorial

# Run tests and output information in stdout
bazel test //test:factorial --test_output=all

# Run all test targets
bazel test //test:* --test_output=all
```

## Produce library
By this time, we should have encountered `cc_library` rule a couple of times. Yep! It could be used to produce libraries that are consumable by other projects.

An example [straight from the docs](https://docs.bazel.build/versions/master/cpp-use-cases.html#using-transitive-includes)

```
cc_library(
    name = "sandwich",
    srcs = ["sandwich.cc"],
    hdrs = ["sandwich.h"],
    deps = [":bread"],
)

cc_library(
    name = "bread",
    srcs = ["bread.cc"],
    hdrs = ["bread.h"],
    deps = [":flour"],
)

cc_library(
    name = "flour",
    srcs = ["flour.cc"],
    hdrs = ["flour.h"],
)
```

## Conclusion

Finally, I am kind of peaceful about what I got done here. But I am on the look out for other options too. For example, in the middle of this I gave up on bazel once and checked out ninja for sometime (haha). But then I already invested in some amount of complexity already that is too hard to ignore and move on.

I also hope that C++20 modules would remove away a lot of complexity and make things easier.
