# SISMEMBER

```json metadata
{
  "schema_version": 2,
  "title": "SISMEMBER",
  "description": "Determines whether a member belongs to a set.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"},{"display_text":"member","name":"member","type":"string"}],
  "syntax_fmt": "SISMEMBER key member",
  "complexity": "O(1)",
  "group": "set",
  "command_flags": ["readonly","fast"],
  "acl_categories": ["@read","@set","@fast"],
  "since": "1.0.0",
  "arity": 3,
  "key_specs": [{"RO":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Returns if `member` is a member of the set stored at `key`.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key that holds the set.

</details>

<details open><summary><code>member</code></summary>

The member to check for.

</details>

## Examples


redis> SADD myset "one"
(integer) 1
redis> SISMEMBER myset "one"
(integer) 1
redis> SISMEMBER myset "two"
(integer) 0


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Integer reply](../../develop/reference/protocol-spec#integers): `0` if the element is not a member of the set, or when the key does not exist.
* [Integer reply](../../develop/reference/protocol-spec#integers): `1` if the element is a member of the set.

**RESP3:**

One of the following:
* [Integer reply](../../develop/reference/protocol-spec#integers): `0` if the element is not a member of the set, or when the key does not exist.
* [Integer reply](../../develop/reference/protocol-spec#integers): `1` if the element is a member of the set.



