# XLEN

```json metadata
{
  "schema_version": 2,
  "title": "XLEN",
  "description": "Return the number of messages in a stream.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"}],
  "syntax_fmt": "XLEN key",
  "complexity": "O(1)",
  "group": "stream",
  "command_flags": ["readonly","fast"],
  "acl_categories": ["@read","@stream","@fast"],
  "since": "5.0.0",
  "arity": 2,
  "key_specs": [{"RO":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Returns the number of entries inside a stream. If the specified key does not
exist the command returns zero, as if the stream was empty.
However note that unlike other Redis types, zero-length streams are
possible, so you should call [`TYPE`](https://redis.io/docs/latest/commands/type) or [`EXISTS`](https://redis.io/docs/latest/commands/exists) in order to check if
a key exists or not.

Streams are not auto-deleted once they have no entries inside (for instance
after an [`XDEL`](https://redis.io/docs/latest/commands/xdel) call), because the stream may have consumer groups
associated with it.

## Required arguments

<details open><summary><code>key</code></summary>

The stream key.

</details>

## Examples


redis> XADD mystream * item 1
"1784722083902-0"
redis> XADD mystream * item 2
"1784722083903-0"
redis> XADD mystream * item 3
"1784722083904-0"
redis> XLEN mystream
(integer) 3


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Integer reply](../../develop/reference/protocol-spec#integers): the number of entries of the stream at _key_.

**RESP3:**

[Integer reply](../../develop/reference/protocol-spec#integers): the number of entries of the stream at _key_.



