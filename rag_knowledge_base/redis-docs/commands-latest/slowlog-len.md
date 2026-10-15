# SLOWLOG LEN

```json metadata
{
  "schema_version": 2,
  "title": "SLOWLOG LEN",
  "description": "Returns the number of entries in the slow log.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "SLOWLOG LEN",
  "complexity": "O(1)",
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

This command returns the current number of entries in the slow log.

A new entry is added to the slow log whenever a command exceeds the execution time threshold defined by the `slowlog-log-slower-than` configuration directive.
The maximum number of entries in the slow log is governed by the `slowlog-max-len` configuration directive.
Once the slog log reaches its maximal size, the oldest entry is removed whenever a new entry is created.
The slow log can be cleared with the [`SLOWLOG RESET`](https://redis.io/docs/latest/commands/slowlog-reset) command.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | Not supported for [scripts](https://redis.io/docs/latest/develop/programmability). |

## Return information

**RESP2:**

[Integer reply](../../develop/reference/protocol-spec#integers): the number of entries in the slow log.

**RESP3:**

[Integer reply](../../develop/reference/protocol-spec#integers): the number of entries in the slow log.



