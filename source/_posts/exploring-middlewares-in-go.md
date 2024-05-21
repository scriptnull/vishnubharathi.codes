---
title: Exploring Middlewares in Go
date: 2024-05-21 00:10:08
tags: ["go"]
---

I came across "Middlewares" for writing HTTP servers originally in the Node.js ecosystem. There is this beautiful library called [express](https://expressjs.com/) which sparked the joy of middlewares in me. In case if you haven't heard of middlewares before, I think you should read [this beautiful page](https://expressjs.com/en/guide/using-middleware.html) from expressjs documentation to get a taste of them. (I genuinely feel that it is the best possible introduction for middleware, hence opening up the post with it)

With enough JavaScript for the day, we will jump into Go now. 😅

My goal for this post is to understand how to {use, write} middlewares in Go HTTP servers. We will also try to search the internet and surface some Go middlewares that we can add to our day to day toolkit.

## Problem

Let us take a simple problem and work our way upwards. Here is the problem statement:

Write a HTTP server that contains multiple routes. When a request is made to a route, print a log line at the start and the end of the request. Something like

```
2024/05/21 00:49:32 INFO start method=GET path=/one
2024/05/21 00:49:32 INFO end method=GET path=/one
2024/05/21 00:49:34 INFO start method=GET path=/two
2024/05/21 00:49:34 INFO end method=GET path=/two
```

## Solution

### Without Middleware

A solution without using middlewares would look like

```go
package main

import (
	"fmt"
	"log/slog"
	"net/http"
)

func main() {
	http.HandleFunc("/one", func(w http.ResponseWriter, r *http.Request) {
		slog.Info("start", "method", r.Method, "path", r.URL.Path)
		defer slog.Info("end", "method", r.Method, "path", r.URL.Path)

		fmt.Fprintln(w, "this is one")
	})

	http.HandleFunc("/two", func(w http.ResponseWriter, r *http.Request) {
		slog.Info("start", "method", r.Method, "path", r.URL.Path)
		defer slog.Info("end", "method", r.Method, "path", r.URL.Path)

		fmt.Fprintln(w, "this is two")
	})

	http.ListenAndServe(":3000", nil)
}
```

How do we avoid copy pasting those two lines to every HTTP handler function? Middlewares for the win!

### Basic Middleware

```go
package main

import (
	"fmt"
	"log/slog"
	"net/http"
)

func logRequest(next func(http.ResponseWriter, *http.Request)) func(http.ResponseWriter, *http.Request) {
	return func(w http.ResponseWriter, r *http.Request) {
		slog.Info("start", "method", r.Method, "path", r.URL.Path)
		defer slog.Info("end", "method", r.Method, "path", r.URL.Path)

		next(w, r)
	}
}

func oneHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, "this is one")
}

func twoHander(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, "this is two")
}

func main() {
	http.HandleFunc("/one", logRequest(oneHandler))
	http.HandleFunc("/two", logRequest(twoHander))

	http.ListenAndServe(":3000", nil)
}
```

### Using http.HandleFunc

We are not done yet! There is still room for improvement. Notice how big the method signature for `logRequest` is! we can start from there. I remember a standard library type called `http.HandlerFunc` which could be used in the place of `func(ResponseWriter, *Request)`. If we start using it, our middleware looks like this.

```go
func logRequest(next http.HandlerFunc) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		slog.Info("start", "method", r.Method, "path", r.URL.Path)
		defer slog.Info("end", "method", r.Method, "path", r.URL.Path)

		next(w, r)
	}
}
```

While browsing through the Go docs, I noticed that `http.HandleFunc` to have the below method signature.

```go
func HandleFunc(pattern string, handler func(ResponseWriter, *Request))
```

That arose a question in me. Why don't they use `func HandleFunc(pattern string, handler http.HandlerFunc)` instead? I thought `http.HandlerFunc` is an alias type for `func(ResponseWriter, *Request)`. Digging through the standard library source code had the answer. It seems like it is just not a simple alias, but more than that. Copy pasting the implementation of `http.HanderFunc` for you straight out of Go source :D

```go
// The HandlerFunc type is an adapter to allow the use of
// ordinary functions as HTTP handlers. If f is a function
// with the appropriate signature, HandlerFunc(f) is a
// [Handler] that calls f.
type HandlerFunc func(ResponseWriter, *Request)

// ServeHTTP calls f(w, r).
func (f HandlerFunc) ServeHTTP(w ResponseWriter, r *Request) {
	f(w, r)
}
```

oh wow, so http.HandleFunc is a `func(ResponseWriter, *Request)` which implements the [http.Handler](https://pkg.go.dev/net/http#Handler) interface.

### Enter http.Handler

Why would we need an adapter like `http.HandlerFunc` that implements the `http.Handler` interface. To understand, let us take a look at the interface definition.

```go
type Handler interface {
	ServeHTTP(ResponseWriter, *Request)
}
```

and also read through the [http.Handler documentation](https://pkg.go.dev/net/http#Handler). At first, it didn't solve my doubt, but then I discovered [this beautiful example](https://pkg.go.dev/net/http#example-Handle) in the docs. Copy pasting the example from the docs here for you to have a quick look.

```go
package main

import (
	"fmt"
	"log"
	"net/http"
	"sync"
)

type countHandler struct {
	mu sync.Mutex // guards n
	n  int
}

func (h *countHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	h.mu.Lock()
	defer h.mu.Unlock()
	h.n++
	fmt.Fprintf(w, "count is %d\n", h.n)
}

func main() {
	http.Handle("/count", new(countHandler))
	log.Fatal(http.ListenAndServe(":8080", nil))
}
```

wow, did you get it? Sometimes your handler is more than just a `func(http.ResponseWriter, *http.Request)`. It could be a struct that contains data that could be used in your request logic. Like in the above case, `countHandler` maintains a counter protected by a mutex. Each and every request to `/count` would increment the counter atomically.

For simple routes, which is just a bunch of instructions we could use `http.HandleFunc`. But once your handler gets complex, like having to maintain data that is common to all requests of the handler, then move upward and go for `http.Handle`.

woah, this just cleared my long standing doubt about "when to use `http.Handle` and `http.HandleFunc`?"

It is getting a bit clear now on why the `http.Handler` interface is needed. With two ways of defining a HTTP handler: one being wrte a `func(http.ResponseWriter, *http.Request)` and pass it to `http.HandleFunc` and another being write a struct with the necessary logic and pass it down to `http.Handle` function, the standard libary needs a common ground in which all its methods can operate on both the types of handlers. Hence an interface.

### http.HandlerFunc to http.Handler

Now that it is evident that a Go programmer could choose between using `http.Handle` or `http.HandleFunc` to serve their handlers, it is necessry that any HTTP middleware should work for both of those use-cases. With the current approach to our solution, we will only support middlerwares which are input to `http.HandleFunc`. Hance moving our middleware to use `http.Handler` interface, that way we could accommodate both types of handlers.

```go
package main

import (
	"fmt"
	"log/slog"
	"net/http"
)

func logRequest(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		slog.Info("start", "method", r.Method, "path", r.URL.Path)
		defer slog.Info("end", "method", r.Method, "path", r.URL.Path)

		next.ServeHTTP(w, r)
	})
}

func oneHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, "this is one")
}

func twoHander(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, "this is two")
}

func main() {
	http.Handle("/one", logRequest(http.HandlerFunc(oneHandler)))
	http.Handle("/two", logRequest(http.HandlerFunc(twoHander)))

	http.ListenAndServe(":3000", nil)
}
```

## Standard library Middlewares

The `net/http` package in the standard library of Go contains middlewares. If you haven't realized it yet, don't worry. That is because they don't advertise those functions as "middleware" (ctrl+f on docs for middleware leaves you with 0 matches :D)

### AllowQuerySemicolons

```go
func AllowQuerySemicolons(h Handler) Handler
```

TIL that we could use semicolons instead of ampersand in query strings (though this style is deprecated by W3C). Read more about it here: https://github.com/golang/go/issues/25192. This middleware is present in the stdlib for soving that problem by replacing the `;` with `&` under the hood. 

### MaxBytesHandler

```go
func MaxBytesHandler(h Handler, n int64) Handler
```

This could be used to limit the acceptable request body size. Under the hood it uses `MaxBytesReader`:

> MaxBytesReader prevents clients from accidentally or maliciously sending a large request and wasting server resources. If possible, it tells the ResponseWriter to close the connection after the limit has been reached.

### StripPrefix

```go
func StripPrefix(prefix string, h Handler) Handler
```

The docs says

> StripPrefix returns a handler that serves HTTP requests by removing the given prefix from the request URL's Path (and RawPath if set) and invoking the handler h.

My first impression is how could this be useful. Oh, wait for the blast! Here we go once again with a beautiful copy paste of an stdlib example.

```go
package main

import (
	"net/http"
)

func main() {
	// To serve a directory on disk (/tmp) under an alternate URL
	// path (/tmpfiles/), use StripPrefix to modify the request
	// URL's path before the FileServer sees it:
	http.Handle("/tmpfiles/", http.StripPrefix("/tmpfiles/", http.FileServer(http.Dir("/tmp"))))
}
```

### TimeoutHandler

```go
func TimeoutHandler(h Handler, dt time.Duration, msg string) Handler
```

Like the name says, it times out the handler if the request is taking more than the given duration.

## Third-party Middlewares

I came across this beautiful library called `chi` which comes loaded up with a bunch of middlewares out of the box: https://github.com/go-chi/chi?tab=readme-ov-file#middlewares

I would suggest starting with the default chi recommendation:

```go
  // A good base middleware stack
  r.Use(middleware.RequestID)
  r.Use(middleware.RealIP)
  r.Use(middleware.Logger)
  r.Use(middleware.Recoverer)
```

and then build up the chain. Go explore and catch 'em all!

(also let me know your favorite middlewares if you have one - because I am trying to discover more third party middlewares in Go)

## Communicate

When writing or using middlewares, you may need to pass down a variable that was created by one middleware into another middleware or in the request handler. In case of JS, we would just mutate the `request` object directly since it is dynamically typed :D (lol, good old days). In case of Go, we can't do that and we will need a way of passing through variable of any type via the available `ResponseWriter` or `Request` objects.

I have previously written a whole blog post on the [pitfalls of context.WithValue](https://vishnubharathi.codes/blog/context-with-value-pitfall) and when not to use them. And well, this is actually the use-case where you can use them!

A context variable is available to you in all the middlewares and the handlers via the `http.Request` object. We could use that to store and pass down information. 

```go

type RequestKey string

var (
	RequestIDKey RequestKey = "request-id"
)

func RequestID(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		ctx := context.WithValue(r.Context(), RequestIDKey, uuid.New())
		next.ServeHTTP(w, r.WithContext(ctx))
	})
}

func handlerThatUsesRequestID(w http.ResponseWriter, r *http.Request) {
	reqID, ok := r.Context().Value(RequestIDKey).(uuid.UUID)
	if !ok || reqID == uuid.Nil {
		fmt.Fprintln(w, "this a request without requestID")
		return
	}
	fmt.Fprintf(w, "request id is %s\n", reqID)
}
```

You still need to be careful while using `context.WithValue`. What if you miss calling a middleware, but try to look up the value that it is supposed to set in `r.Context`? It changes the trajectory of your request during runtime and in the worst-case it will lead to runtime panics in your handler. I am wondering if we could somehow catch this kind of stuff during compile time (like maybe by writing a library or perhaps someone already thought about this before - if so, let me know!)

## Chain

You might soon end up having to call multiple middlewares for your handlers. In that case, your code would look like:

```go
// middlewares for unauthenticated routes
http.Handle("/", Logger(RequestID(homeHandler))))

// middlewares for authenticated routes
http.Handle("/profile", Logger(RequestID(BasicAuth(userProfileHandler)))))
```

We need a way to chain the middlewares and store the chain so that we can re-use it between handlers. I recently discovered a library for this, which might help here: https://github.com/justinas/alice

```go
unAuth := alice.New(Logger, RequestID)
auth := alice.New(Logger, RequestID, BasicAuth)

http.Handle("/", unAuth.Then(homeHandler))
http.Handle("/profile", auth.Then(userProfileHandler))
```

You can also use routing library lke `chi` where the request middlewares are defined at the router level.

## Closing Thoughts

I hope this exploration was useful to you! It definitely made me learn some unexpected things like "when to use http.Handle? when to use http.HandleFunc? ....". This is also inspiring me to write a small middleware library that I have been thinking about.

~ ~ ~ ~

In an alternate universe, someone declared `type Middleware func(Handler) Handler` in `net/http` and (use your imagination).
