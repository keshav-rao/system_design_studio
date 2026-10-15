# CMS.INCRBY

```json metadata
{
  "schema_version": 2,
  "title": "CMS.INCRBY",
  "description": "Increases the count of one or more items by increment",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"key","type":"key"},{"arguments":[{"name":"item","type":"string"},{"name":"increment","type":"integer"}],"multiple":true,"name":"items","type":"block"}],
  "syntax_fmt": "CMS.INCRBY key item increment [item increment ...]",
  "complexity": "O(n) where n is the number of items",
  "group": "cms",
  "acl_categories": ["@cms","@write"],
  "since": "2.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```


Increases the count of item by increment. Multiple items can be increased with one call. 

## Required arguments

<details open><summary><code>key</code></summary>

The name of the sketch.

</details>

<details open><summary><code>item increment [item increment ...]</code></summary>

One or more item-increment pairs. Each `item`'s counter is increased by its corresponding `increment`.

</details>

## Examples

```
redis> CMS.INCRBY test foo 10 bar 42
1) (integer) 10
2) (integer) 42
```

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported"><nobr>&#x2705; Flexible & Annual</nobr></span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

**RESP2:**

One of the following:

* [Array](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) of [integer replies](https://redis.io/docs/latest/develop/reference/protocol-spec#integers) representing updated min-counts of each of the provided items in the sketch.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: invalid arguments, missing key, overflow, or wrong key type.

**RESP3:**

One of the following:

* [Array](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) of [integer replies](https://redis.io/docs/latest/develop/reference/protocol-spec#integers) representing updated min-counts of each of the provided items in the sketch.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: invalid arguments, missing key, overflow, or wrong key type.


