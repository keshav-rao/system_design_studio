# PEXPIRETIME

```json metadata
{
  "schema_version": 2,
  "title": "PEXPIRETIME",
  "description": "Returns the expiration time of a key as a Unix milliseconds timestamp.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"}],
  "syntax_fmt": "PEXPIRETIME key",
  "complexity": "O(1)",
  "group": "generic",
  "command_flags": ["readonly","fast"],
  "acl_categories": ["@keyspace","@read","@fast"],
  "since": "7.0.0",
  "arity": 2,
  "key_specs": [{"RO":true,"access":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

`PEXPIRETIME` has the same semantic as [`EXPIRETIME`](https://redis.io/docs/latest/commands/expiretime), but returns the absolute Unix expiration timestamp in milliseconds instead of seconds.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key.

</details>

## Examples


redis> SET mykey "Hello"
OK
redis> PEXPIREAT mykey 33177117420000
(integer) 1
redis> PEXPIRETIME mykey
(integer) 33177117420000


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Integer reply](../../develop/reference/protocol-spec#integers): Expiration Unix timestamp in milliseconds.
* [Integer reply](../../develop/reference/protocol-spec#integers): `-1` if the key exists but has no associated expiration time.
* [Integer reply](../../develop/reference/protocol-spec#integers): `-2` if the key does not exist.

**RESP3:**

One of the following:
* [Integer reply](../../develop/reference/protocol-spec#integers): Expiration Unix timestamp in milliseconds.
* [Integer reply](../../develop/reference/protocol-spec#integers): `-1` if the key exists but has no associated expiration time.
* [Integer reply](../../develop/reference/protocol-spec#integers): `-2` if the key does not exist.



