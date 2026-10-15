# Redis leaderboard

```json metadata
{
  "schema_version": 2,
  "title": "Redis leaderboard",
  "description": "Build ranked leaderboards with Redis sorted sets and user metadata",
  "categories": ["docs","develop","stack","oss","rs","rc"],
  "tableOfContents": {"sections":[{"id":"when-to-use-a-redis-leaderboard","title":"When to use a Redis leaderboard"},{"id":"why-the-problem-is-hard","title":"Why the problem is hard"},{"id":"what-you-can-expect-from-a-redis-solution","title":"What you can expect from a Redis solution"},{"id":"how-redis-supports-the-solution","title":"How Redis supports the solution"},{"id":"ecosystem","title":"Ecosystem"},{"id":"code-examples-to-build-your-own-redis-leaderboard","title":"Code examples to build your own Redis leaderboard"}]}

,
  "codeExamples": []
}
```


## When to use a Redis leaderboard

Use a Redis leaderboard when you need to rank entities — players, products, sellers, stocks — by a score that changes continuously and serve those rankings to users in real time.

## Why the problem is hard

Computing a single entity's rank in a relational database requires an `ORDER BY` across the full table — O(N) at best — and at millions of rows this pushes query time into seconds. Caching the result doesn't help because scores change on every user action, so any TTL-based cache is immediately stale or triggers thundering-herd refreshes on expiry.

Local in-process data structures break behind load balancers because no single instance holds the complete ranking. A dedicated OLAP or leaderboard service could solve the ranking problem but adds operational overhead for what is fundamentally a single sorted data structure.

This use case is also distinct from [Redis Streams](https://redis.io/docs/latest/develop/data-types/streams) (which record event history but don't maintain ranked state) and from the probabilistic [Top-K](https://redis.io/docs/latest/develop/data-types/probabilistic/top-k) data structure (which approximates heavy hitters but cannot return exact ranks or neighborhood queries).

## What you can expect from a Redis solution

You can:

-   Show any user their exact global rank and the neighbors immediately above and below them, updated on every score change.
-   Serve top-N pages to thousands of concurrent readers without degrading write performance.
-   Run daily, weekly, and monthly boards that create and expire themselves automatically.
-   Aggregate time-windowed boards into composite rankings without application-side sorting.
-   Support millions of ranked members in roughly 500 MB of RAM.
-   Add leaderboard functionality to an existing deployment without provisioning new infrastructure.

## How Redis supports the solution

In practice, the leaderboard is stored as a Redis sorted set — one key per board — with members keyed by entity ID and scored by the value you want to rank on. A companion hash per entity holds metadata (name, avatar, tier) so the sorted set stays lightweight.

Redis provides the following features that make it a good fit for leaderboards:

-   [Sorted sets](https://redis.io/docs/latest/develop/data-types/sorted-sets) maintain rank order automatically, with
    [`ZADD`](https://redis.io/docs/latest/commands/zadd), [`ZRANGE`](https://redis.io/docs/latest/commands/zrange), and
    [`ZREVRANK`](https://redis.io/docs/latest/commands/zrevrank) all running in O(log N) regardless of set size.
-   [`ZINCRBY`](https://redis.io/docs/latest/commands/zincrby) updates scores atomically in place — no
    read-modify-write cycle and no cache invalidation.
-   [`ZRANGE`](https://redis.io/docs/latest/commands/zrange) with `REV` and `LIMIT` serves both top-N and
    "around me" neighborhood queries in a single command.
-   [`EXPIRE`](https://redis.io/docs/latest/commands/expire) on a per-window key cleans up daily, weekly,
    and monthly boards automatically, and
    [`ZUNIONSTORE`](https://redis.io/docs/latest/commands/zunionstore) aggregates windows without
    application-level coordination.
-   [Hashes](https://redis.io/docs/latest/develop/data-types/hashes) store entity metadata so the sorted set
    stays small and fast.
-   Sub-millisecond latency on reads and writes means the leaderboard sits on the request path
    without adding meaningful delay. If Redis is already in the stack, the leaderboard adds zero
    marginal infrastructure.

## Ecosystem

The following libraries and frameworks provide Redis sorted set integrations suitable for leaderboards:

-   **Java**:
    [Spring Data Redis (`ZSetOperations`)](https://docs.spring.io/spring-data/redis/reference/redis/template.html)
-   **Python**: [redis-py](https://redis.readthedocs.io/),
    [redis-om-python](https://github.com/redis/redis-om-python)
-   **Node.js**: [ioredis](https://github.com/redis/ioredis),
    [node-redis](https://github.com/redis/node-redis)
-   **Infrastructure**: [Redis Cloud](https://redis.io/docs/latest/operate/rc)
    (Active-Active for multi-region with conflict-free replicated sorted sets)

## Code examples to build your own Redis leaderboard

The following guides show how to build a simple Redis-backed leaderboard.
Each guide includes a runnable interactive demo for each of the following client libraries:

* [redis-py (Python)](https://redis.io/docs/latest/develop/use-cases/leaderboard/redis-py)
* [node-redis (Node.js)](https://redis.io/docs/latest/develop/use-cases/leaderboard/nodejs)
* [go-redis (Go)](https://redis.io/docs/latest/develop/use-cases/leaderboard/go)
* [Jedis (Java)](https://redis.io/docs/latest/develop/use-cases/leaderboard/java-jedis)
* [Lettuce (Java)](https://redis.io/docs/latest/develop/use-cases/leaderboard/java-lettuce)
* [StackExchange.Redis (C#)](https://redis.io/docs/latest/develop/use-cases/leaderboard/dotnet)
* [Predis (PHP)](https://redis.io/docs/latest/develop/use-cases/leaderboard/php)
* [redis-rb (Ruby)](https://redis.io/docs/latest/develop/use-cases/leaderboard/ruby)
* [redis-rs (Rust)](https://redis.io/docs/latest/develop/use-cases/leaderboard/rust)

