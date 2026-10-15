# Index and query documents

```json metadata
{
  "schema_version": 2,
  "title": "Index and query documents",
  "description": "Learn how to use Redis Search with JSON and hash documents.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "topics": ["Redis Search","JSON","hash"],
  "relatedPages": ["/develop/clients/dotnet/vecsearch","/develop/ai/search-and-query"],
  "scope": "example",
  "tableOfContents": {"sections":[{"id":"initialize","title":"Initialize"},{"id":"create-data","title":"Create data"},{"id":"add-the-index","title":"Add the index"},{"id":"add-the-data","title":"Add the data"},{"id":"query-the-data","title":"Query the data"},{"id":"differences-with-hash-documents","title":"Differences with hash documents"},{"id":"more-information","title":"More information"}]}

,
  "codeExamples": [{"codetabsId":"cs_home_json-stepimport","description":"Foundational: Import required libraries for Redis Search, JSON operations, and search functionality","difficulty":"beginner","id":"import","languages":[{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_cs_home_json-stepimport"}]},{"codetabsId":"cs_home_json-stepcreate_data","description":"Foundational: Define sample user data structures for indexing and querying","difficulty":"beginner","id":"create_data","languages":[{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_cs_home_json-stepcreate_data"}]},{"codetabsId":"cs_home_json-stepconnect","description":"Foundational: Establish a connection to a Redis server for query operations","difficulty":"beginner","id":"connect","languages":[{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_cs_home_json-stepconnect"}]},{"codetabsId":"cs_home_json-stepcleanup_json","description":"Foundational: Clean up existing indexes and documents to prepare for fresh example data","difficulty":"beginner","id":"cleanup_json","languages":[{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_cs_home_json-stepcleanup_json"}]},{"codetabsId":"cs_home_json-stepmake_index","description":"Foundational: Create a search index for JSON documents with field definitions and key prefix filtering","difficulty":"intermediate","id":"make_index","languages":[{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_cs_home_json-stepmake_index"}]},{"codetabsId":"cs_home_json-stepadd_data","description":"Foundational: Store JSON documents in Redis with automatic indexing based on key prefix","difficulty":"beginner","id":"add_data","languages":[{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_cs_home_json-stepadd_data"}]},{"codetabsId":"cs_home_json-stepquery1","description":"Query with filters: Search JSON documents using text matching and numeric range filters to find specific records","difficulty":"intermediate","id":"query1","languages":[{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_cs_home_json-stepquery1"}]},{"codetabsId":"cs_home_json-stepquery2","description":"Query with field projection: Retrieve only specific fields from search results to reduce data transfer","difficulty":"intermediate","id":"query2","languages":[{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_cs_home_json-stepquery2"}]},{"codetabsId":"cs_home_json-stepquery3","description":"Aggregation queries: Use GROUP BY and COUNT operations to summarize and analyze indexed data","difficulty":"advanced","id":"query3","languages":[{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_cs_home_json-stepquery3"}]},{"codetabsId":"cs_home_json-stepcleanup_hash","description":"Foundational: Clean up existing hash indexes and documents to prepare for fresh example data","difficulty":"beginner","id":"cleanup_hash","languages":[{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_cs_home_json-stepcleanup_hash"}]},{"codetabsId":"cs_home_json-stepmake_hash_index","description":"Foundational: Create a search index for hash documents with HASH index type and field definitions","difficulty":"intermediate","id":"make_hash_index","languages":[{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_cs_home_json-stepmake_hash_index"}]},{"codetabsId":"cs_home_json-stepadd_hash_data","description":"Foundational: Store hash documents in Redis with automatic indexing based on key prefix","difficulty":"beginner","id":"add_hash_data","languages":[{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_cs_home_json-stepadd_hash_data"}]},{"codetabsId":"cs_home_json-stepquery1_hash","description":"Query with filters: Search hash documents using text matching and numeric range filters (same as JSON queries)","difficulty":"intermediate","id":"query1_hash","languages":[{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_cs_home_json-stepquery1_hash"}]}]
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


This example shows how to create a
[search index](https://redis.io/docs/latest/develop/ai/search-and-query/indexing)
for [JSON](https://redis.io/docs/latest/develop/data-types/json) documents and
run queries against the index. It then goes on to show the slight differences
in the equivalent code for [hash](https://redis.io/docs/latest/develop/data-types/hashes)
documents.

> [!NOTE]
> From [v1.0.0](https://github.com/redis/NRedisStack/releases/tag/v1.0.0)
> onwards, `NRedisStack` uses query dialect 2 by default.
> Redis Search methods such as [`FT().Search()`](https://redis.io/docs/latest/commands/ft.search)
> will explicitly request this dialect, overriding the default set for the server.
> See
> [Query dialects](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/dialects)
> for more information.

## Initialize

Make sure that you have [Redis Open Source](https://redis.io/docs/latest/operate/oss_and_stack)
or another Redis server available. Also install the
[`NRedisStack`](https://redis.io/docs/latest/develop/clients/dotnet) client library if you
haven't already done so. 

Add the following dependencies:

Foundational: Import required libraries for Redis Search, JSON operations, and search functionality

**Difficulty:** Beginner

**Available in:** C#

##### C#

```csharp
using NRedisStack.RedisStackCommands;
using NRedisStack.Search;
using NRedisStack.Search.Aggregation;
using NRedisStack.Search.Literals.Enums;
using StackExchange.Redis;
```



## Create data

Create some test data to add to the database:

Foundational: Define sample user data structures for indexing and querying

**Difficulty:** Beginner

**Available in:** C#

##### C#

```csharp
        var user1 = new
        {
            name = "Paul John",
            email = "paul.john@example.com",
            age = 42,
            city = "London"
        };

        var user2 = new
        {
            name = "Eden Zamir",
            email = "eden.zamir@example.com",
            age = 29,
            city = "Tel Aviv"
        };

        var user3 = new
        {
            name = "Paul Zamir",
            email = "paul.zamir@example.com",
            age = 35,
            city = "Tel Aviv"
        };
