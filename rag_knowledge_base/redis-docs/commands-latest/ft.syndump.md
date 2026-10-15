# FT.SYNDUMP

```json metadata
{
  "schema_version": 2,
  "title": "FT.SYNDUMP",
  "description": "Dumps the contents of a synonym group",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"index","type":"string"}],
  "syntax_fmt": "FT.SYNDUMP index",
  "complexity": "O(1)",
  "group": "search",
  "acl_categories": ["@search"],
  "since": "1.2.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"see-also","title":"See also"},{"id":"related-topics","title":"Related topics"}]}

,
  "codeExamples": []
}
```


Dump the contents of a synonym group

[Examples](#examples)

## Required arguments

<details open>
<summary><code>index</code></summary>

is index name.
</details>

Use FT.SYNDUMP to dump the synonyms data structure. This command returns a list of synonym terms and their synonym group ids.

## Examples

<details open>
<summary><b>Return the contents of a synonym group</b></summary>


127.0.0.1:6379> FT.SYNDUMP idx
1) "shalom"
2) 1) "synonym1"
   2) "synonym2"
3) "hi"
4) 1) "synonym1"
5) "hello"
6) 1) "synonym1"

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis Cloud<br />Flexible & Annual | Redis Cloud<br />Free & Fixed | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Array](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) of synonym terms and their associated synonym groups.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: no such index.

**RESP3:**

One of the following:
* [Map](https://redis.io/docs/latest/develop/reference/protocol-spec#maps) where keys are synonym terms and values are arrays of their associated synonym groups.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: no such index.



## See also

[`FT.SYNUPDATE`](https://redis.io/docs/latest/commands/ft.synupdate) 

## Related topics

[RediSearch](https://redis.io/docs/latest/develop/ai/search-and-query)
