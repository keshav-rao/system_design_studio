# TOPK.RESERVE

```json metadata
{
  "schema_version": 2,
  "title": "TOPK.RESERVE",
  "description": "Initializes a Top-K sketch with specified parameters",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"key","type":"key"},{"name":"topk","type":"integer"},{"arguments":[{"name":"width","type":"integer"},{"name":"depth","type":"integer"},{"name":"decay","type":"double"}],"name":"params","optional":true,"type":"block"}],
  "syntax_fmt": "TOPK.RESERVE key topk [width depth decay]",
  "complexity": "O(1)",
  "group": "topk",
  "acl_categories": ["@topk","@write","@fast"],
  "since": "2.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Initializes a Top-K sketch with specified parameters.

## Required arguments

<details open><summary><code>key</code></summary>

the name of the Top-k sketch.

</details>

<details open><summary><code>topk</code></summary>

the number of top (k) occurring items to keep.

</details>

## Optional arguments

<details open><summary><code>width</code></summary>

Number of counters kept in each array. (Default 8)

</details>

<details open><summary><code>depth</code></summary>

Number of arrays. (Default 7)

</details>

<details open><summary><code>decay</code></summary>

The probability of reducing a counter in an occupied bucket (decay ^ bucket[i].counter). As the counter gets higher, the likelihood of a reduction is lower. (Default 0.9)

</details>

## Examples

```
redis> TOPK.RESERVE topk 50 2000 7 0.925
OK
```

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

**RESP2:**

One of the following:

* [Simple string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-strings) `OK` if executed correctly.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: incorrect number of arguments, invalid decay value, or key already exists.

**RESP3:**

One of the following:

* [Simple string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-strings) `OK` if executed correctly.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: incorrect number of arguments, invalid decay value, or key already exists.


