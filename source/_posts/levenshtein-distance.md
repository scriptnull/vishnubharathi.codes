---
title: The Levenshtein distance in production
date: 2020-08-22 23:11:29
tags: ["algorithms", "programming", "open source"]
---

You might have heard about the [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance) while in college or while preparing for tech interviews. It is the famous [edit distance problem](https://leetcode.com/problems/edit-distance/). It is one of those must-try [Dynamic Programming](https://en.wikipedia.org/wiki/Dynamic_programming) challenges.

You still there? even after I said the words "Dynamic Programming"? haha. Good! Because unlike you, I am good at running away from it; most of the time. But I am kind of sitting down to learn + practice this stuff now.

[This amazing book](https://www.manning.com/books/grokking-algorithms) played a major role in making this topic a little less scary. What intrigued me the most is the spot where the author tries to explain some practical applications for dynamic programming.

Among all the applications I read there, two of them were practical and in-fact something that I use almost every day. One is in diff tools like `git diff` to compare text and another one is in spell checkers to figure out the closest matching words to the spelling we typed.

That's great! Those are some "open up and read the source code" kind of things. Guess what, I love those kinds of things. Instead of sinking into interview prep materials one after another, I might take this as a fun chance to learn some code that is used in the wild!

![missed hi5](https://media.giphy.com/media/xT1R9YSHqTHAuD9FyU/giphy.gif)

So let us learn about the problem, the way it is implemented in some open-source software (which are used by a lot of people - like a really really big number).

## Problem statement
I am going to copy-paste from Wikipedia to help me here.

>  the Levenshtein distance is a string metric for measuring the difference between two sequences

Basically, it is a way of comparing two strings.

> Informally, the Levenshtein distance between two words is the minimum number of single-character edits (insertions, deletions, or substitutions) required to change one word into the other.

Consider spell checkers. When you type something, the spell checking software should suggest you which is often a valid English word with a minimal Levenshtein distance.

## Git

Here is the cool thing: [Git](https://github.com/git/git) uses dynamic programming. Apart from the mention in that book regarding `git diff`, I found an elegant use-case of Levenshtein distance in some other part of git.

Here is how I found this out. I usually end up typing the git sub-commands wrongly at least once per day. Git would intelligently understand what I am trying to type and output a suggestion like this

![git-status](/images/git-status.png)

So, what is git doing here? It is just spell-checking the sub-command I typed in by comparing it against all the valid git sub-commands. Cool, at that point in time I was like "I think git might be using the Levenshtein distance to do this".

Then I started [greping "The most similar commands are"](https://github.com/git/git/search?q=The+most+similar+commands+are&unscoped_q=The+most+similar+commands+are) in the git source code to dig deep into the source code.

Bingo! Of course it uses the Levenshtein distance :)

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

One interesting thing that I noted is how _practical_ the code is. If we just see it as an interview prep thing, we might just write a recursive implementation and be done with it (which is usually simpler than writing an iterative approach). But in real-world a recursive approach might result in a stack overflow. Hence, an iterative approach to solving this problem is much more desirable.

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
  
  	//...........
	//...........

	i = row1[len2];
	free(row0);
	free(row1);
	free(row2);

	return i;
}
```

## Where else?
After a while of staring at git source code today with a little bit of struggle reading C and getting into all the details of the solution, I wanted to read the implementation in some other programs as well. There are lot of command-line tools and I have noticed a lot of the good ones support this spell check feature.

In fact this kind of functionality should typically be provided by the sub-command parsing cli library so that it is available more easily to cli writers. I was right again! Since I am into Go recently, I tried searching through a famous command line parser library for Go called [Cobra](https://github.com/spf13/cobra).

> Cobra is used in many Go projects such as Kubernetes, Hugo, and Github CLI to name a few

## Cobra
[Cobra](https://github.com/spf13/cobra) contains a reference to Levenshtein distance in the [README file](https://github.com/spf13/cobra#suggestions-when-unknown-command-happens).

![edit-distance-readme](/images/edit-distance-readme.png)

Cool, it even has the configuration to choose the distance based on which the suggestions should be picked.

Now, on to the source code. It is written as [a simple function](https://github.com/spf13/cobra/blob/993cc5372a05240dfd59e3ba952748b36b2cd117/cobra.go#L164).

```go
// ld compares two strings and returns the levenshtein distance between them.
func ld(s, t string, ignoreCase bool) int {
	if ignoreCase {
		s = strings.ToLower(s)
		t = strings.ToLower(t)
	}
	d := make([][]int, len(s)+1)
	for i := range d {
		d[i] = make([]int, len(t)+1)
	}
	for i := range d {
		d[i][0] = i
	}
	for j := range d[0] {
		d[0][j] = j
	}
	for j := 1; j <= len(t); j++ {
		for i := 1; i <= len(s); i++ {
			if s[i-1] == t[j-1] {
				d[i][j] = d[i-1][j-1]
			} else {
				min := d[i-1][j]
				if d[i][j-1] < min {
					min = d[i][j-1]
				}
				if d[i-1][j-1] < min {
					min = d[i-1][j-1]
				}
				d[i][j] = min + 1
			}
		}

	}
	return d[len(s)][len(t)]
}
```

It is an iterative solution. To understand it better, I copy-pasted the function onto the [Go playground](https://play.golang.org/) and started playing around with it.

```go
func main() {
	fmt.Printf("Edit distance = %d", ld("abc", "ac", true))
}
```

The answer correctly came up as 1. (just 1 deletion operation of b)

Now let me try to go line by line and try to figure out what is happening.

We accept two input strings `s` and `t`. We ignore the cases if the flag is set.

```go
if ignoreCase {
	s = strings.ToLower(s)
	t = strings.ToLower(t)
}
```

After that, we create a two-dimensional array called `d` to act as the memo table.

```go
d := make([][]int, len(s)+1)
for i := range d {
	d[i] = make([]int, len(t)+1)
}
```

Now to visualize things, I am adding a little function that prints the memo table.

```
   "  a  c 
"  0  0  0 
a  0  0  0 
b  0  0  0 
c  0  0  0 
```
 
 Next, we initialize the first column of every row with the value of the row index.
 
 ```go
for i := range d {
	d[i][0] = i
}
```

Now the table becomes

```
   "  a  c 
"  0  0  0 
a  1  0  0 
b  2  0  0 
c  3  0  0 
```

After that, we initialize the first row of every column to the value of the column index.
 
```go 
for j := range d[0] {
	d[0][j] = j
}
```

That yields

```
   "  a  c 
"  0  1  2 
a  1  0  0 
b  2  0  0 
c  3  0  0
```

That completes the base case: "When you start with an empty string and start building the strings, the operation count would just increase by one as it involves only one insertion operation.

Now, we start filling the inner parts of the table.

```go
for j := 1; j <= len(t); j++ {
	for i := 1; i <= len(s); i++ {
		// logic
	}
}
```

Ah nice, that felt so easy. If the row and column alphabet value are the same, then we don't need to perform any operation and hence we get to use the last counted operation value by looking at the diagonal.

```go
if s[i-1] == t[j-1] {
	d[i][j] = d[i-1][j-1]
} else {
	//....
}
```

For example: Here is the final table. Notice how `(a,a)` is filled up with looking at the diagonal `(",")`.

```
   "  a  c That is because, when the resulting string is already `a` there is no need to perform any 
"  0  1  2 
a  1  0  1 
b  2  1  1 
c  3  2  1 
```

If the alphabets differ, then we need to perform one of the operations (insert, remove, replace) to arrive at the desired alphabet. It seems like the way we figure out this is by finding the minimum of the adjacent cells (that are already filled) and adding 1 to it (to effectively say that we need to perform one more operation)

```go
min := d[i-1][j]
if d[i][j-1] < min {
	min = d[i][j-1]
}
if d[i-1][j-1] < min {
	min = d[i-1][j-1]
}
d[i][j] = min + 1
```

So, at last, we return the last cell of the matrix.

```go
return d[len(s)][len(t)]
```

It may not be obvious of what is going on especially in the last part of the code explanation above (apologies for not trying to explain that here). The recommendation for it is to watch/read some tutorial on how the memo table is filled up like this. The point of this explanation is to share how cleanly those ideas behind filling up the memo table is implemented in the library code.

## Closing
The main difficulty I feel here is the arrival of the idea behind the memo table. What should be the columns and rows? What should be the values that should be filled up in the cells? How do we compute the value of each cell?

Apart from the interview prep point of view, knowing these techniques (just knowing that these kinds of techniques exist in the world) can be a nice addition to one's problem-solving toolbox. The next time you are working on a cli app or some other app that needs spell check like suggestions, you know what to do!
