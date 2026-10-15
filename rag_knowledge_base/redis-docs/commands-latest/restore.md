# RESTORE

```json metadata
{
  "schema_version": 2,
  "title": "RESTORE",
  "description": "Creates a key from the serialized representation of a value.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"},{"display_text":"ttl","name":"ttl","type":"integer"},{"display_text":"serialized-value","name":"serialized-value","type":"string"},{"display_text":"replace","name":"replace","optional":true,"since":"3.0.0","token":"REPLACE","type":"pure-token"},{"display_text":"absttl","name":"absttl","optional":true,"since":"5.0.0","token":"ABSTTL","type":"pure-token"},{"display_text":"seconds","name":"seconds","optional":true,"since":"5.0.0","token":"IDLETIME","type":"integer"},{"display_text":"frequency","name":"frequency","optional":true,"since":"5.0.0","token":"FREQ","type":"integer"}],
  "syntax_fmt": "RESTORE key ttl serialized-value [REPLACE] [ABSTTL]\n  [IDLETIME seconds] [FREQ frequency]",
  "complexity": "O(1) to create the new key and additional O(N*M) to reconstruct the serialized value, where N is the number of Redis objects composing the value and M their average size. For small string values the time complexity is thus O(1)+O(1*M) where M is small, so simply O(1). However for sorted set values the complexity is O(N*M*log(N)) because inserting values into sorted sets is O(log(N)).",
  "group": "generic",
  "command_flags": ["write","denyoom"],
  "acl_categories": ["@keyspace","@write","@slow","@dangerous"],
  "since": "2.6.0",
  "arity": -4,
  "key_specs": [{"OW":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"},"update":true}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Create a key associated with a value that is obtained by deserializing the
provided serialized value (obtained via [`DUMP`](https://redis.io/docs/latest/commands/dump)).

If `ttl` is 0 the key is created without any expire, otherwise the specified
expire time (in milliseconds) is set.

If the `ABSTTL` modifier was used, `ttl` should represent an absolute
[Unix timestamp](http://en.wikipedia.org/wiki/Unix_time) (in milliseconds) in which the key will expire.

For eviction purposes, you may use the `IDLETIME` or `FREQ` modifiers. See
[`OBJECT`](https://redis.io/docs/latest/commands/object) for more information.

`RESTORE` will return a "Target key name is busy" error when `key` already
exists unless you use the `REPLACE` modifier.

`RESTORE` checks the RDB version and data checksum.
If they don't match an error is returned.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key to create.

</details>

<details open><summary><code>ttl</code></summary>

The time to live for the key, in milliseconds. `0` means no expiration. With `ABSTTL`, this is an absolute Unix timestamp in milliseconds.

</details>

<details open><summary><code>serialized-value</code></summary>

The serialized value, as produced by `DUMP`.

</details>

## Optional arguments

<details open><summary><code>REPLACE</code></summary>

Replace the key if it already exists.

</details>

<details open><summary><code>ABSTTL</code></summary>

Interpret `ttl` as an absolute Unix timestamp in milliseconds rather than a relative time.

</details>

<details open><summary><code>IDLETIME seconds</code></summary>

Set the key's idle time (for LRU eviction) to this many seconds.

</details>

<details open><summary><code>FREQ frequency</code></summary>

Set the key's access-frequency counter (for LFU eviction) to this value.

</details>

## Examples

```
redis> DEL mykey
0
redis> RESTORE mykey 0 "\n\x17\x17\x00\x00\x00\x12\x00\x00\x00\x03\x00\
                        x00\xc0\x01\x00\x04\xc0\x02\x00\x04\xc0\x03\x00\
                        xff\x04\x00u#<\xc0;.\xe9\xdd"
OK
redis> TYPE mykey
list
redis> LRANGE mykey 0 -1
1) "1"
2) "2"
3) "3"
```

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Not supported">&#x274c; Active-Active\*</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Not supported">&#x274c; Active-Active\*</nobr></span> | \*Only supported for module keys. |

## Return information

**RESP2:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.

**RESP3:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.



