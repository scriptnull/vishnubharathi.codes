---
title: Exploring Middlewares in Go
date: 2024-05-21 00:10:08
tags: ["go"]
---

I came across "Middlewares" for writing HTTP servers originally in the Node.js ecosystem. There is this beautiful library called [express](https://expressjs.com/) which sparked the joy of middlewares in me. In case if you haven't heard of middlewares before, I think you should read [this beautiful page](https://expressjs.com/en/guide/using-middleware.html) from express documentation to get a taste of them. (I genuinely feel that it is the best possible introduction for middleware, hence opening up the post with it)

With enough Javascript for the day, we will jump into Go now. 😅

My goal for this post is to understand how to {use, write} middlewares in Go HTTP servers. We will also try to search the internet and surface some Go middlewares that we can add to our day to day toolkit.

## Problem

Let us take a simple problem and work our way upwards. Here is the problem statement:

Write a HTTP server that contains multiple routes. When a request is made to a route, print a log line at the start and the end of the request. Something like

```
2024/05/21 00:39:39 INFO start method=GET path=/one
2024/05/21 00:39:39 INFO start method=GET path=/one
2024/05/21 00:39:42 INFO start method=GET path=/two
2024/05/21 00:39:42 INFO end method=GET path=/two
```

## Solution

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
		defer slog.Info("start", "method", r.Method, "path", r.URL.Path)

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
