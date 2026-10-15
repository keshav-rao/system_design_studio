# MSET

```json metadata
{
  "schema_version": 2,
  "title": "MSET",
  "description": "Atomically creates or modifies the string values of one or more keys.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"arguments":[{"display_text":"key","key_spec_index":0,"name":"key","type":"key"},{"display_text":"value","name":"value","type":"string"}],"multiple":true,"name":"data","type":"block"}],
  "syntax_fmt": "MSET key value [key value ...]",
  "complexity": "O(N) where N is the number of keys to set.",
  "group": "string",
  "command_flags": ["write","denyoom"],
  "acl_categories": ["@write","@string","@slow"],
  "since": "1.0.1",
  "arity": -3,
  "key_specs": [{"OW":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":2,"lastkey":-1,"limit":0},"type":"range"},"update":true}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

> [!NOTE]
> This command's behavior varies in clustered Redis environments. See the [multi-key operations](https://redis.io/docs/latest/develop/using-commands/multi-key-operations) page for more information.


Sets the given keys to their respective values.
`MSET` replaces existing values with new values, just as regular [`SET`](https://redis.io/docs/latest/commands/set).
See [`MSETNX`](https://redis.io/docs/latest/commands/msetnx) if you don't want to overwrite existing values.

`MSET` is atomic, so all given keys are set at once.
It is not possible for clients to see that some of the keys were updated while
others are unchanged.

## Required arguments

<details open><summary><code>key value [key value ...]</code></summary>

One or more key-value pairs to set.

</details>

## Examples


redis> MSET key1 "Hello" key2 "World"
OK
redis> GET key1
"Hello"
redis> GET key2
"World"


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): always `OK` because `MSET` can't fail.

**RESP3:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): always `OK` because `MSET` can't fail.



