# TOPK.QUERY

```json metadata
{
  "schema_version": 2,
  "title": "TOPK.QUERY",
  "description": "Checks whether one or more items are in a sketch",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"key","type":"key"},{"multiple":true,"name":"item","type":"string"}],
  "syntax_fmt": "TOPK.QUERY key item [item ...]",
  "complexity": "O(n) where n is the number of items",
  "group": "topk",
  "acl_categories": ["@topk","@read","@slow"],
  "since": "2.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Checks whether one or more items are one of the Top-K items.

## Required arguments

<details open><summary><code>key</code></summary>

the name of the sketch.

</details>

<details open><summary><code>item [item ...]</code></summary>

the items to be queried.

</details>

## Examples

```
redis> TOPK.QUERY topk 42 nonexist
1) (integer) 1
2) (integer) 0
```

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

**RESP2:**

One of the following:

* [Array](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) of [integer replies](https://redis.io/docs/latest/develop/reference/protocol-spec#integers): `1` if an item is in the Top-K or `0` otherwise.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: non-existant key or key of the incorrect type.

**RESP3:**

* [Array](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) of [boolean replies](https://redis.io/docs/latest/develop/reference/protocol-spec#booleans): `true` if an item is in the Top-K or `false` otherwise.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: non-existant key or key of the incorrect type.


