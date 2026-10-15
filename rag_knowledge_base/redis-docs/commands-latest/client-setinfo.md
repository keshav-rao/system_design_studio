# CLIENT SETINFO

```json metadata
{
  "schema_version": 2,
  "title": "CLIENT SETINFO",
  "description": "Sets information specific to the client or connection.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"arguments":[{"display_text":"libname","name":"libname","token":"LIB-NAME","type":"string"},{"display_text":"libver","name":"libver","token":"LIB-VER","type":"string"}],"name":"attr","type":"oneof"}],
  "syntax_fmt": "CLIENT SETINFO \u003cLIB-NAME libname | LIB-VER libver\u003e",
  "complexity": "O(1)",
  "group": "connection",
  "command_flags": ["noscript","loading","stale"],
  "acl_categories": ["@slow","@connection"],
  "since": "7.2.0",
  "arity": 4,
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"details","title":"Details"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

The `CLIENT SETINFO` command assigns various info attributes to the current connection which are displayed in the output of [`CLIENT LIST`](https://redis.io/docs/latest/commands/client-list) and [`CLIENT INFO`](https://redis.io/docs/latest/commands/client-info).

Client libraries are expected to pipeline this command after authentication on all connections
and ignore failures since they could be connected to an older version that doesn't support them.


## Required arguments

Provide one of the following.

<details open><summary><code>LIB-NAME libname</code></summary>

Set the library name for the current connection.

</details>

<details open><summary><code>LIB-VER libver</code></summary>

Set the library version for the current connection.

</details>

## Details

There is no limit to the length of these attributes. However it is not possible to use spaces, newlines, or other non-printable characters that would violate the format of the [`CLIENT LIST`](https://redis.io/docs/latest/commands/client-list) reply.

[Official client libraries](https://redis.io/docs/latest/develop/connect/clients/) allow extending `lib-name` with a custom suffix to expose additional information about the client. 
For example, high-level libraries like [redis-om-spring](https://github.com/redis/redis-om-spring) can report their version. 
The resulting `lib-name` would be `jedis(redis-om-spring_v1.0.0)`. 
Brace characters are used to delimit the custom suffix and should be avoided in the suffix itself.
We recommend using the following format for the custom suffixes for third-party libraries `(?<custom-name>[ -~]+)[ -~]v(?<custom-version>[\d\.]+)` and use `;` to delimit multiple suffixes.

Note that these attributes are not cleared by the [`RESET`](https://redis.io/docs/latest/commands/reset) command.
## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK` if the attribute name was successfully set.

**RESP3:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK` if the attribute name was successfully set.



