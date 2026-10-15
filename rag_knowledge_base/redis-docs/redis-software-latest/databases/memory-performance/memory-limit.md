# Database memory limits

```json metadata
{
  "schema_version": 2,
  "title": "Database memory limits",
  "description": "When you set a database's memory limit, you define the maximum size the database can reach.",
  "categories": ["docs","operate","rs","rc"],
  "tableOfContents": {"sections":[{"id":"factors-for-sizing","title":"Factors for sizing"},{"children":[{"id":"order-of-events-for-low-ram","title":"Order of events for low RAM"},{"id":"active-active-replication-oom-protection","title":"Active-Active replication OOM protection"}],"id":"what-happens-when-redis-software-is-low-on-ram","title":"What happens when Redis Software is low on RAM?"},{"id":"adaptive-memory-allocation","title":"Adaptive memory allocation"},{"children":[{"id":"resharding-overview","title":"Resharding overview"},{"id":"resharding-duration-factors-1","title":"Resharding duration factors"}],"id":"resharding-duration-factors","title":"Resharding duration factors"},{"id":"memory-metrics","title":"Memory metrics"},{"id":"related-info","title":"Related info"}]}

,
  "codeExamples": []
}
```

When you set a database's memory limit, you define the maximum size the
database can reach in the cluster, across all database replicas and
shards, including both primary and replica shards.

If the total size of the database in the cluster reaches the memory
limit, the data eviction policy is
applied.

## Factors for sizing

Factors to consider when sizing your database:

