# FT.ALIASADD

```json metadata
{
  "schema_version": 2,
  "title": "FT.ALIASADD",
  "description": "Adds an alias to the index",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"alias","type":"string"},{"name":"index","type":"string"}],
  "syntax_fmt": "FT.ALIASADD alias index",
  "complexity": "O(1)",
  "group": "search",
  "acl_categories": ["@search"],
  "since": "1.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"see-also","title":"See also"}]}

,
  "codeExamples": []
}
```


Add an alias to an index

[Examples](#examples)

## Required arguments

<details open>
<summary><code>alias index</code></summary>

is alias to be added to an index.
</details>

Indexes can have more than one alias, but an alias cannot refer to another
alias.

FT.ALIASADD allows administrators to transparently redirect application queries to alternative indexes.

## Examples

<details open>
<summary><b>Add an alias to an index</b></summary>

Add an alias to an index.


127.0.0.1:6379> FT.ALIASADD alias idx
OK


Attempting to add the same alias returns a message that the alias already exists.


127.0.0.1:6379> FT.ALIASADD alias idx
(error) Alias already exists

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis Cloud<br />Flexible & Annual | Redis Cloud<br />Free & Fixed | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Simple string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-strings): `OK` if executed correctly.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: alias already exists, index does not exist.

**RESP3:**

One of the following:
* [Simple string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-strings): `OK` if executed correctly.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: alias already exists, index does not exist.



## See also

[`FT.ALIASDEL`](https://redis.io/docs/latest/commands/ft.aliasdel) | [`FT.ALIASUPDATE`](https://redis.io/docs/latest/commands/ft.aliasupdate)

