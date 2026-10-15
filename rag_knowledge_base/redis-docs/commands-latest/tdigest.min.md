# TDIGEST.MIN

```json metadata
{
  "schema_version": 2,
  "title": "TDIGEST.MIN",
  "description": "Returns the minimum observation value from a t-digest sketch",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"key","type":"key"}],
  "syntax_fmt": "TDIGEST.MIN key",
  "complexity": "O(1)",
  "group": "tdigest",
  "acl_categories": ["@tdigest","@read","@fast"],
  "since": "2.4.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Returns the minimum observation value from a t-digest sketch.

## Required arguments

<details open><summary><code>key</code></summary>

is the key name for an existing t-digest sketch.
</details>

## Examples


redis> TDIGEST.CREATE t
OK
redis> TDIGEST.MIN t
"nan"
redis> TDIGEST.ADD t 3 4 1 2 5
OK
redis> TDIGEST.MIN t
"1"


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

**RESP2:**

One of the following:

* [Bulk string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#bulk-strings) as floating-point representing the minimum observation value from the given sketch. The result is always accurate. `nan` is returned if the sketch is empty.
* [Simple string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-strings) in these cases: incorrect number of arguments or incorrect key type.

**RESP3:**

One of the following:

* [Double reply](https://redis.io/docs/latest/develop/reference/protocol-spec#doubles) representing the minimum observation value from the given sketch. The result is always accurate. `nan` is returned if the sketch is empty.
* [Simple string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-strings) in these cases: incorrect number of arguments or incorrect key type.


