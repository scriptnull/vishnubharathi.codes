---
title: "Vert.x First Attempt"
date: 2018-07-03T06:10:38+05:30
draft: false
tags: ["java", "jvm", "vertx", "microservices", "api"]
---

Ever since I decided to [learn about the Java Ecosystem](/blog/visit-the-old-to-understand-the-new/), I have been wanting to try out something practical. May be write a small app in Java and see how the experience would be. I came across a framework called [Eclipse Vert.x](https://vertx.io/) few months back and decided to give it a try. So I ended up reading its documentation for few weekends and today morning. I am feeling a bit comfortable to write some code on Vert.x finally. Lets see how it goes!

> Eclipse Vert.x is a tool-kit for building reactive applications on the JVM.

The main reasons to choose Vert.x:

- It is polyglot, I suppose "x" in Vert.x stands for any supported programming language.
- It has awesome documentation.
- Gives the bare minimum and could be extended as we like.

> Vert.x is a toolkit, not an opinionated framework where we force you to do things in a certain way.

- Event bus as communication medium between services. (More on this later, if possible)

> The event bus is the nervous system of Vert.x

## Install

Used brew, as I am on macOS.

```
brew install vert.x
```

Check https://vertx.io/download/ for other download options.

## Concept

Lets say, I am trying to build a simple service that does CRUD of a table in a database. I call this table challenges. Here is a thought process on how this could be implemented.

![challenge service](/images/vertx-challenges-service.png)

## Bootstrap

Let me start writing some code now. I am using http://start.vertx.io/ to get a template project.

Coming from a JavaScript background, it feels very weird to download starter projects from webpages as zip packages. In the JS ecosystem, we usually have this baked into command line tools.

It didn't quite workout. I was able to run the sample web server verticle at least.

I am finally able to get autocomplete support, after fiddling for 15 minutes between IntelliJ IDEA, Eclipse, Atom, and VS Code.

VS Code did the magic!

![java-vscode-autocomplete](/images/java-vscode-autocomplete.png)

## Code

I quickly wrote up event listeners in Java.

```java
package codes.vishnubharathi.challenges;

import io.vertx.core.AbstractVerticle;
import io.vertx.core.eventbus.EventBus;

public class MainVerticle extends AbstractVerticle {

    @Override
    public void start() throws Exception {
        EventBus ev = vertx.eventBus();
        ev.consumer("challenges.create", message -> {
            System.out.println("challenges.create -> message" + message.body());
            message.reply("ack " + message.body());
        });
        ev.consumer("challenges.update", message -> {
            System.out.println("challenges.update -> message" + message.body());
            message.reply("ack " + message.body());
        });
        ev.consumer("challenges.delete", message -> {
            System.out.println("challenges.delete -> message" + message.body());
            message.reply("ack " + message.body());
        });
    }
}
```

## Test

To test of our service is listening for the events, I am going to use Vertx unit testing to deploy a verticle.

```java
package codes.vishnubharathi.challenges;

import io.vertx.core.AbstractVerticle;
import io.vertx.core.eventbus.EventBus;
import io.vertx.ext.unit.TestSuite;
import io.vertx.ext.unit.report.ReportOptions;
import io.vertx.ext.unit.Async;
import io.vertx.ext.unit.TestOptions;

public class TestMainVerticle extends AbstractVerticle {

    @Override
    public void start() throws Exception {
        TestSuite suite = TestSuite.create("challenges_events");

        suite.before(context -> {
            MainVerticle challengeVertx = new MainVerticle();
            vertx.deployVerticle(challengeVertx, context.asyncAssertSuccess());
        });

        suite.test("publish events", context -> {
            EventBus ev = vertx.eventBus();
            Async async = context.async(3);
            ev.send("challenges.create", "create payload", ar -> {
                if (ar.succeeded()) {
                    context.assertEquals(ar.result().body(), "ack create payload");
                    async.countDown();
                } else {
                    context.fail();
                }
            });
            ev.send("challenges.update", "update payload", ar -> {
                if (ar.succeeded()) {
                    context.assertEquals(ar.result().body(), "ack update payload");
                    async.countDown();
                } else {
                    context.fail();
                }
            });
            ev.send("challenges.delete", "delete payload", ar -> {
                if (ar.succeeded()) {
                    context.assertEquals(ar.result().body(), "ack delete payload");
                    async.countDown();
                } else {
                    context.fail();
                }
            });
        });

        TestOptions options = new TestOptions().addReporter(new ReportOptions().setTo("console"));
        suite.run(options);
    }
}
```

Running the test using `vertx test TestMainVerticle.java` resulted in my tests getting passed.

```
Begin test suite challenges_events
Begin test suite challenges_events
Begin test publish events
Begin test publish events
challenges.create -> messagecreate payload
challenges.update -> messageupdate payload
challenges.delete -> messagedelete payload
Passed publish events
Passed publish events
End test suite challenges_events , run: 1, Failures: 0, Errors: 0
End test suite challenges_events , run: 1, Failures: 0, Errors: 0
Succeeded in deploying verticle
```

(no idea why "Begin test suite challenges_events" is being printed twice.)

Anyways, I have a basic setup for my application ready. I hope to complete my handler logics afterwards. Bye until then!
