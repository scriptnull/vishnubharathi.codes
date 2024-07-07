---
title: Know when to break up with Go's http.DefaultClient
date: 2024-07-07 21:02:27
tags: ["go"]
---

These might be the first set of snippets that you see when trying to use Go's HTTP client. (taken from the "overview" section of [the standard library docs](https://pkg.go.dev/net/http))

```go
resp, err := http.Get("http://example.com/")
...
resp, err := http.Post("http://example.com/upload", "image/jpeg", &buf)
...
```

The same set of snippets has the potential to cause your first production outage. It is perfectly good code (up to a certain point). Things will start to get dirty when you introduce the following things into the mix:

- when your program is starting to make a lot of HTTP calls.
- when your program is making HTTP calls to more than one service (host names).

The reason behind it is this little variable declared in the `net/http` package.

```go
var DefaultClient = &Client{}
```

## Meet the DefaultClient

`DefaultClient` is of type `*http.Client` and `http.Client` is the struct that has all the code to perform HTTP calls. `DefaultClient` is a HTTP client with all the underlying settings pointing to the default values.

When you try calling those package-level HTTP methods like `http.Get`, `http.Post`, `http.Do` etc., the HTTP call is made using the `DefaultClient` variable. Two fields in the `http.Client` struct could translate the "default" and "shared" behavior of `http.DefaultClient` into potential problems:

```go
type Client struct {
	// Transport specifies the mechanism by which individual
	// HTTP requests are made.
	// If nil, DefaultTransport is used.
	Transport RoundTripper

  // ......

	// Timeout specifies a time limit for requests made by this
	// Client. The timeout includes connection time, any
	// redirects, and reading the response body. The timer remains
	// running after Get, Head, Post, or Do return and will
	// interrupt reading of the Response.Body.
	//
	// A Timeout of zero means no timeout.
	//
	// The Client cancels requests to the underlying Transport
	// as if the Request's Context ended.
	//
	// ....
	Timeout time.Duration
}
```

The default value for `Timeout` is zero, so the `http.DefaultClient` does not timeout by default and will try to hold on to a local port/socket as long as the connection is live. What if there are too many requests? Combine this with an HTTP server which doesn't timeout. Bingo! You got a production outage. You will run out of ports and there won't be newer ports available for making further HTTP calls.

Next up is the `Transport` field in the `http.Client`. By default, the following `DefaultTransport` would be used in `DefaultClient`.

```go
var DefaultTransport RoundTripper = &Transport{
	Proxy: ProxyFromEnvironment,
	DialContext: defaultTransportDialContext(&net.Dialer{
		Timeout:   30 * time.Second,
		KeepAlive: 30 * time.Second,
	}),
	ForceAttemptHTTP2:     true,
	MaxIdleConns:          100,
	IdleConnTimeout:       90 * time.Second,
	TLSHandshakeTimeout:   10 * time.Second,
	ExpectContinueTimeout: 1 * time.Second,
}
```
(a lot of things in there, but turn your attention to `MaxIdleConns`)

Here is the doc on what it does:

```go
	// MaxIdleConns controls the maximum number of idle (keep-alive)
	// connections across all hosts. Zero means no limit.
	MaxIdleConns int
```

Since the `DefaultClient` is shared, you might end up making calls to more than one service (host names) from it. In that case, there might be an unfair distribution of the `MaxIdleConns` maintained by the default client for the given set of hosts.

## A small example

Let us take an example here:

```go
type LoanAPIClient struct {}

func (l *LoanAPIClient) List() ([]Loan, error) {
  // ....
  err := http.Get("https://loan.api.example.com/v1/loans")
  // ....
}

type PaymentAPIClient struct {}

func (p *PaymentAPIClient) Pay(amount int) (error) {
  // ....
  err := http.Post("https://payment.api.example.com/v1/card", "application/json", &req)
  // ....
}
```

Both `LoanAPIClient` and `PaymentAPIClient` use the `http.DefaultClient` by calling into `http.Get` and`http.Post`. Let us say our program makes 80 calls from `LoanAPIClient` initially and then makes 200 calls from `PaymentAPIClient`. By default `DefaultClient` only maintains 100 maximum idle connections. So, `LoadAPIClient` will capture 80 spots in those 100 spots, and `PaymentAPIClient` will only get 20 remanining spots. This means that for the rest of 60 calls from `PaymentAPIClient`, a new connection needs to be opened and closed. This will cause unnecessary pressure on the payments API server. The allocation of these MaxIdleConns will soon get out of your hands! (trust me 😅)

## How do we fix this? 

Increase the `MaxIdleConns`? Yes, you can but if the client is still shared between `LoanAPIClient` and `PaymentAPIClient` then that too shall get out of hand at some scale.

I discovered the sibling of `MaxIdleConns` and that is `MaxIdleConnsPerHost`.

```go

	// MaxIdleConnsPerHost, if non-zero, controls the maximum idle
	// (keep-alive) connections to keep per-host. If zero,
	// DefaultMaxIdleConnsPerHost is used.
	MaxIdleConnsPerHost int
```

This could help in maintaining a predictable number of idle connections for each endpoint (host name).

## OK, how do I really fix this?

If your program is calling into more than one HTTP service, then you might most probably want to tweak other settings of the Client too. So, it might be beneficial to have a separate `http.Client` for these services. That way we can fine-tune them if needed in the future.

```go
type LoanAPIClient struct {
  http.Client
}

type PaymentAPIClient struct {
  http.Client
}
```

## It is fine

The conclusion would be this: It is okay to use `http.DefaultClient` to start with. But if you think you will have more clients and will make more API calls, avoid it.

Bonus: If you are authoring a library that has an API client, do a favor for your users: provide a way to customize the `http.Client` that you are using to make API calls. That way, your users have full control of what they would like to achieve while using your client.

~ ~ ~ ~

HTTP Clients inside an HTTP Server talking to another HTTP Server that has HTTP Clients, all authored by you. That will be your cue.
