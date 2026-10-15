# SCRIPT EXISTS

```json metadata
{
  "schema_version": 2,
  "title": "SCRIPT EXISTS",
  "description": "Determines whether server-side Lua scripts exist in the script cache.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"sha1","multiple":true,"name":"sha1","type":"string"}],
  "syntax_fmt": "SCRIPT EXISTS sha1 [sha1 ...]",
  "complexity": "O(N) with N being the number of scripts to check (so checking a single script is an O(1) operation).",
  "group": "scripting",
  "command_flags": ["noscript"],
  "acl_categories": ["@slow","@scripting"],
  "since": "2.6.0",
  "arity": -3,
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Returns information about the existence of the scripts in the script cache.

This command accepts one or more SHA1 digests and returns a list of 1 and 0 values to indicate whether each script exists in the script cache. Before you run a pipeline, use this command to check whether Redis has loaded the scripts you need. For missing scripts, use [`SCRIPT LOAD`](https://redis.io/docs/latest/commands/script-load); then use [`EVALSHA`](https://redis.io/docs/latest/commands/evalsha) instead of [`EVAL`](https://redis.io/docs/latest/commands/eval) in the pipeline to save bandwidth.

For more information about [`EVAL`](https://redis.io/docs/latest/commands/eval) scripts see [Introduction to Eval Scripts](https://redis.io/docs/latest/develop/programmability/eval-intro).

## Required arguments

<details open><summary><code>sha1 [sha1 ...]</code></summary>

One or more SHA1 digests to look up in the script cache.

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Array reply](../../develop/reference/protocol-spec#arrays): an array of integers that correspond to the specified SHA1 digest arguments.

**RESP3:**

[Array reply](../../develop/reference/protocol-spec#arrays): an array of integers that correspond to the specified SHA1 digest arguments.



