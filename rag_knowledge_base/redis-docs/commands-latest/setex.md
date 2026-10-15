# SETEX

```json metadata
{
  "schema_version": 2,
  "title": "SETEX",
  "description": "Sets the string value and expiration time of a key. Creates the key if it doesn't exist.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"},{"display_text":"seconds","name":"seconds","type":"integer"},{"display_text":"value","name":"value","type":"string"}],
  "syntax_fmt": "SETEX key seconds value",
  "complexity": "O(1)",
  "group": "string",
  "command_flags": ["write","denyoom"],
  "acl_categories": ["@write","@string","@slow"],
  "since": "2.0.0",
  "arity": 4,
  "key_specs": [{"OW":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"},"update":true}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"see-also","title":"See also"}]}

,
  "codeExamples": []
}
```

Set `key` to hold the string `value` and set `key` to timeout after a given
number of seconds.
This command is equivalent to:

```
SET key value EX seconds
```

An error is returned when `seconds` is invalid.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key.

</details>

<details open><summary><code>seconds</code></summary>

The time to live, in seconds.

</details>

<details open><summary><code>value</code></summary>

The value to set.

</details>

## Examples


redis> SETEX mykey 10 "Hello"
OK
redis> TTL mykey
(integer) 10
redis> GET mykey
"Hello"


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.

**RESP3:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.



## See also

[`TTL`](https://redis.io/docs/latest/commands/ttl)

