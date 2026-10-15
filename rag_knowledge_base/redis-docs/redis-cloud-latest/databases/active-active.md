# Active-Active Redis

```json metadata
{
  "schema_version": 2,
  "title": "Active-Active Redis",
  "description": "Overview of the Active-Active feature for Redis Cloud.",
  "categories": ["docs","operate","rc"],
  "tableOfContents": {"sections":[{"children":[{"id":"multi-zone","title":"Multi-zone"},{"id":"local-latency-with-unique-endpoints","title":"Local latency with unique endpoints"},{"id":"conflict-resolution","title":"Conflict resolution"},{"id":"failover-handling","title":"Failover handling"}],"id":"active-active-geo-distributed-replication-highlights","title":"Active-Active geo-distributed replication highlights"},{"id":"sizing-and-memory","title":"Sizing and memory"}]}

,
  "codeExamples": []
}
```


Active-Active databases store data across multiple regions and availability zones.  This improves scalability, performance, and availability, especially when compared to standalone databases.

To create Active-Active databases, you need a Redis Cloud Pro subscription that enables Active-Active Redis and defines the regions for each copy of your databases. See [Create an Active-Active database](https://redis.io/docs/latest/operate/rc/databases/active-active/create-active-active-database) for instructions.

Active-Active databases are distributed across multiple regions (geo-distribution).  This improves performance by reducing latency for nearby users and improves availability by protecting against data loss in case of network or resource failure.

Active-Active databases allow read and write operations in each copy.  Each copy eventually reflects changes made in other copies ([eventual consistency](https://redis.io/docs/latest/glossary#eventual-consistency)).  Conflict-free replicated data types (CRDTs) synchronize read and write operations between copies.  CRDTs ensure consistency and resolve conflicts.

Active-Active databases use TLS to synchronize data between regions.  You can also use TLS to encrypt client connections.  See [Transport Layer Security (TLS)](https://redis.io/docs/latest/operate/rc/security/database-security/tls-ssl) for more information.

When developing for Active-Active databases, you need to consider some important differences. See [Develop applications with Active-Active databases](https://redis.io/docs/latest/operate/rc/databases/active-active/develop) for related information.

> [!NOTE]
> Active-Active subscriptions on Redis Cloud are limited to a maximum of 10 regions and 10 databases.

## Active-Active geo-distributed replication highlights

### Multi-zone

Geo-distributed replication maintains copies of both primary and replica shards in multiple clusters. These clusters can be spread across multiple availability zones. Active-Active Redis uses zone awareness to spread your primary and replica shards across zones, which helps protect against data loss from regional outages.

The availability of each region depends on the number of availability zones it provides:

- Regions with three or more availability zones use multi-zone replication and provide **99.999%** (five-nines) availability.
- Regions with fewer than three availability zones use single-zone replication and provide **99.99%** (four-nines) availability.

An Active-Active database can combine regions with different availability zone counts. When it does, the availability of the entire deployment is determined by the least resilient region. For example, an Active-Active database that spans a region with three availability zones and a region with fewer than three availability zones provides 99.99% (four-nines) availability overall.

> [!NOTE]
> Regions with fewer than three availability zones are not available when you create an Active-Active database in the Redis Cloud console. To create an Active-Active database that includes one of these regions, use the [Redis Cloud REST API](https://redis.io/docs/latest/operate/rc/api). You'll be able to manage these databases using the Redis Cloud console after they're created.

### Local latency with unique endpoints

Applications can connect to a specific copy of an Active-Active database using its unique endpoint. For local latency, configure your application to use a database endpoint in the closest region.

### Conflict resolution

Active-Active databases use special data types called conflict-free replicated data types (CRDT). These automatically resolve conflicts that occur when writes are made to different clusters at the same time.

### Failover handling

After a failure at the process, node, or zone level, Active-Active databases automatically promote replica shards to replace failed primaries, copy data to new replica shards, and migrate shards to new nodes as needed. This reduces downtime and makes the most of your computing resources, even in the event of a failure.  

However, Active-Active databases do not have a built-in [failover](https://en.wikipedia.org/wiki/Failover) or failback mechanism for application connections. To handle cluster-level failures, you should implement one of the following disaster recovery strategies to redirect traffic between regions:

- [Network-based](https://redis.io/docs/latest/operate/rs/databases/active-active/disaster-recovery/network-based): Global traffic managers and load balancers for routing.

- [Proxy-based](https://redis.io/docs/latest/operate/rs/databases/active-active/disaster-recovery/proxy-based): Software proxies handle detection and routing logic.

- [Client library-based](https://redis.io/docs/latest/operate/rs/databases/active-active/disaster-recovery/client-library-based): Database client libraries with built-in failover logic.

- [Application-based](/operate/rc/databases/active-active/develop/app-failover-active-active): Custom application-level monitoring and connectivity management.

For more information and guidance on which disaster recovery strategy to implement, see [Disaster recovery strategies for Active-Active databases](https://redis.io/docs/latest/operate/rs/databases/active-active/disaster-recovery).

Data automatically syncs to a recovered cluster when it returns to a healthy state.

## Sizing and memory

Active-Active databases consume more memory than standalone databases. Because Active-Active requires replication, and Active-Active replication doubles memory consumption on top of that, the memory limit impact can be as large as four times (4x) the original data size.

Active-Active databases also begin evicting keys earlier than standalone databases, at 80% of an instance's memory limit, and reserve additional memory for replication backlogs. Account for these factors when you size your database.

For more information, see [Memory limits and sizing](https://redis.io/docs/latest/operate/rc/databases/configuration/sizing#dataset-size).

