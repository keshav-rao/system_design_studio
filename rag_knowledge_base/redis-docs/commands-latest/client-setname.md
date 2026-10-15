# CLIENT SETNAME

```json metadata
{
  "schema_version": 2,
  "title": "CLIENT SETNAME",
  "description": "Sets the connection name.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"connection-name","name":"connection-name","type":"string"}],
  "syntax_fmt": "CLIENT SETNAME connection-name",
  "complexity": "O(1)",
  "group": "connection",
  "command_flags": ["noscript","loading","stale"],
  "acl_categories": ["@slow","@connection"],
  "since": "2.6.9",
  "arity": 3,
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"details","title":"Details"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

The `CLIENT SETNAME` command assigns a name to the current connection.


## Required arguments

<details open><summary><code>connection-name</code></summary>

The name to assign to the current connection.

</details>

## Details
The assigned name is displayed in the output of [`CLIENT LIST`](https://redis.io/docs/latest/commands/client-list) so that it is possible to identify the client that performed a given connection.

For instance when Redis is used in order to implement a queue, producers and consumers of messages may want to set the name of the connection according to their role.

There is no limit to the length of the name that can be assigned if not the usual limits of the Redis string type (512 MB). However it is not possible to use spaces in the connection name as this would violate the format of the [`CLIENT LIST`](https://redis.io/docs/latest/commands/client-list) reply.

It is possible to entirely remove the connection name setting it to the empty string, that is not a valid connection name since it serves to this specific purpose.

The connection name can be inspected using [`CLIENT GETNAME`](https://redis.io/docs/latest/commands/client-getname).

Every new connection starts without an assigned name.

> [!TIP]
> Setting names to connections is a good way to debug connection leaks due to bugs in the application using Redis.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK` if the connection name was successfully set.

**RESP3:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK` if the connection name was successfully set.



