# ARGET

```json metadata
{
  "schema_version": 2,
  "title": "ARGET",
  "description": "Gets the value at an index in an array.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"key_spec_index":0,"name":"key","type":"key"},{"name":"index","type":"integer"}],
  "syntax_fmt": "ARGET key index",
  "complexity": "O(1)",
  "group": "array",
  "command_flags": ["READONLY","FAST"],
  "acl_categories": ["@read","@array","@fast"],
  "since": "8.8.0",
  "arity": 3,
  "key_specs": [{"begin_search":{"index":{"pos":1}},"find_keys":{"range":{"lastkey":0,"limit":0,"step":1}},"flags":["RO","ACCESS"]}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Gets the value at an index in an array.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key that holds the array.

</details>

<details open><summary><code>index</code></summary>

The zero-based integer index of the element to retrieve.

</details>

## Examples


redis> ARSET myarray 0 "hello"
(integer) 1
redis> ARGET myarray 0
"hello"
redis> ARGET myarray 1
(nil)


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): The value at the given index.
* [Nil reply](../../develop/reference/protocol-spec#null-bulk-strings): Null reply if key or index does not exist.

**RESP3:**

One of the following:
* [Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): The value at the given index.
* [Null reply](../../develop/reference/protocol-spec#nulls): Null reply if key or index does not exist.



