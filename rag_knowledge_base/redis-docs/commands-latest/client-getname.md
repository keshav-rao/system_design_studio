# CLIENT GETNAME

```json metadata
{
  "schema_version": 2,
  "title": "CLIENT GETNAME",
  "description": "Returns the name of the connection.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "CLIENT GETNAME",
  "complexity": "O(1)",
  "group": "connection",
  "command_flags": ["noscript","loading","stale"],
  "acl_categories": ["@slow","@connection"],
  "since": "2.6.9",
  "arity": 2,
  "tableOfContents": {"sections":[{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

The `CLIENT GETNAME` returns the name of the current connection as set by [`CLIENT SETNAME`](https://redis.io/docs/latest/commands/client-setname). Since every new connection starts without an associated name, if no name was assigned nil is returned.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): the connection name of the current connection.
* [Nil reply](../../develop/reference/protocol-spec#bulk-strings): the connection name was not set.

**RESP3:**

One of the following:
* [Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): the connection name of the current connection.
* [Null reply](../../develop/reference/protocol-spec#nulls): the connection name was not set.



