# BGSAVE

```json metadata
{
  "schema_version": 2,
  "title": "BGSAVE",
  "description": "Asynchronously saves the database(s) to disk.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"schedule","name":"schedule","optional":true,"since":"3.2.2","token":"SCHEDULE","type":"pure-token"}],
  "syntax_fmt": "BGSAVE [SCHEDULE]",
  "complexity": "O(1)",
  "group": "server",
  "command_flags": ["admin","noscript","no_async_loading"],
  "acl_categories": ["@admin","@slow","@dangerous"],
  "since": "1.0.0",
  "arity": -1,
  "tableOfContents": {"sections":[{"id":"optional-arguments","title":"Optional arguments"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Save the DB in background.

Normally the OK code is immediately returned.
Redis forks, the parent continues to serve the clients, the child saves the DB
on disk then exits.

An error is returned if there is already a background save running or if there
is another non-background-save process running, specifically an in-progress AOF
rewrite.

If `BGSAVE SCHEDULE` is used, the command will immediately return `OK` when an
AOF rewrite is in progress and schedule the background save to run at the next
opportunity.

A client may be able to check if the operation succeeded using the [`LASTSAVE`](https://redis.io/docs/latest/commands/lastsave)
command.

See the [persistence documentation](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence) for detailed information.

## Optional arguments

<details open><summary><code>SCHEDULE</code></summary>

Schedule the save to run after any in-progress `BGSAVE` finishes, instead of returning an error.

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Simple string reply](../../develop/reference/protocol-spec#simple-strings): `Background saving started`.
* [Simple string reply](../../develop/reference/protocol-spec#simple-strings): `Background saving scheduled`.

**RESP3:**

One of the following:
* [Simple string reply](../../develop/reference/protocol-spec#simple-strings): `Background saving started`.
* [Simple string reply](../../develop/reference/protocol-spec#simple-strings): `Background saving scheduled`.



