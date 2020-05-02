---
title: Badger - WithMeta with cheers!
date: 2020-05-03 01:00:00
tags: ["programming", "API"]
---

This weekend I ended up reading about an open-source project called [Badger](https://github.com/dgraph-io/badger).

To give a short idea about what Badger is, here is an excerpt from the project page.

> BadgerDB is an embeddable, persistent and fast key-value (KV) database written in pure Go. It is the underlying database for Dgraph, a fast, distributed graph database. It's meant to be a performant alternative to non-Go-based key-value stores like RocksDB.

I have been dealing with caches and key-value stores mostly at work for a while and I am generally interested in the API design, internals, client implementations, etc. of key-value stores. So I just started by reading the [README](https://github.com/dgraph-io/badger/blob/master/README.md) to understand what it has to provide.

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

Immediately after that, the discussion about the Entry API starts. The same effect as the above code could be achieved by the below snippet.

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

Just like the fact that you could use `WithTTL` to add a TTL to entry, we could use `WithMeta` to store metadata information about the key-value data.

```go
err := db.Update(func(txn *badger.Txn) error {
  e := badger.NewEntry([]byte("answer"), []byte("42")).WithMeta(byte(1))
  err := txn.SetEntry(e)
  return err
})
```

## Data

Ok, listen more closely from now on. This is the place where things start to make more sense.

Generally, when you are trying to store a key-value pair in a key-value store, you might find yourself storing the data in some kind of format.

When the data to be stored is simple, we could just store the string in raw format (like plain text value)

When you want to store some complicated information (like an object or struct), that is where things start to get interesting.

Consider a ruby hash that gets stored in a key-value store, which we might need to retrieve back from the store at the point of time in the future or perhaps in another ruby process running on some other machine.

This demands us in storing the information in a serialized format. If you are puzzling what it is, I highly recommend you to read through [this](https://en.wikipedia.org/wiki/Serialization).

To simply put it, you will need to convert the object into an array of bytes (a string representation) which could be easily sent over the network or written to a file. At the same time, the format should allow reading the serialized value and construct back the object.

```ruby
user_data = { id: 1, name: 'Naruto', village: 'leaf'}

serialized_val = Marshal.dump(user_data)

# serialized_val will holds the string representation of user_data
# "\x04\b{\b:\aidi\x06:\tnameI\"\vNaruto\x06:\x06ET:\fvillageI\"\tleaf\x06;\aT"

cache.write('user_1', serialized_val)
```

At the reader's end, you will need to do

```ruby
serialized_val = cache.get('user_1')

user_data = Marshal.load(serialized_val)
```

Now, what will we do when we want to read the information in our ruby object in some other service written in some other programming language (Example: a node.js process trying to process our user data)

The solution is to serialize the data using a format that both the services could understand. (In our example, we could convert user data into a JSON string and store it in DB. This will enable us to read the data from any programming language that could deserialize JSON)

So, it is kind of obvious that when storing key-value data, the general use-case is to store it in some kind of format, and _we need a way to store in which format a data is stored_. This will help the readers of the value to use appropriate deserializer to retrieve the information.

This is where we could take advantage of `WithMeta` - to store which serialization format is being used while writing the key-value data.

## Readthis
We will discuss about a popular gem called [readthis](https://github.com/sorentwo/readthis) to resume our API admiration process :D

> Readthis is a Redis backed cache client for Ruby.

The part that I want to concentrate on it is the place where readthis exposes an API to store and retrieve key-value data.

Note: I am trying to compare + co-relate the API rather than comparing the key-value stores itself: Badger Vs Redis is not happening here. All I am trying to do is show how a bunch of methods signatures that are present for doing the basic storage operations and make a conclusion.

The method for storing a key-value pair with readthis seems like this

```ruby
require 'readthis'

cache = Readthis::Cache.new

cache.write('answer', 42)
```

> Readthis uses Ruby's Marshal module for serializing all values by default.

Apart from that, it supports using the following serializers

- Marshal (Native ruby object serialization format)
- JSON (Javascript Object Notation)
- Passthrough (Raw string)

If we try to dig in the [source code](https://github.com/sorentwo/readthis/blob/541c4227b92f6bcd76c647ff95e7783f896259c3/lib/readthis/serializers.rb#L42-L46) for this, we can notice

```ruby
BASE_SERIALIZERS = {
  Marshal => 0x1,
  Passthrough => 0x2,
  JSON => 0x3
}.freeze
```
This is where API comparison part kicks in, uff finally :D

When readthis tries to write information in one of the above formats, it tries to store both the data and the serialization format together in the key-value pair.

But the key-value store here (Redis) does not have an API to store metadata information separately. So, readthis works around by prefixing the values with a byte which represents the serialization format. Further, this byte also contains information regarding if the data is compressed or not.

So, the data stored is not serialized data. Instead it is `metadata byte` + `serialized data`. ([link to source](https://github.com/sorentwo/readthis/blob/541c4227b92f6bcd76c647ff95e7783f896259c3/lib/readthis/entity.rb#L104-L128))

```ruby
def compose(value, marshal, compress)
  flags = serializers.assoc(marshal)
  flags |= COMPRESSED_FLAG if compress

  value.prepend([flags].pack('C'))
end

def decompose(string)
  flags = string[0].unpack('C').first

  if flags < 16
    marshal = serializers.rassoc(flags)
    compress = (flags & COMPRESSED_FLAG) != 0

    [marshal, compress, string[1..-1]]
  else
    [@options[:marshal], @options[:compress], string]
  end
end
```

The key-store not exposing an API to set metadata results in magical workarounds by a client library, which other client libraries written in other programming languages have no idea of. So, the user of the library has to bear with the pain of going through the internals of how a library constructs the value part of a key-value data to access it from some other place.

All because of the reason that the key-store API doesn't expose a simple method to store the metadata.

## Cheers!

When I first saw the `WithMeta` method, I was completely surprised. I hoped people (especially starters) might wonder about it. So, I sat down to write this post down. Hopefully, my thoughts would have answered the questions that I asked at the start of this blog post.

Never thought that having an extra byte in a struct would make me this much cheerful :D 

`WithMeta` API feels to be a result of careful design. A proof of that might be the data-type used. Why use a `byte` to store metadata instead of having some other datatype? Because the designer(s) of the API was able to sense the obvious and avoid a whole bunch of pain for the users like I mentioned earlier.

Whatever be it, they got it right!
