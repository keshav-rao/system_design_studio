# MODULE UNLOAD

```json metadata
{
  "schema_version": 2,
  "title": "MODULE UNLOAD",
  "description": "Unloads a module.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"name","name":"name","type":"string"}],
  "syntax_fmt": "MODULE UNLOAD name",
  "complexity": "O(1)",
  "group": "server",
  "command_flags": ["admin","noscript","no_async_loading"],
  "acl_categories": ["@admin","@slow","@dangerous"],
  "since": "4.0.0",
  "arity": 3,
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Unloads a module.

This command unloads the module specified by `name`. Note that the module's name
is reported by the [`MODULE LIST`](https://redis.io/docs/latest/commands/module-list) command, and may differ from the dynamic
library's filename.

Known limitations:

*   Modules that register custom data types can not be unloaded.

## Required arguments

<details open><summary><code>name</code></summary>

The name of the module to unload, as reported by `MODULE LIST`.

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK` if the module was unloaded.

**RESP3:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK` if the module was unloaded.