```



## Add the index

Connect to your Redis database. The code below shows the most
basic connection but see
[Connect to the server](https://redis.io/docs/latest/develop/clients/dotnet/connect)
to learn more about the available connection options.

Foundational: Establish a connection to a Redis server for query operations

**Difficulty:** Beginner

**Available in:** C#

##### C#

```csharp
        var muxer = ConnectionMultiplexer.Connect("localhost:6379");
        var db = muxer.GetDatabase();
```



Delete any existing index called `idx:users` and any keys that start with `user:`.

Foundational: Clean up existing indexes and documents to prepare for fresh example data

**Difficulty:** Beginner

**Available in:** C#

##### C#

```csharp
        db.KeyDelete(["user:1", "user:2", "user:3"]);
        try { db.FT().DropIndex("idx:users"); } catch { }
```



Create an index. In this example, only JSON documents with the key prefix `user:` are indexed. For more information, see [Query syntax](https://redis.io/docs/latest/develop/ai/search-and-query/query).

Foundational: Create a search index for JSON documents with field definitions and key prefix filtering

**Difficulty:** Intermediate

**Available in:** C#

##### C#

```csharp
        var schema = new Schema()
            .AddTextField(new FieldName("$.name", "name"))
            .AddTagField(new FieldName("$.city", "city"))
            .AddNumericField(new FieldName("$.age", "age"));

        bool indexCreated = db.FT().Create(
            "idx:users",
            new FTCreateParams()
                .On(IndexDataType.JSON)
                .Prefix("user:"),
            schema
        );
```



## Add the data

Add the three sets of user data to the database as
[JSON](https://redis.io/docs/latest/develop/data-types/json) objects.
If you use keys with the `user:` prefix then Redis will index the
objects automatically as you add them:

Foundational: Store JSON documents in Redis with automatic indexing based on key prefix

**Difficulty:** Beginner

**Available in:** C#

##### C#

```csharp
        bool user1Set = db.JSON().Set("user:1", "$", user1);
        bool user2Set = db.JSON().Set("user:2", "$", user2);
        bool user3Set = db.JSON().Set("user:3", "$", user3);
```



## Query the data

You can now use the index to search the JSON objects. The
[query](https://redis.io/docs/latest/develop/ai/search-and-query/query)
below searches for objects that have the text "Paul" in any field
and have an `age` value in the range 30 to 40:

Query with filters: Search JSON documents using text matching and numeric range filters to find specific records

**Difficulty:** Intermediate

**Available in:** C#

##### C#

```csharp
        SearchResult findPaulResult = db.FT().Search(
            "idx:users",
            new("Paul @age:[30 40]")
        );
        Console.WriteLine(string.Join(
            ", ",
            findPaulResult.Documents.Select(x => x["json"])
        ));
        // >>> {"name":"Paul Zamir","email":"paul.zamir@example.com", ...
