---
title: Some RSS feed reader features
date: 2020-05-22 06:48:00
tags: ["reading", "software", "want-to-build"]
---

After all these years, I just started using an RSS reader. I recently read through this article ["If I could bring one thing back to the internet it would be blogs"](http://tttthis.com/blog/if-i-could-bring-one-thing-back-to-the-internet-it-would-be-blogs).

I think the blogs are still out there, but I just got too much attached to places like [HN](https://news.ycombinator.com/) on the internet. They have become that new RSS readers of these times.

I used to catch up on a handful of blogs/websites just by keeping a bookmark of those link in my browser and visiting them once in a while during those nights at my home after college. I didn't know a thing called RSS existing then. haha.

I have tried a few RSS feed apps before. But I kind of stop using them at some point.

I remember RSS readers used as example apps built for new app platforms. When Windows 8 from Microsoft came out, I think there used to be an RSS reader example app that was given to developers to get idea about Windows store apps. With the emergence of new RSS reader apps and with lots of people staying on good old RSS readers (I guess), writing a new RSS feed reader app is always welcome. You can do it as a programming exercise or release a new reader app that have the features you favour.

What I am going to do here is to just put up some features and ideas for an RSS reader app, that I would use/build.

## No sign ups
With the emergence of OAuth, people seem to like to bake in third-pary auth to everything they build. Forget OAuth, I just disovered an RSS reader app that asks you to fill out a form for creating an account when you boot into the app, without which you can't use it any further.

![winds-rss](/images/winds-rss.png)

Each app is unique its own way. I understand the decision taken by the creators of those.

I am guessing that these apps with sign-ups are easier for syncing across devices etc.

May be not all sign-ups are bad. But I wish not get in the way of these little humans on the internet who are trying to categorize bunch of knowledge with a "Sign up or I won't let you categorize things" attitude.

So, may be an optional sign-up after the user starts using the app is ok. But even without the sign-up part, RSS reader still make it useful.

## Import and Export
The core input to an RSS reader is just a list of links.

With these links in hand, it should be easy to take them and put them in a new reader. Hence avoiding any vendor lock-in.

If I ever build an RSS reader, this would be my number one feature, right after the prototype.

I have been taught that we need to maintain good relationship with everyone, especially at the time of parting ways.

When you on-board to a new reader app, if the import feature didn't work properly you would simply not use the app. But when you use an app that doesn't allow you to export the list of links to feed it to a new app, then it is real pain.

After I started setting up my new RSS reader today, I noticed that [it](https://ravenreader.app/) has the button to export, but it ain't working. :/

Also, I found that [OPML](https://en.wikipedia.org/wiki/OPML) is the data format for exporting/importing RSS feeds. So when building this feature, keep a check to not reinvent the wheels.

## Avoid paywalls
I understand that you might be interested in monetizing the app. It's up to you! But here are my thoughts on it.

I think I would not put up a paywall for our new RSS reader. I kind of hate saying "Pay me $x then only you can access this nice little feature." to my user.

Here is an example paywall in a famous RSS reader app called [feedly](https://feedly.com/). When reading an article, I selected something and noticed that a "highlight" option is present.

![feedly-highlight](https://user-images.githubusercontent.com/4211715/82920631-2355f200-9f95-11ea-86b5-953111cfe64b.png)

I said, "oh great, let me hightlight and take notes" and clicked on the "hightlight" button. Then I was slapped with this page on my screen asking me to pay up.

![feedly-paywall](https://user-images.githubusercontent.com/4211715/82921449-02da6780-9f96-11ea-9f37-aba42c0d8623.png)

I think there are other ways of monetizing, but this one feels not so right for me. I think we should be better of getting donations ("pay whatever you like for this piece of software, or don't pay at all"). Critics say this to be a not so feasible way of monetizing software. But I don't care.

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

For example, you could query things like "show all unread blog posts", "show all unread blog posts in a software category", "show all unread blog posts in software and companies categories".

## Unread and Favorites
RSS readers provide often provide a way to list all the unread articles and favorite articles.

Choosing a graph type of categorization naturally lead me to think of these features as just another categories in the reader.

When importing or adding a new RSS feed link to the app, all the articles that get added will be tagged with "unread" category. This should happen at times when a new article is available after syncing an RSS feed.

As far as favorites, users could just tag a post with "Favorite" and be done with it. The favorites section of my current feed reader doesn't allow categorizing posts inside the favorite category. This problem is also solved by having a graph.

## Unseen Vs Unread; notify!
Notifications are great when done within some bounds. The right type of notification that I would expect from my RSS reader app is to "Show the count of new articles in the system tray".

I am focusing on a RSS reader app that is primarily aimed at desktops, rather than mobiles. Hence the system tray terminology.

Here is an example of system tray.

![system-tray](https://user-images.githubusercontent.com/4211715/82918742-c1948880-9f92-11ea-84fb-9c8fa49207e1.png)

If you notice closely, here is the notification for slack app. Instead of a blue dot, we would expect a number of "unseen/unread" articles on the logo of our app.

![slack-notify](https://user-images.githubusercontent.com/4211715/82918939-01f40680-9f93-11ea-9569-1474fdb1348a.png)

It is important to distinguish unseen vs unread to get to the way of doing notifications right!

When an article occurs for the first time, it will get both "unseen" and "unread" tag on it. When the user sees the article list on the app, the "unseen" tag is removed and "seen" tag is added instead. When the article is actually read by the user, "unread" tag is removed and "read" tag is added. "unseen"->"seen" transistion is done automatically by the app when the user sees the new article in a feed list UI on the app. But "unread"->"read" transistion happens when the user of the app explicitly marks an article to be "read". This is popular among many RSS readers; there is a "Mark as read" button on every article.

with that distinction made, I think it makes sense to just notify for "unseen" articles instead of "unread" articles. Ofcourse, it could be easy to have a switch in settings panel for more vigorous readers to notify the count of "unread" article instead of "unseen". But the default is "unseen".

## The forgotten world
I was surprised to see that some of the blogs (especially of tech companies) that I wished to follow along don't provide an RSS feed. Are people forgetting about the RSS world? I wonder!

Example: I wish to follow [Stripe's blog](https://stripe.com/blog) but I couldn't find an RSS feed link for it. It seems like we just got to visit the website for it. In this case, my old bookmarking style blog reading works! At the same time I discovered that [Stripe provides their status page as RSS feed](https://support.stripe.com/questions/subscribing-to-stripe-status-updates-in-an-rss-or-atom-feed-reader)

So, it would be good if our app can let us add links to webpages.

## Themes
When writing the frontend of the app, it would be great to have the notion of themes. Like let us say there is a tree view to see categories, then we would have a css class like `.tree-view`. This would help us overriding the original properties like background color, fonts etc. 

It should be good to start with two themes - light and dark. Allow custom themes.

## Master Feed
It makes me :sweat_smile: for mentioning this at the last. Finally it would be good to have a master feed that aggregates posts from all the links that we have added.

## Preview reader
A basic preview reader for reading the articles would be nice!

## Other RSS feed reader apps
I will use this section to collect information regarding various other RSS feed readers.

### Feedly
This is my favorite RSS reader. It is web-based and also has nice Android client. Already added the screenshot for pricing details above!

Homepage: https://feedly.com/

### NetNewsWire

Seems to be a popular option for Mac and iOS.

I really like some literatures present in the internet on NetNewsWrite; like this nice blog post from [Brent Simmons](https://inessential.com) (author of this app) on [Why NetNewsWire is Fast](https://inessential.com/2020/05/18/why_netnewswire_is_fast) and also this document on [How to support NetNewsWire](https://github.com/Ranchero-Software/NetNewsWire/blob/master/Technotes/HowToSupportNetNewsWire.markdown)

Homepage: https://ranchero.com/netnewswire/

### NewsBlur
"Up to 64 sites" if we don't pay for the app. That's all I wanted to say about this. Added the rest as screenshots.

Homepage: https://newsblur.com/

![newsblur-1](https://user-images.githubusercontent.com/4211715/85141905-2aef7a80-b265-11ea-8413-970e35e711f8.png)

![newsblur-2](https://user-images.githubusercontent.com/4211715/85141271-24acce80-b264-11ea-87c7-a5bb290c767b.png)

## Enough

I think these features are enough for now. ( may be forever :D ) I will add if I missed out something or discover something that I might find useful.

EDIT: I started adding new feature specs to this document already.

So now, go build it and let me know. If you don't, I might!
