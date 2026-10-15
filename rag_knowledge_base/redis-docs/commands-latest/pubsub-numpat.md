# PUBSUB NUMPAT

```json metadata
{
  "schema_version": 2,
  "title": "PUBSUB NUMPAT",
  "description": "Returns a count of unique pattern subscriptions.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "PUBSUB NUMPAT",
  "complexity": "O(1)",
  "group": "pubsub",
  "command_flags": ["pubsub","loading","stale"],
  "acl_categories": ["@pubsub","@slow"],
  "since": "2.8.0",
  "arity": 2,
  "tableOfContents": {"sections":[{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Returns the number of unique patterns that are subscribed to by clients (that are performed using the [`PSUBSCRIBE`](https://redis.io/docs/latest/commands/psubscribe) command).

Note that this isn't the count of clients subscribed to patterns, but the total number of unique patterns all the clients are subscribed to.

Cluster note: in a Redis Cluster clients can subscribe to every node, and can also publish to every other node. The cluster will make sure that published messages are forwarded as needed. That said, [`PUBSUB`](https://redis.io/docs/latest/commands/pubsub)'s replies in a cluster only report information from the node's Pub/Sub context, rather than the entire cluster.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Integer reply](../../develop/reference/protocol-spec#integers): the number of patterns all the clients are subscribed to.

**RESP3:**

[Integer reply](../../develop/reference/protocol-spec#integers): the number of patterns all the clients are subscribed to.



