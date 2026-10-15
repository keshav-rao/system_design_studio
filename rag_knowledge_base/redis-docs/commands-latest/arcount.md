# ARCOUNT

```json metadata
{
  "schema_version": 2,
  "title": "ARCOUNT",
  "description": "Returns the number of non-empty elements in an array.",
  "categories": ["docs","develop","oss","rs","rc","kubernetes","clients"],
  "arguments": [{"key_spec_index":0,"name":"key","type":"key"}],
  "syntax_fmt": "ARCOUNT key",
  "complexity": "O(1)",
  "group": "array",
  "command_flags": ["readonly","fast"],
  "acl_categories": ["@read","@array","@fast"],
  "since": "8.8.0",
  "arity": 2,
  "key_specs": [{"begin_search":{"index":{"pos":1}},"find_keys":{"range":{"lastkey":0,"limit":0,"step":1}},"flags":["ro","access"]}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Returns the number of non-empty elements in an array.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key that holds the array.

</details>

## Examples


redis> ARSET myarray 0 "a"
(integer) 1
redis> ARSET myarray 5 "b"
(integer) 1
redis> ARCOUNT myarray
(integer) 2


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Integer reply](../../develop/reference/protocol-spec#integers): The number of non-empty elements, or 0 if key does not exist.

**RESP3:**

[Integer reply](../../develop/reference/protocol-spec#integers): The number of non-empty elements, or 0 if key does not exist.



