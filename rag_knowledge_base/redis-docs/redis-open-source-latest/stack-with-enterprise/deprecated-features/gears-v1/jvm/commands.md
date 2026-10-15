# RedisGears JVM commands

```json metadata
{
  "schema_version": 2,
  "title": "RedisGears JVM commands",
  "description": "",
  "categories": ["docs","operate","stack"],
  "tableOfContents": {"sections":[{"id":"jvm-plugin-commands","title":"JVM plugin commands"}]}

,
  "codeExamples": []
}
```


Use a Redis client like `redis-cli` to send commands to the RedisGears JVM plugin.

## JVM plugin commands


| Command | Description |
| --- | --- |
| [RG.JDUMPSESSIONS](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/commands/rg-jdumpsessions/) | Outputs information about existing Java sessions. |
| [RG.JEXECUTE](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/commands/rg-jexecute/) | Executes a Java function. |


> [!NOTE]
> Ignore any commands that start with `RG.PY` while using the JVM plugin. The `RG.PY` commands are for the Python plugin.
