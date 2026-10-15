# RedisTimeSeries release notes

```json metadata
{
  "schema_version": 2,
  "title": "RedisTimeSeries release notes",
  "description": "RedisTimeSeries release notes for version 1.12 and earlier",
  "categories": ["docs","operate","stack"],
  "tableOfContents": {"sections":[]}

,
  "codeExamples": []
}
```


| Version (Release date) | Major changes | Min Redis version | Min cluster version |
| --- | --- | --- | --- |
| [v1.12 (July 2024)](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/release-notes/redistimeseries/redistimeseries-1.12-release-notes/) | RedisTimeSeries 1.12 adds a highly requested feature - insertion-filter for close samples. | 7.4 | 7.8 |
| [v1.10 (July 2023)](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/release-notes/redistimeseries/redistimeseries-1.10-release-notes/) | RESP3 support. Performance improvements. | 7.2 | 7.2.4 |
| [v1.8 (November 2022)](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/release-notes/redistimeseries/redistimeseries-1.8-release-notes/) | Added a time-weighted average aggregator, gap filling, ability to control bucket timestamps, ability to control alignment for compaction rules, new reducer types, and ability to include the latest (possibly partial) raw bucket samples when retrieving compactions | 6.0.16 | 6.2.8 |
| [v1.6 (January 2022)](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/release-notes/redistimeseries/redistimeseries-1.6-release-notes/) | Added support for aggregating across multiple time series (multi-key). Can compute queries such as "the maximum observed value of a set of time series" server-side instead of client-side. | 6.0.16 | 6.2.8 |
| [v1.4 (September 2020)](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/release-notes/redistimeseries/redistimeseries-1.4-release-notes/) | Added ability to backfill time series. | 5.0.0 | 6.0.12 |
| [v1.2 (January 2020)](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/release-notes/redistimeseries/redistimeseries-1.2-release-notes/) | Added compression. Stable ingestion time independent of the number of the data points on a time series. API performance improvements. Extended client support. | 5.0.0 | 6.0.12 |
| [v1.0 (June 2019)](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/release-notes/redistimeseries/redistimeseries-1.0-release-notes/) | Downsampling/compaction. Secondary indexing. Aggregation at read time. Integration with Prometheus, Grafana, and Telegraph. | 5.0.0 | 5.4.0 |


