# LATENCY HISTORY

```json metadata
{
  "schema_version": 2,
  "title": "LATENCY HISTORY",
  "description": "Returns timestamp-latency samples for an event.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"event","name":"event","type":"string"}],
  "syntax_fmt": "LATENCY HISTORY event",
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

The `LATENCY HISTORY` command returns the raw data of the `event`'s latency spikes time series.

This is useful to an application that wants to fetch raw data in order to perform monitoring, display graphs, and so forth.

The command will return up to 160 timestamp-latency pairs for the `event`.

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

The latency event to return the history for.

</details>

## Examples

```
127.0.0.1:6379> latency history command
1) 1) (integer) 1405067822
   2) (integer) 251
2) 1) (integer) 1405067941
   2) (integer) 1001
```

For more information refer to the [Latency Monitoring Framework page](https://redis.io/docs/latest/operate/oss_and_stack/management/optimization/latency-monitor).

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Array reply](../../develop/reference/protocol-spec#arrays): an array where each element is a two elements array representing the timestamp and the latency of the event.

**RESP3:**

[Array reply](../../develop/reference/protocol-spec#arrays): an array where each element is a two elements array representing the timestamp and the latency of the event.



