---
title: rlwrap
date: 2018-12-12 11:31:36
tags: ["linux", "software"]
---

Two days back, I got to learn about a command line program called [rlwrap](https://github.com/hanslub42/rlwrap) - short for readline wrapper. This is the kind of software that I would like to write without knowing it already existed in this world. I am feeling very excited about rlwrap because the productivity that it brings to the table is massive.

I originally discovered it while trying to learn Common Lisp. `sbcl` is a common lisp implementation and it gives you a REPL to run lisp code.

![sbcl-repl](/images/sbcl-repl.png)

Most modern REPL implementations (example: Node.js REPL) maintain a history of already executed code and allows the programmers to reuse them by pressing UP arrow.

REPLs are for incremental thinking and coding. Example: if I executed (+ 1 2) first, then I would like to run a similar case to incrementally improve/test/think - in this case, I am checking (+ 1 3). Most of the contents of the latest command are already present in the previous command - `(+ 1 * )`

So, It is natural to just press the UP arrow and edit the previous command to check for the new case.

Unfortunately sbcl does not support this kind of command completion. So what do we do?

## Meet rlwrap

rlwrap could be used in combination with any program that gets input from the terminal.

### sbcl without rlwrap

![sbcl-without-rlwrap](/images/sbcl-without-rlwrap.gif)

### sbcl with rlwrap

![sbcl-with-rlwrap](/images/sbcl-with-rlwrap.gif)

## Use cases

After using rlwrap + sbcl, I felt that rlwrap is powerful and started thinking of various use cases in which it could come handy.

It could be used for getting history completion on any bash script that uses `read` or any program that gets input from standard input.

Consider the follow bash script

```bash
FIRST=""
LAST=""
USERNAME=""

echo "enter first name:"
read FIRST
echo "enter last name:"
read LAST
echo "enter user name:"
read USER

echo "First Name = $FIRST, Last Name = $LAST, User name = $USER"
```

### bash without rlwrap

![bash-without-rlwrap](/images/bash-without-rlwrap.gif)

### bash with rlwrap

![bash-with-rlwrap](/images/bash-with-rlwrap.gif)

### cat with rlwrap

If you often use `cat > file.txt` to create files quickly, try mixing it with rlwrap and suddenly you get to access the previous lines quickly with the press of the UP arrow.

![cat-fib](/images/cat-fib.gif)

Found more interesting use cases for rlwrap? Wait no more and tweet to me [@scriptnull](https://twitter.com/scriptnull). I would love to know how it helped you!
