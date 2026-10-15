# ZMSCORE

```json metadata
{
  "schema_version": 2,
  "title": "ZMSCORE",
  "description": "Returns the score of one or more members in a sorted set.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"},{"display_text":"member","multiple":true,"name":"member","type":"string"}],
  "syntax_fmt": "ZMSCORE key member [member ...]",
  "complexity": "O(N) where N is the number of members being requested.",
  "group": "sorted-set",
  "command_flags": ["readonly","fast"],
  "acl_categories": ["@read","@sortedset","@fast"],
  "since": "6.2.0",
  "arity": -3,
  "key_specs": [{"RO":true,"access":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Returns the scores associated with the specified `members` in the sorted set stored at `key`.

For every `member` that does not exist in the sorted set, a `nil` value is returned.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key that holds the sorted set.

</details>

<details open><summary><code>member [member ...]</code></summary>

One or more members whose scores to return.

</details>

## Examples


redis> ZADD myzset 1 "one"
(integer) 1
redis> ZADD myzset 2 "two"
(integer) 1
redis> ZMSCORE myzset "one" "two" "nofield"
1) "1"
2) "2"
3) (nil)


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Nil reply](../../develop/reference/protocol-spec#bulk-strings): if the member does not exist in the sorted set.
* [Array reply](../../develop/reference/protocol-spec#arrays): a list of [Bulk string reply](../../develop/reference/protocol-spec#bulk-strings) _member_ scores as double-precision floating point numbers.

**RESP3:**

One of the following:
* [Null reply](../../develop/reference/protocol-spec#nulls): if the member does not exist in the sorted set.
* [Array reply](../../develop/reference/protocol-spec#arrays): a list of [Double reply](../../develop/reference/protocol-spec#doubles) _member_ scores as double-precision floating point numbers.



