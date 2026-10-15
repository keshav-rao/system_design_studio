# CLIENT CACHING

```json metadata
{
  "schema_version": 2,
  "title": "CLIENT CACHING",
  "description": "Instructs the server whether to track the keys in the next request.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"arguments":[{"display_text":"yes","name":"yes","token":"YES","type":"pure-token"},{"display_text":"no","name":"no","token":"NO","type":"pure-token"}],"name":"mode","type":"oneof"}],
  "syntax_fmt": "CLIENT CACHING \u003cYES | NO\u003e",
  "complexity": "O(1)",
  "group": "connection",
  "command_flags": ["noscript","loading","stale"],
  "acl_categories": ["@slow","@connection"],
  "since": "6.0.0",
  "arity": 3,
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

This command controls the tracking of the keys in the next command executed
by the connection, when tracking is enabled in `OPTIN` or `OPTOUT` mode.
Please check the
[client side caching documentation](https://redis.io/docs/latest/develop/clients/client-side-caching) for
background information.

When tracking is enabled in Redis, using the [`CLIENT TRACKING`](https://redis.io/docs/latest/commands/client-tracking) command, it is
possible to specify the `OPTIN` or `OPTOUT` options, so that keys
in read only commands are not automatically remembered by the server to
be invalidated later. When we are in `OPTIN` mode, we can enable the
tracking of the keys in the next command by calling `CLIENT CACHING YES`
immediately before it. Similarly when we are in `OPTOUT` mode, and keys
are normally tracked, we can avoid the keys in the next command to be
tracked using `CLIENT CACHING NO`.

Basically the command sets a state in the connection, that is valid only
for the next command execution, that will modify the behavior of client
tracking.

## Required arguments

<details open><summary><code>YES | NO</code></summary>

Whether to cache keys for the next command (`YES`) or not (`NO`) when tracking is in `OPTIN`/`OPTOUT` mode.

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK` or an error if the argument is not "yes" or "no".

**RESP3:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK` or an error if the argument is not "yes" or "no".



