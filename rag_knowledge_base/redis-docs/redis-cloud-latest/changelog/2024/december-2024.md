# Redis Cloud changelog (December 2024)

```json metadata
{
  "schema_version": 2,
  "title": "Redis Cloud changelog (December 2024)",
  "description": "New features, enhancements, and other changes added to Redis Cloud during December 2024.",
  "categories": ["docs","operate","rc"],
  "tableOfContents": {"sections":[{"children":[{"id":"logs-viewer-role","title":"Logs Viewer role"},{"id":"redis-flex-preview-on-redis-cloud-essentials","title":"Redis Flex preview on Redis Cloud Essentials"}],"id":"new-features","title":"New features"}]}

,
  "codeExamples": []
}
```


## New features

### Logs Viewer role

You can now add a user with the **Logs Viewer** role in the [Access Management](https://redis.io/docs/latest/operate/rc/security/access-control/access-management) screen. Logs Viewers can only use the [Redis Cloud API](https://redis.io/docs/latest/operate/rc/api) [`GET logs/`](https://api.redislabs.com/v1/swagger-ui/index.html#/Account/getAccountSystemLogs) endpoint. 

See [Team Management roles](https://redis.io/docs/latest/operate/rc/security/access-control/access-management#team-management-roles) to see an overview of user roles and their permissions.

### Redis Flex preview on Redis Cloud Essentials

Redis Flex is now available in Preview on Redis Cloud Essentials.

Redis Flex databases have a tiered solid state drive (SSD) and RAM architecture. Using SSDs instead of RAM significantly reduces infrastructure costs, which means developers can build applications that require large datasets using the same Redis API.

See [Create a Redis Flex database](https://redis.io/docs/latest/operate/rc/databases/create-database/create-flex-database) for more info.
