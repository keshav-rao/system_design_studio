# TOPK.ADD

```json metadata
{
  "schema_version": 2,
  "title": "TOPK.ADD",
  "description": "Adds an item to a Top-k sketch. Multiple items can be added at the same time.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"key","type":"key"},{"multiple":true,"name":"items","type":"string"}],
  "syntax_fmt": "TOPK.ADD key items [items ...]",
  "complexity": "O(n * k) where n is the number of items and k is the depth",
  "group": "topk",
  "acl_categories": ["@topk","@write","@slow"],
  "since": "2.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```


Adds an item to a Top-k sketch. 
Multiple items can be added at the same time.
If an item enters the Top-K sketch, the item that is expelled (if any) is returned.
This allows dynamic heavy-hitter detection of items being entered or expelled from Top-K sketch. 

## Required arguments

<details open><summary><code>key</code></summary>

the name of the sketch where items are added.

</details>

<details open><summary><code>item [item ...]</code></summary>

the items to be added.

</details>

## Examples

```
redis> TOPK.ADD topk foo bar 42
1) (nil)
2) baz
3) (nil)
```

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported"><nobr>&#x2705; Flexible & Annual</nobr></span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

**RESP2:**

One of the following:

* [Array](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) of [bulk string replies](https://redis.io/docs/latest/develop/reference/protocol-spec#bulk-strings) containing either dropped elements or [nil (null bulk string)](https://redis.io/docs/latest/develop/reference/protocol-spec#bulk-strings).
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: incorrect number of arguments or non-existant key.

**RESP3:**

One of the following:

* [Array](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) of [bulk string replies](https://redis.io/docs/latest/develop/reference/protocol-spec#bulk-strings) containing either dropped elements or [null](https://redis.io/docs/latest/develop/reference/protocol-spec#nulls).
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: incorrect number of arguments, non-existant key, or key of the incorrect type.


