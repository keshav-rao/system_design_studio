# SCRIPT LOAD

```json metadata
{
  "schema_version": 2,
  "title": "SCRIPT LOAD",
  "description": "Loads a server-side Lua script to the script cache.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"script","name":"script","type":"string"}],
  "syntax_fmt": "SCRIPT LOAD script",
  "complexity": "O(N) with N being the length in bytes of the script body.",
  "group": "scripting",
  "command_flags": ["noscript","stale"],
  "acl_categories": ["@slow","@scripting"],
  "since": "2.6.0",
  "arity": 3,
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Load a script into the scripts cache, without executing it.
After the specified command is loaded into the script cache it will be callable
using [`EVALSHA`](https://redis.io/docs/latest/commands/evalsha) with the correct SHA1 digest of the script, exactly like after
the first successful invocation of [`EVAL`](https://redis.io/docs/latest/commands/eval).

The script is guaranteed to stay in the script cache forever (unless `SCRIPT
FLUSH` is called).

The command works in the same way even if the script was already present in the
script cache.

For more information about [`EVAL`](https://redis.io/docs/latest/commands/eval) scripts please see [Introduction to Eval Scripts](https://redis.io/docs/latest/develop/programmability/eval-intro).

## Required arguments

<details open><summary><code>script</code></summary>

The Lua script to load into the script cache. Its SHA1 digest is returned for use with `EVALSHA`.

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): the SHA1 digest of the script added into the script cache.

**RESP3:**

[Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): the SHA1 digest of the script added into the script cache.



