# JSON.GET

```json metadata
{
  "schema_version": 2,
  "title": "JSON.GET",
  "description": "Gets the value at one or more paths in JSON serialized form",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"key","type":"key"},{"name":"indent","optional":true,"token":"INDENT","type":"string"},{"name":"newline","optional":true,"token":"NEWLINE","type":"string"},{"name":"space","optional":true,"token":"SPACE","type":"string"},{"multiple":true,"name":"path","optional":true,"type":"string"}],
  "syntax_fmt": "JSON.GET key [INDENT indent] [NEWLINE newline] [SPACE space] [path\n  [path ...]]",
  "complexity": "O(N) when path is evaluated to a single value where N is the size of the value, O(N) when path is evaluated to multiple values, where N is the size of the key",
  "group": "json",
  "acl_categories": ["@json","@read","@slow"],
  "since": "1.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"see-also","title":"See also"},{"id":"related-topics","title":"Related topics"}]}

,
  "codeExamples": []
}
```

Return the value at `path` in JSON serialized form

[Examples](#examples)

## Required arguments

<details open><summary><code>key</code></summary> 

is key to parse.
</details>

## Optional arguments

<details open><summary><code>path</code></summary> 

is JSONPath to specify. Default is root `$`. JSON.GET accepts multiple `path` arguments.

> [!NOTE]
> When using a single JSONPath, the root of the matching values is a JSON string with a top-level **array** of serialized JSON value. 
> In contrast, a legacy path returns a single value.
>
> When using multiple JSONPath arguments, the root of the matching values is a JSON string with a top-level **object**, with each object value being a top-level array of serialized JSON value.
> In contrast, if all paths are legacy paths, each object value is a single serialized JSON value.
> If there are multiple paths that include both legacy path and JSONPath, the returned value conforms to the JSONPath version (an array of values).

</details>

<details open><summary><code>INDENT</code></summary> 

sets the indentation string for nested levels.
</details>

<details open><summary><code>NEWLINE</code></summary> 

sets the string that's printed at the end of each line.
</details>

<details open><summary><code>SPACE</code></summary> 

sets the string that's put between a key and a value.
</details>
 
Produce pretty-formatted JSON with `redis-cli` by following this example:


~/$ redis-cli --raw
redis> JSON.GET myjsonkey INDENT "\t" NEWLINE "\n" SPACE " " path.to.value[1]


## Examples

<details open>
<summary><b>Return the value at <code>path</code> in JSON serialized form</b></summary>

Create a JSON document.


redis> JSON.SET doc $ '{"a":2, "b": 3, "nested": {"a": 4, "b": null}}'
OK


With a single JSONPath (JSON array bulk string):


redis>  JSON.GET doc $..b
"[3,null]"


Using multiple paths with at least one JSONPath returns a JSON string with a top-level object with an array of JSON values per path:


redis> JSON.GET doc ..a $..b
"{\"$..b\":[3,null],\"..a\":[2,4]}"

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

**RESP2:**

[Bulk string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#bulk-strings): a JSON-encoded string representing the value(s) at the specified path(s).

With a single path, returns the JSON serialization of the value at that path.
With multiple paths, returns a JSON object where each key is a path and each value is an array of JSON serializations.

**RESP3:**

[Bulk string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#bulk-strings): a JSON-encoded string with a top-level array containing the value(s) at the specified path(s).

With a single path using `$` (default in RESP3), returns a JSON array containing the serialized value.
With multiple paths, returns a JSON object where each key is a path and each value is an array of JSON serializations.



## See also

[`JSON.SET`](https://redis.io/docs/latest/commands/json.set) | [`JSON.MGET`](https://redis.io/docs/latest/commands/json.mget) 

## Related topics

* [RedisJSON](https://redis.io/docs/latest/develop/data-types/json)
* [Index and search JSON documents](https://redis.io/docs/latest/develop/ai/search-and-query/indexing)

