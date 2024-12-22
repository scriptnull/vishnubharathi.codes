---
title: Baking a React App into a Go server
date: 2024-12-22 23:21:09
tags: ["go","programming"]
---

After many long years, I am trying to write a small web UI for a side project. It is going to be a single-page application that I would like to be served from my server written in Go. I was introduced to [vite](https://vite.dev/) which gave me a hello world [react](https://react.dev/) app that gave me web assets like

```
webapp/
├── dist
│   ├── assets
│   │   ├── index-n_ryQ3BS.css
│   │   ├── index-uO412iEj.js
│   │   └── react-CHdo91hT.svg
│   ├── index.html
│   └── vite.svg
├── index.html
```

## Basic serve

In order to serve that app from my Go server, I would initialize it to be a go package that exposes a web server that serves it. That means creating `webapp/webapp.go` in our vite project.

```go
package webapp

import (
	"fmt"
	"net/http"
)

type Server struct {
	*http.Server
}

func New(addr string) *Server {
	routes := http.NewServeMux()

	routes.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintln(w, "TODO")
	})

	return &Server{
		Server: &http.Server{
			Addr:    addr,
			Handler: routes,
		},
	}
}
```

Now our react app is also a Go package which could be consumed from other packages like this

```go
webServer := webapp.New(webServerAddr)
if err := webServer.ListenAndServe(); err != nil {
	log.Fatalln("Error starting web server", err)
}
```

## Searching for a handler

We would like to serve whatever is in our  `dist` folder when someone hits our web server. So I searched if there were any such handlers and found two such functions in the standard library.  So that we could register the handler in our `routes` ServeMux.

```go
func FileServer(root FileSystem) Handler
func FileServerFS(root fs.FS) Handler
```

The difference between them is their arguments. `FileSystem` is part of the `net/http` library and I found this note about it in the comments:

```go
// This interface predates the [fs.FS] interface, which can be used instead:
// the [FS] adapter function converts an fs.FS to a FileSystem.
type FileSystem interface {
	Open(name string) (File, error)
}
```

So it is a deprecated interface in favor of a new interface. That leaves us with `fs.FS`.

It seems like `fs.FS` is an interface that represents a file system and is present in the [io/fs package](https://pkg.go.dev/io/fs). I remember that they introduced the `io` package in the standard library to deprecate the `ioutil` package and this should have been a sweet addition that came with it?

Anyway, we will choose `FileServerFS` now.

```go
routes.Handle("/", http.FileServerFS(????))
```

## A filesystem

So we need a filesystem that we can give to our `http.FileServerFS()` method. I searched through the possible implementations of `fs.FS` interface and the first one that I was able to surface is `os.DirFS`.

It is a function that gives `fs.FS` based on the contents of a file system directory.

```go
routes.Handle("/", http.FileServerFS(os.DirFS("/home/vishnu/pers/gokakashi/webapp/dist")))
```

The problem with this approach is, that we will hit troubles when we ship our server to a machine on the internet. Now, someone has to take care of creating `/home/vishnu/pers/gokakashi/webapp/dist` on the server machine or point to a directory that contains our web app's assets. That becomes messy, right?

What I would ideally want is to embed all my HTML, CSS, JS files inside our go server binary itself. That way we ship only the binary and it will be able to serve the web app.

## Baking

I have heard of the `embed` package which could be used for embedding files inside the go binary. There is `embed.FS` which satisfied `fs.FS` interface. So we could probably use it to bake in our assets.

```go
//go:embed dist
var WebAssets embed.FS
```

We make use of it like

```go
routes.Handle("/", http.FileServerFS(WebAssets))
```

This renders:
![image](https://github.com/user-attachments/assets/2fa7a78e-eeb1-4aaf-b969-01c38e044777)

(not quite, what we want) Instead of embedding what is inside dist folder, we have embedded the `dist` folder itself. To inspect what got embedded, we could use the `go list` command like this:

```
$ go list -f '{{.EmbedFiles}}' .
[dist/assets/index-n_ryQ3BS.css dist/assets/index-uO412iEj.js dist/assets/react-CHdo91hT.svg dist/index.html dist/vite.svg]
```

I tried doing `//go:embed dist/*` instead of `//go:embed dist`, that didn't help as well because (from Go docs)

> The difference is that ‘image/*’ embeds ‘image/.tempfile’ while ‘image’ does not. Neither embeds ‘image/dir/.tempfile’.

If I used `//go:embed dist/index.html`, then the file seems to be still embedded with the `dist` folder.

```
$ go list -f '{{.EmbedFiles}}' .
[dist/index.html]
```

I was wondering if there is a way to embed the contents of `dist` at the root of the FS instead of the FS directory. There seems to be no provision in the `embed` package to do it. Because it operates at a package level, and it would force us to declare `dist` as a separate go package and would force us to remove `dist` folder from `.gitignore`. That would be messy.

## Traverse

We know that we can't change the root of the file system, but what if we traverse to a folder and get an `fs.FS` representation that projects the selected directory as the root? I suspected that there might be method to help with that in the `io/fs` package.

yep, look what I discovered:

```go
// Sub returns an FS corresponding to the subtree rooted at fsys's dir.
func Sub(fsys FS, dir string) (FS, error)
```

Now, we just make use of it like this

```go
//go:embed dist
var WebAssets embed.FS

func New(addr string) (*Server, error) {
	routes := http.NewServeMux()

	reactApp, err := fs.Sub(WebAssets, "dist")
	if err != nil {
		return nil, fmt.Errorf("error finding the dist folder: %w", err)
	}

	routes.Handle("/", http.FileServerFS(reactApp))

	return &Server{
		Server: &http.Server{
			Addr:    addr,
			Handler: routes,
		},
	}, nil
}
```

And boom!

![Screenshot from 2024-12-21 12-48-57](https://github.com/user-attachments/assets/150ae840-d520-47e8-9e87-ddf01713614f)

## Compile time

The `//go:embed dist` directive is evaluated during compile time. So when you run `go build`, the compiler looks for a `dist` folder and bakes it in the binary.

Let us say we miss generating the `dist` folder (maybe we failed running `npm run build`), that would lead to a compile-time error

```
$ go build 
webapp/webapp.go:14:12: pattern dist: no matching files found
```

This way we get the guarantee that no one is able to build our Go app without building the frontend that is intended to be embedded in it.
