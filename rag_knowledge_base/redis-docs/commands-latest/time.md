# TIME

```json metadata
{
  "schema_version": 2,
  "title": "TIME",
  "description": "Returns the server time.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "TIME",
  "complexity": "O(1)",
  "group": "server",
  "command_flags": ["loading","stale","fast"],
  "acl_categories": ["@fast"],
  "since": "2.6.0",
  "arity": 1,
  "tableOfContents": {"sections":[{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

The `TIME` command returns the current server time as a two items lists: a Unix
timestamp and the amount of microseconds already elapsed in the current second.
Basically the interface is very similar to the one of the `gettimeofday` system
call.

## Examples


redis> TIME
1) "1784722081"
2) "827551"
redis> TIME
1) "1784722081"
2) "828843"


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Array reply](../../develop/reference/protocol-spec#arrays): specifically, a two-element array consisting of the Unix timestamp in seconds and the microseconds' count.

**RESP3:**

[Array reply](../../develop/reference/protocol-spec#arrays): specifically, a two-element array consisting of the Unix timestamp in seconds and the microseconds' count.



