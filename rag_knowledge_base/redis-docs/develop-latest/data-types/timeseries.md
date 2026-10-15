# Time series

```json metadata
{
  "schema_version": 2,
  "title": "Time series",
  "description": "Ingest and query time series data with Redis",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"create-a-time-series","title":"Create a time series"},{"id":"add-data-points","title":"Add data points"},{"children":[{"id":"query-multiple-time-series","title":"Query multiple time series"}],"id":"query-data-points","title":"Query data points"},{"children":[{"id":"bucket-alignment","title":"Bucket alignment"},{"id":"aggregation-across-timeseries","title":"Aggregation across timeseries"}],"id":"aggregation","title":"Aggregation"},{"children":[{"id":"use-cases-for-nan-values","title":"Use Cases for NaN Values"},{"id":"nan-behavior","title":"NaN Behavior"}],"id":"nan-values","title":"NaN Values"},{"id":"compaction","title":"Compaction"},{"id":"delete-data-points","title":"Delete data points"},{"id":"use-time-series-with-other-metrics-tools","title":"Use time series with other metrics tools"},{"id":"more-information","title":"More information"}]}

,
  "codeExamples": [{"codetabsId":"time_series_tutorial-stepcreate","commands":[{"acl_categories":["@write","@fast","@timeseries"],"complexity":"O(1)","name":"TS.CREATE"},{"acl_categories":["@keyspace","@read","@fast"],"complexity":"O(1)","name":"TYPE"},{"acl_categories":["@read","@fast","@timeseries"],"complexity":"O(1)","name":"TS.INFO"}],"description":"Foundational: Use TS.CREATE to initialize a new time series key","difficulty":"beginner","id":"create","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_time_series_tutorial-stepcreate"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_time_series_tutorial-stepcreate"},{"id":"Node-js","panelId":"panel_Nodejs_time_series_tutorial-stepcreate"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_time_series_tutorial-stepcreate"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_time_series_tutorial-stepcreate"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_time_series_tutorial-stepcreate"}]},{"buildsUpon":["create"],"codetabsId":"time_series_tutorial-stepcreate_retention","commands":[{"acl_categories":["@write","@timeseries"],"complexity":"O(M)","name":"TS.ADD"},{"acl_categories":["@read","@fast","@timeseries"],"complexity":"O(1)","name":"TS.INFO"}],"description":"Data retention: Use TS.ADD with RETENTION option to automatically expire old data points based on time since the last update","difficulty":"intermediate","id":"create_retention","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_time_series_tutorial-stepcreate_retention"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_time_series_tutorial-stepcreate_retention"},{"id":"Node-js","panelId":"panel_Nodejs_time_series_tutorial-stepcreate_retention"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_time_series_tutorial-stepcreate_retention"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_time_series_tutorial-stepcreate_retention"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_time_series_tutorial-stepcreate_retention"}]},{"buildsUpon":["create"],"codetabsId":"time_series_tutorial-stepcreate_labels","commands":[{"acl_categories":["@write","@timeseries"],"complexity":"O(M)","name":"TS.ADD"},{"acl_categories":["@read","@fast","@timeseries"],"complexity":"O(1)","name":"TS.INFO"}],"description":"Labeling: Add metadata labels to time series using LABELS option when you need to organize and filter series by attributes like location or sensor type","difficulty":"beginner","id":"create_labels","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_time_series_tutorial-stepcreate_labels"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_time_series_tutorial-stepcreate_labels"},{"id":"Node-js","panelId":"panel_Nodejs_time_series_tutorial-stepcreate_labels"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_time_series_tutorial-stepcreate_labels"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_time_series_tutorial-stepcreate_labels"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_time_series_tutorial-stepcreate_labels"}]},{"buildsUpon":["create"],"codetabsId":"time_series_tutorial-stepmadd","commands":[{"acl_categories":["@keyspace","@write","@slow"],"complexity":"O(N)","name":"DEL"},{"acl_categories":["@write","@fast","@timeseries"],"complexity":"O(1)","name":"TS.CREATE"},{"acl_categories":["@write","@timeseries"],"complexity":"O(M)","name":"TS.ADD"},{"acl_categories":["@write","@timeseries"],"complexity":"O(N*M)","name":"TS.MADD"}],"description":"Batch operations: Add multiple data points to one or more time series using TS.MADD when you need to reduce round trips to the server","difficulty":"beginner","id":"madd","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_time_series_tutorial-stepmadd"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_time_series_tutorial-stepmadd"},{"id":"Node-js","panelId":"panel_Nodejs_time_series_tutorial-stepmadd"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_time_series_tutorial-stepmadd"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_time_series_tutorial-stepmadd"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_time_series_tutorial-stepmadd"}]},{"buildsUpon":["madd"],"codetabsId":"time_series_tutorial-stepget","commands":[{"acl_categories":["@keyspace","@write","@slow"],"complexity":"O(N)","name":"DEL"},{"acl_categories":["@write","@timeseries"],"complexity":"O(M)","name":"TS.ADD"},{"acl_categories":["@read","@fast","@timeseries"],"complexity":"O(1)","name":"TS.GET"}],"description":"Foundational: Use TS.GET to get the latest value and timestamp","difficulty":"beginner","id":"get","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_time_series_tutorial-stepget"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_time_series_tutorial-stepget"},{"id":"Node-js","panelId":"panel_Nodejs_time_series_tutorial-stepget"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_time_series_tutorial-stepget"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_time_series_tutorial-stepget"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_time_series_tutorial-stepget"}]},{"buildsUpon":["madd"],"codetabsId":"time_series_tutorial-steprange","commands":[{"acl_categories":["@write","@fast","@timeseries"],"complexity":"O(1)","name":"TS.CREATE"},{"acl_categories":["@write","@timeseries"],"complexity":"O(N*M)","name":"TS.MADD"},{"acl_categories":["@read","@timeseries"],"complexity":"O(n/m+k)","name":"TS.RANGE"},{"acl_categories":["@read","@timeseries"],"complexity":"O(n/m+k)","name":"TS.REVRANGE"}],"description":"Range queries: Retrieve data points within a timestamp range using TS.RANGE (ascending) or TS.REVRANGE (descending) when you need to analyze historical data","difficulty":"intermediate","id":"range","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_time_series_tutorial-steprange"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_time_series_tutorial-steprange"},{"id":"Node-js","panelId":"panel_Nodejs_time_series_tutorial-steprange"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_time_series_tutorial-steprange"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_time_series_tutorial-steprange"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_time_series_tutorial-steprange"}]},{"buildsUpon":["range"],"codetabsId":"time_series_tutorial-steprange_filter","commands":[{"acl_categories":["@keyspace","@write","@slow"],"complexity":"O(N)","name":"DEL"},{"acl_categories":["@write","@fast","@timeseries"],"complexity":"O(1)","name":"TS.CREATE"},{"acl_categories":["@write","@timeseries"],"complexity":"O(N*M)","name":"TS.MADD"},{"acl_categories":["@read","@timeseries"],"complexity":"O(n/m+k)","name":"TS.RANGE"},{"acl_categories":["@read","@timeseries"],"complexity":"O(n/m+k)","name":"TS.REVRANGE"}],"description":"Filtering results: Use FILTER_BY_TS and FILTER_BY_VALUE options with range queries when you need to select specific timestamps or value ranges","difficulty":"intermediate","id":"range_filter","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_time_series_tutorial-steprange_filter"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_time_series_tutorial-steprange_filter"},{"id":"Node-js","panelId":"panel_Nodejs_time_series_tutorial-steprange_filter"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_time_series_tutorial-steprange_filter"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_time_series_tutorial-steprange_filter"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_time_series_tutorial-steprange_filter"}]},{"buildsUpon":["create_labels"],"codetabsId":"time_series_tutorial-stepquery_multi","commands":[{"acl_categories":["@write","@fast","@timeseries"],"complexity":"O(1)","name":"TS.CREATE"},{"acl_categories":["@write","@timeseries"],"complexity":"O(N*M)","name":"TS.MADD"},{"acl_categories":["@read","@timeseries"],"complexity":"O(n)","name":"TS.MGET"},{"acl_categories":["@read","@timeseries"],"complexity":"O(n/m+k)","name":"TS.MRANGE"},{"acl_categories":["@read","@timeseries"],"complexity":"O(n/m+k)","name":"TS.MREVRANGE"}],"description":"Multi-series queries: Use TS.MGET, TS.MRANGE, and TS.MREVRANGE with label filters when you need to query multiple time series based on label criteria","difficulty":"advanced","id":"query_multi","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_time_series_tutorial-stepquery_multi"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_time_series_tutorial-stepquery_multi"},{"id":"Node-js","panelId":"panel_Nodejs_time_series_tutorial-stepquery_multi"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_time_series_tutorial-stepquery_multi"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_time_series_tutorial-stepquery_multi"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_time_series_tutorial-stepquery_multi"}]},{"buildsUpon":["madd"],"codetabsId":"time_series_tutorial-stepagg","commands":[{"acl_categories":["@keyspace","@write","@slow"],"complexity":"O(N)","name":"DEL"},{"acl_categories":["@write","@fast","@timeseries"],"complexity":"O(1)","name":"TS.CREATE"},{"acl_categories":["@write","@timeseries"],"complexity":"O(N*M)","name":"TS.MADD"},{"acl_categories":["@read","@timeseries"],"complexity":"O(n/m+k)","name":"TS.RANGE"}],"description":"Aggregation: Use AGGREGATION option with range queries to compute statistics such as avg, sum, min, and max over time buckets when you need to reduce large datasets","difficulty":"intermediate","id":"agg","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_time_series_tutorial-stepagg"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_time_series_tutorial-stepagg"},{"id":"Node-js","panelId":"panel_Nodejs_time_series_tutorial-stepagg"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_time_series_tutorial-stepagg"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_time_series_tutorial-stepagg"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_time_series_tutorial-stepagg"}]},{"buildsUpon":["agg"],"codetabsId":"time_series_tutorial-stepagg_bucket","commands":[{"acl_categories":["@write","@fast","@timeseries"],"complexity":"O(1)","name":"TS.CREATE"},{"acl_categories":["@write","@timeseries"],"complexity":"O(N*M)","name":"TS.MADD"},{"acl_categories":["@read","@timeseries"],"complexity":"O(n/m+k)","name":"TS.RANGE"}],"description":"Bucket alignment: Use AGGREGATION with default zero alignment to group data into fixed-size time buckets when you need consistent time-based aggregations","difficulty":"intermediate","id":"agg_bucket","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_time_series_tutorial-stepagg_bucket"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_time_series_tutorial-stepagg_bucket"},{"id":"Node-js","panelId":"panel_Nodejs_time_series_tutorial-stepagg_bucket"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_time_series_tutorial-stepagg_bucket"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_time_series_tutorial-stepagg_bucket"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_time_series_tutorial-stepagg_bucket"}]},{"buildsUpon":["agg_bucket"],"codetabsId":"time_series_tutorial-stepagg_align","commands":[{"acl_categories":["@keyspace","@write","@slow"],"complexity":"O(N)","name":"DEL"},{"acl_categories":["@write","@fast","@timeseries"],"complexity":"O(1)","name":"TS.CREATE"},{"acl_categories":["@write","@timeseries"],"complexity":"O(N*M)","name":"TS.MADD"},{"acl_categories":["@read","@timeseries"],"complexity":"O(n/m+k)","name":"TS.RANGE"}],"description":"Custom alignment: Use ALIGN option with aggregations to align buckets to query range start/end when you need aggregations relative to specific time boundaries","difficulty":"advanced","id":"agg_align","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_time_series_tutorial-stepagg_align"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_time_series_tutorial-stepagg_align"},{"id":"Node-js","panelId":"panel_Nodejs_time_series_tutorial-stepagg_align"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_time_series_tutorial-stepagg_align"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_time_series_tutorial-stepagg_align"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_time_series_tutorial-stepagg_align"}]},{"buildsUpon":["agg","create_labels"],"codetabsId":"time_series_tutorial-stepagg_multi","commands":[{"acl_categories":["@write","@fast","@timeseries"],"complexity":"O(1)","name":"TS.CREATE"},{"acl_categories":["@write","@timeseries"],"complexity":"O(N*M)","name":"TS.MADD"},{"acl_categories":["@read","@timeseries"],"complexity":"O(n/m+k)","name":"TS.MRANGE"}],"description":"Cross-series aggregation: Use GROUPBY and REDUCE with TS.MRANGE to aggregate data across multiple time series by label when you need to compute statistics across groups","difficulty":"advanced","id":"agg_multi","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_time_series_tutorial-stepagg_multi"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_time_series_tutorial-stepagg_multi"},{"id":"Node-js","panelId":"panel_Nodejs_time_series_tutorial-stepagg_multi"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_time_series_tutorial-stepagg_multi"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_time_series_tutorial-stepagg_multi"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_time_series_tutorial-stepagg_multi"}]},{"buildsUpon":["create"],"codetabsId":"time_series_tutorial-stepcreate_compaction","commands":[{"acl_categories":["@write","@fast","@timeseries"],"complexity":"O(1)","name":"TS.CREATE"},{"acl_categories":["@write","@timeseries"],"complexity":"O(1)","name":"TS.CREATERULE"},{"acl_categories":["@read","@fast","@timeseries"],"complexity":"O(1)","name":"TS.INFO"}],"description":"Compaction rules: Use TS.CREATERULE to automatically aggregate data into a destination time series when you need to maintain pre-computed aggregations","difficulty":"advanced","id":"create_compaction","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_time_series_tutorial-stepcreate_compaction"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_time_series_tutorial-stepcreate_compaction"},{"id":"Node-js","panelId":"panel_Nodejs_time_series_tutorial-stepcreate_compaction"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_time_series_tutorial-stepcreate_compaction"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_time_series_tutorial-stepcreate_compaction"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_time_series_tutorial-stepcreate_compaction"}]},{"buildsUpon":["create_compaction"],"codetabsId":"time_series_tutorial-stepcomp_add","commands":[{"acl_categories":["@keyspace","@write","@slow"],"complexity":"O(N)","name":"DEL"},{"acl_categories":["@write","@fast","@timeseries"],"complexity":"O(1)","name":"TS.CREATE"},{"acl_categories":["@write","@timeseries"],"complexity":"O(1)","name":"TS.CREATERULE"},{"acl_categories":["@write","@timeseries"],"complexity":"O(N*M)","name":"TS.MADD"},{"acl_categories":["@read","@timeseries"],"complexity":"O(n/m+k)","name":"TS.RANGE"},{"acl_categories":["@write","@timeseries"],"complexity":"O(M)","name":"TS.ADD"}],"description":"Compaction behavior: Understand how compaction rules process data incrementally, computing aggregates for completed buckets when new data arrives","difficulty":"intermediate","id":"comp_add","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_time_series_tutorial-stepcomp_add"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_time_series_tutorial-stepcomp_add"},{"id":"Node-js","panelId":"panel_Nodejs_time_series_tutorial-stepcomp_add"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_time_series_tutorial-stepcomp_add"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_time_series_tutorial-stepcomp_add"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_time_series_tutorial-stepcomp_add"}]},{"buildsUpon":["create"],"codetabsId":"time_series_tutorial-stepdel","commands":[{"acl_categories":["@keyspace","@write","@slow"],"complexity":"O(N)","name":"DEL"},{"acl_categories":["@write","@timeseries"],"complexity":"O(M)","name":"TS.ADD"},{"acl_categories":["@read","@fast","@timeseries"],"complexity":"O(1)","name":"TS.INFO"},{"acl_categories":["@write","@timeseries"],"complexity":"O(N)","name":"TS.DEL"}],"description":"Deleting data: Use TS.DEL to remove data points within a timestamp range when you need to clean up or correct historical data","difficulty":"beginner","id":"del","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_time_series_tutorial-stepdel"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_time_series_tutorial-stepdel"},{"id":"Node-js","panelId":"panel_Nodejs_time_series_tutorial-stepdel"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_time_series_tutorial-stepdel"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_time_series_tutorial-stepdel"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_time_series_tutorial-stepdel"}]}]
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


### Time series command summary

**21 commands in this group:**

[View all timeseries commands](https://redis.io/commands/?group=timeseries)

| Command | Summary | Complexity | Since |
|---------|---------|------------|-------|
| [TS.ADD](https://redis.io/commands/ts.add/) | Append a sample to a time series | O(M) where M is the number of compaction rules ... | 1.0.0 |
| [TS.ALTER](https://redis.io/commands/ts.alter/) | Update the retention, chunk size, duplicate policy, and labels of an existing time series | O(N) where N is the number of labels requested ... | 1.0.0 |
| [TS.CREATE](https://redis.io/commands/ts.create/) | Create a new time series | O(1) | 1.0.0 |
| [TS.CREATERULE](https://redis.io/commands/ts.createrule/) | Create a compaction rule | O(1) | 1.0.0 |
| [TS.DECRBY](https://redis.io/commands/ts.decrby/) | Decrease the value of the latest sample | O(M) when M is the amount of compaction rules o... | 1.0.0 |
| [TS.DEL](https://redis.io/commands/ts.del/) | Delete all samples between two timestamps for a given time series | O(N) where N is the number of data points that ... | 1.6.0 |
| [TS.DELETERULE](https://redis.io/commands/ts.deleterule/) | Delete a compaction rule | O(1) | 1.0.0 |
| [TS.GET](https://redis.io/commands/ts.get/) | Get the sample with the highest timestamp from a given time series | O(1) | 1.0.0 |
| [TS.INCRBY](https://redis.io/commands/ts.incrby/) | Increase the value of the latest sample | O(M) when M is the amount of compaction rules o... | 1.0.0 |
| [TS.INFO](https://redis.io/commands/ts.info/) | Returns information and statistics for a time series | O(1) | 1.0.0 |

#### Time series command summary (part 2)

| Command | Summary | Complexity | Since |
|---------|---------|------------|-------|
| [TS.MADD](https://redis.io/commands/ts.madd/) | Append new samples to one or more time series | O(N*M) when N is the amount of series updated a... | 1.0.0 |
| [TS.MGET](https://redis.io/commands/ts.mget/) | Get the sample with the highest timestamp from each time series matching a specific filter | O(n) where n is the number of time-series that ... | 1.0.0 |
| [TS.MRANGE](https://redis.io/commands/ts.mrange/) | Query a range across multiple time series by filters in forward direction | O(n/m+k) where n = Number of data points, m = C... | 1.0.0 |
| [TS.MREVRANGE](https://redis.io/commands/ts.mrevrange/) | Query a range across multiple time series by filters in reverse direction | O(n/m+k) where n = Number of data points, m = C... | 1.4.0 |
| [TS.NRANGE](https://redis.io/commands/ts.nrange/) | Query a range across multiple time series in forward direction, returning the results pivoted by timestamp (one value column per key) | O(numkeys*(n/m+k)) where n = Number of samples,... | 8.10.0 |
| [TS.NREVRANGE](https://redis.io/commands/ts.nrevrange/) | Query a range across multiple time series in reverse direction, returning the results pivoted by timestamp (one value column per key) | O(numkeys*(n/m+k)) where n = Number of samples,... | 8.10.0 |
| [TS.QUERYINDEX](https://redis.io/commands/ts.queryindex/) | Get all time series keys matching a filter list | O(n) where n is the number of time-series that ... | 1.0.0 |
| [TS.QUERYLABELS](https://redis.io/commands/ts.querylabels/) | Get all label names, or all values of a given label, for time series matching a filter list, or all series | O(n) where n is the number of time-series that ... | 8.10.0 |
| [TS.RANGE](https://redis.io/commands/ts.range/) | Query a range in forward direction | O(n/m+k) where n = Number of data points, m = C... | 1.0.0 |
| [TS.READ](https://redis.io/commands/ts.read/) | Read: return up to max_count samples with timestamp >= timestamp. With BLOCK, waits up to milliseconds ms until at least min_count qualifying samples exist | O(log(n)+k) where n is the number of samples in... | 8.10.0 |

#### Time series command summary (part 3)

| Command | Summary | Complexity | Since |
|---------|---------|------------|-------|
| [TS.REVRANGE](https://redis.io/commands/ts.revrange/) | Query a range in reverse direction | O(n/m+k) where n = Number of data points, m = C... | 1.4.0 |



[![Discord](https://img.shields.io/discord/697882427875393627?style=flat-square)](https://discord.gg/KExRgMb)
[![Github](https://img.shields.io/static/v1?label=&message=repository&color=5961FF&logo=github)](https://github.com/RedisTimeSeries/RedisTimeSeries/)

The Redis time series data type lets you store real-valued data points
along with the time they were collected. You can combine the values from a selection
of time series and query them by time or value range. You can also compute
aggregators of the data over periods of time and create new time series
from the results. When you create a time series, you can specify a maximum
retention period for the data, relative to the last reported timestamp, to
prevent the time series from growing indefinitely.

Starting from Redis 8.6, time series support NaN (Not a Number) values, which allow you to represent missing or invalid measurements while maintaining the temporal structure of your data.

Time series support very fast reads and writes, making them ideal for
applications such as:

- Instrument data logging
- System performance metrics
- Financial market data
- Internet of Things (IoT) sensor data
- Smart metering
- Quality of service (QoS) monitoring

Redis time series are available in Redis Open Source, Redis Software, and Redis Cloud.
See
[Install Redis Open Source](https://redis.io/docs/latest/operate/oss_and_stack/install/install-stack) or
[Install Redis Software](https://redis.io/docs/latest/operate/rs/installing-upgrading/install)
for full installation instructions.

## Create a time series

You can create a new empty time series with the [`TS.CREATE`](https://redis.io/docs/latest/commands/ts.create)
command, specifying a key name. Alternatively, if you use [`TS.ADD`](https://redis.io/docs/latest/commands/ts.add)
to add data to a time series key that does not exist, it is automatically created (see
[Adding data points](#adding-data-points) below for more information about `TS.ADD`).

Foundational: Use TS.CREATE to initialize a new time series key

**Difficulty:** Beginner

**Commands:** TS.CREATE, TYPE, TS.INFO

**Complexity:**
- TS.CREATE: O(1)
- TYPE: O(1)
- TS.INFO: O(1)

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python

##### Redis CLI

```
> TS.CREATE thermometer:1
OK
> TYPE thermometer:1
TSDB-TYPE
> TS.INFO thermometer:1
 1) totalSamples
 2) (integer) 0
 3) memoryUsage
 4) (integer) 4504
 5) firstTimestamp
 6) (integer) 0
 7) lastTimestamp
 8) (integer) 0
 9) retentionTime
