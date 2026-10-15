# TS.QUERYINDEX

```json metadata
{
  "schema_version": 2,
  "title": "TS.QUERYINDEX",
  "description": "Get all time series keys matching a filter list",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"arguments":[{"name":"l=v","type":"string"},{"name":"l!=v","type":"string"},{"name":"l=","type":"string"},{"name":"l!=","type":"string"},{"name":"l=(v1,v2,...)","type":"string"},{"name":"l!=(v1,v2,...)","type":"string"}],"multiple":true,"name":"filterExpr","type":"oneof"}],
  "syntax_fmt": "TS.QUERYINDEX \u003cl=v | l!=v | l= | l!= | l=(v1,v2,...) |\n  l!=(v1,v2,...) [l=v | l!=v | l= | l!= | l=(v1,v2,...) |\n  l!=(v1,v2,...) ...]\u003e",
  "complexity": "O(n) where n is the number of time-series that match the filters",
  "group": "timeseries",
  "acl_categories": ["@timeseries","@read","@slow"],
  "since": "1.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"see-also","title":"See also"},{"id":"related-topics","title":"Related topics"}]}

,
  "codeExamples": []
}
```

> [!NOTE]
> This command's behavior varies in clustered Redis environments. See the [multi-key operations](https://redis.io/docs/latest/develop/using-commands/multi-key-operations) page for more information.



Get all time series keys matching a filter list. Note: all matching keys will be listed, whether or not the user has read access.

[Examples](#examples)

## Required arguments

<details open>
<summary><code>filterExpr...</code></summary>

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

<note><b>Note:</b> The `QUERYINDEX` command cannot be part of a transaction when running on a Redis cluster.</note>

## Examples

<details open>
<summary><b>Find keys by location and sensor type</b></summary>

Create a set of sensors to measure temperature and humidity in your study and kitchen.


redis> TS.CREATE telemetry:study:temperature LABELS room study type temperature
OK
redis> TS.CREATE telemetry:study:humidity LABELS room study type humidity
OK
redis> TS.CREATE telemetry:kitchen:temperature LABELS room kitchen type temperature
OK
redis> TS.CREATE telemetry:kitchen:humidity LABELS room kitchen type humidity
OK


Retrieve keys of all time series representing sensors located in the kitchen. 


redis> TS.QUERYINDEX room=kitchen
1) "telemetry:kitchen:humidity"
2) "telemetry:kitchen:temperature"


To retrieve the keys of all time series representing sensors that measure temperature, use this query:


redis> TS.QUERYINDEX type=temperature
1) "telemetry:kitchen:temperature"
2) "telemetry:study:temperature"

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) where each element is a [Bulk string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#bulk-strings): a time series key. The array is empty if no time series matches the filter.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: invalid filter expression.

**RESP3:**

One of the following:
* [Set reply](https://redis.io/docs/latest/develop/reference/protocol-spec#sets) where each element is a [Bulk string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#bulk-strings): a time series key. The set is empty if no time series matches the filter.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: invalid filter expression.



## See also

[`TS.CREATE`](https://redis.io/docs/latest/commands/ts.create) | [`TS.MRANGE`](https://redis.io/docs/latest/commands/ts.mrange) | [`TS.MREVRANGE`](https://redis.io/docs/latest/commands/ts.mrevrange) | [`TS.MGET`](https://redis.io/docs/latest/commands/ts.mget)

## Related topics

[RedisTimeSeries](https://redis.io/docs/latest/develop/data-types/timeseries)

