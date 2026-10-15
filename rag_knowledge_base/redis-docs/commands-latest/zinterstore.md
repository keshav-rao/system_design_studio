# ZINTERSTORE

```json metadata
{
  "schema_version": 2,
  "title": "ZINTERSTORE",
  "description": "Stores the intersect of multiple sorted sets in a key.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"key_spec_index":0,"name":"destination","type":"key"},{"name":"numkeys","type":"integer"},{"key_spec_index":1,"multiple":true,"name":"key","type":"key"},{"multiple":true,"name":"weight","optional":true,"token":"WEIGHTS","type":"integer"},{"arguments":[{"name":"sum","token":"SUM","type":"pure-token"},{"name":"min","token":"MIN","type":"pure-token"},{"name":"max","token":"MAX","type":"pure-token"},{"name":"count","token":"COUNT","type":"pure-token"}],"name":"aggregate","optional":true,"token":"AGGREGATE","type":"oneof"}],
  "syntax_fmt": "ZINTERSTORE destination numkeys key [key ...] [WEIGHTS weight\n  [weight ...]] [AGGREGATE \u003cSUM | MIN | MAX | COUNT\u003e]",
  "complexity": "O(N*K)+O(M*log(M)) worst case with N being the smallest input sorted set, K being the number of input sorted sets and M being the number of elements in the resulting sorted set.",
  "group": "sorted-set",
  "command_flags": ["write","denyoom","movablekeys"],
  "acl_categories": ["@write","@sortedset","@slow"],
  "since": "2.0.0",
  "arity": -4,
  "key_specs": [{"begin_search":{"index":{"pos":1}},"find_keys":{"range":{"lastkey":0,"limit":0,"step":1}},"flags":["OW","UPDATE"]},{"begin_search":{"index":{"pos":2}},"find_keys":{"keynum":{"firstkey":1,"keynumidx":0,"step":1}},"flags":["RO","ACCESS"]}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

> [!NOTE]
> This command's behavior varies in clustered Redis environments. See the [multi-key operations](https://redis.io/docs/latest/develop/using-commands/multi-key-operations) page for more information.


Computes the intersection of `numkeys` sorted sets given by the specified keys,
and stores the result in `destination`.
It is mandatory to provide the number of input keys (`numkeys`) before passing
the input keys and the other (optional) arguments.

By default, the resulting score of an element is the sum of its scores in the
sorted sets where it exists.
Because intersection requires an element to be a member of every given sorted
set, this results in the score of every element in the resulting sorted set to
be equal to the number of input sorted sets.

For a description of the `WEIGHTS` and `AGGREGATE` options, see [`ZUNIONSTORE`](https://redis.io/docs/latest/commands/zunionstore).

If `destination` already exists, it is overwritten.

## Required arguments

<details open><summary><code>destination</code></summary>

The key to store the resulting sorted set in.

</details>

<details open><summary><code>numkeys</code></summary>

The number of keys that follow.

</details>

<details open><summary><code>key [key ...]</code></summary>

One or more sorted-set keys to intersect.

</details>

## Optional arguments

<details open><summary><code>WEIGHTS weight [weight ...]</code></summary>

A multiplication factor for each input set; each set's scores are multiplied by its weight before aggregation. Defaults to 1 for every set.

</details>

<details open><summary><code>AGGREGATE SUM | MIN | MAX | COUNT</code></summary>

How to combine the scores of members that exist in multiple sets: `SUM` (the default), `MIN`, `MAX`, or `COUNT`.

</details>

## Examples


redis> ZADD zset1 1 "one"
(integer) 1
redis> ZADD zset1 2 "two"
(integer) 1
redis> ZADD zset2 1 "one"
(integer) 1
redis> ZADD zset2 2 "two"
(integer) 1
redis> ZADD zset2 3 "three"
(integer) 1
redis> ZINTERSTORE out 2 zset1 zset2 WEIGHTS 2 3
(integer) 2
redis> ZRANGE out 0 -1 WITHSCORES
1) "one"
2) "5"
3) "two"
4) "10"


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Integer reply](../../develop/reference/protocol-spec#integers): the number of members in the resulting sorted set at the _destination_.

**RESP3:**

[Integer reply](../../develop/reference/protocol-spec#integers): the number of members in the resulting sorted set at the _destination_.



