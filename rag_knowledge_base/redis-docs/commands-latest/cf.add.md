# CF.ADD

```json metadata
{
  "schema_version": 2,
  "title": "CF.ADD",
  "description": "Adds an item to a Cuckoo Filter",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"key","type":"key"},{"name":"item","type":"string"}],
  "syntax_fmt": "CF.ADD key item",
  "complexity": "O(k + i), where k is the number of sub-filters and i is maxIterations",
  "group": "cf",
  "acl_categories": ["@cuckoo","@write","@slow"],
  "since": "1.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"complexity","title":"Complexity"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Adds an item to the cuckoo filter.

Cuckoo filters can contain the same item multiple times, and consider each addition as separate.
Use [`CF.ADDNX`](https://redis.io/docs/latest/commands/cf.addnx) to add an item only if it does not exist.

## Required arguments

<details open><summary><code>key</code></summary>

is key name for a cuckoo filter to add the item to.

If `key` does not exist - a new cuckoo filter is created.
</details>

<details open><summary><code>item</code></summary>

is an item to add.
</details>

## Complexity

O(n + i), where n is the number of `sub-filters` and i is `maxIterations`.
Adding items requires up to 2 memory accesses per `sub-filter`.
But as the filter fills up, both locations for an item might be full.
The filter attempts to `Cuckoo` swap items up to `maxIterations` times.

## Examples


redis> CF.ADD cf item1
(integer) 1
redis> CF.ADD cf item1
(integer) 1


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported"><nobr>&#x2705; Flexible & Annual</nobr></span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers): `1` for successfully adding an item to the filter.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: invalid arguments, wrong key type, or when the filter is full.

**RESP3:**

One of the following:
* [Boolean reply](https://redis.io/docs/latest/develop/reference/protocol-spec#booleans): `true` for successfully adding an item to the filter.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: invalid arguments, wrong key type, or when the filter is full.



