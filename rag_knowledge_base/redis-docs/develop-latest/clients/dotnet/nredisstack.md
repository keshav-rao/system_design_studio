# NRedisStack extensions guide

```json metadata
{
  "schema_version": 2,
  "title": "NRedisStack extensions guide",
  "description": "Access Redis Open Source modules",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"install","title":"Install"},{"id":"redis-open-source-modules","title":"Redis Open Source modules"},{"id":"more-information","title":"More information"}]}

,
  "codeExamples": []
}
```


[NRedisStack](https://github.com/redis/NRedisStack) is a library that builds upon [StackExchange.Redis](https://github.com/StackExchange/StackExchange.Redis) and provides an API for the extended set of Redis data types and features, such as [JSON](https://redis.io/docs/latest/develop/data-types/json), [Redis search](https://redis.io/docs/latest/develop/ai/search-and-query),
[probabilistic data types](https://redis.io/docs/latest/develop/data-types/probabilistic), and [Time series](https://redis.io/docs/latest/develop/data-types/timeseries).
The sections below explain how to install `NRedisStack`. Note that this also installs
`StackExchange.Redis` as a dependency, so you don't need to install it as a separate step.

`NRedisStack` requires a running Redis server. For production apps, provision
a hosted Redis resource such as [Redis Cloud](https://redis.io/docs/latest/operate/rc) or
[Azure Managed Redis](https://learn.microsoft.com/en-us/azure/redis/overview). For
local development and testing, you can also run Redis Open Source locally. See
[Install Redis Open Source](https://redis.io/docs/latest/operate/oss_and_stack/install)
for installation instructions.

> [!NOTE]
> You can also access Redis with an object-mapping client interface. See
> [Redis OM for .NET](https://redis.io/docs/latest/integrate/redisom-for-net)
> for more information.

## Install

Using the `dotnet` CLI, run:

```bash
dotnet add package NRedisStack
```

## Redis Open Source modules

To access Redis Open Source capabilities, use the appropriate interface like this:

```cs
IBloomCommands bf = db.BF();    // Bloom filter commands
ICuckooCommands cf = db.CF();  // Cuckoo filter commands
ICmsCommands cms = db.CMS();   // Count-min sketch commands
ITopKCommands topk = db.TOPK(); // Top-K commands
ITdigestCommands tdigest = db.TDIGEST(); // T-digest commands
ISearchCommands ft = db.FT();  // Redis search commands
IJsonCommands json = db.JSON(); // JSON commands
ITimeSeriesCommands ts = db.TS(); // Time series commands
```

## More information

See the other pages in this section for more information and examples.