- **dataset size**: you want your limit to be above your dataset size to leave room for overhead.
- **database throughput**: high throughput needs more shards, leading to a higher memory limit.
- [**modules**](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise): using modules with your database consumes more memory.
- [**database clustering**](https://redis.io/docs/latest/operate/rs/databases/durability-ha/clustering): enables you to spread your data into shards across multiple nodes.
- [**database replication**](https://redis.io/docs/latest/operate/rs/databases/durability-ha/replication): enabling replication doubles memory consumption.

Additional factors for Active-Active databases:

- [**Active-Active replication**](https://redis.io/docs/latest/operate/rs/databases/active-active): enabling Active-Active replication requires double the memory of regular replication, which can be up to two times (2x) the original data size per instance.
- [**database replication backlog**](https://redis.io/docs/latest/operate/rs/databases/active-active/manage#replication-backlog/) for synchronization between shards. By default, this is set to 1% of the database size.
- [**Active-Active replication backlog**](https://redis.io/docs/latest/operate/rs/databases/active-active/manage) for synchronization between clusters. By default, this is set to 1% of the database size.

  It's also important to know Active-Active databases have a lower threshold for activating the eviction policy, because it requires propagation to all participating clusters. The eviction policy starts to evict keys when one of the Active-Active instances reaches 80% of its memory limit.

Additional factors for databases with flash enabled:

- For [Auto Tiering](https://redis.io/docs/latest/operate/rs/databases/flash), the available flash space must be greater than or equal to the total database size (RAM+Flash). The extra space accounts for write buffers and [write amplification](https://en.wikipedia.org/wiki/Write_amplification).

- For [Flex](https://redis.io/docs/latest/operate/rs/flex), flash space should be approximately three times the total memory limit of all Flex databases on the node. Because you can increase a database's memory limit after creation, size flash space for the expected peak memory limit.

- [**database persistence**](https://redis.io/docs/latest/operate/rs/databases/configure/database-persistence): Auto Tiering uses dual database persistence where both the primary and replica shards persist to disk. This may add some processor and network overhead, especially in cloud configurations with network attached storage.

## What happens when Redis Software is low on RAM?

Redis Software manages node memory so that data is entirely in RAM (unless using Auto Tiering). If not enough RAM is available, Redis Software prevents adding more data into the databases.

Redis Software protects the existing data and prevents the database from being able to store data into the shards.

You can configure the cluster to move the data to another node, or even discard it according to the [eviction policy](https://redis.io/docs/latest/operate/rs/databases/memory-performance/eviction-policy) set on each database by the administrator.

[Redis Flex and Auto Tiering](https://redis.io/docs/latest/operate/rs/databases/flash)
manage memory so that you can also use flash memory (SSD) to store data.

### Order of events for low RAM

1. If there are other nodes available, your shards migrate to other nodes.
2. If the eviction policy allows eviction, shards start to release memory,
which can result in data loss.
3. If the eviction policy does not allow eviction, you'll receive
out of memory (OOM) messages.
4. If shards can't free memory, Redis Software relies on the OS processes to stop replicas,
but tries to avoid stopping primary shards.

We recommend that you have a [monitoring platform](https://redis.io/docs/latest/operate/rs/monitoring) that alerts you before a system gets low on RAM.
You must maintain sufficient free memory to make sure that you have a healthy Redis Software installation.

### Active-Active replication OOM protection

When a shard in an Active-Active database reaches an out-of-memory (OOM) condition:

1. Replication between that shard and its peers stops immediately.

1. The syncer process sends commands to the affected shard to trigger garbage collection and free memory.

If the database has no [eviction policy](https://redis.io/docs/latest/operate/rs/databases/memory-performance/eviction-policy) and no keys with [expiration times (TTL)](https://redis.io/docs/latest/develop/using-commands/keyspace#key-expiration), no memory can be freed, which can lead to persistent replication failure and data desynchronization.

To reduce this risk, Active-Active databases running Redis version 8.4 or later support a configurable memory buffer through the `replication_oom_threshold_percent` setting. This setting reserves a percentage of memory below `maxmemory` for internal replication operations.

The `replication_oom_threshold_percent` setting works as follows:

- If memory usage is below the threshold, all client writes proceed normally.

- If memory usage exceeds the threshold, Redis blocks external client write commands with an out-of-memory error, but internal replication and garbage collection continue in the reserved buffer.

- If memory reaches `maxmemory` despite the client block, the standard out-of-memory behavior applies to all operations, including replication.

`replication_oom_threshold_percent` defaults to `5`, which means 5% of `maxmemory` is reserved. To adjust the reserved percentage in all participating clusters, use an [update Active-Active database configuration](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/crdbs#patch-crdbs) REST API request:

```sh
PATCH https://<host>:<port>/v1/crdbs/<crdb_guid>
{ 
  "default_db_config": { 
    "replication_oom_threshold_percent": <integer from 0 to 20> 
  }
}
```

## Adaptive memory allocation

In rare cases during high-velocity data ingestion, databases can temporarily reach up to 200% of their configured memory limit. This adaptive memory allocation strategy allows large amounts of data to be written to the database quickly without rejecting valid transactions.

For example, when pushing data at approximately 100 MB/sec into a 2 GB database:
- A database with 2 shards could reach 199% of its configured memory limit.
- A database with 4 shards could reach around 220% of its configured memory limit.

Databases should return to their configured memory limits after data is removed according to the [eviction policy](https://redis.io/docs/latest/operate/rs/databases/memory-performance/eviction-policy) and [time-to-live (TTL)](https://redis.io/docs/latest/develop/using-commands/keyspace#key-expiration).

If you observe this behavior, consider [monitoring](https://redis.io/docs/latest/operate/rs/monitoring) memory usage and controlling the traffic load on the application side.

## Resharding duration factors

Resharding enables you to increase database capacity by adding shards and utilizing more cluster memory. Understanding resharding duration helps you plan maintenance operations and minimize database risk.

### Resharding overview

Resharding follows a three-stage process for each new shard:

1. **Shard creation**: Creates a new shard and performs partial synchronization based on assigned hash slots
2. **Key trimming**: Removes keys from the original shard according to new hash slot assignments
3. **Defragmentation**: Executes failovers to optimize new shard performance

When resharding multiple shards (for example, expanding from 4 to 8 shards), this process runs serially for each new shard. The operation completes only after all stages finish for every shard.

> [!NOTE]
> Resharding is an atomic operation that cannot be interrupted. Database corruption can occur if the process fails or stops unexpectedly. Minimizing resharding time reduces this risk.

### Resharding duration factors

Resharding duration increases linearly with the number of keys in your database. Key length and network traffic affect resharding duration:

Key length directly affects resharding duration. Longer keys (2000 KB) require more time to process due to increased hash calculation overhead per key compared to short keys (10 bytes). 

Network traffic has a measurable but limited effect on resharding duration. Since resharding operations typically don't reach CPU limits, the impact on both resharding time and ongoing traffic remains minimal.

## Memory metrics

The Cluster Manager UI provides metrics that can help you evaluate your memory use.

- Free RAM
- RAM fragmentation
- Used memory
- Memory usage
- Memory limit

See [console metrics](https://redis.io/docs/latest/operate/rs/references/metrics) for more detailed information.

## Related info

- [Memory and performance](https://redis.io/docs/latest/operate/rs/databases/memory-performance)
- [Disk sizing for heavy write scenarios](https://redis.io/docs/latest/operate/rs/clusters/optimize/disk-sizing-heavy-write-scenarios)
- [Turn off services to free system memory](https://redis.io/docs/latest/operate/rs/clusters/optimize/turn-off-services)
- [Eviction policy](https://redis.io/docs/latest/operate/rs/databases/memory-performance/eviction-policy)
- [Shard placement policy](https://redis.io/docs/latest/operate/rs/databases/memory-performance/shard-placement-policy)
- [Database persistence](https://redis.io/docs/latest/operate/rs/databases/configure/database-persistence)

