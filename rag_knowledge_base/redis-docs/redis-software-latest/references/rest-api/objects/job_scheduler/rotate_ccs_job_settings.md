# Rotate CCS job settings object

```json metadata
{
  "schema_version": 2,
  "title": "Rotate CCS job settings object",
  "description": "Documents the rotate_ccs_job_settings object used with Redis Software REST API calls.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[]}

,
  "codeExamples": []
}
```


| Name | Type/Value | Description |
|------|------------|-------------|
| cron_expression | string | [CRON expression](https://en.wikipedia.org/wiki/Cron#CRON_expression) that defines the CCS rotation schedule |
| enabled | boolean (default: true) | Indicates whether this job is enabled |
| file_suffix | string (default:&nbsp;5min) | String added to the end of the rotated RDB files |
| rotate_max_num | integer, (range:&nbsp;1-100) (default:&nbsp;24) | The maximum number of saved RDB files |

