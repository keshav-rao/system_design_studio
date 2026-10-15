# Redis feature store

```json metadata
{
  "schema_version": 2,
  "title": "Redis feature store",
  "description": "Serve pre-computed ML features on the request path under tight latency budgets, with batch and streaming features kept fresh in the same store.",
  "categories": ["docs","develop","stack","oss","rs","rc"],
  "tableOfContents": {"sections":[{"id":"when-to-use-redis-as-a-feature-store","title":"When to use Redis as a feature store"},{"id":"why-the-problem-is-hard","title":"Why the problem is hard"},{"id":"what-you-can-expect-from-a-redis-solution","title":"What you can expect from a Redis solution"},{"id":"how-redis-supports-the-solution","title":"How Redis supports the solution"},{"id":"ecosystem","title":"Ecosystem"},{"id":"code-examples-to-build-your-own-redis-feature-store","title":"Code examples to build your own Redis feature store"}]}

,
  "codeExamples": []
}
```


## When to use Redis as a feature store

Use Redis as the online layer of a feature store when production models — fraud
scoring, recommendations, dynamic pricing — need dozens of pre-computed features
per prediction on every request, with sub-millisecond reads, mixed batch-and-streaming
freshness, and high write throughput from concurrent ingestion pipelines.

## Why the problem is hard

An online feature store has to serve dozens of features per inference call inside
a request budget measured in milliseconds, while batch jobs and streaming
pipelines update those same features at very different cadences. Some of the
obvious workarounds have real drawbacks:

-   **Querying the offline warehouse directly** adds hundreds of milliseconds per
    inference call, which makes real-time serving impossible.
-   **A bespoke cache in front of the warehouse** solves latency but introduces
    *training-serving skew*: the features served at inference drift from what the
    model trained on, silently degrading accuracy whenever a transform changes
    on one side and not the other.
-   **Disk-backed online stores** hit a throughput wall when every user action
    has to update a dozen features simultaneously across millions of entities —
    the I/O mix of small concurrent writes is exactly what they are slowest at.
-   **Single-TTL stores** can't handle mixed staleness: batch features refreshed
    nightly coexist with streaming features updated every few seconds, and a
    single per-key expiry can't express both. Worse, a failed ingestion
    pipeline must *expire* its features rather than serve stale values silently.

A workable online feature store needs sub-millisecond reads at request rate,
high concurrent write throughput from mixed batch and streaming ingestion,
independent freshness controls per feature, and self-cleaning behavior when an
upstream pipeline fails — without standing up a dedicated piece of
infrastructure beside the rest of the model-serving stack.

## What you can expect from a Redis solution

You can:

-   Serve feature vectors to inference endpoints under 1 ms P99
    (99% of requests have a latency of 1 ms or less) at millions of
    reads per second from a single shard, and scale horizontally beyond that
    with Redis Cluster.
-   Run batch and streaming ingestion concurrently against the same entities
    without locking or version columns — Redis is single-threaded per shard, so
    individual field writes are atomic by construction.
