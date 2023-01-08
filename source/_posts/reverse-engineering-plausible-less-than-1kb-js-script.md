---
title: Reverse engineering Plausible's less than 1kb JS script
date: 2023-01-08 06:02:14
tags: ["javascript", "tinkering"]
---

[Plausible](https://plausible.io/) is "Simple and privacy-friendly Google Analytics alternative". It is an open-source software. While trying to self-host it, I arrived at [a page](https://plausible.io/lightweight-web-analytics) which talks about their less than 1kb analytics script. It got me curious about what would be inside it 🤔

So, here we go. Let us start to understand this from scratch.

## Adding the script

When you want to enable Plausible analytics for your website, it seems like you would start by adding this little snippet to your website.

```html
<script defer data-domain="domain.com"
src="https://plausible.io/js/script.js"></script>
```

- `script` tag is used to load JavaScript on the webpage.
- `src` is the web address to the contents of the JavaScript.

Bigger question here is, "what does `defer` and `data-domain` do?"

Reading through the MDN docs, I learnt that the browser would defer the execution of the JS script to a time when all of the HTML is loaded and parsed. That means all the HTML tags from `<html>....</html>` would be present when the script gets executed.

More specfically, it seems like the script would get eexecuted before the [DOMContentLoaded event](https://developer.mozilla.org/en-US/docs/Web/API/Document/DOMContentLoaded_event). This event waits only for the loading and parsing of HTML and does not wait for other things like stylesheets, images, etc. The more common [load](https://developer.mozilla.org/en-US/docs/Web/API/Window/load_event) seem to be responsible for catching the occurence of loading the HTML document and all its dependencies like the stylesheets, images, etc.

Okay, so this way the script doesn't immediately try to load and block things and it waits for at-least a skeleton of HTML to load.

Regarding the `data-domain` part, I can't seem to find references of it in the MDN docs for the script tag. So it is not an in-built attribute of the `script` tag. I think it might be a way of passing data from HTML to the JS script. Let us continue and see where this leads us.

## The script

This is the entire script.

```javascript
!function(){"use strict";var a=window.location,r=window.document,o=r.currentScript,s=o.getAttribute("data-api")||new URL(o.src).origin+"/api/event";function l(t){console.warn("Ignoring Event: "+t)}function t(t,e){if(/^localhost$|^127(\.[0-9]+){0,2}\.[0-9]+$|^\[::1?\]$/.test(a.hostname)||"file:"===a.protocol)return l("localhost");if(!(window._phantom||window.__nightmare||window.navigator.webdriver||window.Cypress)){try{if("true"===window.localStorage.plausible_ignore)return l("localStorage flag")}catch(t){}var i={};i.n=t,i.u=a.href,i.d=o.getAttribute("data-domain"),i.r=r.referrer||null,i.w=window.innerWidth,e&&e.meta&&(i.m=JSON.stringify(e.meta)),e&&e.props&&(i.p=e.props);var n=new XMLHttpRequest;n.open("POST",s,!0),n.setRequestHeader("Content-Type","text/plain"),n.send(JSON.stringify(i)),n.onreadystatechange=function(){4===n.readyState&&e&&e.callback&&e.callback()}}}var e=window.plausible&&window.plausible.q||[];window.plausible=t;for(var i,n=0;n<e.length;n++)t.apply(this,e[n]);function p(){i!==a.pathname&&(i=a.pathname,t("pageview"))}var w,d=window.history;d.pushState&&(w=d.pushState,d.pushState=function(){w.apply(this,arguments),p()},window.addEventListener("popstate",p)),"prerender"===r.visibilityState?r.addEventListener("visibilitychange",function(){i||"visible"!==r.visibilityState||p()}):p()}();
```

Feels small. Let me try to get some line breaks to make it more readable.

oh wait! Plausible is an Open Source Software. That means, I can try to get the source code of the un-minified version of the above code.

Going to the plausible [github repo](https://github.com/plausible/analytics), pressing "t" and typing "plausible.js" landed me to the file that is in need: https://github.com/plausible/analytics/blob/1772ddff17f5c2880400f7f7c42d7c1aa772feef/tracker/src/plausible.js

Let us start reading the code now!

## The code

The script starts with a good old immediately invoked anonymous function and ['use strict' notation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode).

```javascript
(function(){
  'use strict';
  
  // ......
})();
```

After that some variables and functions are getting defined.

```javascript
  var location = window.location
  var document = window.document

  {{#if compat}}
  var scriptEl = document.getElementById('plausible');
  {{else}}
  var scriptEl = document.currentScript;
  {{/if}}
  var endpoint = scriptEl.getAttribute('data-api') || defaultEndpoint(scriptEl)
```

`location` and `document` are okay - probably defined to avoid typing `window` repeatedly. `{{#if compat}}` seems like a server-renered template language notation. They are using it to get a reference to the script element which is executing the plausible script. After that `endpoint` variable is set by picking the `data-api` if it is present on the script tag or by calling a function called `defaultEndpoint`.

Since the script tag doesn't have the `data-api` attribute, let us look at what `defaultEndpoint` function does.

```javascript
  function defaultEndpoint(el) {
    {{#if compat}}
    var pathArray = el.src.split( '/' );
    var protocol = pathArray[0];
    var host = pathArray[2];
    return protocol + '//' + host  + '/api/event';
    {{else}}
    return new URL(el.src).origin + '/api/event'
    {{/if}}
  }
```

At this point, I am guessing `compat` is for compatibility with old browsers. For now, my browser us comfortable using the `else` block. So, let us zoom on to that. It returns `new URL(el.src).origin + '/api/event'`. That means, it takes the script element's src attribute and forms a new URL object and get's the origin property.


```
> new URL("https://plausible.io/js/script.js").origin

'https://plausible.io' + '/api/event'
```

Moving on. There is this little `warn` function that is bugging myself to paste it here.

```javascript
  function warn(reason) {
    console.warn('Ignoring Event: ' + reason);
  }
```

I cleaned up all the server-side rendered templates to make code folding work for the script :D With that, we are entering the real action.

```javascript
var queue = (window.plausible && window.plausible.q) || []
```

So, we are creating a queue which hopefully is getting saved in `window.plausible.q` object further down the lane.

```javascript
  window.plausible = trigger
  for (var i = 0; i < queue.length; i++) {
    trigger.apply(this, queue[i])
  }
```

`trigger` is a big function and is getting assigned to `window.plausible`. After that, we call `trigger` function for every element in the queue. Initially, the queue will be empty, so I am going to see what is happening when that is the case.


Now there is a divide happening.
```javascript
    {{#if hash}}
    window.addEventListener('hashchange', page)
    {{else}}
    var his = window.history
    if (his.pushState) {
      var originalPushState = his['pushState']
      his.pushState = function() {
        originalPushState.apply(this, arguments)
        page();
      }
      window.addEventListener('popstate', page)
    }
    {{/if}}
```

If the URL contains `#some-id` at the end, then the if block would be executed and if the URL doesn't contain any reference to an HTML element identifier, then the `else` block is executed.

TIL that there is a DOM event called [hashchange](https://developer.mozilla.org/en-US/docs/Web/API/Window/hashchange_event).

> The hashchange event is fired when the fragment identifier of the URL has changed (the part of the URL beginning with and following the # symbol).

So, if the page's URL contains the `#` suffix, then this makes sures that the `page` function is executed after the fragment identified of the URL is changed.

In the other case, we seem to access [window.history](https://developer.mozilla.org/en-US/docs/Web/API/Window/history).


