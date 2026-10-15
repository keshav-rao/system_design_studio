# UNWATCH

```json metadata
{
  "schema_version": 2,
  "title": "UNWATCH",
  "description": "Forgets about watched keys of a transaction.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "UNWATCH",
  "complexity": "O(1)",
  "group": "transactions",
  "command_flags": ["noscript","loading","stale","fast","allow_busy"],
  "acl_categories": ["@fast","@transaction"],
  "since": "2.2.0",
  "arity": 1,
  "tableOfContents": {"sections":[{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Flushes all the previously watched keys for a [transaction](https://redis.io/docs/latest/develop/using-commands/transactions).

If you call [`EXEC`](https://redis.io/docs/latest/commands/exec) or [`DISCARD`](https://redis.io/docs/latest/commands/discard), there's no need to manually call `UNWATCH`.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.

**RESP3:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.