-   Apply *different* freshness guarantees to individual features within the same
    entity hash: seconds for real-time signals, hours for batch aggregates, with
    per-field TTL via [`HEXPIRE`](https://redis.io/docs/latest/commands/hexpire).
-   Let stale streaming features self-expire when their ingestion pipeline
    fails, so models receive missing features rather than silently outdated ones.
-   Retrieve features for hundreds of entities in a single round trip for batch
    scoring, using pipelined [`HMGET`](https://redis.io/docs/latest/commands/hmget).
-   Plug into [Redis Feature Form](https://redis.io/docs/latest/develop/ai/featureform) —
    Redis's own materialize / serve layer — or
    [Feast](https://docs.feast.dev/) with a connection-string change, so no
    bespoke serving code is required.
-   Co-locate the online feature store on the same Redis instance already
    handling cache, sessions, or rate limiting in the stack — no additional
    infrastructure.

## How Redis supports the solution

In practice, each entity (a user, an account, an item) is a single
[Hash](https://redis.io/docs/latest/develop/data-types/hashes) at a deterministic key like
`fs:user:{id}`. The hash holds every feature for that entity as one field per
feature — batch-materialized aggregates alongside streaming-updated signals —
so one [`HMGET`](https://redis.io/docs/latest/commands/hmget) call returns whatever subset
the model needs in one round trip. A key-level
[`EXPIRE`](https://redis.io/docs/latest/commands/expire) aligns with the batch
materialization cycle so a whole entity self-cleans when its pipeline stops
refreshing it, and per-field [`HEXPIRE`](https://redis.io/docs/latest/commands/hexpire)
lets each streaming feature carry its own shorter expiry independent of the
rest of the hash.

Redis provides the following features that make it a good fit for an online
feature store:

-   [Hashes](https://redis.io/docs/latest/develop/data-types/hashes) group every feature
    for an entity under one key, so retrieval reads everything the model needs
    in a single network round trip with [`HMGET`](https://redis.io/docs/latest/commands/hmget),
    and small hashes use *listpack* encoding for compact in-memory representation.
-   [`HSET`](https://redis.io/docs/latest/commands/hset) writes any subset of fields
    atomically, so batch and streaming pipelines can update overlapping or
    disjoint features on the same entity concurrently without locks or version
    columns.
-   [`HEXPIRE`](https://redis.io/docs/latest/commands/hexpire) and
    [`HTTL`](https://redis.io/docs/latest/commands/httl) (Redis 7.4+) give per-field TTLs,
    so streaming features (5-minute freshness) and batch features (24-hour
    freshness) can live in the same hash with independent expiry — the
    *mixed-staleness* problem becomes a one-line server-side guarantee.
-   [`EXPIRE`](https://redis.io/docs/latest/commands/expire) at the key level lets an
    entity disappear entirely if its batch refresher fails, so inference sees
    a missing entity (which the model handler can detect and fall back on)
    rather than silently outdated values.
-   [Pipelining](https://redis.io/docs/latest/develop/using-commands/pipelining) bundles
    [`HMGET`](https://redis.io/docs/latest/commands/hmget) calls for many entities into
    one round trip, which is the right primitive for batch scoring where the
    model needs features for hundreds of entities at once.
-   Sub-millisecond reads and writes from memory keep the feature store off the
    critical path of inference, so the model-server's request budget is spent
    on the model rather than on feature retrieval.

## Ecosystem

The following libraries and platforms use Redis as their online feature store:

-   **[Redis Feature Form](https://redis.io/docs/latest/develop/ai/featureform)** is
    Redis's own feature-engineering platform. It defines features, labels, and
    feature views in a Python definitions file, materializes them through a
    [registered provider](https://redis.io/docs/latest/develop/ai/featureform/register-providers),
    and [serves](https://redis.io/docs/latest/develop/ai/featureform/serve-features)
    them from Redis as the low-latency online store. See the
    [quickstart](https://redis.io/docs/latest/develop/ai/featureform/quickstart) for an
    end-to-end walkthrough.
-   **Python**: [Feast](https://docs.feast.dev/reference/online-stores/redis)
    ships Redis as a first-class online store provider — point a Feast
    `online_store` block at a Redis connection string and the
    `RedisOnlineStore` backend handles materialization and serving.
-   **Compute**: [Apache Spark](https://spark.apache.org/) batch jobs run the
    nightly materialization, writing into Redis via the Redis Feature Form /
    Feast materialize commands or directly with the
    [`spark-redis`](https://github.com/RedisLabs/spark-redis) connector.
-   **Streaming**: [Apache Flink](https://flink.apache.org/) or
    [Kafka Streams](https://kafka.apache.org/documentation/streams/) compute the
    real-time features and `HSET` them into Redis with per-field
    [`HEXPIRE`](https://redis.io/docs/latest/commands/hexpire) so each streaming signal
    carries its own freshness window.
-   **Infrastructure**: [Kubernetes](https://kubernetes.io/) co-locates Redis
    pods alongside the model-serving containers, with horizontal-pod autoscaling
    on the read replicas to track inference load;
    [Active-Active geo-distribution](https://redis.io/docs/latest/operate/rs/databases/active-active)
    on Redis Enterprise / Redis Cloud replicates the online store across
    regions for low-latency reads close to each inference cluster.

## Code examples to build your own Redis feature store

The following guides show how to build a small Redis-backed online feature
store for a fraud-scoring model. Each guide includes a runnable interactive
demo that lets you bulk-load batch features, run a streaming worker that
updates real-time features with per-field TTL, retrieve any subset of features
for a single user under 1 ms, and pipeline batch reads across a hundred users.

* [redis-py (Python)](https://redis.io/docs/latest/develop/use-cases/feature-store/redis-py)
* [node-redis (Node.js)](https://redis.io/docs/latest/develop/use-cases/feature-store/nodejs)
* [go-redis (Go)](https://redis.io/docs/latest/develop/use-cases/feature-store/go)
* [Jedis (Java)](https://redis.io/docs/latest/develop/use-cases/feature-store/java-jedis)
* [Lettuce (Java)](https://redis.io/docs/latest/develop/use-cases/feature-store/java-lettuce)
* [redis-rs (Rust)](https://redis.io/docs/latest/develop/use-cases/feature-store/rust)
* [StackExchange.Redis (C#)](https://redis.io/docs/latest/develop/use-cases/feature-store/dotnet)
* [Predis (PHP)](https://redis.io/docs/latest/develop/use-cases/feature-store/php)
* [redis-rb (Ruby)](https://redis.io/docs/latest/develop/use-cases/feature-store/ruby)

