# HOTKEYS RESET

```json metadata
{
  "schema_version": 2,
  "title": "HOTKEYS RESET",
  "description": "Release the resources used for hotkey tracking.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "HOTKEYS RESET",
  "complexity": "O(1)",
  "group": "server",
  "command_flags": ["admin","noscript"],
  "acl_categories": ["@admin","@slow","@dangerous"],
  "since": "8.6.0",
  "arity": 2,
  "tableOfContents": {"sections":[{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Release the resources used for hotkey tracking.

This command can only be executed when hotkey tracking is stopped. It will return an error if tracking is currently active. Use [`HOTKEYS STOP`](https://redis.io/docs/latest/commands/hotkeys-stop) first to stop tracking, then use `HOTKEYS RESET` to free the allocated resources.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

One of the following:

- [Simple string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-strings): `OK` when resources are successfully released.
- [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors): when tracking is currently active.

**RESP3:**

One of the following:

- [Simple string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-strings): `OK` when resources are successfully released.
- [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors): when tracking is currently active.



