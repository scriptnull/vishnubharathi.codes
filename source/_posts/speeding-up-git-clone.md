---
title: Speeding up git clone
date: 2021-02-03 07:53:04
tags: ["devops","tools","productivity"]
---

Imagine that you need to take the latest source code of a project and deploy it somewhere by creating some artifacts with it. If it is a git project with a few commits, a simple `git clone .....` would do it. But if it is a project with thousands of commits, then you might be bored of your time waiting for the git clone to complete while deploying.

I recently discovered about something called shallow clones in git. The idea is simple: instead of getting all the commits of a git repo, shallow clone only gets the latest commit. The `--depth=N` flag seems to enable shallow cloning in git where N is the number of latest commits to be fetched.

Here is an example for comparing how these much of a time you can save:

I tried cloning the redis project - https://github.com/redis/redis which had 10,009 commits while cloning.

```
$ time git clone git@github.com:redis/redis.git
Cloning into 'redis'...
remote: Enumerating objects: 29, done.
remote: Counting objects: 100% (29/29), done.
remote: Compressing objects: 100% (21/21), done.
remote: Total 71995 (delta 11), reused 17 (delta 8), pack-reused 71966
Receiving objects: 100% (71995/71995), 91.10 MiB | 375.00 KiB/s, done.
Resolving deltas: 100% (51230/51230), done.

real	4m15.938s
user	0m13.796s
sys	0m2.875s
```

So normal clone took `4 minutes and 15 seconds` to complete.

Here is the same thing but with a shallow clone
```
$ time git clone --depth=1 git@github.com:redis/redis.git
Cloning into 'redis'...
remote: Enumerating objects: 937, done.
remote: Counting objects: 100% (937/937), done.
remote: Compressing objects: 100% (843/843), done.
remote: Total 937 (delta 105), reused 568 (delta 70), pack-reused 0
Receiving objects: 100% (937/937), 2.58 MiB | 390.00 KiB/s, done.
Resolving deltas: 100% (105/105), done.

real	0m12.802s
user	0m0.621s
sys	0m0.167s

```

And shallow clone took just `12 seconds` to complete.

so fast!
