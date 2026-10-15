# Observability

```json metadata
{
  "schema_version": 2,
  "title": "Observability",
  "description": "Monitor your client's activity for optimization and debugging.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"installation","title":"Installation"},{"id":"import","title":"Import"},{"id":"configure-the-meter-provider","title":"Configure the meter provider"},{"children":[{"id":"custom-histogram-buckets","title":"Custom histogram buckets"}],"id":"configure-the-redis-client","title":"Configure the Redis client"},{"id":"use-redis","title":"Use Redis"},{"id":"shutdown","title":"Shutdown"}]}

,
  "codeExamples": [{"codetabsId":"observability-stepimport","description":"Foundational: Import required libraries for Redis observability, OpenTelemetry metrics, and Redis operations","difficulty":"beginner","id":"import","languages":[{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_observability-stepimport"}]},{"codetabsId":"observability-stepsetup_meter_provider","description":"Foundational: Configure a meter provider to export metrics to a local Grafana instance every 10 seconds","difficulty":"beginner","id":"setup_meter_provider","languages":[{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_observability-stepsetup_meter_provider"}]},{"codetabsId":"observability-stepclient_config","description":"Foundational: Configure Redis observability with a list of metric groups and optional command filtering and privacy controls","difficulty":"beginner","id":"client_config","languages":[{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_observability-stepclient_config"}]},{"codetabsId":"observability-stepuse_redis","description":"Foundational: Use Redis with automatic instrumentation","difficulty":"beginner","id":"use_redis","languages":[{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_observability-stepuse_redis"}]},{"codetabsId":"observability-stepshutdown","description":"Foundational: Shutdown Redis observability","difficulty":"beginner","id":"shutdown","languages":[{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_observability-stepshutdown"}]}]
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


`redis-py` has built-in support for [OpenTelemetry](https://opentelemetry.io/) (OTel)
instrumentation to collect metrics. This can be very helpful for
diagnosing problems and improving the performance and connection resiliency of
your application. See the
[Observability overview](https://redis.io/docs/latest/develop/clients/observability)
for an introduction to Redis client observability and a reference guide for the
available metrics.

This page explains how to enable and use OTel instrumentation
in `redis-py` using an example configuration for a local [Grafana](https://grafana.com/)
instance. See our
[observability demonstration repository](https://github.com/redis-developer/redis-client-observability)
on GitHub to learn how to set up a suitable Grafana dashboard.

## Installation

Install OTel support for `redis-py` with the following command:

```bash
pip install redis[otel]
```

## Import

Start by importing the required OTel and Redis modules:

Foundational: Import required libraries for Redis observability, OpenTelemetry metrics, and Redis operations

**Difficulty:** Beginner

**Available in:** Python

##### Python

```python
# OpenTelemetry metrics API
from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.exporter.otlp.proto.http.metric_exporter import OTLPMetricExporter

# Redis observability API
from redis.observability.providers import get_observability_instance
from redis.observability.config import OTelConfig, MetricGroup

