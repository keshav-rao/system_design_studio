# TDIGEST.QUANTILE

```json metadata
{
  "schema_version": 2,
  "title": "TDIGEST.QUANTILE",
  "description": "Returns, for each input fraction, a floating-point estimation of the value that is smaller than the given fraction of observations",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"key","type":"key"},{"multiple":true,"name":"quantile","type":"double"}],
  "syntax_fmt": "TDIGEST.QUANTILE key quantile [quantile ...]",
  "complexity": "O(1)",
  "group": "tdigest",
  "acl_categories": ["@tdigest","@read"],
  "since": "2.4.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Returns, for each input fraction, a floating-point estimation of the value that is smaller than the given fraction of observations.
Multiple quantiles can be retrieved in a single call.

## Required arguments

<details open><summary><code>key</code></summary> 

is the key name for an existing t-digest sketch.
</details>

<details open><summary><code>quantile</code></summary> 

is the input fraction between 0 and 1 inclusively.
</details>

## Examples


redis> TDIGEST.CREATE t COMPRESSION 1000
OK
redis> TDIGEST.ADD t 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5
OK
redis> TDIGEST.QUANTILE t 0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1
 1) "1"
 2) "2"
 3) "3"
 4) "3"
 5) "4"
 6) "4"
 7) "4"
 8) "5"
 9) "5"
10) "5"
11) "5"


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

**RESP2:**

One of the following:

* [Array](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) of [bulk string replies](https://redis.io/docs/latest/develop/reference/protocol-spec#bulk-strings) as floating-point estimates, populated with value_1, value_2, ..., value_N.
    * an accurate result when `quantile` is `0`, the value of the smallest observation.
    * an accurate result when `quantile` is `1`, the value of the largest observation.
    * `nan` for all quantiles when the given sketch is empty.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: the given key does not exist or is of an incorrect type, quantile parsing errors, or incorrect number of arguments.

**RESP3:**

One of the following:

* [Array](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) of [double replies](https://redis.io/docs/latest/develop/reference/protocol-spec#doubles) as estimates, populated with value_1, value_2, ..., value_N.
    * an accurate result when `quantile` is `0`, the value of the smallest observation.
    * an accurate result when `quantile` is `1`, the value of the largest observation.
    * `nan` for all quantiles when the given sketch is empty.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: the given key does not exist or is of an incorrect type, quantile parsing errors, or incorrect number of arguments.


