# GearsBuilder

```json metadata
{
  "schema_version": 2,
  "title": "GearsBuilder",
  "description": "Creates a RedisGears pipeline of operations to transform data.",
  "categories": ["docs","operate","stack"],
  "tableOfContents": {"sections":[{"id":"functions","title":"Functions"}]}

,
  "codeExamples": []
}
```


The `GearsBuilder` class allows you to create a pipeline of RedisGears functions that transform data.

It requires a reader to supply data to the pipe.

To create a `GearsBuilder` object, follow this example code:

```java
BaseReader reader = ...; // Initialize the reader
builder = GearsBuilder.CreateGearsBuilder(reader);
```

## Functions


| Function | Description |
| --- | --- |
| [accumulate](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/accumulate/) | Reduces many records in the pipe to a single record. |
| [accumulateBy](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/accumulateby/) | Groups records and reduces each group to a single record per group. |
| [asyncFilter](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/asyncfilter/) | Asynchronously filters out records in the pipe based on a given condition. |
| [asyncForeach](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/asyncforeach/) | For each record in the pipe, asynchronously runs some operations. |
| [asyncMap](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/asyncmap/) | Asynchronously maps records one-to-one. |
| [callNext](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/callnext/) | Calls the next execution that overrides the command or the original command itself. A more flexible version of callNextArray. |
| [callNextArray](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/callnextarray/) | Calls the next execution that overrides the command or the original command itself. |
| [collect](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/collect/) | Collects all records to the origin shard. |
| [configGet](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/config-get/) | Gets the value of a RedisGears configuration setting. |
| [count](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/count/) | Counts the number of records in the pipe. |
| [CreateGearsBuilder](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/creategearsbuilder/) | Creates a new GearsBuilder object. |
| [execute](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/execute/) | Runs a Redis command. A more flexible version of executeArray. |
| [executeArray](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/executearray/) | Runs a Redis command. |
| [filter](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/filter/) | Filters out records in the pipe based on a given condition. |
| [flatMap](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/flatmap/) | Maps a single input record to one or more output records. |
| [foreach](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/foreach/) | For each record in the pipe, runs some operations. |
| [hashtag](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/hashtag/) | Returns a string that maps to the current shard. |
| [localAccumulateBy](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/localaccumulateby/) | Groups records and reduces each group to a single record per group locally on each shard. |
| [log](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/log/) | Writes a log message to the Redis log file. |
| [map](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/map/) | Maps records one-to-one. |
| [register](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/register/) | Registers the pipeline of functions to run when certain events occur. |
| [repartition](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/repartition/) | Moves records between shards according to the extracted data. |
| [run](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/run/) | Runs the pipeline of functions immediately. |

