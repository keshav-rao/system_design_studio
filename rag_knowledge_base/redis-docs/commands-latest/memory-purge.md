# MEMORY PURGE

```json metadata
{
  "schema_version": 2,
  "title": "MEMORY PURGE",
  "description": "Asks the allocator to release memory.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "MEMORY PURGE",
  "complexity": "Depends on how much memory is allocated, could be slow",
  "group": "server",
  "acl_categories": ["@slow"],
  "since": "4.0.0",
  "arity": 2,
  "tableOfContents": {"sections":[{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

The `MEMORY PURGE` command attempts to purge dirty pages so these can be
reclaimed by the allocator.

This command is currently implemented only when using **jemalloc** as an
allocator, and evaluates to a benign NOOP for all others.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.

**RESP3:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.



