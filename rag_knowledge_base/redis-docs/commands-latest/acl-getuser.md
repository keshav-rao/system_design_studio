# ACL GETUSER

```json metadata
{
  "schema_version": 2,
  "title": "ACL GETUSER",
  "description": "Lists the ACL rules of a user.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"username","name":"username","type":"string"}],
  "syntax_fmt": "ACL GETUSER username",
  "complexity": "O(N). Where N is the number of password, command and pattern rules that the user has.",
  "group": "server",
  "command_flags": ["admin","noscript","loading","stale"],
  "acl_categories": ["@admin","@slow","@dangerous"],
  "since": "6.0.0",
  "arity": 3,
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

The command returns all the rules defined for an existing ACL user.

Specifically, it lists the user's ACL flags, password hashes, commands, key patterns, channel patterns (Added in version 6.2) and selectors (Added in version 7.0).
Additional information may be returned in the future if more metadata is added to the user.

Command rules are always returned in the same format as the one used in the [`ACL SETUSER`](https://redis.io/docs/latest/commands/acl-setuser) command.
Before version 7.0, keys and channels were returned as an array of patterns, however in version 7.0 later they are now also returned in same format as the one used in the [`ACL SETUSER`](https://redis.io/docs/latest/commands/acl-setuser) command.
Note: This description of command rules reflects the user's effective permissions, so while it may not be identical to the set of rules used to configure the user, it is still functionally identical.

Selectors are listed in the order they were applied to the user, and include information about commands, key patterns, and channel patterns.

## Required arguments

<details open><summary><code>username</code></summary>

The user whose rules to return.

</details>

## Examples

Here's an example configuration for a user

```
> ACL SETUSER sample on nopass +GET allkeys &* (+SET ~key2)
"OK"
> ACL GETUSER sample
1) "flags"
2) 1) "on"
   2) "allkeys"
   3) "nopass"
3) "passwords"
4) (empty array)
5) "commands"
6) "+@all"
7) "keys"
8) "~*"
9) "channels"
10) "&*"
11) "selectors"
12) 1) 1) "commands"
       6) "+SET"
       7) "keys"
       8) "~key2"
       9) "channels"
       10) "&*"
```

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | Not supported for [scripts](https://redis.io/docs/latest/develop/programmability). |

## Return information

**RESP2:**

One of the following:
* [Array reply](../../develop/reference/protocol-spec#arrays): a list of ACL rule definitions for the user.
* [Nil reply](../../develop/reference/protocol-spec#bulk-strings): if user does not exist.

**RESP3:**

One of the following:
* [Map reply](../../develop/reference/protocol-spec#maps): a set of ACL rule definitions for the user
* [Null reply](../../develop/reference/protocol-spec#nulls): if user does not exist.



