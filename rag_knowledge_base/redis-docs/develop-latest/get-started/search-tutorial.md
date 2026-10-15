# Redis Search tutorial

```json metadata
{
  "schema_version": 2,
  "title": "Redis Search tutorial",
  "description": "A guided, end-to-end tour of Redis Search, from data modeling to vector and hybrid search.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"the-example-a-product-catalog","title":"The example: a product catalog"},{"id":"prerequisites","title":"Prerequisites"},{"id":"choose-your-tool","title":"Choose your tool"},{"id":"connect","title":"Connect"},{"id":"next-steps","title":"Next steps"}]}

,
  "codeExamples": [{"codetabsId":"search_tutorial-stepconnect","description":"Foundational: Connect to a Redis server with redis-cli using host and port parameters","difficulty":"beginner","id":"connect","languages":[{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_search_tutorial-stepconnect"}]}]
}
```

## Code Examples Legend

The code examples below show how to perform the same operations in different programming languages and client libraries:

- **Redis CLI**: Command-line interface for Redis
- **C# (Synchronous)**: StackExchange.Redis synchronous client
- **C# (Asynchronous)**: StackExchange.Redis asynchronous client
- **Go**: go-redis client
- **Java (Synchronous - Jedis)**: Jedis synchronous client
- **Java (Asynchronous - Lettuce)**: Lettuce asynchronous client
- **Java (Reactive - Lettuce)**: Lettuce reactive/streaming client
- **JavaScript (Node.js)**: node-redis client
- **PHP**: Predis client
- **Python**: redis-py client
- **Rust (Synchronous)**: redis-rs synchronous client
- **Rust (Asynchronous)**: redis-rs asynchronous client

Each code example demonstrates the same basic operation across different languages. The specific syntax and patterns vary based on the language and client library, but the underlying Redis commands and behavior remain consistent.

---


This tutorial is a guided, hands-on tour of [Redis Search](https://redis.io/docs/latest/develop/ai/search-and-query). If you have never used Redis before, you are in the right place. You will start with a small dataset and, step by step, build up to running the same kinds of searches that power product catalogs, recommendation systems, and AI applications.

By the end, you will be able to:

1. **[Model your data](https://redis.io/docs/latest/develop/get-started/search-tutorial/data-modeling)** &mdash; decide how to store records in Redis so they can be searched, and understand the trade-offs between hashes and JSON documents.
2. **[Create an index](https://redis.io/docs/latest/develop/get-started/search-tutorial/indexing)** &mdash; build a *secondary index* that tells Redis which fields to index and how, so queries are fast.
3. **[Search and filter](https://redis.io/docs/latest/develop/get-started/search-tutorial/search)** &mdash; find and return exactly the records you want with `FT.SEARCH`.
4. **[Aggregate](https://redis.io/docs/latest/develop/get-started/search-tutorial/aggregation)** &mdash; group and summarize your data with `FT.AGGREGATE`.
5. **[Search by meaning](https://redis.io/docs/latest/develop/get-started/search-tutorial/vector-search)** &mdash; run vector and hybrid searches to find records by semantic similarity.

Each page builds on the previous one and ends with a link to the next step, so you can follow the whole tutorial in order.

## The example: a product catalog

Throughout the tutorial you will work with a small **online store catalog**. Each record is a product with a name, brand, category, free-text description, price, customer rating, and other attributes:

```json
{
  "name": "Aurora AcousticPro Headphones",
  "brand": "Aurora",
  "category": "Audio",
  "description": "Over-ear wireless headphones with active noise cancelling ...",
  "price": 199.99,
  "rating": 4.6,
  "review_count": 1284,
  "stock": 42,
  "release_year": 2024,
  "features": ["wireless", "noise-cancelling", "bluetooth", "over-ear"]
}
```

This kind of data is a good fit for search because people want to query it in many different ways: by keyword ("wireless headphones"), by filter (under $100, in the Audio category), by summary (average price per category), and increasingly by meaning ("something for listening to music on a run").

## Prerequisites

You need a running Redis instance that includes Redis Search and the JSON data type. The easiest options are:

- **Redis Cloud** &mdash; create a [free account](https://redis.io/try-free/). A free database comes with all the Redis Open Source features, including Redis Search and JSON.
- **Local install** &mdash; follow the [install guide](https://redis.io/docs/latest/operate/oss_and_stack/install/install-stack) to run Redis Open Source on your own machine.

> [!NOTE]
> The vector and hybrid search examples in the [last step](https://redis.io/docs/latest/develop/get-started/search-tutorial/vector-search) use features that require Redis 8.8 or later. The earlier steps work on any recent version of Redis with Redis Search.

## Choose your tool

You can follow along using whichever tool you prefer. Every example in this tutorial is shown for each of them:

- **`redis-cli`** &mdash; the command-line client included with Redis. It is the quickest way to try commands and see raw results. This is the default tab in every code example.
- **[Redis Insight](https://redis.io/docs/latest/develop/tools/insight)** &mdash; a free graphical tool for Redis. Its [Search workspace](https://redis.io/docs/latest/develop/tools/insight/search-workspace) lets you browse indexes and run full-text, vector, and hybrid queries in a schema-aware editor. If you prefer to see your data and results visually, this is a great choice.
- **A client library** &mdash; for real applications you will use Redis from your programming language of choice. Each example includes tabs for languages such as Python and Node.js.

Throughout the tutorial, look for **"Try it in Redis Insight"** tips that show how to run the same query in the graphical editor.

## Connect

First, connect to your Redis database. The following example connects with `redis-cli` to a server running on `localhost` (`-h 127.0.0.1`) and listening on the default port (`-p 6379`):

    redis-cli -h 127.0.0.1 -p 6379

Foundational: Connect to a Redis server with redis-cli using host and port parameters

**Difficulty:** Beginner

**Available in:** Python

##### Python

```python
r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)
```



<br/>

&nbsp;

> [!TIP]
> If you are using Redis Cloud, copy the connection details from your database's configuration page. A Cloud connection string has the form `host:port`, for example `redis-16379.c283.us-east-1-4.ec2.cloud.redislabs.com:16379`. You also need the database username and password, which you can pass to your client or supply with the [AUTH command](https://redis.io/docs/latest/commands/auth) after connecting.

## Next steps

Ready to begin? Start with [data modeling](https://redis.io/docs/latest/develop/get-started/search-tutorial/data-modeling) to learn how to store your records so Redis can search them.

