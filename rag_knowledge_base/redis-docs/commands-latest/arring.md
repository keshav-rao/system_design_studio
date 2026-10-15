# ARRING

```json metadata
{
  "schema_version": 2,
  "title": "ARRING",
  "description": "Inserts values into a ring buffer of specified size, wrapping and truncating as needed.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"key_spec_index":0,"name":"key","type":"key"},{"name":"size","type":"integer"},{"multiple":true,"name":"value","type":"string"}],
  "syntax_fmt": "ARRING key size value [value ...]",
  "complexity": "O(M) normally, O(N+M) on ring resize, where N is the maximum of the old and new ring size and M is the number of inserted values",
  "group": "array",
  "command_flags": ["WRITE","DENYOOM"],
  "acl_categories": ["@write","@array","@slow"],
  "since": "8.8.0",
  "arity": -4,
  "key_specs": [{"begin_search":{"index":{"pos":1}},"find_keys":{"range":{"lastkey":0,"limit":0,"step":1}},"flags":["RW","UPDATE"]}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Inserts values into a ring buffer of specified size, wrapping and truncating as needed.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key that holds the array.

</details>

<details open><summary><code>size</code></summary>

The size of the ring buffer window. Each value is inserted at `insert_idx % size`, wrapping back to index `0` when the end of the window is reached. When the buffer is full, newer values overwrite older ones. If `size` is smaller than the current window, the array is truncated to fit.

</details>

<details open><summary><code>value</code></summary>

One or more string values to insert into the ring buffer. Each value is placed at the next position in the ring and the cursor advances accordingly.

</details>

## Examples


redis> ARRING readings 3 "v0"
(integer) 0
redis> ARRING readings 3 "v1"
(integer) 1
redis> ARRING readings 3 "v2"
(integer) 2
redis> ARRING readings 3 "v3"
(integer) 0
redis> ARGET readings 0
"v3"
redis> ARCOUNT readings
(integer) 3
redis> ARLASTITEMS readings 3
1) "v1"
2) "v2"
3) "v3"


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Integer reply](../../develop/reference/protocol-spec#integers): The last index where a value was inserted.

**RESP3:**

[Integer reply](../../develop/reference/protocol-spec#integers): The last index where a value was inserted.



