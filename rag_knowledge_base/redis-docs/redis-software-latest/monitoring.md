# Monitoring with metrics and alerts

```json metadata
{
  "schema_version": 2,
  "title": "Monitoring with metrics and alerts",
  "description": "Use the metrics that measure the performance of your Redis Software clusters, nodes, databases, and shards to track the performance of your databases.",
  "categories": ["docs","operate","rs","kubernetes"],
  "tableOfContents": {"sections":[{"id":"view-metrics-and-configure-alerts","title":"View metrics and configure alerts"},{"id":"metrics-stream-engine","title":"Metrics stream engine"},{"id":"integrate-with-external-monitoring-tools","title":"Integrate with external monitoring tools"},{"id":"metrics-reference","title":"Metrics reference"}]}

,
  "codeExamples": []
}
```


You can use the metrics that measure the performance of your Redis Software clusters, nodes, databases, and shards
to monitor the performance of your databases.

## View metrics and configure alerts

In the Redis Software Cluster Manager UI, you can view metrics, configure alerts, and send notifications based on alert parameters. You can also access metrics and configure alerts through the REST API.

See [Metrics and alerts for monitoring v1](https://redis.io/docs/latest/operate/rs/monitoring/v1_monitoring) for more information.

## Metrics stream engine

The new metrics stream engine is generally available as of [Redis Software version 8.0](https://redis.io/docs/latest/operate/rs/release-notes/rs-8-0-releases) This new engine exposes the v2 Prometheus scraping endpoint at `https://<cluster_name>:8070/v2`, exports all time-series metrics to external monitoring tools, and enables real-time monitoring.

See [Metrics stream engine for monitoring v2](https://redis.io/docs/latest/operate/rs/monitoring/metrics_stream_engine) for more information.

## Integrate with external monitoring tools

To integrate Redis Software metrics into your monitoring environment, see the following integration guides:

- [Grafana](https://redis.io/docs/latest/integrate/prometheus-with-redis-enterprise)

- [Datadog](https://redis.io/docs/latest/integrate/datadog-with-redis-enterprise)

- [Dynatrace](https://redis.io/docs/latest/integrate/dynatrace-with-redis-enterprise)

- [New Relic](https://redis.io/docs/latest/integrate/new-relic-with-redis-enterprise)

For a detailed tutorial to deploy a complete monitoring stack with Prometheus and Grafana, see [Redis Software Observability with Prometheus and Grafana](https://redis.io/learn/operate/observability/redis-software-prometheus-and-grafana).

Filter [Libraries and tools](https://redis.io/docs/latest/integrate) by "observability" for additional tools and guides.

## Metrics reference

Make sure you read the [definition of each metric](https://redis.io/docs/latest/operate/rs/references/metrics)
so that you understand exactly what it represents.

