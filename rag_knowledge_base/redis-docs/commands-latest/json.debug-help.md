# JSON.DEBUG HELP

```json metadata
{
  "schema_version": 2,
  "title": "JSON.DEBUG HELP",
  "description": "Shows helpful information",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "JSON.DEBUG HELP",
  "complexity": "N/A",
  "group": "json",
  "since": "1.0.0",
  "tableOfContents": {"sections":[{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"see-also","title":"See also"},{"id":"related-topics","title":"Related topics"}]}

,
  "codeExamples": []
}
```

Return helpful information about the [`JSON.DEBUG`](https://redis.io/docs/latest/commands/json.debug) command

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

**RESP2:**

[Array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) of [bulk string replies](https://redis.io/docs/latest/develop/reference/protocol-spec#bulk-strings) containing helpful messages about the JSON.DEBUG command.

**RESP3:**

[Array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) of [bulk string replies](https://redis.io/docs/latest/develop/reference/protocol-spec#bulk-strings) containing helpful messages about the JSON.DEBUG command.



## See also

[`JSON.DEBUG`](https://redis.io/docs/latest/commands/json.debug) 

## Related topics

* [RedisJSON](https://redis.io/docs/latest/develop/data-types/json)
* [Index and search JSON documents](https://redis.io/docs/latest/develop/ai/search-and-query/indexing)

