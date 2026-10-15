# ARDEL

```json metadata
{
  "schema_version": 2,
  "title": "ARDEL",
  "description": "Deletes elements at the specified indices in an array.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"key_spec_index":0,"name":"key","type":"key"},{"multiple":true,"name":"index","type":"integer"}],
  "syntax_fmt": "ARDEL key index [index ...]",
  "complexity": "O(N) where N is the number of indices to delete",
  "group": "array",
  "command_flags": ["WRITE","FAST"],
  "acl_categories": ["@write","@array","@fast"],
  "since": "8.8.0",
  "arity": -3,
  "key_specs": [{"begin_search":{"index":{"pos":1}},"find_keys":{"range":{"lastkey":0,"limit":0,"step":1}},"flags":["RW","DELETE"]}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Deletes elements at the specified indices in an array.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key that holds the array.

</details>

<details open><summary><code>index</code></summary>

One or more zero-based integer indices of the elements to delete. Deleting an index that does not exist counts as zero elements deleted and does not modify the array.

</details>

## Examples


redis> ARSET myarray 0 "a"
(integer) 1
redis> ARSET myarray 1 "b"
(integer) 1
redis> ARSET myarray 2 "c"
(integer) 1
redis> ARDEL myarray 1
(integer) 1
redis> ARGET myarray 1
(nil)
redis> ARDEL myarray 0 2
(integer) 2
redis> ARCOUNT myarray
(integer) 0


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Integer reply](../../develop/reference/protocol-spec#integers): Number of elements deleted.

**RESP3:**

[Integer reply](../../develop/reference/protocol-spec#integers): Number of elements deleted.



