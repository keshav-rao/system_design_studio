# BF.INFO

```json metadata
{
  "schema_version": 2,
  "title": "BF.INFO",
  "description": "Returns information about a Bloom Filter",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"key","type":"key"},{"arguments":[{"name":"capacity","token":"CAPACITY","type":"pure-token"},{"name":"size","token":"SIZE","type":"pure-token"},{"name":"filters","token":"FILTERS","type":"pure-token"},{"name":"items","token":"ITEMS","type":"pure-token"},{"name":"expansion","token":"EXPANSION","type":"pure-token"}],"name":"single_value","optional":true,"type":"oneof"}],
  "syntax_fmt": "BF.INFO key [CAPACITY | SIZE | FILTERS | ITEMS | EXPANSION]",
  "complexity": "O(1)",
  "group": "bf",
  "acl_categories": ["@bloom","@read","@fast"],
  "since": "1.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Returns information about a Bloom filter.

## Required arguments

<details open><summary><code>key</code></summary>

is key name for a Bloom filter.
</details>

## Optional arguments

<details open><summary><code>CAPACITY</code></summary>

Return the number of unique items that can be stored in this Bloom filter before scaling would be required (including already added items).
</details>

<details open><summary><code>SIZE</code></summary>

Return the memory size: number of bytes allocated for this Bloom filter.
</details>

<details open><summary><code>FILTERS</code></summary>

Return the number of sub-filters.
</details>

<details open><summary><code>ITEMS</code></summary>

Return the number of items that were added to this Bloom filter and detected as unique (items that caused at least one bit to be set in at least one sub-filter).
</details>

<details open><summary><code>EXPANSION</code></summary>

Return the expansion rate.
</details>

## Examples


redis> BF.ADD bf1 observation1
(integer) 1
redis> BF.INFO bf1
 1) Capacity
 2) (integer) 100
 3) Size
 4) (integer) 240
 5) Number of filters
 6) (integer) 1
 7) Number of items inserted
 8) (integer) 1
 9) Expansion rate
10) (integer) 2
redis> BF.INFO bf1 CAPACITY
1) (integer) 100


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* A singleton [array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) with an [integer](https://redis.io/docs/latest/develop/reference/protocol-spec#integers) representing the value of the requested property.
* An [array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) with [simple string](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-strings) and [integer](https://redis.io/docs/latest/develop/reference/protocol-spec#integers) pairs.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: invalid arguments, wrong key type, or when the key does not exist.

**RESP3:**

One of the following:
* [Map reply](https://redis.io/docs/latest/develop/reference/protocol-spec#maps) with [simple string](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-strings) and [integer](https://redis.io/docs/latest/develop/reference/protocol-spec#integers) pairs.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: invalid arguments, wrong key type, or when the key does not exist.