10) (integer) 0
11) chunkCount
12) (integer) 1
13) chunkSize
14) (integer) 4096
15) chunkType
16) compressed
17) duplicatePolicy
18) block
19) labels
20) (empty array)
21) sourceKey
22) (nil)
23) rules
24) (empty array)
25) ignoreMaxTimeDiff
26) (integer) 0
27) ignoreMaxValDiff
28) "0"
```

##### C#

```csharp
        bool res1 = db.TS().Create(
            "thermometer:1",
            new TsCreateParamsBuilder().build()
        );
        Console.WriteLine(res1); // >>> True

        RedisType res2 = db.KeyType("thermometer:1");
        Console.WriteLine(res2); // >>> TSDB-TYPE

        TimeSeriesInformation res3 = db.TS().Info("thermometer:1");
        Console.WriteLine(res3.TotalSamples); // >>> 0
```

##### Go

```go
	res1, err := rdb.TSCreate(ctx, "thermometer:1").Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // >>> OK

	res2, err := rdb.Type(ctx, "thermometer:1").Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res2) // >>> TSDB-TYPE

	res3, err := rdb.TSInfo(ctx, "thermometer:1").Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res3["totalSamples"]) // >>> 0
```

##### Java (Synchronous - Jedis)

```java
        String res1 = jedis.tsCreate("thermometer:1");
        System.out.println(res1); // >>> OK

        String res2 = jedis.type("thermometer:1");
        System.out.println(res2); // >>> TSDB-TYPE

        TSInfo res3 = jedis.tsInfo("thermometer:1");
        System.out.println(res3.getProperty("totalSamples")); // >>> 0
```

##### JavaScript (Node.js)

```javascript
const res1 = await client.ts.create('thermometer:1');
console.log(res1); // >>> OK

const res2 = await client.type('thermometer:1');
console.log(res2); // >>> TSDB-TYPE

const res3 = await client.ts.info('thermometer:1');
console.log(res3);
// >>> { rules: [], ... totalSamples: 0, ...
```

##### Python

```python
res1 = r.ts().create("thermometer:1")
print(res1)  # >>> True

res2 = r.type("thermometer:1")
print(res2)  # >>> TSDB-TYPE

res3 = r.ts().info("thermometer:1")
print(res3)
# >>> {'rules': [], ... 'total_samples': 0, ...
```



The timestamp for each data point is a 64-bit integer value. The value
represents a Unix timestamp, measured in milliseconds since the
[Unix epoch](https://en.wikipedia.org/wiki/Unix_time).
When you create a time series, you can specify a maximum retention period for the
data, relative to the last reported timestamp. A retention period of zero means
the data does not expire.

Data retention: Use TS.ADD with RETENTION option to automatically expire old data points based on time since the last update

**Difficulty:** Intermediate

**Builds upon:** create

**Commands:** TS.ADD, TS.INFO

**Complexity:**
- TS.ADD: O(M)
- TS.INFO: O(1)

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python

##### Redis CLI

```
# Create a new time series with a first value of 10.8 (Celsius), recorded at time 1, with a retention period of 100ms.
> TS.ADD thermometer:2 1 10.8 RETENTION 100
(integer) 1
> TS.INFO thermometer:2
 1) totalSamples
 2) (integer) 1
 3) memoryUsage
 4) (integer) 4504
 5) firstTimestamp
 6) (integer) 1
 7) lastTimestamp
 8) (integer) 1
 9) retentionTime
10) (integer) 100
11) chunkCount
12) (integer) 1
13) chunkSize
14) (integer) 4096
15) chunkType
16) compressed
17) duplicatePolicy
18) block
19) labels
20) (empty array)
21) sourceKey
22) (nil)
23) rules
24) (empty array)
25) ignoreMaxTimeDiff
26) (integer) 0
27) ignoreMaxValDiff
28) "0"
```

##### C#

```csharp
        long res4 = db.TS().Add(
            "thermometer:2",
            new TsAddParamsBuilder()
                .AddTimestamp(1)
                .AddValue(10.8)
                .AddRetentionTime(100)
                .build()
        );
        Console.WriteLine(res4); // >>> 1

        TimeSeriesInformation res5 = db.TS().Info("thermometer:2");
        Console.WriteLine(res5.RetentionTime);
        // >>> 100
```

##### Go

```go
	res4, err := rdb.TSAddWithArgs(
		ctx,
		"thermometer:2",
		1,
		10.8,
		&redis.TSOptions{
			Retention: 100,
		},
	).Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res4) // >>> 1

	res5, err := rdb.TSInfo(ctx, "thermometer:2").Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res5["retentionTime"]) // >>> 100
```

##### Java (Synchronous - Jedis)

```java
        long res4 = jedis.tsAdd("thermometer:2", 1L, 10.8, 
            TSCreateParams.createParams().retention(100));
        System.out.println(res4); // >>> 1

        TSInfo res5 = jedis.tsInfo("thermometer:2");
        System.out.println(res5.getProperty("retentionTime")); // >>> 100
```

##### JavaScript (Node.js)

```javascript
const res4 = await client.ts.add('thermometer:2', 1, 10.8, { RETENTION: 100 });
console.log(res4); // >>> 1

const res5 = await client.ts.info('thermometer:2');
console.log(res5);
// >>> { rules: [], ... retentionTime: 100, ...
```

##### Python

```python
res4 = r.ts().add("thermometer:2", 1, 10.8, retention_msecs=100)
print(res4)  # >>> 1

res5 = r.ts().info("thermometer:2")
print(res5)
# >>> {'rules': [], ... 'retention_msecs': 100, ...
```



You can also add one or more *labels* to a time series when you create it. Labels
are name-value pairs where both the name and value are strings. You can use
the names and values to select subsets of all the available time series
for queries and aggregations.

Labeling: Add metadata labels to time series using LABELS option when you need to organize and filter series by attributes like location or sensor type

**Difficulty:** Beginner

**Builds upon:** create

**Commands:** TS.ADD, TS.INFO

**Complexity:**
- TS.ADD: O(M)
- TS.INFO: O(1)

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python

##### Redis CLI

```
> TS.ADD thermometer:3 1 10.4 LABELS location UK type Mercury
(integer) 1
> TS.INFO thermometer:3
 1) totalSamples
 2) (integer) 1
 3) memoryUsage
 4) (integer) 5472
 5) firstTimestamp
 6) (integer) 1
 7) lastTimestamp
 8) (integer) 1
 9) retentionTime
10) (integer) 0
11) chunkCount
12) (integer) 1
13) chunkSize
14) (integer) 4096
15) chunkType
16) compressed
17) duplicatePolicy
18) block
19) labels
20) 1) 1) "location"
       2) "UK"
    2) 1) "type"
       2) "Mercury"
21) sourceKey
22) (nil)
23) rules
24) (empty array)
25) ignoreMaxTimeDiff
26) (integer) 0
27) ignoreMaxValDiff
28) "0"
```

##### C#

```csharp
        var labels = new List<TimeSeriesLabel>
        {
            new("location", "UK"),
            new("type", "Mercury")
        };
        long res6 = db.TS().Add(
            "thermometer:3",
            new TsAddParamsBuilder()
                .AddTimestamp(1)
                .AddValue(10.4)
                .AddLabels(labels)
                .build()
        );
        Console.WriteLine(res6); // >>> 1

        TimeSeriesInformation res7 = db.TS().Info("thermometer:3");
        Console.WriteLine(
            $"Labels: {string.Join(", ", res7.Labels!.Select(l => $"{l.Key}={l.Value}"))}"
        );
        // >>> Labels: location=UK, type=Mercury
```

##### Go

```go
	res6, err := rdb.TSAddWithArgs(
		ctx,
		"thermometer:3",
		1,
		10.4,
		&redis.TSOptions{
			Labels: map[string]string{
				"location": "UK",
				"type":     "Mercury",
			},
		},
	).Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res6) // >>> 1

	res7, err := rdb.TSInfo(ctx, "thermometer:3").Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res7["labels"])
	// >>> map[location:UK type:Mercury]
```

##### Java (Synchronous - Jedis)

```java
        Map<String, String> labels = new HashMap<>();
        labels.put("location", "UK");
        labels.put("type", "Mercury");
        
        long res6 = jedis.tsAdd("thermometer:3", 1L, 10.4,
            TSCreateParams.createParams().labels(labels));
        System.out.println(res6); // >>> 1

        TSInfo res7 = jedis.tsInfo("thermometer:3");
        System.out.println("Labels: " + res7.getLabels());
        // >>> Labels: {location=UK, type=Mercury}
```

##### JavaScript (Node.js)

```javascript
const res6 = await client.ts.add('thermometer:3', 1, 10.4, {
  LABELS: { location: 'UK', type: 'Mercury' }
});
console.log(res6); // >>> 1

const res7 = await client.ts.info('thermometer:3');
console.log(res7);
// >>> { labels: [{ name: 'location', value: 'UK' }, { name: 'type', value: 'Mercury' }], ... }
```

##### Python

```python
res6 = r.ts().create(
    "thermometer:3", 1, 10.4,
    labels={"location": "UK", "type": "Mercury"}
)
print(res6)  # >>> 1

res7 = r.ts().info("thermometer:3")
print(res7)
# >>> {'rules': [], ... 'labels': {'location': 'UK', 'type': 'Mercury'}, ...
```



## Add data points

You can add individual data points with [`TS.ADD`](https://redis.io/docs/latest/commands/ts.add),
but you can also use [`TS.MADD`](https://redis.io/docs/latest/commands/ts.madd) to add multiple data
points to one or more time series in a single command. (Note that unlike `TS.ADD`, `TS.MADD`
doesn't create any new time series if you specify keys that don't exist.) The return value
is an array containing the number of samples in each time series after the operation.
If you use the `*` character as the timestamp, Redis will record the current
Unix time, as reported by the server's clock.

Batch operations: Add multiple data points to one or more time series using TS.MADD when you need to reduce round trips to the server

**Difficulty:** Beginner

**Builds upon:** create

**Commands:** DEL, TS.CREATE, TS.ADD, TS.MADD

**Complexity:**
- DEL: O(N)
- TS.CREATE: O(1)
- TS.ADD: O(M)
- TS.MADD: O(N*M)

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python

##### Redis CLI

```
# Recreate the thermometer series so this example runs on its own.
> DEL thermometer:1 thermometer:2
(integer) 2
> TS.CREATE thermometer:1
OK
> TS.ADD thermometer:2 1 10.8
(integer) 1
> TS.MADD thermometer:1 1 9.2 thermometer:1 2 9.9 thermometer:2 2 10.3
1) (integer) 1
2) (integer) 2
3) (integer) 2
```

##### C#

```csharp
        // Recreate the thermometer series so this example runs on its own.
        db.KeyDelete(new RedisKey[] { "thermometer:1", "thermometer:2" });
        db.TS().Create("thermometer:1", new TsCreateParamsBuilder().build());
        db.TS().Add("thermometer:2", 1, 10.8);

        var sequence = new List<(string, TimeStamp, double)>
        {
            ("thermometer:1", 1, 9.2),
            ("thermometer:1", 2, 9.9),
            ("thermometer:2", 2, 10.3)
        };
        IReadOnlyList<TimeStamp> res8 = db.TS().MAdd(sequence);
        Console.WriteLine($"[{string.Join(", ", res8.Select(t => t.Value))}]");
        // >>> [1, 2, 2]
```

##### Go

```go
	// Recreate the thermometer series so this example runs on its own.
	rdb.Del(ctx, "thermometer:1", "thermometer:2")
	rdb.TSCreate(ctx, "thermometer:1")
	rdb.TSAdd(ctx, "thermometer:2", 1, 10.8)

	res1, err := rdb.TSMAdd(ctx, [][]interface{}{
		{"thermometer:1", 1, 9.2},
		{"thermometer:1", 2, 9.9},
		{"thermometer:2", 2, 10.3},
	}).Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // >>> [1 2 2]
```

##### Java (Synchronous - Jedis)

```java
        // Recreate the thermometer series so this example runs on its own.
        jedis.del("thermometer:1", "thermometer:2");
        jedis.tsCreate("thermometer:1");
        jedis.tsAdd("thermometer:2", 1L, 10.8);

        List<Long> res8 = jedis.tsMAdd(
            new AbstractMap.SimpleEntry<>("thermometer:1", new TSElement(1L, 9.2)),
            new AbstractMap.SimpleEntry<>("thermometer:1", new TSElement(2L, 9.9)),
            new AbstractMap.SimpleEntry<>("thermometer:2", new TSElement(2L, 10.3))
        );
        System.out.println(res8); // >>> [1, 2, 2]
```

##### JavaScript (Node.js)

```javascript
// Recreate the thermometer series so this example runs on its own.
await client.del(['thermometer:1', 'thermometer:2']);
await client.ts.create('thermometer:1');
await client.ts.add('thermometer:2', 1, 10.8);

const res8 = await client.ts.mAdd([
  { key: 'thermometer:1', timestamp: 1, value: 9.2 },
  { key: 'thermometer:1', timestamp: 2, value: 9.9 },
  { key: 'thermometer:2', timestamp: 2, value: 10.3 }
]);
console.log(res8); // >>> [1, 2, 2]
```

##### Python

```python
# Recreate the thermometer series so this example runs on its own.
r.delete("thermometer:1", "thermometer:2")
r.ts().create("thermometer:1")
r.ts().add("thermometer:2", 1, 10.8)

res8 = r.ts().madd([
    ("thermometer:1", 1, 9.2),
    ("thermometer:1", 2, 9.9),
    ("thermometer:2", 2, 10.3)
])
print(res8)  # >>> [1, 2, 2]
```



## Query data points

Use [`TS.GET`](https://redis.io/docs/latest/commands/ts.get) to retrieve the data point
with the highest timestamp in a time series. This returns both the timestamp and the value.

Foundational: Use TS.GET to get the latest value and timestamp

**Difficulty:** Beginner

**Builds upon:** madd

**Commands:** DEL, TS.ADD, TS.GET

**Complexity:**
- DEL: O(N)
- TS.ADD: O(M)
- TS.GET: O(1)

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python

##### Redis CLI

```
# Recreate the thermometer:2 series so this example runs on its own.
> DEL thermometer:2
(integer) 1
> TS.ADD thermometer:2 1 10.8
(integer) 1
> TS.ADD thermometer:2 2 10.3
(integer) 2
# The last recorded temperature for thermometer:2
# was 10.3 at time 2ms.
> TS.GET thermometer:2
1) (integer) 2
2) 10.3
```

##### C#

```csharp
        // Recreate the thermometer:2 series so this example runs on its own.
        db.KeyDelete("thermometer:2");
        db.TS().Add("thermometer:2", 1, 10.8);
        db.TS().Add("thermometer:2", 2, 10.3);
        // The last recorded temperature for thermometer:2
        // was 10.3 at time 2.
        TimeSeriesTuple? res9 = db.TS().Get("thermometer:2");
        Console.WriteLine($"({res9!.Time.Value}, {res9.Val})");
        // >>> (2, 10.3)
```

##### Go

```go
	// Recreate the thermometer:2 series so this example runs on its own.
	rdb.Del(ctx, "thermometer:2")
	rdb.TSAdd(ctx, "thermometer:2", 1, 10.8)
	rdb.TSAdd(ctx, "thermometer:2", 2, 10.3)
	// The last recorded temperature for thermometer:2
	// was 10.3 at time 2.
	res2, err := rdb.TSGet(ctx, "thermometer:2").Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res2)
	// >>> {2 10.3}
```

##### Java (Synchronous - Jedis)

```java
        // Recreate the thermometer:2 series so this example runs on its own.
        jedis.del("thermometer:2");
        jedis.tsAdd("thermometer:2", 1L, 10.8);
        jedis.tsAdd("thermometer:2", 2L, 10.3);
        // The last recorded temperature for thermometer:2
        // was 10.3 at time 2.
        TSElement res9 = jedis.tsGet("thermometer:2");
        System.out.println("(" + res9.getTimestamp() + ", " + res9.getValue() + ")");
        // >>> (2, 10.3)
```

##### JavaScript (Node.js)

```javascript
// Recreate the thermometer:2 series so this example runs on its own.
await client.del('thermometer:2');
await client.ts.add('thermometer:2', 1, 10.8);
await client.ts.add('thermometer:2', 2, 10.3);
// The last recorded temperature for thermometer:2
// was 10.3 at time 2.
const res9 = await client.ts.get('thermometer:2');
console.log(res9); // >>> { timestamp: 2, value: 10.3 }
```

##### Python

```python
# Recreate the thermometer:2 series so this example runs on its own.
r.delete("thermometer:2")
r.ts().add("thermometer:2", 1, 10.8)
r.ts().add("thermometer:2", 2, 10.3)
# The last recorded temperature for thermometer:2
# was 10.3 at time 2.
res9 = r.ts().get("thermometer:2")
print(res9)  # >>> (2, 10.3)
```



Use [`TS.RANGE`](https://redis.io/docs/latest/commands/ts.range) to retrieve data points
from a time series that fall within a given timestamp range. The range is inclusive,
meaning that samples whose timestamp equals the start or end of the range are included.
You can use `-` and `+` as the start and end of the range, respectively, to
indicate the minimum and maximum timestamps in the series. The response is
an array of timestamp-value pairs returned in ascending order by timestamp.
If you want the results in descending order, use [`TS.REVRANGE`](https://redis.io/docs/latest/commands/ts.revrange) with the same parameters.

Range queries: Retrieve data points within a timestamp range using TS.RANGE (ascending) or TS.REVRANGE (descending) when you need to analyze historical data

**Difficulty:** Intermediate

**Builds upon:** madd

**Commands:** TS.CREATE, TS.MADD, TS.RANGE, TS.REVRANGE

**Complexity:**
- TS.CREATE: O(1)
- TS.MADD: O(N*M)
- TS.RANGE: O(n/m+k)
- TS.REVRANGE: O(n/m+k)

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python

##### Redis CLI

```
# Add 5 data points to a time series named "rg:1".
> TS.CREATE rg:1
OK
> TS.MADD rg:1 0 18 rg:1 1 14 rg:1 2 22 rg:1 3 18 rg:1 4 24
1) (integer) 0
2) (integer) 1
3) (integer) 2
4) (integer) 3
5) (integer) 4

