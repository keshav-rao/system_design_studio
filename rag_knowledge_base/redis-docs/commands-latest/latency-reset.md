# LATENCY RESET

```json metadata
{
  "schema_version": 2,
  "title": "LATENCY RESET",
  "description": "Resets the latency data for one or more events.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"event","multiple":true,"name":"event","optional":true,"type":"string"}],
  "syntax_fmt": "LATENCY RESET [event [event ...]]",
  "complexity": "O(1)",
  "group": "server",
  "command_flags": ["admin","noscript","loading","stale"],
  "acl_categories": ["@admin","@slow","@dangerous"],
  "since": "2.8.13",
  "arity": -2,
  "tableOfContents": {"sections":[{"id":"optional-arguments","title":"Optional arguments"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

The `LATENCY RESET` command resets the latency spikes time series of all, or only some, events.

When the command is called without arguments, it resets all the
events, discarding the currently logged latency spike events, and resetting
the maximum event time register.

It is possible to reset only specific events by providing the `event` names
as arguments.

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

For more information refer to the [Latency Monitoring Framework page](https://redis.io/docs/latest/operate/oss_and_stack/management/optimization/latency-monitor).

## Optional arguments

<details open><summary><code>event [event ...]</code></summary>

One or more latency events to reset. If omitted, all events are reset.

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Integer reply](../../develop/reference/protocol-spec#integers): the number of event time series that were reset.

**RESP3:**

[Integer reply](../../develop/reference/protocol-spec#integers): the number of event time series that were reset.



