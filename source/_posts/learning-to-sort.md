---
title: Learning to sort
date: 2020-08-02 18:35:35
tags: ["algorithms","programming","data structures","go","tech interviews"]
---

Today, I am trying to learn about various sorting techniques in computing. I kind of procasinate over starting to learn about sorting whenever I am preparing for interviews. Mainly due to the fact that, we need to memorize the working of various soring algorithms. But over the time, I have came to a realization that each sorting algorithm is based on some intution and if we are able to understand those intutions, then it becomes easy to remember how they work.

One of my earliest attempts at learning about sorting algorithms is by writing [machinepack-sort](http://node-machine.org/machinepack-sort)

I am going to do a similar effort here, but this time I am planning to do these steps.
1. Understand and visualize how a sort algorithm works. (by reading blogs, seeing video tutorials and lectures)
1. Come up with the time and space complexity for each of them.
1. Write code and test the implementation using [this leetcode puzzle](https://leetcode.com/problems/sort-an-array/)
1. Try to find practical use cases for each algorithm.

I hope to document each of the above stages below.

# Preface
I will try to collect information that might clarify details for understanding the sorting algorithms in this section. A fair warning: we will also use this section to put some spoilers like "the commonly used sorting algorithm"

## 0,1
I think it is good to think about the very basic cases first and handle them at first. The very basic case is

When the list to be sorted has only one or zero elements, we just have to return back the list itself (because it is already sorted)

```go
func sortArray(nums []int) []int {
    if len(nums) < 2 {
        return nums
    }
    
    // implement sorting for n elements here
}
```

I think that some implementations try to embed this logic in the core logic itself, but anyway I would just like to make things simple and take one thing off from our table right away!

## Stable Sorting

## Non-decreasing order

# Sorting Algorithms

## Selection Sort
A very simple sorting technique. The reason it is called a selection sort is because we will __select__ the lowest/highest element at a time and place it in a sorted manner.

I think this example from [Wikipedia](https://en.wikipedia.org/wiki/Selection_sort) makes it clear

| Sorted sublist | Unsorted sublist | Least element in unsorted list |
|----------------|------------------|--------------------------------|
| () |	(11, 25, 12, 22, 64) | 11 |
| (11) | (25, 12, 22, 64) | 12 |
| (11, 12) | (25, 22, 64) | 22 |
| (11, 12, 22) | (25, 64) | 25 |
| (11, 12, 22, 25) | (64) |	64 |
| (11, 12, 22, 25, 64) | ()	

### Intution
So the intution here is to __select__ the lowest/highest number from the unsorted sublist and move it to sorted sublist.

### Time Complexity
Finding the the lowest/highest element takes O(n). This search needs to be done n times in-order to get the final answer.

The number of items to be searched decreases by one each time. First we search n items, then (n-1) items:

n + (n-1) + (n-2) + .... + 1 

Now it boils to simple math, "Sum of first n natural numbers" = (n*(n+1))/2 = (n<sup>2</sup> + n) / 2

Now omitting the constants and lower degree, we arrive at the time complexity.

__O(n<sup>2</sup>)__

### Space complexity

We move the lowest/highest element each time to a sorted sublist. The space complexity really depends on the way we allocate this sorted sublist.

If we create a new list and append the lowest/highest each time, then we will end up with n allocations. So __O(n)__.

But if we implement our code in a way to just swap the (n-1)<sup>th</sup> index for the n<sup>th</sup> lowest/highest element, we would end up doing everything in-place. So __O(1)__.

### Step by step Code

First we try to write down the logic for finding the lowest number (assume we need to do ascending order sort).

```go
func findSmallest(nums []int) int {
    smallest := nums[0]
    smallestIdx := 0

    for i := 1; i < len(nums); i++ {
        if nums[i] < smallest {
            smallest = nums[i]
            smallestIdx = i
        }
    }
 
    return smallestIdx
}
```

If we execute this n times, we will get back the same index. Our idea here is to reduce the length of the unsorted sublist being passed into the array, so that we get back the index of n<sup>th</sup> lowest item. So building up on that.

```go
func findSmallest(nums []int, start int) int {
    smallest := nums[start]
    smallestIdx := start
    
    for i := start; i < len(nums); i++ {
        if nums[i] < smallest {
            smallest = nums[i]
            smallestIdx = i
        }
    }
    
    return smallestIdx
}
```

Now, we just call the `findSmallest` procedure n times and do a swap everytime to construct the sorted sublist.

```go
func sortArray(nums []int) []int {    
    for i := 0; i < len(nums); i++ {
        smallestIdx := findSmallest(nums, i)
        nums[i], nums[smallestIdx] = nums[smallestIdx], nums[i]
    }
    
    return nums
}
```

### Full code

Now, we have a Space = O(1) and Time = O(n<sup>2</sup>) implementation here!

```go
func sortArray(nums []int) []int {    
    for i := 0; i < len(nums); i++ {
        smallestIdx := findSmallest(nums, i)
        nums[i], nums[smallestIdx] = nums[smallestIdx], nums[i]
    }
    
    return nums
}

func findSmallest(nums []int, start int) int {
    smallest := nums[start]
    smallestIdx := start
    
    for i := start; i < len(nums); i++ {
        if nums[i] < smallest {
            smallest = nums[i]
            smallestIdx = i
        }
    }
    
    return smallestIdx
}
```

### Resources
- [Wikipedia](https://en.wikipedia.org/wiki/Selection_sort)
- [Book: Grokking Algorithms: An illustrated guide for programmers and other curious people](https://learning.oreilly.com/library/view/grokking-algorithms-an/9781617292231/kindle_split_008.html)

## Bubble Sort

