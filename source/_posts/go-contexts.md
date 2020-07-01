---
title: Under the hood of Go's context
date: 2020-06-30 04:02:00
tags: ["go", "programming"]
---

This post is dedicated to you if you had used the Go programming language and ever wondered "What is a context anyway?".

`context` is a package in Go's standard library. I think `context` is idiomatic Go, hence I find quite some external packages and standard library packages using it.

You can read all about it from here - https://golang.org/pkg/context/

What I am trying to do here is just walk through the implementation details of the context package by reading the source file of it - Giving [the link](https://golang.org/src/context/context.go) to the source file, just in case if you decide to do it yourself and not hear me do it!

For all the others, let's do this!

## What is it?
Bare minimum, copy pasted from the docs.

> Package context defines the Context type, which carries deadlines, cancellation signals, and other request-scoped values across API boundaries and between processes.

It can usually be seen as the first argument to a function call.

```go
func DoSomething(ctx context.Context, arg Arg) error {
	// ... use ctx ...
}
```

## When should you use it?

There is this interesting one-liner from the docs, 

> Incoming requests to a server should create a Context, and outgoing calls to servers should accept a Context.

So if you are buiding a server or client application in Go, then you will have to deal with contexts.

That leads to why it has the following concurrent nature.

> The same Context may be passed to functions running in different goroutines; Contexts are safe for simultaneous use by multiple goroutines.

It is mainly used for propogating a request's state across function calls.

I am going to ask a "Sorry" and silently try to assume its usage feels like the `req` object in [express middlewares](https://expressjs.com/en/guide/using-middleware.html)

You have to skip reading this stuff if you are not looking to read JavaScript. 

```js

app.use(function middleware1(req, res, next) {
  // req is mutated to pass down the state of request to next middleware
  req.user = { id: 1, role: 'admin' };
});

app.use(function middleware2(req, res, next) {
  if (req.user.role === 'admin') {
    // do something
  }
});

```

Note how we pass in data across function calls using the `req` object. I think a context has similar functionality.

## How to and How not to use it?
Always propogate contexts as arguments to function and don't store it in a struct. That's some bulletproof wisdom from docs for you! :D

> Pass context.TODO if you are unsure about which Context to use.

The above one-line statement is probably what triggered me to do this deep dive - Why are people (myself included) becoming unaware of what context to use?

> Do not pass a nil Context, even if a function permits it. 


That is enough copy-pastes from the docs.

## API

![go-context](/images/go-context-doc.png)

That is all of context for you!

## The interface
At it's core lies the `Context` interface. it is the object that gets sent around. woah! I always imagined it to be struct. Now it is interesting to note that it is an interface.

```go
type Context interface {
    Deadline() (dealine time.Time, ok bool)
    Done() <-chan struct{}
    Err() error
    Value(key interface{}) interface{}
}
```

This seems to accomodate the information used by various API methods of the context package.

## Errors
context package defines errors which are returned by the `Err()` method if the channel returned by `Done()` is closed. This error message is used to communicate what made the channel close.

```go
var Canceled = errors.New("context canceled")

type deadlineExceededError struct{}
func (deadlineExceededError) Error() string   { return "context deadline exceeded" }
func (deadlineExceededError) Timeout() bool   { return true }
func (deadlineExceededError) Temporary() bool { return true }
```

## Empty context
Next up is an empty context. It is a context with no value, no deadline and is never cancelled. Lets see how it is defined and where it is used.\\

```go
type emptyCtx int

func (*emptyCtx) Deadline() (deadline time.Time, ok bool) {
	return
}

func (*emptyCtx) Done() <-chan struct{} {
	return nil
}

func (*emptyCtx) Err() error {
	return nil
}

func (*emptyCtx) Value(key interface{}) interface{} {
	return nil
}

func (e *emptyCtx) String() string {
	switch e {
	case background:
		return "context.Background"
	case todo:
		return "context.TODO"
	}
	return "unknown empty Context"
}

var (
	background = new(emptyCtx)
	todo       = new(emptyCtx)
)
```

Now that we have an empty context. It seems like both `context.Background()` and `context.TODO()` return an empty context. So when you are creating a context this is probably where we start.

```go
func Background() Context {
	return background
}

func TODO() Context {
	return todo
}
```

