# TS.MGET

```json metadata
{
  "schema_version": 2,
  "title": "TS.MGET",
  "description": "Get the sample with the highest timestamp from each time series matching a specific filter",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"LATEST","optional":true,"since":"1.8.0","type":"string"},{"arguments":[{"name":"WITHLABELS","token":"WITHLABELS","type":"pure-token"},{"arguments":[{"name":"SELECTED_LABELS","token":"SELECTED_LABELS","type":"pure-token"},{"multiple":true,"name":"label1","type":"string"}],"name":"SELECTED_LABELS_BLOCK","type":"block"}],"name":"labels","optional":true,"type":"oneof"},{"arguments":[{"name":"l=v","type":"string"},{"name":"l!=v","type":"string"},{"name":"l=","type":"string"},{"name":"l!=","type":"string"},{"name":"l=(v1,v2,...)","type":"string"},{"name":"l!=(v1,v2,...)","type":"string"}],"multiple":true,"name":"filterExpr","token":"FILTER","type":"oneof"}],
  "syntax_fmt": "TS.MGET [LATEST] [WITHLABELS | SELECTED_LABELS label1 [label1 ...]]\n  FILTER \u003cl=v | l!=v | l= | l!= | l=(v1,v2,...) | l!=(v1,v2,...)\n  [l=v | l!=v | l= | l!= | l=(v1,v2,...) | l!=(v1,v2,...) ...]\u003e",
  "complexity": "O(n) where n is the number of time-series that match the filters",
  "group": "timeseries",
  "acl_categories": ["@timeseries","@read","@slow"],
  "since": "1.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"see-also","title":"See also"},{"id":"related-topics","title":"Related topics"}]}

,
  "codeExamples": []
}
```

> [!NOTE]
> This command's behavior varies in clustered Redis environments. See the [multi-key operations](https://redis.io/docs/latest/develop/using-commands/multi-key-operations) page for more information.



Get the sample with the highest timestamp from each time series matching a specific filter. Starting from Redis 8.6, NaN values are included in the results.

> [!NOTE]
> This command will reply only if the current user has read access to all keys that match the filter.
> Otherwise, it will reply with "*(error): current user doesn't have read permission to one or more keys that match the specified filter*".

[Examples](#examples)

## Required arguments

<details open>
<summary><code>FILTER filterExpr...</code></summary>

filters time series based on their labels and label values.

Each filter expression has one of the following syntaxes:

  - `label!=` - the time series has a label named `label`
  - `label=value` - the time series has a label named `label` with a value equal to `value`
  - `label=(value1,value2,...)` - the time series has a label named `label` with a value equal to one of the values in the list
  - `label=` - the time series does not have a label named `label`
  - `label!=value` - the time series does not have a label named `label` with a value equal to `value`
  - `label!=(value1,value2,...)` - the time series does not have a label named `label` with a value equal to any of the values in the list

  <note><b>Notes:</b>
   - At least one filter expression with a syntax `label=value` or `label=(value1,value2,...)` is required.
   - Filter expressions are conjunctive. For example, the filter `type=temperature room=study` means that `type=temperature` AND `room=study`.
   - Whitespace is not allowed in a filter expression except between quotes or double quotes in values - for example, `x="y y"` or `x='(y y,z z)'`.
   </note>

</details>

## Optional arguments

<details open>
<summary><code>LATEST</code> (since RedisTimeSeries v1.8)</summary> 

is used when a time series is a compaction. With `LATEST`, TS.MGET also reports the compacted value of the latest (possibly partial) bucket, given that this bucket's start time falls within `[fromTimestamp, toTimestamp]`. Without `LATEST`, TS.MGET does not report the latest (possibly partial) bucket. When a time series is not a compaction, `LATEST` is ignored.
  
The data in the latest bucket of a compaction is possibly partial. A bucket is _closed_ and compacted only upon the arrival of a new sample that _opens_ a new _latest_ bucket. There are cases, however, when the compacted value of the latest (possibly partial) bucket is also required. In such a case, use `LATEST`.
</details>

<details open>
<summary><code>WITHLABELS</code></summary> 

includes in the reply all label-value pairs representing metadata labels of the time series. 
If `WITHLABELS` or `SELECTED_LABELS` are not specified, by default, an empty list is reported as label-value pairs.

</details>

<details open>
<summary><code>SELECTED_LABELS label...</code> (since RedisTimeSeries v1.6)</summary> 

returns a subset of the label-value pairs that represent metadata labels of the time series. 
Use when a large number of labels exists per series, but only the values of some of the labels are required. 
If `WITHLABELS` or `SELECTED_LABELS` are not specified, by default, an empty list is reported as label-value pairs.

</details>

<note><b>Note:</b> The [`MGET`](https://redis.io/docs/latest/commands/mget) command cannot be part of a transaction when running on a Redis cluster.</note>

## Examples

<details open>
<summary><b>Select labels to retrieve</b></summary>

Create time series for temperature in Tel Aviv and Jerusalem, then add different temperature samples.


redis> TS.CREATE temp:TLV LABELS type temp location TLV
OK
redis> TS.CREATE temp:JLM LABELS type temp location JLM
OK
redis> TS.MADD temp:TLV 1000 30 temp:TLV 1010 35 temp:TLV 1020 9999 temp:TLV 1030 40
1) (integer) 1000
2) (integer) 1010
3) (integer) 1020
4) (integer) 1030
redis> TS.MADD temp:JLM 1005 30 temp:JLM 1015 35 temp:JLM 1025 9999 temp:JLM 1035 40
1) (integer) 1005
2) (integer) 1015
3) (integer) 1025
4) (integer) 1035


