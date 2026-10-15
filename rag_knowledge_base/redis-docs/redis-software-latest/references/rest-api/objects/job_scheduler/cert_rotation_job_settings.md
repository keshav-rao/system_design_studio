# Certificate rotation job settings object

```json metadata
{
  "schema_version": 2,
  "title": "Certificate rotation job settings object",
  "description": "Documents the cert_rotation_job_settings object used with Redis Software REST API calls.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[]}

,
  "codeExamples": []
}
```


| Name | Type/Value | Description |
|------|------------|-------------|
| cron_expression              | string | [CRON expression](https://en.wikipedia.org/wiki/Cron#CRON_expression) that defines the certificate rotation schedule |
| enabled | boolean (default: true) | Indicates whether this job is enabled |
| expiry_days_before_rotation  | integer, (range:&nbsp;1-90) (default:&nbsp;60) | Number of days before a certificate expires before rotation |

