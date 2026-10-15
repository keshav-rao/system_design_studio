# UNLINK

```json metadata
{
  "schema_version": 2,
  "title": "UNLINK",
  "description": "Asynchronously deletes one or more keys.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"multiple":true,"name":"key","type":"key"}],
  "syntax_fmt": "UNLINK key [key ...]",
  "complexity": "O(1) for each key removed regardless of its size. Then the command does O(N) work in a different thread in order to reclaim memory, where N is the number of allocations the deleted objects where composed of.",
  "group": "generic",
  "command_flags": ["write","fast"],
  "acl_categories": ["@keyspace","@write","@fast"],
  "since": "4.0.0",
  "arity": -2,
  "key_specs": [{"RM":true,"begin_search":{"spec":{"index":1},"type":"index"},"delete":true,"find_keys":{"spec":{"keystep":1,"lastkey":-1,"limit":0},"type":"range"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

> [!NOTE]
> This command's behavior varies in clustered Redis environments. See the [multi-key operations](https://redis.io/docs/latest/develop/using-commands/multi-key-operations) page for more information.


This command is very similar to [`DEL`](https://redis.io/docs/latest/commands/del): it removes the specified keys.
Just like [`DEL`](https://redis.io/docs/latest/commands/del) a key is ignored if it does not exist. However the command
performs the actual memory reclaiming in a different thread, so it is not
blocking, while [`DEL`](https://redis.io/docs/latest/commands/del) is. This is where the command name comes from: the
command just unlinks the keys from the keyspace. The actual removal
will happen later asynchronously.

## Required arguments

<details open><summary><code>key [key ...]</code></summary>

One or more keys to delete asynchronously.

</details>

## Examples


redis> SET key1 "Hello"
OK
redis> SET key2 "World"
OK
redis> UNLINK key1 key2 key3
(integer) 2


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Integer reply](../../develop/reference/protocol-spec#integers): the number of keys that were unlinked.

**RESP3:**

[Integer reply](../../develop/reference/protocol-spec#integers): the number of keys that were unlinked.



