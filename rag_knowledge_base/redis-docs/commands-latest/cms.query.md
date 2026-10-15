# CMS.QUERY

```json metadata
{
  "schema_version": 2,
  "title": "CMS.QUERY",
  "description": "Returns the count for one or more items in a sketch",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"key","type":"key"},{"multiple":true,"name":"item","type":"string"}],
  "syntax_fmt": "CMS.QUERY key item [item ...]",
  "complexity": "O(n) where n is the number of items",
  "group": "cms",
  "acl_categories": ["@cms","@read"],
  "since": "2.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Returns the count for one or more items in a sketch.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the sketch.

</details>

<details open><summary><code>item [item ...]</code></summary>

One or more items for which to return the count.

</details>

## Examples

```
redis> CMS.QUERY test foo bar
1) (integer) 10
2) (integer) 42
```

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

**RESP2:**

One of the following:

* [Array](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) of [integer replies](https://redis.io/docs/latest/develop/reference/protocol-spec#integers)  representing the min-counts of each of the provided items in the sketch.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: invalid arguments, missing key, or wrong key type.

**RESP3:**

One of the following:

* [Array](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) of [integer replies](https://redis.io/docs/latest/develop/reference/protocol-spec#integers) representing the min-counts of each of the provided items in the sketch.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: invalid arguments, missing key, or wrong key type.


