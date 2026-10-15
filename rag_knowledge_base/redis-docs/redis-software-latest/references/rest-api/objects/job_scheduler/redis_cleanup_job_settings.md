# Redis cleanup job settings object

```json metadata
{
  "schema_version": 2,
  "title": "Redis cleanup job settings object",
  "description": "Documents the redis_cleanup_job_settings object used with Redis Software REST API calls.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[]}

,
  "codeExamples": []
}
```


Deprecated and replaced with `persistence_cleanup_scan_interval`.

| Name | Type/Value | Description |
|------|------------|-------------|
| cron_expression | string | [CRON expression](https://en.wikipedia.org/wiki/Cron#CRON_expression) that defines the Redis cleanup schedule |

