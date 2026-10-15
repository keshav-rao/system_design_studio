# BACKUP HELP

```json metadata
{
  "schema_version": 2,
  "title": "BACKUP HELP",
  "description": "Return helpful text about BACKUP command parameters.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "BACKUP HELP",
  "complexity": "O(1)",
  "group": "server",
  "command_flags": ["loading","stale"],
  "acl_categories": ["@slow"],
  "since": "8.10.0",
  "arity": 2,
  "tableOfContents": {"sections":[{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

The `BACKUP HELP` command returns helpful text describing the different subcommands.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Array reply](../../develop/reference/protocol-spec#arrays): a list of sub-commands and their descriptions.

**RESP3:**

[Array reply](../../develop/reference/protocol-spec#arrays): a list of sub-commands and their descriptions.



