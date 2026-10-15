# TYPE

```json metadata
{
  "schema_version": 2,
  "title": "TYPE",
  "description": "Determines the type of value stored at a key.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"}],
  "syntax_fmt": "TYPE key",
  "complexity": "O(1)",
  "group": "generic",
  "command_flags": ["readonly","fast"],
  "acl_categories": ["@keyspace","@read","@fast"],
  "since": "1.0.0",
  "arity": 2,
  "key_specs": [{"RO":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Returns the string representation of the type of the value stored at `key`.
The different types that can be returned are: `string`, `list`, `set`, `zset`,
`hash`, `stream`, and `vectorset`.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key.

</details>

## Examples


redis> SET key1 "value"
OK
redis> LPUSH key2 "value"
(integer) 1
redis> SADD key3 "value"
(integer) 1
redis> TYPE key1
string
redis> TYPE key2
list
redis> TYPE key3
set


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): the type of _key_, or `none` when _key_ doesn't exist.

**RESP3:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): the type of _key_, or `none` when _key_ doesn't exist.



