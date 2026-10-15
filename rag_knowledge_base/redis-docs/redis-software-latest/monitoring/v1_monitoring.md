# Metrics and alerts for monitoring v1

```json metadata
{
  "schema_version": 2,
  "title": "Metrics and alerts for monitoring v1",
  "description": "Monitor Redis Software clusters and databases using internal monitoring systems and external monitoring tools.",
  "categories": ["docs","operate","rs","kubernetes"],
  "tableOfContents": {"sections":[{"children":[{"id":"limitations","title":"Limitations"},{"id":"transition-to-the-metrics-stream-engine","title":"Transition to the metrics stream engine"},{"id":"transition-cluster-manager-alerts","title":"Transition cluster manager alerts"}],"id":"current-monitoring-system-deprecated","title":"Current monitoring system (deprecated)"},{"id":"cluster-manager-metrics","title":"Cluster manager metrics"},{"id":"cluster-alerts","title":"Cluster alerts"},{"id":"database-alerts","title":"Database alerts"},{"id":"send-alerts-by-email","title":"Send alerts by email"}]}

,
  "codeExamples": []
}
```


## Current monitoring system (deprecated)

The current monitoring system, which is deprecated as of Redis Software version 7.22, consists of the following components:

- Internal metrics storage:

    - Metrics are internally aggregated, calculated, and stored for up to one year.

    - This historical data is used to generate trends and performance insights over time.

- [Statistics APIs](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/statistics):

    - This set of RESTful APIs exposes metrics collected at regular intervals from clusters, nodes, databases, shards, and endpoints.

    - These APIs allow customers to retrieve performance and usage statistics directly from the internal storage layer.

- Cluster manager metrics and alerts:

    - The Cluster Manager UI includes [dedicated metrics pages](#cluster-manager-metrics) that display pre-aggregated metrics.

    - [Cluster alerts](#cluster-alerts) are triggered based on thresholds applied to these stored metrics.
      
- v1 Prometheus scraping endpoint:

    - Redis Software exposes a legacy `/prometheus_metrics` endpoint to integrate with external observability platforms like [Prometheus and Grafana](https://redis.io/docs/latest/operate/rs/monitoring/get-started).

    - This endpoint fetches data from the internal storage, providing basic monitoring integration.

### Limitations

The internal monitoring system, while functional, has several limitations that affect scalability and accuracy:
      
- **Limited granularity:** Metrics are aggregated before storage, resulting in a loss of fine-grained insights.

- **Stale data:** Stored metrics can lag behind real-time system states, reducing the effectiveness of alerting.

- **Visibility gaps during management operations:** Metrics and statistics may not be available or updated during management tasks, resulting in incomplete monitoring during critical activities.

- **Scalability constraints:** Internal storage and processing introduce performance overhead and are not optimized for large-scale observability pipelines.

- **Limited extensibility:** The system is tightly coupled with internal components, making it difficult to integrate with modern monitoring ecosystems.

### Transition to the metrics stream engine

To improve monitoring and address current limitations, Redis Software is transitioning to a new observability foundation: the [metrics stream engine](https://redis.io/docs/latest/operate/rs/monitoring/metrics_stream_engine).

This modern monitoring stack introduces:

- Real-time metrics, exposed directly from the engine without intermediate storage for high-fidelity, low-latency insights.

- Scalable architecture designed for cloud-native observability with lightweight Prometheus collectors.

- Deeper visibility by exposing new types of metrics such as key size distribution, server overall latency histograms, and system internals with per-endpoint resolution.

We recommend migrating to the metrics stream engine for enhanced accuracy, scalability, and future-proof observability.

If you are already using the existing scraping endpoint for integration, follow [this guide](https://redis.io/docs/latest/operate/rs/monitoring/metrics_stream_engine/prometheus-metrics-v1-to-v2) to transition and try the new engine. It is possible to scrape both existing and new endpoints simultaneously, allowing advanced dashboard preparation and a smooth transition.

### Transition cluster manager alerts

As part of Redis Software's transition to the [new metrics stream engine](https://redis.io/docs/latest/operate/rs/monitoring/metrics_stream_engine), some internal cluster manager alerts were deprecated in favor of external monitoring solutions. See the [alerts transition plan](https://redis.io/docs/latest/operate/rs/monitoring/metrics_stream_engine/alerts-v1-to-v2) for guidance.

## Cluster manager metrics

You can see the metrics of the cluster in:

- **Cluster > Metrics**
- **Node > Metrics** for each node
- **Database > Metrics** for each database, including the shards for that database

The scale selector at the top of the page allows you to set the X-axis (time) scale of the graph.

To choose which metrics to display in the two large graphs at the top of the page:

1. Hover over the graph you want to show in a large graph.
1. Click on the right or left arrow to choose which side to show the graph.

We recommend that you show two similar metrics in the top graphs so you can compare them side-by-side.

See the following topics for metrics definitions:
- [Database operations](https://redis.io/docs/latest/operate/rs/references/metrics/database-operations) for database metrics
- [Resource usage](https://redis.io/docs/latest/operate/rs/references/metrics/resource-usage) for resource and database usage metrics
- [Auto Tiering](https://redis.io/docs/latest/operate/rs/references/metrics/auto-tiering) for additional metrics for [Auto Tiering ](https://redis.io/docs/latest/operate/rs/databases/flash) databases

## Cluster alerts

In **Cluster > Alert Settings**, you can enable alerts for node or cluster events, such as high memory usage or throughput.

Configured alerts are shown:

- As a notification on the status icon (  ) for the node and cluster
- In the **log**
- In email notifications, if you configure [email alerts](#send-alerts-by-email)

> [!NOTE]
> If you enable alerts for "Node joined" or "Node removed" actions,
> you must also enable "Receive email alerts" so that the notifications are sent.

To enable alerts for a cluster:

1. In **Cluster > Alert Settings**, click **Edit**. 
1. Select the alerts that you want to show for the cluster and click **Save**.

## Database alerts

For each database, you can enable alerts for database events, such as high memory usage or throughput.

Configured alerts are shown:

- As a notification on the status icon (  ) for the database
- In the **log**
- In emails, if you configure [email alerts](#send-alerts-by-email)

To enable alerts for a database:

1. In **Configuration** for the database, click **Edit**.
1. Select the **Alerts** section to open it.
1. Select the alerts that you want to show for the database and click **Save**.

## Send alerts by email

To send cluster and database alerts by email:

1. In **Cluster > Alert Settings**, click **Edit**.
1. Select **Set an email** to configure the [email server settings](https://redis.io/docs/latest/operate/rs/clusters/configure/cluster-settings#configuring-email-server-settings).
1. In **Configuration** for the database, click **Edit**.
1. Select the **Alerts** section to open it.
1. Select **Receive email alerts** and click **Save**.
1. In **Access Control**, select the [database and cluster alerts](https://redis.io/docs/latest/operate/rs/security/access-control/create-users#add-users) that you want each user to receive.

