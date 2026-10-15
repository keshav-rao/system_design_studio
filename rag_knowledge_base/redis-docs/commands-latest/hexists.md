# HEXISTS

```json metadata
{
  "schema_version": 2,
  "title": "HEXISTS",
  "description": "Determines whether a field exists in a hash.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"},{"display_text":"field","name":"field","type":"string"}],
  "syntax_fmt": "HEXISTS key field",
  "complexity": "O(1)",
  "group": "hash",
  "command_flags": ["readonly","fast"],
  "acl_categories": ["@read","@hash","@fast"],
  "since": "2.0.0",
  "arity": 3,
  "key_specs": [{"RO":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Returns if `field` is an existing field in the hash stored at `key`.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key that holds the hash.

</details>

<details open><summary><code>field</code></summary>

The field to check for existence.

</details>

## Examples


redis> HSET myhash field1 "foo"
(integer) 1
redis> HEXISTS myhash field1
(integer) 1
redis> HEXISTS myhash field2
(integer) 0


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Integer reply](../../develop/reference/protocol-spec#integers): `0` if the hash does not contain the field, or the key does not exist.
* [Integer reply](../../develop/reference/protocol-spec#integers): `1` if the hash contains the field.

**RESP3:**

One of the following:
* [Integer reply](../../develop/reference/protocol-spec#integers): `0` if the hash does not contain the field, or the key does not exist.
* [Integer reply](../../develop/reference/protocol-spec#integers): `1` if the hash contains the field.



