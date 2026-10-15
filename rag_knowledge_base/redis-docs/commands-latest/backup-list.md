# BACKUP LIST

```json metadata
{
  "schema_version": 2,
  "title": "BACKUP LIST",
  "description": "List the immutable backup file paths pinned so far.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "BACKUP LIST",
  "complexity": "O(1)",
  "group": "server",
  "command_flags": ["admin","stale"],
  "acl_categories": ["@admin","@slow","@dangerous"],
  "since": "8.10.0",
  "arity": 2,
  "tableOfContents": {"sections":[{"id":"examples","title":"Examples"},{"id":"details","title":"Details"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"see-also","title":"See also"},{"id":"related-topics","title":"Related topics"}]}

,
  "codeExamples": []
}
```

Returns the absolute paths of the immutable backup files pinned so far.

## Examples

While the backup is still in the `incrementing` state, only the BASE file is pinned:

```
127.0.0.1:6379> BACKUP LIST
1) "/var/lib/redis/backupdir/appendonly.aof.3.base.rdb"
```

After [`BACKUP SEAL`](https://redis.io/docs/latest/commands/backup-seal), the INCR file and the manifest are pinned as well:

```
127.0.0.1:6379> BACKUP LIST
1) "/var/lib/redis/backupdir/appendonly.aof.3.base.rdb"
2) "/var/lib/redis/backupdir/appendonly.aof.3.incr.aof"
3) "/var/lib/redis/backupdir/appendonly.aof.manifest"
```

## Details

`BACKUP LIST` reports the absolute paths of the files that have been pinned by hard links so far. This lets the data plane start uploading the BASE snapshot while Redis is still accumulating incremental writes, before the backup is sealed. After the backup is sealed, the list also includes the INCR file and the manifest.

For the full workflow, see [Redis persistence](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence#online-backups-with-the-backup-command-family).

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Array reply](../../develop/reference/protocol-spec#arrays): the absolute paths of the immutable files pinned so far.

**RESP3:**

[Array reply](../../develop/reference/protocol-spec#arrays): the absolute paths of the immutable files pinned so far.



## See also

[`BACKUP START`](https://redis.io/docs/latest/commands/backup-start) | [`BACKUP SEAL`](https://redis.io/docs/latest/commands/backup-seal) | [`BACKUP STATUS`](https://redis.io/docs/latest/commands/backup-status) | [`BACKUP ABORT`](https://redis.io/docs/latest/commands/backup-abort) | [`BACKUP CLEANUP`](https://redis.io/docs/latest/commands/backup-cleanup)

## Related topics

- [Redis persistence](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence)

