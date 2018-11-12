---
title: Fixed-size arrays in C++
date: 2018-11-12 06:13:44
tags: ["programming", "c++"]
---

## Basic Usage

```cpp
// uninitialized array
int un_init_arr[5];

// looping through uninitialized array will print arbitary values
for (int & ele: un_init_arr) {
  cout << "before assign = " << ele << "\n";

  // assigns value, as ele is a reference
  ele = 0;

  cout << "after assign = " << ele << "\n";
}

// initialize array via {} notation
int init_arr[5] = {1,2,3,4,5};
int auto_count_arr[] = {6,7,8};

// access specific index
cout << "should be 3 =  " << init_arr[2] << "\n";

// access out of bound index - no exception thrown
cout << "out of bound access = " << init_arr[6] << "\n";

// loop through initialized arrays
for (const int & ele: init_arr) {
  cout << ele << "\n";
}
for (const int & ele: auto_count_arr) {
  cout << ele << "\n";
}

// length of array
cout << "length of array is " << sizeof(auto_count_arr) / sizeof(*auto_count_arr) << "\n";
```

## Heap allocation

```cpp
// use new to allocate array on heap
// new returns a pointer to allocated space
int *heap_arr = new int[5];

// REAL PROBLEM IS HERE
// range-based for loops result in compile error
for (int & ele: *heap_arr)
  ele = 4;

// delete array from heap
delete[] heap_arr;  
```

## array class

This is a syntactic sugar on top of fixed-size arrays, with no performance overhead.

```cpp
// #include <array> at the top

// uninitialized array
array<int, 5> un_init_arr;

// initialize all elements with a value
un_init_arr.fill(1);

for (const int & ele: un_init_arr)
  cout << ele << "\n";

// initialize array via {} notation
array<int, 5> init_arr = {1,2,3,4,5};

// access specific index
cout << "should be 3 =  " << init_arr[2] << "\n";

// access out of bound index - no exception thrown
cout << "out of bound access = " << init_arr[6] << "\n";

// access out of bound index - exception thrown
cout << "out of bound access = " << init_arr.at(6) << "\n";

// front and back
init_arr.front() = 10;
cout << "first element of the array is " << init_arr.front() << "\n";

init_arr.back() = 11;
cout << "last element of the array is " << init_arr.back() << "\n";

// remember that front, back, at return refs to elements
// so they could be used as lhs of expression

// read-only range-based loop
for (const int & ele: init_arr)
  cout << ele << "\n";

// index based loop
for (auto i = 0; i < init_arr.size(); ++i)
  cout << init_arr.at(i) << "\n";

// iterator based loop
for (auto ele = init_arr.begin(); ele != init_arr.end(); ++ele)
  cout << *ele << "\n";
```

## Take Home
If I need a fixed-size array in C++, I will definitely go with array class.

If I want to access an element, I will always go with `.at()`.

I see using `[]` in C++ program to be evil.

I also guess that the gap between `[]` and `array` is due to the need for maintaining compatibility between C and C++
