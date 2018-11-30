---
title: pure.h
date: 2018-11-30 21:09:03
tags: ["programming", "c++"]
---

## Prelude

When writing pure virtual functions in C++, I raise my eyebrows because the syntax for it feels weird to me.

```cpp
class Command {
public:
  virtual void execute() = 0;
};
```

Notice `= 0` ? It means this virtual function is pure.

For the context of non-C++ programmers here, pure virtual function means a function which must be defined as part of the derived class, thus allowing the class in which they are declared (abstract class) to act as an interface for accessing any class derived from it.

This concept is present in various programming languages like Java, Go etc. and is very useful to implement design patterns like the strategy pattern.

## What C++ needs?

C++ has a concept called specifiers - some keywords mentioned after the () of function to tell more about a function.

My favorite specifier is `const` specifier.

```cpp
class Employee {
private:
  int _id;
public:
  Employee(int id): _id{id} {}
  int getId() const {
    return _id;
  }
};

const Employee emp1 {1};
auto id1 = emp1.getId(); // OK, as type is const Employee

Employee emp2 {2};
auto id2 = emp2.getId(); // Error, as type is Employee
```

`const` specifier allows the function to be available only for the const variant of the class.

This is cool. So, if we want to denote a pure virtual function in a class, all we need is a specifier called `pure`.

```cpp
class Command {
public:
  virtual void execute() pure;
};
```

Even better is

```cpp
class Command {
public:
  void execute() pure virtual;
};
```

But here we are still stuck with `= 0` instead of `pure` or `pure virtual`.

## Why so?
Why C++ does not have a pure keyword?

A Google search skill took me to [this page](https://softwareengineering.stackexchange.com/questions/284412/why-does-c-not-have-a-pure-keyword-for-virtual-functions).

It references Bjarne Stroustrup's answer for this question in [The Design and Evolution of C++](http://www.stroustrup.com/dne.html)

> The curious = 0 syntax was chosen over the obvious alternative of introducing a new keyword pure or abstract because at the time I saw no chance of getting a new keyword accepted. Had I suggested pure, Release 2.0 would have shipped without abstract classes. Given a choice between a nicer syntax and abstract classes, I chose abstract classes. Rather than risking delay and incurring the certain fights over pure, I used the tradition C and C++ convention of using 0 to represent not there.

Seems like even the greatest are in the race to catch release deadlines :D

## Why we are ok with it?

Because C++ allows us to define our own `pure`. Remember macros?

I found this simple and very cool (IMO) technique/code while reading [envoyproxy's code](https://github.com/envoyproxy/envoy).

A pure virtual function in envoyproxy's code base looks like

```cpp
class Command {
public:
  virtual void execute() PURE;
};
```

pretty close to what we need, huh?

I went in and checked how it worked. Answer to it is present in a header file called [pure.h](https://github.com/envoyproxy/envoy/blob/15706964a29e595c045a5d7ef0646d04f347dcc1/include/envoy/common/pure.h).

```cpp
#pragma once

namespace Envoy {
/**
 * Friendly name for a pure virtual routine.
 */
#define PURE = 0
} // Envoy
```

That's it! Simple, but elegant usage of macros. This code is pure bliss and I wish for more things like `pure.h` in this world.
