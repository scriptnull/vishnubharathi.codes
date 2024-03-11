---
title: Rough notes on GCP networking
date: 2024-03-11 06:22:46
tags: ["devops", "cloud"]
---

I am publishing my rough notes on Google Cloud networking which I collected while watching the first few episodes of the [Google Cloud Networking playlist](https://www.youtube.com/watch?v=0hN-dyOV10c&list=PLDGXb-1k3XY1RaEfzp_nDSJMPP0iAQEtP). lol, I don't know how many more times I will need to revise them.

(Any images seen here are attributed to the presentation in the video series mentioned above. This blog post is more like watching those videos on fast-forward and I would definitely encourage you to check out the videos if you would like more clarity)

## VPC
- VPC is a global construct
  - You can create subnets that belong to a different region
- Shared VPC
	- One host project has VPC and subnets
	- Share all or some subnets with other projects that host the project-level service

## Interconnecting to Google Cloud
- Layer 3
	- Dedicated (Direct peering)
	- Shared (Carrier peering)
	- Needs VPN setup to tunnel into private address space
	- No SLAs
	- Free of cost (but check latest)
- Layer 2
	- Dedicated Interconnect
		- Costly (because Gcloud has dedicated hardware)
		- Dedicated bandwidth
	- Partner Interconnect
		- Example: Equinix fabric
		- Shared bandwidth other people who are using the interconnect
	- Has SLA

## Routing
- Pre-programmed routes
	- Automatically created.
	- User can't delete or change these routes
	- Subnet routes are automatically created when a subnet is added to the network
- Default routes
	- Pre-programmed 0.0.0.0/0 route to an internet gateway
	- Unlike pre-programmed routes, this can be changed.
- Cloud Router (CR)
  collapsed:: true
	- Cloud Router is similar to a traditional router but has differences that are important to understand
	- In a traditional router, a router provides two functionalities
		- Control plane functionality - BGP route communication mechanisms.
		- Data plane functionality - packets go into the router and the router makes the decision of where to route it.
	- Cloud router is a "control-plane" only device. Think about it as a BGP speaker. This only speaks BGP, but the routers that you have on-prem might speak other protocols.
	- What does Cloud Router do?
		- Learns routes dynamically, configures routing tables, and pushes those routing tables to the VMs themselves.
		- So when a VM wants to send packets to another VM, it is a host-to-host communication rather than pushing the packet to a router and the router making a choice to reach the destination.
	- It is a Google-managed process, controlled by you, that runs on a Google host. If it fails, Google Cloud will automatically try to restart it. However, the routing from host to host is not affected during this period since it is not a data plane device. BGP connectivity will be lost during this time, so you can't add new routes. The best practice would be to run two cloud routers always.
	- Two routing modes
		- (can be enabled when setting up your VPC)
		- Regional routing
			- CR was brought up in a region. So it can only learn about the subnets in that particular region.
			- Be careful about using these because when a load balancer tries to reach something in us-west-1 but the request ends up in the CR present in us-east-1, then a black hole is created. (i.e. request is not able to be routed to us-west-1 because regional CR doesn't even know that us-west-1 exists)
		- Global routing
			- Allows CR to pick up all the subnets in a VPC
	- Route Priority
		- Route Priority is equivalent to the BGP MED metric (multi-exit discriminator)
		- Local routes have default MED (1000 if not changed)
		- Routes from other regions have a metric based on RTT added to the default MED value.
		- If you have multiple interconnects, you can use route priority to tell the preference order of where the request needs to go.
- Advanced Route
	- Static forwarding to a VPN gateway when cloud routers/dynamic routing isn't used.
	- Force some IPs to be routed to a third-party service

## VPC Peering
- In case of VPNs, you can adverstise only a few subnets between network. In case of VPC peering, it is binary. All subnets in VPC A will get advertised to all subnets in VPC B and vice versa. You are basically smashing two VPCs.
- Security policies still exist in both the VPCs and there is no "single" security policy for the smashed up VPC. So, if something is going wrong, check the firewall rules associated with both VPCs.
- Can not have overlapping IP ranges
- Non-transitive in nature
- Quotas and Limits:
	- 15,500 total VMs across all peering relationships
	- A network can have upto 25 peered networks

## Load Balancers
- Families (based on where they face)
	- External load balancer: Internet-facing
	- Internal load balancer: Internal to google cloud
- Families (based on where they route to)
	- Global
	- Regional
- Families (based on the level they operate at)
	- Network Load balancers
		- Layer 3 and 4.
		- These are external load balancers (internet-facing)
		- These are regional load balancers.
		- Highly available with multiple zones
		- Load balance TCP/UDP traffic and does not look at L7
		- Client IP is preserved, don't need x-forwarded-for
		- It does not perform SSL termination, so your backend needs to do it
		- Client access can be controlled with the VPC Firewall
		- Balances traffic using 2, 3, or 5-tuple hashing
			- 2 tuple: {sourceIp, destIP}
			- 3 tuple: {sourceIp, destIP, Protocol}
			- 5 tuple: {sourceIp, destIP, sourcePort, destPort, Protocol}
		- Session Affinity based on IP address
		- High performance = 1 million+ requests per second
	- DNS-based Global LB
		- This is how traditional public cloud usually had load balancing. But not how Google cloud load balancing works.
		- ![image](https://github.com/scriptnull/vishnubharathi.codes/assets/4211715/145bb23d-d996-4292-bf20-26cbfc880b2b)
		- IP address of servers in different region are added as DNS entries for the domain.
		- The DNS server gives back the IP address when requested in a load balancer fashion (like round robin)
		- Disadvantage: DNS caching happens at multiple places (web browsers, internet providers ec.), so it might be pointing to a invalid IP address at one of those layers
	- Google Global Load Balancer (L7)
		- Built for powering Google search, Gmail and other Google products and then adopted inside Google cloud
		- ![image](https://github.com/scriptnull/vishnubharathi.codes/assets/4211715/0e178e1f-c9c9-472b-9506-f76385ae5870)
	- Single Global Anycast VIP (IPv4/IPv6) across region
	- Cross-region failure and fallback
	- Fast autoscaling
	- Highly available
	- Single point to apply global policies
- Internal Load Balancers
	- ![image](https://github.com/scriptnull/vishnubharathi.codes/assets/4211715/e918cf25-7f13-4697-8fb2-a8550125a5b0)
- L4 Regional LB
	- Internal (RFC 1918) VIP
	- Client IP Preserved
	- TCP, HTTP, HTTPS health checks
	- No middle proxy (delivered through SDN), High performance, and no chokepoints
