---
title: Learning to sort
date: 2020-08-02 18:35:35
tags: ["algorithms","programming","data structures","go","tech interviews"]
---

Today, I am trying to learn about various sorting techniques in computing. I kind of procasinate over starting to learn about sorting whenever I am preparing for interviews. Mainly due to the fact that, we need to memorize the working of various sorting algorithms. But over the time, I have come to a realization that each sorting algorithm is based on some intution and if we are able to understand those intutions, then it becomes easy to remember how they work.

One of my earliest attempts at learning about sorting algorithms is by writing [machinepack-sort](http://node-machine.org/machinepack-sort)

I am going to do a similar effort here, but this time I am planning to do these steps.
1. Understand and visualize how a sorting algorithm works. (by reading blogs, seeing video tutorials and lectures)
1. Come up with the time and space complexity for each of them.
1. Write code and test the implementation using [this leetcode puzzle](https://leetcode.com/problems/sort-an-array/)
1. Try to find practical use cases for each algorithm.

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

When sorting a collection, what if two items with the same value exist.

[5 2 1 1 6]

Notice how 1 is repeated. While sorting, should we leave their relative order the same or should we shift them.

Well, it is up to you. If your sorting implementation maintains the relative order of equal elements, then it is said to be stable sorting.

Here is a more practical example. Consider an array of json objects needs to be sorted based on marks of students.

```json
[
    {"name": "personA", "mark": 50},
    {"name": "personB", "mark": 40},
    {"name": "personC", "mark": 40},
    {"name": "personD", "mark": 80}
]
```

If the above array is to be sorted using stable sorting, we would get

```json
[
    {"name": "personB", "mark": 40},
    {"name": "personC", "mark": 40},
    {"name": "personA", "mark": 50},
    {"name": "personD", "mark": 80}
]
```
In case of a un-stable sort, we might get

```json
[
    {"name": "personC", "mark": 40},
    {"name": "personB", "mark": 40},
    {"name": "personA", "mark": 50},
    {"name": "personD", "mark": 80}
]
```

Notice how the relative order of two persons with same mark is disrupted for an un-stable sort.

Futher reading: https://en.wikipedia.org/wiki/Sorting_algorithm#Stability

## Comparison and non-comparison sorts
woah, just discovered this type of categorisation of sorting algorithms: https://en.wikipedia.org/wiki/Sorting_algorithm#Comparison_of_algorithms

I think for most of the post here we will focus on Comparison sorts, but would like to explore this topic as we explore various algorithms.

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

### Step by step code
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
Values are bubbled up while sorting using Bubble sort. Lets see what we mean by "bubbling up".

The way bubble sort works is, we compare i and i+1 elements and swap them if i<sup>th</sup> element is greater than (i+1)<sup>th</sup> element. If we do this repeatedly for ~n times, the greater elements would start bubbling up at the end of the list and the list will be sorted at the end.

Consider the example of sorting: [5, 4, 6, 2, 1] (into an ascending order list)

`i=0`; First we compare 5 and 4. Since `5 > 4`, we swap.

4 5 6 2 1

`i=1`; We compare 5 and 6. Since `5 < 6`, no swap.

4 5 6 2 1

`i=2`; We compare 6 and 2. Since `6 > 2`, we swap.

4 5 2 6 1

`i=3`; We compare 6 and 1. Since `6 > 1`, we swap.

4 5 2 1 6

That's it! Notice how 6 (the highest number) got __bubbled up__ at the end of the list.

If we perform the same procedure n times, we will end up bubbling all the n highest numbers, thus resulting in sorted order.

### Intution
Bubble up the highest number to the last and build up the sorted list from backwards.

### Time Complexity

We are performing in-memory swaps upto the n-1<sup>th</sup> index in the first iteration. At this point, the highest number is bubbled up at the `n-1`<sup>th</sup> index.

In the second iteration, we perform swapping upto the n-2<sup>th</sup> index. At this point, the highest number is bubbled up at the `n-2`<sup>th</sup> index.

This iteration happens n times and for each iteration the length of the unsorted list goes down by one.

n + (n-1) + (n-2) + .... + 1 

Again it boils to simple math, "Sum of first n natural numbers" = (n*(n+1))/2 = (n<sup>2</sup> + n) / 2

Now omitting the constants and lower degree, we arrive at the time complexity.

__O(n<sup>2</sup>)__

### Space Complexity
This is easy to figure out because we are not allocating any new structures during the process. We are just doing a bunch of in-memory swaps.

So, __O(1)__

### Step by step code
First, we will handle for the case where array is of size 0 or 1. In that case, we just need to return back the same array.

```go
func sortArray(nums []int) []int {
    if len(nums) < 2 {
        return nums
    }
}
```

Now, we will try to get the "bubble up" code done. This part of the code will just bubble the highest element. Once we have this logic, we just perform the logic for n times to bubble up all the elements.

```go
for i := 0; i <= (len(nums)-2); i++ {
    if nums[i] > nums[i+1] {
        nums[i], nums[i+1] = nums[i+1], nums[i]
    }
}
```

Cool, we will wrap up the bubble up code with a loop running n times.

```go
for n := 0; n < len(nums); n++ {
    for i := 0; i <= (len(nums)-2); i++ {
        if nums[i] > nums[i+1] {
            nums[i], nums[i+1] = nums[i+1], nums[i]
        }
    }
}
```

That's it, we should now have nums sorted in-memory. We can try to do one optimisation here. Since we bubble up the highest element, we can avoid trying the swapping logic on already bubbled up values. So, instead of iterating up to `len(nums)-2` index, we will iterate up to `(len(nums)-2)-n)` index, so that we avoid the index of already bubbled up values.

```go
for n := 0; n < len(nums); n++ {
    for i := 0; i <= ((len(nums)-2)-n) ; i++ {
        if nums[i] > nums[i+1] {
            nums[i], nums[i+1] = nums[i+1], nums[i]
        }
    }
}
```

### Full code

```go
func sortArray(nums []int) []int {
    if len(nums) < 2 {
        return nums
    }
    
    for n := 0; n < len(nums); n++ {
        for i := 0; i <= ((len(nums)-2)-n) ; i++ {
            if nums[i] > nums[i+1] {
                nums[i], nums[i+1] = nums[i+1], nums[i]
            }
        }
    }
    
    return nums
}
```

### Resources
- [Hackerrank Youtube](https://www.youtube.com/watch?v=6Gv8vg0kcHc)

## Insertion sort
At first, it felt similar to selection sort and made me wonder what actually is the difference between them.

I would say that insertion sort is little bit intelligent than both of the above algorithms: selection sort and bubble sort. This is because when we feed an already sorted array or an _almost_ sorted array to those algorithms, they don't understand that it is an already/almost sorted array and run for O(n<sup>2</sup>) time, no matter what.

But in that case, insertion sort seem to run just for O(n) time. [This video](https://www.youtube.com/watch?v=eTvQIbB-AuE) gave an example of where we might get an already/almost sorted database: think of a database where keys are already sorted.

### Intution
Given an array, consider the first element to be sorted already. Start from the next element and _insert_ it at the right position in the sorted array. If the element is already in the right position of the sorted array, we just move to the next position.

(I recommend you to watch the video resources below to get more idea about this technique)

### Time complexity

Worst and Average case: O(n<sup>2</sup>) because it would take (n(n+1))/2 swaps in these cases.

Best case: When the array is already sorted, insertion sort just takes O(n) times. If you compare this with selection sort and bubble sort, they both take O(n<sup>2</sup>). Hence insertion sort is a better choice.

### Space complexity
Swaps are done in-place.

So __O(n)__

### Step by step code
First we start with the second item in the array.

```go
for i := 1 ; i < len(nums); i++ {
    // take i-th element and insert it in the right position of the sorted sub-array
    // and index in sorted sub-array obeys 0 <= idx < i
}
```

Now, we just insert the i-th element at the right place of the array.

```go
for i := 1 ; i < len(nums); i++ {
    for j := i; (j > 0) && (nums[j] < nums[j-1]); j-- {
        nums[j], nums[j-1] = nums[j-1], nums[j]
    }
}
```

### Full code
```go
func sortArray(nums []int) []int {
    for i := 1 ; i < len(nums); i++ {
        for j := i; (j > 0) && (nums[j] < nums[j-1]); j-- {
            nums[j], nums[j-1] = nums[j-1], nums[j]
        }
    }
    return nums
}
```
### Resources
- [CS50 Insertion sort](https://www.youtube.com/watch?v=O0VbBkUvriI)
- :star: [San Diego State University - Rob Edwards - Insertion Sort](https://www.youtube.com/watch?v=eTvQIbB-AuE)
- [Insertion Sort Wikipedia](https://en.wikipedia.org/wiki/Insertion_sort)

## Merge sort
### Intution
### Time complexity
### Space complexity
### Step by step code
### Full code
### Resources

## Quick sort
### Intution
### Time complexity
### Space complexity
### Step by step code
### Full code
### Resources

## Heap sort
### Intution
### Time complexity
### Space complexity
### Step by step code
### Full code
### Resources
