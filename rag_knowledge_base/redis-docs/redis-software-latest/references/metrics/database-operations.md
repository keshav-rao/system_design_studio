# Database operations metrics

```json metadata
{
  "schema_version": 2,
  "title": "Database operations metrics",
  "description": "",
  "categories": ["docs","operate","rs","rc"],
  "tableOfContents": {"sections":[{"id":"evicted-objectssec","title":"Evicted objects/sec"},{"id":"expired-objectssec","title":"Expired objects/sec"},{"children":[{"id":"read-missessec","title":"Read misses/sec"},{"id":"write-missessec","title":"Write misses/sec"}],"id":"hit-ratio","title":"Hit ratio"},{"children":[{"id":"reads-latency","title":"Reads latency"},{"id":"writes-latency","title":"Writes latency"},{"id":"other-commands-latency","title":"Other commands latency"}],"id":"latency","title":"Latency"},{"children":[{"id":"readssec","title":"Reads/sec"},{"id":"writessec","title":"Writes/sec"},{"id":"other-commandssec","title":"Other commands/sec"}],"id":"opssec","title":"Ops/sec"},{"id":"total-keys","title":"Total keys"}]}

,
  "codeExamples": []
}
```


The following metrics are available in the Redis Software Cluster Manager UI.

![The database metrics page.](https://redis.io/docs/latest/images/rs/screenshots/metrics/db-metrics.png)

## Evicted objects/sec

Number of objects evicted from the database per second.

Objects are evicted from the database according to the [eviction policy](https://redis.io/docs/latest/operate/rs/databases/memory-performance/eviction-policy).

Object information is not measured during [shard migration](https://redis.io/docs/latest/operate/rs/databases/configure/replica-ha).

**Components measured**: Database and Shard

## Expired objects/sec

Number of expired objects per second.

Object information is not measured during [shard migration](https://redis.io/docs/latest/operate/rs/databases/configure/replica-ha).

**Components measured**: Database and Shard

## Hit ratio 

Ratio of the number of operations on existing keys out of the total number of operations. 

**Components measured**: Database and Shard

### Read misses/sec

The number of [read operations](#readssec) per second on keys that do not exist.

Read misses are not measured during [shard migration](https://redis.io/docs/latest/operate/rs/databases/configure/replica-ha).

**Components measured**: Database

### Write misses/sec 

Number of [write operations](#writessec) per second on keys that do not exist.

Write misses are not measured during [shard migration](https://redis.io/docs/latest/operate/rs/databases/configure/replica-ha).

**Components measured**: Database and Shard

## Latency 

The total amount of time between sending a Redis operation and receiving a response from the database.

The graph shows average, minimum, maximum, and last latency values for all latency metrics.

**Components measured**: Database

### Reads latency 

[Latency](#latency) of [read operations](#readssec).

**Components measured**: Database

### Writes latency 

[Latency](#latency) per [write operation](#writessec).

**Components measured**: Database

### Other commands latency 

[Latency](#latency) of [other operations](#other-commandssec).

**Components measured**: Database

## Ops/sec

Number of total operations per second, which includes [read operations](#readssec), [write operations](#writessec), and [other operations](#other-commandssec).

**Components measured**: Cluster, Node, Database, and Shard

### Reads/sec

Number of total read operations per second.

To find out which commands are read operations, run the following command with [`redis-cli`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/redis-cli):

```sh
ACL CAT read
```

**Components measured**: Database

### Writes/sec

Number of total write operations per second.

To find out which commands are write operations, run the following command with [`redis-cli`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/redis-cli):

```sh
ACL CAT write
```

**Components measured**: Database

#### Pending writes min

Minimum number of write operations queued per [Active-Active](https://redis.io/docs/latest/operate/rs/databases/active-active) replica database. 

#### Pending writes max

Maximum number of write operations queued per [Active-Active](https://redis.io/docs/latest/operate/rs/databases/active-active) replica database. 

### Other commands/sec 

Number of operations per second that are not [read operations](#readssec) or [write operations](#writessec).

Examples of other operations include [PING](https://redis.io/docs/latest/commands/ping), [AUTH](https://redis.io/docs/latest/commands/auth), and [INFO](https://redis.io/docs/latest/commands/info).

**Components measured**: Database

## Total keys 

Total number of keys in the dataset.
 
Does not include replicated keys, even if [replication](https://redis.io/docs/latest/operate/rs/databases/durability-ha/replication) is enabled.

Total keys is not measured during [shard migration](https://redis.io/docs/latest/operate/rs/databases/configure/replica-ha). 

**Components measured**: Database









