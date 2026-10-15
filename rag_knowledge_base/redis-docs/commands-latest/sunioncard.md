# SUNIONCARD

```json metadata
{
  "schema_version": 2,
  "title": "SUNIONCARD",
  "description": "Returns the number of members of the union of multiple sets.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"numkeys","name":"numkeys","type":"integer"},{"display_text":"key","key_spec_index":0,"multiple":true,"name":"key","type":"key"},{"display_text":"approx","name":"approx","optional":true,"token":"APPROX","type":"pure-token"},{"display_text":"limit","name":"limit","optional":true,"token":"LIMIT","type":"integer"}],
  "syntax_fmt": "SUNIONCARD numkeys key [key ...] [APPROX] [LIMIT limit]",
  "complexity": "O(N) where N is the total number of elements in all given sets.",
  "group": "set",
  "command_flags": ["readonly","movablekeys"],
  "acl_categories": ["@read","@set","@slow"],
  "since": "8.10.0",
  "arity": -3,
  "key_specs": [{"RO":true,"access":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"firstkey":1,"keynumidx":0,"keystep":1},"type":"keynum"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"examples","title":"Examples"},{"children":[{"id":"approximate-cardinality","title":"Approximate cardinality"}],"id":"details","title":"Details"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"see-also","title":"See also"},{"id":"related-topics","title":"Related topics"}]}

,
  "codeExamples": []
}
```

> [!NOTE]
> This command's behavior varies in clustered Redis environments. See the [multi-key operations](https://redis.io/docs/latest/develop/using-commands/multi-key-operations) page for more information.


Returns the cardinality of the union of the given sets. This is the count-only counterpart of [`SUNION`](https://redis.io/docs/latest/commands/sunion): it returns just the number of distinct elements in the union, not the members themselves.

## Required arguments

<details open><summary><code>numkeys</code></summary>

The number of keys that follow.

</details>

<details open><summary><code>key [key ...]</code></summary>

One or more set keys to union.

</details>

## Optional arguments

<details open><summary><code>APPROX</code></summary>

Return an approximate cardinality instead of an exact count.

</details>

<details open><summary><code>LIMIT limit</code></summary>

Stop counting once the cardinality reaches `limit`. `0` (the default) means no limit.

</details>

## Examples


redis> SADD key1 "a"
(integer) 1
redis> SADD key1 "b"
(integer) 1
redis> SADD key1 "c"
(integer) 1
redis> SADD key2 "c"
(integer) 1
redis> SADD key2 "d"
(integer) 1
redis> SADD key2 "e"
(integer) 1
redis> SUNION key1 key2
1) "a"
2) "c"
3) "d"
4) "b"
5) "e"
redis> SUNIONCARD 2 key1 key2
(integer) 5
redis> SUNIONCARD 2 key1 key2 LIMIT 3
(integer) 3


## Details

Keys that do not exist are considered to be empty sets.

When provided with the optional `LIMIT` argument (which defaults to `0`, meaning unlimited), if the union cardinality reaches `limit` partway through the computation, the command stops and returns `limit` as the cardinality. This ensures a significant speedup for queries where the limit is lower than the actual union cardinality. `LIMIT` works in both exact and approximate modes.

### Approximate cardinality

By default, `SUNIONCARD` returns the exact union cardinality. With the `APPROX` option, it instead uses [HyperLogLog](https://redis.io/docs/latest/develop/data-types/probabilistic/hyperloglogs) internally to estimate the cardinality with a standard error of about 0.81%, without materializing the full union. This is useful for very large unions, where computing an exact count is expensive in both time and memory.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Integer reply](../../develop/reference/protocol-spec#integers): the number of elements in the resulting union.

**RESP3:**

[Integer reply](../../develop/reference/protocol-spec#integers): the number of elements in the resulting union.



## See also

[`SUNION`](https://redis.io/docs/latest/commands/sunion) | [`SUNIONSTORE`](https://redis.io/docs/latest/commands/sunionstore)

## Related topics

- [Redis sets](https://redis.io/docs/latest/develop/data-types/sets)
- [Multi-key operations](https://redis.io/docs/latest/develop/using-commands/multi-key-operations)


