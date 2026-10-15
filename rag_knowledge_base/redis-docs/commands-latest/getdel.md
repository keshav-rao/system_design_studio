# GETDEL

```json metadata
{
  "schema_version": 2,
  "title": "GETDEL",
  "description": "Returns the string value of a key after deleting the key.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"}],
  "syntax_fmt": "GETDEL key",
  "complexity": "O(1)",
  "group": "string",
  "command_flags": ["write","fast"],
  "acl_categories": ["@write","@string","@fast"],
  "since": "6.2.0",
  "arity": 2,
  "key_specs": [{"RW":true,"access":true,"begin_search":{"spec":{"index":1},"type":"index"},"delete":true,"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Get the value of `key` and delete the key.
This command is similar to [`GET`](https://redis.io/docs/latest/commands/get), except for the fact that it also deletes the key on success (if and only if the key's value type is a string).

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key to get and then delete.

</details>

## Examples


redis> SET mykey "Hello"
OK
redis> GETDEL mykey
"Hello"
redis> GET mykey
(nil)


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): the value of the key.
* [Nil reply](../../develop/reference/protocol-spec#bulk-strings): if the key does not exist or if the key's value type is not a string.

**RESP3:**

One of the following:
* [Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): the value of the key.
* [Null reply](../../develop/reference/protocol-spec#nulls): if the key does not exist or if the key's value type is not a string.



