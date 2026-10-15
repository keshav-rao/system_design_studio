# ACL LIST

```json metadata
{
  "schema_version": 2,
  "title": "ACL LIST",
  "description": "Dumps the effective rules in ACL file format.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "ACL LIST",
  "complexity": "O(N). Where N is the number of configured users.",
  "group": "server",
  "command_flags": ["admin","noscript","loading","stale"],
  "acl_categories": ["@admin","@slow","@dangerous"],
  "since": "6.0.0",
  "arity": 2,
  "tableOfContents": {"sections":[{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

The command shows the currently active ACL rules in the Redis server. Each
line in the returned array defines a different user, and the format is the
same used in the redis.conf file or the external ACL file, so you can
cut and paste what is returned by the ACL LIST command directly inside a
configuration file if you wish (but make sure to check [`ACL SAVE`](https://redis.io/docs/latest/commands/acl-save)).

## Examples

```
> ACL LIST
1) "user antirez on #9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08 ~objects:* &* +@all -@admin -@dangerous"
2) "user default on nopass ~* &* +@all"
```

> [!NOTE]
> In some cases, you might see `allchannels` instead of `&*` and `allkeys` instead of `~*` in the output. This is because `allchannels` and `allkeys` are aliases for `&*` and `~*` respectively.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | Not supported for [scripts](https://redis.io/docs/latest/develop/programmability). |

## Return information

**RESP2:**

[Array reply](../../develop/reference/protocol-spec#arrays): an array of [Bulk string reply](../../develop/reference/protocol-spec#bulk-strings) elements.

**RESP3:**

[Array reply](../../develop/reference/protocol-spec#arrays): an array of [Bulk string reply](../../develop/reference/protocol-spec#bulk-strings) elements.



