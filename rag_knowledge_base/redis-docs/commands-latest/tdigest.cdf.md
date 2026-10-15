# TDIGEST.CDF

```json metadata
{
  "schema_version": 2,
  "title": "TDIGEST.CDF",
  "description": "Returns, for each input value, an estimation of the floating-point fraction of (observations smaller than the given value + half the observations equal to the given value)",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"key","type":"key"},{"multiple":true,"name":"value","type":"double"}],
  "syntax_fmt": "TDIGEST.CDF key value [value ...]",
  "complexity": "O(1)",
  "group": "tdigest",
  "acl_categories": ["@tdigest","@read"],
  "since": "2.4.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Returns, for each input value, an estimation of the floating-point fraction of (_observations smaller than the given value_ + _half the observations equal to the given value_).
Multiple fractions can be retrieved in a single call.

## Required arguments

<details open><summary><code>key</code></summary>

is the key name for an existing t-digest sketch.
</details>

<details open><summary><code>value</code></summary>

are the values for which the CDF (Cumulative Distribution Function) should be retrieved.
</details>

## Examples


redis> TDIGEST.CREATE t COMPRESSION 1000
OK
redis> TDIGEST.ADD t 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5
OK
redis> TDIGEST.CDF t 0 1 2 3 4 5 6
1) "0"
2) "0.033333333333333333"
3) "0.13333333333333333"
4) "0.29999999999999999"
5) "0.53333333333333333"
6) "0.83333333333333337"
7) "1"


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

**RESP2:**

One of the following:

* [Array](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) of [bulk string replies](https://redis.io/docs/latest/develop/reference/protocol-spec#bulk-strings) as floating-points, populated with fraction_1, fraction_2, ..., fraction_N.
All values are `nan` if the given sketch is empty.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: the given key does not exist or is of an incorrect type, value parsing errors, or an incorrect number of arguments.

**RESP3:**

One of the following:

* [Array](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) of [doubles](https://redis.io/docs/latest/develop/reference/protocol-spec#bulk-strings) populated with fraction_1, fraction_2, ..., fraction_N.
All values are `nan` if the given sketch is empty.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: the given key does not exist or is of an incorrect type, value parsing errors, or an incorrect number of arguments.



