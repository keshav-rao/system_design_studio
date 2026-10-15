# JSON.FORGET

```json metadata
{
  "schema_version": 2,
  "title": "JSON.FORGET",
  "description": "Deletes a value",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"key","type":"key"},{"name":"path","optional":true,"type":"string"}],
  "syntax_fmt": "JSON.FORGET key [path]",
  "complexity": "O(N) when path is evaluated to a single value where N is the size of the deleted value, O(N) when path is evaluated to multiple values, where N is the size of the key",
  "group": "json",
  "acl_categories": ["@json","@write","@slow"],
  "since": "1.0.0",
  "tableOfContents": {"sections":[{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

See [`JSON.DEL`](https://redis.io/docs/latest/commands/json.del).

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

**RESP2:**

[Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers): the number of paths deleted (0 or more).

**RESP3:**

[Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers): the number of paths deleted (0 or more).



