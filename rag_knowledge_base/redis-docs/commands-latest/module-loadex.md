# MODULE LOADEX

```json metadata
{
  "schema_version": 2,
  "title": "MODULE LOADEX",
  "description": "Loads a module using extended parameters.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"path","name":"path","type":"string"},{"arguments":[{"display_text":"name","name":"name","type":"string"},{"display_text":"value","name":"value","type":"string"}],"multiple":true,"multiple_token":true,"name":"configs","optional":true,"token":"CONFIG","type":"block"},{"display_text":"args","multiple":true,"name":"args","optional":true,"token":"ARGS","type":"string"}],
  "syntax_fmt": "MODULE LOADEX path [CONFIG name value [CONFIG name value ...]]\n  [ARGS args [args ...]]",
  "complexity": "O(1)",
  "group": "server",
  "command_flags": ["admin","noscript","no_async_loading"],
  "acl_categories": ["@admin","@slow","@dangerous"],
  "since": "7.0.0",
  "arity": -3,
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Loads a module from a dynamic library at runtime with configuration directives.

This is an extended version of the [`MODULE LOAD`](https://redis.io/docs/latest/commands/module-load) command.

It loads and initializes the Redis module from the dynamic library specified by the `path` argument. The `path` should be the absolute path of the library, including the full filename.

You can use the optional `CONFIG` argument to provide the module with configuration directives.
Any additional arguments that follow the `ARGS` keyword are passed unmodified to the module.

**Note**: modules can also be loaded at server startup with `loadmodule`
configuration directive in `redis.conf`.

## Required arguments

<details open><summary><code>path</code></summary>

The absolute path to the module library file.

</details>

## Optional arguments

<details open><summary><code>CONFIG name value [CONFIG name value ...]</code></summary>

One or more module configuration name-value pairs to set at load time.

</details>

<details open><summary><code>ARGS args [args ...]</code></summary>

Additional arguments passed to the module's initialization function.

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK` if the module was loaded.

**RESP3:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK` if the module was loaded.



