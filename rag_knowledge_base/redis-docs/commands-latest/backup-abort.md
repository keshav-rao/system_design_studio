# BACKUP ABORT

```json metadata
{
  "schema_version": 2,
  "title": "BACKUP ABORT",
  "description": "Cancel a backup that has not been sealed yet.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "BACKUP ABORT",
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

Cancels a backup that has not been sealed yet.

## Examples

```
127.0.0.1:6379> BACKUP ABORT
OK
```

## Details

`BACKUP ABORT` cancels an in-progress backup and moves the backup state machine to `failed`. It is valid from the `pending`, `snapshotting`, and `incrementing` states. After the backup has been sealed, use [`BACKUP CLEANUP`](https://redis.io/docs/latest/commands/backup-cleanup) instead.

After aborting, you can start a new backup with [`BACKUP START`](https://redis.io/docs/latest/commands/backup-start).

For the full workflow, see [Redis persistence](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence#online-backups-with-the-backup-command-family).

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

[`BACKUP START`](https://redis.io/docs/latest/commands/backup-start) | [`BACKUP SEAL`](https://redis.io/docs/latest/commands/backup-seal) | [`BACKUP STATUS`](https://redis.io/docs/latest/commands/backup-status) | [`BACKUP LIST`](https://redis.io/docs/latest/commands/backup-list) | [`BACKUP CLEANUP`](https://redis.io/docs/latest/commands/backup-cleanup)

## Related topics

- [Redis persistence](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence)

