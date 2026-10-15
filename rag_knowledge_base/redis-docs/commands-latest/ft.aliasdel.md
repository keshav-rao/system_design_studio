# FT.ALIASDEL

```json metadata
{
  "schema_version": 2,
  "title": "FT.ALIASDEL",
  "description": "Deletes an alias from the index",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"alias","type":"string"}],
  "syntax_fmt": "FT.ALIASDEL alias",
  "complexity": "O(1)",
  "group": "search",
  "acl_categories": ["@search"],
  "since": "1.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"see-also","title":"See also"}]}

,
  "codeExamples": []
}
```


Remove an alias from an index

[Examples](#examples)

## Required arguments

<details open>
<summary><code>alias</code></summary>

is index alias to be removed.
</details>

## Examples

<details open>
<summary><b>Remove an alias from an index</b></summary>

Remove an alias from an index.


127.0.0.1:6379> FT.ALIASDEL alias
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
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: alias does not exist.

**RESP3:**

One of the following:
* [Simple string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-strings): `OK` if executed correctly.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: alias does not exist.



## See also

[`FT.ALIASADD`](https://redis.io/docs/latest/commands/ft.aliasadd) | [`FT.ALIASUPDATE`](https://redis.io/docs/latest/commands/ft.aliasupdate)

