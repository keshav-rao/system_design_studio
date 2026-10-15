# CMS.INITBYPROB

```json metadata
{
  "schema_version": 2,
  "title": "CMS.INITBYPROB",
  "description": "Initializes a Count-Min Sketch to accommodate requested tolerances.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"key","type":"key"},{"name":"error","type":"double"},{"name":"probability","type":"double"}],
  "syntax_fmt": "CMS.INITBYPROB key error probability",
  "complexity": "O(1)",
  "group": "cms",
  "acl_categories": ["@cms","@write","@fast"],
  "since": "2.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Initializes a Count-Min Sketch to accommodate requested tolerances.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the sketch.

</details>

<details open><summary><code>error</code></summary>

Estimate size of error. The error is a percent of total counted items. This effects the width of the sketch.

</details>

<details open><summary><code>probability</code></summary>

The desired probability for inflated count. This should be a decimal value between 0 and 1. This effects the depth of the sketch. For example, for a desired false positive rate of 0.1% (1 in 1000), error_rate should be set to 0.001. The closer this number is to zero, the greater the memory consumption per item and the more CPU usage per operation.

</details>

## Examples

```
redis> CMS.INITBYPROB test 0.001 0.01
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


