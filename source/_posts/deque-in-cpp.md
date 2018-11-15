---
title: Deque in C++
date: 2018-11-15 10:13:56
tags: ["programming", "c++", "data structures"]
---

- Double Ended queue
- Pronounced as "deck"
- Insertion and deletion takes place at both the ends
- Used as default underlying container for stacks and queues.

> Both vectors and deques provide a very similar interface and can be used for similar purposes, but internally both work in quite different ways: While vectors use a single array that needs to be occasionally reallocated for growth, the elements of a deque can be scattered in different chunks of storage, with the container keeping the necessary information internally to provide direct access to any of its elements in constant time and with a uniform sequential interface (through iterators). Therefore, deques are a little more complex internally than vectors, but this allows them to grow more efficiently under certain circumstances, especially with very long sequences, where reallocations become more expensive.


## Basic Usage

```cpp
// Initialize
deque<int> dq;

// Add at the front
dq.push_front(3);
dq.push_front(4);
dq.push_front(10);

// Add at the end
dq.push_back(1);
dq.push_back(2);
dq.push_back(10);

// Remove at front and back
dq.pop_front();
dq.pop_back();

// Size of the deque
cout << "size = " << dq.size() << "\n";

// Access front and back
cout << "front = " << dq.front() << "\n";
cout << "back = " << dq.back() << "\n";

// Range based iteration
for (const int & ele: dq) {
  cout << ele << "\n";
}

// Random Access
cout << dq[0] << "\n";
cout << dq.at(2) << "\n"; // throws exception for out of range index

// Random access iteration
for (auto it = dq.begin(); it != dq.end(); ++it) {
  cout << *it << "\n";    
}

// Insert in between
dq.insert(dq.begin() + 1, 10);

// Erase in between
dq.erase(dq.begin() + 1);
```

## References
- http://www.cplusplus.com/reference/deque/deque/
