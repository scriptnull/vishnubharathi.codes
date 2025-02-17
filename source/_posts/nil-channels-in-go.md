---
title: Nil channels in Go
date: 2025-02-18 02:02:12
tags: ["go","programming"]
---

A friend from work messaged me today that they had a hard time because they had used `var c chan int` instead of `c := make(chan int)` in their Go code.

I responded by saying that I usually have one rule of thumb i.e. to always use of `make()` whenever I need a channel or map. That way I can be very sure that I can use those immediately.

They added that the surprising thing was it didn't panic the program rather they ended up with an infinite loop that ran silently. I got more intrigued about the situation. So many questions started popping up in my mind. Why was I not able to catch it in the code review? Why was there no linter rule that could catch this? What is the point of having a nil channel in Go if I am brainwashing myself to always use `make()`?

I went on to get some answers and here they are!

## Nil channel

It is just a channel assigned to nil value.

```go
var c chan int
```

Nothing wrong with it!

## Send to a nil channel

When you try to send to a nil channel. 

```go
var c chan int
c <- 1
```

You get a deadlock.

```
fatal error: all goroutines are asleep - deadlock!

goroutine 1 [chan send (nil chan)]:
main.main()
        /home/vishnu/pers/chanbug/main.go:5 +0x1c
exit status 2
```

## Receive from a nil channel

When you try to receive a value from a nil channel

```go
var c chan int
<-c
```

You again get a deadlock.

```
fatal error: all goroutines are asleep - deadlock!

goroutine 1 [chan receive (nil chan)]:
main.main()
        /home/vishnu/pers/chanbug/main.go:5 +0x17
exit status 2
```

## Send and Receive

Now let us try doing both from a nil channel.

```go
package main

import "fmt"

func main() {
	var c chan int

	go func() {
		defer close(c)
		for i := 1; i < 4; i++ {
			c <- i
		}
	}()

	for i := range c {
		fmt.Println(i)
	}
	fmt.Println("all done")
}
```

This ended up with deadlock too.

```
fatal error: all goroutines are asleep - deadlock!

goroutine 1 [chan receive (nil chan)]:
main.main()
        /home/vishnu/pers/chanbug/main.go:15 +0x91

goroutine 18 [chan send (nil chan)]:
main.main.func1()
        /home/vishnu/pers/chanbug/main.go:11 +0x65
created by main.main in goroutine 1
        /home/vishnu/pers/chanbug/main.go:8 +0x35
exit status 2
```

But my friend mentioned they ran into an infinite loop and not a deadlock. How so?

## The `for select` construct

My immediate suspicion was a `for select` construct instead of `for range` construct in the above program.

```go
func main() {
	var c chan int

	go func() {
		defer close(c)
		for i := 1; i < 4; i++ {
			c <- i
		}
	}()

	for {
		select {
		case i := <-c:
			fmt.Println(i)
		default:
		}
	}
	fmt.Println("all done")
}
```

Now that leads to an infinite loop without printing anything! Because `select` seems to not execute the `case i := <-c` block when `c` is a nil channel. What can it do after all? It can't really receive anything from an un-initialized nil channel, right? So it ignores the `case` block and always runs the `default` block again and again.

## Initialized channel

Now let us initialize the channel by using `make(chan int)` instead of `var c chan int` to see how our dear friend `select` behaves.

```go
func main() {
	c := make(chan int)

	go func() {
		defer close(c)
		for i := 1; i < 4; i++ {
			c <- i
		}
	}()

	for {
		select {
		case i := <-c:
			fmt.Println(i)
		default:
		}
	}
	fmt.Println("all done")
}
```

It was again an infinite loop, but this time the output was different. 

```
$ go run main.go | head -n 10
1
2
3
0
0
0
0
0
0
0
```

The zeros took over the output. I had to pipe the output to `head` to stop the program from running infinitely and at the same time collect some sample output.

What are these zeros? Where are they coming from?

Those are arising from the `case i := <-c` block of the select. When the channel is not nil, our select statement attempts to receive a value. That results in printing `1 2 3`, the three values that were sent to the channel. When we close a channel, all we get is the zero value. Hence we are getting zeros after that.

Is there a way to check if a channel is closed? yes, there is.

```go
for {
	select {
	case i, ok := <-c:
		if ok {
			fmt.Println(i)
		}
	default:
	}
}
fmt.Println("all done")  // this is still unreachable
```

We avoided printing zeros, but it is still leading to an infinite loop. Because the select is alternating between `case` and `default` blocks and continuously executes them.

Let us get rid of `default`.

```go
for {
	select {
	case i, ok := <-c:
		if ok {
			fmt.Println(i)
		}
	}
}
fmt.Println("all done")  // this is still unreachable
```
That didn't prevent the infinite loop, our friend `select` is going on and on choose the `case i, ok := <-c` block and performing the if condition that evaluates to false always as the channel is closed after sending 3.

