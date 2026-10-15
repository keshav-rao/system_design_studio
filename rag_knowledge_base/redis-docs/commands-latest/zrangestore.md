# ZRANGESTORE

```json metadata
{
  "schema_version": 2,
  "title": "ZRANGESTORE",
  "description": "Stores a range of members from sorted set in a key.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"dst","key_spec_index":0,"name":"dst","type":"key"},{"display_text":"src","key_spec_index":1,"name":"src","type":"key"},{"display_text":"min","name":"min","type":"string"},{"display_text":"max","name":"max","type":"string"},{"arguments":[{"display_text":"byscore","name":"byscore","token":"BYSCORE","type":"pure-token"},{"display_text":"bylex","name":"bylex","token":"BYLEX","type":"pure-token"}],"name":"sortby","optional":true,"type":"oneof"},{"display_text":"rev","name":"rev","optional":true,"token":"REV","type":"pure-token"},{"arguments":[{"display_text":"offset","name":"offset","type":"integer"},{"display_text":"count","name":"count","type":"integer"}],"name":"limit","optional":true,"token":"LIMIT","type":"block"}],
  "syntax_fmt": "ZRANGESTORE dst src min max [BYSCORE | BYLEX] [REV] [LIMIT offset\n  count]",
  "complexity": "O(log(N)+M) with N being the number of elements in the sorted set and M the number of elements stored into the destination key.",
  "group": "sorted-set",
  "command_flags": ["write","denyoom"],
  "acl_categories": ["@write","@sortedset","@slow"],
  "since": "6.2.0",
  "arity": -5,
  "key_specs": [{"OW":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"},"update":true},{"RO":true,"access":true,"begin_search":{"spec":{"index":2},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

> [!NOTE]
> This command's behavior varies in clustered Redis environments. See the [multi-key operations](https://redis.io/docs/latest/develop/using-commands/multi-key-operations) page for more information.


This command is like [`ZRANGE`](https://redis.io/docs/latest/commands/zrange), but stores the result in the `<dst>` destination key.

## Required arguments

<details open><summary><code>dst</code></summary>

The key to store the resulting sorted set in.

</details>

<details open><summary><code>src</code></summary>

The source sorted-set key.

</details>

<details open><summary><code>min</code></summary>

The start of the range. By default a zero-based index (negatives count from the end); a score bound with `BYSCORE`; or a lexicographical bound with `BYLEX`.

</details>

<details open><summary><code>max</code></summary>

The end of the range, inclusive. Interpreted the same way as `min`.

</details>

## Optional arguments

<details open><summary><code>BYSCORE | BYLEX</code></summary>

Interpret the range as a score range (`BYSCORE`) or a lexicographical range (`BYLEX`) instead of an index range.

</details>

<details open><summary><code>REV</code></summary>

Reverse the ordering so results are returned from high to low.

</details>

<details open><summary><code>LIMIT offset count</code></summary>

Skip `offset` matching members and return up to `count` of them. Requires `BYSCORE` or `BYLEX`. A negative `count` returns all remaining members.

</details>

## Examples


redis> ZADD srczset 1 "one" 2 "two" 3 "three" 4 "four"
(integer) 4
redis> ZRANGESTORE dstzset srczset 2 -1
(integer) 2
redis> ZRANGE dstzset 0 -1
1) "three"
2) "four"


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Integer reply](../../develop/reference/protocol-spec#integers): the number of elements in the resulting sorted set.

**RESP3:**

[Integer reply](../../develop/reference/protocol-spec#integers): the number of elements in the resulting sorted set.



