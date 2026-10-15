# FT.CONFIG SET

```json metadata
{
  "schema_version": 2,
  "title": "FT.CONFIG SET",
  "description": "Sets runtime configuration options",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"option","type":"string"},{"name":"value","type":"string"}],
  "syntax_fmt": "FT.CONFIG SET option value",
  "complexity": "O(1)",
  "group": "search",
  "acl_categories": ["@admin","@search"],
  "since": "1.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"see-also","title":"See also"},{"id":"related-topics","title":"Related topics"}]}

,
  "codeExamples": []
}
```


Set the value of a RediSearch configuration parameter.

Values set using `FT.CONFIG SET` are not persisted after server restart.

RediSearch configuration parameters are detailed in [Configuration parameters](https://redis.io/docs/latest/develop/ai/search-and-query/administration/configuration).

> [!NOTE]
> As detailed in the link above, not all RediSearch configuration parameters can be set at runtime.

[Examples](#examples)

## Required arguments

<details open>
<summary><code>option</code></summary> 

is name of the configuration option, or '*' for all. 
</details>

<details open>
<summary><code>value</code></summary> 

is value of the configuration option. 
</details>

## Examples

<details open>
<summary><b>Set runtime configuration options</b></summary>


127.0.0.1:6379> FT.CONFIG SET TIMEOUT 42
OK

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis Cloud<br />Flexible & Annual | Redis Cloud<br />Free & Fixed | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:-----------------|:------|
| <span title="Not supported"><nobr>&#x26A0;&#xFE0F; Not supported</span><sup>1</sup> | <span title="Not supported"><nobr>&#x26A0;&#xFE0F; Not supported</span><sup>2</sup> | <span title="Not supported"><nobr>&#x274c; Not supported</nobr></span> |  |

1. Use [`rladmin`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin) or the [REST API](https://redis.io/docs/latest/operate/rs/references/rest-api) to change search and query configuration for Redis Software. See [search and query configuration compatibility with Redis Software](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/search/config) for more information and examples.

2. [Contact support](https://redis.com/company/support/) to view the current configuration values or request configuration changes for Flexible or Annual Redis Cloud subscriptions.

## Return information

**RESP2:**

One of the following:
* [Simple string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-strings): `OK` if executed correctly.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: invalid option, invalid value.

**RESP3:**

One of the following:
* [Simple string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-strings): `OK` if executed correctly.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: invalid option, invalid value.



## See also

[`FT.CONFIG GET`](https://redis.io/docs/latest/commands/ft.config-get) | [`FT.CONFIG HELP`](https://redis.io/docs/latest/commands/ft.config-help) 

## Related topics

[RediSearch](https://redis.io/docs/latest/develop/ai/search-and-query)

