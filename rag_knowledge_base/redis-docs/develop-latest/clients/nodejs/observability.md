# Observability

```json metadata
{
  "schema_version": 2,
  "title": "Observability",
  "description": "Monitor your client's activity for optimization and debugging.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"installation","title":"Installation"},{"id":"import","title":"Import"},{"id":"configure-the-meter-provider","title":"Configure the meter provider"},{"children":[{"id":"custom-histogram-buckets","title":"Custom histogram buckets"}],"id":"configure-the-redis-client","title":"Configure the Redis client"},{"id":"use-redis","title":"Use Redis"},{"id":"shutdown","title":"Shutdown"}]}

,
  "codeExamples": [{"codetabsId":"observability-stepimport","description":"Foundational: Import required libraries for Redis observability, OpenTelemetry metrics, and Redis operations","difficulty":"beginner","id":"import","languages":[{"id":"Node-js","panelId":"panel_Nodejs_observability-stepimport"}]},{"codetabsId":"observability-stepsetup_meter_provider","description":"Foundational: Configure a meter provider to export metrics to a local Grafana instance every 10 seconds","difficulty":"beginner","id":"setup_meter_provider","languages":[{"id":"Node-js","panelId":"panel_Nodejs_observability-stepsetup_meter_provider"}]},{"codetabsId":"observability-stepclient_config","description":"Foundational: Configure Redis observability with a list of metric groups and optional command filtering and privacy controls","difficulty":"beginner","id":"client_config","languages":[{"id":"Node-js","panelId":"panel_Nodejs_observability-stepclient_config"}]},{"codetabsId":"observability-stepuse_redis","description":"Foundational: Use Redis with automatic instrumentation","difficulty":"beginner","id":"use_redis","languages":[{"id":"Node-js","panelId":"panel_Nodejs_observability-stepuse_redis"}]},{"codetabsId":"observability-stepshutdown","description":"Foundational: Shutdown Redis observability","difficulty":"beginner","id":"shutdown","languages":[{"id":"Node-js","panelId":"panel_Nodejs_observability-stepshutdown"}]}]
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


`node-redis` has built-in support for [OpenTelemetry](https://opentelemetry.io/) (OTel)
instrumentation to collect metrics. This can be very helpful for
diagnosing problems and improving the performance and connection resiliency of
your application. See the
[Observability overview](https://redis.io/docs/latest/develop/clients/observability)
for an introduction to Redis client observability and a reference guide for the
available metrics.

This page explains how to enable and use OTel instrumentation
in `node-redis` using an example configuration for a local [Grafana](https://grafana.com/)
instance. See our
[observability demonstration repository](https://github.com/redis-developer/redis-client-observability)
on GitHub to learn how to set up a suitable Grafana dashboard.

## Installation

Install the OTel dependencies with the following commands:

```bash
npm install @opentelemetry/api
npm install @opentelemetry/sdk-metrics
```

## Import

Start by importing the required OTel and Redis modules:

Foundational: Import required libraries for Redis observability, OpenTelemetry metrics, and Redis operations

**Difficulty:** Beginner

**Available in:** JavaScript (Node.js)

##### JavaScript (Node.js)

```javascript
import { createClient, OpenTelemetry } from 'redis';
import { metrics } from '@opentelemetry/api';
import {
  ConsoleMetricExporter,
  MeterProvider,
  PeriodicExportingMetricReader
} from '@opentelemetry/sdk-metrics';
```



## Configure the meter provider

Otel uses a [Meter provider](https://opentelemetry.io/docs/concepts/signals/metrics/#meter-provider)
to create the objects that collect the metric information. The example below
configures a meter provider to export metrics to a local Grafana instance
every 10 seconds, but see the [OpenTelemetry Node.js docs](https://opentelemetry.io/docs/languages/js/)
to learn more about other export options.

Foundational: Configure a meter provider to export metrics to a local Grafana instance every 10 seconds

**Difficulty:** Beginner

**Available in:** JavaScript (Node.js)

##### JavaScript (Node.js)

```javascript
const reader = new PeriodicExportingMetricReader({
    exporter: new ConsoleMetricExporter(),
});

const meterProvider = new MeterProvider({
    readers: [reader]
});

