# TOUCH

```json metadata
{
  "schema_version": 2,
  "title": "TOUCH",
  "description": "Returns the number of existing keys out of those specified after updating the time they were last accessed.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"multiple":true,"name":"key","type":"key"}],
  "syntax_fmt": "TOUCH key [key ...]",
  "complexity": "O(N) where N is the number of keys that will be touched.",
  "group": "generic",
  "command_flags": ["readonly","fast"],
  "acl_categories": ["@keyspace","@read","@fast"],
  "since": "3.2.1",
  "arity": -2,
  "key_specs": [{"RO":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":-1,"limit":0},"type":"range"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

> [!NOTE]
> This command's behavior varies in clustered Redis environments. See the [multi-key operations](https://redis.io/docs/latest/develop/using-commands/multi-key-operations) page for more information.


Alters the last access time of one or more keys.
A key is ignored if it does not exist.

## Required arguments

<details open><summary><code>key [key ...]</code></summary>

One or more keys whose last-access time to update.

</details>

## Examples


redis> SET key1 "Hello"
OK
redis> SET key2 "World"
OK
redis> TOUCH key1 key2
(integer) 2


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Integer reply](../../develop/reference/protocol-spec#integers): the number of touched keys.

**RESP3:**

[Integer reply](../../develop/reference/protocol-spec#integers): the number of touched keys.



