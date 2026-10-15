# BACKUP START

```json metadata
{
  "schema_version": 2,
  "title": "BACKUP START",
  "description": "Start a new backup into the configured 'backupdirname'.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "BACKUP START",
  "complexity": "O(1)",
  "group": "server",
  "command_flags": ["admin","noscript"],
  "acl_categories": ["@admin","@slow","@dangerous"],
  "since": "8.10.0",
  "arity": 2,
  "tableOfContents": {"sections":[{"id":"examples","title":"Examples"},{"id":"details","title":"Details"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"see-also","title":"See also"},{"id":"related-topics","title":"Related topics"}]}

,
  "codeExamples": []
}
```

Starts a new backup, opening a backup window and producing a fresh BASE snapshot in the directory named by the `backupdirname` configuration setting.

## Examples

```
127.0.0.1:6379> BACKUP START
OK
```

## Details

`BACKUP START` moves the backup state machine from `idle` to `snapshotting` and begins producing a fresh BASE snapshot through an append-only file rewrite (AOFRW). It works whether or not AOF persistence is enabled:

* If AOF is enabled, Redis reuses the existing [multi-part AOF](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence#append-only-file) directly.
* If AOF is disabled, Redis temporarily starts the AOF machinery without changing the configured `appendonly` value.
* If an AOFRW is already active or scheduled and can be reused, the backup attaches to it.
* If another child process is active, the backup enters the `pending` state and starts when an AOFRW can run.

After the snapshot rewrite completes, Redis hard-links the BASE file into the backup directory and enters the `incrementing` state, where it continues to accumulate incremental writes until you call [`BACKUP SEAL`](https://redis.io/docs/latest/commands/backup-seal).

The backup directory (named by `backupdirname` and resolved under the Redis working directory `dir`) must be empty when you call `BACKUP START`. Only one backup can be in progress at a time.

For the full workflow and restore procedure, see [Redis persistence](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence#online-backups-with-the-backup-command-family).

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.

**RESP3:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.



## See also

[`BACKUP SEAL`](https://redis.io/docs/latest/commands/backup-seal) | [`BACKUP STATUS`](https://redis.io/docs/latest/commands/backup-status) | [`BACKUP LIST`](https://redis.io/docs/latest/commands/backup-list) | [`BACKUP ABORT`](https://redis.io/docs/latest/commands/backup-abort) | [`BACKUP CLEANUP`](https://redis.io/docs/latest/commands/backup-cleanup)

## Related topics

- [Redis persistence](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence)

