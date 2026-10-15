# BZPOPMIN

```json metadata
{
  "schema_version": 2,
  "title": "BZPOPMIN",
  "description": "Removes and returns the member with the lowest score from one or more sorted sets. Blocks until a member is available otherwise. Deletes the sorted set if the last element was popped.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"multiple":true,"name":"key","type":"key"},{"display_text":"timeout","name":"timeout","type":"double"}],
  "syntax_fmt": "BZPOPMIN key [key ...] timeout",
  "complexity": "O(log(N)) with N being the number of elements in the sorted set.",
  "group": "sorted-set",
  "command_flags": ["write","blocking","fast"],
  "acl_categories": ["@write","@sortedset","@fast","@blocking"],
  "since": "5.0.0",
  "arity": -3,
  "key_specs": [{"RW":true,"access":true,"begin_search":{"spec":{"index":1},"type":"index"},"delete":true,"find_keys":{"spec":{"keystep":1,"lastkey":-2,"limit":0},"type":"range"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

> [!NOTE]
> This command's behavior varies in clustered Redis environments. See the [multi-key operations](https://redis.io/docs/latest/develop/using-commands/multi-key-operations) page for more information.


`BZPOPMIN` is the blocking variant of the sorted set [`ZPOPMIN`](https://redis.io/docs/latest/commands/zpopmin) primitive.

It is the blocking version because it blocks the connection when there are no
members to pop from any of the given sorted sets.
A member with the lowest score is popped from first sorted set that is
non-empty, with the given keys being checked in the order that they are given.

The `timeout` argument is interpreted as a double value specifying the maximum
number of seconds to block. A timeout of zero can be used to block indefinitely.

See the [BLPOP documentation](https://redis.io/docs/latest/commands/blpop) for the exact semantics, since `BZPOPMIN` is
identical to [`BLPOP`](https://redis.io/docs/latest/commands/blpop) with the only difference being the data structure being
popped from.

## Required arguments

<details open><summary><code>key [key ...]</code></summary>

One or more sorted-set keys to pop from.

</details>

<details open><summary><code>timeout</code></summary>

The maximum time to block, in seconds. A timeout of `0` blocks indefinitely.

</details>

## Examples

```
redis> DEL zset1 zset2
(integer) 0
redis> ZADD zset1 0 a 1 b 2 c
(integer) 3
redis> BZPOPMIN zset1 zset2 0
1) "zset1"
2) "a"
3) "0"
```

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Nil reply](../../develop/reference/protocol-spec#bulk-strings): when no element could be popped and the _timeout_ expired.
* [Array reply](../../develop/reference/protocol-spec#arrays): the keyname, popped member, and its score.

**RESP3:**

One of the following:
* [Null reply](../../develop/reference/protocol-spec#nulls): when no element could be popped and the _timeout_ expired.
* [Array reply](../../develop/reference/protocol-spec#arrays): the keyname, popped member, and its score.



