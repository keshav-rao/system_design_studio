# EXEC

```json metadata
{
  "schema_version": 2,
  "title": "EXEC",
  "description": "Executes all commands in a transaction.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "EXEC",
  "complexity": "Depends on commands in the transaction",
  "group": "transactions",
  "command_flags": ["noscript","loading","stale","skip_slowlog"],
  "acl_categories": ["@slow","@transaction"],
  "since": "1.2.0",
  "arity": 1,
  "tableOfContents": {"sections":[{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

> [!NOTE]
> This command's behavior varies in clustered Redis environments. See the [multi-key operations](https://redis.io/docs/latest/develop/using-commands/multi-key-operations) page for more information.


Executes all previously queued commands in a [transaction](https://redis.io/docs/latest/develop/using-commands/transactions) and restores the
connection state to normal.

When using [`WATCH`](https://redis.io/docs/latest/commands/watch), `EXEC` will execute commands only if the watched keys were
not modified, allowing for a [check-and-set mechanism](https://redis.io/docs/latest/develop/using-commands/transactions#cas).

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Array reply](../../develop/reference/protocol-spec#arrays): each element being the reply to each of the commands in the atomic transaction.
* [Nil reply](../../develop/reference/protocol-spec#bulk-strings): the transaction was aborted because a `WATCH`ed key was touched.

**RESP3:**

One of the following:
* [Array reply](../../develop/reference/protocol-spec#arrays): each element being the reply to each of the commands in the atomic transaction.
* [Null reply](../../develop/reference/protocol-spec#nulls): the transaction was aborted because a `WATCH`ed key was touched.



