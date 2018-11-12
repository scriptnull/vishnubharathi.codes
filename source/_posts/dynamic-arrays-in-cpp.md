---
title: Dynamic arrays in C++
date: 2018-11-12 19:00:34
tags: ["programming", "c++"]
---

## Initialize

```cpp
// add <vector> preprocessor to use this
#include <vector>

vector<int> arr;
vector<int> init_arr = {4, 5, 6};
```

## Push and Pop

```cpp
// add items to the back
arr.push_back(1);
arr.push_back(2);
arr.push_back(3);
arr.push_back(4);

// remove an item from the back
arr.pop_back();
```

## Size and Capacity

```cpp
// print size of vector
cout << "size = " << arr.size() << "\n";
cout << "capacity = " << arr.capacity() << "\n";
```

## Access

```cpp
// access items
cout << "front = " << arr.front() << "\n";
cout << "back = " << arr.back() << "\n";
cout << "[1] = " << arr[1] << "\n";
cout << "at 1 = " << arr.at(1) << "\n";

// accessing out of range elements
cout << "[10] = " << arr[10] << "\n"; // gives arbitary value
cout << "at 10 = " << arr.at(10) << "\n"; // throws exception
```

## Iterate

```cpp
for (int & ele: arr)
  ele += 1;

for (int i = 0; i < arr.size(); ++i)
  arr.at(i) += 1;

for (auto it = arr.begin(); it != arr.end(); ++it)
  *it += 1;

// read-only access
for (const int & ele: arr)
  cout << ele << "\n";

// iterate list in reverse
for (auto it = arr.rbegin(); it != arr.rend(); ++it)
  cout << *it << "\n";
```

## Uncommon Operations

```cpp
// remove element using iterator
arr.erase(arr.begin() + 1);

// remove elements using iterator range
arr.erase(arr.begin() + 1, arr.end() - 1);

// remove everything
arr.clear();
```
