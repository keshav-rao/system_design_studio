# CLIENT HELP

```json metadata
{
  "schema_version": 2,
  "title": "CLIENT HELP",
  "description": "Returns helpful text about the different subcommands.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "CLIENT HELP",
  "complexity": "O(1)",
  "group": "connection",
  "command_flags": ["loading","stale"],
  "acl_categories": ["@slow","@connection"],
  "since": "5.0.0",
  "arity": 2,
  "tableOfContents": {"sections":[{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

The `CLIENT HELP` command returns a helpful text describing the different subcommands.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Array reply](../../develop/reference/protocol-spec#arrays): a list of subcommands and their descriptions.

**RESP3:**

[Array reply](../../develop/reference/protocol-spec#arrays): a list of subcommands and their descriptions.



