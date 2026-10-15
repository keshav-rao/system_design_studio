# FT.CONFIG HELP

```json metadata
{
  "schema_version": 2,
  "title": "FT.CONFIG HELP",
  "description": "Help description of runtime configuration options",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"option","type":"string"}],
  "syntax_fmt": "FT.CONFIG HELP option",
  "complexity": "O(1)",
  "group": "search",
  "command_flags": ["readonly"],
  "acl_categories": ["@admin","@search"],
  "since": "1.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"see-also","title":"See also"},{"id":"related-topics","title":"Related topics"}]}

,
  "codeExamples": []
}
```


Describe configuration options

[Examples](#examples)

## Required arguments

<details open>
<summary><code>option</code></summary> 

is name of the configuration option, or '*' for all. 
</details>

## Examples

<details open>
<summary><b>Get configuration details</b></summary>


127.0.0.1:6379> FT.CONFIG HELP TIMEOUT
1) 1) TIMEOUT
   2) Description
   3) Query (search) timeout
   4) Value
   5) "42"

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis Cloud<br />Flexible & Annual | Redis Cloud<br />Free & Fixed | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:-----------------|:------|
| <span title="Not supported"><nobr>&#x274c; Not supported</span> | <span title="Not supported"><nobr>&#x274c; Not supported</span> | <span title="Not supported"><nobr>&#x274c; Not supported</nobr></span> |  |

## Return information

**RESP2:**

[Array](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) of help information.

**RESP3:**

[Array](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) of help information.



## See also

[`FT.CONFIG SET`](https://redis.io/docs/latest/commands/ft.config-set) | [`FT.CONFIG GET`](https://redis.io/docs/latest/commands/ft.config-get) 

## Related topics

[RediSearch](https://redis.io/docs/latest/develop/ai/search-and-query)
