---
title: The Levenshtein distance in production
date: 2020-08-22 23:11:29
tags: ["algorithms", "programming", "open source"]
---

You might have heard about the [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance) while in college or while preparing for tech interviews. It is the famous [edit distance problem](https://leetcode.com/problems/edit-distance/). It is one of those must-try [Dynamic Programming](https://en.wikipedia.org/wiki/Dynamic_programming) challenges.

You still there? even after I said the words "Dynamic Programming"? haha. Good! Because unlike you I am good at running away from it; most of the time. But I am kind of sitting down to learn + practice this stuff now.

[This amazing book](https://www.manning.com/books/grokking-algorithms) played a major role in making this topic a little less scary. What intriguied me the most is the spot where the author tries to explain some practical application for dynamic programming.

Among all the applications I read there, two of them were practical and in-fact something that I use almost everyday. One is in diff tools like `git diff` to compare text and another one is in spell checkers to figure out the closest matching words to the spelling we typed.

That's great! Those are some "open up and read the source code" kind of things. Guess what, I love those kind of things. Instead of sinking into inteview prep materials one after another, I might take this as a fun chance to actually learn some code that is actually used in the wild!

![missed hi5](https://media.giphy.com/media/xT1R9YSHqTHAuD9FyU/giphy.gif)

So let us learn about the problem, the way it is implemented in some open source software (which are used by a lot of people - like a really really big number).

## Problem statement

I am going to copy-paste from wikipedia to help with me here.

>  the Levenshtein distance is a string metric for measuring the difference between two sequences

Basically it is a way of comparing two strings.

> Informally, the Levenshtein distance between two words is the minimum number of single-character edits (insertions, deletions or substitutions) required to change one word into the other.

Consider spell checkers. When you type something, the spell checking software should suggest you which is often a valid english word with a minimal Levenshtein distance.

## Git

Here is the cool thing: [Git](https://github.com/git/git) uses dynamic programming. Apart from the mention in that book regarding `git diff`, I found an elegant use-case of Levenshtein distance in some other part of git.

Here is how I found this out. I usually end up typing the git sub-commands wrongly at least once per day. Git would intelligently understand what I am trying to type and output a suggestion like this

![git-status](/images/git-status.png)

So, what is git doing here? It is just spell checking the sub-command I typed in by comparing it against all the valid git sub-commands. cool, at that point of time I was like "I think git might be using the Levenshtein distance to do this".

Then I started [greping "The most similar commands are"](https://github.com/git/git/search?q=The+most+similar+commands+are&unscoped_q=The+most+similar+commands+are) in the git source code to dig deep into the source code.

Bingo! Ofcourse it uses the Levenshtein distance :)

```c
int levenshtein(const char *string1, const char *string2,
	int swap_penalty, int substitution_penalty,
	int insertion_penalty, int deletion_penalty);
```

Here is the [header file](https://github.com/git/git/blob/53f9a3e157dbbc901a02ac2c73346d375e24978c/levenshtein.h) that declares the function and the [c implementation of the logic](https://github.com/git/git/blob/53f9a3e157dbbc901a02ac2c73346d375e24978c/levenshtein.c).

It gets called in [help.c](https://github.com/git/git/blob/4f0a8be78499454eac3985b6e7e144b8376ab0a5/help.c#L514-L623), the source file responsible for showing help message in git.

The function first loads all the valid sub-commands of git (including the aliases we have - just knew this fact while digging the source).

```c
	load_command_list("git-", &main_cmds, &other_cmds);

	add_cmd_list(&main_cmds, &aliases);
	add_cmd_list(&main_cmds, &other_cmds);
	QSORT(main_cmds.names, main_cmds.cnt, cmdname_compare);
	uniq(&main_cmds);
```

After that, it computes the Levenshtein distance and decides which command to suggest.

One interesting thing that I noted is how _practical_ the code is. If we just see it as a interview prep thing, we might just write a recursive implementation and be done with it (which is usually simpler than writing an iterative approach). But in real-world a recursive approach might result in a stack overflow. Hence, an iterative approach to solving this problem is much more desirable.

Also, see the level of optimization, they do! A comment from the source below:

```
 * The idea is to build a distance matrix for the substrings of both
 * strings.  To avoid a large space complexity, only the last three rows
 * are kept in memory (if swaps had the same or higher cost as one deletion
 * plus one insertion, only two rows would be needed).
 ```
 
 At any given point of time, they are just using 3 rows of the memo table to figure out the answer, instead of keeping the entire memo table in memory.
 
 ```c
int levenshtein(const char *string1, const char *string2,
		int w, int s, int a, int d)
{
	int len1 = strlen(string1), len2 = strlen(string2);
	int *row0, *row1, *row2;
	int i, j;

	ALLOC_ARRAY(row0, len2 + 1);
	ALLOC_ARRAY(row1, len2 + 1);
	ALLOC_ARRAY(row2, len2 + 1);
  
  // Do DP logic

	i = row1[len2];
	free(row0);
	free(row1);
	free(row2);

	return i;
}
```
