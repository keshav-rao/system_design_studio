# LATENCY HISTOGRAM

```json metadata
{
  "schema_version": 2,
  "title": "LATENCY HISTOGRAM",
  "description": "Returns the cumulative distribution of latencies of a subset or all commands.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"command","multiple":true,"name":"command","optional":true,"type":"string"}],
  "syntax_fmt": "LATENCY HISTOGRAM [command [command ...]]",
  "complexity": "O(N) where N is the number of commands with latency information being retrieved.",
  "group": "server",
  "command_flags": ["admin","noscript","loading","stale"],
  "acl_categories": ["@admin","@slow","@dangerous"],
  "since": "7.0.0",
  "arity": -2,
  "tableOfContents": {"sections":[{"id":"optional-arguments","title":"Optional arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

`LATENCY HISTOGRAM` returns a cumulative distribution of commands' latencies in histogram format.

By default, all available latency histograms are returned.
You can filter the reply by providing specific command names.

Each histogram consists of the following fields:

* Command name
* The total calls for that command
* A map of time buckets:
  * Each bucket represents a latency range
  * Each bucket covers twice the previous bucket's range
  * Empty buckets are excluded from the reply
  * The tracked latencies are between 1 nanosecond and roughly 1 second
  * Everything above 1 second is considered +Inf
  * At max, there will be log2(1,000,000,000) = 30 buckets

This command requires the extended latency monitoring feature to be enabled, which is the default.
If you need to enable it, call `CONFIG SET latency-tracking yes`.

To delete the latency histograms' data use the [`CONFIG RESETSTAT`](https://redis.io/docs/latest/commands/config-resetstat) command.

## Optional arguments

<details open><summary><code>command [command ...]</code></summary>

One or more command names to return latency histograms for. If omitted, histograms for all commands are returned.

</details>

## Examples

```
127.0.0.1:6379> LATENCY HISTOGRAM set
1# "set" =>
   1# "calls" => (integer) 100000
   2# "histogram_usec" =>
      1# (integer) 1 => (integer) 99583
      2# (integer) 2 => (integer) 99852
      3# (integer) 4 => (integer) 99914
      4# (integer) 8 => (integer) 99940
      5# (integer) 16 => (integer) 99968
      6# (integer) 33 => (integer) 100000
```

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Array reply](../../develop/reference/protocol-spec#arrays): a map where each key is a command name, and each value is a map with the total calls, and an inner map of the histogram time buckets.

**RESP3:**

[Map reply](../../develop/reference/protocol-spec#maps): a map where each key is a command name, and each value is a map with the total calls, and an inner map of the histogram time buckets.



