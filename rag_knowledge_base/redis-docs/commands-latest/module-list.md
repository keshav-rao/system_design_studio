# MODULE LIST

```json metadata
{
  "schema_version": 2,
  "title": "MODULE LIST",
  "description": "Returns all loaded modules.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "MODULE LIST",
  "complexity": "O(N) where N is the number of loaded modules.",
  "group": "server",
  "command_flags": ["admin","noscript"],
  "acl_categories": ["@admin","@slow","@dangerous"],
  "since": "4.0.0",
  "arity": 2,
  "tableOfContents": {"sections":[{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Returns information about the modules loaded to the server.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Array reply](../../develop/reference/protocol-spec#arrays): list of loaded modules. Each element in the list represents a represents a module, and is in itself a list of property names and their values. The following properties is reported for each loaded module:
* name: the name of the module.
* ver: the version of the module.

**RESP3:**

[Array reply](../../develop/reference/protocol-spec#arrays): list of loaded modules. Each element in the list represents a represents a module, and is a [Map reply](../../develop/reference/protocol-spec#maps) of property names and their values. The following properties is reported for each loaded module:
* name: the name of the module.
* ver: the version of the module.



