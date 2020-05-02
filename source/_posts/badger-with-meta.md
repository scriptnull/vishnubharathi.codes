---
title: Badger - WithMeta with love
date: 2020-05-03 01:00:00
tags: ["programming", "API"]
---

This weekend I ended up reading about an open source project called [Badger](https://github.com/dgraph-io/badger).

To give a short idea about what Badger is, here is an excerpt from the project page.

> BadgerDB is an embeddable, persistent and fast key-value (KV) database written in pure Go. It is the underlying database for Dgraph, a fast, distributed graph database. It's meant to be a performant alternative to non-Go-based key-value stores like RocksDB.

I have been dealing with caches and key-value stores mostly at work for a while amd I am generally interested in the API design, internals, client implementations, etc. of key-value stores. So I just started by reading the [README](https://github.com/dgraph-io/badger/blob/master/README.md) to understand what it has to provide.

## Discovery

When reading on how to use the Badger API methods to perform basic key-value operations, I happen to discover something in the docs which completely put a smile on my face!

It's the presence of this little method called `WithMeta`

All you can do with it is store some metadata (of atmost a size of `byte`) alongside a key-value data.

hmm, ok! just a `byte`? just 8 bits? All you can do is store an unsigned integer ( 0 through 255 ) alongside the key-value data. What can you possibly do with it? Why is it like this? Why not allow a bigger metadata value to be stored?

So, we got some questions to start with :D

Have you had those "why is it present? just why?" moments when using an API before? This case might just be that for people who are getting started in using a key-value store.

I will try to explain a few details, that might give you answers.

## Entry

It all started with what I call the Entry API in Badger. Lets read some snippets, one at a time ;)

The starting point of saving a key-value pair in Badger is using the `txn.Set` method.

```go
err := db.Update(func(txn *badger.Txn) error {
  err := txn.Set([]byte("answer"), []byte("42"))
  return err
})
```

Immediately after that, the discussion about the Entry API starts. The same effect as above code could be achieved by the below snippet.

```go
err := db.Update(func(txn *badger.Txn) error {
  e := badger.NewEntry([]byte("answer"), []byte("42"))
  err := txn.SetEntry(e)
  return err
})
```

Two ways to do one thing, why? It seems like `txn.Set` is targetted at users who just want to set a key-value and just done with it. But with `txn.SetEntry` more things are possible.

If you want to set a TTL on a key-value data - you must be using `txn.SetEntry` instead of `txn.Set`. 

```go
err := db.Update(func(txn *badger.Txn) error {
  e := badger.NewEntry([]byte("answer"), []byte("42")).WithTTL(time.Hour)
  err := txn.SetEntry(e)
  return err
})
```

Just like the fact that you could use `WithTTL` to add a TTL to an entry, we could use `WithMeta` to store a metadata information about the key-value data.

```go
err := db.Update(func(txn *badger.Txn) error {
  e := badger.NewEntry([]byte("answer"), []byte("42")).WithMeta(byte(1))
  err := txn.SetEntry(e)
  return err
})
```

## Readthis
That's quite some golang to digest. While you are at it, we will take a break to discuss about a popular gem called [readthis](https://github.com/sorentwo/readthis); some ruby code - coming up next!

> Readthis is a Redis backed cache client for Ruby.

The part that I want to concentrate on it is the place where readthis exposes an API to store and retrieve key-value data.

Note: I am trying to compare + co-relate the API rather than comparing the key-value stores itself: Badger Vs Redis is not happening here. All I am trying to do is show how a bunch of methods signatures that are present for doing the basic storage operations and make a conclusion.

The method for storing a key-value pair with readthis seems like this

```ruby
require 'readthis'

cache = Readthis::Cache.new

cache.write('answer', 42)
```

Ok, listen more closely from now on. This is the place where things start to make more sense.

Generally when you are trying to store a key-value pair in a key-value store, you might find yourself storing the data in some kind of format.

When the data to be stored is simple, we could just store the string in raw format (like plain text value for a key)

When you want to store some complicated information (like an object or struct), that is where things start to get interesting.
