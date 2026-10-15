# BF.EXISTS

```json metadata
{
  "schema_version": 2,
  "title": "BF.EXISTS",
  "description": "Checks whether an item exists in a Bloom Filter",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"key","type":"key"},{"name":"item","type":"string"}],
  "syntax_fmt": "BF.EXISTS key item",
  "complexity": "O(k), where k is the number of hash functions used by the last sub-filter",
  "group": "bf",
  "acl_categories": ["@bloom","@read","@slow"],
  "since": "1.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Determines whether a given item was added to a Bloom filter.

This command is similar to [`BF.MEXISTS`](https://redis.io/docs/latest/commands/bf.mexists), except that only one item can be checked.

## Required arguments

<details open><summary><code>key</code></summary>

is key name for a Bloom filter.

</details>

<details open><summary><code>item</code></summary>

is an item to check.
</details>

## Examples


redis> BF.ADD bf item1
(integer) 1
redis> BF.EXISTS bf item1
(integer) 1
redis> BF.EXISTS bf item2
(integer) 0


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers), where a value of `1` means the item was probably already added to the filter. A value of `0` means the item was definitely not added, `key` does not exist, or `key` contains a value of the wrong type.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) if invalid arguments are passed.

**RESP3:**

One of the following:
* [Boolean reply](https://redis.io/docs/latest/develop/reference/protocol-spec#booleans), where a value of `true` means the item was probably already added to the filter. A value of `false` means the item was definitely not added, `key` does not exist, or `key` contains a value of the wrong type.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) if invalid arguments are passed.


