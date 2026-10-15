# GETSET

```json metadata
{
  "schema_version": 2,
  "title": "GETSET",
  "description": "Returns the previous string value of a key after setting it to a new value.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"},{"display_text":"value","name":"value","type":"string"}],
  "syntax_fmt": "GETSET key value",
  "complexity": "O(1)",
  "group": "string",
  "command_flags": ["write","denyoom","fast"],
  "acl_categories": ["@write","@string","@fast"],
  "since": "1.0.0",
  "arity": 3,
  "key_specs": [{"RW":true,"access":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"},"update":true}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"children":[{"id":"design-pattern","title":"Design pattern"}],"id":"details","title":"Details"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Atomically sets `key` to `value` and returns the old value stored at `key`.
Returns an error when `key` exists but does not hold a string value.  Any 
previous time to live associated with the key is discarded on successful 
[`SET`](https://redis.io/docs/latest/commands/set) operation.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key.

</details>

<details open><summary><code>value</code></summary>

The new value to set.

</details>

## Examples


redis> SET mykey "Hello"
OK
redis> GETSET mykey "World"
"Hello"
redis> GET mykey
"World"


## Details

### Design pattern

You can use GETSET with [INCR](https://redis.io/docs/latest/commands/incr) to count events and reset the counter atomically.
For example, you can call [INCR](https://redis.io/docs/latest/commands/incr) on the key `mycounter` each time an event occurs. When you need to read the counter value and reset it to zero atomically, call GETSET.
This can be done using `GETSET mycounter "0"`:


redis> INCR mycounter
(integer) 1
redis> GETSET mycounter "0"
"1"
redis> GET mycounter
"0"


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | Deprecated as of Redis v6.2.0. |

## Return information

**RESP2:**

One of the following:
* [Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): the old value stored at the key.
* [Nil reply](../../develop/reference/protocol-spec#bulk-strings): if the key does not exist.

**RESP3:**

One of the following:
* [Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): the old value stored at the key.
* [Null reply](../../develop/reference/protocol-spec#nulls): if the key does not exist.



