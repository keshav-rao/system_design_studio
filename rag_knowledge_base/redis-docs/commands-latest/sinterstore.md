# SINTERSTORE

```json metadata
{
  "schema_version": 2,
  "title": "SINTERSTORE",
  "description": "Stores the intersect of multiple sets in a key.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"destination","key_spec_index":0,"name":"destination","type":"key"},{"display_text":"key","key_spec_index":1,"multiple":true,"name":"key","type":"key"}],
  "syntax_fmt": "SINTERSTORE destination key [key ...]",
  "complexity": "O(N*M) worst case where N is the cardinality of the smallest set and M is the number of sets.",
  "group": "set",
  "command_flags": ["write","denyoom"],
  "acl_categories": ["@write","@set","@slow"],
  "since": "1.0.0",
  "arity": -3,
  "key_specs": [{"OW":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"},"update":true},{"RO":true,"access":true,"begin_search":{"spec":{"index":2},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":-1,"limit":0},"type":"range"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"see-also","title":"See also"}]}

,
  "codeExamples": []
}
```

> [!NOTE]
> This command's behavior varies in clustered Redis environments. See the [multi-key operations](https://redis.io/docs/latest/develop/using-commands/multi-key-operations) page for more information.


This command is equal to [`SINTER`](https://redis.io/docs/latest/commands/sinter), but instead of returning the resulting set,
it is stored in `destination`.

If `destination` already exists, it is overwritten.

## Required arguments

<details open><summary><code>destination</code></summary>

The key to store the resulting set in.

</details>

<details open><summary><code>key [key ...]</code></summary>

One or more set keys to intersect.

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
redis> SINTERSTORE key key1 key2
(integer) 1
redis> SMEMBERS key
1) "c"


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Integer reply](../../develop/reference/protocol-spec#integers): the number of elements in the resulting set.

**RESP3:**

[Integer reply](../../develop/reference/protocol-spec#integers): the number of elements in the result set.



## See also

[`SINTER`](https://redis.io/docs/latest/commands/sinter) | [`SINTERCARD`](https://redis.io/docs/latest/commands/sintercard)
