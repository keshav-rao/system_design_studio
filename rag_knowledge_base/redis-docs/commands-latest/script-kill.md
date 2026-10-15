# SCRIPT KILL

```json metadata
{
  "schema_version": 2,
  "title": "SCRIPT KILL",
  "description": "Terminates a server-side Lua script during execution.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "SCRIPT KILL",
  "complexity": "O(1)",
  "group": "scripting",
  "command_flags": ["noscript","allow_busy"],
  "acl_categories": ["@slow","@scripting"],
  "since": "2.6.0",
  "arity": 2,
  "tableOfContents": {"sections":[{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Kills the currently executing [`EVAL`](https://redis.io/docs/latest/commands/eval) script, assuming no write operation was yet
performed by the script.

This command is mainly useful to kill a script that is running for too much
time(for instance, because it entered an infinite loop because of a bug).
The script will be killed, and the client currently blocked into EVAL will see
the command returning with an error.

If the script has already performed write operations, it can not be killed in this
way because it would violate Lua's script atomicity contract.
In such a case, only `SHUTDOWN NOSAVE` can kill the script, killing
the Redis process in a hard way and preventing it from persisting with half-written
information.

For more information about [`EVAL`](https://redis.io/docs/latest/commands/eval) scripts please refer to [Introduction to Eval Scripts](https://redis.io/docs/latest/develop/programmability/eval-intro).

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.

**RESP3:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.



