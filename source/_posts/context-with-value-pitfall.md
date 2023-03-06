---
title: How not to use context.WithValue in Go
date: 2023-03-06 05:29:45
tags: ["go"]
---

While working on my [recent Go project](https://github.com/scriptnull/waymond), I had a use-case where I wanted to pass a struct between two Go packages and I used `context.WithValue` to do it.

In retrospect while reading the Go docs for it, I believe I have gone against every possible rule for using it 😅 Sometimes you will have to try things out practically to get a lasting lesson.

This is such a case and I am going to share the lessons that I learned here.

All these lessons come from [this single commit](https://github.com/scriptnull/waymond/commit/f429fe9d0d6d1d7b1b6cdfe819a3f8c3eb7e9503) - feel free to take a look at it if you are interested.

## my use-case

I have three packages.
- `main` package - starting point of my app
- `trigger`, `connector`, `scaler` packages - these are called from `main` and accept a context.
- `event` package which is initialized in `main` and supposed to be used in the above packages

```go
package main

func main() {
  // .....

  eventBus, err := event.Init()
	if err != nil {
		fmt.Println("error initializing the event bus", err)
		os.Exit(1)
	}
	ctx = context.WithValue(ctx, "eventBus", eventBus)
  
  // .....
  
  for id, scaler := range scalers {
		err := scaler.Register(ctx)
		if err != nil {
			registerErrs = append(registerErrs, err)
		}
	}
  
  // .....
}
```

Inside the scaler, I would do something like this.

```go
func (s *Scaler) Register(ctx context.Context) error {
  // .....

	eventBus := ctx.Value("eventBus").(event.Bus)
	eventBus.Subscribe(fmt.Sprintf("scaler.%s", s.id), func() {
  }
  
  // .....
} 
```

## what's wrong here?

This line `ctx = context.WithValue(ctx, "eventBus", eventBus)` in `main.go` is what is wrong.

While trying to refactor, I accidently removed that line from `main.go` and ran `go build`. Guess what? The build succeeded without any problem 😱

This is scary because the `eventBus` is at the core of my project. All the packages emit and subscribe to events via it. I would maybe expect a compiler error if something as obvious as not passing it to these packages was happening.

If we try to run the passing build, it would result in a runtime panic whenever we hit the code path where it was used. Because we are getting the `eventBus := ctx.Value("eventBus").(event.Bus)` at runtime and we missed setting that value via `context.WithValue`, we will get back a nil reference. Since that value is being used just after that `eventBus.Subscribe()`, it will lead to a runtime panic.

```
panic: interface conversion: interface {} is nil, not event.Bus
```

## Let us visit the docs

It is time to visit [the Go docs for context.WithValue](https://pkg.go.dev/context#WithValue)

> WithValue returns a copy of parent in which the value associated with key is val.

Yep, I did want value associated with my key.

> Use context Values only for request-scoped data that transits processes and APIs, not for passing optional parameters to functions.

LOL, I was not even trying to pass an optional parameter, but a mandatory parameter.

> The provided key must be comparable and should not be of type string or any other built-in type to avoid collisions between packages using context.

LOL, I was using string type.

> Users of WithValue should define their own types for keys.

I did have this idea in mind and wanted to do it as a refactor.

> To avoid allocating when assigning to an interface{}, context keys often have concrete type struct{}. Alternatively, exported context key variables' static type should be a pointer or interface.

Okay, I still don't fully understand this part because the example in the Go Doc seem to use the type of `string`

```go
type favContextKey string

k1 := favContextKey("k1")
k2 := favContextKey("k2")
```

I would have expected it to be something like based on that last line from the docs

```go
type favContextKey struct{}

s1 := favContextKey{}
s2 := favContextKey{}
```

I am guessing `k1` and `k2` will result in memory allocation whereas `s1` and `s2` won't. Could somebody comfirm it for me?

## Then how to use context.WithValue

As the docs suggest, it is should be strictly used for carrying request-scoped data that ideally live only during lifetime of a request.

Example: let us consider a http handler which gets called everytime we make a http request to a client.

```go
func(w http.ResponseWriter, r *http.Request) {
  // ......
  
  ctx := context.WithValue(r.Context(), userAgent{}, r.Header.Get("User-Agent"))
  resp, err := someOtherAPI.client.Request(ctx)
  
  // ....
}
```

So, here the context is very specific to the handler and lives only throughout the lifetime of the handler. It is used to store an information very specific to the request (i.e. the user agent of the request) and pass it to the downstream API requests which could make use of it.

But definitely not something that you would pass as an optional argument or a mandatory argument 😅

## References

Two URLs on the internet helped me in my learning here:

- Go docs: https://pkg.go.dev/context#WithValue
- This blog post from Dave Cheney: https://dave.cheney.net/2017/01/26/context-is-for-cancelation 

~ ~ ~ ~

I dedicate this to all people who are faced with the question of "should I pass down my logger in my go context?" in their busy lives. Answer is simple. Don't do it.
