# SLOWLOG RESET

```json metadata
{
  "schema_version": 2,
  "title": "SLOWLOG RESET",
  "description": "Clears all entries from the slow log.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "SLOWLOG RESET",
  "complexity": "O(N) where N is the number of entries in the slowlog",
  "group": "server",
  "command_flags": ["admin","loading","stale"],
  "acl_categories": ["@admin","@slow","@dangerous"],
  "since": "2.2.12",
  "arity": 2,
  "tableOfContents": {"sections":[{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

This command resets the slow log, clearing all entries in it.

Once deleted the information is lost forever.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | Not supported for [scripts](https://redis.io/docs/latest/develop/programmability). |

## Return information

**RESP2:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.

**RESP3:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.



