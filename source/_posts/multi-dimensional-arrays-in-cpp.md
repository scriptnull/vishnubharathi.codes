---
title: Multidimensional arrays in C++
date: 2018-11-19 06:18:37
tags: ["programming", "c++", "data structures"]
---

Multidimensional arrays have values in rows and columns.

## Built-in arrays

```cpp
// Using array notation
// Build 3x3 matrix
int init_arr[3][3] = {
  {1, 2, 3},
  {4, 5, 6},
  {7, 8, 9}
};

// Infer row-size automatically
int auto_num[][2] = {
  {1, 2},
  {3, 4}
};

// Iterate
for (auto i = 0; i < sizeof(init_arr) / sizeof(*init_arr); ++i) {
  for (auto j = 0; j < sizeof(init_arr[i]) / sizeof(int); ++j) {
    cout << init_arr[i][j] << " ";
  }
  cout << "\n";
}
```

## array class

```cpp
// Include
#include <array>

// Using array class
// Build 2x3 matrix
array<array<int, 3>, 2>  arr;

arr.fill({1,2,3});

for (auto i = 0; i < arr.size(); ++i) {
  for (auto j = 0; j < arr[0].size(); ++j) {
    cout << arr.at(i).at(j) << " ";
  }
  cout << "\n";
}
```

## vector class

```cpp
// Using vector class
// Build 3x3 matrix
vector<vector<int>> vec;

int num = 1;
for (auto i = 0; i < 3; ++i) {
  vector<int> temp;
  for (auto j = 0; j < 3; ++j) {
    temp.push_back(num++);
  }
  vec.push_back(temp);
}

for (auto i = 0; i < 3; ++i) {
  for (auto j = 0; j < 3; ++j) {
    cout << vec.at(i).at(j) << "\n";
  }
}
```

## Jagged arrays
Jagged arrays are array of variable length arrays like

```
| 1 2 |
| 4 1 3 |
| 5 |
| 1 4 5 6 7 |
```

```cpp
// Build jagged array
// Avoid using **, as it results in hard-to-question about code
int **jagged_arr = new int*[3];

// Use a array + vector if row size won't change
array<vector<int>, 3> jag_3_n;

// Use a vector + vector if row size changes
vector<vector<int>> jag_n_n;

```
