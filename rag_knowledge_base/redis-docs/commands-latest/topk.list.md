# TOPK.LIST

```json metadata
{
  "schema_version": 2,
  "title": "TOPK.LIST",
  "description": "Return the full list of items in the Top-K sketch",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"key","type":"key"},{"name":"withcount","optional":true,"token":"WITHCOUNT","type":"pure-token"}],
  "syntax_fmt": "TOPK.LIST key [WITHCOUNT]",
  "complexity": "O(k) where k is the value of top-k",
  "group": "topk",
  "acl_categories": ["@topk","@read","@slow"],
  "since": "2.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Return the full list of items in Top-K sketch.

## Required arguments

<details open><summary><code>key</code></summary>

the name of the sketch.

</details>

## Optional arguments

<details open><summary><code>WITHCOUNT</code></summary>

the count of each element is also returned.

</details>

## Examples

```
TOPK.LIST topk
1) foo
2) 42
3) bar
```

```
TOPK.LIST topk WITHCOUNT
1) foo
2) (integer) 12
3) 42
4) (integer) 7
5) bar
6) (integer) 2
```

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

k (or less) items in the given Top-k sketch. The list is sorted by decreased count estimation.

**RESP2:**

One of the following:

* [Array](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) of [bulk string replies](https://redis.io/docs/latest/develop/reference/protocol-spec#bulk-strings) representing the names of items in the given sketch. If `WITHCOUNT` is requested, an [array](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) of [bulk string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#bulk-strings) and 
[integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers) pairs, representing the names of the items in the sketch together with their counts.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: invalid arguments, non-existant key, or key of the incorrect type.

**RESP3:**

One of the following:

* [Array](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) of [bulk string replies](https://redis.io/docs/latest/develop/reference/protocol-spec#bulk-strings) representing the names of items in the given sketch. If `WITHCOUNT` is requested, an [array](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) of [bulk string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#bulk-strings) and 
[integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers) pairs, representing the names of the items in the sketch together with their counts.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: invalid arguments, non-existant key, or key of the incorrect type.


