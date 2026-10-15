# Database modules requests

```json metadata
{
  "schema_version": 2,
  "title": "Database modules requests",
  "description": "Redis module requests",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"id":"configure-module","title":"Configure module"},{"id":"upgrade-module","title":"Upgrade module"}]}

,
  "codeExamples": []
}
```


## Configure module
| Method | Path | Description |
|--------|------|-------------|
| [POST](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/bdbs/modules/config#post-bdb-modules-config) | `/v1/bdbs/{uid}/modules/config` | Configure module |

## Upgrade module
| Method | Path | Description |
|--------|------|-------------|
| [POST](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/bdbs/modules/upgrade#post-bdb-modules-upgrade) | `/v1/bdbs/{uid}/modules/upgrade` | Upgrade module |
