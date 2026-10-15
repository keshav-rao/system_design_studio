# Rolling sensor graph demo with Redis

```json metadata
{
  "schema_version": 2,
  "title": "Rolling sensor graph demo with Redis",
  "description": "Build a rolling sensor graph demo with Redis time series data",
  "categories": ["docs","develop","stack","oss","rs","rc"],
  "tableOfContents": {"sections":[{"id":"when-to-use-redis-time-series","title":"When to use Redis time series"},{"id":"why-the-problem-is-hard","title":"Why the problem is hard"},{"id":"what-you-can-expect-from-a-redis-solution","title":"What you can expect from a Redis solution"},{"id":"how-redis-supports-the-solution","title":"How Redis supports the solution"},{"id":"ecosystem","title":"Ecosystem"},{"id":"code-examples-to-build-your-own-redis-time-series-dashboard","title":"Code examples to build your own Redis time series dashboard"}]}

,
  "codeExamples": []
}
```


## When to use Redis time series

Use Redis time series when you need to ingest, query, and retain high-velocity time-ordered numeric data — sensor readings, application metrics, telemetry, or prices — with sub-millisecond latency and automatic downsampling.

## Why the problem is hard

Time series workloads invert the typical read-heavy ratio: ingestion can reach hundreds of thousands of samples per second while reads are comparatively infrequent. Relational and document databases were not designed for this write volume and degrade under sustained load.

Without a purpose-built structure, teams approximate time series with sorted sets or custom Lua scripts, which works at small scale but lacks native aggregation, automatic downsampling, and per-sample retention — leading to fragile cleanup jobs and growing memory costs.

Dedicated time series databases like InfluxDB or TimescaleDB handle petabyte-scale cold archival and batch analytics, but add a separate system to provision, scale, and monitor when the requirement is real-time latency on an instance already in the stack. ([Redis Streams](https://redis.io/docs/latest/develop/data-types/streams) solve a different problem — ordered event logs with consumer-group delivery, not numeric aggregation over time windows.)

## What you can expect from a Redis solution

You can:

-   Ingest device telemetry or application metrics at sustained high volume without a separate ingestion pipeline.
-   Run aggregated range queries over arbitrary time windows for dashboards and alerting with single-digit millisecond response times.
-   Define multi-tier downsampling (raw → 1-minute averages → 1-hour averages) that runs automatically as data arrives.
-   Enforce retention policies that keep memory bounded without manual cleanup jobs.
-   Query across thousands of series by label for root-cause analysis and operational monitoring.
-   Power real-time operational dashboards without a separate metrics backend.

## How Redis supports the solution

In practice, each metric is stored as a Redis [time series](https://redis.io/docs/latest/develop/data-types/timeseries) key with optional labels for the dimensions you want to query by (region, host, sensor type), and compaction rules to write downsampled summaries into companion keys as new samples arrive.

Redis provides the following features that make it a good fit for time series workloads:

-   The [time series](https://redis.io/docs/latest/develop/data-types/timeseries) data structure
    (`TS.*` commands) is designed for sustained high-velocity ingestion with sub-millisecond
    write latency.
-   [`TS.RANGE`](https://redis.io/docs/latest/commands/ts.range) and
    [`TS.MRANGE`](https://redis.io/docs/latest/commands/ts.mrange) return aggregated results
    (`avg`, `sum`, `min`, `max`, `count`, `std.p`, `std.s`, `twa`, and others) over
    arbitrary time windows in single-digit milliseconds, eliminating application-side
    aggregation logic.
-   [`TS.CREATERULE`](https://redis.io/docs/latest/commands/ts.createrule) defines source-to-destination
    compaction with an aggregation function and bucket duration, so downsampling runs inside
    Redis without an external pipeline.
-   The `RETENTION` parameter on [`TS.CREATE`](https://redis.io/docs/latest/commands/ts.create) enforces
    per-sample trimming relative to the newest sample, keeping memory bounded without
    manual cleanup or key-level [`EXPIRE`](https://redis.io/docs/latest/commands/expire).
-   Label-based secondary indexing enables cross-series queries
    ([`TS.MRANGE`](https://redis.io/docs/latest/commands/ts.mrange) … `FILTER`) across thousands of keys
    by any dimension — region, host, sensor type — in a single call.

## Ecosystem

The following tools and libraries integrate with Redis time series:

-   **Grafana**:
    [Redis Data Source plugin](https://grafana.com/grafana/plugins/redis-datasource/)
    for real-time time series dashboards
-   **Prometheus**: RedisTimeSeries remote read/write adapter
-   **Telegraf**: output plugin for streaming collected metrics into Redis
-   **Client libraries**: `TS.*` commands are available through standard Redis client
    libraries including [redis-py](https://redis.readthedocs.io/),
    [Jedis](https://github.com/redis/jedis),
    [ioredis](https://github.com/redis/ioredis), and
    [go-redis](https://github.com/redis/go-redis)
-   **Infrastructure**: [Redis Cloud](https://redis.io/docs/latest/operate/rc) for managed deployments
    with built-in time series support

## Code examples to build your own Redis time series dashboard

The following guides show how to build a rolling sensor graph demo backed by Redis time series.
Each guide includes a runnable example with three simulated sensors, a rolling graph of raw
readings, bucketed min/max/average summaries on the same time axis, and a short retention
window where old samples visibly expire:

* [redis-py (Python)](https://redis.io/docs/latest/develop/use-cases/time-series-dashboard/redis-py)
* [node-redis (Node.js)](https://redis.io/docs/latest/develop/use-cases/time-series-dashboard/nodejs)
* [go-redis (Go)](https://redis.io/docs/latest/develop/use-cases/time-series-dashboard/go)
* [Jedis (Java)](https://redis.io/docs/latest/develop/use-cases/time-series-dashboard/java-jedis)
* [Lettuce (Java)](https://redis.io/docs/latest/develop/use-cases/time-series-dashboard/java-lettuce)
* [NRedisStack (C#)](https://redis.io/docs/latest/develop/use-cases/time-series-dashboard/dotnet)
* [Predis (PHP)](https://redis.io/docs/latest/develop/use-cases/time-series-dashboard/php)
* [redis-rb (Ruby)](https://redis.io/docs/latest/develop/use-cases/time-series-dashboard/ruby)
* [redis-rs (Rust)](https://redis.io/docs/latest/develop/use-cases/time-series-dashboard/rust)

