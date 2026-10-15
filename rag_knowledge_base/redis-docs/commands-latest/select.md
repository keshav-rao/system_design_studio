# SELECT

```json metadata
{
  "schema_version": 2,
  "title": "SELECT",
  "description": "Changes the selected database.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"index","name":"index","type":"integer"}],
  "syntax_fmt": "SELECT index",
  "complexity": "O(1)",
  "group": "connection",
  "command_flags": ["loading","stale","fast"],
  "acl_categories": ["@fast","@connection"],
  "since": "1.0.0",
  "arity": 2,
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Select the logical Redis database having the specified zero-based numeric index.
New connections always use database zero.

Selectable Redis databases are a form of namespacing: all databases are still persisted in the same RDB or AOF file. However, different databases can have keys with the same name, and commands like [`FLUSHDB`](https://redis.io/docs/latest/commands/flushdb), [`SWAPDB`](https://redis.io/docs/latest/commands/swapdb) or [`RANDOMKEY`](https://redis.io/docs/latest/commands/randomkey) work on specific databases.

Use Redis databases to separate keys within the same application when needed. Don’t use them to run multiple unrelated applications in a single Redis instance.

When using Redis Cluster, the `SELECT` command cannot be used, since Redis Cluster only supports database zero. Having multiple databases would be useless and an unnecessary source of complexity. Commands operating atomically on a single database would not be possible with the Redis Cluster's design and goals.

Since the currently selected database is a property of the connection, clients should track the currently selected database and re-select it on reconnection. While there is no command in order to query the selected database in the current connection, the [`CLIENT LIST`](https://redis.io/docs/latest/commands/client-list) output shows, for each client, the currently selected database.

## Required arguments

<details open><summary><code>index</code></summary>

The zero-based index of the database to switch to.

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | Redis Software does not support shared databases due to potential negative performance impacts and blocks any related commands. The `SELECT` command is supported solely for compatibility with Redis Open Source but does not perform any operations in Redis Software. |

## Return information

**RESP2:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.

**RESP3:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.



