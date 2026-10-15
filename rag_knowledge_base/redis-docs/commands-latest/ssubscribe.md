# SSUBSCRIBE

```json metadata
{
  "schema_version": 2,
  "title": "SSUBSCRIBE",
  "description": "Listens for messages published to shard channels.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"shardchannel","multiple":true,"name":"shardchannel","type":"string"}],
  "syntax_fmt": "SSUBSCRIBE shardchannel [shardchannel ...]",
  "complexity": "O(N) where N is the number of shard channels to subscribe to.",
  "group": "pubsub",
  "command_flags": ["pubsub","noscript","loading","stale"],
  "acl_categories": ["@pubsub","@slow"],
  "since": "7.0.0",
  "arity": -2,
  "key_specs": [{"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":-1,"limit":0},"type":"range"},"not_key":true}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Subscribes the client to the specified shard channels.

In Redis Cluster, shard channels are assigned to slots with the same algorithm Redis uses to assign keys to slots. To receive messages published to a shard channel, subscribe to a node, either a primary or replica, that serves the channel’s slot.

All shard channels in a single SSUBSCRIBE call must belong to the same slot. To subscribe to shard channels across different slots, use separate SSUBSCRIBE calls.

For more information about sharded Pub/Sub, see [Sharded Pub/Sub](https://redis.io/docs/latest/develop/pubsub#sharded-pubsub).

## Required arguments

<details open><summary><code>shardchannel [shardchannel ...]</code></summary>

One or more shard channels to subscribe to.

</details>

## Examples

```
> ssubscribe orders
Reading messages... (press Ctrl-C to quit)
1) "ssubscribe"
2) "orders"
3) (integer) 1
1) "smessage"
2) "orders"
3) "hello"
```

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

When successful, this command doesn't return anything. Instead, for each shard channel, one message with the first element being the string `ssubscribe` is pushed as a confirmation that the command succeeded. Note that this command can also return a -MOVED redirect.

**RESP3:**

When successful, this command doesn't return anything. Instead, for each shard channel, one message with the first element being the string 'ssubscribe' is pushed as a confirmation that the command succeeded. Note that this command can also return a -MOVED redirect.



