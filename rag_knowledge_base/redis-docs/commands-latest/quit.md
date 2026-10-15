# QUIT

```json metadata
{
  "schema_version": 2,
  "title": "QUIT",
  "description": "Closes the connection.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "QUIT",
  "complexity": "O(1)",
  "group": "connection",
  "command_flags": ["noscript","loading","stale","fast","no_auth","allow_busy"],
  "acl_categories": ["@fast","@connection"],
  "since": "1.0.0",
  "arity": -1,
  "tableOfContents": {"sections":[{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Ask the server to close the connection.
The connection is closed as soon as all pending replies have been written to the
client.

**Note:** Clients should not use this command.
Instead, clients should simply close the connection when they're not used anymore.
Terminating a connection on the client side is preferable, as it eliminates `TIME_WAIT` lingering sockets on the server side.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | Deprecated as of Redis v7.2.0. |

## Return information

**RESP2:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): OK.

**RESP3:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.



