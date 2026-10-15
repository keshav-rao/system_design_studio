# JSON.STRLEN

```json metadata
{
  "schema_version": 2,
  "title": "JSON.STRLEN",
  "description": "Returns the length of JSON strings at the paths matching a given path expression",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"key","type":"key"},{"name":"path","optional":true,"type":"string"}],
  "syntax_fmt": "JSON.STRLEN key [path]",
  "complexity": "O(1) when path is evaluated to a single value, O(N) when path is evaluated to multiple values, where N is the size of the key",
  "group": "json",
  "acl_categories": ["@json","@read","@slow"],
  "since": "1.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"see-also","title":"See also"},{"id":"related-topics","title":"Related topics"}]}

,
  "codeExamples": []
}
```

Returns the length of JSON strings at the paths matching a given path expression.

[Examples](#examples)

## Required arguments

<details open><summary><code>key</code></summary> 

is a Redis key storing a value of type JSON.

</details>

## Optional arguments

<details open><summary><code>path</code></summary> 

is either 

- A JSONPath expression
  - The root "`$`", or any string that starts with "`$.`" or "`$[`".
  - Resolves to all matching locations in `key`.
- A legacy path expression 
  - Any string that does not match the JSONPath syntax above.
  - Allow the leading "`.`" to be omitted (for example, "`name`" and "`.name`" are equivalent).
  - Resolves to only the first matching location in `key`.

Default: "`.`" (legacy path pointing to the root of the document).

</details>

## Examples


redis> JSON.SET doc $ '{"a":"foo", "nested": {"a": "hello"}, "nested2": {"a": 31}}'
OK
redis> JSON.STRLEN doc $..a
1) (integer) 3
2) (integer) 5
3) (nil)


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

**RESP2:**

If `path` is a JSONPath expression:

- A [simple error](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) if `key` does not exist.
- An empty [array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) if `path` has no matches.
- An [array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) where each array element corresponds to one match:
  - [`nil`](https://redis.io/docs/latest/develop/reference/protocol-spec#null-bulk-strings) if the match is not a string.
  - An [integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers): the length of the string.

If `path` is a legacy path expression:

- [`nil`](https://redis.io/docs/latest/develop/reference/protocol-spec#null-bulk-strings) if `key` does not exist.
- A [simple error](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) if `path` has no matches.
- A [simple error](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) if the first match is not a string.
- An [integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers): the length of the string at the first match.

**RESP3:**

If `path` is a JSONPath expression:

- A [simple error](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) if `key` does not exist.
- An empty [array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) if `path` has no matches.
- An [array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) where each array element corresponds to one match:
  - [`nil`](https://redis.io/docs/latest/develop/reference/protocol-spec#nulls) if the match is not a string.  
  - An [integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers): the length of the string.

If `path` is a legacy path expression:

- [`nil`](https://redis.io/docs/latest/develop/reference/protocol-spec#nulls) if `key` does not exist.
- A [simple error](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) if `path` has no matches.
- A [simple error](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) if the first match is not a string.
- An [integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers): the length of the string at the first match.



## See also

[`JSON.STRAPPEND`](https://redis.io/docs/latest/commands/json.strappend) | [`JSON.ARRLEN`](https://redis.io/docs/latest/commands/json.arrlen) | [`JSON.OBJLEN`](https://redis.io/docs/latest/commands/json.objlen) 

## Related topics

* [The JSON data type](https://redis.io/docs/latest/develop/data-types/json)
* [JSONPath](https://redis.io/docs/latest/develop/data-types/json/path)
* [Index and search JSON documents](https://redis.io/docs/latest/develop/ai/search-and-query/indexing)

