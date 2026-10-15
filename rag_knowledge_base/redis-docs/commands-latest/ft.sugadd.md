# FT.SUGADD

```json metadata
{
  "schema_version": 2,
  "title": "FT.SUGADD",
  "description": "Adds a suggestion string to an auto-complete suggestion dictionary",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"key","type":"string"},{"name":"string","type":"string"},{"name":"score","type":"double"},{"arguments":[{"name":"incr","token":"INCR","type":"pure-token"}],"name":"increment score","optional":true,"type":"oneof"},{"name":"payload","optional":true,"token":"PAYLOAD","type":"string"}],
  "syntax_fmt": "FT.SUGADD key string score [INCR] [PAYLOAD payload]",
  "complexity": "O(1)",
  "group": "suggestion",
  "acl_categories": ["@search","@write"],
  "since": "1.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"see-also","title":"See also"},{"id":"related-topics","title":"Related topics"}]}

,
  "codeExamples": []
}
```


Add a suggestion string to an auto-complete suggestion dictionary

[Examples](#examples)

## Required arguments

<details open>
<summary><code>key</code></summary>

is suggestion dictionary key.
</details>

<details open>
<summary><code>string</code></summary> 

is suggestion string to index.
</details>

<details open>
<summary><code>score</code></summary> 

is floating point number of the suggestion string's weight.
</details>

The auto-complete suggestion dictionary is disconnected from the index definitions and leaves creating and updating suggestions dictionaries to the user.

## Optional arguments

<details open>
<summary><code>INCR</code></summary> 

increments the existing entry of the suggestion by the given score, instead of replacing the score. This is useful for updating the dictionary based on user queries in real time.
</details>

<details open>
<summary><code>PAYLOAD {payload}</code></summary> 

saves an extra payload with the suggestion, that can be fetched by adding the `WITHPAYLOADS` argument to [`FT.SUGGET`](https://redis.io/docs/latest/commands/ft.sugget).
</details>

## Examples

<details open>
<summary><b>Add a suggestion string to an auto-complete suggestion dictionary</b></summary>


127.0.0.1:6379> FT.SUGADD sug "hello world" 1
(integer) 3

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | Not supported on clustered databases. |

## Return information

**RESP2:**

[Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers): number of elements added to the suggestion dictionary.

**RESP3:**

[Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers): number of elements added to the suggestion dictionary.



## See also

[`FT.SUGGET`](https://redis.io/docs/latest/commands/ft.sugget) | [`FT.SUGDEL`](https://redis.io/docs/latest/commands/ft.sugdel) | [`FT.SUGLEN`](https://redis.io/docs/latest/commands/ft.suglen) 

## Related topics

[RediSearch](https://redis.io/docs/latest/develop/ai/search-and-query)
