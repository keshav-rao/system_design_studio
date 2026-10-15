# CLIENT ID

```json metadata
{
  "schema_version": 2,
  "title": "CLIENT ID",
  "description": "Returns the unique client ID of the connection.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "CLIENT ID",
  "complexity": "O(1)",
  "group": "connection",
  "command_flags": ["noscript","loading","stale"],
  "acl_categories": ["@slow","@connection"],
  "since": "5.0.0",
  "arity": 2,
  "tableOfContents": {"sections":[{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

The command just returns the ID of the current connection. Every connection
ID has certain guarantees:

1. It is never repeated, so if `CLIENT ID` returns the same number, the caller can be sure that the underlying client did not disconnect and reconnect the connection, but it is still the same connection.
2. The ID is monotonically incremental. If the ID of a connection is greater than the ID of another connection, it is guaranteed that the second connection was established with the server at a later time.

This command is especially useful together with [`CLIENT UNBLOCK`](https://redis.io/docs/latest/commands/client-unblock) which was
introduced also in Redis 5 together with `CLIENT ID`. Check the [`CLIENT UNBLOCK`](https://redis.io/docs/latest/commands/client-unblock) command page for a pattern involving the two commands.

## Examples


redis> CLIENT ID


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | Because Redis Software clustering allows [multiple active proxies](https://redis.io/docs/latest/operate/rs/databases/configure/proxy-policy), `CLIENT ID` cannot guarantee incremental IDs between clients that connect to different nodes under multi proxy policies. |

## Return information

**RESP2:**

[Integer reply](../../develop/reference/protocol-spec#integers): the ID of the client.

**RESP3:**

[Integer reply](../../develop/reference/protocol-spec#integers): the ID of the client.



