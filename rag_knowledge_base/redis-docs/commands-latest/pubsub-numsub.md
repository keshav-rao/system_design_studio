# PUBSUB NUMSUB

```json metadata
{
  "schema_version": 2,
  "title": "PUBSUB NUMSUB",
  "description": "Returns a count of subscribers to channels.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"channel","multiple":true,"name":"channel","optional":true,"type":"string"}],
  "syntax_fmt": "PUBSUB NUMSUB [channel [channel ...]]",
  "complexity": "O(N) for the NUMSUB subcommand, where N is the number of requested channels",
  "group": "pubsub",
  "command_flags": ["pubsub","loading","stale"],
  "acl_categories": ["@pubsub","@slow"],
  "since": "2.8.0",
  "arity": -2,
  "tableOfContents": {"sections":[{"id":"optional-arguments","title":"Optional arguments"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Returns the number of subscribers (exclusive of clients subscribed to patterns) for the specified channels.

Note that it is valid to call this command without channels. In this case it will just return an empty list.

Cluster note: in a Redis Cluster, clients can subscribe to every node, and can also publish to every other node. The cluster will make sure that published messages are forwarded as needed. That said, [`PUBSUB`](https://redis.io/docs/latest/commands/pubsub)'s replies in a cluster only report information from the node's Pub/Sub context, rather than the entire cluster.

## Optional arguments

<details open><summary><code>channel [channel ...]</code></summary>

One or more channels to report the subscriber count for.

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Array reply](../../develop/reference/protocol-spec#arrays): the number of subscribers per channel, each even element (including the 0th) is channel name, each odd element is the number of subscribers

**RESP3:**

[Array reply](../../develop/reference/protocol-spec#arrays): the number of subscribers per channel, each even element (including the 0th) is channel name, each odd element is the number of subscribers



