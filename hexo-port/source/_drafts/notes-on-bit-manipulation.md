---
title: "Notes on Bit Manipulation"
date: 2018-09-05T21:11:40+05:30
draft: true
tags: ["programming"]
---

I am finally sitting down to learn some computer science basics.

Bit Manipulation is a technique that will help us to perform operations on numbers more efficiently on a computer. To learn this technique, we will need to first try to understand how the numbers are being represented on a computer.

---

# Binary number

> In mathematics and digital electronics, a binary number is a number expressed in the base-2 numeral system or binary numeral system, which uses only two symbols: typically 0 (zero) and 1 (one).

Computers store data in binary format. So, it is useful to understand how to represent/find the equivalent binary number for a given decimal number (base 10)

## Find in paper

[Use short division by 2](https://www.wikihow.com/Convert-from-Decimal-to-Binary) to convert a decimal to binary number

![short division](https://www.wikihow.com/images/thumb/b/b2/Convert-from-Decimal-to-Binary-Step-4-Version-4.jpg/aid5981-v4-900px-Convert-from-Decimal-to-Binary-Step-4-Version-4.jpg)

Source: https://www.wikihow.com/Convert-from-Decimal-to-Binary

## Find in program

I had previously used JavaScript's `toString()` to convert from decimal to binary numbers.

```javascript

// Decimal to Binary

const getBinaryVal = num => num.toString(2); // base 2
console.log(getBinaryVal(156)); // 10011100

// Binary to Decimal

const getDecimalVal = num => parseInt(num, 2);
console.log(getDecimalVal('10011100')); // 156
```

## Most Significant Bit

> In computing, the most significant bit (MSB, also called the high-order bit) is the bit position in a binary number having the greatest value.

```
156

1 0 0 1 1 1 0 0
^
|
MSB
```

since JavaScript's `toString(baseVal)` returns a string, we could just access the 0th index to get the MSB.

```javascript
const getMSB = num => num.toString(2)[0];

console.log(getMSB(156)) // 1
```

## Least Significant Bit

> In computing, the least significant bit (LSB) is the bit position in a binary integer giving the units value, that is, determining whether the number is even or odd.

```
156

1 0 0 1 1 1 0 0
              ^
              |
             LSB
```

Same story for LSB. Just access the last index of the string.

```javascript
const getLSB = num => {
  const binary = num.toString(2);
  return binary[binary.length-1];
}

console.log(getLSB(156)); // 0
```

---

# Endianness

I remember hearing this word again and again from embedded device programmers. Digging a little bit into our topic made me feel that I must understand what "Endianness" is before moving on.

> Endianness refers to the sequential order in which bytes are arranged into larger numerical values when stored in memory or when transmitted over digital links.

> Endianness is of interest in computer science because two conflicting and incompatible formats are in common use: words may be represented in big-endian or little-endian format

Ok. What exactly is a "word"?

> In computing, a word is the natural unit of data used by a particular processor design.

> The size of a word is reflected in many aspects of a computer's structure and operation; the majority of the registers in a processor are usually word sized and the largest piece of data that can be transferred to and from the working memory in a single operation is a word in many (not all) architectures.

Ok. What are "registers"?

> In computer architecture, a processor register is a quickly accessible location available to a computer's central processing unit (CPU).

When it comes to speed of access: Registers > Primary memory (RAM) > Secondary memory

There are various kinds of registers and they differ widely for various processors (Guess what? this is how processor companies make money, by designing these hardware components)

- _User accessible registers_ : registers can be read or written by machine instructions.
- _Internal registers_ : registers not accessible by instructions, used internally for processor operations.

> Registers are normally measured by the number of bits they can hold, for example, an "8-bit register", "32-bit register" or a "64-bit register" (or even with more bits).

Ok. Going back a level up, words are more useful than being helpful for determining the register sizes. A detailed list of uses could be found [here](https://en.wikipedia.org/wiki/Word_(computer_architecture)#Uses_of_words).

So, now that we know words are kind of important and Endianness is the way in which bytes of the words are stored in memory or transmitted over digital links.

## Big-endian

> In big-endian format, whenever addressing memory or sending/storing words bytewise, the most significant byte—the byte containing the most significant bit—is stored first (has the lowest address) or sent first.

![big-endian](https://upload.wikimedia.org/wikipedia/commons/5/54/Big-Endian.svg)

> Big-endian is the most common format in data networking; fields in the protocols of the Internet protocol suite, such as IPv4, IPv6, TCP, and UDP, are transmitted in big-endian order. For this reason, big-endian byte order is also referred to as network byte order.

## Little-endian

> the sequence addresses/sends/stores the least significant byte first (lowest address) and the most significant byte last (highest address)

![little-endian](https://upload.wikimedia.org/wikipedia/commons/e/ed/Little-Endian.svg)

This format was popularised by Intel and is being used in their architectures (x86, x86_64).

---

# 1's and 2's Complement

At this point, I am so pumped up to dive into various bitwise operators in programming and understand the use of them. I also tried to do it, but I couldn't do it. I bailed out in the middle because, I am unclear about two concepts: 1's complement and 2's complement.

### What is 1's complement?

> The ones' complement of a binary number is defined as the value obtained by inverting all the bits in the binary representation of the number (swapping 0s for 1s and vice versa).


### What is 2's complement?

> The two's complement of an N-bit number is defined as its complement with respect to 2<sup>N</sup>. For instance, for the three-bit number 010, the two's complement is 110, because 010 + 110 = 1000.

### How much could 1's complement represent?

with N bits, a 1's complement system could represent numbers belonging to the following range.

TODO: insert the range

With N bits, a 2's complement system could represent number belonging to the following range.

TODO: insert the range

---

# Bitwise Operators

Operations that could be performed on bits.

## NOT (~)

## AND (&)



# References
1. https://en.wikipedia.org/wiki/Binary_number
1. https://www.wikihow.com/Convert-from-Decimal-to-Binary
1. https://en.wikipedia.org/wiki/Endianness
1. https://en.wikipedia.org/wiki/Word_(computer_architecture)
1. https://en.wikipedia.org/wiki/Processor_register
1. https://en.wikipedia.org/wiki/Ones%27_complement
