# SDIFFCARD

```json metadata
{
  "schema_version": 2,
  "title": "SDIFFCARD",
  "description": "Returns the number of members of the difference between the first set and all successive sets.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"numkeys","name":"numkeys","type":"integer"},{"display_text":"key","key_spec_index":0,"multiple":true,"name":"key","type":"key"},{"display_text":"limit","name":"limit","optional":true,"token":"LIMIT","type":"integer"}],
  "syntax_fmt": "SDIFFCARD numkeys key [key ...] [LIMIT limit]",
  "complexity": "O(N) where N is the total number of elements in all given sets.",
  "group": "set",
  "command_flags": ["readonly","movablekeys"],
  "acl_categories": ["@read","@set","@slow"],
  "since": "8.10.0",
  "arity": -3,
  "key_specs": [{"RO":true,"access":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"firstkey":1,"keynumidx":0,"keystep":1},"type":"keynum"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"examples","title":"Examples"},{"id":"details","title":"Details"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"see-also","title":"See also"},{"id":"related-topics","title":"Related topics"}]}

,
  "codeExamples": []
}
```

> [!NOTE]
> This command's behavior varies in clustered Redis environments. See the [multi-key operations](https://redis.io/docs/latest/develop/using-commands/multi-key-operations) page for more information.


Returns the cardinality of the difference between the first set and all the successive sets. This is the count-only counterpart of [`SDIFF`](https://redis.io/docs/latest/commands/sdiff): it returns just the number of elements in the difference, not the members themselves.

## Required arguments

<details open><summary><code>numkeys</code></summary>

The number of keys that follow.

</details>

<details open><summary><code>key [key ...]</code></summary>

One or more set keys. The result counts the members of the first set that are not present in any of the subsequent sets.

</details>

## Optional arguments

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
redis> SDIFF key1 key2
1) "b"
2) "a"
redis> SDIFFCARD 2 key1 key2
(integer) 2
redis> SDIFFCARD 2 key1 key2 LIMIT 1
(integer) 1


## Details

Keys that do not exist are considered to be empty sets.

When provided with the optional `LIMIT` argument (which defaults to `0`, meaning unlimited), if the difference cardinality reaches `limit` partway through the computation, the command stops and returns `limit` as the cardinality. This ensures a significant speedup for queries where the limit is lower than the actual difference cardinality.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Integer reply](../../develop/reference/protocol-spec#integers): the number of elements in the resulting difference.

**RESP3:**

[Integer reply](../../develop/reference/protocol-spec#integers): the number of elements in the resulting difference.



## See also

[`SDIFF`](https://redis.io/docs/latest/commands/sdiff) | [`SDIFFSTORE`](https://redis.io/docs/latest/commands/sdiffstore)

## Related topics

- [Redis sets](https://redis.io/docs/latest/develop/data-types/sets)
- [Multi-key operations](https://redis.io/docs/latest/develop/using-commands/multi-key-operations)


