# HIMPORT DISCARD

```json metadata
{
  "schema_version": 2,
  "title": "HIMPORT DISCARD",
  "description": "Removes a single session-local fieldset by name.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"fieldset-name","name":"fieldset-name","type":"string"}],
  "syntax_fmt": "HIMPORT DISCARD fieldset-name",
  "complexity": "O(N) where N is the number of session-local fieldsets.",
  "group": "hash",
  "acl_categories": ["@hash","@slow"],
  "since": "8.10.0",
  "arity": 3,
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"details","title":"Details"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"see-also","title":"See also"}]}

,
  "codeExamples": []
}
```

Removes a single session-local fieldset, previously defined with [`HIMPORT PREPARE`](https://redis.io/docs/latest/commands/himport-prepare), from the current connection.

## Required arguments

<details open><summary><code>fieldset-name</code></summary>

The name of the fieldset to remove from the current connection.

</details>

## Examples


redis> HIMPORT PREPARE u name email age
OK
redis> HIMPORT DISCARD u
(integer) 1
redis> HIMPORT DISCARD u
(integer) 0


## Details

Discarding a fieldset only removes the fieldset itself; it does not affect any hashes already created from it with [`HIMPORT SET`](https://redis.io/docs/latest/commands/himport-set).

Use `HIMPORT DISCARD` to free up resources on the connection once a bulk-ingestion job that used a given fieldset has finished. If you don't discard it, the fieldset stays allocated on the connection until the connection closes or the client issues the [`RESET`](https://redis.io/docs/latest/commands/reset) command.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Integer reply](../../develop/reference/protocol-spec#integers): `1` if the fieldset was removed, or `0` if no fieldset with that name existed on the connection.

**RESP3:**

[Integer reply](../../develop/reference/protocol-spec#integers): `1` if the fieldset was removed, or `0` if no fieldset with that name existed on the connection.



## See also

[`HIMPORT PREPARE`](https://redis.io/docs/latest/commands/himport-prepare) | [`HIMPORT DISCARDALL`](https://redis.io/docs/latest/commands/himport-discardall)

