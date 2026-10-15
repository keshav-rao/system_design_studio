# SINTERCARD

```json metadata
{
  "schema_version": 2,
  "title": "SINTERCARD",
  "description": "Returns the number of members of the intersect of multiple sets.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"numkeys","name":"numkeys","type":"integer"},{"display_text":"key","key_spec_index":0,"multiple":true,"name":"key","type":"key"},{"display_text":"limit","name":"limit","optional":true,"token":"LIMIT","type":"integer"}],
  "syntax_fmt": "SINTERCARD numkeys key [key ...] [LIMIT limit]",
  "complexity": "O(N*M) worst case where N is the cardinality of the smallest set and M is the number of sets.",
  "group": "set",
  "command_flags": ["readonly","movablekeys"],
  "acl_categories": ["@read","@set","@slow"],
  "since": "7.0.0",
  "arity": -3,
  "key_specs": [{"RO":true,"access":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"firstkey":1,"keynumidx":0,"keystep":1},"type":"keynum"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"see-also","title":"See also"}]}

,
  "codeExamples": []
}
```

> [!NOTE]
> This command's behavior varies in clustered Redis environments. See the [multi-key operations](https://redis.io/docs/latest/develop/using-commands/multi-key-operations) page for more information.


This command is similar to [`SINTER`](https://redis.io/docs/latest/commands/sinter), but instead of returning the result set, it returns just the cardinality of the result.
Returns the cardinality of the set which would result from the intersection of all the given sets.

Keys that do not exist are considered to be empty sets.
With one of the keys being an empty set, the resulting set is also empty (since set intersection with an empty set always results in an empty set).

By default, the command calculates the cardinality of the intersection of all given sets.
When provided with the optional `LIMIT` argument (which defaults to 0 and means unlimited), if the intersection cardinality reaches limit partway through the computation, the algorithm will exit and yield limit as the cardinality.
Such implementation ensures a significant speedup for queries where the limit is lower than the actual intersection cardinality.

## Required arguments

<details open><summary><code>numkeys</code></summary>

The number of keys that follow.

</details>

<details open><summary><code>key [key ...]</code></summary>

One or more set keys to intersect.

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
redis> SADD key1 "d"
(integer) 1
redis> SADD key2 "c"
(integer) 1
redis> SADD key2 "d"
(integer) 1
redis> SADD key2 "e"
(integer) 1
redis> SINTER key1 key2
1) "c"
2) "d"
redis> SINTERCARD 2 key1 key2
(integer) 2
redis> SINTERCARD 2 key1 key2 LIMIT 1
(integer) 1


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Integer reply](../../develop/reference/protocol-spec#integers): the number of elements in the resulting intersection.

**RESP3:**

[Integer reply](../../develop/reference/protocol-spec#integers): the number of elements in the resulting intersection.



## See also

[`SINTER`](https://redis.io/docs/latest/commands/sinter) | [`SINTERSTORE`](https://redis.io/docs/latest/commands/sinterstore)
