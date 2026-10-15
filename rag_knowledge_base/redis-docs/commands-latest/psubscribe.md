# PSUBSCRIBE

```json metadata
{
  "schema_version": 2,
  "title": "PSUBSCRIBE",
  "description": "Listens for messages published to channels that match one or more patterns.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"pattern","multiple":true,"name":"pattern","type":"pattern"}],
  "syntax_fmt": "PSUBSCRIBE pattern [pattern ...]",
  "complexity": "O(N) where N is the number of patterns to subscribe to.",
  "group": "pubsub",
  "command_flags": ["pubsub","noscript","loading","stale"],
  "acl_categories": ["@pubsub","@slow"],
  "since": "2.0.0",
  "arity": -2,
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Subscribes the client to the given patterns.


Once the client enters the subscribed state it is not supposed to issue any other commands, except for additional [`SUBSCRIBE`](https://redis.io/docs/latest/commands/subscribe), [`SSUBSCRIBE`](https://redis.io/docs/latest/commands/ssubscribe), `PSUBSCRIBE`, [`UNSUBSCRIBE`](https://redis.io/docs/latest/commands/unsubscribe), [`SUNSUBSCRIBE`](https://redis.io/docs/latest/commands/sunsubscribe), [`PUNSUBSCRIBE`](https://redis.io/docs/latest/commands/punsubscribe), [`PING`](https://redis.io/docs/latest/commands/ping), [`RESET`](https://redis.io/docs/latest/commands/reset) and [`QUIT`](https://redis.io/docs/latest/commands/quit) commands.
However, if RESP3 is used (see [`HELLO`](https://redis.io/docs/latest/commands/hello)), it is possible for a client to issue any commands while in a subscribed state.

For more information, see [Pub/sub](https://redis.io/docs/latest/develop/pubsub).

## Required arguments

<details open><summary><code>pattern [pattern ...]</code></summary>

One or more glob-style patterns to subscribe to. Messages published to any channel whose name matches a pattern are delivered to the client.

Supported glob-style patterns:

* `h?llo` subscribes to `hello`, `hallo` and `hxllo`
* `h*llo` subscribes to `hllo` and `heeeello`
* `h[ae]llo` subscribes to `hello` and `hallo,` but not `hillo`

Use `\` to escape special characters if you want to match them verbatim.

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

When successful, this command doesn't return anything. Instead, for each pattern, one message with the first element being the string `psubscribe` is pushed as a confirmation that the command succeeded.

**RESP3:**

When successful, this command doesn't return anything. Instead, for each pattern, one message with the first element being the string `psubscribe` is pushed as a confirmation that the command succeeded.



