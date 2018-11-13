---
title: Stacks and queues in C++
date: 2018-11-12 23:24:08
tags: ["programming", "c++", "data structures"]
---

## Stack
- LIFO - Last In First Out
- stacks are implemented as containers adaptors
- default underlying container is deque

container classes that could be used as underlying container are vector, deque, list and any class that implements the following methods
  - empty
  - size
  - back
  - push_back
  - pop_back

```cpp
// add <stack> preprocessor
#include <stack>

// initialize
stack<int> st;

// Add to stack
st.push(1);
st.push(2);
st.push(3);
st.push(4);

// Access top element
cout << "top = " << st.top() << "\n";

// Size of the stack
cout << "size = " << st.size() << "\n";

// Pop top element
st.pop();

// check if stack is empty
if (st.empty())
  cout << "stack is empty" << "\n";
else
  cout << "stack is not empty" << "\n";

// iterate
while(!st.empty()) {
  cout << st.top() << "\n";
  st.pop();
}
```

## Queue
- FIFO - First In First Out
- queues are implemented as container adaptors
- default underlying container is deque

container classes that could be used as underlying container are deque, list and any class that implements the following methods
  - empty
  - size
  - front
  - back
  - push_back
  - pop_back

```cpp
// add preprocessor
#include <queue>

// initialize
queue<int> q;

// Add to queue
q.push(1);
q.push(2);
q.push(3);
q.push(4);

// Access front element
cout << "front = " << q.front() << "\n";

// Access back element
cout << "back = " << q.back() << "\n";

// Size of the queue
cout << "size = " << q.size() << "\n";

// Pop from front
q.pop();

// check if queue is empty
if (q.empty())
  cout << "queue is empty" << "\n";
else
  cout << "queue is not empty" << "\n";

// iterate
while (!q.empty()) {
  cout << q.front() << "\n";
  q.pop();
}
```
