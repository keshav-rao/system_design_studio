# REPLCONF

```json metadata
{
  "schema_version": 2,
  "title": "REPLCONF",
  "description": "An internal command for configuring the replication stream.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "REPLCONF",
  "complexity": "O(1)",
  "group": "server",
  "command_flags": ["admin","noscript","loading","stale","allow_busy"],
  "acl_categories": ["@admin","@slow","@dangerous"],
  "since": "3.0.0",
  "arity": -1,
  "tableOfContents": {"sections":[{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

The `REPLCONF` command is an internal command.
It is used by a Redis master to configure a connected replica.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.

**RESP3:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.



