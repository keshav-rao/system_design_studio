# ZREMRANGEBYRANK

```json metadata
{
  "schema_version": 2,
  "title": "ZREMRANGEBYRANK",
  "description": "Removes members in a sorted set within a range of indexes. Deletes the sorted set if all members were removed.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"},{"display_text":"start","name":"start","type":"integer"},{"display_text":"stop","name":"stop","type":"integer"}],
  "syntax_fmt": "ZREMRANGEBYRANK key start stop",
  "complexity": "O(log(N)+M) with N being the number of elements in the sorted set and M the number of elements removed by the operation.",
  "group": "sorted-set",
  "command_flags": ["write"],
  "acl_categories": ["@write","@sortedset","@slow"],
  "since": "2.0.0",
  "arity": 4,
  "key_specs": [{"RW":true,"begin_search":{"spec":{"index":1},"type":"index"},"delete":true,"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Removes all elements in the sorted set stored at `key` with rank between `start`
and `stop`.
Both `start` and `stop` are `0` -based indexes with `0` being the element with
the lowest score.
These indexes can be negative numbers, where they indicate offsets starting at
the element with the highest score.
For example: `-1` is the element with the highest score, `-2` the element with
the second highest score and so forth.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key that holds the sorted set.

</details>

<details open><summary><code>start</code></summary>

The start index, zero-based. Negative values count from the end of the sorted set (`-1` is the member with the highest score).

</details>

<details open><summary><code>stop</code></summary>

The stop index, zero-based and inclusive. Negative values count from the end of the sorted set.

</details>

## Examples


redis> ZADD myzset 1 "one"
(integer) 1
redis> ZADD myzset 2 "two"
(integer) 1
redis> ZADD myzset 3 "three"
(integer) 1
redis> ZREMRANGEBYRANK myzset 0 1
(integer) 2
redis> ZRANGE myzset 0 -1 WITHSCORES
1) "three"
2) "3"


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Integer reply](../../develop/reference/protocol-spec#integers): the number of members removed.

**RESP3:**

[Integer reply](../../develop/reference/protocol-spec#integers): Number of members removed.