```



Specify query options to return only the `city` field:

Query with field projection: Retrieve only specific fields from search results to reduce data transfer

**Difficulty:** Intermediate

**Available in:** C#

##### C#

```csharp
        var citiesResult = db.FT().Search(
            "idx:users",
            new Query("Paul")
                .ReturnFields(new FieldName("$.city", "city"))
        );
        Console.WriteLine(string.Join(
            ", ",
            citiesResult.Documents.Select(x => x["city"]).OrderBy(x => x)
        ));
        // >>> London, Tel Aviv
```



Use an
[aggregation query](https://redis.io/docs/latest/develop/ai/search-and-query/query/aggregation)
to count all users in each city.

Aggregation queries: Use GROUP BY and COUNT operations to summarize and analyze indexed data

**Difficulty:** Advanced

**Available in:** C#

##### C#

```csharp
        AggregationRequest aggRequest = new AggregationRequest("*")
            .GroupBy("@city", Reducers.Count().As("count"));

        AggregationResult aggResult = db.FT().Aggregate("idx:users", aggRequest);
        IReadOnlyList<Dictionary<string, RedisValue>> resultsList =
                                                        aggResult.GetResults();

        for (var i = 0; i < resultsList.Count; i++)
        {
            Dictionary<string, RedisValue> item = resultsList.ElementAt(i);
            Console.WriteLine($"{item["city"]} - {item["count"]}");
        }
        // >>> London - 1
        // >>> Tel Aviv - 2
```



## Differences with hash documents

Indexing for hash documents is very similar to JSON indexing but you
need to specify some slightly different options.

When you create the schema for a hash index, you don't need to
add aliases for the fields, since you use the basic names to access
the fields anyway. Also, you must set the `On` option to `IndexDataType.HASH`
in the `FTCreateParams` object when you create the index. The code below shows
these changes with a new index called `hash-idx:users`, which is otherwise the
same as the `idx:users` index used for JSON documents in the previous examples.

First, delete any existing index called `hash-idx:users` and any keys that start with `huser:`.

Foundational: Clean up existing hash indexes and documents to prepare for fresh example data

**Difficulty:** Beginner

**Available in:** C#

##### C#

```csharp
        db.KeyDelete(["huser:1", "huser:2", "huser:3"]);
        try { db.FT().DropIndex("hash-idx:users"); } catch { }
```



Now create the new index:

Foundational: Create a search index for hash documents with HASH index type and field definitions

**Difficulty:** Intermediate

**Available in:** C#

##### C#

```csharp
        var hashSchema = new Schema()
            .AddTextField("name")
            .AddTagField("city")
            .AddNumericField("age");

        bool hashIndexCreated = db.FT().Create(
            "hash-idx:users",
            new FTCreateParams()
                .On(IndexDataType.HASH)
                .Prefix("huser:"),
            hashSchema
        );
```



You use [`HashSet()`](https://redis.io/docs/latest/commands/hset) to add the hash
documents instead of [`JSON.Set()`](https://redis.io/docs/latest/commands/json.set).
Also, you must add the fields as key-value pairs instead of combining them
into a single object.

Foundational: Store hash documents in Redis with automatic indexing based on key prefix

**Difficulty:** Beginner

**Available in:** C#

##### C#

```csharp
        db.HashSet("huser:1", [
            new("name", "Paul John"),
            new("email", "paul.john@example.com"),
            new("age", 42),
            new("city", "London")
        ]);

        db.HashSet("huser:2", [
            new("name", "Eden Zamir"),
            new("email", "eden.zamir@example.com"),
            new("age", 29),
            new("city", "Tel Aviv")
        ]);

        db.HashSet("huser:3", [
            new("name", "Paul Zamir"),
            new("email", "paul.zamir@example.com"),
            new("age", 35),
            new("city", "Tel Aviv")
        ]);
```



The query commands work the same here for hash as they do for JSON (but
the name of the hash index is different). The format of the result is
almost the same except that the fields are returned directly in the
`Document` object of the result (for JSON, the fields are all enclosed
in a string under the key `json`):

Query with filters: Search hash documents using text matching and numeric range filters (same as JSON queries)

**Difficulty:** Intermediate

**Available in:** C#

##### C#

```csharp
        SearchResult findPaulHashResult = db.FT().Search(
            "hash-idx:users",
            new("Paul @age:[30 40]")
        );

        foreach (Document doc in findPaulHashResult.Documents)
        {
            Console.WriteLine(
                $"Name: {doc["name"]}, email: {doc["email"]}, " +
                $"age: {doc["age"]}, city:{doc["city"]}"
            );
        }
        // >>> Name: Paul Zamir, email: paul.zamir@example.com, age: 35, ...
```



## More information

See the [Redis Search](https://redis.io/docs/latest/develop/ai/search-and-query) docs
for a full description of all query features with examples.

