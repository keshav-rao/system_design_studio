# ZSCORE

```json metadata
{
  "schema_version": 2,
  "title": "ZSCORE",
  "description": "Returns the score of a member in a sorted set.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"},{"display_text":"member","name":"member","type":"string"}],
  "syntax_fmt": "ZSCORE key member",
  "complexity": "O(1)",
  "group": "sorted-set",
  "command_flags": ["readonly","fast"],
  "acl_categories": ["@read","@sortedset","@fast"],
  "since": "1.2.0",
  "arity": 3,
  "key_specs": [{"RO":true,"access":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Returns the score of `member` in the sorted set at `key`.

If `member` does not exist in the sorted set, or `key` does not exist, `nil` is
returned.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key that holds the sorted set.

</details>

<details open><summary><code>member</code></summary>

The member whose score to return.

</details>

## Examples


redis> ZADD myzset 1 "one"
(integer) 1
redis> ZSCORE myzset "one"
"1"


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): the score of the member (a double-precision floating point number), represented as a string.
* [Nil reply](../../develop/reference/protocol-spec#bulk-strings): if _member_ does not exist in the sorted set, or the key does not exist.

**RESP3:**

One of the following:
* [Double reply](../../develop/reference/protocol-spec#doubles): the score of the member (a double-precision floating point number).
* [Nil reply](../../develop/reference/protocol-spec#bulk-strings): if _member_ does not exist in the sorted set, or the key does not exist.



