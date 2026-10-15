# COMMAND LIST

```json metadata
{
  "schema_version": 2,
  "title": "COMMAND LIST",
  "description": "Returns a list of command names.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"arguments":[{"display_text":"module-name","name":"module-name","token":"MODULE","type":"string"},{"display_text":"category","name":"category","token":"ACLCAT","type":"string"},{"display_text":"pattern","name":"pattern","token":"PATTERN","type":"pattern"}],"name":"filterby","optional":true,"token":"FILTERBY","type":"oneof"}],
  "syntax_fmt": "COMMAND LIST [FILTERBY \u003cMODULE module-name | ACLCAT category |\n  PATTERN pattern\u003e]",
  "complexity": "O(N) where N is the total number of Redis commands",
  "group": "server",
  "command_flags": ["loading","stale"],
  "acl_categories": ["@slow","@connection"],
  "since": "7.0.0",
  "arity": -2,
  "tableOfContents": {"sections":[{"id":"optional-arguments","title":"Optional arguments"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Return an array of the Redis server's command names.

## Optional arguments

<details open><summary><code>FILTERBY MODULE module-name | ACLCAT category | PATTERN pattern</code></summary>

Filter the listed commands by module (`MODULE`), [ACL category](https://redis.io/docs/latest/operate/oss_and_stack/management/security/acl#command-categories) (`ACLCAT`), or a glob-style name pattern (`PATTERN`).

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Array reply](../../develop/reference/protocol-spec#arrays): a list of command names.

**RESP3:**

[Array reply](../../develop/reference/protocol-spec#arrays): a list of command names.



