# TDIGEST.INFO

```json metadata
{
  "schema_version": 2,
  "title": "TDIGEST.INFO",
  "description": "Returns information and statistics about a t-digest sketch",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"key","type":"key"}],
  "syntax_fmt": "TDIGEST.INFO key",
  "complexity": "O(1)",
  "group": "tdigest",
  "acl_categories": ["@tdigest","@read"],
  "since": "2.4.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Returns information and statistics about a t-digest sketch.

## Required arguments

<details open><summary><code>key</code></summary> 

is the key name for an existing t-digest sketch.
</details>

## Examples


redis> TDIGEST.CREATE t
OK
redis> TDIGEST.ADD t 1 2 3 4 5
OK
redis> TDIGEST.INFO t
 1) Compression
 2) (integer) 100
 3) Capacity
 4) (integer) 610
 5) Merged nodes
 6) (integer) 0
 7) Unmerged nodes
 8) (integer) 5
 9) Merged weight
10) (integer) 0
11) Unmerged weight
12) (integer) 5
13) Observations
14) (integer) 5
15) Total compressions
16) (integer) 0
17) Memory usage
18) (integer) 9768


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

**RESP2:**

One of the following:

* [Array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) with information about the given sketch as name-value pairs:

    | Name<br>[Simple string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-strings) | Description
    | ---------------------------- | -
    | `Compression`        | [Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers)<br> The compression (controllable trade-off between accuracy and memory consumption) of the sketch 
    | `Capacity`           | [Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers)<br> Size of the buffer used for storing the centroids and for the incoming unmerged observations
    | `Merged nodes`       | [Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers)<br> Number of merged observations
    | `Unmerged nodes`     | [Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers)<br> Number of buffered nodes (uncompressed observations)
    | `Merged weight`      | [Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers)<br> Weight of values of the merged nodes
    | `Unmerged weight`    | [Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers)<br> Weight of values of the unmerged nodes (uncompressed observations)
    | `Observations`       | [Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers)<br> Number of observations added to the sketch
    | `Total compressions` | [Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers)<br> Number of times this sketch compressed data together
    | `Memory usage`       | [Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers)<br> Number of bytes allocated for the sketch
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: the given key does not exist or is of an incorrect type or an incorrect number of arguments.

**RESP3:**

One of the following:

* [Map reply](https://redis.io/docs/latest/develop/reference/protocol-spec#maps) with information about the given sketch as name-value pairs:

    | Name<br>[Simple string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-strings) | Description
    | ---------------------------- | -
    | `Compression`        | [Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers)<br> The compression (controllable trade-off between accuracy and memory consumption) of the sketch 
    | `Capacity`           | [Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers)<br> Size of the buffer used for storing the centroids and for the incoming unmerged observations
    | `Merged nodes`       | [Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers)<br> Number of merged observations
    | `Unmerged nodes`     | [Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers)<br> Number of buffered nodes (uncompressed observations)
    | `Merged weight`      | [Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers)<br> Weight of values of the merged nodes
    | `Unmerged weight`    | [Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers)<br> Weight of values of the unmerged nodes (uncompressed observations)
    | `Observations`       | [Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers)<br> Number of observations added to the sketch
    | `Total compressions` | [Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers)<br> Number of times this sketch compressed data together
    | `Memory usage`       | [Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers)<br> Number of bytes allocated for the sketch
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: the given key does not exist or is of an incorrect type or an incorrect number of arguments.



