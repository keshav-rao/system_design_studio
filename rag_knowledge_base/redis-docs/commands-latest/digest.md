# DIGEST

```json metadata
{
  "schema_version": 2,
  "title": "DIGEST",
  "description": "Returns the hash digest of a string value.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"}],
  "syntax_fmt": "DIGEST key",
  "complexity": "O(N) where N is the length of the string value.",
  "group": "string",
  "command_flags": ["readonly","fast"],
  "acl_categories": ["@read","@string","@fast"],
  "since": "8.4.0",
  "arity": 2,
  "key_specs": [{"RO":true,"access":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"children":[{"id":"hash-digest","title":"Hash Digest"}],"id":"details","title":"Details"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Get the [hash digest](#hash-digest) for the value stored in the specified key as a hexadecimal string. Keys must be of type string.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key.

</details>

## Examples


> SET key1 "Hello world"
OK
> DIGEST key1
"b6acb9d84a38ff74"


## Details

### Hash Digest {#hash-digest}

A hash digest is a fixed-size numerical representation of a string value, computed using the XXH3 hash algorithm. Redis uses this hash digest for efficient comparison operations without needing to compare the full string content. You can use these hash digests with the [SET](https://redis.io/docs/latest/commands/set) command's `IFDEQ` and `IFDNE` options, and also the [DELEX](https://redis.io/docs/latest/commands/delex) command's `IFDEQ` and `IFDNE` options.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

One of the following:

- [Null bulk string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#bulk-strings) if the key does not exist.
- [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) if the key exists but holds a value which is not a string.
- [Bulk string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#bulk-strings) the hash digest of the value stored in the key as a hexadecimal string.

**RESP3:**

One of the following:

- [Null bulk string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#bulk-strings) if the key does not exist.
- [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) if the key exists but holds a value which is not a string.
- [Bulk string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#bulk-strings) the hash digest of the value stored in the key as a hexadecimal string.



