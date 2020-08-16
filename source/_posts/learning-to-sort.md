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
Merge sort is a good example for divide and conquer algorithm. It is easy to solve this problem by thinking in recursion. To give a mental model of what a merge sort looks like, I am going to use a nice picture that I found in [Wikipedia](https://en.wikipedia.org/wiki/Merge_sort)

![mergesort](https://upload.wikimedia.org/wikipedia/commons/e/e6/Merge_sort_algorithm_diagram.svg)

Found this insight in [The Algorithm Design Manual book](http://www.algorist.com/),

> Mergesort is a great algorithm for sorting linked lists, because it does not rely on random access to elements as does heapsort or quicksort.


### Intution
Split the array to be sorted into two, sort those individually, and merge them back together. Repeatedly apply this on the divided arrays. When the divided array has only one element, it is already sorted. (That's the point where we stop splitting and merging back starts!)

### Time complexity
Recommending the [MIT 6.006 Merge Sort video](https://youtu.be/Kg4bqzAqRBM?t=1487) to figure out how this is done.

At each level of splitted arrays, we access `n` items and we would have a total of `log n` levels. Hence, time complexity is __O(n log n)__

### Space complexity
I tried implementing merge sort with the help of "Top Down Split Merge" + "Two queues" like mentioned in [The Algorithm Design Manual book](http://www.algorist.com/). I think the space for this method is also __O(n log n)__.

But if we follow the algorithm where we use a temporary array instead of allocating two queues everytime , we can get a __O(n)__ space complexity.

### Step by step code
We will try to code the temp array method here! Two queue method is relatively easy. You should try doing the two queue method first, if you are not sure. (I have provided the two queue technique in the full code section below.

Prepare for a recursive ride! haha. Merge sort has two parts: Split and Merge (remember the diagram).

first we make a temporary array (which we use to merge) and call merge sort procedure from index `0` to `n-1`.

```go
func sortArray(nums []int) []int {
    temp := make([]int, len(nums))
    ms(nums, temp, 0, len(nums)-1)
    return nums
}
```

The `ms` call actually does the split. then we call a merge function to perform the merge.

```go
func ms(nums, temp []int, low, high int) {
    if low < high {
        mid := (low + high) / 2
        ms(nums, temp, low, mid)
        ms(nums, temp, mid+1, high)
        merge(nums, temp, low, mid, high)
    }
}
```

Now the merge part:

```go
func merge(nums, temp []int, low, mid, high int) {
    i1 := low
    i2 := mid+1
    i := low
    
    for (i1 <= mid) && (i2 <= high) {
        if nums[i1] <= nums[i2] {
            temp[i] = nums[i1]
            i1++
        } else {
            temp[i] = nums[i2]
            i2++
        }
        i++
    }
    
    for i1 <= mid {
        temp[i] = nums[i1]
        i++
        i1++
    }
    for i2 <= high {
        temp[i] = nums[i2]
        i++
        i2++
    }
    
    for i := low; i <= high; i++ {
        nums[i] = temp[i]
    }
}
```

The thing that I miss out is the last section of merge where we copy the temp array to the source array.

### Full code
#### Two queues
```go
func sortArray(nums []int) []int {
    ms(nums, 0, len(nums)-1)
    return nums
}

func ms(nums []int, low, high int) {
    if low < high {
        mid := (low + high) / 2
        ms(nums, low, mid)
        ms(nums, mid+1, high)
        merge(nums, low, mid, high)
    }
}

type Queue struct {
    qList *list.List
}

func NewQueue() *Queue {
    return &Queue{
        qList: list.New(),
    }
}

func (q *Queue) Enqueue(item int) {
    q.qList.PushBack(item)
}

func (q *Queue) Dequeue() int {
    return q.qList.Remove(q.qList.Front()).(int)
}

func (q *Queue) Empty() bool {
    return q.qList.Len() == 0
}

func (q *Queue) Top() int {
    return q.qList.Front().Value.(int)
}

func merge(nums []int, low, mid, high int) {
    var q1 = NewQueue()
    var q2 = NewQueue()

    for i := low; i <= mid; i++ {
        q1.Enqueue(nums[i])
    }
    for i := mid+1; i <= high; i++ {
        q2.Enqueue(nums[i])
    }
    
    i := low
    for !q1.Empty() && !q2.Empty() {
        if q1.Top() < q2.Top() {
            nums[i] = q1.Dequeue()
        } else {
            nums[i] = q2.Dequeue()
        }
        i++
    }
    
    for !q1.Empty() {
        nums[i] = q1.Dequeue()
        i++
    }
    for !q2.Empty() {
        nums[i] = q2.Dequeue()
        i++
    }
}
```

#### Temporary array
```go
func sortArray(nums []int) []int {
    temp := make([]int, len(nums))
    ms(nums, temp, 0, len(nums)-1)
    return nums
}

func ms(nums, temp []int, low, high int) {
    if low < high {
        mid := (low + high) / 2
        ms(nums, temp, low, mid)
        ms(nums, temp, mid+1, high)
        merge(nums, temp, low, mid, high)
    }
}

func merge(nums, temp []int, low, mid, high int) {
    i1 := low
    i2 := mid+1
    i := low
    
    for (i1 <= mid) && (i2 <= high) {
        if nums[i1] <= nums[i2] {
            temp[i] = nums[i1]
            i1++
        } else {
            temp[i] = nums[i2]
            i2++
        }
        i++
    }
    
    for i1 <= mid {
        temp[i] = nums[i1]
        i++
        i1++
    }
    for i2 <= high {
        temp[i] = nums[i2]
        i++
        i2++
    }
    
    for i := low; i <= high; i++ {
        nums[i] = temp[i]
    }
}
```

### Resources
- [Merge Sort Wikipedia](https://en.wikipedia.org/wiki/Merge_sort)
- [MIT 6.006 Merge Sort](https://youtu.be/Kg4bqzAqRBM?t=1487)
- [The Algorithm Design Manual Book](http://www.algorist.com/)
- :star: [San Diego State University - Rob Edwards - Merge Sort](https://www.youtube.com/watch?v=jr10xrAFSEg) (Despite the black screen problem in the video, I still think the video did a good job of explaining the merge part)

## Quick sort
Quick sort is one of the sorting algorithms that I have noticed in practice often. For example: I remember noticing `QSORT` while reading [git's source code](https://github.com/git/git/search?q=QSORT&unscoped_q=QSORT) on how git suggests commands when we make a mistake while typing a git command.

Also, I have read that quick sort seems to be a choice for standard library implementation of sorting in some programming languages. Example: [Go's sort package](https://golang.org/src/sort/sort.go?s=8174:8200#L183)

There are different flavours of qsort and one needs to consider the tradeoffs to choose the one that suits their needs. For example: [Lomuto Partition Scheme](https://en.wikipedia.org/wiki/Quicksort#Lomuto_partition_scheme) chooses the pivot point as the last element of the array and performs qsort, whereas 

### Intution
Choose a pivot point (probably the last element of the array) and partition lesser and higher elements based on the pivot. Perform the pivot and partition logic recursively for the partitions.

### Time complexity
If the pivot point we choose is approximately the middle of sorted list, then the list is divided equally (like merge sort). So quick sort has a time complexity of __O(n log n)__ for best and average case.

For the worst case, (where we choose the pivot point as the first or last element of sorted array as the first pivot), the algorithm performs O(n<sup>2</sup>).

### Space complexity
For the best and average case, the space complexity would be __(log n)__ (because of the call stack used for recursion). In the worst case, that would become __O(n)__

### Step by step code
First, we write the recursive logic of partition and qsort.

```go
func qsort(nums []int, low, high int) {
    if low < high {
        p := part(nums, low, high)
        qsort(nums, low, p-1)
        qsort(nums, p+1, high)
    }
}
```

Next we implement the partitioning logic. I am using the [Lomuto Partition Scheme](https://en.wikipedia.org/wiki/Quicksort#Lomuto_partition_scheme) here.

```go
func part(nums []int, low, high int) int {
    pivot := nums[high]
    i := low
    
    for j := low; j <= high; j++ {
        if nums[j] < pivot {
            nums[j], nums[i] = nums[i], nums[j]
            i++
        }
    }

    nums[i], nums[high] = nums[high], nums[i]
    return i
}
```

### Full code
```go
func sortArray(nums []int) []int {
    qsort(nums, 0, len(nums)-1)
    
    return nums
}

func qsort(nums []int, low, high int) {
    if low < high {
        p := part(nums, low, high)
        qsort(nums, low, p-1)
        qsort(nums, p+1, high)
    }
}

func part(nums []int, low, high int) int {
    pivot := nums[high]
    i := low
    
    for j := low; j <= high; j++ {
        if nums[j] < pivot {
            nums[j], nums[i] = nums[i], nums[j]
            i++
        }
    }

    nums[i], nums[high] = nums[high], nums[i]
    return i
}
```

### Resources
- :star: [Quick sort Wikipedia](https://en.wikipedia.org/wiki/Quicksort#Lomuto_partition_scheme)
- [San Diego State University - Rob Edwards - Quick sort](https://www.youtube.com/watch?v=ZHVk2blR45Q)
- [San Diego State University - Rob Edwards - Quick sort worst case](https://www.youtube.com/watch?v=auclbmnm4iA)
- [San Diego State University - Rob Edwards - Quick sort code](https://www.youtube.com/watch?v=4IE3wIXFVPc)

## Heap sort
The most important idea behind heap sort is to first build a heap out of the given array. A heap is just a common way of implementing a priority queue. A priority queue is just a data-strucutre, where we could request for an element with either the largest or smallest priority at a given point of time.

With that intution, the implementation could be pretty simple. Consider a language with a priority queue implementation built into the standard library like C++. In this case, we could write something like,

```cpp
class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        std::vector<int> result;
        // build a min-heap
        priority_queue<int, vector<int>, std::greater<int>> q;
        
        for (int n : nums) {
            q.push(n);
        }
        
        while (!q.empty()) {
            result.push_back(q.top());
            q.pop();
        }
        
        return result;
    }
};
```

We just create a min-heap and extract the minimum element each time and append it to a list. While this approach involves allocating space, there is a way to achieve this in-memory if the input is an array.

### Intution
Construct a max-heap and pick the largest element using it, one at a time to fill it at the end of the sorted list.

### Time complexity
I recommend watching the [MIT 6.006 Heaps and Heap sort](https://www.youtube.com/watch?v=B7hVxCmfPtM) lecture for deriving the time complexity. It seems like building a heap from scratch is O(n) and extracting a min/max element seems to be O(log n), since we extract the min/max n times, the time complexity would be __O(n log n)__

### Space complexity
A naive implementation of constructing a priority queue from scrach (like with standard library code or any other libarary) might lead to O(n).

But we will be using a binary heap (just represented in-place in the given array), there is no extra space allocated. So the space complexity would be __O(1)__.

This might seem to be the best algorithm so far, but there should be something that we are losing, right? It is the stableness. Seems like heap sort is not stable.

### Step by step code
We need to learn and remember about a few array-tree math before trying to code it. First binary heaps are array representation of a binary tree.

[0 1 2 3 4]

Value at 0 is the root node. value at 1 and 2 are children of root node (0). The children of 1 would be 3 and 4.

This leads to arriving at the following formulae.

left child of a node at index i is given by `(2 * i) + 1` and right child of a node at index i is given by `(2 * i) + 2`.

If there are n nodes, `(n/2) - 1`th index will give the node whose children will all be leaf nodes. This is a very useful insight that I got from [MIT 6.006 Heaps and Heap sort](https://www.youtube.com/watch?v=B7hVxCmfPtM). This means that, since its children are leaf nodes, they already satisfy the heap property and it might be the right place to start recursion procedure for building up the heap from bottom up.

Ok, lets start writing this! First we call the `heapify` procedure from `(n/2)-1`th index to `0`th index

```go
for i := (len(nums)/2) - 1; i >= 0; i-- {
    heapify(nums, len(nums), i)
}
```

With this, the root node is guaranted to have the largest element. So, we start filling up the array from back by extracting the max element. Everytime we extract the max element, the heap becomes dirty. So we could just call heapify for only the unsorted sub-array at the beginning.

```go
for i := len(nums)-1; i >= 0; i-- {
    nums[i], nums[0] = nums[0], nums[i]
    heapify(nums, i, 0)
}
```

Ok, now we start implementing the heapify function.

```go
func heapify(nums []int, n, idx int) {    
    largest := idx
    left := (2 * idx) + 1
    right := (2 * idx) + 2
    
    if left < n && nums[largest] < nums[left] {
        largest = left
    }
    
    if right < n && nums[largest] < nums[right] {
        largest = right
    }
    
    if largest != idx {
        nums[idx], nums[largest] = nums[largest], nums[idx]
        
        heapify(nums, n, largest)
    }
}
```

### Full code
```go
func sortArray(nums []int) []int {
    for i := (len(nums)/2) - 1; i >= 0; i-- {
        heapify(nums, len(nums), i)
    }
    
    for i := len(nums)-1; i >= 0; i-- {
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)
    }
    
    return nums
}

func heapify(nums []int, n, idx int) {    
    largest := idx
    left := (2 * idx) + 1
    right := (2 * idx) + 2
    
    if left < n && nums[largest] < nums[left] {
        largest = left
    }
    
    if right < n && nums[largest] < nums[right] {
        largest = right
    }
    
    if largest != idx {
        nums[idx], nums[largest] = nums[largest], nums[idx]
        
        heapify(nums, n, largest)
    }
}
```

### Resources
- [MIT 6.006 Heaps and Heap sort](https://www.youtube.com/watch?v=B7hVxCmfPtM)
- [GeeksForGeeks solution](https://www.geeksforgeeks.org/heap-sort/) (this closely follows the ideas behind the MIT 6.006 lecture)
