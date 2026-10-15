# Redis Cloud changelog (September 2023)

```json metadata
{
  "schema_version": 2,
  "title": "Redis Cloud changelog (September 2023)",
  "description": "New features, enhancements, and other changes added to Redis Cloud during September 2023.",
  "categories": ["docs","operate","rc"],
  "tableOfContents": {"sections":[{"children":[{"id":"resp-protocol-selection","title":"RESP protocol selection"},{"id":"opt-in-to-redis-72","title":"Opt-in to Redis 7.2"}],"id":"new-features","title":"New features"}]}

,
  "codeExamples": []
}
```


## New features

### RESP protocol selection

For all databases using Redis 7.2, you can now choose between the RESP2 and RESP3 protocols when you [create a database](https://redis.io/docs/latest/operate/rc/databases/create-database). For more information about the different RESP versions, see the [Redis serialization protocol specification](https://redis.io/docs/latest/develop/reference/protocol-spec#resp-versions).

### Opt-in to Redis 7.2

Select **Opt-in to 7.2** to request to upgrade your subscription and databases to Redis 7.2 (*Redis 6.2 and earlier only*).

![Opt-in to 7.2 button.](https://redis.io/docs/latest/images/rc/button-opt-in-to-72.png)

The upgrade will start one week from your request, according to [maintenance windows](https://redis.io/docs/latest/operate/rc/subscriptions/maintenance/set-maintenance-windows). 

Redis 7.2 introduces several changes to existing Redis commands; see the list of [breaking changes](https://redis.io/docs/latest/operate/rc/changelog/2023/june-2023#redis-72-breaking-changes) for more details.


