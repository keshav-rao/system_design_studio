# Observability

```json metadata
{
  "schema_version": 2,
  "title": "Observability",
  "description": "Monitor your client's activity for optimization and debugging.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"installation","title":"Installation"},{"id":"import","title":"Import"},{"id":"configure-the-meter-provider","title":"Configure the meter provider"},{"children":[{"id":"custom-histogram-buckets","title":"Custom histogram buckets"}],"id":"configure-the-redis-client","title":"Configure the Redis client"},{"id":"use-redis","title":"Use Redis"},{"id":"shutdown","title":"Shutdown"}]}

,
  "codeExamples": [{"codetabsId":"observability-stepimport","description":"Foundational: Import required libraries for Redis observability, OpenTelemetry metrics, and Redis operations","difficulty":"beginner","id":"import","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_observability-stepimport"}]},{"codetabsId":"observability-stepsetup_meter_provider","description":"Foundational: Configure a meter provider to export metrics to a local Grafana instance every 10 seconds","difficulty":"beginner","id":"setup_meter_provider","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_observability-stepsetup_meter_provider"}]},{"codetabsId":"observability-stepclient_config","description":"Foundational: Configure Redis observability with a list of metric groups and optional command filtering and privacy controls","difficulty":"beginner","id":"client_config","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_observability-stepclient_config"}]},{"codetabsId":"observability-stepuse_redis","description":"Foundational: Use Redis with automatic instrumentation","difficulty":"beginner","id":"use_redis","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_observability-stepuse_redis"}]},{"codetabsId":"observability-stepshutdown","description":"Foundational: Shutdown Redis observability","difficulty":"beginner","id":"shutdown","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_observability-stepshutdown"}]}]
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


`go-redis` has built-in support for [OpenTelemetry](https://opentelemetry.io/) (OTel)
instrumentation to collect metrics. This can be very helpful for
diagnosing problems and improving the performance and connection resiliency of
your application. See the
[Observability overview](https://redis.io/docs/latest/develop/clients/observability)
for an introduction to Redis client observability and a reference guide for the
available metrics.

This page explains how to enable and use OTel instrumentation
in `go-redis` using an example configuration for a local [Grafana](https://grafana.com/)
instance. See our
[observability demonstration repository](https://github.com/redis-developer/redis-client-observability)
on GitHub to learn how to set up a suitable Grafana dashboard.

## Installation

Install OTel support for `go-redis` with the following commands:

```bash
go get github.com/redis/go-redis/extra/redisotel-native/v9
go get go.opentelemetry.io/otel
```

## Import

Start by importing the required OTel and Redis modules:

Foundational: Import required libraries for Redis observability, OpenTelemetry metrics, and Redis operations

**Difficulty:** Beginner

**Available in:** Go

##### Go

```go
import (
	"context"
	"fmt"
	"time"

	"github.com/redis/go-redis/extra/redisotel-native/v9"
	"github.com/redis/go-redis/v9"
	"go.opentelemetry.io/otel"
	"go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetricgrpc"
	"go.opentelemetry.io/otel/sdk/metric"
	"go.opentelemetry.io/otel/sdk/resource"
	semconv "go.opentelemetry.io/otel/semconv/v1.24.0"
)

```



## Configure the meter provider

Otel uses a [Meter provider](https://opentelemetry.io/docs/concepts/signals/metrics/#meter-provider)
to create the objects that collect the metric information. The example below
configures a meter provider to export metrics to a local Otel collector
every 10 seconds, but see the [OpenTelemetry Go docs](https://opentelemetry.io/docs/languages/go/)
to learn more about other export options.

Foundational: Configure a meter provider to export metrics to a local Grafana instance every 10 seconds

**Difficulty:** Beginner

**Available in:** Go

##### Go

```go
	ctx := context.Background()

	// Create OTLP exporter that sends metrics to the collector
	// Default endpoint is localhost:4317 (gRPC)
	exporter, err := otlpmetricgrpc.New(ctx,
		otlpmetricgrpc.WithInsecure(), // Use insecure for local development
		// For production, configure TLS and authentication:
		// otlpmetricgrpc.WithEndpoint("your-collector:4317"),
		// otlpmetricgrpc.WithTLSCredentials(...),
	)

	if err != nil {
		panic(err)
	}

	// Create resource with service name
	res, err := resource.New(ctx,
		resource.WithAttributes(
			semconv.ServiceName(
				fmt.Sprintf("go-redis-examples:%d", time.Now().Unix()),
			),
		),
	)

	if err != nil {
		panic(err)
	}

	// Create meter provider with periodic reader
	// Metrics are exported every 10 seconds
	meterProvider := metric.NewMeterProvider(
		metric.WithResource(res),
		metric.WithReader(
			metric.NewPeriodicReader(exporter,
				metric.WithInterval(10*time.Second),
			),
		),
	)

	// Set the global meter provider
	otel.SetMeterProvider(meterProvider)