# Retrieve all the data points in ascending order.
> TS.RANGE rg:1 - +
1) 1) (integer) 0
   2) 18
2) 1) (integer) 1
   2) 14
3) 1) (integer) 2
   2) 22
4) 1) (integer) 3
   2) 18
5) 1) (integer) 4
   2) 24

# Retrieve data points up to time 1 (inclusive).
> TS.RANGE rg:1 - 1
1) 1) (integer) 0
   2) 18
2) 1) (integer) 1
   2) 14

# Retrieve data points from time 3 onwards.
> TS.RANGE rg:1 3 +
1) 1) (integer) 3
   2) 18
2) 1) (integer) 4
   2) 24

# Retrieve all the data points in descending order.
> TS.REVRANGE rg:1 - +
1) 1) (integer) 4
   2) 24
2) 1) (integer) 3
   2) 18
3) 1) (integer) 2
   2) 22
4) 1) (integer) 1
   2) 14
5) 1) (integer) 0
   2) 18

# Retrieve data points up to time 1 (inclusive), but
# return them in descending order.
> TS.REVRANGE rg:1 - 1
1) 1) (integer) 1
   2) 14
2) 1) (integer) 0
   2) 18
```

##### C#

```csharp
        // Add 5 data points to a time series named "rg:1".
        bool res10 = db.TS().Create(
            "rg:1",
            new TsCreateParamsBuilder().build()
        );
        Console.WriteLine(res10); // >>> True

        var sequence2 = new List<(string, TimeStamp, double)>
        {
            ("rg:1", 0, 18),
            ("rg:1", 1, 14),
            ("rg:1", 2, 22),
            ("rg:1", 3, 18),
            ("rg:1", 4, 24)
        };
        IReadOnlyList<TimeStamp> res11 = db.TS().MAdd(sequence2);
        Console.WriteLine(
            $"[{string.Join(", ", res11.Select(t => t.Value))}]"
        );
        // >>> [0, 1, 2, 3, 4]

        // Retrieve all the data points in ascending order.
        IReadOnlyList<TimeSeriesTuple> res12 = db.TS().Range("rg:1", "-", "+");
        Console.WriteLine(
            $"[{string.Join(", ", res12.Select(t => $"({t.Time.Value}, {t.Val})"))}]"
        );
        // >>> [(0, 18), (1, 14), (2, 22), (3, 18), (4, 24)]

        // Retrieve data points up to time 1 (inclusive).
        IReadOnlyList<TimeSeriesTuple> res13 = db.TS().Range("rg:1", "-", 1);
        Console.WriteLine(
            $"[{string.Join(", ", res13.Select(t => $"({t.Time.Value}, {t.Val})"))}]"
        );
        // >>> [(0, 18), (1, 14)]

        // Retrieve data points from time 3 onwards.
        IReadOnlyList<TimeSeriesTuple> res14 = db.TS().Range("rg:1", 3, "+");
        Console.WriteLine(
            $"[{string.Join(", ", res14.Select(t => $"({t.Time.Value}, {t.Val})"))}]"
        );
        // >>> [(3, 18), (4, 24)]

        // Retrieve all the data points in descending order.
        IReadOnlyList<TimeSeriesTuple> res15 = db.TS().RevRange("rg:1", "-", "+");
        Console.WriteLine(
            $"[{string.Join(", ", res15.Select(t => $"({t.Time.Value}, {t.Val})"))}]"
        );
        // >>> [(4, 24), (3, 18), (2, 22), (1, 14), (0, 18)]

        // Retrieve data points up to time 1 (inclusive), but return them
        // in descending order.
        IReadOnlyList<TimeSeriesTuple> res16 = db.TS().RevRange("rg:1", "-", 1);
        Console.WriteLine(
            $"[{string.Join(", ", res16.Select(t => $"({t.Time.Value}, {t.Val})"))}]"
        );
        // >>> [(1, 14), (0, 18)]
```

##### Go

```go
	// Add 5 data points to a time series named "rg:1".
	res1, err := rdb.TSCreate(ctx, "rg:1").Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // >>> OK

	res2, err := rdb.TSMAdd(ctx, [][]interface{}{
		{"rg:1", 0, 18},
		{"rg:1", 1, 14},
		{"rg:1", 2, 22},
		{"rg:1", 3, 18},
		{"rg:1", 4, 24},
	}).Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res2) // >>> [0 1 2 3 4]

	// Retrieve all the data points in ascending order.
	// Note: use 0 and `math.MaxInt64` instead of - and +
	// to denote the minimum and maximum possible timestamps.
	res3, err := rdb.TSRange(ctx, "rg:1", 0, math.MaxInt64).Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res3)
	// >>> [{0 18} {1 14} {2 22} {3 18} {4 24}]

	// Retrieve data points up to time 1 (inclusive).
	res4, err := rdb.TSRange(ctx, "rg:1", 0, 1).Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res4)
	// >>> [{0 18} {1 14}]

	// Retrieve data points from time 3 onwards.
	res5, err := rdb.TSRange(ctx, "rg:1", 3, math.MaxInt64).Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res5)
	// >>> [{3 18} {4 24}]

	// Retrieve all the data points in descending order.
	res6, err := rdb.TSRevRange(ctx, "rg:1", 0, math.MaxInt64).Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res6)
	// >>> [{4 24} {3 18} {2 22} {1 14} {0 18}]

	// Retrieve data points up to time 1 (inclusive), but return them
	// in descending order.
	res7, err := rdb.TSRevRange(ctx, "rg:1", 0, 1).Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res7)
	// >>> [{1 14} {0 18}]
```

##### Java (Synchronous - Jedis)

```java
        // Add 5 data points to a time series named "rg:1"
        String res10 = jedis.tsCreate("rg:1");
        System.out.println(res10); // >>> OK

        List<Long> res11 = jedis.tsMAdd(
            new AbstractMap.SimpleEntry<>("rg:1", new TSElement(0L, 18.0)),
            new AbstractMap.SimpleEntry<>("rg:1", new TSElement(1L, 14.0)),
            new AbstractMap.SimpleEntry<>("rg:1", new TSElement(2L, 22.0)),
            new AbstractMap.SimpleEntry<>("rg:1", new TSElement(3L, 18.0)),
            new AbstractMap.SimpleEntry<>("rg:1", new TSElement(4L, 24.0))
        );
        System.out.println(res11); // >>> [0, 1, 2, 3, 4]

        // Retrieve all the data points in ascending order
        List<TSElement> res12 = jedis.tsRange("rg:1", 0L, 4L);
        System.out.println(res12);
        // >>> [(0:18.0), (1:14.0), (2:22.0), (3:18.0), (4:24.0)]

        // Retrieve data points up to time 1 (inclusive)
        List<TSElement> res13 = jedis.tsRange("rg:1", 0L, 1L);
        System.out.println(res13);
        // >>> [(0:18.0), (1:14.0)]

        // Retrieve data points from time 3 onwards
        List<TSElement> res14 = jedis.tsRange("rg:1", 3L, 4L);
        System.out.println(res14);
        // >>> [(3:18.0), (4:24.0)]

        // Retrieve all the data points in descending order
        List<TSElement> res15 = jedis.tsRevRange("rg:1", 0L, 4L);
        System.out.println(res15);
        // >>> [(4:24.0), (3:18.0), (2:22.0), (1:14.0), (0:18.0)]

        // Retrieve data points up to time 1 (inclusive), in descending order
        List<TSElement> res16 = jedis.tsRevRange("rg:1", 0L, 1L);
        System.out.println(res16);
        // >>> [(1:14.0), (0:18.0)]
```

##### JavaScript (Node.js)

```javascript
// Add 5 data points to a time series named "rg:1".
const res10 = await client.ts.create('rg:1');
console.log(res10); // >>> OK

const res11 = await client.ts.mAdd([
  { key: 'rg:1', timestamp: 0, value: 18 },
  { key: 'rg:1', timestamp: 1, value: 14 },
  { key: 'rg:1', timestamp: 2, value: 22 },
  { key: 'rg:1', timestamp: 3, value: 18 },
  { key: 'rg:1', timestamp: 4, value: 24 }
]);
console.log(res11); // >>> [0, 1, 2, 3, 4]

// Retrieve all the data points in ascending order.
const res12 = await client.ts.range('rg:1', '-', '+');
console.log(res12);
// >>> [{ timestamp: 0, value: 18 }, { timestamp: 1, value: 14 }, ...]

// Retrieve data points up to time 1 (inclusive).
const res13 = await client.ts.range('rg:1', '-', 1);
console.log(res13);
// >>> [{ timestamp: 0, value: 18 }, { timestamp: 1, value: 14 }]

// Retrieve data points from time 3 onwards.
const res14 = await client.ts.range('rg:1', 3, '+');
console.log(res14);
// >>> [{ timestamp: 3, value: 18 }, { timestamp: 4, value: 24 }]

// Retrieve all the data points in descending order.
const res15 = await client.ts.revRange('rg:1', '-', '+');
console.log(res15);
// >>> [{ timestamp: 4, value: 24 }, { timestamp: 3, value: 18 }, ...]

// Retrieve data points up to time 1 (inclusive), but return them
// in descending order.
const res16 = await client.ts.revRange('rg:1', '-', 1);
console.log(res16);
// >>> [{ timestamp: 1, value: 14 }, { timestamp: 0, value: 18 }]
```

##### Python

```python
# Add 5 data points to a time series named "rg:1".
res10 = r.ts().create("rg:1")
print(res10)  # >>> True

res11 = r.ts().madd([
        ("rg:1", 0, 18),
        ("rg:1", 1, 14),
        ("rg:1", 2, 22),
        ("rg:1", 3, 18),
        ("rg:1", 4, 24),
])
print(res11)  # >>> [0, 1, 2, 3, 4]

# Retrieve all the data points in ascending order.
res12 = r.ts().range("rg:1", "-", "+")
print(res12)  # >>> [(0, 18.0), (1, 14.0), (2, 22.0), (3, 18.0), (4, 24.0)]

# Retrieve data points up to time 1 (inclusive).
res13 = r.ts().range("rg:1", "-", 1)
print(res13)  # >>> [(0, 18.0), (1, 14.0)]

# Retrieve data points from time 3 onwards.
res14 = r.ts().range("rg:1", 3, "+")
print(res14)  # >>> [(3, 18.0), (4, 24.0)]

# Retrieve all the data points in descending order.
res15 = r.ts().revrange("rg:1", "-", "+")
print(res15)  # >>> [(4, 24.0), (3, 18.0), (2, 22.0), (1, 14.0), (0, 18.0)]

# Retrieve data points up to time 1 (inclusive), but return them
# in descending order.
res16 = r.ts().revrange("rg:1", "-", 1)
print(res16)  # >>> [(1, 14.0), (0, 18.0)]
```



Both `TS.RANGE` and `TS.REVRANGE` also let you filter results. Specify
a list of timestamps to include only samples with those exact timestamps
in the results (you must still specify timestamp range parameters if you
use this option). Specify a minimum and maximum value to include only
samples within that range. The value range is inclusive and you can
use the same value for the minimum and maximum to filter for a single value.

Filtering results: Use FILTER_BY_TS and FILTER_BY_VALUE options with range queries when you need to select specific timestamps or value ranges

**Difficulty:** Intermediate

**Builds upon:** range

**Commands:** DEL, TS.CREATE, TS.MADD, TS.RANGE, TS.REVRANGE

**Complexity:**
- DEL: O(N)
- TS.CREATE: O(1)
- TS.MADD: O(N*M)
- TS.RANGE: O(n/m+k)
- TS.REVRANGE: O(n/m+k)

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python

##### Redis CLI

```
# Recreate the rg:1 series so this example runs on its own.
> DEL rg:1
(integer) 1
> TS.CREATE rg:1
OK
> TS.MADD rg:1 0 18 rg:1 1 14 rg:1 2 22 rg:1 3 18 rg:1 4 24
1) (integer) 0
2) (integer) 1
3) (integer) 2
4) (integer) 3
5) (integer) 4
> TS.RANGE rg:1 - + FILTER_BY_TS 0 2 4
1) 1) (integer) 0
   2) 18
2) 1) (integer) 2
   2) 22
3) 1) (integer) 4
   2) 24
> TS.REVRANGE rg:1 - + FILTER_BY_TS 0 2 4 FILTER_BY_VALUE 20 25
1) 1) (integer) 4
   2) 24
2) 1) (integer) 2
   2) 22
> TS.REVRANGE rg:1 - + FILTER_BY_TS 0 2 4 FILTER_BY_VALUE 22 22
1) 1) (integer) 2
   2) 22
```

##### C#

```csharp
        // Recreate the rg:1 series so this example runs on its own.
        db.KeyDelete("rg:1");
        db.TS().Create("rg:1", new TsCreateParamsBuilder().build());
        db.TS().MAdd(new List<(string, TimeStamp, double)>
        {
            ("rg:1", 0, 18),
            ("rg:1", 1, 14),
            ("rg:1", 2, 22),
            ("rg:1", 3, 18),
            ("rg:1", 4, 24)
        });

        var filterByTs = new List<TimeStamp> { 0, 2, 4 };
        IReadOnlyList<TimeSeriesTuple> res17 = db.TS().Range(
            "rg:1", "-", "+", filterByTs: filterByTs
        );
        Console.WriteLine(
            $"[{string.Join(", ", res17.Select(t => $"({t.Time.Value}, {t.Val})"))}]"
        );
        // >>> [(0, 18), (2, 22), (4, 24)]

        IReadOnlyList<TimeSeriesTuple> res18 = db.TS().RevRange(
            "rg:1", "-", "+",
            filterByTs: filterByTs,
            filterByValue: (20, 25)
        );
        Console.WriteLine(
            $"[{string.Join(", ", res18.Select(t => $"({t.Time.Value}, {t.Val})"))}]"
        );
        // >>> [(4, 24), (2, 22)]

        IReadOnlyList<TimeSeriesTuple> res19 = db.TS().RevRange(
            "rg:1", "-", "+",
            filterByTs: filterByTs,
            filterByValue: (22, 22),
            count: 1
        );
        Console.WriteLine(
            $"[{string.Join(", ", res19.Select(t => $"({t.Time.Value}, {t.Val})"))}]"
        );
        // >>> [(2, 22)]
```

##### Go

```go
	// Recreate the rg:1 series so this example runs on its own.
	rdb.Del(ctx, "rg:1")
	rdb.TSCreate(ctx, "rg:1")
	rdb.TSMAdd(ctx, [][]interface{}{
		{"rg:1", 0, 18},
		{"rg:1", 1, 14},
		{"rg:1", 2, 22},
		{"rg:1", 3, 18},
		{"rg:1", 4, 24},
	})

	res8, err := rdb.TSRangeWithArgs(
		ctx,
		"rg:1",
		0,
		math.MaxInt64,
		&redis.TSRangeOptions{
			FilterByTS: []int{0, 2, 4},
		},
	).Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res8) // >>> [{0 18} {2 22} {4 24}]

	res9, err := rdb.TSRevRangeWithArgs(
		ctx,
		"rg:1",
		0,
		math.MaxInt64,
		&redis.TSRevRangeOptions{
			FilterByTS:    []int{0, 2, 4},
			FilterByValue: []int{20, 25},
		},
	).Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res9) // >>> [{4 24} {2 22}]

	res10, err := rdb.TSRevRangeWithArgs(
		ctx,
		"rg:1",
		0,
		math.MaxInt64,
		&redis.TSRevRangeOptions{
			FilterByTS:    []int{0, 2, 4},
			FilterByValue: []int{22, 22},
		},
	).Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res10) // >>> [{2 22}]
```

##### Java (Synchronous - Jedis)

```java
        // Recreate the rg:1 series so this example runs on its own.
        jedis.del("rg:1");
        jedis.tsCreate("rg:1");
        jedis.tsMAdd(
            new AbstractMap.SimpleEntry<>("rg:1", new TSElement(0L, 18.0)),
            new AbstractMap.SimpleEntry<>("rg:1", new TSElement(1L, 14.0)),
            new AbstractMap.SimpleEntry<>("rg:1", new TSElement(2L, 22.0)),
            new AbstractMap.SimpleEntry<>("rg:1", new TSElement(3L, 18.0)),
            new AbstractMap.SimpleEntry<>("rg:1", new TSElement(4L, 24.0))
        );

        List<TSElement> res17 = jedis.tsRange("rg:1",  
            TSRangeParams.rangeParams()
                .fromTimestamp(0L)
                .toTimestamp(4L)
                .filterByTS(0L, 2L, 4L)
        );
        System.out.println(res17);
        // >>> [(0:18.0), (2:22.0), (4:24.0)]

        List<TSElement> res18 = jedis.tsRevRange("rg:1",
            TSRangeParams.rangeParams()
                .fromTimestamp(0L)
                .toTimestamp(4L)
                .filterByTS(0L, 2L, 4L)
                .filterByValues(20.0, 25.0)
        );
        System.out.println(res18);
        // >>> [(4:24.0), (2:22.0)]

        List<TSElement> res19 = jedis.tsRevRange("rg:1",
            TSRangeParams.rangeParams()
                .fromTimestamp(0L)
                .toTimestamp(4L)
                .filterByTS(0L, 2L, 4L)
                .filterByValues(22.0, 22.0)
                .count(1)
        );
        System.out.println(res19);
        // >>> [(2:22.0)]
```

##### JavaScript (Node.js)

```javascript
// Recreate the rg:1 series so this example runs on its own.
await client.del('rg:1');
await client.ts.create('rg:1');
await client.ts.mAdd([
  { key: 'rg:1', timestamp: 0, value: 18 },
  { key: 'rg:1', timestamp: 1, value: 14 },
  { key: 'rg:1', timestamp: 2, value: 22 },
  { key: 'rg:1', timestamp: 3, value: 18 },
  { key: 'rg:1', timestamp: 4, value: 24 }
]);

const res17 = await client.ts.range('rg:1', '-', '+', {
  FILTER_BY_TS: [0, 2, 4]
});
console.log(res17);
// >>> [{ timestamp: 0, value: 18 }, { timestamp: 2, value: 22 }, { timestamp: 4, value: 24 }]

const res18 = await client.ts.revRange('rg:1', '-', '+', {
  FILTER_BY_TS: [0, 2, 4],
  FILTER_BY_VALUE: { min: 20, max: 25 }
});
console.log(res18);
// >>> [{ timestamp: 4, value: 24 }, { timestamp: 2, value: 22 }]

const res19 = await client.ts.revRange('rg:1', '-', '+', {
  FILTER_BY_TS: [0, 2, 4],
  FILTER_BY_VALUE: { min: 22, max: 22 },
  COUNT: 1
});
console.log(res19);
// >>> [{ timestamp: 2, value: 22 }]
```

##### Python

```python
# Recreate the rg:1 series so this example runs on its own.
r.delete("rg:1")
r.ts().create("rg:1")
r.ts().madd([
    ("rg:1", 0, 18),
    ("rg:1", 1, 14),
    ("rg:1", 2, 22),
    ("rg:1", 3, 18),
    ("rg:1", 4, 24),
])

res17 = r.ts().range("rg:1", "-", "+", filter_by_ts=[0, 2, 4])
print(res17)  # >>> [(0, 18.0), (2, 22.0), (4, 24.0)]

