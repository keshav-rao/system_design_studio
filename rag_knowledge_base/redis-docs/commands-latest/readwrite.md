# READWRITE

```json metadata
{
  "schema_version": 2,
  "title": "READWRITE",
  "description": "Enables read-write queries for a connection to a Redis Cluster replica node.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "READWRITE",
  "complexity": "O(1)",
  "group": "cluster",
  "command_flags": ["loading","stale","fast"],
  "acl_categories": ["@fast","@connection"],
  "since": "3.0.0",
  "arity": 1,
  "tableOfContents": {"sections":[{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Disables read queries for a connection to a Redis Cluster replica node.

Read queries against a Redis Cluster replica node are disabled by default,
but you can use the [`READONLY`](https://redis.io/docs/latest/commands/readonly) command to change this behavior on a per-
connection basis. The `READWRITE` command resets the readonly mode flag
of a connection back to readwrite.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.

**RESP3:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.



