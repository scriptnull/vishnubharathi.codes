---
title: Priority queues in C++
date: 2018-11-13 23:12:42
tags: ["programming", "c++", "data structures"]
---

## Prelude

- Priority queues are implemented as container adaptors
- default underlying container is vector

container classes that could be used as underlying container are deque, vector and any class that implements the following methods along with [random access iterator](http://www.cplusplus.com/reference/iterator/RandomAccessIterator/)
  - empty
  - size
  - front
  - push_back
  - pop_back

## Basic Usage

```cpp
// include
#include <queue>

// initialize
priority_queue<int> pq;

// add items
pq.push(1);
pq.push(2);
pq.push(10);
pq.push(11);
pq.push(3);

// pop top element
pq.pop();

// size
cout << "size = " << pq.size() << "\n";

// iterate
while (!pq.empty()) {
  cout << pq.top() << "\n";
  pq.pop();
}
```
This outputs the following:
```
size = 4
10
3
2
1
```

## Functional Compare
By default, priority queue gives the element with highest priority. What if we want our priority queue to give the least priority element on call to `top()`.

`priority_queue` class takes advantage of templating and `<functional>` classes to facilitate this.

By default, `priority_queue` has the following signature
```cpp
template <class T, class Container = vector<T>,
  class Compare = less<typename Container::value_type> > class priority_queue;
```

Note that `less<T>` resides inside `<functional>`.

Using `less` for `Compare` instructs `priority_queue` to have a top element which is not *less* than any other element.

So, we just negate the `Compare` to make the `priority_queue` to hold the least priority element at the top.

```cpp
// include functional for greater, less etc. classes
#include <functional>

// change declaration for make_heap to use greater
priority_queue<int, vector<int>, greater<int>> pq;
```

I am not going to lie here, it is not very obvious for me. I hope that I could understand why it is this way in future.

## Practical Usage

Imagine job scheduling problem with each job containing a priority.
```cpp
class job {
public:
  int id;
  int priority;
  int resource_consumed;
};
```

Let us say that we are designing different types of schedulers for scheduling the jobs.

- schedule jobs with high priority first
- schedule jobs with low resource consumption first

We could use priority queue inside the scheduler to get the jobs by the desired priority.

To do that, we start defining functors that express those behaviours.

```cpp
class high_priority {
public:
  bool operator()(const job & lhs, const job & rhs) const {
    return lhs.priority < rhs.priority;
  }
};

class low_resource_consumption {
public:
  bool operator()(const job & lhs, const job & rhs) const {
    return lhs.resource_consumed > rhs.resource_consumed;
  }
};
```

Now, the priority queues could be constructed like this.
```cpp
job j1 {1, 101, 40};
job j2 {2, 50, 50};
job j3 {3, 102, 60};

cout << "high priority jobs first" << "\n";
priority_queue<job, vector<job>, high_priority> pq1;
pq1.push(j1);
pq1.push(j2);
pq1.push(j3);
iterate<job, high_priority>(pq1);

cout << "low resource consuming jobs first" << "\n";
priority_queue<job, vector<job>, low_resource_consumption> pq2;
pq2.push(j1);
pq2.push(j2);
pq2.push(j3);
iterate<job, low_resource_consumption>(pq2);
```

## Strict Weak Ordering

The functors `high_priority` and `low_resource_consumption` are used to form the [strict weak ordering](https://en.wikipedia.org/wiki/Weak_ordering#Examples).

`comp(a,b)` returns true if `a` should go before `b` in the strict weak ordering.

`top()` of `priority_queue` points to the last of the strict weak ordering.

By default `less<T>` is the strict weak ordering function that keeps the maximum element at the top in a normal `priority_queue<T>`.
