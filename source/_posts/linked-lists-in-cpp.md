---
title: Linked Lists in C++
date: 2018-11-15 10:49:44
tags: ["programming", "c++", "data structures"]
---

## forward_list
- Singly Linked List
- No direct access to the elements. To access n-th element, iterate through n-1 elements.

> By design, it is as efficient as a simple handwritten C-style singly-linked list, and in fact is the only standard container to deliberately lack a size member function for efficiency considerations: due to its nature as a linked list, having a size member that takes constant time would require it to keep an internal counter for its size (as list does)

```cpp
// Include
#include <forward_list>

// Initialize
forward_list<int> fl;
forward_list<int> init_fl = {2, 3, 4, 5};

// Add element
fl.push_front(1);
fl.push_front(2);
fl.push_front(3);
fl.push_front(4);

// Remove element
fl.pop_front();

// Access front
cout << "front = " << fl.front() << "\n";

// Insert after 1st element
fl.insert_after(fl.begin(), 4);

// Insert as 1st element - note before_begin() usage
fl.insert_after(fl.before_begin(), 4);

// Remove an element using iterator
fl.erase_after(fl.begin());

// Remove an element using value
fl.remove(1);

// Sort elements
fl.sort();

// Remove duplicates
fl.unique();

// Reverse list
init_fl.reverse();

// Check if empty
if (fl.empty())
  cout << "forward list is empty" << "\n";
else
  cout << "forward list is not empty" << "\n";

// Range-based iteration
for (int & ele: fl) {
  cout << ele << "\n";
}

// Iterators-based iteration
for (auto it = init_fl.begin(); it != init_fl.end(); ++it) {
  cout << *it << "\n";
}

// Merge
fl.merge(init_fl); // Removes init_fl elements and adds to end of fl
```

## list
- Doubly Linked List
- No direct access to the elements. To access n-th element, iterate through n-1 elements.

```cpp
// Include
#include <list>

// Initialize
list<int> l;
list<int> init_list = {1, 3, 2, 4};

// Add element
l.push_front(1);
l.push_front(2);
l.push_front(3);
l.push_back(4);
l.push_back(5);
l.push_back(6);

// Remove element
l.pop_front();
l.pop_back();

// Access front and back
cout << "front = " << l.front() << "\n";
cout << "back = " << l.back() << "\n";

// Size
cout << "size = " << l.size() << "\n";

// Sort
init_list.sort();
init_list.sort(greater<int>());

// Reverse
init_list.reverse();

// Remove
auto it = init_list.erase(init_list.begin());

// Insert
init_list.insert(it, 1);

// Range-based iteration
for (const int & ele: init_list)
  cout << ele << "\n";

// Iterator based iteration
for (auto it = l.begin(); it != l.end(); ++it)
  cout << *it << "\n";

// Print reverse
for (auto it = l.rbegin(); it != l.rend(); ++it)
  cout << *it << "\n";
```

## References
- http://www.cplusplus.com/reference/forward_list/forward_list/
- http://www.cplusplus.com/reference/list/list/
