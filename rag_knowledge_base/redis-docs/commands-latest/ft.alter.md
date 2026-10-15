# FT.ALTER

```json metadata
{
  "schema_version": 2,
  "title": "FT.ALTER",
  "description": "Adds a new field to the index",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"index","type":"string"},{"name":"skipinitialscan","optional":true,"token":"SKIPINITIALSCAN","type":"pure-token"},{"name":"schema","token":"SCHEMA","type":"pure-token"},{"name":"add","token":"ADD","type":"pure-token"},{"name":"field","type":"string"},{"name":"options","type":"string"}],
  "syntax_fmt": "FT.ALTER index [SKIPINITIALSCAN] SCHEMA ADD field options",
  "complexity": "O(N) where N is the number of keys in the keyspace",
  "group": "search",
  "acl_categories": ["@search"],
  "since": "1.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"see-also","title":"See also"},{"id":"related-topics","title":"Related topics"}]}

,
  "codeExamples": []
}
```


Add a new attribute to the index. Adding an attribute to the index causes any future document updates to use the new attribute when indexing and reindexing existing documents.

[Examples](#examples)

## Required arguments

<details open>
<summary><code>index</code></summary> 

is index name to create. 
</details>

<details open>
<summary><code>SKIPINITIALSCAN</code></summary> 

if set, does not scan and index.
</details>

<details open>
<summary><code>SCHEMA ADD {attribute} {options} ...</code></summary>

after the SCHEMA keyword, declares which fields to add:

- `attribute` is attribute to add.
- `options` are attribute options. Refer to [`FT.CREATE`](https://redis.io/docs/latest/commands/ft.create) for more information.

<note><b>Note:</b>

Depending on how the index was created, you may be limited by the number of additional text
attributes which can be added to an existing index. If the current index contains fewer than 32
text attributes, then `SCHEMA ADD` will only be able to add attributes up to 32 total attributes (meaning that the
index will only ever be able to contain 32 total text attributes). If you wish for the index to
contain more than 32 attributes, create it with the `MAXTEXTFIELDS` option.
</note>
</details>

## Examples

<details open>
<summary><b>Alter an index</b></summary>


127.0.0.1:6379> FT.ALTER idx SCHEMA ADD id2 NUMERIC SORTABLE
OK

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis Cloud<br />Flexible & Annual | Redis Cloud<br />Free & Fixed | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Simple string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-strings): `OK` if executed correctly.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: no such index, invalid schema syntax.

**RESP3:**

One of the following:
* [Simple string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-strings): `OK` if executed correctly.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: no such index, invalid schema syntax.



## See also

[`FT.CREATE`](https://redis.io/docs/latest/commands/ft.create) 

## Related topics

- [RediSearch](https://redis.io/docs/latest/develop/ai/search-and-query)


