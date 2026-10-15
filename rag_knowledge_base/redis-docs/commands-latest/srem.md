# SREM

```json metadata
{
  "schema_version": 2,
  "title": "SREM",
  "description": "Removes one or more members from a set. Deletes the set if the last member was removed.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"},{"display_text":"member","multiple":true,"name":"member","type":"string"}],
  "syntax_fmt": "SREM key member [member ...]",
  "complexity": "O(N) where N is the number of members to be removed.",
  "group": "set",
  "command_flags": ["write","fast"],
  "acl_categories": ["@write","@set","@fast"],
  "since": "1.0.0",
  "arity": -3,
  "key_specs": [{"RW":true,"begin_search":{"spec":{"index":1},"type":"index"},"delete":true,"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Remove the specified members from the set stored at `key`.
Specified members that are not a member of this set are ignored.
If `key` does not exist, it is treated as an empty set and this command returns
`0`.

An error is returned when the value stored at `key` is not a set.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key that holds the set.

</details>

<details open><summary><code>member [member ...]</code></summary>

One or more members to remove from the set.

</details>

## Examples


redis> SADD myset "one"
(integer) 1
redis> SADD myset "two"
(integer) 1
redis> SADD myset "three"
(integer) 1
redis> SREM myset "one"
(integer) 1
redis> SREM myset "four"
(integer) 0
redis> SMEMBERS myset
1) "two"
2) "three"


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Integer reply](../../develop/reference/protocol-spec#integers): the number of members that were removed from the set, not including non existing members.

**RESP3:**

[Integer reply](../../develop/reference/protocol-spec#integers): Number of members that were removed from the set, not including non existing members.



