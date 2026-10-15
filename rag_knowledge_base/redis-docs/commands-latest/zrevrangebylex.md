# ZREVRANGEBYLEX

```json metadata
{
  "schema_version": 2,
  "title": "ZREVRANGEBYLEX",
  "description": "Returns members in a sorted set within a lexicographical range in reverse order.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"},{"display_text":"max","name":"max","type":"string"},{"display_text":"min","name":"min","type":"string"},{"arguments":[{"display_text":"offset","name":"offset","type":"integer"},{"display_text":"count","name":"count","type":"integer"}],"name":"limit","optional":true,"token":"LIMIT","type":"block"}],
  "syntax_fmt": "ZREVRANGEBYLEX key max min [LIMIT offset count]",
  "complexity": "O(log(N)+M) with N being the number of elements in the sorted set and M the number of elements being returned. If M is constant (e.g. always asking for the first 10 elements with LIMIT), you can consider it O(log(N)).",
  "group": "sorted-set",
  "command_flags": ["readonly"],
  "acl_categories": ["@read","@sortedset","@slow"],
  "since": "2.8.9",
  "arity": -4,
  "key_specs": [{"RO":true,"access":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

When all the elements in a sorted set are inserted with the same score, in order to force lexicographical ordering, this command returns all the elements in the sorted set at `key` with a value between `max` and `min`.

Apart from the reversed ordering, `ZREVRANGEBYLEX` is similar to [`ZRANGEBYLEX`](https://redis.io/docs/latest/commands/zrangebylex).

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key that holds the sorted set.

</details>

<details open><summary><code>max</code></summary>

The maximum member, compared lexicographically. Prefix with `[` for an inclusive bound or `(` for an exclusive bound; use `+` for the highest possible value.

</details>

<details open><summary><code>min</code></summary>

The minimum member, compared lexicographically. Prefix with `[` for an inclusive bound or `(` for an exclusive bound; use `-` for the lowest possible value.

</details>

## Optional arguments

<details open><summary><code>LIMIT offset count</code></summary>

Skip `offset` matching members and return up to `count` of them. A negative `count` returns all remaining members.

</details>

## Examples


redis> ZADD myzset 0 a 0 b 0 c 0 d 0 e 0 f 0 g
(integer) 7
redis> ZREVRANGEBYLEX myzset [c -
1) "c"
2) "b"
3) "a"
redis> ZREVRANGEBYLEX myzset (c -
1) "b"
2) "a"
redis> ZREVRANGEBYLEX myzset (g [aaa
1) "f"
2) "e"
3) "d"
4) "c"
5) "b"


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | Deprecated as of Redis v6.2.0. |

## Return information

**RESP2:**

[Array reply](../../develop/reference/protocol-spec#arrays): a list of members in the specified score range.

**RESP3:**

[Array reply](../../develop/reference/protocol-spec#arrays): List of the elements in the specified score range.



