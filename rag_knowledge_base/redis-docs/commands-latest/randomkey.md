# RANDOMKEY

```json metadata
{
  "schema_version": 2,
  "title": "RANDOMKEY",
  "description": "Returns a random key name from the database.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "RANDOMKEY",
  "complexity": "O(1)",
  "group": "generic",
  "command_flags": ["readonly"],
  "acl_categories": ["@keyspace","@read","@slow"],
  "since": "1.0.0",
  "arity": 1,
  "tableOfContents": {"sections":[{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Return a random key from the currently selected database.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Nil reply](../../develop/reference/protocol-spec#bulk-strings): when the database is empty.
* [Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): a random key in database.

**RESP3:**

One of the following:
* [Null reply](../../develop/reference/protocol-spec#nulls): when the database is empty.
* [Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): a random key in the database.



