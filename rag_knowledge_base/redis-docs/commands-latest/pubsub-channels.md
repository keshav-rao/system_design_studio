# PUBSUB CHANNELS

```json metadata
{
  "schema_version": 2,
  "title": "PUBSUB CHANNELS",
  "description": "Returns the active channels.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"pattern","name":"pattern","optional":true,"type":"pattern"}],
  "syntax_fmt": "PUBSUB CHANNELS [pattern]",
  "complexity": "O(N) where N is the number of active channels, and assuming constant time pattern matching (relatively short channels and patterns)",
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

Lists the currently active Pub/Sub channels.

An active channel is a Pub/Sub channel with one or more subscribers (excluding clients subscribed to patterns).

If no `pattern` is specified, all the channels are listed, otherwise if pattern is specified only channels matching the specified glob-style pattern are listed.

Cluster note: in a Redis Cluster, clients can subscribe to every node and can also publish to every other node. The cluster will make sure that published messages are forwarded as needed. That said, [`PUBSUB`](https://redis.io/docs/latest/commands/pubsub)'s replies in a cluster only report information from the node's Pub/Sub context, rather than the entire cluster.

## Optional arguments

<details open><summary><code>pattern</code></summary>

List only active channels whose names match the given glob-style pattern. If omitted, all active channels are listed.

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Array reply](../../develop/reference/protocol-spec#arrays): a list of active channels, optionally matching the specified pattern.

**RESP3:**

[Array reply](../../develop/reference/protocol-spec#arrays): a list of active channels, optionally matching the specified pattern.



