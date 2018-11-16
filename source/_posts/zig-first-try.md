---
title: Zig Programming Language - First Try
date: 2018-11-16 18:58:56
tags: ["programming", "zig"]
---

I discovered [Zig](https://ziglang.org/) programming language yesterday while checking out [recurse center](https://www.recurse.com).

It aims to be a system programming language. Go, Rust, Crystal and now this. I have given all of them a try and I am always in the look out to explore more. So, here we go!

> Zig is an open-source programming language designed for robustness, optimality, and clarity.

If you haven't watched this amazing talk, check it out.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Z4oYSByyRak" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Zig is still in very early stages. Early stages like you won't even have syntax highlighting for code shared on this page and very primitive editor tooling.

So, if you have looked up to hack in developer tools, now is your time to steal the spot. (I am trying my best to steal one for me!)

## Install
```bash
# I am on a mac
# so using brew

brew install zig
```

## Hello World!

### import
To print "Hello World!" to stdout, we need to first import the `std` package. This could be achieved with [@import](https://ziglang.org/documentation/master/#import)

```zig
const std = @import("std");
```

Unfortunately, there is no standard library documentation in zig yet. So, if you wonder what could be imported, check out [this](https://github.com/ziglang/zig/tree/master/std), especially [this](https://github.com/ziglang/zig/blob/master/std/index.zig)

### main
As in many programming languages, Zig also starts execution from `main` function. So, define one

```zig
pub fn main() !void {
    var stdout = try std.io.getStdOut();
    try stdout.write("Hello World!\n");
}
```

Some points to notice here,
- `pub` - publish this function to the file importing the current file. Leaving this out made the `main` to be private and gives error.
- `try` - keyword is to denote that, the upcoming function call could result in an exception, which could be catched or rethrown. Excuse me for my terminology because I am not sure how these are called in Zig yet.
- `!void` - return type of the function `!` denotes possibility of error arising from this function.

### program

Here is the full program.

```zig
const std = @import("std");

pub fn main() !void {
    var stdout = try std.io.getStdOut();
    try stdout.write("Hello World!\n");
}
```

## Run
```bash
zig build-exe hello.zig

./hello
```

## Community
- IRC: `#zig` on Freenode ([Channel Logs](https://irclog.whitequark.org/zig/)) :: This is memorable for me, because this is the first time ever for me to chat on IRC.
- Reddit: [/r/zig](https://www.reddit.com/r/zig) :: Share your blog posts, questions, thoughts etc.
- Github Issues: [ziglang/zig](https://github.com/ziglang/zig/issues) :: Get to know about various proposals and pretty much everything.
- Email list: [ziglang@googlegroups.com](https://groups.google.com/forum/#!forum/ziglang) :: Not sure how active this is.

See you there!
