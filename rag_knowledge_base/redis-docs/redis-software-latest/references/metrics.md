# Real-time metrics

```json metadata
{
  "schema_version": 2,
  "title": "Real-time metrics",
  "description": "Documents the metrics that are tracked with Redis Software.",
  "categories": ["docs","operate","rs","rc"],
  "tableOfContents": {"sections":[{"id":"cluster-manager-metrics","title":"Cluster manager metrics"},{"id":"prometheus-metrics","title":"Prometheus metrics"},{"children":[{"id":"shard-limit","title":"Shard limit"},{"id":"metrics-not-shown-during-shard-migration","title":"Metrics not shown during shard migration"}],"id":"limitations","title":"Limitations"}]}

,
  "codeExamples": []
}
```


## Cluster manager metrics

In the Redis Software Cluster Manager UI, you can see real-time performance metrics for clusters, nodes, databases, and shards, and configure alerts that send notifications based on alert parameters. Select the **Metrics** tab to view the metrics for each component. For more information, see [Monitoring with metrics and alerts](https://redis.io/docs/latest/operate/rs/monitoring).

![The database metrics page.](https://redis.io/docs/latest/images/rs/screenshots/metrics/db-metrics.png)

See the following topics for metrics definitions:
- [Database operations](https://redis.io/docs/latest/operate/rs/references/metrics/database-operations) for database metrics
- [Resource usage](https://redis.io/docs/latest/operate/rs/references/metrics/resource-usage) for resource and database usage metrics
- [Auto Tiering](https://redis.io/docs/latest/operate/rs/references/metrics/auto-tiering) for additional metrics for [Auto Tiering ](https://redis.io/docs/latest/operate/rs/databases/flash) databases

## Prometheus metrics

To collect and display metrics data from your databases and other cluster components,
you can connect your [Prometheus](https://prometheus.io/) and [Grafana](https://grafana.com/) server to your Redis Software cluster. We recommend you use Prometheus and Grafana to view metrics history and trends.

See [Prometheus integration](https://redis.io/docs/latest/operate/rs/monitoring/get-started) to learn how to connect Prometheus and Grafana to your Redis Software database.

The new metrics stream engine that exposes the v2 Prometheus scraping endpoint at `https://<cluster_name>:8070/v2` is generally available as of Redis Software version 8.0.
This new engine exports all time-series metrics to external monitoring tools such as Grafana, DataDog, NewRelic, and Dynatrace using Prometheus.

The new engine enables real-time monitoring, including full monitoring during maintenance operations, providing full visibility into performance during events such as shards' failovers and scaling operations.

For a list of available metrics, see the following references:

- [Prometheus metrics v1](https://redis.io/docs/latest/operate/rs/references/metrics/prometheus-metrics-v1)

- [Prometheus metrics v2](https://redis.io/docs/latest/operate/rs/references/metrics/prometheus-metrics-v2)

If you are already using the existing scraping endpoint for integration, follow [this guide](https://redis.io/docs/latest/operate/rs/references/metrics/prometheus-metrics-v1-to-v2) to transition and try the new engine. It is possible to scrape both existing and new endpoints simultaneously, allowing advanced dashboard preparation and a smooth transition.

## Limitations

### Shard limit

Metrics information is not shown for clusters with more than 128 shards. For large clusters, we recommend you use [Prometheus and Grafana](https://redis.io/docs/latest/operate/rs/monitoring/get-started) to view metrics.

### Metrics not shown during shard migration

The following metrics are not measured during [shard migration](https://redis.io/docs/latest/operate/rs/databases/configure/replica-ha) when using the [internal monitoring systems](https://redis.io/docs/latest/operate/rs/monitoring/v1_monitoring). If you view these metrics while resharding, the graph will be blank.

- [Evicted objects/sec](https://redis.io/docs/latest/operate/rs/references/metrics/database-operations#evicted-objectssec)
- [Expired objects/sec](https://redis.io/docs/latest/operate/rs/references/metrics/database-operations#expired-objectssec)
- [Read misses/sec](https://redis.io/docs/latest/operate/rs/references/metrics/database-operations#read-missessec)
- [Write misses/sec](https://redis.io/docs/latest/operate/rs/references/metrics/database-operations#write-missessec)
- [Total keys](https://redis.io/docs/latest/operate/rs/references/metrics/database-operations#total-keys)
- [Incoming traffic](https://redis.io/docs/latest/operate/rs/references/metrics/resource-usage#incoming-traffic)
- [Outgoing traffic](https://redis.io/docs/latest/operate/rs/references/metrics/resource-usage#outgoing-traffic)
- [Used memory](https://redis.io/docs/latest/operate/rs/references/metrics/resource-usage#used-memory)

This limitation does not apply to the new [metrics stream engine](https://redis.io/docs/latest/operate/rs/monitoring/metrics_stream_engine).

