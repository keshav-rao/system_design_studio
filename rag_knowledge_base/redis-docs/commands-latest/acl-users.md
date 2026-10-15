# ACL USERS

```json metadata
{
  "schema_version": 2,
  "title": "ACL USERS",
  "description": "Lists all ACL users.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "ACL USERS",
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

The command shows a list of all the usernames of the currently configured
users in the Redis ACL system.

## Examples

```
> ACL USERS
1) "anna"
2) "antirez"
3) "default"
```

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | Not supported for [scripts](https://redis.io/docs/latest/develop/programmability). |

## Return information

**RESP2:**

[Array reply](../../develop/reference/protocol-spec#arrays): list of existing ACL users.

**RESP3:**

[Array reply](../../develop/reference/protocol-spec#arrays): list of existing ACL users.



