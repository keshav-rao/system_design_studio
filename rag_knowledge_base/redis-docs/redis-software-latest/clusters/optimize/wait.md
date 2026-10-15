# Use the WAIT command to improve data safety and durability

```json metadata
{
  "schema_version": 2,
  "title": "Use the WAIT command to improve data safety and durability",
  "description": "Use the wait command to take full advantage of Redis Software's replication-based durability.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"id":"non-blocking-redis-write-operation","title":"Non-blocking Redis write operation"},{"id":"blocking-write-operation-on-replication","title":"Blocking write operation on replication"}]}

,
  "codeExamples": []
}
```

Redis Software comes with the ability to replicate data
to another replica for high availability and persist in-memory data on
disk permanently for durability. With the [`WAIT`](https://redis.io/docs/latest/commands/wait) command, you can
control the consistency and durability guarantees for the replicated and
persisted database.

## Non-blocking Redis write operation

Any updates that are issued to the database are typically performed with the following flow:

1. Application issues a write.
1. Proxy communicates with the correct primary shard in the system that contains the given key.
1. The acknowledgment is sent to proxy after the write operation completes.
1. The proxy sends the acknowledgment back to the application.

Independently, the write is communicated from the primary shard to the replica, and
replication acknowledges the write back to the primary shard. These are steps 5 and 6.

Independently, the write to a replica is also persisted to disk and
acknowledged within the replica. These are steps 7 and 8.

![](https://redis.io/docs/latest/images/rs/weak-consistency.png)

## Blocking write operation on replication

With the [`WAIT`](https://redis.io/docs/latest/commands/wait) or [`WAITAOF`](https://redis.io/docs/latest/commands/waitaof) commands, applications can ask to wait for
acknowledgments only after replication or persistence is confirmed on
the replica. The flow of a write operation with `WAIT` or `WAITAOF` is:

1. The application issues a write.
1. The proxy communicates with the correct primary shard in the system that contains the given key.
1. Replication communicates the update to the replica shard.
1. If using `WAITAOF` and the AOF every write setting, the replica persists the update to disk before sending the acknowledgment.
1. The acknowledgment is sent back from the replica all the way to the proxy with steps 5 to 8.

The application only gets the acknowledgment from the write after durability is achieved with replication to the replica for `WAIT` or `WAITAOF` and to the persistent storage for `WAITAOF` only.

![](https://redis.io/docs/latest/images/rs/strong-consistency.png)

The `WAIT` command always returns the number of replicas that acknowledged the write commands sent by the current client before the `WAIT` command, both in the case where the specified number of replicas are reached, or when the timeout is reached. In Redis Software, the number of replicas is always 1 for databases with high availability enabled.

See the [`WAITAOF`](https://redis.io/docs/latest/commands/waitaof) command for details for enhanced data safety and durability capabilities introduced with Redis 7.2.

