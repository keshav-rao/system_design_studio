# FT.SPELLCHECK

```json metadata
{
  "schema_version": 2,
  "title": "FT.SPELLCHECK",
  "description": "Performs spelling correction on a query, returning suggestions for misspelled terms",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"index","type":"string"},{"name":"query","type":"string"},{"name":"distance","optional":true,"token":"DISTANCE","type":"integer"},{"arguments":[{"arguments":[{"name":"include","token":"INCLUDE","type":"pure-token"},{"name":"exclude","token":"EXCLUDE","type":"pure-token"}],"name":"inclusion","type":"oneof"},{"name":"dictionary","type":"string"},{"multiple":true,"name":"terms","optional":true,"type":"string"}],"name":"terms","optional":true,"token":"TERMS","type":"block"},{"name":"dialect","optional":true,"since":"2.4.3","token":"DIALECT","type":"integer"}],
  "syntax_fmt": "FT.SPELLCHECK index query [DISTANCE distance] [TERMS \u003cINCLUDE |\n  EXCLUDE\u003e dictionary [terms [terms ...]]] [DIALECT dialect]",
  "complexity": "O(1)",
  "group": "search",
  "command_flags": ["readonly"],
  "acl_categories": ["@search"],
  "since": "1.4.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"return","title":"Return"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"see-also","title":"See also"},{"id":"related-topics","title":"Related topics"}]}

,
  "codeExamples": []
}
```


Perform spelling correction on a query, returning suggestions for misspelled terms

[Examples](#examples)

## Required arguments

<details open>
<summary><code>index</code></summary>

is index with the indexed terms.
</details>

<details open>
<summary><code>query</code></summary> 

is search query.
</details>

See [Spellchecking](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/spellcheck) for more details.

## Optional arguments

<details open>
<summary><code>TERMS</code></summary>

specifies an inclusion (`INCLUDE`) or exclusion (`EXCLUDE`) of a custom dictionary. To learn more about managing custom dictionaries, see [`FT.DICTADD`](https://redis.io/docs/latest/commands/ft.dictadd), [`FT.DICTDEL`](https://redis.io/docs/latest/commands/ft.dictdel), and [`FT.DICTDUMP`](https://redis.io/docs/latest/commands/ft.dictdump).

You can specify multiple inclusion and exclusion `TERMS`.
</details>

<details open>
<summary><code>DISTANCE</code></summary> 

is maximum Levenshtein distance for spelling suggestions (default: 1, max: 4).
</details>

<details open>
<summary><code>DIALECT {dialect_version}</code></summary> 

selects the dialect version under which to execute the query. If not specified, the query will execute under the default dialect version set during module initial loading or via [`FT.CONFIG SET`](https://redis.io/docs/latest/commands/ft.config-set) command.
</details>

## Return

FT.SPELLCHECK returns an array reply, in which each element represents a misspelled term from the query. The misspelled terms are ordered by their order of appearance in the query. 
Each misspelled term, in turn, is a 3-element array consisting of the constant string `TERM`, the term itself and an array of suggestions for spelling corrections.
Each element in the spelling corrections array consists of the score of the suggestion and the suggestion itself. The suggestions array, per misspelled term, is ordered in descending order by score.
The score is calculated by dividing the number of documents in which the suggested term exists by the total number of documents in the index. Results can be normalized by dividing scores by the highest score.

## Examples

<details open>
<summary><b>Perform spelling correction on a query</b></summary>


127.0.0.1:6379> FT.SPELLCHECK idx held DISTANCE 2
1) 1) "TERM"
   2) "held"
   3) 1) 1) "0.66666666666666663"
         2) "hello"
      2) 1) "0.33333333333333331"
         2) "help"

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis Cloud<br />Flexible & Annual | Redis Cloud<br />Free & Fixed | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Array](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) of spell check results for each term.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: no such index.

**RESP3:**

One of the following:
* [Map](https://redis.io/docs/latest/develop/reference/protocol-spec#maps) with a `results` key containing spell check results for each term.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: no such index.



## See also

[`FT.CONFIG SET`](https://redis.io/docs/latest/commands/ft.config-set) | [`FT.DICTADD`](https://redis.io/docs/latest/commands/ft.dictadd) | [`FT.DICTDEL`](https://redis.io/docs/latest/commands/ft.dictdel) | [`FT.DICTDUMP`](https://redis.io/docs/latest/commands/ft.dictdump)

## Related topics

- [Spellchecking](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/spellcheck)
- [RediSearch](https://redis.io/docs/latest/develop/ai/search-and-query)
