# DBSIZE

```json metadata
{
  "schema_version": 2,
  "title": "DBSIZE",
  "description": "Returns the number of keys in the database.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "DBSIZE",
  "complexity": "O(1)",
  "group": "server",
  "command_flags": ["readonly","fast"],
  "acl_categories": ["@keyspace","@read","@fast"],
  "since": "1.0.0",
  "arity": 1,
  "tableOfContents": {"sections":[{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

> [!NOTE]
> This command's behavior varies in clustered Redis environments. See the [multi-key operations](https://redis.io/docs/latest/develop/using-commands/multi-key-operations) page for more information.


Return the number of keys in the currently-selected database.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Integer reply](../../develop/reference/protocol-spec#integers): the number of keys in the currently-selected database.

**RESP3:**

[Integer reply](../../develop/reference/protocol-spec#integers): the number of keys in the currently-selected database.



