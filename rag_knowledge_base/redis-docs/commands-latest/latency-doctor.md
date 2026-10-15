# LATENCY DOCTOR

```json metadata
{
  "schema_version": 2,
  "title": "LATENCY DOCTOR",
  "description": "Returns a human-readable latency analysis report.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "LATENCY DOCTOR",
  "complexity": "O(1)",
  "group": "server",
  "command_flags": ["admin","noscript","loading","stale"],
  "acl_categories": ["@admin","@slow","@dangerous"],
  "since": "2.8.13",
  "arity": 2,
  "tableOfContents": {"sections":[{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

The `LATENCY DOCTOR` command reports about different latency-related issues and advises about possible remedies.

This command is the most powerful analysis tool in the latency monitoring
framework, and is able to provide additional statistical data like the average
period between latency spikes, the median deviation, and a human-readable
analysis of the event. For certain events, like `fork`, additional information
is provided, like the rate at which the system forks processes.

This is the output you should post in the Redis mailing list if you are
looking for help about Latency related issues.

## Examples

```
127.0.0.1:6379> latency doctor

Dave, I have observed latency spikes in this Redis instance.
You don't mind talking about it, do you Dave?

1. command: 5 latency spikes (average 300ms, mean deviation 120ms,
    period 73.40 sec). Worst all time event 500ms.

I have a few advices for you:

- Your current Slow Log configuration only logs events that are
    slower than your configured latency monitor threshold. Please
    use 'CONFIG SET slowlog-log-slower-than 1000'.
- Check your Slow Log to understand what are the commands you are
    running which are too slow to execute. Please check
    http://redis.io/commands/slowlog for more information.
- Deleting, expiring or evicting (because of maxmemory policy)
    large objects is a blocking operation. If you have very large
    objects that are often deleted, expired, or evicted, try to
    fragment those objects into multiple smaller objects.
```

**Note:** the doctor has erratic psychological behaviors, so we recommend interacting with it carefully.

For more information refer to the [Latency Monitoring Framework page](https://redis.io/docs/latest/operate/oss_and_stack/management/optimization/latency-monitor).

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): a human readable latency analysis report.

**RESP3:**

[Verbatim string reply](../../develop/reference/protocol-spec#verbatim-strings): a human readable latency analysis report.



