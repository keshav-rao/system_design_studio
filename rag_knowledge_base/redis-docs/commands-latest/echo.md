# ECHO

```json metadata
{
  "schema_version": 2,
  "title": "ECHO",
  "description": "Returns the given string.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"message","name":"message","type":"string"}],
  "syntax_fmt": "ECHO message",
  "complexity": "O(1)",
  "group": "connection",
  "command_flags": ["loading","stale","fast"],
  "acl_categories": ["@fast","@connection"],
  "since": "1.0.0",
  "arity": 2,
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Returns `message`.

## Required arguments

<details open><summary><code>message</code></summary>

The message to echo back.

</details>

## Examples


redis> ECHO "Hello World!"
"Hello World!"


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): the given string.

**RESP3:**

[Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): the given string.