```



## Configure the Redis client

You configure the client library for OTel only once per application. This will
enable OTel for all Redis connections you create. The example below shows the
options you can pass to the observability instance via the `redisotel.Config` object
during initialization.

Foundational: Configure Redis observability with a list of metric groups and optional command filtering and privacy controls

**Difficulty:** Beginner

**Available in:** Go

##### Go

```go
	// Initialize OTel instrumentation BEFORE creating Redis clients
	otelInstance := redisotel.GetObservabilityInstance()
	config := redisotel.NewConfig().
		// You must enable OTel explicitly
		WithEnabled(true).
		// Enable the metric groups you want to collect. Use bitwise OR
		// to combine multiple groups. The default is `MetricGroupAll`
		// which includes all groups.
		WithMetricGroups(redisotel.MetricGroupFlagCommand |
			redisotel.MetricGroupFlagConnectionBasic |
			redisotel.MetricGroupFlagResiliency |
			redisotel.MetricGroupFlagConnectionAdvanced).
		// Filter which commands to track
		WithIncludeCommands([]string{"GET", "SET"}).
		WithExcludeCommands([]string{"DEBUG", "SLOWLOG"}).
		// Privacy controls
		WithHidePubSubChannelNames(true).
		WithHideStreamNames(true).
		// Custom histogram buckets
		WithHistogramBuckets([]float64{
			0.0001, // 0.1ms
			0.0005, // 0.5ms
			0.001,  // 1ms
			0.005,  // 5ms
			0.01,   // 10ms
			0.05,   // 50ms
			0.1,    // 100ms
			0.5,    // 500ms
			1.0,    // 1s
			5.0,    // 5s
			10.0,   // 10s
		})

	if err := otelInstance.Init(config); err != nil {
		panic(err)
	}
```



The available option methods for `redisotel.Config` are described in the table below.

| Method | Type | Description |
| --- | --- | --- |
| `WithEnabled` | `bool` | Enable or disable OTel instrumentation. Default is `false`, so you must enable it explicitly. |
| `WithMetricGroups` | `MetricGroupFlag` | Bitmap of metric groups to enable. By default, all metrics are enabled (equivalent to `MetricGroupAll`). See [Redis metric groups](https://redis.io/docs/latest/develop/clients/observability#redis-metric-groups) for a list of available groups. |
| `WithIncludeCommands` | `[]string` | List of Redis commands to track. If set, only these commands will be tracked. Note that you should use the Redis command name rather than the Go method name (for example `LPOP` rather than `LPopCount`). |
| `WithExcludeCommands` | `[]string` | List of Redis commands to exclude from tracking. If set, all commands except these will be tracked. Note that you should use the Redis command name rather than the Go method name (for example `LPOP` rather than `LPopCount`). |
| `WithHidePubSubChannelNames` | `bool` | If true, channel names in pub/sub metrics will be hidden. |
| `WithHideStreamNames` | `bool` | If true, stream names in streaming metrics will be hidden. |
| `WithHistogramBuckets` | `[]float64` | List of bucket boundaries for the histogram metrics. See [Custom histogram buckets](#custom-histogram-buckets) below for more information. |

### Custom histogram buckets

For the histogram metrics, a reasonable default set of buckets is defined, but
you can customize the bucket boundaries to suit your needs (the buckets are the
ranges of data values counted for each bar of the histogram). Pass an increasing
list of float values to the `WithHistogramBuckets` option when you create the `redisotel.Config`
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

**Available in:** Go

##### Go

```go
	rdb := redis.NewClient(&redis.Options{
		Addr:     "localhost:6379",
		Password: "", // no password set
		DB:       0,  // use default DB
	})

	rdb.Set(ctx, "key", "value", 0)
	v, err := rdb.Get(ctx, "key").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(v)
```



## Shutdown

When your application exits, you should close the Redis connection and then
you should call the `Shutdown()` method on the
`ObservabilityInstance` and `MeterProvider` instances to ensure that all pending
metrics are exported. You may find it useful to put the shutdown code in a
`defer` statement to ensure that it is called even if the main function
exits early due to an error.

Foundational: Shutdown Redis observability

**Difficulty:** Beginner

**Available in:** Go

##### Go

```go
	rdb.Close()
	otelInstance.Shutdown()
	meterProvider.Shutdown(context.Background())
```



