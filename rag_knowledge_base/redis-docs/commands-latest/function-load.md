# FUNCTION LOAD

```json metadata
{
  "schema_version": 2,
  "title": "FUNCTION LOAD",
  "description": "Creates a library.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"replace","name":"replace","optional":true,"token":"REPLACE","type":"pure-token"},{"display_text":"function-code","name":"function-code","type":"string"}],
  "syntax_fmt": "FUNCTION LOAD [REPLACE] function-code",
  "complexity": "O(1) (considering compilation time is redundant)",
  "group": "scripting",
  "command_flags": ["write","denyoom","noscript"],
  "acl_categories": ["@write","@slow","@scripting"],
  "since": "7.0.0",
  "arity": -3,
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Load a library to Redis.

The command takes one required parameter: the source code that implements the library. The library payload must start with a _shebang_ statement that provides the library metadata, including the engine to use and the library name.

Use this shebang format:

`#!<engine name> name=<library name>`.

Currently, `<engine name>` must be `lua`.

For the Lua engine, the implementation should declare one or more entry points to the library with the [`redis.register_function()`](https://redis.io/docs/latest/develop/programmability/lua-api#redis.register_function) API.
Once loaded, you can call the functions in the library with the [`FCALL`](https://redis.io/docs/latest/commands/fcall) or [`FCALL_RO`](https://redis.io/docs/latest/commands/fcall_ro) commands, as appropriate.



For more information please refer to [Introduction to Redis Functions](https://redis.io/docs/latest/develop/programmability/functions-intro).

## Required arguments

<details open><summary><code>function-code</code></summary>

The library's source code. It must begin with a Shebang statement that declares the engine and library name, for example `#!lua name=mylib`.

</details>

## Optional arguments

<details open><summary><code>REPLACE</code></summary>

Replace an existing library that has the same name.

</details>

## Examples

The following example will create a library named `mylib` with a single function, `myfunc`, that returns the first argument it gets.

```
redis> FUNCTION LOAD "#!lua name=mylib \n redis.register_function('myfunc', function(keys, args) return args[1] end)"
mylib
redis> FCALL myfunc 0 hello
"hello"
```

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

One of the following:

- [Bulk string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#bulk-strings): the library name that was loaded.
- [Simple error string](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in the following circumstances: an invalid engine-name was provided, 
the library's name already exists without the `REPLACE` modifier, 
a function in the library is created with a name that already exists in another library (even when `REPLACE` is specified), 
the engine failed in creating the library's functions (for example, because of a compilation error), or 
no functions were declared by the library.

**RESP3:**

One of the following:

- [Bulk string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#bulk-strings): the library name that was loaded.
- [Simple error string](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in the following circumstances: an invalid engine-name was provided, 
the library's name already exists without the `REPLACE` modifier, 
a function in the library is created with a name that already exists in another library (even when `REPLACE` is specified), 
the engine failed in creating the library's functions (for example, because of a compilation error), or 
no functions were declared by the library.



