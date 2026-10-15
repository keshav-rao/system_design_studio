# ZCARD

```json metadata
{
  "schema_version": 2,
  "title": "ZCARD",
  "description": "Returns the number of members in a sorted set.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"}],
  "syntax_fmt": "ZCARD key",
  "complexity": "O(1)",
  "group": "sorted-set",
  "command_flags": ["readonly","fast"],
  "acl_categories": ["@read","@sortedset","@fast"],
  "since": "1.2.0",
  "arity": 2,
  "key_specs": [{"RO":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Returns the sorted set cardinality (number of elements) of the sorted set stored
at `key`.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key that holds the sorted set.

</details>

## Examples


redis> ZADD myzset 1 "one"
(integer) 1
redis> ZADD myzset 2 "two"
(integer) 1
redis> ZCARD myzset
(integer) 2


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Integer reply](../../develop/reference/protocol-spec#integers): the cardinality (number of members) of the sorted set, or 0 if the key doesn't exist.

**RESP3:**

[Integer reply](../../develop/reference/protocol-spec#integers): the cardinality (number of members) of the sorted set, or 0 if the key doesn't exist.



