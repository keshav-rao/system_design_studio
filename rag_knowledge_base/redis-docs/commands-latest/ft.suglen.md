# FT.SUGLEN

```json metadata
{
  "schema_version": 2,
  "title": "FT.SUGLEN",
  "description": "Gets the size of an auto-complete suggestion dictionary",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"key","type":"string"}],
  "syntax_fmt": "FT.SUGLEN key",
  "complexity": "O(1)",
  "group": "suggestion",
  "acl_categories": ["@search"],
  "since": "1.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"see-also","title":"See also"},{"id":"related-topics","title":"Related topics"}]}

,
  "codeExamples": []
}
```


Get the size of an auto-complete suggestion dictionary

[Examples](#examples)

## Required arguments

<details open>
<summary><code>key</code></summary>

is suggestion dictionary key.
</details>

## Examples

<details open>
<summary><b>Get the size of an auto-complete suggestion dictionary</b></summary>


127.0.0.1:6379> FT.SUGLEN sug
(integer) 2

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | Not supported on clustered databases. |

## Return information

**RESP2:**

[Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers): number of suggestions in the dictionary.

**RESP3:**

[Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers): number of suggestions in the dictionary.



## See also

[`FT.SUGADD`](https://redis.io/docs/latest/commands/ft.sugadd) | [`FT.SUGDEL`](https://redis.io/docs/latest/commands/ft.sugdel) | [`FT.SUGGET`](https://redis.io/docs/latest/commands/ft.sugget) 

## Related topics

[RediSearch](https://redis.io/docs/latest/develop/ai/search-and-query)
