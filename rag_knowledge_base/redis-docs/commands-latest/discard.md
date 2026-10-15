# DISCARD

```json metadata
{
  "schema_version": 2,
  "title": "DISCARD",
  "description": "Discards a transaction.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "DISCARD",
  "complexity": "O(N), when N is the number of queued commands",
  "group": "transactions",
  "command_flags": ["noscript","loading","stale","fast","allow_busy"],
  "acl_categories": ["@fast","@transaction"],
  "since": "2.0.0",
  "arity": 1,
  "tableOfContents": {"sections":[{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Flushes all previously queued commands in a [transaction](https://redis.io/docs/latest/develop/using-commands/transactions) and restores the
connection state to normal.

If [`WATCH`](https://redis.io/docs/latest/commands/watch) was used, `DISCARD` unwatches all keys watched by the connection.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.

**RESP3:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.



