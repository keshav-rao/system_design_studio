# FT.EXPLAINCLI

```json metadata
{
  "schema_version": 2,
  "title": "FT.EXPLAINCLI",
  "description": "Returns the execution plan for a complex query",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"index","type":"string"},{"name":"query","type":"string"},{"name":"dialect","optional":true,"since":"2.4.3","token":"DIALECT","type":"integer"}],
  "syntax_fmt": "FT.EXPLAINCLI index query [DIALECT dialect]",
  "complexity": "O(1)",
  "group": "search",
  "command_flags": ["readonly"],
  "acl_categories": ["@search"],
  "since": "1.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"see-also","title":"See also"},{"id":"related-topics","title":"Related topics"}]}

,
  "codeExamples": []
}
```


Return the execution plan for a complex query but formatted for easier reading without using `redis-cli --raw`

[Examples](#examples)

## Required arguments

<details open>
<summary><code>index</code></summary>

is index name. You must first create the index using [`FT.CREATE`](https://redis.io/docs/latest/commands/ft.create).
</details>

<details open>
<summary><code>query</code></summary>

is query string, as if sent to FT.SEARCH`.
</details>

## Optional arguments

<details open>
<summary><code>DIALECT {dialect_version}</code></summary>

is dialect version under which to execute the query. If not specified, the query executes under the default dialect version set during module initial loading or via [`FT.CONFIG SET`](https://redis.io/docs/latest/commands/ft.config-set) command.

> [!NOTE]
>  
> In the returned response, a `+` on a term is an indication of stemming.

</details>

## Examples

<details open>
<summary><b>Return the execution plan for a complex query</b></summary>


$ redis-cli

127.0.0.1:6379> FT.EXPLAINCLI rd "(foo bar)|(hello world) @date:[100 200]|@date:[500 +inf]"
 1) INTERSECT {
 2)   UNION {
 3)     INTERSECT {
 4)       UNION {
 5)         foo
 6)         +foo(expanded)
 7)       }
 8)       UNION {
 9)         bar
10)         +bar(expanded)
11)       }
12)     }
13)     INTERSECT {
14)       UNION {
15)         hello
16)         +hello(expanded)
17)       }
18)       UNION {
19)         world
20)         +world(expanded)
21)       }
22)     }
23)   }
24)   UNION {
25)     NUMERIC {100.000000 <= @date <= 200.000000}
26)     NUMERIC {500.000000 <= @date <= inf}
27)   }
28) }
29)

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis Cloud<br />Flexible & Annual | Redis Cloud<br />Free & Fixed | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Array](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) of [bulk string replies](https://redis.io/docs/latest/develop/reference/protocol-spec#bulk-strings) containing the query execution plan in CLI format.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: no such index, syntax error in query.

**RESP3:**

One of the following:
* [Array](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) of [bulk string replies](https://redis.io/docs/latest/develop/reference/protocol-spec#bulk-strings) containing the query execution plan in CLI format.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: no such index, syntax error in query.



## See also

[`FT.CREATE`](https://redis.io/docs/latest/commands/ft.create) | [`FT.SEARCH`](https://redis.io/docs/latest/commands/ft.search) | [`FT.CONFIG SET`](https://redis.io/docs/latest/commands/ft.config-set)

## Related topics

[RediSearch](https://redis.io/docs/latest/develop/ai/search-and-query)


