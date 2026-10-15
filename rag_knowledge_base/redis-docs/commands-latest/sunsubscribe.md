# SUNSUBSCRIBE

```json metadata
{
  "schema_version": 2,
  "title": "SUNSUBSCRIBE",
  "description": "Stops listening to messages posted to shard channels.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"shardchannel","multiple":true,"name":"shardchannel","optional":true,"type":"string"}],
  "syntax_fmt": "SUNSUBSCRIBE [shardchannel [shardchannel ...]]",
  "complexity": "O(N) where N is the number of shard channels to unsubscribe.",
  "group": "pubsub",
  "command_flags": ["pubsub","noscript","loading","stale"],
  "acl_categories": ["@pubsub","@slow"],
  "since": "7.0.0",
  "arity": -1,
  "key_specs": [{"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":-1,"limit":0},"type":"range"},"not_key":true}],
  "tableOfContents": {"sections":[{"id":"optional-arguments","title":"Optional arguments"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Unsubscribes the client from the specified patterns, or from all patterns if none are specified.

If you don’t specify any shard channels, the client unsubscribes from all previously subscribed shard channels. The client receives one message for each shard channel it unsubscribes from.

Note: global channels and shard channels need to be unsubscribed from separately.

For more information about sharded Pub/Sub, see [Sharded Pub/Sub](https://redis.io/docs/latest/develop/pubsub#sharded-pubsub).

## Optional arguments

<details open><summary><code>shardchannel [shardchannel ...]</code></summary>

One or more shard channels to unsubscribe from. If omitted, the client is unsubscribed from all shard channels.

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

When successful, this command doesn't return anything. Instead, for each shard channel, one message with the first element being the string `sunsubscribe` is pushed as a confirmation that the command succeeded.

**RESP3:**

When successful, this command doesn't return anything. Instead, for each shard channel, one message with the first element being the string `sunsubscribe` is pushed as a confirmation that the command succeeded.



