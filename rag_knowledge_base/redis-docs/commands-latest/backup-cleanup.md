# BACKUP CLEANUP

```json metadata
{
  "schema_version": 2,
  "title": "BACKUP CLEANUP",
  "description": "Remove sealed backup files and return to idle.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "BACKUP CLEANUP",
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

Removes sealed backup files and returns the backup state machine to idle.

## Examples

```
127.0.0.1:6379> BACKUP CLEANUP
OK
```

## Details

`BACKUP CLEANUP` removes the sealed (or failed) backup artifacts and releases the files that were pinned by hard links, moving the backup state machine from `sealed` back to `idle`. Call it after the data plane has finished copying the files reported by [`BACKUP LIST`](https://redis.io/docs/latest/commands/backup-list).

By default a sealed backup is kept until you clean it up explicitly. If the `backup-sealed-ttl` configuration setting is non-zero, Redis automatically cleans up a sealed backup after the configured number of seconds; a value of `0` disables automatic cleanup.

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

[`BACKUP START`](https://redis.io/docs/latest/commands/backup-start) | [`BACKUP SEAL`](https://redis.io/docs/latest/commands/backup-seal) | [`BACKUP STATUS`](https://redis.io/docs/latest/commands/backup-status) | [`BACKUP LIST`](https://redis.io/docs/latest/commands/backup-list) | [`BACKUP ABORT`](https://redis.io/docs/latest/commands/backup-abort)

## Related topics

- [Redis persistence](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence)

