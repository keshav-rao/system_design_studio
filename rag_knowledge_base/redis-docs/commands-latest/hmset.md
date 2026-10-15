# HMSET

```json metadata
{
  "schema_version": 2,
  "title": "HMSET",
  "description": "Sets the values of multiple fields.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"},{"arguments":[{"display_text":"field","name":"field","type":"string"},{"display_text":"value","name":"value","type":"string"}],"multiple":true,"name":"data","type":"block"}],
  "syntax_fmt": "HMSET key field value [field value ...]",
  "complexity": "O(N) where N is the number of fields being set.",
  "group": "hash",
  "command_flags": ["write","denyoom","fast"],
  "acl_categories": ["@write","@hash","@fast"],
  "since": "2.0.0",
  "arity": -4,
  "key_specs": [{"RW":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"},"update":true}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Sets the specified fields to their respective values in the hash stored at
`key`.
This command overwrites any specified fields already existing in the hash.
If `key` does not exist, a new key holding a hash is created.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key that holds the hash.

</details>

<details open><summary><code>field value [field value ...]</code></summary>

One or more field-value pairs to set in the hash.

</details>

## Examples


redis> HMSET myhash field1 "Hello" field2 "World"
OK
redis> HGET myhash field1
"Hello"
redis> HGET myhash field2
"World"


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | Deprecated as of Redis v4.0.0. |

## Return information

**RESP2:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.

**RESP3:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.