metrics.setGlobalMeterProvider(meterProvider);
```



## Configure the Redis client

You configure the client library for OTel only once per application. This will
enable OTel for all Redis connections you create. The example below shows the
options you can pass to the observability instance via the `MetricConfig` object
during initialization.

Foundational: Configure Redis observability with a list of metric groups and optional command filtering and privacy controls

**Difficulty:** Beginner

**Available in:** JavaScript (Node.js)

##### JavaScript (Node.js)

```javascript
OpenTelemetry.init({
    metrics: {
        enabled: true,
        enabledMetricGroups: ["command", "pubsub", "streaming", "resiliency"],
        includeCommands: ["GET", "HSET", "XREADGROUP", "PUBLISH"],
        excludeCommands: ["SET"],
        hidePubSubChannelNames: true,
        hideStreamNames: false,
        bucketsOperationDuration: [0.001, 0.01, 0.1, 1],
        bucketsStreamProcessingDuration: [0.01, 0.1, 1, 5],
    },
});
```



The available options for `MetricConfig` are described in the table below:

| Property | Default | Description |
| -------- | ------- | ----------- |
| `enabled` | `false` | Set this to `true` explicitly to enable metrics. |
| `meterProvider` |  | Uses this provider instead of the global provider from `@opentelemetry/api`. |
| `includeCommands` | `[]` | List of Redis commands to track. If set, only these commands will be tracked. Note that you should use the Redis command name rather than the node-redis method name where the two differ. |
| `excludeCommands` | `[]` | List of Redis commands to exclude from tracking. If set, all commands except these will be tracked. Note that you should use the Redis command name rather than the node-redis method name where the two differ. |
| `enabledMetricGroups` | `['connection-basic', 'resiliency']` | List of metric groups to enable. By default, only `connection-basic` and `resiliency` are enabled. See [Redis metric groups](https://redis.io/docs/latest/develop/clients/observability#redis-metric-groups) for a list of available groups. |
| `hidePubSubChannelNames` | `false` | If true, channel names in pub/sub metrics will be hidden. |
| `hideStreamNames` | `false` | If true, stream names in streaming metrics will be hidden. |
| `bucketsOperationDuration` | `[0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5, 10]` | List of bucket boundaries for the [`operation.duration`](https://redis.io/docs/latest/develop/clients/observability#metric-db.client.operation.duration) histogram (see [Custom histogram buckets](#custom-histogram-buckets) below). |
| `bucketsConnectionCreateTime` | `[0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5, 10]` | List of bucket boundaries for the [`connection.create_time`](https://redis.io/docs/latest/develop/clients/observability#metric-db.client.connection.create_time) histogram (see [Custom histogram buckets](#custom-histogram-buckets) below). |
| `bucketsConnectionWaitTime` | `[0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5, 10]` | List of bucket boundaries for the [`connection.wait_time`](https://redis.io/docs/latest/develop/clients/observability#metric-db.client.connection.wait_time) histogram (see [Custom histogram buckets](#custom-histogram-buckets) below). |
| `bucketsStreamProcessingDuration` | `[0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5, 10]` | List of bucket boundaries for the [`stream.lag`](https://redis.io/docs/latest/develop/clients/observability#metric-redis.client.stream.lag) histogram (see [Custom histogram buckets](#custom-histogram-buckets) below). |

### Custom histogram buckets

For the histogram metrics, a reasonable default set of buckets is defined, but
you can customize the bucket boundaries to suit your needs (the buckets are the
ranges of data values counted for each bar of the histogram). Pass an increasing
list of float values to the `bucketsXxx` options when you create the `MetricConfig`
object. The first and last values in the list are the lower and upper bounds of the
histogram, respectively, and the values in between define the bucket boundaries.

## Use Redis

Once you have configured the client, all Redis connections you create will be
automatically instrumented and the collected metrics will be exported to your
configured destination.

The example below shows the simplest Redis connection and a few commands,
but see the
[observability demonstration repository](https://github.com/redis-developer/redis-client-observability)
for an example that calls a variety of commands in a more realistic way.

Foundational: Use Redis with automatic instrumentation

**Difficulty:** Beginner

**Available in:** JavaScript (Node.js)

##### JavaScript (Node.js)

```javascript
const client = createClient();

await client.connect();

await client.set('key', 'value');
const value = await client.get('key');
console.log(value); // >>> value
```



## Shutdown

When your application exits, you should call the `shutdown()` method to ensure
that all pending metrics are exported.

Foundational: Shutdown Redis observability

**Difficulty:** Beginner

**Available in:** JavaScript (Node.js)

##### JavaScript (Node.js)

```javascript
await meterProvider.forceFlush();
await meterProvider.shutdown();
await client.destroy();
```



