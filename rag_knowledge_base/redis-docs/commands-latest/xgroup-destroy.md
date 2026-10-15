# XGROUP DESTROY

```json metadata
{
  "schema_version": 2,
  "title": "XGROUP DESTROY",
  "description": "Destroys a consumer group.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"},{"display_text":"group","name":"group","type":"string"}],
  "syntax_fmt": "XGROUP DESTROY key group",
  "complexity": "O(N) where N is the number of entries in the group's pending entries list (PEL).",
  "group": "stream",
  "command_flags": ["write"],
  "acl_categories": ["@write","@stream","@slow"],
  "since": "5.0.0",
  "arity": 4,
  "key_specs": [{"RW":true,"begin_search":{"spec":{"index":2},"type":"index"},"delete":true,"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

The `XGROUP DESTROY` command completely destroys a consumer group.

The consumer group will be destroyed even if there are active consumers, and pending messages, so make sure to call this command only when really needed.

## Required arguments

<details open><summary><code>key</code></summary>

The stream key.

</details>

<details open><summary><code>group</code></summary>

The name of the consumer group to destroy.

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Integer reply](../../develop/reference/protocol-spec#integers): the number of destroyed consumer groups, either 0 or 1.

**RESP3:**

[Integer reply](../../develop/reference/protocol-spec#integers): the number of destroyed consumer groups, either 0 or 1.



