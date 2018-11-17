---
title: Maps in C++
date: 2018-11-17 06:30:30
tags: ["programming", "c++", "data structures"]
---

Maps are associate containers. They associate a key and a value as pair and store them. There are four kinds of maps in C++

1. map
1. multimap
1. unordered_map
1. unordered_multimap

## map
- Internally, keys are sorted following a strict weak ordering criteria - default is `less<Key>`
- Implemented using binary search trees, so access takes O(log n)

```cpp
template < class Key,                                     // map::key_type
           class T,                                       // map::mapped_type
           class Compare = less<Key>,                     // map::key_compare
           class Alloc = allocator<pair<const Key,T> >    // map::allocator_type
           > class map;
```

```cpp
// Include
#include <map>

// Initialize
map<int,string> m;

// [] returns ref if already found, if not creates a kv in map
m[1] = "apple";
m[2] = "strawberry";
m[3] = "blueberry";
cout << "1 => " << m[1] << "\n";
cout << "is not present = " << (m[4] == "") << "\n";

// at - access kv in map if present, if not throw exception
cout << "2 => " << m.at(2) << "\n";
// cout << m.at(4) << "\n"; // throws exception

// Size
cout << "size = " << m.size() << "\n";

// Check presence of a key
if (m.find(2) != m.end())
  cout << "key-2 is present" << "\n";

if (m.find(6) == m.end())
  cout << "key-6 is not present" << "\n";

// Insert
m.insert(pair<int,string> (1, "apple"));
m.insert(pair<int,string> (4, "orange"));

auto ret = m.insert(pair<int,string> (5, "pineapple"));
auto already_there = m.insert(pair<int,string> (5, "pineapple"));

if (ret.second)
  cout << "element was inserted newly" << "\n";

if (!already_there.second)
  cout << "element was already there" << "\n";

cout << "access inserted item via iterator" << "\n";
cout << "key = " << ret.first->first << "\n";
cout << "value = " << ret.first->second << "\n";

// Erase
m.erase(m.find(1));

// Iterate
for (auto ele: m) {
  cout << "first = " << ele.first << "\n";
  cout << "second = " << ele.second << "\n";
}
```

## multimap
Like map, but key could occur more than once.

```cpp
template < class Key,                                     // multimap::key_type
           class T,                                       // multimap::mapped_type
           class Compare = less<Key>,                     // multimap::key_compare
           class Alloc = allocator<pair<const Key,T> >    // multimap::allocator_type
           > class multimap;
```

```cpp
// Include
#include <map>

// Initialize
multimap<int,string> m;

// Insert
m.insert(pair<int,string> (1, "apple"));
m.insert(pair<int,string> (1, "pineapple"));
m.insert(pair<int,string> (4, "orange"));
m.insert(pair<int,string> (2, "watermelon"));

// Find
cout << m.find(1)->second << "\n";

if (m.find(6) == m.end())
  cout << "key value of 6 not found" << "\n";

// Find all kv pair for given key
auto iter = m.equal_range(1);

for (auto it = iter.first; it != iter.second; ++it)
  cout << it->second << "\n";

// Erase
m.erase(1);

// Iterate
for (auto ele: m) {
  cout << "key = " << ele.first << "\n";
  cout << "value = " << ele.second << "\n";
}
```

## unordered_map
- Internally, keys are not sorted and a hash value of key is used to organise the kv pair in buckets.
- Faster access time due to hash function -> constant average time

```cpp
template < class Key,                                    // unordered_map::key_type
           class T,                                      // unordered_map::mapped_type
           class Hash = hash<Key>,                       // unordered_map::hasher
           class Pred = equal_to<Key>,                   // unordered_map::key_equal
           class Alloc = allocator< pair<const Key,T> >  // unordered_map::allocator_type
           > class unordered_map;
```

```cpp
// Include
#include <unordered_map>

// APIs similar to map
unordered_map<int,string> m;
m[1] = "apple";
cout << m[1] <<"\n";

// Refer docs for extra functions like hash related functions .load_factor()
```

## unordered_multimap
- Like `unordered_map`, but the key could occur more than once.
- Faster compared to `multimap`, as it uses hash function to internally store kv pairs in buckets based on the key.

```cpp
template < class Key,                                    // unordered_multimap::key_type
           class T,                                      // unordered_multimap::mapped_type
           class Hash = hash<Key>,                       // unordered_multimap::hasher
           class Pred = equal_to<Key>,                   // unordered_multimap::key_equal
           class Alloc = allocator< pair<const Key,T> >  // unordered_multimap::allocator_type
           > class unordered_multimap;
```

```cpp
// Include
#include <unordered_map>

// API similar to multimap
unordered_map<int,string> m;
m.insert(pair<int,string> (1, "apple"));
m.insert(pair<int,string> (1, "pineapple"));
cout << m.find(1)->second << "\n";

```

## References
- http://www.cplusplus.com/reference/map/map/
- http://www.cplusplus.com/reference/map/multimap/
- http://www.cplusplus.com/reference/unordered_map/unordered_map/
- http://www.cplusplus.com/reference/unordered_map/unordered_multimap/
