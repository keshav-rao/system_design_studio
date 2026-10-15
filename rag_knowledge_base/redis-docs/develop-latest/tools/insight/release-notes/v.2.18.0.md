# RedisInsight v2.18.0, January 2023

```json metadata
{
  "schema_version": 2,
  "title": "RedisInsight v2.18.0, January 2023",
  "description": "RedisInsight v2.18.0",
  "categories": null,
  "tableOfContents": {"sections":[{"children":[{"id":"highlights","title":"Highlights"},{"id":"details","title":"Details"}],"id":"2180-january-2023","title":"2.18.0 (January 2023)"}]}

,
  "codeExamples": []
}
```

## 2.18.0 (January 2023)
This is the General Availability (GA) release of RedisInsight 2.18.

### Highlights
- Support for SSH tunnel to connect to your Redis database
- Ability to switch between database indexes while connected to your database
- Recommendations on how to optimize the usage of your database

### Details
**Features and improvements**
- [#1567](https://github.com/RedisInsight/RedisInsight/pull/1567), [#1576](https://github.com/RedisInsight/RedisInsight/pull/1576), [#1577](https://github.com/RedisInsight/RedisInsight/pull/1577) Connect to your Redis database via SSH tunnel using a password or private key in PEM format.
- [#1540](https://github.com/RedisInsight/RedisInsight/pull/1540), [#1608](https://github.com/RedisInsight/RedisInsight/pull/1608) Switch between database indexes while connected to your database in Browser, Workbench, and Database Analysis.
- [#1457](https://github.com/RedisInsight/RedisInsight/pull/1457), [#1465](https://github.com/RedisInsight/RedisInsight/pull/1465), [#1590](https://github.com/RedisInsight/RedisInsight/pull/1590) Run Database Analysis to generate recommendations on how to save memory and optimize the usage of your database. These recommendations are based on industry standards and Redis best practices. Upvote or downvote recommendations in terms of their usefulness. 
- [#1598](https://github.com/RedisInsight/RedisInsight/pull/1598) Check and highlight the [JSON](https://redis.io/docs/stack/json/) syntax using new [Monaco Editor](https://microsoft.github.io/monaco-editor/).
- [#1583](https://github.com/RedisInsight/RedisInsight/pull/1583) Click a pencil icon to make changes to database aliases.
- [#1579](https://github.com/RedisInsight/RedisInsight/pull/1579) Increase the database password length limitation to 10,000.

