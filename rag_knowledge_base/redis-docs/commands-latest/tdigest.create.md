# TDIGEST.CREATE

```json metadata
{
  "schema_version": 2,
  "title": "TDIGEST.CREATE",
  "description": "Allocates memory and initializes a new t-digest sketch",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"key","type":"key"},{"name":"compression","optional":true,"token":"COMPRESSION","type":"integer"}],
  "syntax_fmt": "TDIGEST.CREATE key [COMPRESSION compression]",
  "complexity": "O(1)",
  "group": "tdigest",
  "acl_categories": ["@tdigest","@write"],
  "since": "2.4.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Allocates memory and initializes a new t-digest sketch.

## Required arguments

<details open><summary><code>key</code></summary> 

is the key name for this new t-digest sketch.
</details>

## Optional arguments

<details open><summary><code>COMPRESSION compression</code></summary>

is a controllable tradeoff between accuracy and memory consumption. 100 is a common value for normal uses and also the default if not specified. 1000 is more accurate. For more information on scaling of accuracy versus the compression value see [_The t-digest: Efficient estimates of distributions_](https://www.sciencedirect.com/science/article/pii/S2665963820300403).
</details>

## Examples


redis> TDIGEST.CREATE t COMPRESSION 100
OK


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

**RESP2:**

One of the following:

* [Simple string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-strings) `OK` if executed correctly.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: incorrect key type or incorrect keyword.

**RESP3:**

One of the following:

* [Simple string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-strings) `OK` if executed correctly.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: incorrect key type or incorrect keyword.



