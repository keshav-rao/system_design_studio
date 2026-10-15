# LATENCY GRAPH

```json metadata
{
  "schema_version": 2,
  "title": "LATENCY GRAPH",
  "description": "Returns a latency graph for an event.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"event","name":"event","type":"string"}],
  "syntax_fmt": "LATENCY GRAPH event",
  "complexity": "O(1)",
  "group": "server",
  "command_flags": ["admin","noscript","loading","stale"],
  "acl_categories": ["@admin","@slow","@dangerous"],
  "since": "2.8.13",
  "arity": 3,
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Produces an ASCII-art style graph for the specified event.

`LATENCY GRAPH` lets you intuitively understand the latency trend of an `event` via state-of-the-art visualization. It can be used for quickly grasping the situation before resorting to means such parsing the raw data from [`LATENCY HISTORY`](https://redis.io/docs/latest/commands/latency-history) or external tooling.

Valid values for `event` are:
* `active-defrag-cycle`
* `aof-fsync-always`
* `aof-stat`
* `aof-rewrite-diff-write`
* `aof-rename`
* `aof-write`
* `aof-write-active-child`
* `aof-write-alone`
* `aof-write-pending-fsync`
* `command`
* `expire-cycle`
* `eviction-cycle`
* `eviction-del`
* `fast-command`
* `fork`
* `rdb-unlink-temp-file`

## Required arguments

<details open><summary><code>event</code></summary>

The latency event to graph.

</details>

## Examples

```
127.0.0.1:6379> latency reset command
(integer) 0
127.0.0.1:6379> debug sleep .1
OK
127.0.0.1:6379> debug sleep .2
OK
127.0.0.1:6379> debug sleep .3
OK
127.0.0.1:6379> debug sleep .5
OK
127.0.0.1:6379> debug sleep .4
OK
127.0.0.1:6379> latency graph command
command - high 500 ms, low 101 ms (all time high 500 ms)
--------------------------------------------------------------------------------
   #_
  _||
 _|||
_||||

11186
542ss
sss
```

The vertical labels under each graph column represent the amount of seconds,
minutes, hours or days ago the event happened. For example "15s" means that the
first graphed event happened 15 seconds ago.

The graph is normalized in the min-max scale so that the zero (the underscore
in the lower row) is the minimum, and a # in the higher row is the maximum.

For more information refer to the [Latency Monitoring Framework page](https://redis.io/docs/latest/operate/oss_and_stack/management/optimization/latency-monitor).

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): Latency graph

**RESP3:**

[Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): Latency graph



