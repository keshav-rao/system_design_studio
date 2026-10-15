# PUBSUB SHARDNUMSUB

```json metadata
{
  "schema_version": 2,
  "title": "PUBSUB SHARDNUMSUB",
  "description": "Returns the count of subscribers of shard channels.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"shardchannel","multiple":true,"name":"shardchannel","optional":true,"type":"string"}],
  "syntax_fmt": "PUBSUB SHARDNUMSUB [shardchannel [shardchannel ...]]",
  "complexity": "O(N) for the SHARDNUMSUB subcommand, where N is the number of requested shard channels",
  "group": "pubsub",
  "command_flags": ["pubsub","loading","stale"],
  "acl_categories": ["@pubsub","@slow"],
  "since": "7.0.0",
  "arity": -2,
  "tableOfContents": {"sections":[{"id":"optional-arguments","title":"Optional arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Returns the number of subscribers for the specified shard channels.

Note that it is valid to call this command without channels, in this case it will just return an empty list.

Cluster note: in a Redis Cluster, [`PUBSUB`](https://redis.io/docs/latest/commands/pubsub)'s replies in a cluster only report information from the node's Pub/Sub context, rather than the entire cluster.

## Optional arguments

<details open><summary><code>shardchannel [shardchannel ...]</code></summary>

One or more shard channels to report the subscriber count for.

</details>

## Examples

```
> PUBSUB SHARDNUMSUB orders
1) "orders"
2) (integer) 1
```

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Array reply](../../develop/reference/protocol-spec#arrays): the number of subscribers per shard channel, each even element (including the 0th) is channel name, each odd element is the number of subscribers.

**RESP3:**

[Array reply](../../develop/reference/protocol-spec#arrays): the number of subscribers per shard channel, each even element (including the 0th) is channel name, each odd element is the number of subscribers.



