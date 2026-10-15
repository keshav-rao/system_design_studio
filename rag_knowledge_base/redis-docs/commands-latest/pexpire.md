# PEXPIRE

```json metadata
{
  "schema_version": 2,
  "title": "PEXPIRE",
  "description": "Sets the expiration time of a key in milliseconds.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"},{"display_text":"milliseconds","name":"milliseconds","type":"integer"},{"arguments":[{"display_text":"nx","name":"nx","token":"NX","type":"pure-token"},{"display_text":"xx","name":"xx","token":"XX","type":"pure-token"},{"display_text":"gt","name":"gt","token":"GT","type":"pure-token"},{"display_text":"lt","name":"lt","token":"LT","type":"pure-token"}],"name":"condition","optional":true,"since":"7.0.0","type":"oneof"}],
  "syntax_fmt": "PEXPIRE key milliseconds [NX | XX | GT | LT]",
  "complexity": "O(1)",
  "group": "generic",
  "command_flags": ["write","fast"],
  "acl_categories": ["@keyspace","@write","@fast"],
  "since": "2.6.0",
  "arity": -3,
  "key_specs": [{"RW":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"},"update":true}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

This command works exactly like [`EXPIRE`](https://redis.io/docs/latest/commands/expire) but the time to live of the key is
specified in milliseconds instead of seconds.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key to set a timeout on.

</details>

<details open><summary><code>milliseconds</code></summary>

The timeout, in milliseconds.

</details>

## Optional arguments

The following options modify the command's behavior. They are mutually exclusive.

<details open><summary><code>NX</code></summary>

Set expiry only when the key has no expiry.

</details>

<details open><summary><code>XX</code></summary>

Set expiry only when the key has an existing expiry.

</details>

<details open><summary><code>GT</code></summary>

Set expiry only when the new expiry is greater than the current one. A non-volatile key is treated as an infinite TTL for the purpose of `GT`.

</details>

<details open><summary><code>LT</code></summary>

Set expiry only when the new expiry is less than the current one. A non-volatile key is treated as an infinite TTL for the purpose of `LT`.

</details>

## Examples


redis> SET mykey "Hello"
OK
redis> PEXPIRE mykey 1500
(integer) 1
redis> TTL mykey
(integer) 2
redis> PTTL mykey
(integer) 1500
redis> PEXPIRE mykey 1000 XX
(integer) 1
redis> TTL mykey
(integer) 1
redis> PEXPIRE mykey 1000 NX
(integer) 0
redis> TTL mykey
(integer) 1


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Integer reply](../../develop/reference/protocol-spec#integers): `0` if the timeout was not set. For example, if the key doesn't exist, or the operation skipped because of the provided arguments.
* [Integer reply](../../develop/reference/protocol-spec#integers): `1` if the timeout was set.

**RESP3:**

One of the following:
* [Integer reply](../../develop/reference/protocol-spec#integers): `0` if the timeout was not set. For example, if the key doesn't exist, or the operation skipped because of the provided arguments.
* [Integer reply](../../develop/reference/protocol-spec#integers): `1` if the timeout was set.



