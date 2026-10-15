# BF.ADD

```json metadata
{
  "schema_version": 2,
  "title": "BF.ADD",
  "description": "Adds an item to a Bloom Filter",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"key","type":"key"},{"name":"item","type":"string"}],
  "syntax_fmt": "BF.ADD key item",
  "complexity": "O(k), where k is the number of hash functions used by the last sub-filter",
  "group": "bf",
  "acl_categories": ["@bloom","@write","@slow"],
  "since": "1.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Adds an item to a Bloom filter.

This command is similar to [`BF.MADD`](https://redis.io/docs/latest/commands/bf.madd), except that only one item can be added.

## Required arguments

<details open><summary><code>key</code></summary>

is key name for a Bloom filter to add the item to.

If `key` does not exist - a new Bloom filter is created with default error rate, capacity, and expansion (see [`BF.RESERVE`](https://redis.io/docs/latest/commands/bf.reserve)).
</details>

<details open><summary><code>item</code></summary>

is an item to add.
</details>

## Examples


redis> BF.ADD bf item1
(integer) 1
redis> BF.ADD bf item1
(integer) 0


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported"><nobr>&#x2705; Flexible & Annual</nobr></span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers): `1` for successfully adding an item, or `0` if there's a probability that the item was already added to the filter.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: invalid arguments, wrong key type, or when the filter is full.

**RESP3:**

One of the following:
* [Boolean reply](https://redis.io/docs/latest/develop/reference/protocol-spec#booleans): `true` for successfully adding an item, or `false` if there's a probability that the item was already added to the filter.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: invalid arguments, wrong key type, or when the filter is full.


