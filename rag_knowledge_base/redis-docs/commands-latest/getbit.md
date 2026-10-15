# GETBIT

```json metadata
{
  "schema_version": 2,
  "title": "GETBIT",
  "description": "Returns a bit value by offset.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"},{"display_text":"offset","name":"offset","type":"integer"}],
  "syntax_fmt": "GETBIT key offset",
  "complexity": "O(1)",
  "group": "bitmap",
  "command_flags": ["readonly","fast"],
  "acl_categories": ["@read","@bitmap","@fast"],
  "since": "2.2.0",
  "arity": 3,
  "key_specs": [{"RO":true,"access":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Returns the bit value at _offset_ in the string value stored at _key_.

When _offset_ is beyond the string length, the string is assumed to be a
contiguous space with 0 bits.
When _key_ does not exist it is assumed to be an empty string, so _offset_ is
always out of range and the value is also assumed to be a contiguous space with
0 bits.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key that holds the string.

</details>

<details open><summary><code>offset</code></summary>

The zero-based bit offset to read.

</details>

## Examples


redis> SETBIT mykey 7 1
(integer) 0
redis> GETBIT mykey 0
(integer) 0
redis> GETBIT mykey 7
(integer) 1
redis> GETBIT mykey 100
(integer) 0


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

The bit value stored at _offset_, one of the following:
* [Integer reply](../../develop/reference/protocol-spec#integers): `0`.
* [Integer reply](../../develop/reference/protocol-spec#integers): `1`.

**RESP3:**

The bit value stored at _offset_, one of the following:
* [Integer reply](../../develop/reference/protocol-spec#integers): `0`.
* [Integer reply](../../develop/reference/protocol-spec#integers): `1`.



