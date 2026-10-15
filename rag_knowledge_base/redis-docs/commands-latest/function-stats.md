# FUNCTION STATS

```json metadata
{
  "schema_version": 2,
  "title": "FUNCTION STATS",
  "description": "Returns information about a function during execution.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "FUNCTION STATS",
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

Return information about the function that's currently running and information about the available execution engines.

The reply is map with two keys:

1. `running_script`: information about the running script.
  If there's no in-flight function, the server replies with a _nil_.
  Otherwise, this is a map with the following keys:
  * **name:** the name of the function.
  * **command:** the command and arguments used for invoking the function.
  * **duration_ms:** the function's runtime duration in milliseconds.
2. `engines`: this is a map of maps. Each entry in the map represent a single engine.
   Engine map contains statistics about the engine like number of functions and number of libraries.

You can use this command to inspect the invocation of a long-running function and decide whether kill it with the [`FUNCTION KILL`](https://redis.io/docs/latest/commands/function-kill) command.

For more information please refer to [Introduction to Redis Functions](https://redis.io/docs/latest/develop/programmability/functions-intro).

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Array reply](../../develop/reference/protocol-spec#arrays): information about the function that's currently running and information about the available execution engines.

**RESP3:**

[Map reply](../../develop/reference/protocol-spec#maps): information about the function that's currently running and information about the available execution engines.



