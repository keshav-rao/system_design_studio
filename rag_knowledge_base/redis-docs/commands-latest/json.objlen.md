# JSON.OBJLEN

```json metadata
{
  "schema_version": 2,
  "title": "JSON.OBJLEN",
  "description": "Returns the number of keys in JSON objects at the paths matching a given path expression",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"key","type":"key"},{"name":"path","optional":true,"type":"string"}],
  "syntax_fmt": "JSON.OBJLEN key [path]",
  "complexity": "O(1) when path is evaluated to a single value, O(N) when path is evaluated to multiple values, where N is the size of the key",
  "group": "json",
  "acl_categories": ["@json","@read","@slow"],
  "since": "1.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"see-also","title":"See also"},{"id":"related-topics","title":"Related topics"}]}

,
  "codeExamples": []
}
```

Returns the number of keys in JSON objects at the paths matching a given path expression.

> [!NOTE]
> A JSON object is a structure within a JSON document that contains an unordered set of key-value pairs (also called name-value pairs). Do not confuse Redis keys with JSON object keys.

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


redis> JSON.SET doc $ '{"a":[3], "nested": {"a": {"b":2, "c": 1}}}'
OK
redis> JSON.OBJLEN doc $..a
1) (nil)
2) (integer) 2


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
  - [`nil`](https://redis.io/docs/latest/develop/reference/protocol-spec#null-bulk-strings) if the match is not an object.
  - An [integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers): the number of keys in the object.

If `path` is a legacy path expression:

- [`nil`](https://redis.io/docs/latest/develop/reference/protocol-spec#null-bulk-strings) if `key` does not exist.
- [`nil`](https://redis.io/docs/latest/develop/reference/protocol-spec#null-bulk-strings) if `path` has no matches.
- A [simple error](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) if the first match is not an object.
- An [integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers): the number of keys in the first match.

**RESP3:**

If `path` is a JSONPath expression:

- A [simple error](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) if `key` does not exist.
- An empty [array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) if `path` has no matches.
- An [array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) where each array element corresponds to one match:
  - [`nil`](https://redis.io/docs/latest/develop/reference/protocol-spec#nulls) if the match is not an object.
  - An [integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers): the number of keys in the object.

If `path` is a legacy path expression:

- [`nil`](https://redis.io/docs/latest/develop/reference/protocol-spec#nulls) if `key` does not exist.
- [`nil`](https://redis.io/docs/latest/develop/reference/protocol-spec#nulls) if `path` has no matches.
- A [simple error](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) if the first match is not an object.
- An [integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers): the number of keys in the first match.



## See also

[`JSON.OBJKEYS`](https://redis.io/docs/latest/commands/json.objkeys)

## Related topics

* [The JSON data type](https://redis.io/docs/latest/develop/data-types/json)
* [JSONPath](https://redis.io/docs/latest/develop/data-types/json/path)
* [Index and search JSON documents](https://redis.io/docs/latest/develop/ai/search-and-query/indexing)

