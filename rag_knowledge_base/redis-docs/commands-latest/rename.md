# RENAME

```json metadata
{
  "schema_version": 2,
  "title": "RENAME",
  "description": "Renames a key and overwrites the destination.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"},{"display_text":"newkey","key_spec_index":1,"name":"newkey","type":"key"}],
  "syntax_fmt": "RENAME key newkey",
  "complexity": "O(1)",
  "group": "generic",
  "command_flags": ["write"],
  "acl_categories": ["@keyspace","@write","@slow"],
  "since": "1.0.0",
  "arity": 3,
  "key_specs": [{"RW":true,"access":true,"begin_search":{"spec":{"index":1},"type":"index"},"delete":true,"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"}},{"OW":true,"begin_search":{"spec":{"index":2},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"},"update":true}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

> [!NOTE]
> This command's behavior varies in clustered Redis environments. See the [multi-key operations](https://redis.io/docs/latest/develop/using-commands/multi-key-operations) page for more information.


Renames `key` to `newkey`.
It returns an error when `key` does not exist.
If `newkey` already exists it is overwritten, when this happens `RENAME` executes an implicit [`DEL`](https://redis.io/docs/latest/commands/del) operation, so if the deleted key contains a very big value it may cause high latency even if `RENAME` itself is usually a constant-time operation.

In Cluster mode, both `key` and `newkey` must be in the same **hash slot**, meaning that in practice only keys that have the same hash tag can be reliably renamed in cluster.

## Required arguments

<details open><summary><code>key</code></summary>

The key to rename.

</details>

<details open><summary><code>newkey</code></summary>

The new key name. An existing key with this name is overwritten.

</details>

## Examples


redis> SET mykey "Hello"
OK
redis> RENAME mykey myotherkey
OK
redis> GET myotherkey
"Hello"


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active\*</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active\*</nobr></span> | For Active-Active or clustered databases, the original key and new key must be in the same hash slot.<br /><br />\*Not supported for stream consumer group info. |

## Return information

**RESP2:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.

**RESP3:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.



