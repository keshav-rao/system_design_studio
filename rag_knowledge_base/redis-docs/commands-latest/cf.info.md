# CF.INFO

```json metadata
{
  "schema_version": 2,
  "title": "CF.INFO",
  "description": "Returns information about a Cuckoo Filter",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"key","type":"key"}],
  "syntax_fmt": "CF.INFO key",
  "complexity": "O(1)",
  "group": "cf",
  "acl_categories": ["@cuckoo","@read","@fast"],
  "since": "1.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Returns information about a cuckoo filter.

## Required arguments

<details open><summary><code>key</code></summary>

is key name for a cuckoo filter.
</details>

## Examples


redis> CF.ADD cf item1
(integer) 1
redis> CF.INFO cf
 1) Size
 2) (integer) 1080
 3) Number of buckets
 4) (integer) 512
 5) Number of filters
 6) (integer) 1
 7) Number of items inserted
 8) (integer) 1
 9) Number of items deleted
10) (integer) 0
11) Bucket size
12) (integer) 2
13) Expansion rate
14) (integer) 1
15) Max iterations
16) (integer) 20


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

One of the following:

**RESP2:**

* [Array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) with argument name ([Simple string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-strings)) and value ([Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers)) pairs.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) if invalid arguments are passed, `key` does not exist, or `key` is not of the correct type.

**RESP3:**

* [Map reply](https://redis.io/docs/latest/develop/reference/protocol-spec#maps) with argument name ([Simple string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-strings)) and value ([Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers)) pairs.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) if invalid arguments are passed, `key` does not exist, or `key` is not of the correct type.