res18 = r.ts().revrange(
    "rg:1", "-", "+",
    filter_by_ts=[0, 2, 4],
    filter_by_min_value=20,
    filter_by_max_value=25,
)
print(res18)  # >>> [(4, 24.0), (2, 22.0)]

res19 = r.ts().revrange(
    "rg:1", "-", "+",
    filter_by_ts=[0, 2, 4],
    filter_by_min_value=22,
    filter_by_max_value=22,
    count=1,
)
print(res19)  # >>> [(2, 22.0)]
```



### Query multiple time series

The `TS.GET`, `TS.RANGE`, and `TS.REVRANGE` commands also have
corresponding
[`TS.MGET`](https://redis.io/docs/latest/commands/ts.mget),
[`TS.MRANGE`](https://redis.io/docs/latest/commands/ts.mrange), and
[`TS.MREVRANGE`](https://redis.io/docs/latest/commands/ts.mrevrange) versions that
operate on multiple time series. `TS.MGET` returns the data point with the highest
timestamp from each time series, while `TS.MRANGE` and `TS.MREVRANGE`
return data points from a range of timestamps in each time series.

The parameters are mostly the same except that the multiple time series
commands don't take a key name as the first parameter. Instead, you
specify a filter expression to include only time series with
specific labels. (See [Creating a time series](#creating-a-time-series)
above to learn how to add labels to a time series.) The filter expressions
use a simple syntax that lets you include or exclude time series based on
the presence or value of a label. See the description in the
[`TS.MGET`](https://redis.io/docs/latest/commands/ts.mget#required-arguments) command reference
for details of the filter syntax. You can also request that
data points be returned with all their labels or with a selected subset of them.

Multi-series queries: Use TS.MGET, TS.MRANGE, and TS.MREVRANGE with label filters when you need to query multiple time series based on label criteria

**Difficulty:** Advanced

**Builds upon:** create_labels

**Commands:** TS.CREATE, TS.MADD, TS.MGET, TS.MRANGE, TS.MREVRANGE

**Complexity:**
- TS.CREATE: O(1)
- TS.MADD: O(N*M)
- TS.MGET: O(n)
- TS.MRANGE: O(n/m+k)
- TS.MREVRANGE: O(n/m+k)

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python

##### Redis CLI

```
# Create three new "rg:" time series (two in the US
# and one in the UK, with different units) and add some
# data points.
> TS.CREATE rg:2 LABELS location us unit cm
OK
> TS.CREATE rg:3 LABELS location us unit in
OK
> TS.CREATE rg:4 LABELS location uk unit mm
OK
> TS.MADD rg:2 0 1.8 rg:3 0 0.9 rg:4 0 25
1) (integer) 0
2) (integer) 0
3) (integer) 0
> TS.MADD rg:2 1 2.1 rg:3 1 0.77 rg:4 1 18
1) (integer) 1
2) (integer) 1
3) (integer) 1
> TS.MADD rg:2 2 2.3 rg:3 2 1.1 rg:4 2 21
1) (integer) 2
2) (integer) 2
3) (integer) 2
> TS.MADD rg:2 3 1.9 rg:3 3 0.81 rg:4 3 19
1) (integer) 3
2) (integer) 3
3) (integer) 3
> TS.MADD rg:2 4 1.78 rg:3 4 0.74 rg:4 4 23
1) (integer) 4
2) (integer) 4
3) (integer) 4

# Retrieve the last data point from each US time series. If
# you don't specify any labels, an empty array is returned
# for the labels.
> TS.MGET FILTER location=us
1) 1) "rg:2"
   2) (empty array)
   3) 1) (integer) 4
      2) 1.78
2) 1) "rg:3"
   2) (empty array)
   3) 1) (integer) 4
      2) 7.4E-1

# Retrieve the same data points, but include the `unit`
# label in the results.
> TS.MGET SELECTED_LABELS unit FILTER location=us
1) 1) "rg:2"
   2) 1) 1) "unit"
         2) "cm"
   3) 1) (integer) 4
      2) 1.78
2) 1) "rg:3"
   2) 1) 1) "unit"
         2) "in"
   3) 1) (integer) 4
      2) 7.4E-1

# Retrieve data points up to time 2 (inclusive) from all
# time series that use millimeters as the unit. Include all
# labels in the results.
> TS.MRANGE - 2 WITHLABELS FILTER unit=mm
1) 1) "rg:4"
   2) 1) 1) "location"
         2) "uk"
      2) 1) "unit"
         2) "mm"
   3) 1) 1) (integer) 0
         2) 25
      2) 1) (integer) 1
         2) 18
      3) 1) (integer) 2
         2) 21

# Retrieve data points from time 1 to time 3 (inclusive) from
# all time series that use centimeters or millimeters as the unit,
# but only return the `location` label. Return the results
# in descending order of timestamp.
> TS.MREVRANGE 1 3 SELECTED_LABELS location FILTER unit=(cm,mm)
1) 1) "rg:2"
   2) 1) 1) "location"
         2) "us"
   3) 1) 1) (integer) 3
         2) 1.9
      2) 1) (integer) 2
         2) 2.3
      3) 1) (integer) 1
         2) 2.1
2) 1) "rg:4"
   2) 1) 1) "location"
         2) "uk"
   3) 1) 1) (integer) 3
         2) 19
      2) 1) (integer) 2
         2) 21
      3) 1) (integer) 1
         2) 18
```

##### C#

```csharp
        // Create three new "rg:" time series (two in the US
        // and one in the UK, with different units) and add some
        // data points.
        var labels2 = new List<TimeSeriesLabel>
        {
            new("location", "us"),
            new("unit", "cm")
        };
        bool res20 = db.TS().Create(
            "rg:2",
            new TsCreateParamsBuilder()
                .AddLabels(labels2)
                .build()
        );
        Console.WriteLine(res20); // >>> True

        var labels3 = new List<TimeSeriesLabel>
        {
            new("location", "us"),
            new("unit", "in")
        };

        bool res21 = db.TS().Create(
            "rg:3",
            new TsCreateParamsBuilder()
                .AddLabels(labels3)
                .build()
        );
        Console.WriteLine(res21); // >>> True

        var labels4 = new List<TimeSeriesLabel>
        {
            new("location", "uk"),
            new("unit", "mm")
        };
        bool res22 = db.TS().Create(
            "rg:4",
            new TsCreateParamsBuilder()
                .AddLabels(labels4)
                .build()
        );
        Console.WriteLine(res22); // >>> True

        var sequence3 = new List<(string, TimeStamp, double)>
        {
            ("rg:2", 0, 1.8),
            ("rg:3", 0, 0.9),
            ("rg:4", 0, 25)
        };
        IReadOnlyList<TimeStamp> res23 = db.TS().MAdd(sequence3);
        Console.WriteLine(
            $"[{string.Join(", ", res23.Select(t => t.Value))}]"
        );
        // >>> [0, 0, 0]

        var sequence4 = new List<(string, TimeStamp, double)>
        {
            ("rg:2", 1, 2.1),
            ("rg:3", 1, 0.77),
            ("rg:4", 1, 18)
        };

        IReadOnlyList<TimeStamp> res24 = db.TS().MAdd(sequence4);
        Console.WriteLine(
            $"[{string.Join(", ", res24.Select(t => t.Value))}]"
        );
        // >>> [1, 1, 1]

        var sequence5 = new List<(string, TimeStamp, double)>
        {
            ("rg:2", 2, 2.3),
            ("rg:3", 2, 1.1),
            ("rg:4", 2, 21)
        };

        IReadOnlyList<TimeStamp> res25 = db.TS().MAdd(sequence5);
        Console.WriteLine(
            $"[{string.Join(", ", res25.Select(t => t.Value))}]"
        );
        // >>> [2, 2, 2]

        var sequence6 = new List<(string, TimeStamp, double)>
        {
            ("rg:2", 3, 1.9),
            ("rg:3", 3, 0.81),
            ("rg:4", 3, 19)
        };

        IReadOnlyList<TimeStamp> res26 = db.TS().MAdd(sequence6);
        Console.WriteLine(
            $"[{string.Join(", ", res26.Select(t => t.Value))}]"
        );
        // >>> [3, 3, 3]

        var sequence7 = new List<(string, TimeStamp, double)>
        {
            ("rg:2", 4, 1.78),
            ("rg:3", 4, 0.74),
            ("rg:4", 4, 23)
        };
        IReadOnlyList<TimeStamp> res27 = db.TS().MAdd(sequence7);
        Console.WriteLine(
            $"[{string.Join(", ", res27.Select(t => t.Value))}]"
        );
        // >>> [4, 4, 4]

        // Retrieve the last data point from each US time series. If
        // you don't specify any labels, an empty array is returned
        // for the labels.
        var filters = new List<string> { "location=us" };
        var res28 = db.TS().MGet(filters);
        Console.WriteLine(res28.Count); // >>> 2

        foreach (var (key, labelsResult, value) in res28)
        {
            Console.WriteLine($"{key}: ({value.Time.Value}, {value.Val})");
        }
        // >>> rg:2: (4, 1.78)
        // >>> rg:3: (4, 0.74)

        // Retrieve the same data points, but include the `unit`
        // label in the results.
        var selectUnitLabel = new List<string> { "unit" };

        var res29 = db.TS().MGet(
            filters,
            selectedLabels: selectUnitLabel
        );
        Console.WriteLine(res29.Count); // >>> 2

        foreach (var (key, labelsResult, value) in res29)
        {
            var unitLabel = labelsResult.FirstOrDefault(l => l.Key == "unit");
            Console.WriteLine($"{key} (unit: {unitLabel?.Value}): ({value.Time.Value}, {value.Val})");
        }
        // >>> rg:2 (unit: cm): (4, 1.78)
        // >>> rg:3 (unit: in): (4, 0.74)

        // Retrieve data points up to time 2 (inclusive) from all
        // time series that use millimeters as the unit. Include all
        // labels in the results.
        var mmFilters = new List<string> { "unit=mm" };

        IReadOnlyList<
            (string, IReadOnlyList<TimeSeriesLabel>, IReadOnlyList<TimeSeriesTuple>)
        > res30 = db.TS().MRange(
            "-", 2, mmFilters, withLabels: true
        );
        Console.WriteLine(res30.Count); // >>> 1

        foreach (var (key, labelsResult, values) in res30)
        {
            Console.WriteLine($"{key}:");
            Console.WriteLine($"  Labels: ({string.Join(", ", labelsResult.Select(l => $"{l.Key}={l.Value}"))})");
            Console.WriteLine($"  Values: [{string.Join(", ", values.Select(t => $"({t.Time.Value}, {t.Val})"))}]");
        }
        // >>> rg:4:
        // >>>   Labels:location=uk,unit=mm
        // >>>   Values: [(1, 23), (2, 21), (3, 19)]

        // Retrieve data points from time 1 to time 3 (inclusive) from
        // all time series that use centimeters or millimeters as the unit,
        // but only return the `location` label. Return the results
        // in descending order of timestamp.
        var cmMmFilters = new List<string> { "unit=(cm,mm)" };
        var locationLabels = new List<string> { "location" };
        IReadOnlyList<
            (string, IReadOnlyList<TimeSeriesLabel>, IReadOnlyList<TimeSeriesTuple>)
        > res31 = db.TS().MRevRange(
            1, 3, cmMmFilters, selectLabels: locationLabels
        );
        Console.WriteLine(res31.Count); // >>> 2

        foreach (var (key, labelsResult, values) in res31)
        {
            var locationLabel = labelsResult.FirstOrDefault(l => l.Key == "location");
            Console.WriteLine($"{key} (location: {locationLabel?.Value})");
            Console.WriteLine($"  Values: [{string.Join(", ", values.Select(t => $"({t.Time.Value}, {t.Val})"))}]");
        }
        // >>> rg:4 (location: uk)
        // >>>   Values: [(3, 19), (2, 21), (1, 23)]
        // >>> rg:2 (location: us)
        // >>>   Values: [(3, 2.3), (2, 2.1), (1, 1.8)]
```

##### Go

```go
	// Create three new "rg:" time series (two in the US
	// and one in the UK, with different units) and add some
	// data points.
	res20, err := rdb.TSCreateWithArgs(ctx, "rg:2", &redis.TSOptions{
		Labels: map[string]string{"location": "us", "unit": "cm"},
	}).Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res20) // >>> OK

	res21, err := rdb.TSCreateWithArgs(ctx, "rg:3", &redis.TSOptions{
		Labels: map[string]string{"location": "us", "unit": "in"},
	}).Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res21) // >>> OK

	res22, err := rdb.TSCreateWithArgs(ctx, "rg:4", &redis.TSOptions{
		Labels: map[string]string{"location": "uk", "unit": "mm"},
	}).Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res22) // >>> OK

	res23, err := rdb.TSMAdd(ctx, [][]interface{}{
		{"rg:2", 0, 1.8},
		{"rg:3", 0, 0.9},
		{"rg:4", 0, 25},
	}).Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res23) // >>> [0 0 0]

	res24, err := rdb.TSMAdd(ctx, [][]interface{}{
		{"rg:2", 1, 2.1},
		{"rg:3", 1, 0.77},
		{"rg:4", 1, 18},
	}).Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res24) // >>> [1 1 1]

	res25, err := rdb.TSMAdd(ctx, [][]interface{}{
		{"rg:2", 2, 2.3},
		{"rg:3", 2, 1.1},
		{"rg:4", 2, 21},
	}).Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res25) // >>> [2 2 2]

	res26, err := rdb.TSMAdd(ctx, [][]interface{}{
		{"rg:2", 3, 1.9},
		{"rg:3", 3, 0.81},
		{"rg:4", 3, 19},
	}).Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res26) // >>> [3 3 3]

	res27, err := rdb.TSMAdd(ctx, [][]interface{}{
		{"rg:2", 4, 1.78},
		{"rg:3", 4, 0.74},
		{"rg:4", 4, 23},
	}).Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res27) // >>> [4 4 4]

	// Retrieve the last data point from each US time series.
	res28, err := rdb.TSMGet(ctx, []string{"location=us"}).Result()
	if err != nil {
		panic(err)
	}

	res28Keys := slices.Collect(maps.Keys(res28))
	sort.Strings(res28Keys)

	for _, k := range res28Keys {
		labels := res28[k][0].(map[interface{}]interface{})

		labelKeys := make([]string, 0, len(labels))

		for lk := range labels {
			labelKeys = append(labelKeys, lk.(string))
		}

		sort.Strings(labelKeys)

		fmt.Printf("%v:\n", k)

		for _, lk := range labelKeys {
			fmt.Printf("  %v: %v\n", lk, labels[lk])
		}

		fmt.Printf("  %v\n", res28[k][1])
	}
	// >>> rg:2:
	// >>>   {4 1.78}
	// >>> rg:3:
	// >>>   {4 0.74}

	// Retrieve the same data points, but include the `unit`
	// label in the results.
	res29, err := rdb.TSMGetWithArgs(
		ctx,
		[]string{"location=us"},
		&redis.TSMGetOptions{
			SelectedLabels: []interface{}{"unit"},
		},
	).Result()
	if err != nil {
		panic(err)
	}

	res29Keys := slices.Collect(maps.Keys(res29))
	sort.Strings(res29Keys)

	for _, k := range res29Keys {
		labels := res29[k][0].(map[interface{}]interface{})

		labelKeys := make([]string, 0, len(labels))

		for lk := range labels {
			labelKeys = append(labelKeys, lk.(string))
		}

		sort.Strings(labelKeys)

		fmt.Printf("%v:\n", k)

		for _, lk := range labelKeys {
			fmt.Printf("  %v: %v\n", lk, labels[lk])
		}

		fmt.Printf("  %v\n", res29[k][1])
	}

	// >>> rg:2:
	// >>>   unit: cm
	// >>>   [4 1.78]
	// >>> rg:3:
	// >>>   unit: in
	// >>>   [4 0.74]

	// Retrieve data points up to time 2 (inclusive) from all
	// time series that use millimeters as the unit. Include all
	// labels in the results.
	// Note that the `aggregators` field is empty if you don't
	// specify any aggregators.
	res30, err := rdb.TSMRangeWithArgs(
		ctx,
		0,
		2,
		[]string{"unit=mm"},
		&redis.TSMRangeOptions{
			WithLabels: true,
		},
	).Result()
	if err != nil {
		panic(err)
	}

	res30Keys := slices.Collect(maps.Keys(res30))
	sort.Strings(res30Keys)

	for _, k := range res30Keys {
		labels := res30[k][0].(map[interface{}]interface{})
		labelKeys := make([]string, 0, len(labels))

		for lk := range labels {
			labelKeys = append(labelKeys, lk.(string))
		}

		sort.Strings(labelKeys)

		fmt.Printf("%v:\n", k)

		for _, lk := range labelKeys {
			fmt.Printf("  %v: %v\n", lk, labels[lk])
		}

		fmt.Printf("  Aggregators: %v\n", res30[k][1])
		fmt.Printf("  %v\n", res30[k][2])
	}
	// >>> rg:4:
	// >>>   location: uk
	// >>>   unit: mm
	// >>>   Aggregators: map[aggregators:[]]
	// >>>   [{0 25} {1 18} {2 21}]

	// Retrieve data points from time 1 to time 3 (inclusive) from
	// all time series that use centimeters or millimeters as the unit,
	// but only return the `location` label. Return the results
	// in descending order of timestamp.
	res31, err := rdb.TSMRevRangeWithArgs(
		ctx,
		1,
		3,
		[]string{"unit=(cm,mm)"},
		&redis.TSMRevRangeOptions{
			SelectedLabels: []interface{}{"location"},
		},
	).Result()
	if err != nil {
		panic(err)
	}

	res31Keys := slices.Collect(maps.Keys(res31))
	sort.Strings(res31Keys)

	for _, k := range res31Keys {
		labels := res31[k][0].(map[interface{}]interface{})
		labelKeys := make([]string, 0, len(labels))

		for lk := range labels {
			labelKeys = append(labelKeys, lk.(string))
		}

		sort.Strings(labelKeys)

		fmt.Printf("%v:\n", k)

		for _, lk := range labelKeys {
			fmt.Printf("  %v: %v\n", lk, labels[lk])
		}

		fmt.Printf("  Aggregators: %v\n", res31[k][1])
		fmt.Printf("  %v\n", res31[k][2])
	}
	// >>> rg:2:
	// >>>   location: us
	// >>>   Aggregators: map[aggregators:[]]
	// >>>   [{3 1.9} {2 2.3} {1 2.1}]
	// >>> rg:4:
	// >>>   location: uk
	// >>>   Aggregators: map[aggregators:[]]
	// >>>   [{3 19} {2 21} {1 18}]
