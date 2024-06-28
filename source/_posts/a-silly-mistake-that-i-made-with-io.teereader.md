---
title: A silly mistake that I made with io.TeeReader
date: 2024-06-27 06:09:47
tags: ["go"]
---

I recently made a silly mistake while using `io.TeeReader` in Go and I am writing this blog post to sum up my learnings from this experience.

## Why I used it in the first place

Ok, here is why I chose to use it in the first place: I had some content and two functions that needed that content and perform uploads to two different HTTP endpoints. Something like

```go
func main() {
	Upload(strings.NewReader("hello world"))
}

func Upload(r io.Reader) error {
	if err := firstUpload(r); err != nil {
		return err
	}

	if err := secondUpload(r); err != nil {
		return err
	}

	return nil
}

func firstUpload(r io.Reader) error {
	content := io.MultiReader(strings.NewReader("first upload:"), r, strings.NewReader("\n"))
	if _, err := io.Copy(os.Stdout, content); err != nil {
		return err
	}

	return nil
}

func secondUpload(r io.Reader) error {
	content := io.MultiReader(strings.NewReader("second upload:"), r, strings.NewReader("\n"))
	if _, err := io.Copy(os.Stdout, content); err != nil {
		return err
	}

	return nil
}
```

The output of the above program would be

```
first upload:hello world
second upload:
```

The first upload consumes all the data from the reader and by the time the reader reaches the second upload, there isn't anything to be read. If this is new to you, I encourage you to take a look at the standard lib docs for `io.Reader` to better understand the situation: https://pkg.go.dev/io#Reader

## Using TeeReader (but with my mistake)

OK, so what do I do now? I google search the problem and discover about Go's [io.TeeReader](https://pkg.go.dev/io#TeeReader). Let us see what the program would look like after I tried to use the TeeReader.

```go
func Upload(r io.Reader) error {
	contentForFirstUpload := new(bytes.Buffer)
	contentForSecondUpload := io.TeeReader(r, contentForFirstUpload)

	if err := firstUpload(contentForFirstUpload); err != nil {
		return err
	}

	if err := secondUpload(contentForSecondUpload); err != nil {
		return err
	}

	return nil
}
```

And the output for this is

```
first upload:
second upload:hello world
```

That is weird. The second upload is succeeding but not the first one?

## Fixing the mistake

This probably is the best place to quote the docs of `io.TeeReader`:

```go
func TeeReader(r Reader, w Writer) Reader
```

> TeeReader returns a Reader that writes to w what it reads from r. All reads from r performed through it are matched with corresponding writes to w. There is no internal buffering - the write must complete before the read completes. Any error encountered while writing is reported as a read error.

So we get back a Reader (`contentForSecondUpload` in our case) and when that is read, a simultaneous write is happening to the writer (`contentForFirstUpload` in our case) that we pass. But what happens in the code is, we try to read from the writer before writes are happening to it.

I am not sure if I did a good job of explaining the fix in plain words above, but here is the code that fixes the problem:

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

So rule no.1 here is: always read the reader returned back from `io.TeeReader` first. That is the thing that is copying the data and making it available for the other buffer (writer).

That's it, that is the only rule.

## io.Pipe

Now that we have fixed the problem, I think we can take a short detour to visit one of my favorite Go constructs: `io.Pipe` which could also help solve these kinds of problems.

Here is a quick refactor of our code using `io.Pipe`.

```go
func Upload(r io.Reader) error {
	var upload errgroup.Group

	fr, fw := io.Pipe()
	upload.Go(func() error {
		return firstUpload(fr)
	})

	sr, sw := io.Pipe()
	upload.Go(func() error {
		return secondUpload(sr)
	})

	upload.Go(func() error {
		var err error
		defer func() {
			fw.CloseWithError(err)
			sw.CloseWithError(err)
		}()

		_, err = io.Copy(io.MultiWriter(fw, sw), r)
		return err
	})

	return upload.Wait()
}
```

This has some advantages and one of them would have helped me in avoiding my mistake with `io.TeeReader`.
- uploads become concurrent naturally unlike TeeReader where it is sequential.
- the order in which we read the readers for the first upload and second upload does not matter anymore.

With that said, I would still be mindful about introducing `io.Pipe`. Here is what I have decided.

If I need to write to one or two writers and do not need concurrency, I would stick with `io.TeeReader`. I will stick to `io.Pipe` for every other case.

I have changed my mind a bit, please turn to the next page: https://vishnubharathi.codes/blog/against-the-io.teereader/
