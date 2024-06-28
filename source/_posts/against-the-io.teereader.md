---
title: Against the io.TeeReader
date: 2024-06-29 00:07:19
tags: ["go"]
---

This is a follow-up blog post to my previous blog post about the `io.TeeReader` in Go. Here is the link for it if you haven't read it yet: https://vishnubharathi.codes/blog/a-silly-mistake-that-i-made-with-io.teereader/

## Motivation

The motivation for this blog post is [this Reddit comment](https://www.reddit.com/r/golang/comments/1dpfz28/comment/lah1uzz/). One of the reasons why I write blog posts and share them on the internet is because I almost always learn more from the comments. That comment made me think more about the code I wrote in the previous blog post and realize some things I want to write up here. (A big thanks to the people writing insightful comments on the internet)

## That weird `new(bytes.Buffer)`

To recap, I had a `io.Reader` as input and I was trying to read it twice so that I could upload the same data two times. Here is how the final solution looked like when using an `io.TeeReader`:

```go
func Upload(r io.Reader) error {
	contentForSecondUpload := new(bytes.Buffer)
	contentForFirstUpload := io.TeeReader(r, contentForSecondUpload)

	if err := firstUpload(contentForFirstUpload); err != nil {
		return err
	}

	if err := secondUpload(contentForSecondUpload); err != nil {
		return err
	}

	return nil
}
```

I always felt weird about the `new(bytes.Buffer)` that I have allocated in the code.

## The whole point

The whole point of `io.TeeReader` is to take in one source reader and perform reads on it efficiently and make the data available at the other two ends of the "T".

One of the highlights of that Reddit comment is, if I am allocating a buffer to store the contents of the source reader, why use a TeeReader at all?

> If you're going to allocate a buffer, then you might read the entire thing into memory first and read it twice.

That would look like

```go
func Upload(r io.Reader) error {
	contentForUpload, err := io.ReadAll(r)
	if err != nil {
		return err
	}

	if err := firstUpload(bytes.NewReader(contentForUpload)); err != nil {
		return err
	}

	if err := secondUpload(bytes.NewReader(contentForUpload)); err != nil {
		return err
	}

	return nil
}
```

This is a valid solution if I am okay with reading the entire input in memory and want my uploads to happen synchronously one after another.

## io.TeeReader + io.Pipe

The comment made me realize that we could use `io.TeeReader` and `io.Pipe` together to achieve concurrent uploads like my final solution in the previous blog post did.

```go
func Upload(r io.Reader) error {
	contentForSecondUpload, contentWriter := io.Pipe()
	contentForFirstUpload := io.TeeReader(r, contentWriter)

	var upload errgroup.Group
	upload.Go(func() error {
		return firstUpload(contentForFirstUpload)
	})
	upload.Go(func() error {
		return secondUpload(contentForSecondUpload)
	})
	return upload.Wait()
}
```

I am going to take this step by step. The above program would cause a deadlock. The reason: `contentWriter` is not closed and the `secondUpload` will always be waiting for more content to be available which it will never receive. To fix it, we must close the `contentWriter` somewhere, but where?

In the case of the pure `io.Pipe` implementation in the previous blog post, it was clear: We close the writers in the go routine where we finish the writing.

In the case of a TeeReader, the writes for `contentForSecondUpload` is complete when the read of `contentForFirstUpload` is finished. That looks like:

```go
func Upload(r io.Reader) error {
	contentForSecondUpload, contentWriter := io.Pipe()
	contentForFirstUpload := io.TeeReader(r, contentWriter)

	var upload errgroup.Group
	upload.Go(func() error {
		var err error
		defer func() {
			contentWriter.CloseWithError(err)
		}()
		err = firstUpload(contentForFirstUpload)
		return err
	})
	upload.Go(func() error {
		return secondUpload(contentForSecondUpload)
	})
	return upload.Wait()
}
```

I feel that the above code would be hard to follow. It can easily make one spend time thinking about "why would they close the writer of the second reader after reading the first reader?".

The pure `io.Pipe` implementation feels more natural and human-friendly: we close the writer in the go routine where we are done writing to all the writers. At the same time, it gets the job done.

## Verdict

I will avoid using `io.TeeReader` at all places and prefer using `io.Pipe + io.MultiWriter` instead. (the code from the previous blog post)

That makes the code efficient, concurrent, and easy to read/write/extend.

~ ~ ~ ~

Always use the pipe and close it.