```

##### Java (Synchronous - Jedis)

```java
        // Create three new "rg:" time series (two in the US
        // and one in the UK, with different units) and add some
        // data points.
        Map<String, String> usLabels1 = new HashMap<>();
        usLabels1.put("location", "us");
        usLabels1.put("unit", "cm");
        
        Map<String, String> usLabels2 = new HashMap<>();
        usLabels2.put("location", "us");
        usLabels2.put("unit", "in");
        
        Map<String, String> ukLabels = new HashMap<>();
        ukLabels.put("location", "uk");
        ukLabels.put("unit", "mm");

        String res20 = jedis.tsCreate("rg:2",
            TSCreateParams.createParams().labels(usLabels1));
        System.out.println(res20); // >>> OK

        String res21 = jedis.tsCreate("rg:3",
            TSCreateParams.createParams().labels(usLabels2));
        System.out.println(res21); // >>> OK

        String res22 = jedis.tsCreate("rg:4",
            TSCreateParams.createParams().labels(ukLabels));
        System.out.println(res22); // >>> OK

        List<Long> res23 = jedis.tsMAdd(
            new AbstractMap.SimpleEntry<>("rg:2", new TSElement(0L, 1.8)),
            new AbstractMap.SimpleEntry<>("rg:3", new TSElement(0L, 0.9)),
            new AbstractMap.SimpleEntry<>("rg:4", new TSElement(0L, 25.0))
        );
        System.out.println(res23); // >>> [0, 0, 0]

        List<Long> res24 = jedis.tsMAdd(
            new AbstractMap.SimpleEntry<>("rg:2", new TSElement(1L, 2.1)),
            new AbstractMap.SimpleEntry<>("rg:3", new TSElement(1L, 0.77)),
            new AbstractMap.SimpleEntry<>("rg:4", new TSElement(1L, 18.0))
        );
        System.out.println(res24); // >>> [1, 1, 1]

        List<Long> res25 = jedis.tsMAdd(
            new AbstractMap.SimpleEntry<>("rg:2", new TSElement(2L, 2.3)),
            new AbstractMap.SimpleEntry<>("rg:3", new TSElement(2L, 1.1)),
            new AbstractMap.SimpleEntry<>("rg:4", new TSElement(2L, 21.0))
        );
        System.out.println(res25); // >>> [2, 2, 2]
        
        List<Long> res26 = jedis.tsMAdd(
            new AbstractMap.SimpleEntry<>("rg:2", new TSElement(3L, 1.9)),
            new AbstractMap.SimpleEntry<>("rg:3", new TSElement(3L, 0.81)),
            new AbstractMap.SimpleEntry<>("rg:4", new TSElement(3L, 19.0))
        );
        System.out.println(res26); // >>> [3, 3, 3]

        List<Long> res27 = jedis.tsMAdd(
            new AbstractMap.SimpleEntry<>("rg:2", new TSElement(4L, 1.78)),
            new AbstractMap.SimpleEntry<>("rg:3", new TSElement(4L, 0.74)),
            new AbstractMap.SimpleEntry<>("rg:4", new TSElement(4L, 23.0))
        );
        System.out.println(res27); // >>> [4, 4, 4]

        // Retrieve the last data point from each US time series.
        Map<String, TSMGetElement> res28 = jedis.tsMGet(
            TSMGetParams.multiGetParams().latest(),
             "location=us"
        );
        System.out.println(res28);
        // >>> {rg:2=TSMGetElement{key=rg:2, labels={}, element=(4:1.78)}...

        // Retrieve the same data points, but include the `unit`
        // label in the results.
        Map<String, TSMGetElement> res29 = jedis.tsMGet(
            TSMGetParams.multiGetParams().selectedLabels("unit"), 
            "location=us"
        );
        System.out.println(res29);
        // >>> {rg:2=TSMGetElement{key=rg:2, labels={unit=cm}, element=(4:1.78)}...

        // Retrieve data points up to time 2 (inclusive) from all
        // time series that use millimeters as the unit. Include all
        // labels in the results.
        Map<String, TSMRangeElements> res30 = jedis.tsMRange(
            TSMRangeParams.multiRangeParams(0L, 2L)
                .withLabels()
                .filter("unit=mm")
        );
        System.out.println(res30);
        // >>> {rg:4=TSMRangeElements{key=rg:4, labels={location=uk, unit=mm}, value=[(0:25.0), (1:18.0), (2:21.0)]}}

        // Retrieve data points from time 1 to time 3 (inclusive) from
        // all time series that use centimeters or millimeters as the unit,
        // but only return the `location` label. Return the results
        // in descending order of timestamp.
        Map<String, TSMRangeElements> res31 = jedis.tsMRevRange(
            TSMRangeParams.multiRangeParams(1L, 3L)
                .selectedLabels("location")
                .filter("unit=(cm,mm)")
        );
        System.out.println(res31);
        // >>> {rg:2=TSMRangeElements{key=rg:2, labels={location=us, unit=cm}, value=[(1:2.1)...
```

##### JavaScript (Node.js)

```javascript
// Create three new "rg:" time series (two in the US
// and one in the UK, with different units) and add some
// data points.
const res20 = await client.ts.create('rg:2', {
  LABELS: { location: 'us', unit: 'cm' }
});
console.log(res20); // >>> OK

const res21 = await client.ts.create('rg:3', {
  LABELS: { location: 'us', unit: 'in' }
});
console.log(res21); // >>> OK

const res22 = await client.ts.create('rg:4', {
  LABELS: { location: 'uk', unit: 'mm' }
});
console.log(res22); // >>> OK

const res23 = await client.ts.mAdd([
  { key: 'rg:2', timestamp: 0, value: 1.8 },
  { key: 'rg:3', timestamp: 0, value: 0.9 },
  { key: 'rg:4', timestamp: 0, value: 25 }
]);
console.log(res23); // >>> [0, 0, 0]

const res24 = await client.ts.mAdd([
  { key: 'rg:2', timestamp: 1, value: 2.1 },
  { key: 'rg:3', timestamp: 1, value: 0.77 },
  { key: 'rg:4', timestamp: 1, value: 18 }
]);
console.log(res24); // >>> [1, 1, 1]

const res25 = await client.ts.mAdd([
  { key: 'rg:2', timestamp: 2, value: 2.3 },
  { key: 'rg:3', timestamp: 2, value: 1.1 },
  { key: 'rg:4', timestamp: 2, value: 21 }
]);
console.log(res25); // >>> [2, 2, 2]

const res26 = await client.ts.mAdd([
  { key: 'rg:2', timestamp: 3, value: 1.9 },
  { key: 'rg:3', timestamp: 3, value: 0.81 },
  { key: 'rg:4', timestamp: 3, value: 19 }
]);
console.log(res26); // >>> [3, 3, 3]

const res27 = await client.ts.mAdd([
  { key: 'rg:2', timestamp: 4, value: 1.78 },
  { key: 'rg:3', timestamp: 4, value: 0.74 },
  { key: 'rg:4', timestamp: 4, value: 23 }
]);
console.log(res27); // >>> [4, 4, 4]

// Retrieve the last data point from each US time series.
const res28 = await client.ts.mGet(['location=us']);
console.log(res28);
// >>> { "rg:2": { sample: { timestamp: 4, value: 1.78 } }, "rg:3": { sample: { timestamp: 4, value: 0.74 } } }

// Retrieve the same data points, but include the `unit`
// label in the results.
const res29 = await client.ts.mGetSelectedLabels(['location=us'], ['unit']);
console.log(res29);
// >>> { "rg:2": { labels: { unit: 'cm' }, sample: { timestamp: 4, value: 1.78 } }, "rg:3": { labels: { unit: 'in' }, sample: { timestamp: 4, value: 0.74 } } }

// Retrieve data points up to time 2 (inclusive) from all
// time series that use millimeters as the unit. Include all
// labels in the results.
const res30 = await client.ts.mRangeWithLabels('-', 2, 'unit=mm');
console.log(res30);
// >>> { "rg:4": { labels: { location: 'uk', unit: 'mm' }, samples: [
//   { timestamp: 0, value: 25 },
//   { timestamp: 1, value: 18 },
//   { timestamp: 2, value: 21 }
// ] } }

// Retrieve data points from time 1 to time 3 (inclusive) from
// all time series that use centimeters or millimeters as the unit,
// but only return the `location` label. Return the results
// in descending order of timestamp.
const res31 = await client.ts.mRevRangeSelectedLabels(
  1, 3,
  ['location'],
  ['unit=(cm,mm)']
);
console.log(res31);
// >>> { "rg:2": { labels: { location: 'us' }, samples: [
//   { timestamp: 3, value: 1.9 },
//   { timestamp: 2, value: 2.3 },
//   { timestamp: 1, value: 2.1 }
// ] }, "rg:4": { labels: { location: 'uk' }, samples: [
//   { timestamp: 3, value: 19 },
//   { timestamp: 2, value: 21 },
//   { timestamp: 1, value: 18 }
// ] } }
```

##### Python

```python
# Create three new "rg:" time series (two in the US
# and one in the UK, with different units) and add some
# data points.
res20 = r.ts().create(
    "rg:2",
    labels={"location": "us", "unit": "cm"},
)
print(res20)  # >>> True

res21 = r.ts().create(
    "rg:3",
    labels={"location": "us", "unit": "in"},
)
print(res21)  # >>> True

res22 = r.ts().create(
    "rg:4",
    labels={"location": "uk", "unit": "mm"},
)
print(res22)  # >>> True

res23 = r.ts().madd([
        ("rg:2", 0, 1.8),
        ("rg:3", 0, 0.9),
        ("rg:4", 0, 25),
])
print(res23)  # >>> [0, 0, 0]

res24 = r.ts().madd([
        ("rg:2", 1, 2.1),
        ("rg:3", 1, 0.77),
        ("rg:4", 1, 18),
])
print(res24)  # >>> [1, 1, 1]

res25 = r.ts().madd([
        ("rg:2", 2, 2.3),
        ("rg:3", 2, 1.1),
        ("rg:4", 2, 21),
])
print(res25)  # >>> [2, 2, 2]

res26 = r.ts().madd([
        ("rg:2", 3, 1.9),
        ("rg:3", 3, 0.81),
        ("rg:4", 3, 19),
])
print(res26)  # >>> [3, 3, 3]

res27 = r.ts().madd([
        ("rg:2", 4, 1.78),
        ("rg:3", 4, 0.74),
        ("rg:4", 4, 23),
])
print(res27)  # >>> [4, 4, 4]

# Retrieve the last data point from each US time series. If
# you don't specify any labels, an empty array is returned
# for the labels.
res28 = r.ts().mget(["location=us"])
print(res28)  # >>> [{'rg:2': [{}, 4, 1.78]}, {'rg:3': [{}, 4, 0.74]}]

# Retrieve the same data points, but include the `unit`
# label in the results.
res29 = r.ts().mget(["location=us"], select_labels=["unit"])
print(res29)
# >>> [{'rg:2': [{'unit': 'cm'}, 4, 1.78]}, {'rg:3': [{'unit': 'in'}, 4, 0.74]}]

# Retrieve data points up to time 2 (inclusive) from all
# time series that use millimeters as the unit. Include all
# labels in the results.
res30 = r.ts().mrange(
    "-", 2, filters=["unit=mm"], with_labels=True
)
print(res30)
# >>> [{'rg:4': [{'location': 'uk', 'unit': 'mm'}, [(0, 25.4),...

# Retrieve data points from time 1 to time 3 (inclusive) from
# all time series that use centimeters or millimeters as the unit,
# but only return the `location` label. Return the results
# in descending order of timestamp.
res31 = r.ts().mrevrange(
    1, 3, filters=["unit=(cm,mm)"], select_labels=["location"]
)
print(res31)
# >>> [[{'location': 'uk'}, (3, 19.0), (2, 21.0), (1, 18.0)],...
```



## Aggregation

A time series can become large if samples are added very frequently. Instead
of dealing with individual samples, it is sometimes useful to split the full
time range of the series into equal-sized "buckets" and represent each
bucket by an aggregate value, such as the average or maximum value.

For example, if you expect to collect more than one billion data points in a day, you could aggregate the data using buckets of one minute. Since each bucket is represented by a single value, this reduces 
the dataset size to 1,440 data points (24 hours x 60 minutes = 1,440 minutes).

The range query commands let you specify one or more aggregators and bucket size.
The available aggregators are:

| aggregator   | Description                                                     |
| ------------ | --------------------------------------------------------------- |
| `avg`        | Arithmetic mean of all non-NaN values                           |
| `sum`        | Sum of all non-NaN values                                       |
| `min`        | Minimum non-NaN value                                           |
| `max`        | Maximum non-NaN value                                           |
| `range`      | Difference between the maximum and the minimum non-NaN values   |
| `count`      | Number of non-NaN values                                        |
| `countNaN`   | Number of NaN values (since Redis 8.6)                          |
| `countAll`   | Number of values, including NaN and non-NaN (since Redis 8.6)   |
| `first`      | The non-NaN value with the lowest timestamp in the bucket       |
| `last`       | The non-NaN value with the highest timestamp in the bucket      |
| `std.p`      | Population standard deviation of the non-NaN values             |
| `std.s`      | Sample standard deviation of the non-NaN values                 |
| `var.p`      | Population variance of the non-NaN values                       |
| `var.s`      | Sample variance of the non-NaN values                           |
| `twa`        | Time-weighted average over the bucket's timeframe (ignores NaN values) (since RedisTimeSeries 1.8) |

For example, the example below shows an aggregation with the `avg` aggregator over all
five data points in the `rg:2` time series. The bucket size is 2ms, so there are three
aggregated values with only one value used to calculate the average for the last bucket.

Aggregation: Use AGGREGATION option with range queries to compute statistics such as avg, sum, min, and max over time buckets when you need to reduce large datasets

**Difficulty:** Intermediate

**Builds upon:** madd

**Commands:** DEL, TS.CREATE, TS.MADD, TS.RANGE

**Complexity:**
- DEL: O(N)
- TS.CREATE: O(1)
- TS.MADD: O(N*M)
- TS.RANGE: O(n/m+k)

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python

##### Redis CLI

```
# Recreate the rg:2 series so this example runs on its own.
> DEL rg:2
(integer) 1
> TS.CREATE rg:2
OK
> TS.MADD rg:2 0 1.8 rg:2 1 2.1 rg:2 2 2.3 rg:2 3 1.9 rg:2 4 1.78
1) (integer) 0
2) (integer) 1
3) (integer) 2
4) (integer) 3
5) (integer) 4
> TS.RANGE rg:2 - + AGGREGATION avg 2
1) 1) (integer) 0
   2) 1.9500000000000002
2) 1) (integer) 2
   2) 2.0999999999999996
3) 1) (integer) 4
   2) 1.78
```

##### C#

```csharp
        // Recreate the rg:2 series so this example runs on its own.
        db.KeyDelete("rg:2");
        db.TS().Create("rg:2", new TsCreateParamsBuilder().build());
        db.TS().MAdd(new List<(string, TimeStamp, double)>
        {
            ("rg:2", 0, 1.8),
            ("rg:2", 1, 2.1),
            ("rg:2", 2, 2.3),
            ("rg:2", 3, 1.9),
            ("rg:2", 4, 1.78)
        });

        IReadOnlyList<TimeSeriesTuple> res32 = db.TS().Range(
            "rg:2", "-", "+",
            aggregation: TsAggregation.Avg,
            timeBucket: 2
        );
        Console.WriteLine($"[{string.Join(", ", res32.Select(t => $"({t.Time.Value}, {t.Val})"))}]");
        // >>> [(0, 1.95), (2, 2.1), (4, 1.78)]
```

##### Go

```go
	// Recreate the rg:2 series so this example runs on its own.
	rdb.Del(ctx, "rg:2")
	rdb.TSCreate(ctx, "rg:2")
	rdb.TSMAdd(ctx, [][]interface{}{
		{"rg:2", 0, 1.8},
		{"rg:2", 1, 2.1},
		{"rg:2", 2, 2.3},
		{"rg:2", 3, 1.9},
		{"rg:2", 4, 1.78},
	})

	res32, err := rdb.TSRangeWithArgs(
		ctx,
		"rg:2",
		0,
		math.MaxInt64,
		&redis.TSRangeOptions{
			Aggregator:     redis.Avg,
			BucketDuration: 2,
		},
	).Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res32)
	// >>> [{0 1.9500000000000002} {2 2.0999999999999996} {4 1.78}]
```

##### Java (Synchronous - Jedis)

```java
        // Recreate the rg:2 series so this example runs on its own.
        jedis.del("rg:2");
        jedis.tsCreate("rg:2");
        jedis.tsMAdd(
            new AbstractMap.SimpleEntry<>("rg:2", new TSElement(0L, 1.8)),
            new AbstractMap.SimpleEntry<>("rg:2", new TSElement(1L, 2.1)),
            new AbstractMap.SimpleEntry<>("rg:2", new TSElement(2L, 2.3)),
            new AbstractMap.SimpleEntry<>("rg:2", new TSElement(3L, 1.9)),
            new AbstractMap.SimpleEntry<>("rg:2", new TSElement(4L, 1.78))
        );

        List<TSElement> res32 = jedis.tsRange("rg:2",
            TSRangeParams.rangeParams()
                .fromTimestamp(0L)
                .toTimestamp(4L)
                .aggregation(AggregationType.AVG, 2)
        );
        System.out.println(res32);
        // >>> [(0:1.9500000000000002), (2:2.0999999999999996), (4:1.78)]
```

##### JavaScript (Node.js)

```javascript
// Recreate the rg:2 series so this example runs on its own.
await client.del('rg:2');
await client.ts.create('rg:2');
await client.ts.mAdd([
  { key: 'rg:2', timestamp: 0, value: 1.8 },
  { key: 'rg:2', timestamp: 1, value: 2.1 },
  { key: 'rg:2', timestamp: 2, value: 2.3 },
  { key: 'rg:2', timestamp: 3, value: 1.9 },
  { key: 'rg:2', timestamp: 4, value: 1.78 }
]);

const res32 = await client.ts.range('rg:2', '-', '+', {
  AGGREGATION: {
    type: TIME_SERIES_AGGREGATION_TYPE.AVG,
    timeBucket: 2
  }
});
console.log(res32);
// >>> [{ timestamp: 0, value: 1.9500000000000002 },{ timestamp: 2, value: 2.0999999999999996 }, { timestamp: 4, value: 1.78 }]
```

##### Python

```python
# Recreate the rg:2 series so this example runs on its own.
r.delete("rg:2")
r.ts().create("rg:2")
r.ts().madd([
    ("rg:2", 0, 1.8),
    ("rg:2", 1, 2.1),
    ("rg:2", 2, 2.3),
    ("rg:2", 3, 1.9),
    ("rg:2", 4, 1.78),
])

res32 = r.ts().range(
    "rg:2", "-", "+",
    aggregation_type="avg",
    bucket_size_msec=2
)
print(res32)
# >>> [(0, 1.9500000000000002), (2, 2.0999999999999996), (4, 1.78)]
```



To use multiple aggregators in a single query, separate the aggregators with comma characters as in the following example.

```bash
TS.RANGE rg:2 - + AGGREGATION min,avg,max 2
```

<note><b>NaN Handling (Redis 8.6+):</b> Starting from Redis 8.6, all existing aggregators ignore NaN values when computing results. For example, if a bucket contains values [1.0, NaN, 3.0], the `avg` aggregator will return 2.0 (average of 1.0 and 3.0), and the `count` aggregator will return 2. Use the new `countNaN` and `countAll` aggregators to count NaN values and total values respectively.</note>

### Bucket alignment

The sequence of buckets has a reference timestamp, which is the timestamp where
the first bucket in the sequence starts. By default, the reference timestamp is zero.
For example, the following commands create a time series and apply a `min` aggregator
with a bucket size of 25 milliseconds at the default zero alignment.

Bucket alignment: Use AGGREGATION with default zero alignment to group data into fixed-size time buckets when you need consistent time-based aggregations

**Difficulty:** Intermediate

**Builds upon:** agg

**Commands:** TS.CREATE, TS.MADD, TS.RANGE

**Complexity:**
- TS.CREATE: O(1)
- TS.MADD: O(N*M)
- TS.RANGE: O(n/m+k)

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python

##### Redis CLI

```
> TS.CREATE sensor3
OK
> TS.MADD sensor3 10 1000 sensor3 20 2000 sensor3 30 3000 sensor3 40 4000 sensor3 50 5000 sensor3 60 6000 sensor3 70 7000
1) (integer) 10
2) (integer) 20
3) (integer) 30
4) (integer) 40
5) (integer) 50
6) (integer) 60
7) (integer) 70
> TS.RANGE sensor3 10 70 AGGREGATION min 25
1) 1) (integer) 0
   2) 1000
2) 1) (integer) 25
   2) 3000
3) 1) (integer) 50
   2) 5000
