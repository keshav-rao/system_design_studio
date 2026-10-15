# FT.ALIASLIST

```json metadata
{
  "schema_version": 2,
  "title": "FT.ALIASLIST",
  "description": "Lists all aliases for the index",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"index","name":"index","summary":"Specifies the name of the index. The index must be created using `FT.CREATE`.","type":"string"}],
  "syntax_fmt": "FT.ALIASLIST index",
  "complexity": "O(N) where N is the number of aliases",
  "group": "search",
  "command_flags": ["readonly","module"],
  "acl_categories": ["@search"],
  "since": "8.10.0",
  "arity": 2,
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Lists all aliases for the given `index`.

## Required arguments

<details open><summary><code>index</code></summary>

is the name of the index for which to list aliases.

</details>

## Examples

<details open>
<summary><b>Add an alias to an index</b></summary>

Add an alias to an index.

```
> FT.ALIASADD alias idx:bicycle
OK
```

List the aliases for `idx:bicycle`

```
> FT.ALIASLIST idx:bicycle
1) "alias"
```

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis Cloud<br />Flexible & Annual | Redis Cloud<br />Free & Fixed | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Not supported</span> | <span title="Not supported">&#x274c; Not supported</span> | <span title="Not supported">&#x274c; Not supported</nobr></span> |  |

## Return information

**RESP2:**

One of the following:

* An [array](https://redis.io/docs/latest/develop/reference/protocol-spec#array) of [bulk strings](https://redis.io/docs/latest/develop/reference/protocol-spec#bulk-strings), the names of existing index aliases, or an empty array if no aliases exist.
* A [simple error](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) when the provided index doesn't exist.

**RESP3:**

One of the following:

* A [set](https://redis.io/docs/latest/develop/reference/protocol-spec#sets) of [bulk strings](https://redis.io/docs/latest/develop/reference/protocol-spec#bulk-strings), the names of index aliases, or an empty set if no aliases exist.
* A [simple error](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) when the provided index doesn't exist.



