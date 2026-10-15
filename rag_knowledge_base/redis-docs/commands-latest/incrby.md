# INCRBY

```json metadata
{
  "schema_version": 2,
  "title": "INCRBY",
  "description": "Increments the integer value of a key by a number. Uses 0 as initial value if the key doesn't exist.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"},{"display_text":"increment","name":"increment","type":"integer"}],
  "syntax_fmt": "INCRBY key increment",
  "complexity": "O(1)",
  "group": "string",
  "command_flags": ["write","denyoom","fast"],
  "acl_categories": ["@write","@string","@fast"],
  "since": "1.0.0",
  "arity": 3,
  "key_specs": [{"RW":true,"access":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"},"update":true}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Increments the number stored at `key` by `increment`.
If the key does not exist, it is set to `0` before performing the operation.
An error is returned if the key contains a value of the wrong type or contains a
string that can not be represented as integer.
This operation is limited to 64-bit signed integers.

See [`INCR`](https://redis.io/docs/latest/commands/incr) for extra information on increment/decrement operations.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key.

</details>

<details open><summary><code>increment</code></summary>

The integer amount to add to the value.

</details>

## Examples


redis> SET mykey "10"
OK
redis> INCRBY mykey 5
(integer) 15


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Integer reply](../../develop/reference/protocol-spec#integers): the value of the key after the increment.

**RESP3:**

[Integer reply](../../develop/reference/protocol-spec#integers): the value of the key after the increment.



