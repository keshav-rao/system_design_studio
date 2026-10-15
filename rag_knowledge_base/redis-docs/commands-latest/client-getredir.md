# CLIENT GETREDIR

```json metadata
{
  "schema_version": 2,
  "title": "CLIENT GETREDIR",
  "description": "Returns the client ID to which the connection's tracking notifications are redirected.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "CLIENT GETREDIR",
  "complexity": "O(1)",
  "group": "connection",
  "command_flags": ["noscript","loading","stale"],
  "acl_categories": ["@slow","@connection"],
  "since": "6.0.0",
  "arity": 2,
  "tableOfContents": {"sections":[{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

This command returns the client ID we are redirecting our
[tracking](https://redis.io/docs/latest/develop/clients/client-side-caching#tracking) notifications to. We set a client
to redirect to when using [`CLIENT TRACKING`](https://redis.io/docs/latest/commands/client-tracking) to enable tracking. However in
order to avoid forcing client libraries implementations to remember the
ID notifications are redirected to, this command exists in order to improve
introspection and allow clients to check later if redirection is active
and towards which client ID.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Integer reply](../../develop/reference/protocol-spec#integers): `0` when not redirecting notifications to any client.
* [Integer reply](../../develop/reference/protocol-spec#integers): `-1` if client tracking is not enabled.
* [Integer reply](../../develop/reference/protocol-spec#integers): the ID of the client to which notification are being redirected.

**RESP3:**

One of the following:
* [Integer reply](../../develop/reference/protocol-spec#integers): `0` when not redirecting notifications to any client.
* [Integer reply](../../develop/reference/protocol-spec#integers): `-1` if client tracking is not enabled.
* [Integer reply](../../develop/reference/protocol-spec#integers): the ID of the client to which notification are being redirected.



