---
title: Too many clocks at my home
date: 2024-12-12 23:47:26
tags: ["distributed systems"]
---

This is supposed to be a distributed systems blog post that I [promised](https://bsky.app/profile/vishnubharathi.codes/post/3lcyrndlxvs2u) to write, but I am unable to keep quiet about a fact that I realized while thinking about writing this post.

That is, "I got too many clocks at my home" - like one per room, except the bathrooms. Trying to convince my family to allow me to achieve full coverage, but they just won't allow me to have a ticking clock in our bathrooms - lol 😂 

## Clock Skew

If you have a lot of clocks like me, then there is a good chance that not all the clocks in all rooms are showing the same time. The clock in my bedroom is five minutes faster than the clock in our hall. That makes me a time traveller when I go from one room to another room.

The time in my bedroom is 8:35 AM, but the time in my hall is 8:30 AM. If I believe in both of my clocks and walk from my bedroom to the hall, congrats to me because I have travelled back in time.

It seems like there is a similar situation at hand when you are running multiple different computers. Every machine has its own system clock. There is no guarantee that all the system clocks are having the same time. This difference in time has been causing headaches for programmers and this is what our computer scientists call it to be a "clock skew".

## NTP

What if I went through my house all day long and adjusted all the clocks to the same time? Will that make sure to get rid of the clock skew? Not really, the skew can still occur because the seconds hand in real-world clocks cannot be synchronized with one another. There are external factors like the battery power going down which could eventually cause a clock skew.

In the case of computing, there seems to be a protocol called  [NTP (Network Time Protocol)](https://en.wikipedia.org/wiki/Network_Time_Protocol) that helps do the equivalent of me going around the house and syncing clocks. It synchronizes the clocks between computers and helps us to maintain the clock skew to be minimum. I first heard about it back in 2016 or 2017 at work when we faced some problems due to the clocks going out of sync between the machines in our system. So we had to install the NTP daemon service on all the machines to solve the problem.

If you are using an NTP daemon in production, make sure to have an alerting and monitoring setup for it. I learned that some people go to the extremes of plotting graphs against the clock skew and network latency between the machines in their system [^1]. It might be good to have a sense of how much of a clock skew can usually happen while using NTP. 100 to 500 milliseconds seem to be a practical estimate for clock skews [^2].

## Reference clocks

You might be wondering if two clocks are out of sync, which one does the NTP consider a source of truth and adjust accordingly.

To understand it, we have to visit where time comes from. Prepare to be amazed by [this list](https://en.wikipedia.org/wiki/Clock#History_of_time-measuring_devices) of all kinds of ways humans have been finding time so far in history. If you scroll to the bottom of the list, you will find two kinds of clocks that are of interest to us here.

### Quartz clock

> Quartz clocks are timepieces that use an [electronic oscillator](https://en.wikipedia.org/wiki/Electronic_oscillator) regulated by a [quartz](https://en.wikipedia.org/wiki/Quartz) crystal to keep time. [^3]

If you ever wondered how your laptop shows the right time when you switch it off and turn it on after a month. The reason is that your laptop contains a quartz clock with a separate battery which runs always. When your operating system boots up, it gets the time from this clock.

### Atomic clock

> An atomic clock is a [clock](https://en.wikipedia.org/wiki/Clock) that measures time by monitoring the resonant frequency of atoms. [^4]

Atomic clocks are the most accurate clocks in existence as of now. In fact, it is so accurate that we have to infer what a second is by using it 🤯 

> The second, symbol s, is the SI unit of time. It is defined by taking the fixed numerical value of the caesium frequency, the unperturbed ground-state hyperfine transition frequency of the caesium-133 atom, to be 9192631770 when expressed in the unit Hz, which is equal to s−1.

While storing date-time values in your applications, you might have heard of Co-ordinated Universal Time (UTC).

> UTC is based on TAI, which is a weighted average of hundreds of [atomic clocks](https://en.wikipedia.org/wiki/Atomic_clock) worldwide.

Now you know how UTC is calculated! If you install NTP on your machines, it will use UTC as the reference time to adjust the clock skew on your machine.

Satellites (with atomic clocks installed on them) seem to be the ultimate reference clock. GPS receivers can get signals from these satellites about what time it is. NTP uses different levels of reference clocks and these levels are called startum. The atomic clock in the satellite is the stratum 0 which is the reference clock for stratum 1 and so on. [^5]

### Clock bound

We know that we can't trust our clocks anymore. Big giants like Google and AWS have been thinking about what they can do to improve the situation. As a result, they set up the fancy stratum 0 atomic clocks on satellites connected to their data center regions. Clock skew is inevitable, but with this fancy setup, they are able to achieve clock skews that are within certain bounds.

> In Spanner’s case, Google mentions an upper bound of 7ms.....

This means two machines that are part of the spanner cluster can at-most be of 7ms apart. They cleverly use this property:

> So how does Spanner use TrueTime to provide linearizability given that there are still inaccuracies between clocks? It’s actually surprisingly simple. It waits. Before a node is allowed to report that a transaction has committed, it must wait 7ms. Because all clocks in the system are within 7ms of each other, waiting 7ms means that no subsequent transaction may commit at an earlier timestamp, even if the earlier transaction was committed on a node with a clock which was fast by the maximum 7ms. Pretty clever. [^6] 

Some interesting things to explore here would be:
- [Google's TrueTime](https://cloud.google.com/spanner/docs/true-time-external-consistency)
- [Amazon's Time Sync Service](https://aws.amazon.com/about-aws/whats-new/2017/11/introducing-the-amazon-time-sync-service/)
- AWS's [clockbound library](https://github.com/aws/clock-bound) can give you a timestamp and the bounds of the timestamp which can be used by your application running on EC2.

## Causal Ordering

All the above were attempts to make the clock to be more "trustable". There is another extreme where things get even more interesting.

To get there, the first thing you need to note is: It is "causal ordering" and not "casual ordering".

Causal means "one" thing in a system _caused_ some other thing in the system. If it was not for the first thing, the things that come after that would have never happened.

I sent some money to my friend and they received it in their bank account. Sending the money is the event that causes the money to be received in my friend's account. It can't be the other way around: My friend received some money out of nowhere and then I sent the money which went nowhere but got detected from my account - there is no causal order here.

If you think deeply, we need a clock in most of the distributed systems because we just like to have causal ordering of events happening in our system. Be it an e-commerce app or a banking app, the order in which events flow is what we are interested in.

## Logical clocks

This is where things get exciting even more! Let us say we ditch our system clock altogether.

Instead of a system clock both our server(s) and client would have their own clock (typically as a shared library). Instead of observing the real-world time from this custom clock, our application logic could observe a monotonically increasing counter value. This counter value could give a number that the event can record and increment for the next event to use.

Do you see what we did here? Instead of storing "event A" that happened at a particular time `hh:mm:ss`, we record that event A happened as the Nth event in our system. If we sort the numbers stored alongside the event, we get the causal ordering of events. This can help us ensure things like my friend doesn't get money out of nowhere.

```go
type Clock struct {
	time uint64

	mu sync.RWMutex
}

func (c *Clock) Time() uint64 {
	c.mu.RLock()
	defer c.mu.RUnlock()
	return c.time
}

func (c *Clock) Increment() uint64 {
	c.mu.Lock()
	defer c.mu.Unlock()
	c.time++
	return c.time
}
```

Both our server and client would have their own clocks.

```go
type Server struct {
	clock *Clock
}

type Client struct {
	clock *Clock
}
```

And how do we synchronize the time between them? Simple! We just try to adjust the clock whenever we feel like the clock might be running behind.

```go
func (c *Clock) Adjust(time uint64) {
	c.mu.Lock()
	defer c.mu.Unlock()

	if c.time > time {
		return
	}

	c.time = time + 1
}
```

Here is a toy example of this. The client talks to the server via an HTTP API and tries to store a key-value pair. It will also send its clock time. But the counter (time) value in the Client's clock is running behind the server's clock. So, the server can respond back with an error - maybe a 400 Bad request and a response header containing the latest server time. Now the clock can adjust itself to that time and reattempt the API call once more with the new time.

```go
// This is a super toy version of what could happen in the Client
// I really badly want to get away with code instead of diagrams to explain this
// You will now have to excuse me for using `http.Get` and an unbounded recursive call here.
func (c *Client) Store(key, value string) (string, error) {
	resp, err := c.Get(
		fmt.Sprintf("http://localhost:8080/put?key=%s&value=%s,&time=%d",
			key, value, c.clock.Time(),
		))
	if err != nil {
		return "", err
	}
	defer resp.Body.Close()

	if serverTime, err := strconv.ParseUint(resp.Header.Get("CLOCK_TIME"), 10, 64); err != nil {
		c.clock.Adjust(serverTime)
		return c.Store(key, value)
	}

	return resp.Status, nil
}
```

This `type Clock struct` that we have here is the logical clock. In fact, this was the first of its kind called the Lamport Clock [^7].

There are other types of logical clocks that can be seen in the wild like vector clocks, hybrid logical clocks, etc. Something for us to explore!

[^1]:  [Clock Skew and Distributed Systems (Donny Nadolny, PagerDuty)](https://youtu.be/IjsJLTriLzs?si=qFhFtB1XfWkx1uBs)
[^2]: [What is the average clock skew when using NTP?](https://www.perplexity.ai/search/what-is-the-average-clock-skew-GWjRvNpYSbmRad_YHBswMg#0)
[^3]: [Quartz Clock](https://en.wikipedia.org/wiki/Quartz_clock)
[^4]: [Atomic Clock](https://en.wikipedia.org/wiki/Atomic_clock)
[^5]: [NTP FAQ](https://www.ntp.org/ntpfaq/NTP-s-algo/#5111-what-is-a-reference-clock)
[^6]: [Living without atomic clocks: Where CockroachDB and Spanner diverge](https://www.cockroachlabs.com/blog/living-without-atomic-clocks/)
[^7]: Leslie Lamport. 1978. Time, clocks, and the ordering of events in a distributed system. Commun. ACM 21, 7 (July 1978), 558–565. https://doi.org/10.1145/359545.359563

~ ~ ~ ~

Hope you had a good time learning about time!
