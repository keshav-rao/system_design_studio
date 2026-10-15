# PUNSUBSCRIBE

```json metadata
{
  "schema_version": 2,
  "title": "PUNSUBSCRIBE",
  "description": "Stops listening to messages published to channels that match one or more patterns.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"pattern","multiple":true,"name":"pattern","optional":true,"type":"pattern"}],
  "syntax_fmt": "PUNSUBSCRIBE [pattern [pattern ...]]",
  "complexity": "O(N) where N is the number of patterns to unsubscribe.",
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

Unsubscribes the client from the specified patterns, or from all patterns if none are specified.

If you don’t specify any patterns, the client unsubscribes from all previously subscribed patterns. The client receives one message for each pattern it unsubscribes from.

## Optional arguments

<details open><summary><code>pattern [pattern ...]</code></summary>

One or more patterns to unsubscribe from. If omitted, the client is unsubscribed from all patterns.

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

When successful, this command doesn't return anything. Instead, for each pattern, one message with the first element being the string `punsubscribe` is pushed as a confirmation that the command succeeded.

**RESP3:**

When successful, this command doesn't return anything. Instead, for each pattern, one message with the first element being the string `punsubscribe` is pushed as a confirmation that the command succeeded.



