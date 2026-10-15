# SCARD

```json metadata
{
  "schema_version": 2,
  "title": "SCARD",
  "description": "Returns the number of members in a set.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"}],
  "syntax_fmt": "SCARD key",
  "complexity": "O(1)",
  "group": "set",
  "command_flags": ["readonly","fast"],
  "acl_categories": ["@read","@set","@fast"],
  "since": "1.0.0",
  "arity": 2,
  "key_specs": [{"RO":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Returns the set cardinality (number of elements) of the set stored at `key`.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key that holds the set.

</details>

## Examples


redis> SADD myset "Hello"
(integer) 1
redis> SADD myset "World"
(integer) 1
redis> SCARD myset
(integer) 2


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Integer reply](../../develop/reference/protocol-spec#integers): the cardinality (number of elements) of the set, or `0` if the key does not exist.

**RESP3:**

[Integer reply](../../develop/reference/protocol-spec#integers): The cardinality (number of elements) of the set, or 0 if the key does not exist.



