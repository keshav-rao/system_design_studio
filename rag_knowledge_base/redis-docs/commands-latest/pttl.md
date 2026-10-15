# PTTL

```json metadata
{
  "schema_version": 2,
  "title": "PTTL",
  "description": "Returns the expiration time in milliseconds of a key.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"}],
  "syntax_fmt": "PTTL key",
  "complexity": "O(1)",
  "group": "generic",
  "command_flags": ["readonly","fast"],
  "acl_categories": ["@keyspace","@read","@fast"],
  "since": "2.6.0",
  "arity": 2,
  "key_specs": [{"RO":true,"access":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Like [`TTL`](https://redis.io/docs/latest/commands/ttl) this command returns the remaining time to live of a key that has an
expire set, with the sole difference that [`TTL`](https://redis.io/docs/latest/commands/ttl) returns the amount of remaining
time in seconds while `PTTL` returns it in milliseconds.

In Redis 2.6 or older the command returns `-1` if the key does not exist or if the key exist but has no associated expire.

Starting with Redis 2.8 the return value in case of error changed:

* The command returns `-2` if the key does not exist.
* The command returns `-1` if the key exists but has no associated expire.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key.

</details>

## Examples


redis> SET mykey "Hello"
OK
redis> EXPIRE mykey 1
(integer) 1
redis> PTTL mykey
(integer) 1000


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Integer reply](../../develop/reference/protocol-spec#integers): TTL in milliseconds.
* [Integer reply](../../develop/reference/protocol-spec#integers): `-1` if the key exists but has no associated expiration.
* [Integer reply](../../develop/reference/protocol-spec#integers): `-2` if the key does not exist.

**RESP3:**

One of the following:
* [Integer reply](../../develop/reference/protocol-spec#integers): TTL in milliseconds.
* [Integer reply](../../develop/reference/protocol-spec#integers): `-1` if the key exists but has no associated expiration.
* [Integer reply](../../develop/reference/protocol-spec#integers): `-2` if the key does not exist.



