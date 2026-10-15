# FUNCTION LIST

```json metadata
{
  "schema_version": 2,
  "title": "FUNCTION LIST",
  "description": "Returns information about all libraries.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"library-name-pattern","name":"library-name-pattern","optional":true,"token":"LIBRARYNAME","type":"string"},{"display_text":"withcode","name":"withcode","optional":true,"token":"WITHCODE","type":"pure-token"}],
  "syntax_fmt": "FUNCTION LIST [LIBRARYNAME library-name-pattern] [WITHCODE]",
  "complexity": "O(N) where N is the number of functions",
  "group": "scripting",
  "command_flags": ["noscript"],
  "acl_categories": ["@slow","@scripting"],
  "since": "7.0.0",
  "arity": -2,
  "tableOfContents": {"sections":[{"id":"optional-arguments","title":"Optional arguments"},{"id":"details","title":"Details"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Return information about loaded functions and libraries.

For more information see [Introduction to Redis Functions](https://redis.io/docs/latest/develop/programmability/functions-intro).

## Optional arguments

<details open><summary><code>LIBRARYNAME library-name-pattern</code></summary>

List only libraries whose names match the given pattern.

</details>

<details open><summary><code>WITHCODE</code></summary>

Include the source code of each library in the reply.

</details>

## Details

The following information is provided for each of the libraries in the response:

* `library_name:` the name of the library.
* `engine:` the engine of the library.
* `functions:` the list of functions in the library.
  Each function has the following fields:
  * `name:` the name of the function.
  * `description:` the function's description.
  * `flags:` an array of [function flags](https://redis.io/docs/latest/develop/programmability/functions-intro#function-flags).
* `library_code:` the library's source code (when given the `WITHCODE` modifier).

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Array reply](../../develop/reference/protocol-spec#arrays): information about loaded functions and libraries.

**RESP3:**

[Map reply](../../develop/reference/protocol-spec#maps): information about loaded functions and libraries.



