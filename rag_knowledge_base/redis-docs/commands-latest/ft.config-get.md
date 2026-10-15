# FT.CONFIG GET

```json metadata
{
  "schema_version": 2,
  "title": "FT.CONFIG GET",
  "description": "Retrieves runtime configuration options",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"option","type":"string"}],
  "syntax_fmt": "FT.CONFIG GET option",
  "complexity": "O(1)",
  "group": "search",
  "command_flags": ["readonly"],
  "acl_categories": ["@admin","@search"],
  "since": "1.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"see-also","title":"See also"},{"id":"related-topics","title":"Related topics"}]}

,
  "codeExamples": []
}
```


Retrieve configuration options

[Examples](#examples)

## Required arguments

<details open>
<summary><code>option</code></summary> 

is name of the configuration option, or '*' for all. 
</details>

## Examples

<details open>
<summary><b>Retrieve configuration options</b></summary>


127.0.0.1:6379> FT.CONFIG GET TIMEOUT
1) 1) TIMEOUT
   2) 42



127.0.0.1:6379> FT.CONFIG GET *
 1) 1) EXTLOAD
    2) (nil)
 2) 1) SAFEMODE
    2) true
 3) 1) CONCURRENT_WRITE_MODE
    2) false
 4) 1) NOGC
    2) false
 5) 1) MINPREFIX
    2) 2
 6) 1) FORKGC_SLEEP_BEFORE_EXIT
    2) 0
 7) 1) MAXDOCTABLESIZE
    2) 1000000
 8) 1) MAXSEARCHRESULTS
    2) 1000000
 9) 1) MAXAGGREGATERESULTS
    2) unlimited
10) 1) MAXEXPANSIONS
    2) 200
11) 1) MAXPREFIXEXPANSIONS
    2) 200
12) 1) TIMEOUT
    2) 42
13) 1) INDEX_THREADS
    2) 8
14) 1) SEARCH_THREADS
    2) 20
15) 1) FRISOINI
    2) (nil)
16) 1) ON_TIMEOUT
    2) return
17) 1) GCSCANSIZE
    2) 100
18) 1) MIN_PHONETIC_TERM_LEN
    2) 3
19) 1) GC_POLICY
    2) fork
20) 1) FORK_GC_RUN_INTERVAL
    2) 30
21) 1) FORK_GC_CLEAN_THRESHOLD
    2) 100
22) 1) FORK_GC_RETRY_INTERVAL
    2) 5
23) 1) FORK_GC_CLEAN_NUMERIC_EMPTY_NODES
    2) true
24) 1) _FORK_GC_CLEAN_NUMERIC_EMPTY_NODES
    2) true
25) 1) _MAX_RESULTS_TO_UNSORTED_MODE
    2) 1000
26) 1) UNION_ITERATOR_HEAP
    2) 20
27) 1) CURSOR_MAX_IDLE
    2) 300000
28) 1) NO_MEM_POOLS
    2) false
29) 1) PARTIAL_INDEXED_DOCS
    2) false
30) 1) UPGRADE_INDEX
    2) Upgrade config for upgrading
31) 1) _NUMERIC_COMPRESS
    2) false
32) 1) _FREE_RESOURCE_ON_THREAD
    2) true
33) 1) _PRINT_PROFILE_CLOCK
    2) true
34) 1) RAW_DOCID_ENCODING
    2) false
35) 1) _NUMERIC_RANGES_PARENTS
    2) 0
36) 1) MINSTEMLEN
    2) 4

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis Cloud<br />Flexible & Annual | Redis Cloud<br />Free & Fixed | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:-----------------|:------|
| <span title="Not supported"><nobr>&#x274c; Not supported</span> | <span title="Not supported"><nobr>&#x26A0;&#xFE0F; Not supported</span><sup>1</sup> | <span title="Not supported"><nobr>&#x274c; Not supported</nobr></span> |  |

1. </a>[Contact support](https://redis.com/company/support/) to view the current configuration values or request configuration changes for Flexible or Annual Redis Cloud subscriptions.

## Return information

**RESP2:**

[Array](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) of [arrays](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays), where each sub-array contains a configuration option name and its value.

**RESP3:**

[Map](https://redis.io/docs/latest/develop/reference/protocol-spec#maps) where keys are configuration option names and values are their corresponding values.



## See also

[`FT.CONFIG SET`](https://redis.io/docs/latest/commands/ft.config-set) | [`FT.CONFIG HELP`](https://redis.io/docs/latest/commands/ft.config-help)

## Related topics

[RediSearch](https://redis.io/docs/latest/develop/ai/search-and-query)
