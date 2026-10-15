# BACKUP STATUS

```json metadata
{
  "schema_version": 2,
  "title": "BACKUP STATUS",
  "description": "Report the current backup state.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "BACKUP STATUS",
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

Reports the current backup state.

## Examples

```
127.0.0.1:6379> BACKUP STATUS
1) "state"
2) "incrementing"
3) "error"
4) ""
5) "start_time"
6) "1717921800"
7) "end_time"
8) "0"
```

## Details

`BACKUP STATUS` reports the current state of the backup state machine along with timing and error information. The reply contains the following fields:

| Field | Description |
|:------|:------------|
| `state` | The current backup state (see below). |
| `error` | The error message if the backup failed; an empty string otherwise. |
| `start_time` | The Unix time, in seconds, when the current backup started; `0` if no backup has started. |
| `end_time` | The Unix time, in seconds, when the current backup was sealed; `0` if it has not been sealed. |

The `state` field is one of the following:

| State | Description |
|:------|:------------|
| `idle` | No backup is in progress. |
| `pending` | A backup was requested but is waiting for an append-only file rewrite (AOFRW) to become available. |
| `snapshotting` | Redis is producing the BASE snapshot. |
| `incrementing` | The BASE snapshot is complete and pinned; Redis is accumulating incremental writes and waiting to be sealed. |
| `sealed` | The backup is frozen; the file set is complete and immutable, awaiting data-plane consumption and cleanup. |
| `failed` | The backup failed or was aborted. A new backup can be started. |

For lightweight monitoring, `INFO persistence` also exposes a `backup_in_progress` boolean. Full backup state, error, and timestamps are available only through `BACKUP STATUS`.

For the full workflow, see [Redis persistence](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence#online-backups-with-the-backup-command-family).

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Array reply](../../develop/reference/protocol-spec#arrays): a flat array of field-value pairs describing the current backup state.

**RESP3:**

[Map reply](../../develop/reference/protocol-spec#maps): a map of fields to values describing the current backup state.



## See also

[`BACKUP START`](https://redis.io/docs/latest/commands/backup-start) | [`BACKUP SEAL`](https://redis.io/docs/latest/commands/backup-seal) | [`BACKUP LIST`](https://redis.io/docs/latest/commands/backup-list) | [`BACKUP ABORT`](https://redis.io/docs/latest/commands/backup-abort) | [`BACKUP CLEANUP`](https://redis.io/docs/latest/commands/backup-cleanup)

## Related topics

- [Redis persistence](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence)

