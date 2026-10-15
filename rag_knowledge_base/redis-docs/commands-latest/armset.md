# ARMSET

```json metadata
{
  "schema_version": 2,
  "title": "ARMSET",
  "description": "Sets multiple index-value pairs in an array.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"key_spec_index":0,"name":"key","type":"key"},{"arguments":[{"name":"index","type":"integer"},{"name":"value","type":"string"}],"multiple":true,"name":"data","type":"block"}],
  "syntax_fmt": "ARMSET key index value [index value ...]",
  "complexity": "O(N) where N is the number of pairs",
  "group": "array",
  "command_flags": ["WRITE","DENYOOM","FAST"],
  "acl_categories": ["@write","@array","@fast"],
  "since": "8.8.0",
  "arity": -4,
  "key_specs": [{"begin_search":{"index":{"pos":1}},"find_keys":{"range":{"lastkey":0,"limit":0,"step":1}},"flags":["RW","UPDATE"]}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Sets multiple index-value pairs in an array.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key that holds the array.

</details>

<details open><summary><code>data</code></summary>

One or more `index value` pairs. Each `index` is a zero-based integer specifying where to write, and each `value` is the string to store at that position. Pairs may be non-contiguous and in any order.

</details>

## Examples


redis> ARMSET myarray 0 "alpha" 5 "beta" 100 "gamma"
(integer) 3
redis> ARGET myarray 0
"alpha"
redis> ARGET myarray 5
"beta"
redis> ARGET myarray 100
"gamma"


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Integer reply](../../develop/reference/protocol-spec#integers): Number of new slots that were set (previously empty).

**RESP3:**

[Integer reply](../../develop/reference/protocol-spec#integers): Number of new slots that were set (previously empty).



