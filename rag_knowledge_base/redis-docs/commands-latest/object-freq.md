# OBJECT FREQ

```json metadata
{
  "schema_version": 2,
  "title": "OBJECT FREQ",
  "description": "Returns the logarithmic access frequency counter of a Redis object.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"}],
  "syntax_fmt": "OBJECT FREQ key",
  "complexity": "O(1)",
  "group": "generic",
  "command_flags": ["readonly"],
  "acl_categories": ["@keyspace","@read","@slow"],
  "since": "4.0.0",
  "arity": 3,
  "key_specs": [{"RO":true,"begin_search":{"spec":{"index":2},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

This command returns the logarithmic access frequency counter of a Redis object stored at `key`.

The command is only available when the `maxmemory-policy` configuration directive is set to one of the LFU policies.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key.

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
[Integer reply](../../develop/reference/protocol-spec#integers): the counter's value.
[Nil reply](../../develop/reference/protocol-spec#bulk-strings): if _key_ doesn't exist.

**RESP3:**

One of the following:
[Integer reply](../../develop/reference/protocol-spec#integers): the counter's value.
[Null reply](../../develop/reference/protocol-spec#nulls): if _key_ doesn't exist.



