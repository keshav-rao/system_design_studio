# FUNCTION FLUSH

```json metadata
{
  "schema_version": 2,
  "title": "FUNCTION FLUSH",
  "description": "Deletes all libraries and functions.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"arguments":[{"display_text":"async","name":"async","token":"ASYNC","type":"pure-token"},{"display_text":"sync","name":"sync","token":"SYNC","type":"pure-token"}],"name":"flush-type","optional":true,"type":"oneof"}],
  "syntax_fmt": "FUNCTION FLUSH [ASYNC | SYNC]",
  "complexity": "O(N) where N is the number of functions deleted",
  "group": "scripting",
  "command_flags": ["write","noscript"],
  "acl_categories": ["@write","@slow","@scripting"],
  "since": "7.0.0",
  "arity": -2,
  "tableOfContents": {"sections":[{"id":"optional-arguments","title":"Optional arguments"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Deletes all the libraries.

Unless called with the optional mode argument, the `lazyfree-lazy-user-flush` configuration directive sets the effective behavior.

For more information please refer to [Introduction to Redis Functions](https://redis.io/docs/latest/develop/programmability/functions-intro).

## Optional arguments

<details open><summary><code>ASYNC | SYNC</code></summary>

Flush the function libraries asynchronously (`ASYNC`) or synchronously (`SYNC`). The default is set by the `lazyfree-lazy-user-flush` configuration directive.

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.

**RESP3:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.



