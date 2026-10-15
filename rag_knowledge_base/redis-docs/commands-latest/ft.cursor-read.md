# FT.CURSOR READ

```json metadata
{
  "schema_version": 2,
  "title": "FT.CURSOR READ",
  "description": "Reads from a cursor",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"index","type":"string"},{"name":"cursor_id","type":"integer"},{"name":"read size","optional":true,"token":"COUNT","type":"integer"}],
  "syntax_fmt": "FT.CURSOR READ index cursor_id [COUNT read size]",
  "complexity": "O(1)",
  "group": "search",
  "acl_categories": ["@read","@search"],
  "since": "1.1.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"see-also","title":"See also"},{"id":"related-topics","title":"Related topics"}]}

,
  "codeExamples": []
}
```


Read next results from an existing cursor

[Examples](#examples)

See [Cursor API](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/aggregations#cursor-api) for more details.

## Required arguments

<details open>
<summary><code>index</code></summary>

is index name.
</details>

<details open>
<summary><code>cursor_id</code></summary>

is id of the cursor.
</details>

<details open>
<summary><code>[COUNT read_size]</code></summary>

is number of results to read. This parameter overrides `COUNT` specified in [`FT.AGGREGATE`](https://redis.io/docs/latest/commands/ft.aggregate).
</details>

## Examples

<details open>
<summary><b>Read next results from a cursor</b></summary>


127.0.0.1:6379> FT.CURSOR READ idx 342459320 COUNT 50

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis Cloud<br />Flexible & Annual | Redis Cloud<br />Free & Fixed | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Array](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) with search results and metadata.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: cursor not found.

**RESP3:**

One of the following:
* [Map](https://redis.io/docs/latest/develop/reference/protocol-spec#maps) with structured search results and metadata.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: cursor not found.



## See also

[`FT.CURSOR DEL`](https://redis.io/docs/latest/commands/ft.cursor-del) | [`FT.AGGREGATE`](https://redis.io/docs/latest/commands/ft.aggregate)

## Related topics

- [RediSearch](https://redis.io/docs/latest/develop/ai/search-and-query)
- [Search commands in MULTI/EXEC transactions and Lua scripts](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/transactions)

