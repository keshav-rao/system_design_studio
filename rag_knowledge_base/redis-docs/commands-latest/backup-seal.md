# BACKUP SEAL

```json metadata
{
  "schema_version": 2,
  "title": "BACKUP SEAL",
  "description": "Freeze the current backup (BASE + INCR + manifest).",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "BACKUP SEAL",
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

Freezes the current backup, producing the final immutable file set: the BASE snapshot, the incremental append-only file (INCR), and a standalone manifest.

## Examples

```
127.0.0.1:6379> BACKUP SEAL
OK
```

## Details

`BACKUP SEAL` moves the backup state machine from `incrementing` to `sealed`. Restore loads `BASE + INCR`, so the restored dataset reflects the state at the seal boundary, not merely the earlier BASE snapshot. Sealing performs the following steps:

* Flushes and fsyncs the current INCR file.
* Hard-links the INCR file into the backup directory.
* Writes a standalone manifest that references only this backup's `{BASE, INCR}` file set.
* Rotates the live AOF when AOF persistence is enabled.
* Stops and removes the temporary AOF state when the backup created it for an `appendonly no` instance.

After sealing, the file set is complete and immutable. The data plane can copy the files reported by [`BACKUP LIST`](https://redis.io/docs/latest/commands/backup-list), then call [`BACKUP CLEANUP`](https://redis.io/docs/latest/commands/backup-cleanup) to release them.

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

[`BACKUP START`](https://redis.io/docs/latest/commands/backup-start) | [`BACKUP STATUS`](https://redis.io/docs/latest/commands/backup-status) | [`BACKUP LIST`](https://redis.io/docs/latest/commands/backup-list) | [`BACKUP ABORT`](https://redis.io/docs/latest/commands/backup-abort) | [`BACKUP CLEANUP`](https://redis.io/docs/latest/commands/backup-cleanup)

## Related topics

- [Redis persistence](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence)

