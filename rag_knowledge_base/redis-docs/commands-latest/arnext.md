# ARNEXT

```json metadata
{
  "schema_version": 2,
  "title": "ARNEXT",
  "description": "Returns the next index ARINSERT would use.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"key_spec_index":0,"name":"key","type":"key"}],
  "syntax_fmt": "ARNEXT key",
  "complexity": "O(1)",
  "group": "array",
  "command_flags": ["READONLY","FAST"],
  "acl_categories": ["@read","@array","@fast"],
  "since": "8.8.0",
  "arity": 2,
  "key_specs": [{"begin_search":{"index":{"pos":1}},"find_keys":{"range":{"lastkey":0,"limit":0,"step":1}},"flags":["RO","ACCESS"]}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Returns the next index ARINSERT would use.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key that holds the array.

</details>

## Examples


redis> ARINSERT myarray "a"
(integer) 0
redis> ARINSERT myarray "b"
(integer) 1
redis> ARNEXT myarray
(integer) 2


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Integer reply](../../develop/reference/protocol-spec#integers): The next index ARINSERT would use. Returns 0 for missing keys or when no insert happened yet.
* [Nil reply](../../develop/reference/protocol-spec#null-bulk-strings): Null when the insertion cursor is exhausted (next insert would overflow).

**RESP3:**

One of the following:
* [Integer reply](../../develop/reference/protocol-spec#integers): The next index ARINSERT would use. Returns 0 for missing keys or when no insert happened yet.
* [Null reply](../../develop/reference/protocol-spec#nulls): Null when the insertion cursor is exhausted (next insert would overflow).



