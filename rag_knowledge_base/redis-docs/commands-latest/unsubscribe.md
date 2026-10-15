# UNSUBSCRIBE

```json metadata
{
  "schema_version": 2,
  "title": "UNSUBSCRIBE",
  "description": "Stops listening to messages posted to channels.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"channel","multiple":true,"name":"channel","optional":true,"type":"string"}],
  "syntax_fmt": "UNSUBSCRIBE [channel [channel ...]]",
  "complexity": "O(N) where N is the number of channels to unsubscribe.",
  "group": "pubsub",
  "command_flags": ["pubsub","noscript","loading","stale"],
  "acl_categories": ["@pubsub","@slow"],
  "since": "2.0.0",
  "arity": -1,
  "tableOfContents": {"sections":[{"id":"optional-arguments","title":"Optional arguments"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```


Unsubscribes the client from the specified channels, or from all channels if none are specified.

If you don’t specify any channels, the client unsubscribes from all previously subscribed channels. The client receives one message for each channel it unsubscribes from.

## Optional arguments

<details open><summary><code>channel [channel ...]</code></summary>

One or more channels to unsubscribe from. If omitted, the client is unsubscribed from all channels.

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

When successful, this command doesn't return anything. Instead, for each channel, one message with the first element being the string `unsubscribe` is pushed as a confirmation that the command succeeded.

**RESP3:**

When successful, this command doesn't return anything. Instead, for each channel, one message with the first element being the string `unsubscribe` is pushed as a confirmation that the command succeeded.



