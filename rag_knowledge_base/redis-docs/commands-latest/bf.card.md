# BF.CARD

```json metadata
{
  "schema_version": 2,
  "title": "BF.CARD",
  "description": "Returns the cardinality of a Bloom filter",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"key","type":"key"}],
  "syntax_fmt": "BF.CARD key",
  "complexity": "O(1)",
  "group": "bf",
  "acl_categories": ["@bloom","@read","@fast"],
  "since": "2.4.4",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Returns the cardinality of a Bloom filter - number of items that were added to a Bloom filter and detected as unique (items that caused at least one bit to be set in at least one sub-filter)

(since RedisBloom 2.4.4)

## Required arguments

<details open><summary><code>key</code></summary>

is key name for a Bloom filter.

</details>

## Examples


redis> BF.ADD bf1 item_foo
(integer) 1
redis> BF.CARD bf1
(integer) 1
redis> BF.CARD bf_new
(integer) 0


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported"><nobr>&#x2705; Flexible & Annual</nobr></span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers): the number of items detected as unique that were added to the Bloom filter (items that caused at least one bit to be set in at least one sub-filter), or `0` when the given `key` does not exist.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: invalid arguments, wrong key type, or when the filter is full.

Note: when `key` exists, `BF.CARD` returns the same value as `BF.INFO key ITEMS`.

**RESP3:**

One of the following:
* [Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers): the number of items detected as unique that were added to the Bloom filter (items that caused at least one bit to be set in at least one sub-filter), or `0` when the given `key` does not exist.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: invalid arguments, wrong key type, or when the filter is full.

Note: when `key` exists, `BF.CARD` returns the same value as `BF.INFO key ITEMS`.


