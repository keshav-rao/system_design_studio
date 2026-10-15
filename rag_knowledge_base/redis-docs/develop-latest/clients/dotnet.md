# StackExchange.Redis guide (C#/.NET)

```json metadata
{
  "schema_version": 2,
  "title": "StackExchange.Redis guide (C#/.NET)",
  "description": "Connect your .NET application to a Redis database",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"install","title":"Install"},{"id":"connect-and-test","title":"Connect and test"},{"id":"more-information","title":"More information"}]}

,
  "codeExamples": [{"codetabsId":"landing-stepimport","description":"Foundational: Import required SE.Redis namespaces for Redis client functionality","difficulty":"beginner","id":"import","languages":[{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_landing-stepimport"},{"id":"dotnet-Async (SE-Redis)","panelId":"panel_Csharp-Async (SERedis)_landing-stepimport"}]},{"codetabsId":"landing-stepconnect","description":"Foundational: Connect to a Redis server and establish a client connection","difficulty":"beginner","id":"connect","languages":[{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_landing-stepconnect"},{"id":"dotnet-Async (SE-Redis)","panelId":"panel_Csharp-Async (SERedis)_landing-stepconnect"}]},{"codetabsId":"landing-stepset_get_string","description":"Foundational: Set and retrieve string values using SET and GET commands","difficulty":"beginner","id":"set_get_string","languages":[{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_landing-stepset_get_string"},{"id":"dotnet-Async (SE-Redis)","panelId":"panel_Csharp-Async (SERedis)_landing-stepset_get_string"}]},{"codetabsId":"landing-stepset_get_hash","description":"Foundational: Store and retrieve hash data structures using HSET and HGETALL","difficulty":"beginner","id":"set_get_hash","languages":[{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_landing-stepset_get_hash"},{"id":"dotnet-Async (SE-Redis)","panelId":"panel_Csharp-Async (SERedis)_landing-stepset_get_hash"}]}]
}
```

## Code Examples Legend

The code examples below show how to perform the same operations in different programming languages and client libraries:

- **Redis CLI**: Command-line interface for Redis
- **C# (Synchronous)**: StackExchange.Redis synchronous client
- **C# (Asynchronous)**: StackExchange.Redis asynchronous client
- **Go**: go-redis client
- **Java (Synchronous - Jedis)**: Jedis synchronous client
- **Java (Asynchronous - Lettuce)**: Lettuce asynchronous client
- **Java (Reactive - Lettuce)**: Lettuce reactive/streaming client
- **JavaScript (Node.js)**: node-redis client
- **PHP**: Predis client
- **Python**: redis-py client
- **Rust (Synchronous)**: redis-rs synchronous client
- **Rust (Asynchronous)**: redis-rs asynchronous client

Each code example demonstrates the same basic operation across different languages. The specific syntax and patterns vary based on the language and client library, but the underlying Redis commands and behavior remain consistent.

---


