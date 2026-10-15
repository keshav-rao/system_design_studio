# Job scheduler object

```json metadata
{
  "schema_version": 2,
  "title": "Job scheduler object",
  "description": "An object for job scheduler settings",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[]}

,
  "codeExamples": []
}
```


An API object that represents the job scheduler settings in the cluster.

| Name | Type/Value | Description |
|------|------------|-------------|
| backup_job_settings | [backup_job_settings](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/job_scheduler/backup_job_settings) object | Backup job settings |
| <span class="break-all">bdb_usage_report_job_settings</span> | <span class="break-all">[bdb_usage_report_job_settings](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/job_scheduler/bdb_usage_report_job_settings)</span> object | Job settings for database usage reports |
| <span class="break-all">cert_rotation_job_settings</span> | <span class="break-all">[cert_rotation_job_settings](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/job_scheduler/cert_rotation_job_settings)</span> object | Job settings for internal certificate rotation |
| <span class="break-all">granular_metrics_job_settings</span> | <span class="break-all">[granular_metrics_job_settings](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/job_scheduler/granular_metrics_job_settings)</span> object | Job settings for granular metrics collection |
| <span class="break-all">log_rotation_job_settings</span> | <span class="break-all">[log_rotation_job_settings](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/job_scheduler/log_rotation_job_settings)</span> object | Log rotation job settings |
| <span class="break-all">node_checks_job_settings</span> | <span class="break-all">[node_checks_job_settings](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/job_scheduler/node_checks_job_settings)</span> object | Node checks job settings |
| <span class="break-all">redis_cleanup_job_settings</span> | <span class="break-all">[redis_cleanup_job_settings](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/job_scheduler/redis_cleanup_job_settings)</span> object | Redis cleanup job settings (deprecated as of Redis Software v6.4.2, replaced with persistence_cleanup_scan_interval) |
| rotate_ccs_job_settings | [rotate_ccs_job_settings](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/job_scheduler/rotate_ccs_job_settings) object | Rotate CCS job settings |

