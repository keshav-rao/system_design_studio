# BF.MADD

```json metadata
{
  "schema_version": 2,
  "title": "BF.MADD",
  "description": "Adds one or more items to a Bloom Filter. A filter will be created if it does not exist",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"key","type":"key"},{"multiple":true,"name":"item","type":"string"}],
  "syntax_fmt": "BF.MADD key item [item ...]",
  "complexity": "O(k * n), where k is the number of hash functions and n is the number of items",
  "group": "bf",
  "acl_categories": ["@bloom","@write","@slow"],
  "since": "1.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Adds one or more items to a Bloom filter.

This command is similar to [`BF.ADD`](https://redis.io/docs/latest/commands/bf.add), except that you can add more than one item.

This command is similar to [`BF.INSERT`](https://redis.io/docs/latest/commands/bf.insert), except that the error rate, capacity, and expansion cannot be specified.

## Required arguments

<details open><summary><code>key</code></summary>

is key name for a Bloom filter to add the items to.

If `key` does not exist - a new Bloom filter is created with default error rate, capacity, and expansion (see [`BF.RESERVE`](https://redis.io/docs/latest/commands/bf.reserve)).
</details>

<details open><summary><code>item...</code></summary>

One or more items to add.
</details>

## Examples


redis> BF.MADD bf item1 item2 item2
1) (integer) 1
2) (integer) 1
3) (integer) 0


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) where each element is either
  * an [integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers), where `1` means that the item has been added successfully, and `0` means there's a probability that the item was already added to the filter.
  * a [simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) when the item cannot be added because the filter is full.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: invalid arguments, key not found, wrong key type, or when the filter is full.

**RESP3:**

One of the following:
* [Array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) where each element is either
  * a [boolean reply](https://redis.io/docs/latest/develop/reference/protocol-spec#booleans), where `true` means that the item has been added successfully, and `false` means there's a probability that the item was already added to the filter.
  * a [simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) when the item cannot be added because the filter is full.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: invalid arguments, key not found, wrong key type, or when the filter is full.


