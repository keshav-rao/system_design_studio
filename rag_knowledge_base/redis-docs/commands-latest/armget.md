# ARMGET

```json metadata
{
  "schema_version": 2,
  "title": "ARMGET",
  "description": "Gets values at multiple indices in an array.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"key_spec_index":0,"name":"key","type":"key"},{"multiple":true,"name":"index","type":"integer"}],
  "syntax_fmt": "ARMGET key index [index ...]",
  "complexity": "O(N) where N is the number of indices",
  "group": "array",
  "command_flags": ["READONLY","FAST"],
  "acl_categories": ["@read","@array","@fast"],
  "since": "8.8.0",
  "arity": -3,
  "key_specs": [{"begin_search":{"index":{"pos":1}},"find_keys":{"range":{"lastkey":0,"limit":0,"step":1}},"flags":["RO","ACCESS"]}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Gets values at multiple indices in an array.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key that holds the array.

</details>

<details open><summary><code>index</code></summary>

One or more zero-based integer indices of the elements to retrieve. The reply preserves the order of the requested indices and returns nil for any index that is not set.

</details>

## Examples


redis> ARMSET myarray 0 "a" 1 "b" 5 "c"
(integer) 3
redis> ARMGET myarray 0 1 5 3
1) "a"
2) "b"
3) "c"
4) (nil)


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Array reply](../../develop/reference/protocol-spec#arrays)

**RESP3:**

[Array reply](../../develop/reference/protocol-spec#arrays)