## The lesson

How do we avoid the infinite loop? Remember how the select statement ignored the `case` block when my friend accidentally used the nil channel instead of an initialized channel at the start of this post? That is exactly what we need to __disable__ the case in the `select` statement.

```go
for {
	select {
	case i, ok := <-c:
		if !ok {
			c = nil
			break
		}
		fmt.Println(i)
	}
}
fmt.Println("all done") // this is still unreachable
```

Now we are out of an infinite loop but are hitting a deadlock after the channel is closed.

```
1
2
3
fatal error: all goroutines are asleep - deadlock!

goroutine 1 [chan receive (nil chan)]:
main.main()
        /home/vishnu/pers/chanbug/main.go:19 +0xa8
exit status 2
```

Because after we __disable__ the case, the `select` statement essentially reduces to an empty `select` clause.

```go
package main

func main() {
	select {}
}
```

Makes the go routine sleep forever, there is no case statement that it can listen to for receiving a message.

The core lesson however is

> nil channels are useful for disabling `case` blocks of `select`

I kind of arrived at this lesson in a weird way, but [this just for func episode](https://www.youtube.com/watch?v=t9bEg2A4jsw) teaches it in a beautiful way. (Thanks Campoy if you are reading this!)

This is particularly useful when you are dealing with multiple channels in different cases of a `select` and if you want to diable the case blocks one by one when those channels are no longer needed. Going to copy-paste the example from that justforfunc episode to capture the idea.

The problem is to merge values coming from two channels and output them in another channel.

``` go
func main() {
	a := asChan(1, 3, 5, 7)
	b := asChan(2, 4, 6, 8)
	c := merge(a, b)
	for v := range c {
		fmt.Println(v)
	}
}
```

Now the `merge` routine could listen on both the channels and disable the case for a channel after it is closed to make sure that we don't spend any more CPU time on that case.

```go
func merge(a, b <-chan int) <-chan int {
	c := make(chan int)

	go func() {
		defer close(c)
		for a != nil || b != nil {
			select {
			case v, ok := <-a:
				if !ok {
					a = nil
					log.Printf("a is done")
					continue
				}
				c <- v
			case v, ok := <-b:
				if !ok {
					b = nil
					log.Printf("b is done")
					continue
				}
				c <- v
			}
		}
	}()
	return c
}
```

Beautiful, right? 

Now back to our problem.

## The solution

Let me solve the rest of the problem just for closure.

One way would be to break to an `outer` label as shown below. That way, 

```go
func main() {
	c := make(chan int)

	go func() {
		defer close(c)
		for i := 1; i < 4; i++ {
			c <- i
		}
	}()

outer:
	for {
		select {
		case i, ok := <-c:
			if !ok {
				c = nil
				break outer
			}
			fmt.Println(i)
		}
	}
	fmt.Println("all done")
}
```

And finally, we get

```
1
2
3
all done
```

NOTE: this would work without the `c = nil` statement also.

```go
outer:
	for {
		select {
		case i, ok := <-c:
			if !ok {
				break outer
			}
			fmt.Println(i)
		}
	}
	fmt.Println("all done")
```

If the above is same as the previous solution, what is the point? We noticed that setting a channel to `nil` is beneficial when we have multiple cases. In here, I could maybe use that as a check for the `for`.

```go
func main() {
	c := make(chan int)

	go func() {
		defer close(c)
		for i := 1; i < 4; i++ {
			c <- i
		}
	}()

	for c != nil {
		select {
		case i, ok := <-c:
			if !ok {
				c = nil
				break
			}
			fmt.Println(i)
		}
	}
	fmt.Println("all done")
}
```

I should probably start brainwasing myself to make sure I set the channel to `nil` after consuming it completely. That way I can avoid the weird break label syntax and disable select cases to get more throughput.

Anyhow I know of a simpler solution. So my recommended solution for my friend would be to
- initialize the channel with `make()`
- use a `for range` construct instead of `for select` construct.

That would look like:

```go
func main() {
	c := make(chan int)

	go func() {
		defer close(c)
		for i := 1; i < 4; i++ {
			c <- i
		}
	}()

	for i := range c {
		fmt.Println(i)
	}
	fmt.Println("all done")
}
```

## A proverb

The example that I gave was a very "trimmed down" version of what my friend was trying to accomplish in a real-world system. He was trying to consume a channel and split the messages into two other channels. The miss was failing to _initialize_ the channels where the split was occurring.

On the other end, we learned from the justforfunc example that, when we try to merge two channels into one, we could start setting the consumed channel(s) to nil.

This is provoking me to make up [a Go proverb](https://go-proverbs.github.io/) of my own 😅 Please excuse me if it sounds bad! You have come so far. So you can't escape from it now - lol :D

~ ~ ~ ~ 

"Init when you split, Nil when you merge."
