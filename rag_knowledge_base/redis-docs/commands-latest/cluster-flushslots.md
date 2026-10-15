# CLUSTER FLUSHSLOTS

```json metadata
{
  "schema_version": 2,
  "title": "CLUSTER FLUSHSLOTS",
  "description": "Deletes all slots information from a node.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "CLUSTER FLUSHSLOTS",
  "complexity": "O(1)",
  "group": "cluster",
  "command_flags": ["admin","stale","no_async_loading"],
  "acl_categories": ["@admin","@slow","@dangerous"],
  "since": "3.0.0",
  "arity": 2,
  "tableOfContents": {"sections":[{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Deletes all slots from a node.

The `CLUSTER FLUSHSLOTS` deletes all information about slots from the connected node. It can only be called when the database is empty.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`

**RESP3:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.