[StackExchange.Redis](https://github.com/StackExchange/StackExchange.Redis) is the main
.NET client for Redis. It provides an API for the core Redis data types and commands.
A separate library,
[NRedisStack](https://github.com/redis/NRedisStack), builds upon `StackExchange.Redis` with
support for an extended set of data types and features, such as [JSON](https://redis.io/docs/latest/develop/data-types/json),
[Redis search](https://redis.io/docs/latest/develop/ai/search-and-query),
[probabilistic data types](https://redis.io/docs/latest/develop/data-types/probabilistic), and
[Time series](https://redis.io/docs/latest/develop/data-types/timeseries).

The sections below explain how to install `StackExchange.Redis` and connect your application
to a Redis database. See the [NRedisStack guide](https://redis.io/docs/latest/develop/clients/dotnet/nredisstack) for information about installing and using `NRedisStack` to access the extended feature set.

`StackExchange.Redis` requires a running Redis server. For production apps,
provision a hosted Redis resource such as [Redis Cloud](https://redis.io/docs/latest/operate/rc)
or [Azure Managed Redis](https://learn.microsoft.com/en-us/azure/redis/overview).
For local development and testing, you can also run Redis Open Source locally.
See [Install Redis Open Source](https://redis.io/docs/latest/operate/oss_and_stack/install)
for installation instructions.

> [!NOTE]
> You can also access Redis with an object-mapping client interface. See
> [Redis OM for .NET](https://redis.io/docs/latest/integrate/redisom-for-net)
> for more information.

## Install

Using the `dotnet` CLI, run:

```bash
dotnet add package StackExchange.Redis
```

## Connect and test

Add the following imports to your source file:

Foundational: Import required SE.Redis namespaces for Redis client functionality

**Difficulty:** Beginner

**Available in:** C#, C#

##### C#

```csharp
using StackExchange.Redis;
```

##### C#

```csharp
using StackExchange.Redis;
```

##### C#

```csharp
using StackExchange.Redis;
```

##### C#

```csharp
using StackExchange.Redis;
```



Connect to localhost on port 6379. The client supports both synchronous and asynchronous commands.

Foundational: Connect to a Redis server and establish a client connection

**Difficulty:** Beginner

**Available in:** C#, C#

##### C#

```csharp
        var muxer = await ConnectionMultiplexer.ConnectAsync("localhost:6379");
        var db = muxer.GetDatabase();
```

##### C#

```csharp
        var muxer = ConnectionMultiplexer.Connect("localhost:6379");
        var db = muxer.GetDatabase();
```

##### C#

```csharp
        var muxer = await ConnectionMultiplexer.ConnectAsync("localhost:6379");
        var db = muxer.GetDatabase();
```

##### C#

```csharp
        var muxer = ConnectionMultiplexer.Connect("localhost:6379");
        var db = muxer.GetDatabase();
```



You can test the connection by storing and retrieving a simple string.

Foundational: Set and retrieve string values using SET and GET commands

**Difficulty:** Beginner

**Available in:** C#, C#

##### C#

```csharp
        await db.StringSetAsync("foo", "bar");
        string? fooResult = await db.StringGetAsync("foo");
        Console.WriteLine(fooResult); // >>> bar
```

##### C#

```csharp
        db.StringSet("foo", "bar");
        Console.WriteLine(db.StringGet("foo")); // >>> bar
```

##### C#

```csharp
        await db.StringSetAsync("foo", "bar");
        string? fooResult = await db.StringGetAsync("foo");
        Console.WriteLine(fooResult); // >>> bar
```

##### C#

```csharp
        db.StringSet("foo", "bar");
        Console.WriteLine(db.StringGet("foo")); // >>> bar
```



Store and retrieve a HashMap.

Foundational: Store and retrieve hash data structures using HSET and HGETALL

**Difficulty:** Beginner

**Available in:** C#, C#

##### C#

```csharp
        var hash = new HashEntry[] { 
            new HashEntry("name", "John"), 
            new HashEntry("surname", "Smith"),
            new HashEntry("company", "Redis"),
            new HashEntry("age", "29"),
            };
        await db.HashSetAsync("user-session:123", hash);

        var hashFields = await db.HashGetAllAsync("user-session:123");
        Console.WriteLine(String.Join("; ", hashFields));
        // >>> name: John; surname: Smith; company: Redis; age: 29
```

##### C#

```csharp
        var hash = new HashEntry[] {
            new HashEntry("name", "John"),
            new HashEntry("surname", "Smith"),
            new HashEntry("company", "Redis"),
            new HashEntry("age", "29"),
        };
        db.HashSet("user-session:123", hash);

        var hashFields = db.HashGetAll("user-session:123");
        Console.WriteLine(String.Join("; ", hashFields));
        // >>> name: John; surname: Smith; company: Redis; age: 29
```

##### C#

```csharp
        var hash = new HashEntry[] { 
            new HashEntry("name", "John"), 
            new HashEntry("surname", "Smith"),
            new HashEntry("company", "Redis"),
            new HashEntry("age", "29"),
            };
        await db.HashSetAsync("user-session:123", hash);

        var hashFields = await db.HashGetAllAsync("user-session:123");
        Console.WriteLine(String.Join("; ", hashFields));
        // >>> name: John; surname: Smith; company: Redis; age: 29
```

##### C#

```csharp
        var hash = new HashEntry[] {
            new HashEntry("name", "John"),
            new HashEntry("surname", "Smith"),
            new HashEntry("company", "Redis"),
            new HashEntry("age", "29"),
        };
        db.HashSet("user-session:123", hash);

        var hashFields = db.HashGetAll("user-session:123");
        Console.WriteLine(String.Join("; ", hashFields));
        // >>> name: John; surname: Smith; company: Redis; age: 29
```



## More information

See the other pages in this section for more information and examples.

