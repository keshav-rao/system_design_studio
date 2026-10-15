# HOTKEYS GET

```json metadata
{
  "schema_version": 2,
  "title": "HOTKEYS GET",
  "description": "Returns lists of top K hotkeys depending on metrics chosen in HOTKEYS START command.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "HOTKEYS GET",
  "complexity": "O(K) where K is the number of hotkeys returned.",
  "group": "server",
  "command_flags": ["admin","noscript"],
  "acl_categories": ["@admin","@slow","@dangerous"],
  "since": "8.6.0",
  "arity": 2,
  "tableOfContents": {"sections":[{"id":"example-both-net-and-cpu-metrics-specified","title":"Example (both NET and CPU metrics specified)"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Returns tracking results and metadata from the current or most recent hotkeys tracking session.

This command returns comprehensive information about the hotkeys tracking session, including:

- Tracking metadata (start time, duration, sample ratio, etc.)
- Performance statistics (CPU time, network bytes)
- Lists of top K hot keys sorted by the metrics specified in `HOTKEYS START`

The following metrics are collected for non-clustered as well as clustered Redis environments:

- `tracking-active` (integer): 1 if tracking is active, 0 if stopped
- `sample-ratio` (integer): The sampling ratio used during tracking
- `selected-slots` (array): [Array](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) of select slots and slot ranges
- `all-commands-all-slots-us` (integer): CPU time in microseconds for all commands on all slots
- `net-bytes-all-commands-all-slots` (integer): Network bytes for all commands on all slots
- `collection-start-time-unix-ms` (integer): Unix timestamp in milliseconds when tracking started
- `collection-duration-ms` (integer): Duration of tracking in milliseconds
- `total-cpu-time-user-ms` (integer): User CPU time used in milliseconds (only when the `CPU` metric was specified with `HOTKEYS START`)
- `total-cpu-time-sys-ms` (integer): System CPU time used in milliseconds (only when the `CPU` metric was specified with `HOTKEYS START`)
- `total-net-bytes` (integer): Total network bytes processed (only when the `NET` metric was specified with `HOTKEYS START`)
- `by-cpu-time-us` (array): [Array](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) of key-time pairs sorted by CPU time in microseconds (only when the `CPU` metric was specified with `HOTKEYS START`)
- `by-net-bytes` (array): [Array](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) of key-bytes pairs sorted by network bytes (only when the `NET` metric was specified with `HOTKEYS START`)

The following additional results are collected only on clustered Redis environments, when `SLOTS` was used with `HOTKEYS START`:

- `sampled-commands-selected-slots-us` (integer): CPU time in milliseconds for sampled commands in selected slots (only when `SAMPLE` was used with `HOTKEYS START`)
- `all-commands-selected-slots-us` (integer): CPU time in milliseconds for all commands in selected slots
- `net-bytes-sampled-commands-selected-slots` (integer): Network bytes for sampled commands in selected slots (only when `SAMPLE` was used with `HOTKEYS START`)
- `net-bytes-all-commands-selected-slots` (integer): Network bytes for all commands on selected slots


## Example (both `NET` and `CPU` metrics specified)

```
HOTKEYS GET
1)  1) "tracking-active"
    2) (integer) 0
    3) "sample-ratio"
    4) (integer) 1
    5) "selected-slots"
    6) 1) 1) (integer) 0
          2) (integer) 16383
    7) "all-commands-all-slots-us"
    8) (integer) 103
    9) "net-bytes-all-commands-all-slots"
   10) (integer) 2042
   11) "collection-start-time-unix-ms"
   12) (integer) 1770824933147
   13) "collection-duration-ms"
   14) (integer) 0
   15) "total-cpu-time-user-ms"
   16) (integer) 23
   17) "total-cpu-time-sys-ms"
   18) (integer) 7
   19) "total-net-bytes"
   20) (integer) 2038
   21) "by-cpu-time-us"
   22)  1) "hotkey_001_counter"
        2) (integer) 29
        3) "hotkey_001"
        4) (integer) 25
        5) "hotkey_001_hash"
        6) (integer) 11
        7) "hotkey_001_list"
        8) (integer) 9
        9) "hotkey_001_set"
       10) (integer) 9
   23) "by-net-bytes"
   24)  1) "hotkey_001"
        2) (integer) 446
        3) "hotkey_002"
        4) (integer) 328
        5) "hotkey_001_hash"
        6) (integer) 198
        7) "hotkey_001_set"
        8) (integer) 167
        9) "hotkey_001_counter"
       10) (integer) 116
```

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

One of the following:

- [Array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) when tracking data is available, containing a single array with alternating field names and values.
- [Null reply](https://redis.io/docs/latest/develop/reference/protocol-spec#bulk-strings) when no tracking has been started or data has been reset.

**RESP3:**

One of the following:

- [Array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) when tracking data is available, containing a single [map](https://redis.io/docs/latest/develop/reference/protocol-spec#maps) with field names and values.
- [Null reply](https://redis.io/docs/latest/develop/reference/protocol-spec#bulk-strings) when no tracking has been started or data has been reset.



