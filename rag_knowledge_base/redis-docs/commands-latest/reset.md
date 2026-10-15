# RESET

```json metadata
{
  "schema_version": 2,
  "title": "RESET",
  "description": "Resets the connection.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "RESET",
  "complexity": "O(1)",
  "group": "connection",
  "command_flags": ["noscript","loading","stale","fast","no_auth","allow_busy"],
  "acl_categories": ["@fast","@connection"],
  "since": "6.2.0",
  "arity": 1,
  "tableOfContents": {"sections":[{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

This command performs a full reset of the connection's server-side context, 
mimicking the effect of disconnecting and reconnecting again.

When the command is called from a regular client connection, it does the
following:

* Discards the current [`MULTI`](https://redis.io/docs/latest/commands/multi) transaction block, if one exists.
* Unwatches all keys [`WATCH`](https://redis.io/docs/latest/commands/watch)ed by the connection.
* Disables [`CLIENT TRACKING`](https://redis.io/docs/latest/commands/client-tracking), if in use.
* Sets the connection to [`READWRITE`](https://redis.io/docs/latest/commands/readwrite) mode.
* Cancels the connection's [`ASKING`](https://redis.io/docs/latest/commands/asking) mode, if previously set.
* Sets [`CLIENT REPLY`](https://redis.io/docs/latest/commands/client-reply) to `ON`.
* Sets the protocol version to RESP2.
* [`SELECT`](https://redis.io/docs/latest/commands/select)s database 0.
* Exits [`MONITOR`](https://redis.io/docs/latest/commands/monitor) mode, when applicable.
* Aborts Pub/Sub's subscription state ([`SUBSCRIBE`](https://redis.io/docs/latest/commands/subscribe) and [`PSUBSCRIBE`](https://redis.io/docs/latest/commands/psubscribe)), when
  appropriate.
* Deauthenticates the connection, requiring a call [`AUTH`](https://redis.io/docs/latest/commands/auth) to reauthenticate when
  authentication is enabled.
* Turns off `NO-EVICT` mode.
* Turns off `NO-TOUCH` mode.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `RESET`.

**RESP3:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `RESET`.



