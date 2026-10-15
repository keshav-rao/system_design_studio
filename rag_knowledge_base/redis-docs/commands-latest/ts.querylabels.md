# TS.QUERYLABELS

```json metadata
{
  "schema_version": 2,
  "title": "TS.QUERYLABELS",
  "description": "Get all label names, or all values of a given label, for time series matching a filter list, or all series",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"arguments":[{"display_text":"LABELS","name":"LABELS","token":"LABELS","type":"pure-token"},{"arguments":[{"display_text":"VALUES","name":"VALUES","token":"VALUES","type":"pure-token"},{"display_text":"label","name":"label","type":"string"}],"name":"VALUES","type":"block"}],"name":"subtype","type":"oneof"},{"arguments":[{"display_text":"FILTER","name":"FILTER","token":"FILTER","type":"pure-token"},{"display_text":"filterExpr","multiple":true,"name":"filterExpr","type":"string"}],"name":"FILTER","optional":true,"type":"block"}],
  "syntax_fmt": "TS.QUERYLABELS \u003cLABELS | VALUES label\u003e [FILTER filterExpr\n  [filterExpr ...]]",
  "complexity": "O(n) where n is the number of time-series that match the filters (all indexed series when FILTER is omitted)",
  "group": "timeseries",
  "command_flags": ["readonly","module"],
  "acl_categories": ["@read","@timeseries"],
  "since": "8.10.0",
  "arity": -2,
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"examples","title":"Examples"},{"children":[{"id":"access-control","title":"Access control"}],"id":"details","title":"Details"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"see-also","title":"See also"},{"id":"related-topics","title":"Related topics"}]}

,
  "codeExamples": []
}
```

> [!NOTE]
> This command's behavior varies in clustered Redis environments. See the [multi-key operations](https://redis.io/docs/latest/develop/using-commands/multi-key-operations) page for more information.

Get all label names, or all values of a given label, for the time series matching a filter list (or all series when no filter is given).

[Examples](#examples)

## Required arguments

<details open>
<summary><code>LABELS | VALUES label</code></summary>

selects what the command returns:

  - `LABELS` - returns the set of distinct label names used by the matching time series.
  - `VALUES label` - returns the set of distinct values of `label` used by the matching time series. The result is empty (not an error) when `label` does not exist or when no matching series carries it.

Each name or value appears at most once, regardless of how many series it belongs to. The order of the results is not defined.
</details>

## Optional arguments

<details open>
<summary><code>FILTER filterExpr [filterExpr ...]</code></summary>

restricts the command to the time series whose labels and label values match all of the filter expressions. When `FILTER` is omitted, the command considers all indexed time series.

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

## Examples

<details open>
<summary><b>List labels and label values for a set of sensors</b></summary>

Create a set of sensors to measure temperature and humidity in your study and kitchen.

```
redis> TS.CREATE telemetry:study:temperature LABELS room study type temperature
OK
redis> TS.CREATE telemetry:study:humidity LABELS room study type humidity
OK
redis> TS.CREATE telemetry:kitchen:temperature LABELS room kitchen type temperature
OK
redis> TS.CREATE telemetry:kitchen:humidity LABELS room kitchen type humidity
OK
```

Retrieve the label names used by the time series located in the kitchen.

```
redis> TS.QUERYLABELS LABELS FILTER room=kitchen
1) "room"
2) "type"
```

Retrieve the distinct values of the `type` label across all time series.

```
redis> TS.QUERYLABELS VALUES type
1) "humidity"
2) "temperature"
```
</details>

## Details

### Access control

Unlike [`TS.QUERYINDEX`](https://redis.io/docs/latest/commands/ts.queryindex), which lists every matching key whether or not the user has read access to it, `TS.QUERYLABELS` silently omits the time series that the user is not allowed to read. Label names and values that belong only to unreadable series do not appear in the result.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) where each element is a [Bulk string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#bulk-strings): a label name (with `LABELS`) or a label value (with `VALUES`). The array is empty if no time series matches the filter.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: invalid subtype, missing label after `VALUES`, or invalid filter expression.

**RESP3:**

One of the following:
* [Set reply](https://redis.io/docs/latest/develop/reference/protocol-spec#sets) where each element is a [Bulk string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#bulk-strings): a label name (with `LABELS`) or a label value (with `VALUES`). The set is empty if no time series matches the filter.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: invalid subtype, missing label after `VALUES`, or invalid filter expression.



## See also

[`TS.QUERYINDEX`](https://redis.io/docs/latest/commands/ts.queryindex) | [`TS.CREATE`](https://redis.io/docs/latest/commands/ts.create) | [`TS.MGET`](https://redis.io/docs/latest/commands/ts.mget) | [`TS.MRANGE`](https://redis.io/docs/latest/commands/ts.mrange)

## Related topics

[RedisTimeSeries](https://redis.io/docs/latest/develop/data-types/timeseries)

