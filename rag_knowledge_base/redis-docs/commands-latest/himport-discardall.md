# HIMPORT DISCARDALL

```json metadata
{
  "schema_version": 2,
  "title": "HIMPORT DISCARDALL",
  "description": "Removes all session-local fieldsets for the connection.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "HIMPORT DISCARDALL",
  "complexity": "O(N) where N is the number of session-local fieldsets.",
  "group": "hash",
  "acl_categories": ["@hash","@slow"],
  "since": "8.10.0",
  "arity": 2,
  "tableOfContents": {"sections":[{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"see-also","title":"See also"}]}

,
  "codeExamples": []
}
```

Removes every fieldset held by the current connection, discarding all definitions previously created with [`HIMPORT PREPARE`](https://redis.io/docs/latest/commands/himport-prepare).

## Examples


redis> HIMPORT PREPARE u name email age
OK
redis> HIMPORT PREPARE o id total
OK
redis> HIMPORT DISCARDALL
(integer) 2


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Integer reply](../../develop/reference/protocol-spec#integers): the number of fieldsets removed.

**RESP3:**

[Integer reply](../../develop/reference/protocol-spec#integers): the number of fieldsets removed.



## See also

[`HIMPORT PREPARE`](https://redis.io/docs/latest/commands/himport-prepare) | [`HIMPORT DISCARD`](https://redis.io/docs/latest/commands/himport-discard)

