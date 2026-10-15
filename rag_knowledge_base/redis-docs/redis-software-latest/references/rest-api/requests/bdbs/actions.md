# Database actions requests

```json metadata
{
  "schema_version": 2,
  "title": "Database actions requests",
  "description": "Database action requests",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"id":"backup","title":"Backup"},{"id":"export","title":"Export"},{"id":"import","title":"Import"},{"id":"optimize-shards-placement","title":"Optimize shards placement"},{"id":"rebalance","title":"Rebalance"},{"id":"recover","title":"Recover"},{"id":"resume-traffic","title":"Resume traffic"},{"id":"stop-traffic","title":"Stop traffic"}]}

,
  "codeExamples": []
}
```


## Backup

| Method | Path | Description |
|--------|------|-------------|
| [PUT](https://redis.io/docs/latest/./backup_reset_status#put-bdbs-actions-backup-reset-status) | `/v1/bdbs/{uid}/actions/backup_reset_status` | Reset database backup status |

## Export

| Method | Path | Description |
|--------|------|-------------|
| [PUT](https://redis.io/docs/latest/./export_reset_status#put-bdbs-actions-export-reset-status) | `/v1/bdbs/{uid}/actions/export_reset_status` | Reset database export status |
| [POST](https://redis.io/docs/latest/./export#post-bdbs-actions-export) | `/v1/bdbs/{uid}/actions/export` | Initiate database export |

## Import

| Method | Path | Description |
|--------|------|-------------|
| [PUT](https://redis.io/docs/latest/./import_reset_status#put-bdbs-actions-import-reset-status) | `/v1/bdbs/{uid}/actions/import_reset_status` | Reset database import status |
| [POST](https://redis.io/docs/latest/./import#post-bdbs-actions-import) | `/v1/bdbs/{uid}/actions/import` | Initiate manual dataset import |

## Optimize shards placement

| Method | Path | Description |
|--------|------|-------------|
| [GET](https://redis.io/docs/latest/./optimize_shards_placement#get-bdbs-actions-optimize-shards-placement) | `/v1/bdbs/{uid}/actions/optimize_shards_placement` | Get optimized shards placement for a database  |

## Rebalance

| Method | Path | Description |
|--------|------|-------------|
| [PUT](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/bdbs/actions/rebalance#put-bdbs-actions-rebalance) | `/v1/bdbs/{uid}/actions/rebalance` | Rebalance database shards |

## Recover

| Method | Path | Description |
|--------|------|-------------|
| [GET](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/bdbs/actions/recover#get-bdbs-actions-recover) | `/v1/bdbs/{uid}/actions/recover` | Get database recovery plan  |
| [POST](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/bdbs/actions/recover#post-bdbs-actions-recover) | `/v1/bdbs/{uid}/actions/recover` | Recover database  |

## Resume traffic
| Method | Path | Description |
|--------|------|-------------|
| [POST](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/bdbs/actions/resume_traffic#post-bdbs-actions-resume-traffic) | `/v1/bdbs/{uid}/actions/resume_traffic` | Resume database traffic |

## Stop traffic
| Method | Path | Description |
|--------|------|-------------|
| [POST](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/bdbs/actions/stop_traffic#post-bdbs-actions-stop-traffic) | `/v1/bdbs/{uid}/actions/stop_traffic` | Stop database traffic |

