# CMS.INITBYDIM

```json metadata
{
  "schema_version": 2,
  "title": "CMS.INITBYDIM",
  "description": "Initializes a Count-Min Sketch to dimensions specified by user",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"key","type":"key"},{"name":"width","type":"integer"},{"name":"depth","type":"integer"}],
  "syntax_fmt": "CMS.INITBYDIM key width depth",
  "complexity": "O(1)",
  "group": "cms",
  "acl_categories": ["@cms","@write","@fast"],
  "since": "2.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Initializes a Count-Min Sketch to dimensions specified by user.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the sketch.

</details>

<details open><summary><code>width</code></summary>

Number of counters in each array. Reduces the error size.

</details>

<details open><summary><code>depth</code></summary>

Number of counter-arrays. Reduces the probability for an error of a certain size (percentage of total count).

</details>

## Examples

```
redis> CMS.INITBYDIM test 2000 5
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
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) if the given key already exists.

**RESP3:**

One of the following:

* [Simple string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-strings) `OK` if executed correctly.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) if the given key already exists.


