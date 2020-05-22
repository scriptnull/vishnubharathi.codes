---
title: Some RSS feed reader features
date: 2020-05-22 06:48:00
tags: ["reading", "software"]
---

After all these years, I just started using an RSS reader. I recently read through this article ["If I could bring one thing back to the internet it would be blogs"](http://tttthis.com/blog/if-i-could-bring-one-thing-back-to-the-internet-it-would-be-blogs).

I think the blogs are still out there, but I just got too much attached to places like [HN](https://news.ycombinator.com/) on the internet. They have become that new RSS readers of these times.

I used to catch up on a handful of blogs/websites just by keeping a bookmark of those link in my browser and visiting them once in a while during those nights at my home after college. I didn't know a thing called RSS existing then. haha.

I have tried a few RSS feed apps before. But I kind of stop using them at some point.

I remember RSS readers used as example apps built for new app platforms. When Windows 8 from Microsoft came out, I think there used to be an RSS reader example app that was given to developers to get idea about Windows store apps. With the emergence of new RSS reader apps and with lots of people staying on good old RSS readers (I guess), writing a new RSS feed reader app is always welcome. You can do it as a programming exercise or release a new reader app that have the features you favour.

What I am going to do here is to just put up some features and ideas for an RSS reader app, that I would use/build.

## No sign ups
With the emergence of OAuth, people seem to like to bake in third-pary auth to everything they build. Forget OAuth, I just disovered an RSS reader app that asks you to fill out a form for creating an account, without which you can't use it any further.

![winds-rss](/images/winds-rss.png)

Each app is unique its own way. I understand the decision taken by the creators of those and choose to use an app that I like.

I am guessing that these apps with sign-ups are easier for syncing across devices etc.

May be not all sign-ups are bad.

So, may be an optional sign-up after the user starts using the app is ok. But even without the sign-up part, RSS reader still make it useful.

## Import and Export
The core input to an RSS reader is just a list of links.

With these links in hand, it should be easy to take them and put them in a new reader. Hence avoiding any vendor lock-in.

If I ever build an RSS reader, this would be my number one feature, right after the prototype.

I have been taught that we need to maintain good relationship with everyone, especially at the time of parting ways.

When you on-board to a new reader app, if the import feature didn't work properly you would simply not use the app. But when you use an app that doesn't allow you to export the list of links to feed it to a new app, then it is real pain.

After I started setting up my new RSS reader today, I noticed that [it](https://ravenreader.app/) has the button to export, but it ain't working. :/

Also, I found that [OPML](https://en.wikipedia.org/wiki/OPML) is the data format for exporting/importing RSS feeds. So when building this feature, keep a check to not reinvent the wheels.

## Categories
### A tree
A fairly simple RSS reader categorization technique is just to say, each of the RSS feed link we provide belongs to one category. So that you get folders of containing a list of blogs.

```
.
├── Companies
│   ├── company-blog-1
│   └── company-blog-2
├── People
│   ├── person-blog-1
│   └── person-blog-2
└── News
    ├── news-blog-1
    └── news-blog-2
```

### A deep tree
When you introduce sub-categories, you get a tree which has more depth.

```
.
└── Software
    ├── Companies
    │   ├── company-blog-1
    │   └── company-blog-2
    └── People
        ├── person-blog-1
        └── person-blog-2
```

Here the categories are `Software`, `Software->Companies`, `Software->People`.

### Graphs

What if we model categories as a graph.

```
.
├── Companies
│   └── company-blog-1
├── People
│   └── person-blog-1
└── Software
    ├── company-blog-1
    └── person-blog-1
```

This allows in a type of cateforization where a blog post could belong to more than one category.

### What would I choose
I think I would go with a Graph. It will serve simple as well as complex use cases.


### Unread and Favorites
RSS readers provide often provide a way to list all the unread articles and favorite articles.

Choosing a graph type of categorization naturally lead me to think of these features as just another categories in the reader.

When importing or adding a new RSS feed link to the app, all the articles that get added will be tagged with "unread" category. This should happen at times when a new article is available after syncing an RSS feed.

As far as favorites, users could just tag a post with "Favorite" and be done with it. The favorites section of my current feed reader doesn't allow categorizing posts inside the favorite category. This problem is also solved by having a graph.

### The forgotten world
I was surprised to see that some of the blogs (especially of tech companies) that I wished to follow along don't provide an RSS feed. Are people forgetting about the RSS world? I wonder!

Example: I wish to follow [Stripe's blog](https://stripe.com/blog) but I couldn't find an RSS feed link for it. It seems like we just got to visit the website for it. In this case, my old bookmarking style blog reading works! At the same time I discovered that [Stripe provides their status page as RSS feed](https://support.stripe.com/questions/subscribing-to-stripe-status-updates-in-an-rss-or-atom-feed-reader)

So, it would be good if our app can let us add links to webpages.

### Themes
When writing the frontend of the app, it would be great to have the notion of themes. Like let us say there is a tree view to see categories, then we would have a css class like `.tree-view`. This would help us overriding the original properties like background color, fonts etc. 

It should be good to start with two themes - light and dark. Allow custom themes.

### Master Feed
It makes me :sweat_smile: for mentioning at the last. Finally it would be good to have a master feed that aggregates posts from all the links that we have added.

### Enough

I think these features are enough for now. ( may be forever :D ) I will add if I missed out something or discover something that I might find useful.

So now, go build it and let me know. If you don't, I might!
