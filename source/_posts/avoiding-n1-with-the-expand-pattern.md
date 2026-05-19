---
title: Avoiding n+1 with the expand pattern
date: 2026-05-19 19:57:43
tags: ["programming", "api-design"]
---

You might have heard of the n+1 problem in API design. I have heavily relied on using GraphQL and have taken it for granted to avoid the problem.

Today, I came across a way to avoid it in REST APIs too while working with the [Stripe API](https://docs.stripe.com/api). I am naming this the Expand pattern (courtesy of Stripe API Developers). Take this pattern and implement in your REST APIs to avoid the n+1 problem.

## Problem

Let us look at a simple API call.

```http
GET /v1/invoices/:invoice-id
```

```json
{
  "id": "in_1MtHbELkdIwHu7ixl4OzzPMv",
  "object": "invoice",
  "customer": "cus_NeZwdNtLEOXuvB",
  "subscription": "sub_1MoGGTLkdIwHu7ixZkAA1J0n",
  "payment_intent": "pi_3MtHbELkdIwHu7ix0rUOgsLj",
  "amount_due": 5000,
  "currency": "usd",
  "status": "open"
}
```

You usually want to make another request for a field whose ID is present in the response. Let us say we want the customer's email address. Then we end up making one more API call to get the full customer object.

This does not look bad for a single invoice. But we usually list things.

```http
GET /v1/invoices
```

```json
{
  "object": "list",
  "url": "/v1/invoices",
  "has_more": false,
  "data": [
    {
      "id": "in_1MtHbELkdIwHu7ixl4OzzPMv",
      "object": "invoice",
      "customer": "cus_NeZwdNtLEOXuvB",
      "amount_due": 5000,
      "currency": "usd",
      "status": "open"
    },
    {
      "id": "in_1NaB2cLkdIwHu7ix9Qe3FpzT",
      "object": "invoice",
      "customer": "cus_OpZ1aRtMFQYwxC",
      "amount_due": 8200,
      "currency": "usd",
      "status": "open"
    }
  ]
}
```

To show the customer's email for each invoice, we make one more call per invoice. List N invoices and we make N more calls - 1 for the list and N for the customers. That is the n+1 problem.

## Expand Pattern

Stripe provides a param called [expand](https://docs.stripe.com/api/expanding_objects) for this on most of its APIs. You can use it to pass the
field names that you want to expand. That means you get the full object
instead of just the object id.

```http
GET /v1/invoices/:invoice-id?expand[]=customer
```

```json
{
  "id": "in_1MtHbELkdIwHu7ixl4OzzPMv",
  "object": "invoice",
  "customer": {
    "id": "cus_NeZwdNtLEOXuvB",
    "object": "customer",
    "email": "jenny.rosen@example.com",
    "name": "Jenny Rosen"
  },
  "subscription": "sub_1MoGGTLkdIwHu7ixZkAA1J0n",
  "payment_intent": "pi_3MtHbELkdIwHu7ix0rUOgsLj",
  "amount_due": 5000,
  "currency": "usd",
  "status": "open"
}
```

The same works on a list. Expand `data.customer` and every customer comes back inlined in that single call.

```http
GET /v1/invoices?expand[]=data.customer
```

No more N extra calls.

## GraphQL, when?

What if I only want the customer's email and not the whole customer object?

That seems to be not possible with expand. It returns all the fields of the expanded object.

This is the place where we enter the
GraphQL territory. GraphQL lets you pick exactly the fields you want. expand
only saves you the extra round trip, not the over-fetching cost. But still a great win to rejoice!

## Nested Expand

It seems like you can do nested expands in Stripe API like this

```http
GET /v1/invoices/:invoice-id?expand[]=customer.default_source
```

```json
{
  "id": "in_1MtHbELkdIwHu7ixl4OzzPMv",
  "object": "invoice",
  "customer": {
    "id": "cus_NeZwdNtLEOXuvB",
    "object": "customer",
    "email": "jenny.rosen@example.com",
    "name": "Jenny Rosen",
    "default_source": {
      "id": "card_1NLOFm2eZvKYlo2C8Z9k3K2L",
      "object": "card",
      "brand": "Visa",
      "last4": "4242",
      "exp_month": 8,
      "exp_year": 2026
    }
  },
  "subscription": "sub_1MoGGTLkdIwHu7ixZkAA1J0n",
  "payment_intent": "pi_3MtHbELkdIwHu7ix0rUOgsLj",
  "amount_due": 5000,
  "currency": "usd",
  "status": "open"
}
```

However there is a limitation for how deep you can traverse - 4 levels. Still, a deeply nested fetch that would have been several round trips collapses into one call.

There is no particular reason mentioned for picking 4 as the limit, but if we were to implement the expand pattern in our APIs, we can do something like this. We want a default max depth so a single request cannot fan out forever:

```
Let T = number of tables
Let D = maximum depth of relations between your tables   (the optimal value)
Let B = a higher limit you pick for your app's use case / bandwidth savings

limit = min(D, B),  where  limit < T
```

## No worries

I think this pattern is useful to know about to avoid overthinking things like what if my app becomes a hit overnight and it's doing a lot of n+1 calls. That won't scale! I am never going to worry anything like that while building new apps from now on. Focus on solid REST API and do the expand pattern. That should give us a good mileage.
