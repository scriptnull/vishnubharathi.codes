---
title: Sets in C++
date: 2018-11-18 12:27:24
tags: ["programming", "c++", "data structures"]
---

Sets are containers that store unique elements. There are four kinds of sets in C++

1. set
1. multiset
1. unordered_set
1. unordered_multiset

## set
- Internally, keys are sorted following a strict weak ordering criteria - default is `less<Key>`
- Implemented using binary search trees, so access takes O(log n)

```cpp
template < class T,                        // set::key_type/value_type
           class Compare = less<T>,        // set::key_compare/value_compare
           class Alloc = allocator<T>      // set::allocator_type
           > class set;
```

```cpp
// Include
#include <set>

// Initialize
set<int> s;

// Insert
s.insert(1);
s.insert(2);
s.insert(3);
auto res = s.insert(3);
if (res.second)
  cout << "value = " << *res.first << " was newly added!" << "\n";

// Find
if (s.find(11) == s.end())
  cout << "11 is not present in the set" << "\n";

// Find a single element
auto it = s.find(2);
cout << *it << "\n";

// Erase
s.erase(3);
s.erase(it);

// Iterate
for (auto ele: s)
  cout << ele << "\n";
```

## multiset
Like set, but multiple values could have an equivalent key.

```cpp
template < class T,                        // multiset::key_type/value_type
           class Compare = less<T>,        // multiset::key_compare/value_compare
           class Alloc = allocator<T>     // multiset::allocator_type
           > class multiset;
```

```cpp
// Include
#include <set>

// Initialize
multiset<int> s;

// Insert
s.insert(1);
s.insert(2);
s.insert(3);
s.insert(3);
s.insert(4);

// Find
if (s.find(11) == s.end())
  cout << "11 is not present in the set" << "\n";

// Find a single element
auto it = s.find(2);
cout << *it << "\n";

// Erase
s.erase(4);
s.erase(it);

// Count
cout << "no. of elements with key 3 = " << s.count(3) << "\n";

// Iterate
for (auto ele: s)
  cout << ele << "\n";

// Iterate for given key
auto range_it = s.equal_range(3);

for (auto it = range_it.first; it != range_it.second; ++it)
  cout << *it << "\n";
```

## unordered_set
- Internally, keys are not sorted and a hash value of key is used to organise the values in buckets.
- Faster access time due to hash function -> constant average time

```cpp
template < class Key,                         // unordered_set::key_type/value_type
           class Hash = hash<Key>,            // unordered_set::hasher
           class Pred = equal_to<Key>,        // unordered_set::key_equal
           class Alloc = allocator<Key>       // unordered_set::allocator_type
           > class unordered_set;
```

```cpp
// Include
#include <unordered_set>

unordered_set<int> s;

// APIs similar to set
// Refer docs for extra functions like hash related functions .load_factor()
```

## unordered_multiset
- Like `unordered_set`, but multiple values could have an equivalent key.
- Faster compared to `multiset`, as it uses hash function to internally store values in buckets based on the key.

```cpp
template < class Key,                         // unordered_multiset::key_type/value_type
           class Hash = hash<Key>,            // unordered_multiset::hasher
           class Pred = equal_to<Key>,        // unordered_multiset::key_equal
           class Alloc = allocator<Key>       // unordered_multiset::allocator_type
           > class unordered_multiset;
```

```cpp
// Include
#include <unordered_set>

unordered_multiset<int> s;

// API similar to multiset
// Note that .insert() returns iterator, instead of a pair<iterator,bool>
```

## References
- http://www.cplusplus.com/reference/set/set/
- http://www.cplusplus.com/reference/set/multiset/
- http://www.cplusplus.com/reference/unordered_set/unordered_set/
- http://www.cplusplus.com/reference/unordered_set/unordered_multiset/
