# TS.DELETERULE

```json metadata
{
  "schema_version": 2,
  "title": "TS.DELETERULE",
  "description": "Delete a compaction rule",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"sourceKey","type":"key"},{"name":"destKey","type":"key"}],
  "syntax_fmt": "TS.DELETERULE sourceKey destKey",
  "complexity": "O(1)",
  "group": "timeseries",
  "acl_categories": ["@timeseries","@write","@fast"],
  "since": "1.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"see-also","title":"See also"},{"id":"related-topics","title":"Related topics"}]}

,
  "codeExamples": []
}
```

> [!NOTE]
> This command's behavior varies in clustered Redis environments. See the [multi-key operations](https://redis.io/docs/latest/develop/using-commands/multi-key-operations) page for more information.



Delete a compaction rule

## Required arguments

<details open><summary><code>sourceKey</code></summary>

is key name for the source time series.
</details>

<details open><summary><code>destKey</code></summary> 

is key name for destination (compacted) time series.
</details>

<note><b>Note:</b> This command does not delete the compacted series.</note>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Simple string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-strings): `OK` when the compaction rule is deleted successfully.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: invalid arguments, or when such rule does not exist.

**RESP3:**

One of the following:
* [Simple string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-strings): `OK` when the compaction rule is deleted successfully.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: invalid arguments, or when such rule does not exist.



## See also

[`TS.CREATERULE`](https://redis.io/docs/latest/commands/ts.createrule) 

## Related topics

[RedisTimeSeries](https://redis.io/docs/latest/develop/data-types/timeseries)

