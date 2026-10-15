# TDIGEST.ADD

```json metadata
{
  "schema_version": 2,
  "title": "TDIGEST.ADD",
  "description": "Adds one or more observations to a t-digest sketch",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"key","type":"key"},{"arguments":[{"name":"value","type":"double"}],"multiple":true,"name":"values","type":"block"}],
  "syntax_fmt": "TDIGEST.ADD key value [value ...]",
  "complexity": "O(N), where N is the number of samples to add",
  "group": "tdigest",
  "acl_categories": ["@tdigest","@write","@slow"],
  "since": "2.4.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Adds one or more observations to a t-digest sketch.

## Required arguments

<details open><summary><code>key</code></summary> 

is the key name for an existing t-digest sketch.
</details>

<details open><summary><code>value</code></summary> 

is the floating-point value of an observation.
</details>

## Examples


redis> TDIGEST.ADD t 1 2 3
OK



redis> TDIGEST.ADD t string
(error) ERR T-Digest: error parsing val parameter


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported"><nobr>&#x2705; Flexible & Annual</nobr></span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

**RESP2:**

One of the following:

* [Simple string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-strings) `OK` if executed correctly.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: the given key does not exist or the value parameter is of the incorrect type.

**RESP3:**

One of the following:

* [Simple string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-strings) `OK` if executed correctly.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: the given key does not exist or the value parameter is of the incorrect type.



