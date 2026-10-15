# FUNCTION KILL

```json metadata
{
  "schema_version": 2,
  "title": "FUNCTION KILL",
  "description": "Terminates a function during execution.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "FUNCTION KILL",
  "complexity": "O(1)",
  "group": "scripting",
  "command_flags": ["noscript","allow_busy"],
  "acl_categories": ["@slow","@scripting"],
  "since": "7.0.0",
  "arity": 2,
  "tableOfContents": {"sections":[{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Kill a function that is currently executing.

The `FUNCTION KILL` command can be used only on functions that did not modify the dataset during their execution (since stopping a read-only function does not violate the scripting engine's guaranteed atomicity).

For more information please refer to [Introduction to Redis Functions](https://redis.io/docs/latest/develop/programmability/functions-intro).

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.

**RESP3:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.



