---
title: Language server for Zig
tags: ["programming", "zig"]
---

After trying to write [hello world Zig program](/blog/zig-first-try/) on VS Code, I found that it just has very primitive support - just basic syntax highlighting.

Also there is no documentation for standard library at this point. I was troubled to switch back and forth between github source for standard library and my editor. Having autocomplete would really be helpful here.

Ok, how to get it?

Well, build it.

[Language Server Protocol](https://microsoft.github.io/language-server-protocol/) helps editors to populate autocomplete, go to definition etc.

Now, we just need to build a Language Server for Zig, in C++ or Zig. I don't about it yet. Let me give it a try.
