# Metrics configuration

```json metadata
{
  "schema_version": 2,
  "title": "Metrics configuration",
  "description": "Configure the Redis Software v2 metrics stream engine.",
  "categories": ["docs","integrate","rs"],
  "group": "observability",
  "tableOfContents": {"sections":[{"children":[{"id":"rest-api","title":"REST API"},{"id":"rladmin","title":"rladmin"}],"id":"configure-metrics-settings","title":"Configure metrics settings"}]}

,
  "codeExamples": []
}
```


The metrics configuration is a cluster-wide resource that controls the behavior of the [v2 metrics stream engine](https://redis.io/docs/latest/operate/rs/monitoring/metrics_stream_engine), such as which optional metrics are collected and how metrics are stored and exported.

For the full list of configuration fields, their types, and defaults, see the [metrics configuration object](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/metrics_config).

## Configure metrics settings

You can read and update the metrics configuration through the REST API or with `rladmin`.

Changes to the metrics configuration are recorded in the cluster's [event logs](https://redis.io/docs/latest/operate/rs/clusters/logging), so you can review who changed a setting and when.

### REST API

Use the `GET` and `PUT` `/v1/metrics_config` requests to read and update the configuration. For request and response details, required permissions, and status codes, see [Metrics configuration requests](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/metrics_config).

### rladmin

Use [`rladmin info metrics`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/info#info-metrics) to view the current configuration and [`rladmin metrics config`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/metrics#metrics-config) to update it.

