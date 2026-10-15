# HKEYS

```json metadata
{
  "schema_version": 2,
  "title": "HKEYS",
  "description": "Returns all fields in a hash.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"}],
  "syntax_fmt": "HKEYS key",
  "complexity": "O(N) where N is the size of the hash.",
  "group": "hash",
  "command_flags": ["readonly"],
  "acl_categories": ["@read","@hash","@slow"],
  "since": "2.0.0",
  "arity": 2,
  "key_specs": [{"RO":true,"access":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Returns all field names in the hash stored at `key`.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key that holds the hash.

</details>

## Examples


redis> HSET myhash field1 "Hello"
(integer) 1
redis> HSET myhash field2 "World"
(integer) 1
redis> HKEYS myhash
1) "field1"
2) "field2"


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Array reply](../../develop/reference/protocol-spec#arrays): a list of fields in the hash, or an empty list when the key does not exist

**RESP3:**

[Array reply](../../develop/reference/protocol-spec#arrays): a list of fields in the hash, or an empty list when the key does not exist.



