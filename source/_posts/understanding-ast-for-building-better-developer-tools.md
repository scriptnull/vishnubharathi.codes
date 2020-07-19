---
title: Understanding AST for building better developer tools
date: 2017-08-02 04:00:00
tags: ["software", "programming"]
---
If you had used a full fledged IDE like Visual Studio, Eclipse, Android Studio etc. you may have noticed features like code completion, linters etc.

![Code completion in VS Code](https://cdn-images-1.medium.com/max/2000/1*AzXU42cs7MUtW5ZuMX6vpg.png)*Code completion in VS Code*

![Code linting in VS Code](https://cdn-images-1.medium.com/max/2000/1*AevLZ5XepOaLNrhZmWRMTA.png)*Code linting in VS Code*

These are pretty amazing features, that help a lot. I always wonder how these kind of tools work?

Seems like the answer is pretty simple. They all use [Abstract Syntax Tree (AST)](https://en.wikipedia.org/wiki/Abstract_syntax_tree).

That’s interesting, because I have taken a “Compiler Design” course in college and seem to have come across the term throughout the course. But never really got to see it in action.

So, I decided to jump a bit and explore.

<iframe src="https://medium.com/media/32d528fe3448b395032630a34fae30de" frameborder=0></iframe>

### What is AST?

Abstract is not having a concrete form. Syntax is the structure of code. Tree is a data structure.

When the compiler tries to compile the source code, it does it [phase by phase](https://www.tutorialspoint.com/compiler_design/compiler_design_phases_of_compiler.htm). First, the compiler generates tokens from the source code. Then it forms a tree with the tokens generated previously. This help us in removing inessential data like punctuation marks, spaces etc. and help the compiler to just focus on the important things. Yay! [No more “Tabs Vs Spaces”](https://www.youtube.com/watch?v=SsoOG6ZeyUI).

Feel free to dive deep on the [Wikipedia](https://en.wikipedia.org/wiki/Abstract_syntax_tree) Page.

### Compilers and AST

One thing to note is if there is some error, compiler uses the information in the AST to report where the error exists to the user. Thats freaking awesome. All the error messages that I see while compiling my code is actually being generated with the help of AST.

### Developer tools and AST

Do we have to wait for the compiler to report errors in our code. Couldn’t we just make our code editor catch those silly errors and show to them while typing the code. If the IDE program or editor plugin could generate the tool AST by themselves, when the user types in the code, this could be possible.

So, my initial guess is that generating ASTs alone inside the developer tools could help a lot in accessing various information related to the code that user writes.

### Practice

So, I wanted to play around with ASTs practically. Recently, I have been trying to program in Go programming language. I came across this tool called [gosimple](https://github.com/dominikh/go-tools/tree/master/cmd/gosimple). It is a linter that provides suggestion for simplifying the code.

I saw some of the open tasks welcoming contribution in the issue tracker of that tool. So, I decided to [pick one](https://github.com/dominikh/go-tools/issues/67) and started working on it. May be this will help me unveil the truth.

Yes. It did. Seems like gosimple uses the inbuilt [go/ast package](https://golang.org/pkg/go/ast/) provided by Go standard library. The same package is being used by the Go parser to build Go source code.

A tree is built of nodes. In go/ast, the tree is built on top three kinds of nodes.
> There are 3 main classes of nodes: Expressions and type nodes, statement nodes, and declaration nodes. — [go/ast source code commen](https://github.com/golang/go/blob/master/src/go/ast/ast.go#L20)t

Once I learnt about the basic node types, it was easy for me to write the [linting rule for gosimple, that I was working on.](https://github.com/dominikh/go-tools/issues/67) gosimple traverses the AST in a depth-first order and checks for the satisfaction of a linting rule at every node. If the node matches the preconditions, the linting rule is run and we return a boolean representing to allow traversal further down.

Cool! I sat down to write some code and here it is
[**simple: adds S1031 LintNilCheckAroundRange by scriptnull · Pull Request #148 · dominikh/go-tools**
*Fixes #67 I am relatively new to manipulating AST and this code base. So, please take a look at the code and let me…*github.com](https://github.com/dominikh/go-tools/pull/148)

Its still in review phase at the time of writing this post. So, let me wait and see how things turn out. But overall, it was fun to read, understand and write code with ASTs.

Thanks for reading. I quote verses from my favourite Tamil literature “[Tirukkuṛaḷ](https://en.wikipedia.org/wiki/Tirukku%E1%B9%9Ba%E1%B8%B7)” at the end of my blog posts.
> # “அடுக்கி வரினும் அழிவிலான் உற்ற
> # இடுக்கண் இடுக்கட் படும்.”
> # *— திருக்குறள்*

Translated meaning (in my words): When a man tries to overcome his sorrows in life constantly, the sorrows will become sorrowful in front of him and eventually fade away.