Get all the labels associated with the last sample.


redis> TS.MGET WITHLABELS FILTER type=temp
1) 1) "temp:JLM"
   2) 1) 1) "type"
         2) "temp"
      2) 1) "location"
         2) "JLM"
   3) 1) (integer) 1035
      2) 40
2) 1) "temp:TLV"
   2) 1) 1) "type"
         2) "temp"
      2) 1) "location"
         2) "TLV"
   3) 1) (integer) 1030
      2) 40


To get only the `location` label for each last sample, use `SELECTED_LABELS`.


redis> TS.MGET SELECTED_LABELS location FILTER type=temp
1) 1) "temp:JLM"
   2) 1) 1) "location"
         2) "JLM"
   3) 1) (integer) 1035
      2) 40
2) 1) "temp:TLV"
   2) 1) 1) "location"
         2) "TLV"
   3) 1) (integer) 1030
      2) 40

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

**RESP2:**

[Array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays): for each time series matching the specified filters, the following is reported:
- [Bulk string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#bulk-strings): The time series key name
- [Array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays): label-value pairs ([Bulk string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#bulk-strings), [Bulk string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#bulk-strings))
  - By default, an empty array is reported
  - If `WITHLABELS` is specified, all labels associated with this time series are reported
  - If `SELECTED_LABELS label...` is specified, the selected labels are reported (null value when no such label defined)
- [Array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays): a single timestamp-value pair ([Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers), [Simple string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-strings))

**RESP3:**

[Map reply](https://redis.io/docs/latest/develop/reference/protocol-spec#maps): for each time series matching the specified filters, the following is reported:
- [Bulk string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#bulk-strings): The time series key name
- [Map reply](https://redis.io/docs/latest/develop/reference/protocol-spec#maps) or [Array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays): label-value pairs
  - By default, an empty array is reported
  - If `WITHLABELS` is specified, all labels associated with this time series are reported as a map
  - If `SELECTED_LABELS label...` is specified, the selected labels are reported as a map (null value when no such label defined)
- [Array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays): a single timestamp-value pair ([Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers), [Double reply](https://redis.io/docs/latest/develop/reference/protocol-spec#doubles))



## See also

[`TS.MRANGE`](https://redis.io/docs/latest/commands/ts.mrange) | [`TS.RANGE`](https://redis.io/docs/latest/commands/ts.range) | [`TS.MREVRANGE`](https://redis.io/docs/latest/commands/ts.mrevrange) | [`TS.REVRANGE`](https://redis.io/docs/latest/commands/ts.revrange)

## Related topics

[RedisTimeSeries](https://redis.io/docs/latest/develop/data-types/timeseries)


