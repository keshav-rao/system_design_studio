# HEXPIRETIME

```json metadata
{
  "schema_version": 2,
  "title": "HEXPIRETIME",
  "description": "Returns the expiration time of a hash field as a Unix timestamp, in seconds.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"},{"arguments":[{"display_text":"numfields","name":"numfields","type":"integer"},{"display_text":"field","multiple":true,"name":"field","type":"string"}],"name":"fields","token":"FIELDS","type":"block"}],
  "syntax_fmt": "HEXPIRETIME key FIELDS numfields field [field ...]",
  "complexity": "O(N) where N is the number of specified fields",
  "group": "hash",
  "command_flags": ["readonly","fast"],
  "acl_categories": ["@read","@hash","@fast"],
  "since": "7.4.0",
  "arity": -5,
  "key_specs": [{"RO":true,"access":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Returns the absolute Unix timestamp in seconds since Unix epoch at which the given key's field(s) will expire.

See also the [`HPEXPIRETIME`](https://redis.io/docs/latest/commands/hpexpiretime) command, which returns the same information with millisecond resolution.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key that holds the hash.

</details>

<details open><summary><code>FIELDS numfields field [field ...]</code></summary>

The hash fields to retrieve the expiration time for. `numfields` is the number of fields, followed by that many field names.

</details>

## Examples


redis> HSET mykey field1 "hello" field2 "world"
(integer) 2
redis> HEXPIRE mykey 300  FIELDS 2 field1 field2
1) (integer) 1
2) (integer) 1
redis> HEXPIRETIME mykey FIELDS 2 field1 field2
1) (integer) 1715705914
2) (integer) 1715705914


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

* [Array reply](../../develop/reference/protocol-spec#arrays). For each field:
    - [Integer reply](../../develop/reference/protocol-spec#integers): `-2` if no such field exists in the provided hash key, or the provided key does not exist.
    - [Integer reply](../../develop/reference/protocol-spec#integers): `-1` if the field exists but has no associated expiration set.
    - [Integer reply](../../develop/reference/protocol-spec#integers): the expiration (Unix timestamp) in seconds.

**RESP3:**

* [Array reply](../../develop/reference/protocol-spec#arrays). For each field:
    - [Integer reply](../../develop/reference/protocol-spec#integers): `-2` if no such field exists in the provided hash key, or the provided key does not exist.
    - [Integer reply](../../develop/reference/protocol-spec#integers): `-1` if the field exists but has no associated expiration set.
    - [Integer reply](../../develop/reference/protocol-spec#integers): the expiration (Unix timestamp) in seconds.



