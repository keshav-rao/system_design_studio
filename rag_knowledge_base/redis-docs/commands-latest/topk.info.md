# TOPK.INFO

```json metadata
{
  "schema_version": 2,
  "title": "TOPK.INFO",
  "description": "Returns information about a sketch",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"key","type":"key"}],
  "syntax_fmt": "TOPK.INFO key",
  "complexity": "O(1)",
  "group": "topk",
  "acl_categories": ["@topk","@read","@fast"],
  "since": "2.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Returns number of required items (k), width, depth, and decay values of a given sketch.

## Required arguments

<details open><summary><code>key</code></summary>

the name of the sketch.

</details>

## Examples

```
TOPK.INFO topk
1) k
2) (integer) 50
3) width
4) (integer) 2000
5) depth
6) (integer) 7
7) decay
8) "0.92500000000000004"
```

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

**RESP2:**

One of the following:

* [Array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) of [simple string](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-strings) and [integer](https://redis.io/docs/latest/develop/reference/protocol-spec#integers) pairs. For decay, a [simple string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-strings) is used to represent the floating point value.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: incorrect number of arguments, non-existant key, or key of the incorrect type.

**RESP3:**

One of the following:

* [A map](https://redis.io/docs/latest/develop/reference/protocol-spec#maps) of [simple string](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-strings) and [integer](https://redis.io/docs/latest/develop/reference/protocol-spec#integers) pairs. For decay, a [double reply](https://redis.io/docs/latest/develop/reference/protocol-spec#doubles) is used to represent the floating point value.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: incorrect number of arguments, non-existant key, or key of the incorrect type.


