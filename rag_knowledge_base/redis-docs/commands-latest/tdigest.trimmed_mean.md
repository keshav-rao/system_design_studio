# TDIGEST.TRIMMED_MEAN

```json metadata
{
  "schema_version": 2,
  "title": "TDIGEST.TRIMMED_MEAN",
  "description": "Returns an estimation of the mean value from the sketch, excluding observation values outside the low and high cutoff quantiles",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"key","type":"key"},{"name":"low_cut_quantile","type":"double"},{"name":"high_cut_quantile","type":"double"}],
  "syntax_fmt": "TDIGEST.TRIMMED_MEAN key low_cut_quantile high_cut_quantile",
  "complexity": "O(N) where N is the number of centroids",
  "group": "tdigest",
  "acl_categories": ["@tdigest","@read"],
  "since": "2.4.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Returns an estimation of the mean value from the sketch, excluding observation values outside the low and high cutoff quantiles.

## Required arguments

<details open><summary><code>key</code></summary> 

is the key name for an existing t-digest sketch.
</details>

<details open><summary><code>low_cut_quantile</code></summary> 
  
a floating-point value in the range [0..1]. It must be lower than `high_cut_quantile`.
  
When equal to 0, no low cut.
  
When greater than 0, exclude observation values lower than this quantile.
</details>

<details open><summary><code>high_cut_quantile</code></summary> 
  
a floating-point value in the range [0..1]. It must be higher than `low_cut_quantile`.
  
When less than 1, exclude observation values greater than or equal to this quantile.

When equal to 1, no high cut.
</details>

## Examples


redis> TDIGEST.CREATE t COMPRESSION 1000
OK
redis> TDIGEST.ADD t 1 2 3 4 5 6 7 8 9 10
OK
redis> TDIGEST.TRIMMED_MEAN t 0.1 0.6
"4"
redis> TDIGEST.TRIMMED_MEAN t 0.3 0.9
"6.5"
redis> TDIGEST.TRIMMED_MEAN t 0 1
"5.5"


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

**RESP2:**

One of the following:

* [Bulk string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#bulk-strings) as a floating-point estimation of the mean value.
* `nan` if the sketch is empty.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: the given key does not exist or is of an incorrect type, quantiles out of range [0..1], or incorrect number of arguments.

**RESP3:**

One of the following:

* [Double reply](https://redis.io/docs/latest/develop/reference/protocol-spec#doubles) as an estimation of the mean value.
* `nan` if the sketch is empty.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: the given key does not exist or is of an incorrect type, quantiles out of range [0..1], or incorrect number of arguments.


