# SAVE

```json metadata
{
  "schema_version": 2,
  "title": "SAVE",
  "description": "Synchronously saves the database(s) to disk.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "SAVE",
  "complexity": "O(N) where N is the total number of keys in all databases",
  "group": "server",
  "command_flags": ["admin","noscript","no_async_loading","no_multi"],
  "acl_categories": ["@admin","@slow","@dangerous"],
  "since": "1.0.0",
  "arity": 1,
  "tableOfContents": {"sections":[{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

The `SAVE` commands performs a **synchronous** save of the dataset producing a
_point in time_ snapshot of all the data inside the Redis instance, in the form
of an RDB file.

You almost never want to call `SAVE` in production environments where it will
block all the other clients.
Instead usually [`BGSAVE`](https://redis.io/docs/latest/commands/bgsave) is used.
However in case of issues preventing Redis to create the background saving child
(for instance errors in the fork(2) system call), the `SAVE` command can be a
good last resort to perform the dump of the latest dataset.

See the [persistence documentation](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence) for detailed information.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.

**RESP3:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.



