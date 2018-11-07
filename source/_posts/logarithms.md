---
title: Logarithms
date: 2018-11-07 18:42:05
tags: ["mathematics"]
---

A few months back, I asked one of my programmer friends about the impact of Logarithms in analysing algorithms. I was particularly interested in knowing about the base of log for all the log notation used in algorithm analysis.

At the end of the phone call, I got into a state where `log` notation used in algorithm analysis is always base 2. Because it is computer science and we deal with 0s and 1s which is binary, hence log base 2. (Wrong, so wrong!)

I was not convinced though. I knew I am not understanding something very basic and as a result of which I could not ask more from him. From that point onwards, I was on the look out to understand logarithms and their application.

I read few pages of "The Algorithm Design Manual" by Steven S Skiena today. I was surprised to find "Logarithms and Their Applications" section in it which had some very useful insights in it.

> Logarithm is an anagram of algorithm, but that's not why we need to know what logarithms are.
>
> -- Steven S Skiena. The Algorithm Design Manual (Kindle Locations 649-650). Kindle Edition.

## Notations

First thing I learnt is the common notations of logarithms.

- `lg` means log base 2
- `log` means log base 10
- `ln` means log base e (natural logarithm, where e = 2.718)

ah, I always missed the subtle difference between `log` and `lg`.

`log` is the log I used in high school math. Remember those tiny books with lot of numbers and periodic table in it? It is mainly used to multiply two big numbers easily.

I had spent quite sometime helping my math professor in research works during college and I had often come across `ln` (and I was taught to read it as lawn).

## Trees

A rooted binary tree with height h has 2<sup>h</sup> leaves.

h = 1; 2<sup>h</sup> = 2<sup>1</sup> = 2 leaves
h = 2; 2<sup>h</sup> = 2<sup>2</sup> = 4 leaves
h = 3; 2<sup>h</sup> = 2<sup>3</sup> = 8 leaves

So, the formula to calculate the height of a binary tree from the number of leaves is log<sub>2</sub>n, where n = number of leaves.

Now consider, a tree with 3 nodes at each level instead of 2. If height is h, then the number of leaves is given by 3<sup>h</sup>

h = 1; 3<sup>h</sup> = 3<sup>1</sup> = 3 leaves
h = 2; 3<sup>h</sup> = 3<sup>2</sup> = 9 leaves
h = 3; 3<sup>h</sup> = 3<sup>3</sup> = 27 leaves

So, the formula to calculate the height of the tree with exactly 3 nodes at each level from the number of leaves is log<sub>3</sub>, where n = number of leaves.

## Binary Search

The runtime of binary search is O(log<sub>2</sub>n), when we split and search evenly with 2. An example discussed in the book demands for a 1/3 + 2/3 split while searching instead of 1/2 + 1/2 split.

By spending sometime on paper, I was able to arrive at the answer that the running time is now O(log<sub>3/2</sub>n).

How 3/2? (this is kind of hard to converse via writing, but I'll try)

In case of 1/2 + 1/2 split, in the worst case our binary search had only n/2, n/4,...1 remaining items to be searched, meaning that the items at each search point got reduced by 1/2 and hence the growth of the function is given by O(log<sub>2</sub>n) and the base 2 comes by reciprocating 1/2.

Applying the same thing to 1/3 + 2/3 split, in the worst case our search had only 2n/3, 4n/9,...1 remaining items to be searched, meaning that the items at each search point got reduced by 2/3 and hence the growth of the function is given by O(log<sub>3/2</sub>n) and the base 3/2 comes by reciprocating 2/3.

> The power of binary search comes from its logarithmic complexity, not the base of the log.
>
> -- Steven S Skiena. The Algorithm Design Manual (Kindle Location 715). Kindle Edition.

For example, a search on 1 million items using the above to strategies.

log<sub>3/2</sub>1,000,000 ≈ 35
log<sub>2</sub>1,000,000 ≈ 20

Note how the value is affected by the logarithmic function rather than the base.

## Conclusion

Coming back to the question "are all `log` in algorithm analysis log base 2?"

Answer is "most of the time it is, but there are cases where it could be anything else". To add more to this answer, the base of a logarithmic function is not as important as the logarithmic function itself, hence we tend to usually not denote the base in Big-oh notation.

## Properties

I also got to revise few interesting properties of logarithms.

log xy = log x + log y

log x<sup>y</sup> =  ylog x

The following is one of the interesting properties that I didn't notice for a long time.

log<sub>b</sub> a = log<sub>c</sub>a / log<sub>c</sub>b

Mainly because it could be useful to represent of a log value of particular base in terms of another base.

Surprisingly I found this code snippet on [JavaScript MDN reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/log).

```javascript
function getBaseLog(x, y) {
  return Math.log(y) / Math.log(x);
}

// Math.log uses natural logarithm.
```

This function applies the above principle to calculate the log value of any base in terms of base e.
