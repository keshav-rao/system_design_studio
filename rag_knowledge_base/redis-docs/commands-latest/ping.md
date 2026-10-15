# PING

```json metadata
{
  "schema_version": 2,
  "title": "PING",
  "description": "Returns the server's liveliness response.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"message","name":"message","optional":true,"type":"string"}],
  "syntax_fmt": "PING [message]",
  "complexity": "O(1)",
  "group": "connection",
  "command_flags": ["fast"],
  "acl_categories": ["@fast","@connection"],
  "since": "1.0.0",
  "arity": -1,
  "tableOfContents": {"sections":[{"id":"optional-arguments","title":"Optional arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```


This command returns the bulk string `PONG` if no argument is provided, otherwise it returns a copy of the
provided `message` as a bulk string.

This command is useful for:
1. Testing whether a connection is still alive.
1. Verifying the server's ability to serve data - an error is returned when this isn't the case (for example, during load from persistence data or accessing a stale replica).
1. Measuring latency.

If the client is subscribed to a channel or a pattern, it will instead return a
multi-bulk string with `PONG` in the first position and an empty bulk string in the second
position, unless an argument is provided, in which case it returns a copy
of the argument.

## Optional arguments

<details open><summary><code>message</code></summary>

A message to return instead of `PONG`.

</details>

## Examples


redis> PING
PONG
redis> PING "hello world"
"hello world"


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

Any of the following:
* [Simple string reply](../../develop/reference/protocol-spec#simple-strings): `PONG` when no argument is provided.
* [Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): the provided argument.

**RESP3:**

Any of the following:
* [Simple string reply](../../develop/reference/protocol-spec#simple-strings): `PONG` when no argument is provided.
* [Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): the provided argument.



