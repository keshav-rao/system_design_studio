# HSETNX

```json metadata
{
  "schema_version": 2,
  "title": "HSETNX",
  "description": "Sets the value of a field in a hash only when the field doesn't exist.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"},{"display_text":"field","name":"field","type":"string"},{"display_text":"value","name":"value","type":"string"}],
  "syntax_fmt": "HSETNX key field value",
  "complexity": "O(1)",
  "group": "hash",
  "command_flags": ["write","denyoom","fast"],
  "acl_categories": ["@write","@hash","@fast"],
  "since": "2.0.0",
  "arity": 4,
  "key_specs": [{"RW":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"},"insert":true}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Sets `field` in the hash stored at `key` to `value`, only if `field` does not
yet exist.
If `key` does not exist, a new key holding a hash is created.
If `field` already exists, this operation has no effect.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key that holds the hash.

</details>

<details open><summary><code>field</code></summary>

The field to set, only if it does not already exist.

</details>

<details open><summary><code>value</code></summary>

The value to set.

</details>

## Examples


redis> HSETNX myhash field "Hello"
(integer) 1
redis> HSETNX myhash field "World"
(integer) 0
redis> HGET myhash field
"Hello"


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Integer reply](../../develop/reference/protocol-spec#integers): `0` if the field already exists in the hash and no operation was performed.
* [Integer reply](../../develop/reference/protocol-spec#integers): `1` if the field is a new field in the hash and the value was set.

**RESP3:**

One of the following:
* [Integer reply](../../develop/reference/protocol-spec#integers): `0` if the field already exists in the hash and no operation was performed.
* [Integer reply](../../develop/reference/protocol-spec#integers): `1` if the field is a new field in the hash and the value was set.



