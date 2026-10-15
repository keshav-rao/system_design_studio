# PUBSUB SHARDCHANNELS

```json metadata
{
  "schema_version": 2,
  "title": "PUBSUB SHARDCHANNELS",
  "description": "Returns the active shard channels.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"pattern","name":"pattern","optional":true,"type":"pattern"}],
  "syntax_fmt": "PUBSUB SHARDCHANNELS [pattern]",
  "complexity": "O(N) where N is the number of active shard channels, and assuming constant time pattern matching (relatively short shard channels).",
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

Lists the currently active shard channels.

An active shard channel is a Pub/Sub shard channel with one or more subscribers.

If no `pattern` is specified, all the channels are listed, otherwise if pattern is specified, only channels matching the specified glob-style pattern are listed.

The information returned about the active shard channels are at the shard level and not at the cluster level.

## Optional arguments

<details open><summary><code>pattern</code></summary>

List only active shard channels whose names match the given glob-style pattern. If omitted, all active shard channels are listed.

</details>

## Examples

```
> PUBSUB SHARDCHANNELS
1) "orders"
> PUBSUB SHARDCHANNELS o*
1) "orders"
```

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Array reply](../../develop/reference/protocol-spec#arrays): a list of active channels, optionally matching the specified pattern.

**RESP3:**

[Array reply](../../develop/reference/protocol-spec#arrays): a list of active channels, optionally matching the specified pattern.