```

##### C#

```csharp
        bool res33 = db.TS().Create(
            "sensor3",
            new TsCreateParamsBuilder()
                .build()
        );
        Console.WriteLine(res33); // >>> True

        var sensorSequence = new List<(string, TimeStamp, double)>
        {
            ("sensor3", 10, 1000),
            ("sensor3", 20, 2000),
            ("sensor3", 30, 3000),
            ("sensor3", 40, 4000),
            ("sensor3", 50, 5000),
            ("sensor3", 60, 6000),
            ("sensor3", 70, 7000)
        };
        IReadOnlyList<TimeStamp> res34 = db.TS().MAdd(sensorSequence);
        Console.WriteLine($"[{string.Join(", ", res34.Select(t => t.Value))}]");
        // >>> [10, 20, 30, 40, 50, 60, 70]

        IReadOnlyList<TimeSeriesTuple> res35 = db.TS().Range(
            "sensor3", 10, 70,
            aggregation: TsAggregation.Min,
            timeBucket: 25
        );
        Console.WriteLine($"[{string.Join(", ", res35.Select(t => $"({t.Time.Value}, {t.Val})"))}]");
        // >>> [(0, 1000), (25, 3000), (50, 5000)]
```

##### Go

```go
	res1, err := rdb.TSCreate(ctx, "sensor3").Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // >>> OK

	res2, err := rdb.TSMAdd(ctx, [][]interface{}{
		{"sensor3", 10, 1000},
		{"sensor3", 20, 2000},
		{"sensor3", 30, 3000},
		{"sensor3", 40, 4000},
		{"sensor3", 50, 5000},
		{"sensor3", 60, 6000},
		{"sensor3", 70, 7000},
	}).Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res2) // >>> [10 20 30 40 50 60 70]

	res3, err := rdb.TSRangeWithArgs(
		ctx,
		"sensor3",
		10,
		70,
		&redis.TSRangeOptions{
			Aggregator:     redis.Min,
			BucketDuration: 25,
		},
	).Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res3) // >>> [{0 1000} {25 3000} {50 5000}]
```

##### Java (Synchronous - Jedis)

```java
        String res33 = jedis.tsCreate("sensor3");
        System.out.println(res33); // >>> OK

        List<Long> res34 = jedis.tsMAdd(
            new AbstractMap.SimpleEntry<>("sensor3", new TSElement(10L, 1000.0)),
            new AbstractMap.SimpleEntry<>("sensor3", new TSElement(20L, 2000.0)),
            new AbstractMap.SimpleEntry<>("sensor3", new TSElement(30L, 3000.0)),
            new AbstractMap.SimpleEntry<>("sensor3", new TSElement(40L, 4000.0)),
            new AbstractMap.SimpleEntry<>("sensor3", new TSElement(50L, 5000.0)),
            new AbstractMap.SimpleEntry<>("sensor3", new TSElement(60L, 6000.0)),
            new AbstractMap.SimpleEntry<>("sensor3", new TSElement(70L, 7000.0))
        );
        System.out.println(res34); // >>> [10, 20, 30, 40, 50, 60, 70]

        List<TSElement> res35 = jedis.tsRange("sensor3",
            TSRangeParams.rangeParams()
                .fromTimestamp(10L)
                .toTimestamp(70L)
                .aggregation(AggregationType.MIN, 25)
        );
        System.out.println(res35);
        // >>> [(0:1000.0), (25:3000.0), (50:5000.0)]
```

##### JavaScript (Node.js)

```javascript
const res33 = await client.ts.create('sensor3');
console.log(res33); // >>> OK

const res34 = await client.ts.mAdd([
  { key: 'sensor3', timestamp: 10, value: 1000 },
  { key: 'sensor3', timestamp: 20, value: 2000 },
  { key: 'sensor3', timestamp: 30, value: 3000 },
  { key: 'sensor3', timestamp: 40, value: 4000 },
  { key: 'sensor3', timestamp: 50, value: 5000 },
  { key: 'sensor3', timestamp: 60, value: 6000 },
  { key: 'sensor3', timestamp: 70, value: 7000 }
]);
console.log(res34); // >>> [10, 20, 30, 40, 50, 60, 70]

const res35 = await client.ts.range('sensor3', 10, 70, {
  AGGREGATION: {
    type: TIME_SERIES_AGGREGATION_TYPE.MIN,
    timeBucket: 25
  }
});
console.log(res35);
// >>> [{ timestamp: 0, value: 1000 }, { timestamp: 25, value: 3000 }, { timestamp: 50, value: 5000 }]
```

##### Python

```python
res33 = r.ts().create("sensor3")
print(res33)  # >>> True

res34 = r.ts().madd([
    ("sensor3", 10, 1000),
    ("sensor3", 20, 2000),
    ("sensor3", 30, 3000),
    ("sensor3", 40, 4000),
    ("sensor3", 50, 5000),
    ("sensor3", 60, 6000),
    ("sensor3", 70, 7000),
])
print(res34)  # >>> [10, 20, 30, 40, 50, 60, 70]

res35 = r.ts().range(
    "sensor3", 10, 70,
    aggregation_type="min",
    bucket_size_msec=25
)
print(res35)
# >>> [(0, 1000.0), (25, 3000.0), (50, 5000.0)]
```



The diagram below shows the aggregation buckets and their alignment to the reference timestamp
at time zero.

```
Value:        |      (1000)     (2000)     (3000)     (4000)     (5000)     (6000)     (7000)
Timestamp:    |-------|10|-------|20|-------|30|-------|40|-------|50|-------|60|-------|70|--->

Bucket(25ms): |_________________________||_________________________||___________________________|
                           V                          V                           V
                  min(1000, 2000)=1000      min(3000, 4000)=3000     min(5000, 6000, 7000)=5000
```

You can also align the buckets to the start or end of the query range. For example, the following command aligns the buckets to the start of the query range at time 10.

Custom alignment: Use ALIGN option with aggregations to align buckets to query range start/end when you need aggregations relative to specific time boundaries

**Difficulty:** Advanced

**Builds upon:** agg_bucket

**Commands:** DEL, TS.CREATE, TS.MADD, TS.RANGE

**Complexity:**
- DEL: O(N)
- TS.CREATE: O(1)
- TS.MADD: O(N*M)
- TS.RANGE: O(n/m+k)

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python

##### Redis CLI

```
# Recreate the sensor3 series so this example runs on its own.
> DEL sensor3
(integer) 1
> TS.CREATE sensor3
OK
> TS.MADD sensor3 10 1000 sensor3 20 2000 sensor3 30 3000 sensor3 40 4000 sensor3 50 5000 sensor3 60 6000 sensor3 70 7000
1) (integer) 10
2) (integer) 20
3) (integer) 30
4) (integer) 40
5) (integer) 50
6) (integer) 60
7) (integer) 70
> TS.RANGE sensor3 10 70 AGGREGATION min 25 ALIGN start
1) 1) (integer) 10
   2) 1000
2) 1) (integer) 35
   2) 4000
3) 1) (integer) 60
   2) 6000
```

##### C#

```csharp
        // Recreate the sensor3 series so this example runs on its own.
        db.KeyDelete("sensor3");
        db.TS().Create("sensor3", new TsCreateParamsBuilder().build());
        db.TS().MAdd(new List<(string, TimeStamp, double)>
        {
            ("sensor3", 10, 1000),
            ("sensor3", 20, 2000),
            ("sensor3", 30, 3000),
            ("sensor3", 40, 4000),
            ("sensor3", 50, 5000),
            ("sensor3", 60, 6000),
            ("sensor3", 70, 7000)
        });

        IReadOnlyList<TimeSeriesTuple> res36 = db.TS().Range(
            "sensor3", 10, 70,
            aggregation: TsAggregation.Min,
            timeBucket: 25,
            align: "-"
        );
        Console.WriteLine(
            $"[{string.Join(", ", res36.Select(t => $"({t.Time.Value}, {t.Val})"))}]"
        );
        // >>> [(10, 1000), (35, 4000), (60, 6000)]
```

##### Go

```go
	// Recreate the sensor3 series so this example runs on its own.
	rdb.Del(ctx, "sensor3")
	rdb.TSCreate(ctx, "sensor3")
	rdb.TSMAdd(ctx, [][]interface{}{
		{"sensor3", 10, 1000},
		{"sensor3", 20, 2000},
		{"sensor3", 30, 3000},
		{"sensor3", 40, 4000},
		{"sensor3", 50, 5000},
		{"sensor3", 60, 6000},
		{"sensor3", 70, 7000},
	})

	res4, err := rdb.TSRangeWithArgs(
		ctx,
		"sensor3",
		10,
		70,
		&redis.TSRangeOptions{
			Aggregator:     redis.Min,
			BucketDuration: 25,
			Align:          "START",
		},
	).Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res4) // >>> [{10 1000} {35 4000} {60 6000}]
```

##### Java (Synchronous - Jedis)

```java
        // Recreate the sensor3 series so this example runs on its own.
        jedis.del("sensor3");
        jedis.tsCreate("sensor3");
        jedis.tsMAdd(
            new AbstractMap.SimpleEntry<>("sensor3", new TSElement(10L, 1000.0)),
            new AbstractMap.SimpleEntry<>("sensor3", new TSElement(20L, 2000.0)),
            new AbstractMap.SimpleEntry<>("sensor3", new TSElement(30L, 3000.0)),
            new AbstractMap.SimpleEntry<>("sensor3", new TSElement(40L, 4000.0)),
            new AbstractMap.SimpleEntry<>("sensor3", new TSElement(50L, 5000.0)),
            new AbstractMap.SimpleEntry<>("sensor3", new TSElement(60L, 6000.0)),
            new AbstractMap.SimpleEntry<>("sensor3", new TSElement(70L, 7000.0))
        );

        List<TSElement> res36 = jedis.tsRange("sensor3",
            TSRangeParams.rangeParams()
                .fromTimestamp(10L)
                .toTimestamp(70L)
                .aggregation(AggregationType.MIN, 25)
                .alignStart()
        );
        System.out.println(res36);
        // >>> [(10:1000.0), (35:4000.0), (60:6000.0)]
```

##### JavaScript (Node.js)

```javascript
// Recreate the sensor3 series so this example runs on its own.
await client.del('sensor3');
await client.ts.create('sensor3');
await client.ts.mAdd([
  { key: 'sensor3', timestamp: 10, value: 1000 },
  { key: 'sensor3', timestamp: 20, value: 2000 },
  { key: 'sensor3', timestamp: 30, value: 3000 },
  { key: 'sensor3', timestamp: 40, value: 4000 },
  { key: 'sensor3', timestamp: 50, value: 5000 },
  { key: 'sensor3', timestamp: 60, value: 6000 },
  { key: 'sensor3', timestamp: 70, value: 7000 }
]);

const res36 = await client.ts.range('sensor3', 10, 70, {
  AGGREGATION: {
    type: TIME_SERIES_AGGREGATION_TYPE.MIN,
    timeBucket: 25
  },
  ALIGN: 'START'
});
console.log(res36);
// >>> [{ timestamp: 10, value: 1000 }, { timestamp: 35, value: 4000 }, { timestamp: 60, value: 6000 }]
```

##### Python

```python
# Recreate the sensor3 series so this example runs on its own.
r.delete("sensor3")
r.ts().create("sensor3")
r.ts().madd([
    ("sensor3", 10, 1000),
    ("sensor3", 20, 2000),
    ("sensor3", 30, 3000),
    ("sensor3", 40, 4000),
    ("sensor3", 50, 5000),
    ("sensor3", 60, 6000),
    ("sensor3", 70, 7000),
])

res36 = r.ts().range(
    "sensor3", 10, 70,
    aggregation_type="min",
    bucket_size_msec=25,
    align="START"
)
print(res36)
# >>> [(10, 1000.0), (35, 4000.0), (60, 6000.0)]
```



The diagram below shows this arrangement of buckets.

```
Value:        |      (1000)     (2000)     (3000)     (4000)     (5000)     (6000)     (7000)
Timestamp:    |-------|10|-------|20|-------|30|-------|40|-------|50|-------|60|-------|70|--->

Bucket(25ms):          |__________________________||_________________________||___________________________|
                                    V                          V                           V
                        min(1000, 2000, 3000)=1000      min(4000, 5000)=4000     min(6000, 7000)=6000
```

### Aggregation across timeseries

By default, the results from
[`TS.MRANGE`](https://redis.io/docs/latest/commands/ts.mrange) and
[`TS.MREVRANGE`](https://redis.io/docs/latest/commands/ts.mrevrange) are grouped by time series. However, you can use the `GROUPBY` and `REDUCE` options to group them by label and apply an aggregation over elements
that have the same timestamp and the same label value (this feature is available from RedisTimeSeries v1.6 onwards).

For example, the following commands create four time series, two for the UK and two for the US, and add some data points. The first `TS.MRANGE` command groups the results by country and applies a `max` aggregation to find the maximum sample value in each country at each timestamp. The second `TS.MRANGE` command uses the same grouping, but applies an `avg` aggregation.

Cross-series aggregation: Use GROUPBY and REDUCE with TS.MRANGE to aggregate data across multiple time series by label when you need to compute statistics across groups

**Difficulty:** Advanced

**Builds upon:** agg, create_labels

**Commands:** TS.CREATE, TS.MADD, TS.MRANGE

**Complexity:**
- TS.CREATE: O(1)
- TS.MADD: O(N*M)
- TS.MRANGE: O(n/m+k)

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python

##### Redis CLI

```
> TS.CREATE wind:1 LABELS country uk
OK
> TS.CREATE wind:2 LABELS country uk
OK
> TS.CREATE wind:3 LABELS country us
OK
> TS.CREATE wind:4 LABELS country us
OK
> TS.MADD wind:1 1 12 wind:2 1 18 wind:3 1 5 wind:4 1 20
1) (integer) 1
2) (integer) 1
3) (integer) 1
4) (integer) 1
> TS.MADD wind:1 2 14 wind:2 2 21 wind:3 2 4 wind:4 2 25
1) (integer) 2
2) (integer) 2
3) (integer) 2
4) (integer) 2
> TS.MADD wind:1 3 10 wind:2 3 24 wind:3 3 8 wind:4 3 18
1) (integer) 3
2) (integer) 3
3) (integer) 3
4) (integer) 3

# The result pairs contain the timestamp and the maximum sample value
# for the country at that timestamp.
> TS.MRANGE - + FILTER country=(us,uk) GROUPBY country REDUCE max
1) 1) "country=uk"
   2) (empty array)
   3) 1) 1) (integer) 1
         2) 18
      2) 1) (integer) 2
         2) 21
      3) 1) (integer) 3
         2) 24
2) 1) "country=us"
   2) (empty array)
   3) 1) 1) (integer) 1
         2) 20
      2) 1) (integer) 2
         2) 25
      3) 1) (integer) 3
         2) 18

# The result pairs contain the timestamp and the average sample value
# for the country at that timestamp.
> TS.MRANGE - + FILTER country=(us,uk) GROUPBY country REDUCE avg
1) 1) "country=uk"
   2) (empty array)
   3) 1) 1) (integer) 1
         2) 15
      2) 1) (integer) 2
         2) 17.5
      3) 1) (integer) 3
         2) 17
2) 1) "country=us"
   2) (empty array)
   3) 1) 1) (integer) 1
         2) 12.5
      2) 1) (integer) 2
         2) 14.5
      3) 1) (integer) 3
         2) 13
```

##### C#

```csharp
        var ukLabels = new List<TimeSeriesLabel> { new("country", "uk") };

        bool res37 = db.TS().Create(
            "wind:1",
            new TsCreateParamsBuilder()
                .AddLabels(ukLabels)
                .build()
        );
        Console.WriteLine(res37); // >>> True

        bool res38 = db.TS().Create(
            "wind:2",
            new TsCreateParamsBuilder()
                .AddLabels(ukLabels)
                .build()
        );
        Console.WriteLine(res38); // >>> True

        var usLabels = new List<TimeSeriesLabel> { new("country", "us") };
        bool res39 = db.TS().Create(
            "wind:3",
            new TsCreateParamsBuilder()
                .AddLabels(usLabels)
                .build()
        );
        Console.WriteLine(res39); // >>> True

        bool res40 = db.TS().Create(
            "wind:4",
            new TsCreateParamsBuilder()
                .AddLabels(usLabels)
                .build()
        );
        Console.WriteLine(res40); // >>> True

        var windSequence1 = new List<(string, TimeStamp, double)>
        {
            ("wind:1", 1, 12),
            ("wind:2", 1, 18),
            ("wind:3", 1, 5),
            ("wind:4", 1, 20)
        };
        IReadOnlyList<TimeStamp> res41 = db.TS().MAdd(windSequence1);
        Console.WriteLine(
            $"[{string.Join(", ", res41.Select(t => t.Value))}]"
        );
        // >>> [1, 1, 1, 1]

        var windSequence2 = new List<(string, TimeStamp, double)>
        {
            ("wind:1", 2, 14),
            ("wind:2", 2, 21),
            ("wind:3", 2, 4),
            ("wind:4", 2, 25)
        };
        IReadOnlyList<TimeStamp> res42 = db.TS().MAdd(windSequence2);
        Console.WriteLine(
            $"[{string.Join(", ", res42.Select(t => t.Value))}]"
        );
        // >>> [2, 2, 2, 2]

        var windSequence3 = new List<(string, TimeStamp, double)>
        {
            ("wind:1", 3, 10),
            ("wind:2", 3, 24),
            ("wind:3", 3, 8),
            ("wind:4", 3, 18)
        };
        IReadOnlyList<TimeStamp> res43 = db.TS().MAdd(windSequence3);
        Console.WriteLine(
            $"[{string.Join(", ", res43.Select(t => t.Value))}]"
        );
        // >>> [3, 3, 3, 3]

        // The result pairs contain the timestamp and the maximum sample value
        // for the country at that timestamp.
        var countryFilters = new List<string> { "country=(us,uk)" };
        IReadOnlyList<
            (string, IReadOnlyList<TimeSeriesLabel>, IReadOnlyList<TimeSeriesTuple>)
        > res44 = db.TS().MRange(
            "-", "+",
            countryFilters,
            groupbyTuple: ("country", TsReduce.Max)
        );
        Console.WriteLine(res44.Count); // >>> 2

        foreach (var (key, labelsResult, values) in res44)
        {
            Console.WriteLine($"{key}:");
            Console.WriteLine($"  Values: [{string.Join(", ", values.Select(t => $"({t.Time.Value}, {t.Val})"))}]");
        }
        // >>> country=uk
        // >>>   Values: [(1, 18), (2, 21), (3, 24)]
        // >>> country=us
        // >>>   Values: [(1, 20), (2, 25), (3, 18)]

        // The result pairs contain the timestamp and the average sample value
        // for the country at that timestamp.
        IReadOnlyList<
            (string, IReadOnlyList<TimeSeriesLabel>, IReadOnlyList<TimeSeriesTuple>)
        > res45 = db.TS().MRange(
            "-", "+",
            countryFilters,
            groupbyTuple: ("country", TsReduce.Avg)
        );
        Console.WriteLine(res45.Count); // >>> 2

        foreach (var (key, labelsResult, values) in res45)
        {
            Console.WriteLine($"{key}:");
            Console.WriteLine($"  Values: [{string.Join(", ", values.Select(t => $"({t.Time.Value}, {t.Val})"))}]");
        }
        // >>>   country=uk
        // >>>      Values: [(1, 14), (2, 18), (3, 10)]
        // >>>   country=us
        // >>>      Values: [(1, 16), (2, 22), (3, 14)]
