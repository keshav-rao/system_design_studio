# HOTKEYS STOP

```json metadata
{
  "schema_version": 2,
  "title": "HOTKEYS STOP",
  "description": "Stops hotkeys tracking.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "HOTKEYS STOP",
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

Stops hotkeys tracking but preserves the collected data.

After stopping, the tracking data remains available through [`HOTKEYS GET`](https://redis.io/docs/latest/commands/hotkeys-get) until [`HOTKEYS RESET`](https://redis.io/docs/latest/commands/hotkeys-reset) is called or a new tracking session is started.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

One of the following:

- [Simple string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-strings): `OK` when tracking is successfully stopped.
- [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors): when tracking is not currently active.

**RESP3:**

One of the following:

- [Simple string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-strings): `OK` when tracking is successfully stopped.
- [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors): when tracking is not currently active.



