# FT.DROPINDEX

```json metadata
{
  "schema_version": 2,
  "title": "FT.DROPINDEX",
  "description": "Deletes the index",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"index","type":"string"},{"arguments":[{"name":"delete docs","token":"DD","type":"pure-token"}],"name":"delete docs","optional":true,"type":"oneof"}],
  "syntax_fmt": "FT.DROPINDEX index [DD]",
  "complexity": "O(1) or O(N) if documents are deleted, where N is the number of keys in the keyspace",
  "group": "search",
  "acl_categories": ["@dangerous","@search","@slow","@write"],
  "since": "2.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"see-also","title":"See also"},{"id":"related-topics","title":"Related topics"}]}

,
  "codeExamples": []
}
```


Delete an index

[Examples](#examples)

## Required arguments

<details open>
<summary><code>index</code></summary>

is full-text index name. You must first create the index using [`FT.CREATE`](https://redis.io/docs/latest/commands/ft.create).
</details>

## Optional arguments

<details open>
<summary><code>DD</code></summary>

drop index operation that, if set, deletes the actual document keys. `FT.DROPINDEX index DD` is an asynchronous operation.

By default, FT.DROPINDEX does not delete the documents associated with the index. Adding the `DD` option deletes the documents as well. 
If an index creation is still running ([`FT.CREATE`](https://redis.io/docs/latest/commands/ft.create) is running asynchronously), only the document hashes that have already been indexed are deleted. 
The document hashes left to be indexed remain in the database.
To check the completion of the indexing, use [`FT.INFO`](https://redis.io/docs/latest/commands/ft.info).

</details>

## Examples

<details open>
<summary><b>Delete an index</b></summary>


127.0.0.1:6379> FT.DROPINDEX idx DD
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
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: no such index.

**RESP3:**

One of the following:
* [Simple string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-strings): `OK` if executed correctly.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: no such index.



## See also

[`FT.CREATE`](https://redis.io/docs/latest/commands/ft.create) | [`FT.INFO`](https://redis.io/docs/latest/commands/ft.info)

## Related topics

[RediSearch](https://redis.io/docs/latest/develop/ai/search-and-query)

