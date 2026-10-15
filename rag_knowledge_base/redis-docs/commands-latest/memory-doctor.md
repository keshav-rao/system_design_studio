# MEMORY DOCTOR

```json metadata
{
  "schema_version": 2,
  "title": "MEMORY DOCTOR",
  "description": "Outputs a memory problems report.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "MEMORY DOCTOR",
  "complexity": "O(1)",
  "group": "server",
  "acl_categories": ["@slow"],
  "since": "4.0.0",
  "arity": 2,
  "tableOfContents": {"sections":[{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

The `MEMORY DOCTOR` command reports about different memory-related issues that
the Redis server experiences, and advises about possible remedies.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): a memory problems report.

**RESP3:**

[Verbatim string reply](../../develop/reference/protocol-spec#verbatim-strings): a memory problems report.



