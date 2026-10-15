# RedisGears readers

```json metadata
{
  "schema_version": 2,
  "title": "RedisGears readers",
  "description": "Extracts data from the database and creates records to pass through a RedisGears pipeline.",
  "categories": ["docs","operate","stack"],
  "tableOfContents": {"sections":[{"id":"classes","title":"Classes"}]}

,
  "codeExamples": []
}
```


A reader extracts data from the database and creates records.

The [`GearsBuilder.CreateGearsBuilder(reader)`](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/creategearsbuilder) function takes a reader as a parameter and passes the generated records through a pipeline of RedisGears functions.

## Classes


| Class | Description |
| --- | --- |
| [CommandOverrider](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/readers/commandoverrider/) | Override a Redis command. |
| [CommandReader](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/readers/commandreader/) | Run RedisGears functions on command. |
| [JavaReader](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/readers/javareader/) | A template for creating custom readers. |
| [KeysOnlyReader](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/readers/keysonlyreader/) | Gets key names from a database. |
| [KeysReader](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/readers/keysreader/) | Gets keys and their values from a database. |
| [ShardsIDReader](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/readers/shardsidreader/) | Gets the shard ID for each shard in a database. |
| [StreamReader](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/readers/streamreader/) | Reads Redis stream data. |