```

##### Go

```go
	res37, err := rdb.TSCreateWithArgs(ctx, "wind:1", &redis.TSOptions{
		Labels: map[string]string{"country": "uk"},
	}).Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res37) // >>> OK

	res38, err := rdb.TSCreateWithArgs(ctx, "wind:2", &redis.TSOptions{
		Labels: map[string]string{"country": "uk"},
	}).Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res38) // >>> OK

	res39, err := rdb.TSCreateWithArgs(ctx, "wind:3", &redis.TSOptions{
		Labels: map[string]string{"country": "us"},
	}).Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res39) // >>> OK

	res40, err := rdb.TSCreateWithArgs(ctx, "wind:4", &redis.TSOptions{
		Labels: map[string]string{"country": "us"},
	}).Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res40) // >>> OK

	res41, err := rdb.TSMAdd(ctx, [][]interface{}{
		{"wind:1", 1, 12},
		{"wind:2", 1, 18},
		{"wind:3", 1, 5},
		{"wind:4", 1, 20},
	}).Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res41) // >>> [1 1 1 1]

	res42, err := rdb.TSMAdd(ctx, [][]interface{}{
		{"wind:1", 2, 14},
		{"wind:2", 2, 21},
		{"wind:3", 2, 4},
		{"wind:4", 2, 25},
	}).Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res42) // >>> [2 2 2 2]

	res43, err := rdb.TSMAdd(ctx, [][]interface{}{
		{"wind:1", 3, 10},
		{"wind:2", 3, 24},
		{"wind:3", 3, 8},
		{"wind:4", 3, 18},
	}).Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res43) // >>> [3 3 3 3]

	// The result pairs contain the timestamp and the maximum sample value
	// for the country at that timestamp.
	res44, err := rdb.TSMRangeWithArgs(
		ctx,
		0,
		math.MaxInt64,
		[]string{"country=(us,uk)"},
		&redis.TSMRangeOptions{
			GroupByLabel: "country",
			Reducer:      "max",
		},
	).Result()
	if err != nil {
		panic(err)
	}

	res44Keys := slices.Collect(maps.Keys(res44))
	sort.Strings(res44Keys)

	for _, k := range res44Keys {
		labels := res44[k][0].(map[interface{}]interface{})
		labelKeys := make([]string, 0, len(labels))

		for lk := range labels {
			labelKeys = append(labelKeys, lk.(string))
		}

		sort.Strings(labelKeys)

		fmt.Printf("%v:\n", k)

		for _, lk := range labelKeys {
			fmt.Printf("  %v: %v\n", lk, labels[lk])
		}

		fmt.Printf("  %v\n", res44[k][1])
		fmt.Printf("  %v\n", res44[k][2])
		fmt.Printf("  %v\n", res44[k][3])
	}
	// >>> country=uk:
	// >>>   map[reducers:[max]]
	// >>>   map[sources:[wind:1 wind:2]]
	// >>>   [[1 18] [2 21] [3 24]]
	// >>> country=us:
	// >>>   map[reducers:[max]]
	// >>>   map[sources:[wind:3 wind:4]]
	// >>>   [[1 20] [2 25] [3 18]]

	// The result pairs contain the timestamp and the average sample value
	// for the country at that timestamp.
	res45, err := rdb.TSMRangeWithArgs(
		ctx,
		0,
		math.MaxInt64,
		[]string{"country=(us,uk)"},
		&redis.TSMRangeOptions{
			GroupByLabel: "country",
			Reducer:      "avg",
		},
	).Result()
	if err != nil {
		panic(err)
	}

	res45Keys := slices.Collect(maps.Keys(res45))
	sort.Strings(res45Keys)

	for _, k := range res45Keys {
		labels := res45[k][0].(map[interface{}]interface{})
		labelKeys := make([]string, 0, len(labels))

		for lk := range labels {
			labelKeys = append(labelKeys, lk.(string))
		}

		sort.Strings(labelKeys)

		fmt.Printf("%v:\n", k)

		for _, lk := range labelKeys {
			fmt.Printf("  %v: %v\n", lk, labels[lk])
		}

		fmt.Printf("  %v\n", res45[k][1])
		fmt.Printf("  %v\n", res45[k][2])
		fmt.Printf("  %v\n", res45[k][3])
	}
	// >>> country=uk:
	// >>>   map[reducers:[avg]]
	// >>>   map[sources:[wind:1 wind:2]]
	// >>>   [[1 15] [2 17.5] [3 17]]
	// >>> country=us:
	// >>>   map[reducers:[avg]]
	// >>>   map[sources:[wind:3 wind:4]]
	// >>>   [[1 12.5] [2 14.5] [3 13]]
```

##### Java (Synchronous - Jedis)

```java
        Map<String, String> ukCountry = new HashMap<>();
        ukCountry.put("country", "uk");
        
        Map<String, String> usCountry = new HashMap<>();
        usCountry.put("country", "us");

        jedis.tsCreate("wind:1", TSCreateParams.createParams().labels(ukCountry));
        jedis.tsCreate("wind:2", TSCreateParams.createParams().labels(ukCountry));
        jedis.tsCreate("wind:3", TSCreateParams.createParams().labels(usCountry));
        jedis.tsCreate("wind:4", TSCreateParams.createParams().labels(usCountry));

        jedis.tsMAdd(
            new AbstractMap.SimpleEntry<>("wind:1", new TSElement(0L, 10.0)),
            new AbstractMap.SimpleEntry<>("wind:2", new TSElement(0L, 12.0)),
            new AbstractMap.SimpleEntry<>("wind:3", new TSElement(0L, 8.0)),
            new AbstractMap.SimpleEntry<>("wind:4", new TSElement(0L, 15.0))
        );

        jedis.tsMAdd(
            new AbstractMap.SimpleEntry<>("wind:1", new TSElement(1L, 11.0)),
            new AbstractMap.SimpleEntry<>("wind:2", new TSElement(1L, 13.0)),
            new AbstractMap.SimpleEntry<>("wind:3", new TSElement(1L, 9.0)),
            new AbstractMap.SimpleEntry<>("wind:4", new TSElement(1L, 16.0))
        );

        jedis.tsMAdd(
            new AbstractMap.SimpleEntry<>("wind:1", new TSElement(2L, 9.0)),
            new AbstractMap.SimpleEntry<>("wind:2", new TSElement(2L, 11.0)),
            new AbstractMap.SimpleEntry<>("wind:3", new TSElement(2L, 7.0)),
            new AbstractMap.SimpleEntry<>("wind:4", new TSElement(2L, 14.0))
        );

        jedis.tsMAdd(
            new AbstractMap.SimpleEntry<>("wind:1", new TSElement(3L, 12.0)),
            new AbstractMap.SimpleEntry<>("wind:2", new TSElement(3L, 14.0)),
            new AbstractMap.SimpleEntry<>("wind:3", new TSElement(3L, 10.0)),
            new AbstractMap.SimpleEntry<>("wind:4", new TSElement(3L, 17.0))
        );

        jedis.tsMAdd(
            new AbstractMap.SimpleEntry<>("wind:1", new TSElement(4L, 8.0)),
            new AbstractMap.SimpleEntry<>("wind:2", new TSElement(4L, 10.0)),
            new AbstractMap.SimpleEntry<>("wind:3", new TSElement(4L, 6.0)),
            new AbstractMap.SimpleEntry<>("wind:4", new TSElement(4L, 13.0))
        );

        // Group by country with max reduction
        Map<String, TSMRangeElements> res44 = jedis.tsMRange(
            TSMRangeParams.multiRangeParams(0L, 4L)
                .filter("country=(us,uk)")
                .groupBy("country", "max"));
        System.out.println(res44);
        // >>> {country=uk=TSMRangeElements{key=country=uk, labels={}, value=[(0:12.0)...

        // Group by country with avg reduction
        Map<String, TSMRangeElements> res45 = jedis.tsMRange(
            TSMRangeParams.multiRangeParams(0L, 4L)
                .filter("country=(us,uk)")
                .groupBy("country", "avg"));
        System.out.println(res45);
        // >>> {country=uk=TSMRangeElements{key=country=uk, labels={}, value=[(0:11.0)...
```

##### JavaScript (Node.js)

```javascript
const res37 = await client.ts.create('wind:1', {
  LABELS: { country: 'uk' }
});
console.log(res37); // >>> OK

const res38 = await client.ts.create('wind:2', {
  LABELS: { country: 'uk' }
});
console.log(res38); // >>> OK

const res39 = await client.ts.create('wind:3', {
  LABELS: { country: 'us' }
});
console.log(res39); // >>> OK

const res40 = await client.ts.create('wind:4', {
  LABELS: { country: 'us' }
});
console.log(res40); // >>> OK

const res41 = await client.ts.mAdd([
  { key: 'wind:1', timestamp: 1, value: 12 },
  { key: 'wind:2', timestamp: 1, value: 18 },
  { key: 'wind:3', timestamp: 1, value: 5 },
  { key: 'wind:4', timestamp: 1, value: 20 }
]);
console.log(res41); // >>> [1, 1, 1, 1]

const res42 = await client.ts.mAdd([
  { key: 'wind:1', timestamp: 2, value: 14 },
  { key: 'wind:2', timestamp: 2, value: 21 },
  { key: 'wind:3', timestamp: 2, value: 4 },
  { key: 'wind:4', timestamp: 2, value: 25 }
]);
console.log(res42); // >>> [2, 2, 2, 2]

const res43 = await client.ts.mAdd([
  { key: 'wind:1', timestamp: 3, value: 10 },
  { key: 'wind:2', timestamp: 3, value: 24 },
  { key: 'wind:3', timestamp: 3, value: 8 },
  { key: 'wind:4', timestamp: 3, value: 18 }
]);
console.log(res43); // >>> [3, 3, 3, 3]

// The result pairs contain the timestamp and the maximum sample value
// for the country at that timestamp.
const res44 = await client.ts.mRangeGroupBy(
  '-', '+', ['country=(us,uk)'],
  {label: 'country', REDUCE: TIME_SERIES_REDUCERS.MAX}
);
console.log(res44);
// >>> { "country=uk": { samples: [
//   { timestamp: 1, value: 18 },
//   { timestamp: 2, value: 21 },
//   { timestamp: 3, value: 24 }
// ] }, "country=us": { samples: [
//   { timestamp: 1, value: 20 },
//   { timestamp: 2, value: 25 },
//   { timestamp: 3, value: 18 }
// ] } }

// The result pairs contain the timestamp and the average sample value
// for the country at that timestamp.
const res45 = await client.ts.mRangeGroupBy(
  '-', '+', ['country=(us,uk)'],
  { label: 'country', REDUCE: TIME_SERIES_REDUCERS.AVG}
);
console.log(res45);
// >>> {
// "country=uk": {
//   samples: [{ timestamp: 1, value: 15 }, { timestamp: 2, value: 17.5 }, { timestamp: 3, value: 17 }]
// },
// "country=us": {
//   samples: [{ timestamp: 1, value: 12.5 }, { timestamp: 2, value: 14.5 }, { timestamp: 3, value: 13 }]
// }
// }
```

##### Python

```python
res37 = r.ts().create(
    "wind:1",
    labels={"country": "uk"}
)
print(res37)  # >>> True

res38 = r.ts().create(
    "wind:2",
    labels={"country": "uk"}
)
print(res38)  # >>> True

res39 = r.ts().create(
    "wind:3",
    labels={"country": "us"}
)
print(res39)  # >>> True

res40 = r.ts().create(
    "wind:4",
    labels={"country": "us"}
)
print(res40)  # >>> True

res41 = r.ts().madd([
        ("wind:1", 1, 12),
        ("wind:2", 1, 18),
        ("wind:3", 1, 5),
        ("wind:4", 1, 20),
])
print(res41)  # >>> [1, 1, 1, 1]

res42 = r.ts().madd([
        ("wind:1", 2, 14),
        ("wind:2", 2, 21),
        ("wind:3", 2, 4),
        ("wind:4", 2, 25),
])
print(res42)  # >>> [2, 2, 2, 2]

res43 = r.ts().madd([
        ("wind:1", 3, 10),
        ("wind:2", 3, 24),
        ("wind:3", 3, 8),
        ("wind:4", 3, 18),
])
print(res43)  # >>> [3, 3, 3, 3]

# The result pairs contain the timestamp and the maximum sample value
# for the country at that timestamp.
res44 = r.ts().mrange(
    "-", "+",
    filters=["country=(us,uk)"],
    groupby="country",
    reduce="max"
)
print(res44)
# >>> [{'country=uk': [{}, [(1, 18.0), (2, 21.0), (3, 24.0)]]}, ...

# The result pairs contain the timestamp and the average sample value
# for the country at that timestamp.
res45 = r.ts().mrange(
    "-", "+",
    filters=["country=(us,uk)"],
    groupby="country",
    reduce="avg"
)
print(res45)
# >>> [{'country=uk': [{}, [(1, 15.0), (2, 17.5), (3, 17.0)]]}, ...
```



## NaN Values

Starting from Redis 8.6, time series support NaN (Not a Number) values. This feature allows you to insert measurements that represent missing, invalid, or unknown data while preserving the temporal structure of your time series.

### Use Cases for NaN Values

NaN values are useful in scenarios where you need to distinguish between:
- **Missing data**: A timestamp where no measurement was taken
- **Invalid data**: A timestamp where a measurement was attempted but failed (for example, sensor malfunction)
- **Unknown data**: A timestamp where the measurement value is semantically "unknown" and may be filled in later

### NaN Behavior

- **Adding NaN values**: Use [`TS.ADD`](https://redis.io/docs/latest/commands/ts.add) and [`TS.MADD`](https://redis.io/docs/latest/commands/ts.madd) to insert NaN values
- **Querying NaN values**: All raw measurement queries ([`TS.GET`](https://redis.io/docs/latest/commands/ts.get), [`TS.RANGE`](https://redis.io/docs/latest/commands/ts.range), etc.) include NaN values in results
- **Aggregation with NaN**: All existing aggregators except `countNaN` and `countAll` ignore NaN values. Use `countNaN` and `countAll` to count NaN and total values
- **Increment/Decrement**: [`TS.INCRBY`](https://redis.io/docs/latest/commands/ts.incrby) and [`TS.DECRBY`](https://redis.io/docs/latest/commands/ts.decrby) return errors when the current value or operand is NaN
- **Duplicate policies**: Special handling for `MIN`, `MAX`, and `SUM` policies when mixing NaN and non-NaN values
- **Filtering**: [`FILTER_BY_VALUE`](https://redis.io/docs/latest/commands/ts.range#filter_by_value-min-max-since-redistimeseries-v16) parameters cannot be NaN values
- **Ignore duplicates**: NaN values are never considered duplicates when using `IGNORE` parameters

```bash
# Create a temperature sensor time series
> TS.CREATE sensor:temp LABELS type temperature location outdoor

# Add normal readings and NaN for sensor malfunction
> TS.MADD sensor:temp 1000 25.5 sensor:temp 1010 26.1 sensor:temp 1020 NaN sensor:temp 1030 24.8
1) (integer) 1000
2) (integer) 1010
3) (integer) 1020
4) (integer) 1030

# Query all values - NaN is included in raw results
> TS.RANGE sensor:temp - +
1) 1) (integer) 1000
   2) 25.5
2) 1) (integer) 1010
   2) 26.1
3) 1) (integer) 1020
   2) NaN
4) 1) (integer) 1030
   2) 24.8

# Aggregate ignores NaN - average of 25.5, 26.1, 24.8 = 25.47
> TS.RANGE sensor:temp - + AGGREGATION avg 1000
1) 1) (integer) 1000
   2) 25.466666666666665

# Count non-NaN values
> TS.RANGE sensor:temp - + AGGREGATION count 1000
1) 1) (integer) 1000
   2) 3

# Count NaN values
> TS.RANGE sensor:temp - + AGGREGATION countNaN 1000
1) 1) (integer) 1000
   2) 1

# Count all values
> TS.RANGE sensor:temp - + AGGREGATION countAll 1000
1) 1) (integer) 1000
   2) 4
```

## Compaction

[Aggregation](#aggregation) queries let you extract the important information from a large data set
into a smaller, more manageable set. If you are continually adding new data to a
time series as it is generated, you may need to run the same aggregation
regularly on the latest data. Instead of running the query manually
each time, you can add a *compaction rule* to a time series to compute an
aggregation incrementally on data as it arrives. The values from the
aggregation buckets are stored in a separate time series, leaving the original
series unchanged.

Use [`TS.CREATERULE`](https://redis.io/docs/latest/commands/ts.createrule) to create a
compaction rule, specifying the source and destination time series keys, an
aggregator, and the bucket duration. Note that the destination time
series must already exist when you create the rule and also that the compaction will
only process data that is added to the source series after you create the rule.

For example, you could use the commands below to create a time series along with a
compaction rule to find the minimum reading in each period of 3ms.

Compaction rules: Use TS.CREATERULE to automatically aggregate data into a destination time series when you need to maintain pre-computed aggregations

**Difficulty:** Advanced

**Builds upon:** create

**Commands:** TS.CREATE, TS.CREATERULE, TS.INFO

**Complexity:**
- TS.CREATE: O(1)
- TS.CREATERULE: O(1)
- TS.INFO: O(1)

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python

##### Redis CLI

```
# The source time series.
> TS.CREATE hyg:1
OK
# The destination time series for the compacted data.
> TS.CREATE hyg:compacted
OK
# The compaction rule.
> TS.CREATERULE hyg:1 hyg:compacted AGGREGATION min 3
OK
> TS.INFO hyg:1
 1) totalSamples
 2) (integer) 0
 3) memoryUsage
 4) (integer) 4592
 5) firstTimestamp
 6) (integer) 0
 7) lastTimestamp
 8) (integer) 0
 9) retentionTime
10) (integer) 0
11) chunkCount
12) (integer) 1
13) chunkSize
14) (integer) 4096
15) chunkType
16) compressed
17) duplicatePolicy
18) block
19) labels
20) (empty array)
21) sourceKey
22) (nil)
23) rules
24) 1) 1) "hyg:compacted"
       2) (integer) 3
       3) MIN
       4) (integer) 0
25) ignoreMaxTimeDiff
26) (integer) 0
27) ignoreMaxValDiff
28) "0"
```

##### C#

```csharp
        bool res46 = db.TS().Create(
            "hyg:1",
            new TsCreateParamsBuilder().build()
        );
        Console.WriteLine(res46); // >>> True

        bool res47 = db.TS().Create(
            "hyg:compacted",
            new TsCreateParamsBuilder().build()
        );
        Console.WriteLine(res47); // >>> True

        var compactionRule = new TimeSeriesRule("hyg:compacted", 3, TsAggregation.Min);
        bool res48 = db.TS().CreateRule("hyg:1", compactionRule);
        Console.WriteLine(res48); // >>> True

        TimeSeriesInformation res49 = db.TS().Info("hyg:1");
        Console.WriteLine(res49.Rules!.Count);
        // >>> 1

        TimeSeriesInformation res50 = db.TS().Info("hyg:compacted");
        Console.WriteLine(res50.SourceKey);
        // >>> hyg:1
```

##### Go

```go
	res45, err := rdb.TSCreate(ctx, "hyg:1").Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res45) // >>> OK

	res46, err := rdb.TSCreate(ctx, "hyg:compacted").Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res46) // >>> OK

	res47, err := rdb.TSCreateRule(
		ctx, "hyg:1", "hyg:compacted", redis.Min, 3,
	).Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res47) // >>> OK

	res48, err := rdb.TSInfo(ctx, "hyg:1").Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res48["rules"]) // >>> [[hyg:compacted 3 MIN 0]]

	res49, err := rdb.TSInfo(ctx, "hyg:compacted").Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res49["sourceKey"]) // >>> hyg:1
```

##### Java (Synchronous - Jedis)

```java
        String res46 = jedis.tsCreate("hyg:1");
        System.out.println(res46); // >>> OK

        String res47 = jedis.tsCreate("hyg:compacted");
        System.out.println(res47); // >>> OK

        String res48 = jedis.tsCreateRule("hyg:1", "hyg:compacted", AggregationType.MIN, 3);
        System.out.println(res48); // >>> OK

        TSInfo res49 = jedis.tsInfo("hyg:1");
        System.out.println("Rules: " + res49.getProperty("rules"));
        // >>> Rules: [{compactionKey=hyg:compacted, bucketDuration=3, aggregationType=MIN, alignmentTimestamp=0}]

        TSInfo res50 = jedis.tsInfo("hyg:compacted");
        System.out.println("Source key: " + res50.getProperty("sourceKey"));
        // >>> Source key: hyg:1
```

##### JavaScript (Node.js)

```javascript
const res46 = await client.ts.create('hyg:1');
console.log(res46); // >>> OK

const res47 = await client.ts.create('hyg:compacted');
console.log(res47); // >>> OK

const res48 = await client.ts.createRule('hyg:1', 'hyg:compacted', TIME_SERIES_AGGREGATION_TYPE.MIN, 3);
console.log(res48); // >>> OK

