# ACL HELP

```json metadata
{
  "schema_version": 2,
  "title": "ACL HELP",
  "description": "Returns helpful text about the different subcommands.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "ACL HELP",
  "complexity": "O(1)",
  "group": "server",
  "command_flags": ["loading","stale"],
  "acl_categories": ["@slow"],
  "since": "6.0.0",
  "arity": 2,
  "tableOfContents": {"sections":[{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

The `ACL HELP` command returns a helpful text describing the different subcommands.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | Not supported for [scripts](https://redis.io/docs/latest/develop/programmability). |

## Return information

**RESP2:**

[Array reply](../../develop/reference/protocol-spec#arrays): a list of subcommands and their descriptions.

**RESP3:**

[Array reply](../../develop/reference/protocol-spec#arrays): a list of subcommands and their descriptions.



