# MOVE

```json metadata
{
  "schema_version": 2,
  "title": "MOVE",
  "description": "Moves a key to another database.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"},{"display_text":"db","name":"db","type":"integer"}],
  "syntax_fmt": "MOVE key db",
  "complexity": "O(1)",
  "group": "generic",
  "command_flags": ["write","fast"],
  "acl_categories": ["@keyspace","@write","@fast"],
  "since": "1.0.0",
  "arity": 3,
  "key_specs": [{"RW":true,"access":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"},"update":true}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Move `key` from the currently selected database (see [`SELECT`](https://redis.io/docs/latest/commands/select)) to the specified
destination database.
When `key` already exists in the destination database, or it does not exist in
the source database, it does nothing.
It is possible to use `MOVE` as a locking primitive because of this.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key.

</details>

<details open><summary><code>db</code></summary>

The destination database index.

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | Redis Software does not support shared databases due to potential negative performance impacts and blocks any related commands. |

## Return information

**RESP2:**

One of the following:
* [Integer reply](../../develop/reference/protocol-spec#integers): `1` if _key_ was moved.
* [Integer reply](../../develop/reference/protocol-spec#integers): `0` if _key_ wasn't moved.

**RESP3:**

One of the following:
* [Integer reply](../../develop/reference/protocol-spec#integers): `1` if _key_ was moved.
* [Integer reply](../../develop/reference/protocol-spec#integers): `0` if _key_ wasn't moved.