# Redis client
import redis
```



## Configure the meter provider

Otel uses a [Meter provider](https://opentelemetry.io/docs/concepts/signals/metrics/#meter-provider)
to create the objects that collect the metric information. The example below
configures a meter provider to export metrics to a local Grafana instance
every 10 seconds, but see the [OpenTelemetry Python docs](https://opentelemetry.io/docs/languages/python/)
to learn more about other export options.

Foundational: Configure a meter provider to export metrics to a local Grafana instance every 10 seconds

**Difficulty:** Beginner

**Available in:** Python

##### Python

```python
exporter = OTLPMetricExporter(endpoint="http://localhost:4318/v1/metrics")
reader = PeriodicExportingMetricReader(exporter=exporter, export_interval_millis=10000)
provider = MeterProvider(metric_readers=[reader])
metrics.set_meter_provider(provider)
```



## Configure the Redis client

You configure the client library for OTel only once per application. This will
enable OTel for all Redis connections you create. The example below shows the
options you can pass to the observability instance via the `OTelConfig` object
during initialization.

Foundational: Configure Redis observability with a list of metric groups and optional command filtering and privacy controls

**Difficulty:** Beginner

**Available in:** Python

##### Python

```python
otel = get_observability_instance()
otel.init(OTelConfig(
    # Metric groups to enable (default: CONNECTION_BASIC | RESILIENCY)
    metric_groups=[
        MetricGroup.CONNECTION_BASIC,    # Connection creation time, relaxed timeout
        MetricGroup.CONNECTION_ADVANCED, # Connection wait time, timeouts, closed connections
        MetricGroup.COMMAND,             # Command execution duration
        MetricGroup.RESILIENCY,          # Error counts, maintenance notifications
        MetricGroup.PUBSUB,              # PubSub message counts
        MetricGroup.STREAMING,           # Stream message lag
        MetricGroup.CSC,                 # Client Side Caching metrics
    ],

    # Filter which commands to track
    include_commands=['GET', 'SET', 'HGET'],  # Only track these commands
    # OR
    exclude_commands=['DEBUG', 'SLOWLOG'],    # Track all except these

    # Privacy controls
    hide_pubsub_channel_names=True,  # Hide channel names in PubSub metrics
    hide_stream_names=True,          # Hide stream names in streaming metrics

    # Custom histogram buckets
    buckets_operation_duration=[
        0.0001, 0.00025, 0.0005, 0.001, 0.0025, 0.005, 0.01, 0.025, 0.05, 0.1,
        0.25, 0.5, 1, 2.5,
    ],
    buckets_stream_processing_duration=[
        0.0001, 0.00025, 0.0005, 0.001, 0.0025, 0.005, 0.01, 0.025, 0.05, 0.1,
        0.25, 0.5, 1, 2.5,
    ],
    buckets_connection_create_time=[
        0.0001, 0.00025, 0.0005, 0.001, 0.0025, 0.005, 0.01, 0.025, 0.05, 0.1,
        0.25, 0.5, 1, 2.5,
    ],
    buckets_connection_wait_time=[
        0.0001, 0.00025, 0.0005, 0.001, 0.0025, 0.005, 0.01, 0.025, 0.05, 0.1,
        0.25, 0.5, 1, 2.5,
    ],
))
```



The available options for `OTelConfig` are described in the table below:

| Option | Type | Description |
| --- | --- | --- |
| `metric_groups` | `List[MetricGroup]` | List of metric groups to enable. By default, only `CONNECTION_BASIC` and `RESILIENCY` are enabled. See [Redis metric groups](https://redis.io/docs/latest/develop/clients/observability#redis-metric-groups) for a list of available groups. |
| `include_commands` | `List[str]` | List of Redis commands to track. If set, only these commands will be tracked. Note that you should use the Redis command name rather than the Python method name where the two differ. |
| `exclude_commands` | `List[str]` | List of Redis commands to exclude from tracking. If set, all commands except these will be tracked. Note that you should use the Redis command name rather than the Python method name where the two differ. |
| `hide_pubsub_channel_names` | `bool` | If true, channel names in pub/sub metrics will be hidden. |
| `hide_stream_names` | `bool` | If true, stream names in streaming metrics will be hidden. |
| `buckets_operation_duration` | `List[float]` | List of bucket boundaries for the [`operation.duration`](https://redis.io/docs/latest/develop/clients/observability#metric-db.client.operation.duration) histogram (see [Custom histogram buckets](#custom-histogram-buckets) below). |
| `buckets_stream_processing_duration` | `List[float]` | List of bucket boundaries for the [`stream.lag`](https://redis.io/docs/latest/develop/clients/observability#metric-redis.client.stream.lag) histogram (see [Custom histogram buckets](#custom-histogram-buckets) below). |
| `buckets_connection_create_time` | `List[float]` | List of bucket boundaries for the [`connection.create.time`](https://redis.io/docs/latest/develop/clients/observability#metric-db.client.connection.create_time) histogram (see [Custom histogram buckets](#custom-histogram-buckets) below). |
| `buckets_connection_wait_time` | `List[float]` | List of bucket boundaries for the [`connection.wait.time`](https://redis.io/docs/latest/develop/clients/observability#metric-db.client.connection.wait_time) histogram (see [Custom histogram buckets](#custom-histogram-buckets) below). |

### Custom histogram buckets

For the histogram metrics, a reasonable default set of buckets is defined, but
you can customize the bucket boundaries to suit your needs (the buckets are the
ranges of data values counted for each bar of the histogram). Pass an increasing
list of float values to the `buckets_xxx` options when you create the `OTelConfig`
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

**Available in:** Python

##### Python

```python
r = redis.Redis(host='localhost', port=6379)
r.set('key', 'value')  # Metrics collected automatically
r.get('key')
```



## Shutdown

When your application exits, you should call the `shutdown()` method to ensure
that all pending metrics are exported.

Foundational: Shutdown Redis observability

**Difficulty:** Beginner

**Available in:** Python

##### Python

```python
otel.shutdown()
```



