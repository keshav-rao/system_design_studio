# TS.GET

```json metadata
{
  "schema_version": 2,
  "title": "TS.GET",
  "description": "Get the sample with the highest timestamp from a given time series",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"key","type":"key"},{"name":"LATEST","optional":true,"since":"1.8.0","type":"string"}],
  "syntax_fmt": "TS.GET key [LATEST]",
  "complexity": "O(1)",
  "group": "timeseries",
  "acl_categories": ["@timeseries","@read","@fast"],
  "since": "1.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"see-also","title":"See also"},{"id":"related-topics","title":"Related topics"}]}

,
  "codeExamples": []
}
```


Get the sample with the highest timestamp from a given time series. Starting from Redis 8.6, NaN values are included in the results.

[Examples](#examples)

## Required arguments

<details open><summary><code>key</code></summary> 

is key name for the time series.
</details>

## Optional arguments

<details open><summary><code>LATEST</code> (since RedisTimeSeries v1.8)</summary> 

is used when a time series is a compaction. With `LATEST`, TS.GET reports the compacted value of the latest (possibly partial) bucket. Without `LATEST`, TS.GET does not report the latest (possibly partial) bucket. When a time series is not a compaction, `LATEST` is ignored.
  
The data in the latest bucket of a compaction is possibly partial. A bucket is _closed_ and compacted only upon arrival of a new sample that _opens_ a new _latest_ bucket. There are cases, however, when the compacted value of the latest (possibly partial) bucket is also required. In such a case, use `LATEST`.
</details>

## Examples

<details open>
<summary><b>Get latest measured temperature for a city</b></summary>

Create a time series to store the temperatures measured in Tel Aviv and add four measurements for Sun Jan 01 2023
  

127.0.0.1:6379> TS.CREATE temp:TLV LABELS type temp location TLV
OK
127.0.0.1:6379> TS.MADD temp:TLV 1672534800 12 temp:TLV 1672556400 16 temp:TLV 1672578000 21 temp:TLV 1672599600 14

  
Next, get the latest measured temperature (the temperature with the highest timestamp)


127.0.0.1:6379> TS.GET temp:TLV
1) (integer) 1672599600
2) 14

</details>

<details open>
<summary><b>Get latest maximal daily temperature for a city</b></summary>

Create a time series to store the temperatures measured in Jerusalem


127.0.0.1:6379> TS.CREATE temp:JLM LABELS type temp location JLM
OK


Next, create a compacted time series named _dailyAvgTemp:JLM_ containing one compacted sample per 24 hours: the maximum of all measurements taken from midnight to next midnight.


127.0.0.1:6379> TS.CREATE dailyMaxTemp:JLM LABELS type temp location JLM
OK
127.0.0.1:6379> TS.CREATERULE temp:JLM dailyMaxTemp:JLM AGGREGATION max 86400000
OK


Add four measurements for Sun Jan 01 2023 and three measurements for Mon Jan 02 2023


127.0.0.1:6379> TS.MADD temp:JLM 1672534800000 12 temp:JLM 1672556400000 16 temp:JLM 1672578000000 21 temp:JLM 1672599600000 14
1) (integer) 1672534800000
2) (integer) 1672556400000
3) (integer) 1672578000000
4) (integer) 1672599600000
127.0.0.1:6379> TS.MADD temp:JLM 1672621200000 11 temp:JLM 1672642800000 21 temp:JLM 1672664400000 26
1) (integer) 1672621200000
2) (integer) 1672642800000
3) (integer) 1672664400000

  
Next, get the latest maximum daily temperature; do not report the latest, possibly partial, bucket 


127.0.0.1:6379> TS.GET dailyMaxTemp:JLM
1) (integer) 1672531200000
2) 21


Get the latest maximum daily temperature (the temperature with the highest timestamp); report the latest, possibly partial, bucket


127.0.0.1:6379> TS.GET dailyMaxTemp:JLM LATEST
1) (integer) 1672617600000
2) 26


</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) of a single ([Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers), [Simple string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-strings)) pair representing (timestamp, value) of the sample with the highest timestamp.
* An empty [Array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) when the time series is empty.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: invalid arguments, wrong key type, key does not exist, etc.

**RESP3:**

One of the following:
* [Array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) of a single ([Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers), [Double reply](https://redis.io/docs/latest/develop/reference/protocol-spec#doubles)) pair representing (timestamp, value) of the sample with the highest timestamp.
* An empty [Array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) when the time series is empty.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: invalid arguments, wrong key type, key does not exist, etc.



## See also

[`TS.MGET`](https://redis.io/docs/latest/commands/ts.mget)  

## Related topics

[RedisTimeSeries](https://redis.io/docs/latest/develop/data-types/timeseries)

