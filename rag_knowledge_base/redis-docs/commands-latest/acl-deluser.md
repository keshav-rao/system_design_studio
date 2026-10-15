# ACL DELUSER

```json metadata
{
  "schema_version": 2,
  "title": "ACL DELUSER",
  "description": "Deletes ACL users, and terminates their connections.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"username","multiple":true,"name":"username","type":"string"}],
  "syntax_fmt": "ACL DELUSER username [username ...]",
  "complexity": "O(1) amortized time considering the typical user.",
  "group": "server",
  "command_flags": ["admin","noscript","loading","stale"],
  "acl_categories": ["@admin","@slow","@dangerous"],
  "since": "6.0.0",
  "arity": -3,
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Delete all the specified ACL users and terminate all the connections that are
authenticated with such users. Note: the special `default` user cannot be
removed from the system, this is the default user that every new connection
is authenticated with. The list of users may include usernames that do not
exist, in such case no operation is performed for the non existing users.

## Required arguments

<details open><summary><code>username [username ...]</code></summary>

One or more usernames to delete.

</details>

## Examples

```
> ACL DELUSER antirez
1
```

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Integer reply](../../develop/reference/protocol-spec#integers): the number of users that were deleted. This number will not always match the number of arguments since certain users may not exist.

**RESP3:**

[Integer reply](../../develop/reference/protocol-spec#integers): the number of users that were deleted. This number will not always match the number of arguments since certain users may not exist.



