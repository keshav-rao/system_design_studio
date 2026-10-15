# CMS.INFO

```json metadata
{
  "schema_version": 2,
  "title": "CMS.INFO",
  "description": "Returns information about a sketch",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"key","type":"key"}],
  "syntax_fmt": "CMS.INFO key",
  "complexity": "O(1)",
  "group": "cms",
  "acl_categories": ["@cms","@read","@fast"],
  "since": "2.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Returns width, depth and total count of the sketch.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the sketch.

</details>

## Examples

```
redis> CMS.INFO test
 1) width
 2) (integer) 2000
 3) depth
 4) (integer) 7
 5) count
 6) (integer) 0
```

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

**RESP2:**

One of the following:

* [Array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) of [simple string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-strings) and [integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers) pairs containing sketch information.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: invalid arguments, missing key, or wrong key type.

**RESP3:**

One of the following:

* [Map reply](https://redis.io/docs/latest/develop/reference/protocol-spec#maps) of [simple string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-strings) and [integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers) pairs containing sketch information.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: invalid arguments, missing key, or wrong key type.


