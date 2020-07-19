---
title: Scribble
date: 2017-09-13 04:00:00
tags: ["blogging", "js13kgames", "javascript", "gaming"]
---
It’s the name of the game, I am about to develop now. Time is Sept 10, 2017 7:34 PM IST when I am starting to type this post.

![](https://cdn-images-1.medium.com/max/2000/1*0NVnpOq-kr2m4eVHGf_OCg.png)

The thought to develop a game first occurred to me after I read [this blog post from github](https://github.com/blog/2409-build-a-game-in-13kb-or-less-with-js13kgames). It was about a game development competition called [JS13KGAMES](http://js13kgames.com/). It’s a competition in which a game has to be coded and the source files should be within 13 kilobytes.

I shared this with some of my friends. [One of them](https://twitter.com/riturajcse) took time and got his game out.
[**The Lost Elephant | js13kGames**
*An elephant has lost his way to his friends. You have to help him reach his friends without getting killed by speeding…*js13kgames.com](http://js13kgames.com/entries/the-lost-elephant)

He happened to write it in under 3 hours and he said it was inspired by the Cross Creeper game that we played in an Arcade outside our office the day before. That’s cool !

<iframe src="https://medium.com/media/5c61a4970c08a5315ee4b830884bd002" frameborder=0></iframe>

The last date for submission is Sept 13, 2017. I had power cut all day. I know that it’s kind of late to start on this project. But, I am not willing to give up. I am going to try.

<iframe src="https://medium.com/media/d5fcb7f558bcbece8144e6285ffb89ec" frameborder=0></iframe>

### Gameplay

“Scribble” is a clone of [my favorite multiplayer game](https://www.facebook.com/drawmything/), which I and [my friend](https://twitter.com/argon_laser) used to play a lot during our college days. Unfortunately, the support for playing it on the browser stopped suddenly. That’s quite a disappointment.

Scribble is a minimalistic clone of [Draw my thing](https://www.facebook.com/drawmything/). Two players join one game. One player will be given a word and he is supposed to express that word by drawing it on a canvas. Whatever he draws will be synced and seen on the canvas of other player in realtime. The other player is supposed to guess the word with the help of the drawer.

### Tech

I am going to start with the sandbox server provided for the competition.
[**js13kGames/js13kserver**
*js13kserver - js13kGames 2016 Server category files and rules*github.com](https://github.com/js13kGames/js13kserver)

Backend is written in Node.js with Socket.IO. For the frontend, I am thinking of writing it in plain javascript or may be use Elm. Oh wait! I came across [this post on hackernews](https://reasonml.github.io/community/blog/#messengercom-now-50-converted-to-reason) today morning.

<iframe src="https://medium.com/media/8b7f168908d2e0cb08552ab938298d10" frameborder=0></iframe>

Reason seems quite interesting, but the learning curve is too much right now. So, I am going to just start with Vanilla JS and throw in something if I really feel like doing so.

Time is Sept 11, 2017 AA:28 AM. I am sitting at my desk in office. Damn, last night was awesome. The experience took me to my college days, where I would spend lot of time at night experimenting news things and writing code without caring much. It’s been 1.7 years and I am feeling it again. “The mixed feeling of want to complete and will I complete?”. Let me get back to work now and continue this in evening.

Time is Sept 11, 2017 9:32 PM. Last night, I was not able to able to correctly program canvas to be used as drawing board. So, today I asked help from [my friend](https://twitter.com/riturajcse) at [office](https://www.shippable.com/) in evening to help with the piece of code. We did it.

<iframe src="https://medium.com/media/b00e3ca6d592d48c5a08fdb4bd9b2496" frameborder=0></iframe>

### Bare Minimum

I just now completed the bare minimum version of the game and installing heroku cli to deploy it.

![User enters the game](https://cdn-images-1.medium.com/max/2880/1*eeON9l60r9kvekTJbR50xw.png)*User enters the game*

![Gameplay](https://cdn-images-1.medium.com/max/2776/1*8IM2UjfGbHms2jy71Q9qmg.gif)*Gameplay*

To be honest, at this point of time I have this huge chunks of Spaghetti code on both server side and client side. My next top priority is make this game look decent.

At last, I submitted the game in [js13kgames and waiting to see](http://js13kgames.com/entries/2017) if it will be approved as an entry. ( Entry got accepted and here it is — [http://js13kgames.com/entries/scribble](http://js13kgames.com/entries/scribble) ). In the meantime here is the [github repository](http://github.com/scriptnull/scribble) containing the source code. The code is definitely lacking few things like code style, basic refactoring, removing logs etc. I suppose this is the side effect of me trying to think fast and do things quickly. Next time, I hope to find more time and do stuff like this in advance. Please bear with me this time!

Currently one game can accommodate only 2 players, but the code is extensible to [any number of players](https://github.com/scriptnull/scribble/blob/master/public/server.js#L26). Since I didn’t have time to write UI code, I limited the capacity.

Here is a final look at the game and the size of the game is 6.7kb. Feel free to try it here — [https://scribble-game.herokuapp.com/](https://scribble-game.herokuapp.com/)

![Final gameplay. Chrome on left and Firefox on right.](https://cdn-images-1.medium.com/max/2774/1*CRvDBcUTjDCgwnJPFI6OfA.png)*Final gameplay. Chrome on left and Firefox on right.*

### Thanks

I personally like to thank [Rituraj](http://www.riturajcse.com/) for telling me to not give up on this project. Thanks to [Venkata Krishna](https://twitter.com/argon_laser) for helping beta test the game. I also like to thank the [Andrzej Mazur](http://end3r.com/) for organising [js13kgames](http://js13kgames.com/).

### Moving Forward

Escaping from the normal routine and writing something like this definitely helped me in getting better. The most valuable lesson being “Try to manage time properly. I have to somehow figure this out.”

It’s fascinating to note that a bare minimum version of a massive multiplayer game like [Draw My Thing](https://www.facebook.com/drawmything/) could be developed under 13kb in under 6 hours. The growth of web APIs and the sophistication of frameworks ( like Socket.IO ) is making me awestruck. I am very much interested in the future of the web and the tools that will give us more power.

Thanks for reading. I quote verses from my favourite Tamil literature “[Tirukkuṛaḷ](https://en.wikipedia.org/wiki/Tirukku%E1%B9%9Ba%E1%B8%B7)” at the end of my blog posts.
> # “அருவினை யென்ப உளவோ கருவியான்
> # காலம் அறிந்து செயின்.”
> # *— திருக்குறள்*

Translated meaning (in my words): Is something not possible for a man, who knows the right tools and acts at the right time?


# Scribble

It’s the name of the game, I am about to develop now. Time is Sept 10, 2017 7:34 PM IST when I am starting to type this post.

![](https://cdn-images-1.medium.com/max/2000/1*0NVnpOq-kr2m4eVHGf_OCg.png)

The thought to develop a game first occurred to me after I read [this blog post from github](https://github.com/blog/2409-build-a-game-in-13kb-or-less-with-js13kgames). It was about a game development competition called [JS13KGAMES](http://js13kgames.com/). It’s a competition in which a game has to be coded and the source files should be within 13 kilobytes.

I shared this with some of my friends. [One of them](https://twitter.com/riturajcse) took time and got his game out.
[**The Lost Elephant | js13kGames**
*An elephant has lost his way to his friends. You have to help him reach his friends without getting killed by speeding…*js13kgames.com](http://js13kgames.com/entries/the-lost-elephant)

He happened to write it in under 3 hours and he said it was inspired by the Cross Creeper game that we played in an Arcade outside our office the day before. That’s cool !

<iframe src="https://medium.com/media/5c61a4970c08a5315ee4b830884bd002" frameborder=0></iframe>

The last date for submission is Sept 13, 2017. I had power cut all day. I know that it’s kind of late to start on this project. But, I am not willing to give up. I am going to try.

<iframe src="https://medium.com/media/d5fcb7f558bcbece8144e6285ffb89ec" frameborder=0></iframe>

### Gameplay

“Scribble” is a clone of [my favorite multiplayer game](https://www.facebook.com/drawmything/), which I and [my friend](https://twitter.com/argon_laser) used to play a lot during our college days. Unfortunately, the support for playing it on the browser stopped suddenly. That’s quite a disappointment.

Scribble is a minimalistic clone of [Draw my thing](https://www.facebook.com/drawmything/). Two players join one game. One player will be given a word and he is supposed to express that word by drawing it on a canvas. Whatever he draws will be synced and seen on the canvas of other player in realtime. The other player is supposed to guess the word with the help of the drawer.

### Tech

I am going to start with the sandbox server provided for the competition.
[**js13kGames/js13kserver**
*js13kserver - js13kGames 2016 Server category files and rules*github.com](https://github.com/js13kGames/js13kserver)

Backend is written in Node.js with Socket.IO. For the frontend, I am thinking of writing it in plain javascript or may be use Elm. Oh wait! I came across [this post on hackernews](https://reasonml.github.io/community/blog/#messengercom-now-50-converted-to-reason) today morning.

<iframe src="https://medium.com/media/8b7f168908d2e0cb08552ab938298d10" frameborder=0></iframe>

Reason seems quite interesting, but the learning curve is too much right now. So, I am going to just start with Vanilla JS and throw in something if I really feel like doing so.

Time is Sept 11, 2017 AA:28 AM. I am sitting at my desk in office. Damn, last night was awesome. The experience took me to my college days, where I would spend lot of time at night experimenting news things and writing code without caring much. It’s been 1.7 years and I am feeling it again. “The mixed feeling of want to complete and will I complete?”. Let me get back to work now and continue this in evening.

Time is Sept 11, 2017 9:32 PM. Last night, I was not able to able to correctly program canvas to be used as drawing board. So, today I asked help from [my friend](https://twitter.com/riturajcse) at [office](https://www.shippable.com/) in evening to help with the piece of code. We did it.

<iframe src="https://medium.com/media/b00e3ca6d592d48c5a08fdb4bd9b2496" frameborder=0></iframe>

### Bare Minimum

I just now completed the bare minimum version of the game and installing heroku cli to deploy it.

![User enters the game](https://cdn-images-1.medium.com/max/2880/1*eeON9l60r9kvekTJbR50xw.png)*User enters the game*

![Gameplay](https://cdn-images-1.medium.com/max/2776/1*8IM2UjfGbHms2jy71Q9qmg.gif)*Gameplay*

To be honest, at this point of time I have this huge chunks of Spaghetti code on both server side and client side. My next top priority is make this game look decent.

At last, I submitted the game in [js13kgames and waiting to see](http://js13kgames.com/entries/2017) if it will be approved as an entry. ( Entry got accepted and here it is — [http://js13kgames.com/entries/scribble](http://js13kgames.com/entries/scribble) ). In the meantime here is the [github repository](http://github.com/scriptnull/scribble) containing the source code. The code is definitely lacking few things like code style, basic refactoring, removing logs etc. I suppose this is the side effect of me trying to think fast and do things quickly. Next time, I hope to find more time and do stuff like this in advance. Please bear with me this time!

Currently one game can accommodate only 2 players, but the code is extensible to [any number of players](https://github.com/scriptnull/scribble/blob/master/public/server.js#L26). Since I didn’t have time to write UI code, I limited the capacity.

Here is a final look at the game and the size of the game is 6.7kb. Feel free to try it here — [https://scribble-game.herokuapp.com/](https://scribble-game.herokuapp.com/)

![Final gameplay. Chrome on left and Firefox on right.](https://cdn-images-1.medium.com/max/2774/1*CRvDBcUTjDCgwnJPFI6OfA.png)*Final gameplay. Chrome on left and Firefox on right.*

### Thanks

I personally like to thank [Rituraj](http://www.riturajcse.com/) for telling me to not give up on this project. Thanks to [Venkata Krishna](https://twitter.com/argon_laser) for helping beta test the game. I also like to thank the [Andrzej Mazur](http://end3r.com/) for organising [js13kgames](http://js13kgames.com/).

### Moving Forward

Escaping from the normal routine and writing something like this definitely helped me in getting better. The most valuable lesson being “Try to manage time properly. I have to somehow figure this out.”

It’s fascinating to note that a bare minimum version of a massive multiplayer game like [Draw My Thing](https://www.facebook.com/drawmything/) could be developed under 13kb in under 6 hours. The growth of web APIs and the sophistication of frameworks ( like Socket.IO ) is making me awestruck. I am very much interested in the future of the web and the tools that will give us more power.

Thanks for reading. I quote verses from my favourite Tamil literature “[Tirukkuṛaḷ](https://en.wikipedia.org/wiki/Tirukku%E1%B9%9Ba%E1%B8%B7)” at the end of my blog posts.
> # “அருவினை யென்ப உளவோ கருவியான்
> # காலம் அறிந்து செயின்.”
> # *— திருக்குறள்*

Translated meaning (in my words): Is something not possible for a man, who knows the right tools and acts at the right time?
