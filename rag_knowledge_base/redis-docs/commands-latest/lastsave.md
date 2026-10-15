# LASTSAVE

```json metadata
{
  "schema_version": 2,
  "title": "LASTSAVE",
  "description": "Returns the Unix timestamp of the last successful save to disk.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "LASTSAVE",
  "complexity": "O(1)",
  "group": "server",
  "command_flags": ["loading","stale","fast"],
  "acl_categories": ["@admin","@fast","@dangerous"],
  "since": "1.0.0",
  "arity": 1,
  "tableOfContents": {"sections":[{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Return the UNIX TIME of the last DB save executed with success.
A client may check if a [`BGSAVE`](https://redis.io/docs/latest/commands/bgsave) command succeeded reading the `LASTSAVE` value,
then issuing a [`BGSAVE`](https://redis.io/docs/latest/commands/bgsave) command and checking at regular intervals every N
seconds if `LASTSAVE` changed. Redis considers the database saved successfully at startup.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Integer reply](../../develop/reference/protocol-spec#integers): UNIX TIME of the last DB save executed with success.

**RESP3:**

[Integer reply](../../develop/reference/protocol-spec#integers): UNIX TIME of the last DB save executed with success.



