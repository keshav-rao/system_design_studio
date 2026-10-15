# Client library-based disaster recovery

```json metadata
{
  "schema_version": 2,
  "title": "Client library-based disaster recovery",
  "description": "Client library-based disaster recovery for Active-Active databases using Redis client libraries with built-in failover logic.",
  "categories": ["docs","operate","rs","rc"],
  "tableOfContents": {"sections":[]}

,
  "codeExamples": []
}
```


Some Redis client libraries support geographic failover and failback. These client libraries monitor all Active-Active database members and instantiate connections for all endpoints in advance to allow faster failover and failback.

Advantages:

- No additional hardware or software components required.

- No high availability considerations.

- No scalability concerns.

- Tighter control over connectivity, such as timeouts, connection retries, and dynamic reconfiguration.

- OSS Cluster API support (currently only available in redis-py)

- Low latency.

Considerations:

- Requires code changes for failover and failback logic.

- Concurrent access across replicas is possible, but can be mitigated using the distributed health status provided by the database availability API requests.

- When a development framework uses Redis transparently, failover and failback might not be easy to configure.

The following diagram shows a client library-based disaster recovery approach:

![Diagram of client libraries routing traffic to Active-Active database members](https://redis.io/docs/latest/images/active-active-disaster-recovery/client-library.svg)

The following diagram shows a client-based disaster recovery approach that also uses [connection pooling](https://redis.io/docs/latest/develop/clients/pools-and-muxing#connection-pooling):

![Diagram of client libraries with connection pooling routing traffic to Active-Active database members](https://redis.io/docs/latest/images/active-active-disaster-recovery/client-library-connection-pool.svg)

For additional information, see the the introduction to
[Client-side geographic failover](https://redis.io/docs/latest/develop/clients/failover)
and also the following client library guides for failover and failback:

- [Jedis (Java)](https://redis.io/docs/latest/develop/clients/jedis/failover)

- [Lettuce (Java)](https://redis.io/docs/latest/develop/clients/lettuce/failover)

- [redis-py (Python)](https://redis.io/docs/latest/develop/clients/redis-py/failover)


