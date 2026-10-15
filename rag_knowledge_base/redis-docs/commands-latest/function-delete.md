# FUNCTION DELETE

```json metadata
{
  "schema_version": 2,
  "title": "FUNCTION DELETE",
  "description": "Deletes a library and its functions.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"library-name","name":"library-name","type":"string"}],
  "syntax_fmt": "FUNCTION DELETE library-name",
  "complexity": "O(1)",
  "group": "scripting",
  "command_flags": ["write","noscript"],
  "acl_categories": ["@write","@slow","@scripting"],
  "since": "7.0.0",
  "arity": 3,
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Delete a library and all its functions.

This command deletes the library called `library-name` and all functions in it.
If the library doesn't exist, the server returns an error.

For more information please refer to [Introduction to Redis Functions](https://redis.io/docs/latest/develop/programmability/functions-intro).

## Required arguments

<details open><summary><code>library-name</code></summary>

The name of the library to delete.

</details>

## Examples

```
redis> FUNCTION LOAD "#!lua name=mylib \n redis.register_function('myfunc', function(keys, args) return 'hello' end)"
"mylib"
redis> FCALL myfunc 0
"hello"
redis> FUNCTION DELETE mylib
OK
redis> FCALL myfunc 0
(error) ERR Function not found
```

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.

**RESP3:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.



