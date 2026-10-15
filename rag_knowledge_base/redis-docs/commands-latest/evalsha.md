# EVALSHA

```json metadata
{
  "schema_version": 2,
  "title": "EVALSHA",
  "description": "Executes a server-side Lua script by SHA1 digest.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"sha1","name":"sha1","type":"string"},{"display_text":"numkeys","name":"numkeys","type":"integer"},{"display_text":"key","key_spec_index":0,"multiple":true,"name":"key","optional":true,"type":"key"},{"display_text":"arg","multiple":true,"name":"arg","optional":true,"type":"string"}],
  "syntax_fmt": "EVALSHA sha1 numkeys [key [key ...]] [arg [arg ...]]",
  "complexity": "Depends on the script that is executed.",
  "group": "scripting",
  "command_flags": ["noscript","stale","skip_monitor","no_mandatory_keys","movablekeys"],
  "acl_categories": ["@slow","@scripting"],
  "since": "2.6.0",
  "arity": -3,
  "key_specs": [{"RW":true,"access":true,"begin_search":{"spec":{"index":2},"type":"index"},"find_keys":{"spec":{"firstkey":1,"keynumidx":0,"keystep":1},"type":"keynum"},"update":true}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

> [!NOTE]
> This command's behavior varies in clustered Redis environments. See the [multi-key operations](https://redis.io/docs/latest/develop/using-commands/multi-key-operations) page for more information.


Evaluate a script from the server's cache by its SHA1 digest.

The server caches scripts by using the [`SCRIPT LOAD`](https://redis.io/docs/latest/commands/script-load) command.
The command is otherwise identical to [`EVAL`](https://redis.io/docs/latest/commands/eval).

Please refer to the [Redis Programmability](https://redis.io/docs/latest/develop/programmability) and [Introduction to Eval Scripts](https://redis.io/docs/latest/develop/programmability/eval-intro) for more information about Lua scripts.

## Required arguments

<details open><summary><code>sha1</code></summary>

The SHA1 digest of a script previously cached with `SCRIPT LOAD` or `EVAL`.

</details>

<details open><summary><code>numkeys</code></summary>

The number of key names that follow. Arguments after the keys are passed as regular arguments.

</details>

## Optional arguments

<details open><summary><code>key [key ...]</code></summary>

The key names the script accesses, provided to it via the Lua `KEYS` global variable. There must be exactly `numkeys` of them.

</details>

<details open><summary><code>arg [arg ...]</code></summary>

Additional arguments provided to the script via the Lua `ARGV` variable.

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

The return value depends on the script that was executed.

**RESP3:**

The return value depends on the script that was executed.



