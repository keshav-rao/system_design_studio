# ZUNION

```json metadata
{
  "schema_version": 2,
  "title": "ZUNION",
  "description": "Returns the union of multiple sorted sets.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"numkeys","type":"integer"},{"key_spec_index":0,"multiple":true,"name":"key","type":"key"},{"multiple":true,"name":"weight","optional":true,"token":"WEIGHTS","type":"integer"},{"arguments":[{"name":"sum","token":"SUM","type":"pure-token"},{"name":"min","token":"MIN","type":"pure-token"},{"name":"max","token":"MAX","type":"pure-token"},{"name":"count","token":"COUNT","type":"pure-token"}],"name":"aggregate","optional":true,"token":"AGGREGATE","type":"oneof"},{"name":"withscores","optional":true,"token":"WITHSCORES","type":"pure-token"}],
  "syntax_fmt": "ZUNION numkeys key [key ...] [WEIGHTS weight [weight ...]]\n  [AGGREGATE \u003cSUM | MIN | MAX | COUNT\u003e] [WITHSCORES]",
  "complexity": "O(N)+O(M*log(M)) with N being the sum of the sizes of the input sorted sets, and M being the number of elements in the resulting sorted set.",
  "group": "sorted-set",
  "command_flags": ["readonly","movablekeys"],
  "acl_categories": ["@read","@sortedset","@slow"],
  "since": "6.2.0",
  "arity": -3,
  "key_specs": [{"begin_search":{"index":{"pos":1}},"find_keys":{"keynum":{"firstkey":1,"keynumidx":0,"step":1}},"flags":["RO","ACCESS"]}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

> [!NOTE]
> This command's behavior varies in clustered Redis environments. See the [multi-key operations](https://redis.io/docs/latest/develop/using-commands/multi-key-operations) page for more information.


This command is similar to [`ZUNIONSTORE`](https://redis.io/docs/latest/commands/zunionstore), but instead of storing the resulting
sorted set, it is returned to the client.

For a description of the `WEIGHTS` and `AGGREGATE` options, see [`ZUNIONSTORE`](https://redis.io/docs/latest/commands/zunionstore).

## Required arguments

<details open><summary><code>numkeys</code></summary>

The number of keys that follow.

</details>

<details open><summary><code>key [key ...]</code></summary>

One or more sorted-set keys to union.

</details>

## Optional arguments

<details open><summary><code>WEIGHTS weight [weight ...]</code></summary>

A multiplication factor for each input set; each set's scores are multiplied by its weight before aggregation. Defaults to 1 for every set.

</details>

<details open><summary><code>AGGREGATE SUM | MIN | MAX | COUNT</code></summary>

How to combine the scores of members that exist in multiple sets: `SUM` (the default), `MIN`, `MAX`, or `COUNT`.

</details>

<details open><summary><code>WITHSCORES</code></summary>

Also return the score of each member.

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
redis> ZUNION 2 zset1 zset2
1) "one"
2) "three"
3) "two"
redis> ZUNION 2 zset1 zset2 WITHSCORES
1) "one"
2) "2"
3) "three"
4) "3"
5) "two"
6) "4"


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Array reply](../../develop/reference/protocol-spec#arrays): the result of the union with, optionally, their scores when _WITHSCORES_ is used.

**RESP3:**

[Array reply](../../develop/reference/protocol-spec#arrays): the result of the union with, optionally, their scores when _WITHSCORES_ is used.