const res49 = await client.ts.info('hyg:1');
console.log(res49.rules);
// >>> [{ aggregationType: 'MIN', key: 'hyg:compacted', timeBucket: 3}]

const res50 = await client.ts.info('hyg:compacted');
console.log(res50.sourceKey); // >>> 'hyg:1'
```

##### Python

```python
res45 = r.ts().create("hyg:1")
print(res45)  # >>> True

res46 = r.ts().create("hyg:compacted")
print(res46)  # >>> True

res47 = r.ts().createrule("hyg:1", "hyg:compacted", "min", 3)
print(res47)  # >>> True

res48 = r.ts().info("hyg:1")
print(res48.rules)
# >>> [['hyg:compacted', 3, 'MIN', 0]]

res49 = r.ts().info("hyg:compacted")
print(res49.source_key)  # >>> 'hyg:1'
```



Adding data points within the first 3ms (the first bucket) doesn't
produce any data in the compacted series. However, when you add data for
time 4 (in the second bucket), the compaction rule computes the minimum
value for the first bucket and adds it to the compacted series.

Compaction behavior: Understand how compaction rules process data incrementally, computing aggregates for completed buckets when new data arrives

**Difficulty:** Intermediate

**Builds upon:** create_compaction

**Commands:** DEL, TS.CREATE, TS.CREATERULE, TS.MADD, TS.RANGE, TS.ADD

**Complexity:**
- DEL: O(N)
- TS.CREATE: O(1)
- TS.CREATERULE: O(1)
- TS.MADD: O(N*M)
- TS.RANGE: O(n/m+k)
- TS.ADD: O(M)

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python

##### Redis CLI

```
# Recreate the compaction rule so this example runs on its own.
> DEL hyg:1 hyg:compacted
(integer) 2
> TS.CREATE hyg:1
OK
> TS.CREATE hyg:compacted
OK
> TS.CREATERULE hyg:1 hyg:compacted AGGREGATION min 3
OK
> TS.MADD hyg:1 0 75 hyg:1 1 77 hyg:1 2 78
1) (integer) 0
2) (integer) 1
3) (integer) 2
> ts.range hyg:compacted - +
(empty array)
> TS.ADD hyg:1 3 79
(integer) 3
> ts.range hyg:compacted - +
1) 1) (integer) 0
   2) 75
```

##### C#

```csharp
        // Recreate the compaction rule so this example runs on its own.
        db.KeyDelete(new RedisKey[] { "hyg:1", "hyg:compacted" });
        db.TS().Create("hyg:1", new TsCreateParamsBuilder().build());
        db.TS().Create("hyg:compacted", new TsCreateParamsBuilder().build());
        db.TS().CreateRule("hyg:1", new TimeSeriesRule("hyg:compacted", 3, TsAggregation.Min));

        var hygSequence1 = new List<(string, TimeStamp, double)>
        {
            ("hyg:1", 0, 75),
            ("hyg:1", 1, 77),
            ("hyg:1", 2, 78)
        };
        IReadOnlyList<TimeStamp> res51 = db.TS().MAdd(hygSequence1);
        Console.WriteLine($"[{string.Join(", ", res51.Select(t => t.Value))}]");
        // >>> [0, 1, 2]

        IReadOnlyList<TimeSeriesTuple> res52 = db.TS().Range("hyg:compacted", "-", "+");
        Console.WriteLine(res52.Count); // >>> 0

        TimeStamp res53 = db.TS().Add(
            "hyg:1",
            new TsAddParamsBuilder()
                .AddTimestamp(3)
                .AddValue(79)
                .build()
        );
        Console.WriteLine(res53.Value); // >>> 3

        IReadOnlyList<TimeSeriesTuple> res54 = db.TS().Range("hyg:compacted", "-", "+");
        Console.WriteLine(
            $"[{string.Join(", ", res54.Select(t => $"({t.Time.Value}, {t.Val})"))}]"
        );
        // >>> [(0, 75)]
```

##### Go

```go
	// Recreate the compaction rule so this example runs on its own.
	rdb.Del(ctx, "hyg:1", "hyg:compacted")
	rdb.TSCreate(ctx, "hyg:1")
	rdb.TSCreate(ctx, "hyg:compacted")
	rdb.TSCreateRule(ctx, "hyg:1", "hyg:compacted", redis.Min, 3)

	res50, err := rdb.TSMAdd(ctx, [][]interface{}{
		{"hyg:1", 0, 75},
		{"hyg:1", 1, 77},
		{"hyg:1", 2, 78},
	}).Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res50) // >>> [0 1 2]

	res51, err := rdb.TSRange(
		ctx, "hyg:compacted", 0, math.MaxInt64,
	).Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res51) // >>> []

	res52, err := rdb.TSAdd(ctx, "hyg:1", 3, 79).Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res52) // >>> 3

	res53, err := rdb.TSRange(
		ctx, "hyg:compacted", 0, math.MaxInt64,
	).Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res53) // >>> [{0 75}]
```

##### Java (Synchronous - Jedis)

```java
        // Recreate the compaction rule so this example runs on its own.
        jedis.del("hyg:1", "hyg:compacted");
        jedis.tsCreate("hyg:1");
        jedis.tsCreate("hyg:compacted");
        jedis.tsCreateRule("hyg:1", "hyg:compacted", AggregationType.MIN, 3);

        List<Long> res51 = jedis.tsMAdd(
            new AbstractMap.SimpleEntry<>("hyg:1", new TSElement(0L, 75.0)),
            new AbstractMap.SimpleEntry<>("hyg:1", new TSElement(1L, 77.0)),
            new AbstractMap.SimpleEntry<>("hyg:1", new TSElement(2L, 78.0))
        );
        System.out.println(res51); // >>> [0, 1, 2]

        List<TSElement> res52 = jedis.tsRange("hyg:compacted", 0L, 10L);
        System.out.println(res52); // >>> []

        long res53 = jedis.tsAdd("hyg:1", 3L, 79.0);
        System.out.println(res53); // >>> 3

        List<TSElement> res54 = jedis.tsRange("hyg:compacted", 0L, 10L);
        System.out.println(res54); // >>> [(0:75.0)]
```

##### JavaScript (Node.js)

```javascript
// Recreate the compaction rule so this example runs on its own.
await client.del(['hyg:1', 'hyg:compacted']);
await client.ts.create('hyg:1');
await client.ts.create('hyg:compacted');
await client.ts.createRule('hyg:1', 'hyg:compacted', TIME_SERIES_AGGREGATION_TYPE.MIN, 3);

const res51 = await client.ts.mAdd([
  { key: 'hyg:1', timestamp: 0, value: 75 },
  { key: 'hyg:1', timestamp: 1, value: 77 },
  { key: 'hyg:1', timestamp: 2, value: 78 }
]);
console.log(res51); // >>> [0, 1, 2]

const res52 = await client.ts.range('hyg:compacted', '-', '+');
console.log(res52); // >>> []

const res53 = await client.ts.add('hyg:1', 3, 79);
console.log(res53); // >>> 3

const res54 = await client.ts.range('hyg:compacted', '-', '+');
console.log(res54); // >>> [{ timestamp: 0, value: 75 }]
```

##### Python

```python
# Recreate the compaction rule so this example runs on its own.
r.delete("hyg:1", "hyg:compacted")
r.ts().create("hyg:1")
r.ts().create("hyg:compacted")
r.ts().createrule("hyg:1", "hyg:compacted", "min", 3)

res50 = r.ts().madd([
    ("hyg:1", 0, 75),
    ("hyg:1", 1, 77),
    ("hyg:1", 2, 78),
])
print(res50)  # >>> [0, 1, 2]

res51 = r.ts().range("hyg:compacted", "-", "+")
print(res51)  # >>> []

res52 = r.ts().add("hyg:1", 3, 79)
print(res52)  # >>> 3

res53 = r.ts().range("hyg:compacted", "-", "+")
print(res53)  # >>> [(0, 75.0)]
```



The general strategy is that the rule does not add data to the
compaction for the latest bucket in the source series, but will add and
update the compacted data for any previous buckets. This reflects the
typical usage pattern of adding data samples sequentially in real time
(an aggregate value typically isn't correct until its bucket period is over).
But note that earlier buckets are not "closed" when you add data to a later
bucket. If you add or [delete](#deleting-data-points) data in a bucket before
the latest one, the compaction rule will still update the compacted data for
that bucket.

## Delete data points

Use [`TS.DEL`](https://redis.io/docs/latest/commands/ts.del) to delete data points
that fall within a given timestamp range. The range is inclusive, meaning that
samples whose timestamp equals the start or end of the range are deleted.
If you want to delete a single timestamp, use it as both the start and end of the range.

Deleting data: Use TS.DEL to remove data points within a timestamp range when you need to clean up or correct historical data

**Difficulty:** Beginner

**Builds upon:** create

**Commands:** DEL, TS.ADD, TS.INFO, TS.DEL

**Complexity:**
- DEL: O(N)
- TS.ADD: O(M)
- TS.INFO: O(1)
- TS.DEL: O(N)

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python

##### Redis CLI

```
# Recreate the thermometer:1 series so this example runs on its own.
> DEL thermometer:1
(integer) 1
> TS.ADD thermometer:1 1 9.2
(integer) 1
> TS.ADD thermometer:1 2 9.9
(integer) 2
> TS.INFO thermometer:1
 1) totalSamples
 2) (integer) 2
 3) memoryUsage
 4) (integer) 4504
 5) firstTimestamp
 6) (integer) 1
 7) lastTimestamp
 8) (integer) 2
 9) retentionTime
10) (integer) 0
11) chunkCount
12) (integer) 1
13) chunkSize
14) (integer) 4096
15) chunkType
16) compressed
17) duplicatePolicy
18) block
19) labels
20) (empty array)
21) sourceKey
22) (nil)
23) rules
24) (empty array)
25) ignoreMaxTimeDiff
26) (integer) 0
27) ignoreMaxValDiff
28) "0"
> TS.ADD thermometer:1 3 9.7
(integer) 3
> TS.INFO thermometer:1
 1) totalSamples
 2) (integer) 3
 3) memoryUsage
 4) (integer) 4504
 5) firstTimestamp
 6) (integer) 1
 7) lastTimestamp
 8) (integer) 3
 9) retentionTime
10) (integer) 0
11) chunkCount
12) (integer) 1
13) chunkSize
14) (integer) 4096
15) chunkType
16) compressed
17) duplicatePolicy
18) block
19) labels
20) (empty array)
21) sourceKey
22) (nil)
23) rules
24) (empty array)
25) ignoreMaxTimeDiff
26) (integer) 0
27) ignoreMaxValDiff
28) "0"
> TS.DEL thermometer:1 1 2
(integer) 2
> TS.INFO thermometer:1
 1) totalSamples
 2) (integer) 1
 3) memoryUsage
 4) (integer) 4504
 5) firstTimestamp
 6) (integer) 3
 7) lastTimestamp
 8) (integer) 3
 9) retentionTime
10) (integer) 0
11) chunkCount
12) (integer) 1
13) chunkSize
14) (integer) 4096
15) chunkType
16) compressed
17) duplicatePolicy
18) block
19) labels
20) (empty array)
21) sourceKey
22) (nil)
23) rules
24) (empty array)
25) ignoreMaxTimeDiff
26) (integer) 0
27) ignoreMaxValDiff
28) "0"
> TS.DEL thermometer:1 3 3
(integer) 1
> TS.INFO thermometer:1
 1) totalSamples
 2) (integer) 0
 3) memoryUsage
 4) (integer) 4504
 5) firstTimestamp
 6) (integer) 0
 7) lastTimestamp
 8) (integer) 0
 9) retentionTime
10) (integer) 0
11) chunkCount
12) (integer) 1
13) chunkSize
14) (integer) 4096
15) chunkType
16) compressed
17) duplicatePolicy
18) block
19) labels
20) (empty array)
21) sourceKey
22) (nil)
23) rules
24) (empty array)
25) ignoreMaxTimeDiff
26) (integer) 0
27) ignoreMaxValDiff
28) "0"
```

##### C#

```csharp
        // Recreate the thermometer:1 series so this example runs on its own.
        db.KeyDelete("thermometer:1");
        db.TS().Add("thermometer:1", 1, 9.2);
        db.TS().Add("thermometer:1", 2, 9.9);

        TimeSeriesInformation res55 = db.TS().Info("thermometer:1");
        Console.WriteLine(res55.TotalSamples); // >>> 2
        Console.WriteLine(res55.FirstTimeStamp!); // >>> 1
        Console.WriteLine(res55.LastTimeStamp!); // >>> 2

        TimeStamp res56 = db.TS().Add(
            "thermometer:1",
            new TsAddParamsBuilder()
                .AddTimestamp(3)
                .AddValue(9.7)
                .build()
        );
        Console.WriteLine(res56.Value); // >>> 3

        TimeSeriesInformation res57 = db.TS().Info("thermometer:1");
        Console.WriteLine(res57.TotalSamples); // >>> 3
        Console.WriteLine(res57.FirstTimeStamp!); // >>> 1
        Console.WriteLine(res57.LastTimeStamp!); // >>> 3

        long res58 = db.TS().Del("thermometer:1", 1, 2);
        Console.WriteLine(res58); // >>> 2

        TimeSeriesInformation res59 = db.TS().Info("thermometer:1");
        Console.WriteLine(res59.TotalSamples); // >>> 1
        Console.WriteLine(res59.FirstTimeStamp!); // >>> 3
        Console.WriteLine(res59.LastTimeStamp!); // >>> 3

        long res60 = db.TS().Del("thermometer:1", 3, 3);
        Console.WriteLine(res60); // >>> 1

        TimeSeriesInformation res61 = db.TS().Info("thermometer:1");
        Console.WriteLine(res61.TotalSamples); // >>> 0
```

##### Go

```go
	// Recreate the thermometer:1 series so this example runs on its own.
	rdb.Del(ctx, "thermometer:1")
	rdb.TSAdd(ctx, "thermometer:1", 1, 9.2)
	rdb.TSAdd(ctx, "thermometer:1", 2, 9.9)

	res54, err := rdb.TSInfo(ctx, "thermometer:1").Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res54["totalSamples"])   // >>> 2
	fmt.Println(res54["firstTimestamp"]) // >>> 1
	fmt.Println(res54["lastTimestamp"])  // >>> 2

	res55, err := rdb.TSAdd(ctx, "thermometer:1", 3, 9.7).Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res55) // >>> 3

	res56, err := rdb.TSInfo(ctx, "thermometer:1").Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res56["totalSamples"])   // >>> 3
	fmt.Println(res56["firstTimestamp"]) // >>> 1
	fmt.Println(res56["lastTimestamp"])  // >>> 3

	res57, err := rdb.TSDel(ctx, "thermometer:1", 1, 2).Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res57) // >>> 2

	res58, err := rdb.TSInfo(ctx, "thermometer:1").Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res58["totalSamples"])   // >>> 1
	fmt.Println(res58["firstTimestamp"]) // >>> 3
	fmt.Println(res58["lastTimestamp"])  // >>> 3

	res59, err := rdb.TSDel(ctx, "thermometer:1", 3, 3).Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res59) // >>> 1

	res60, err := rdb.TSInfo(ctx, "thermometer:1").Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(res60["totalSamples"]) // >>> 0
```

##### Java (Synchronous - Jedis)

```java
        // Recreate the thermometer:1 series so this example runs on its own.
        jedis.del("thermometer:1");
        jedis.tsAdd("thermometer:1", 1L, 9.2);
        jedis.tsAdd("thermometer:1", 2L, 9.9);

        TSInfo res55 = jedis.tsInfo("thermometer:1");
        System.out.println(res55.getProperty("totalSamples")); // >>> 2
        System.out.println(res55.getProperty("firstTimestamp")); // >>> 1
        System.out.println(res55.getProperty("lastTimestamp")); // >>> 2

        long res56 = jedis.tsAdd("thermometer:1", 3L, 9.7);
        System.out.println(res56); // >>> 3

        TSInfo res57 = jedis.tsInfo("thermometer:1");
        System.out.println(res57.getProperty("totalSamples")); // >>> 3

        long res58 = jedis.tsDel("thermometer:1", 1L, 2L);
        System.out.println(res58); // >>> 2

        TSInfo res59 = jedis.tsInfo("thermometer:1");
        System.out.println(res59.getProperty("totalSamples")); // >>> 1

        long res60 = jedis.tsDel("thermometer:1", 3L, 3L);
        System.out.println(res60); // >>> 1

        TSInfo res61 = jedis.tsInfo("thermometer:1");
        System.out.println(res61.getProperty("totalSamples")); // >>> 0
```

##### JavaScript (Node.js)

```javascript
// Recreate the thermometer:1 series so this example runs on its own.
await client.del('thermometer:1');
await client.ts.add('thermometer:1', 1, 9.2);
await client.ts.add('thermometer:1', 2, 9.9);

const res55 = await client.ts.info('thermometer:1');
console.log(res55.totalSamples); // >>> 2
console.log(res55.firstTimestamp); // >>> 1
console.log(res55.lastTimestamp); // >>> 2

const res56 = await client.ts.add('thermometer:1', 3, 9.7);
console.log(res56); // >>> 3

const res57 = await client.ts.info('thermometer:1');
console.log(res57.totalSamples); // >>> 3
console.log(res57.firstTimestamp); // >>> 1
console.log(res57.lastTimestamp); // >>> 3

const res58 = await client.ts.del('thermometer:1', 1, 2);
console.log(res58); // >>> 2

const res59 = await client.ts.info('thermometer:1');
console.log(res59.totalSamples); // >>> 1
console.log(res59.firstTimestamp); // >>> 3
console.log(res59.lastTimestamp); // >>> 3

const res60 = await client.ts.del('thermometer:1', 3, 3);
console.log(res60); // >>> 1

const res61 = await client.ts.info('thermometer:1');
console.log(res61.totalSamples); // >>> 0
```

##### Python

```python
# Recreate the thermometer:1 series so this example runs on its own.
r.delete("thermometer:1")
r.ts().add("thermometer:1", 1, 9.2)
r.ts().add("thermometer:1", 2, 9.9)

res54 = r.ts().info("thermometer:1")
print(res54.total_samples)  # >>> 2
print(res54.first_timestamp)  # >>> 1
print(res54.last_timestamp)  # >>> 2

res55 = r.ts().add("thermometer:1", 3, 9.7)
print(res55)  # >>> 3

res56 = r.ts().info("thermometer:1")
print(res56.total_samples)  # >>> 3
print(res56.first_timestamp)  # >>> 1
print(res56.last_timestamp)  # >>> 3

res57 = r.ts().delete("thermometer:1", 1, 2)
print(res57)  # >>> 2

res58 = r.ts().info("thermometer:1")
print(res58.total_samples)  # >>> 1
print(res58.first_timestamp)  # >>> 3
print(res58.last_timestamp)  # >>> 3

res59 = r.ts().delete("thermometer:1", 3, 3)
print(res59)  # >>> 1

res60 = r.ts().info("thermometer:1")
print(res60.total_samples)  # >>> 0
```



## Use time series with other metrics tools

In the [RedisTimeSeries](https://github.com/RedisTimeSeries) GitHub organization, you can
find projects that help you integrate RedisTimeSeries with other tools, including:

1. [Prometheus](https://github.com/RedisTimeSeries/prometheus-redistimeseries-adapter), a read/write adapter to use RedisTimeSeries as the backend database.
2. [Grafana 7.1+](https://github.com/RedisTimeSeries/grafana-redis-datasource), using the [Redis Data Source](https://redislabs.com/blog/introducing-the-redis-data-source-plug-in-for-grafana/).
3. [Telegraf](https://github.com/influxdata/telegraf). Download the plugin from [InfluxData](https://portal.influxdata.com/downloads/). 
4. StatsD, Graphite exports using graphite protocol.

## More information

The other pages in this section describe RedisTimeSeries concepts in more detail.
See also the [time series command reference](/commands/?group=timeseries).

