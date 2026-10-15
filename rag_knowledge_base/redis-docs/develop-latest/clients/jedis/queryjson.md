# Index and query documents

```json metadata
{
  "schema_version": 2,
  "title": "Index and query documents",
  "description": "Learn how to use Redis Search with JSON and hash documents.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "topics": ["Redis Search","JSON","hash"],
  "relatedPages": ["/develop/clients/jedis/vecsearch","/develop/ai/search-and-query"],
  "scope": "example",
  "tableOfContents": {"sections":[{"id":"initialize","title":"Initialize"},{"id":"create-data","title":"Create data"},{"id":"add-the-index","title":"Add the index"},{"id":"add-the-data","title":"Add the data"},{"id":"query-the-data","title":"Query the data"},{"id":"differences-with-hash-documents","title":"Differences with hash documents"},{"id":"more-information","title":"More information"}]}

,
  "codeExamples": [{"codetabsId":"java_home_json-stepimport","description":"Foundational: Import required Jedis classes for JSON indexing and query operations","difficulty":"beginner","id":"import","languages":[{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_java_home_json-stepimport"}]},{"codetabsId":"java_home_json-stepcreate_data","description":"Foundational: Define sample user data structures for indexing and querying","difficulty":"beginner","id":"create_data","languages":[{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_java_home_json-stepcreate_data"}]},{"codetabsId":"java_home_json-stepconnect","description":"Foundational: Establish a connection to a Redis server for query operations","difficulty":"beginner","id":"connect","languages":[{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_java_home_json-stepconnect"}]},{"codetabsId":"java_home_json-stepcleanup_json","description":"Foundational: Clean up existing indexes and data before creating new indexes","difficulty":"beginner","id":"cleanup_json","languages":[{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_java_home_json-stepcleanup_json"}]},{"codetabsId":"java_home_json-stepmake_index","description":"Foundational: Create a search index for JSON documents with field definitions and key prefix filtering","difficulty":"intermediate","id":"make_index","languages":[{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_java_home_json-stepmake_index"}]},{"codetabsId":"java_home_json-stepadd_data","description":"Foundational: Store JSON documents in Redis with automatic indexing based on key prefix","difficulty":"beginner","id":"add_data","languages":[{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_java_home_json-stepadd_data"}]},{"codetabsId":"java_home_json-stepquery1","description":"Query with filters: Search JSON documents using text matching and numeric range filters to find specific records","difficulty":"intermediate","id":"query1","languages":[{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_java_home_json-stepquery1"}]},{"codetabsId":"java_home_json-stepquery2","description":"Query with field projection: Retrieve only specific fields from search results to reduce data transfer","difficulty":"intermediate","id":"query2","languages":[{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_java_home_json-stepquery2"}]},{"codetabsId":"java_home_json-stepquery3","description":"Aggregation query: Group and count results by field values to analyze data patterns","difficulty":"intermediate","id":"query3","languages":[{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_java_home_json-stepquery3"}]},{"codetabsId":"java_home_json-stepcleanup_hash","description":"Foundational: Clean up existing hash indexes and data before creating new indexes","difficulty":"beginner","id":"cleanup_hash","languages":[{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_java_home_json-stepcleanup_hash"}]},{"codetabsId":"java_home_json-stepmake_hash_index","description":"Foundational: Create a search index for hash documents with field definitions and key prefix filtering","difficulty":"intermediate","id":"make_hash_index","languages":[{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_java_home_json-stepmake_hash_index"}]},{"codetabsId":"java_home_json-stepadd_hash_data","description":"Foundational: Store hash documents in Redis with automatic indexing based on key prefix","difficulty":"beginner","id":"add_hash_data","languages":[{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_java_home_json-stepadd_hash_data"}]},{"codetabsId":"java_home_json-stepquery1_hash","description":"Query with filters: Search hash documents using text matching and numeric range filters (same as JSON queries)","difficulty":"intermediate","id":"query1_hash","languages":[{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_java_home_json-stepquery1_hash"}]}]
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
> From [v6.0.0](https://github.com/redis/jedis/releases/tag/v6.0.0) onwards,
> `Jedis` uses query dialect 2 by default.
> Redis Search methods such as [`ftSearch()`](https://redis.io/docs/latest/commands/ft.search)
> will explicitly request this dialect, overriding the default set for the server.
> See
> [Query dialects](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/dialects)
> for more information.

## Initialize

Make sure that you have [Redis Open Source](https://redis.io/docs/latest/operate/oss_and_stack)
or another Redis server available. Also install the
[Jedis](https://redis.io/docs/latest/develop/clients/jedis) client library if you
haven't already done so.

Add the following dependencies. All of them are applicable to both JSON and hash,
except for the `Path` and `JSONObject` classes, which are specific to JSON (see
[Path](https://redis.io/docs/latest/develop/data-types/json/path) for a description of the
JSON path syntax).

Foundational: Import required Jedis classes for JSON indexing and query operations

**Difficulty:** Beginner

**Available in:** Java (Synchronous - Jedis)

##### Java (Synchronous - Jedis)

```java
import redis.clients.jedis.RedisClient;
import redis.clients.jedis.exceptions.JedisDataException;
import redis.clients.jedis.json.Path2;
import redis.clients.jedis.search.*;
import redis.clients.jedis.search.aggr.*;
import redis.clients.jedis.search.schemafields.*;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
```



## Create data

Create some test data to add to the database:

Foundational: Define sample user data structures for indexing and querying

**Difficulty:** Beginner

**Available in:** Java (Synchronous - Jedis)

##### Java (Synchronous - Jedis)

```java
        JSONObject user1 = new JSONObject()
                .put("name", "Paul John")
                .put("email", "paul.john@example.com")
                .put("age", 42)
                .put("city", "London");
        
        JSONObject user2 = new JSONObject()
                .put("name", "Eden Zamir")
                .put("email", "eden.zamir@example.com")
                .put("age", 29)
                .put("city", "Tel Aviv");
        
        JSONObject user3 = new JSONObject()
                .put("name", "Paul Zamir")
                .put("email", "paul.zamir@example.com")
                .put("age", 35)
                .put("city", "Tel Aviv");
```



## Add the index

Connect to your Redis database. The code below shows the most
basic connection but see
[Connect to the server](https://redis.io/docs/latest/develop/clients/jedis/connect)
to learn more about the available connection options.

Foundational: Establish a connection to a Redis server for query operations

**Difficulty:** Beginner

**Available in:** Java (Synchronous - Jedis)

##### Java (Synchronous - Jedis)

```java
        RedisClient jedis = new RedisClient("redis://localhost:6379");
```



Delete any existing index called `idx:users` and any keys that start with `user:`.

Foundational: Clean up existing indexes and data before creating new indexes

**Difficulty:** Beginner

**Available in:** Java (Synchronous - Jedis)

##### Java (Synchronous - Jedis)

```java
        try {jedis.ftDropIndex("idx:users");} catch (JedisDataException j){}
        jedis.del("user:1", "user:2", "user:3");
```



Create an index. In this example, only JSON documents with the key prefix `user:` are indexed. For more information, see [Query syntax](https://redis.io/docs/latest/develop/ai/search-and-query/query).

Foundational: Create a search index for JSON documents with field definitions and key prefix filtering

**Difficulty:** Intermediate

**Available in:** Java (Synchronous - Jedis)

##### Java (Synchronous - Jedis)

```java
        SchemaField[] schema = {
            TextField.of("$.name").as("name"),
            TextField.of("$.city").as("city"),
            NumericField.of("$.age").as("age")
        };

        String createResult = jedis.ftCreate("idx:users",
            FTCreateParams.createParams()
                .on(IndexDataType.JSON)
                .addPrefix("user:"),
                schema
        );

        System.out.println(createResult); // >>> OK
```



## Add the data

Add the three sets of user data to the database as
[JSON](https://redis.io/docs/latest/develop/data-types/json) objects.
If you use keys with the `user:` prefix then Redis will index the
objects automatically as you add them:

Foundational: Store JSON documents in Redis with automatic indexing based on key prefix

**Difficulty:** Beginner

**Available in:** Java (Synchronous - Jedis)

##### Java (Synchronous - Jedis)

```java
        String user1Set = jedis.jsonSet("user:1", new Path2("$"), user1);
        String user2Set = jedis.jsonSet("user:2", new Path2("$"), user2);
        String user3Set = jedis.jsonSet("user:3", new Path2("$"), user3);
```



## Query the data

You can now use the index to search the JSON objects. The
[query](https://redis.io/docs/latest/develop/ai/search-and-query/query)
below searches for objects that have the text "Paul" in any field
and have an `age` value in the range 30 to 40:

Query with filters: Search JSON documents using text matching and numeric range filters to find specific records

**Difficulty:** Intermediate

**Available in:** Java (Synchronous - Jedis)

##### Java (Synchronous - Jedis)

```java
        SearchResult findPaulResult = jedis.ftSearch("idx:users",
             "Paul @age:[30 40]"
        );
        
        System.out.println(findPaulResult.getTotalResults()); // >>> 1

        List<Document> paulDocs = findPaulResult.getDocuments();

        for (Document doc: paulDocs) {
            System.out.println(doc.getId());
        }
        // >>> user:3
```



Specify query options to return only the `city` field:

Query with field projection: Retrieve only specific fields from search results to reduce data transfer

**Difficulty:** Intermediate

**Available in:** Java (Synchronous - Jedis)

##### Java (Synchronous - Jedis)

```java
        SearchResult citiesResult = jedis.ftSearch("idx:users",
            "Paul",
            FTSearchParams.searchParams()
                .returnFields("city")
        );

        System.out.println(citiesResult.getTotalResults()); // >>> 2

        for (Document doc: citiesResult.getDocuments()) {
            System.out.println(doc.getId());
        }
        // >>> user:1
        // >>> user:3
```



Use an
[aggregation query](https://redis.io/docs/latest/develop/ai/search-and-query/query/aggregation)
to count all users in each city.

Aggregation query: Group and count results by field values to analyze data patterns

**Difficulty:** Intermediate

**Available in:** Java (Synchronous - Jedis)

##### Java (Synchronous - Jedis)

```java
        AggregationResult aggResult = jedis.ftAggregate("idx:users",
            new AggregationBuilder("*")
                .groupBy("@city", Reducers.count().as("count"))
        );

        System.out.println(aggResult.getTotalResults()); // >>> 2

        for (Row cityRow: aggResult.getRows()) {
            System.out.printf("%s - %d%n",
                cityRow.getString("city"), cityRow.getLong("count"));
        }
        // >>> London - 1
        // >>> Tel Aviv - 2
```



## Differences with hash documents

Indexing for hash documents is very similar to JSON indexing but you
need to specify some slightly different options.

When you create the schema for a hash index, you don't need to
add aliases for the fields, since you use the basic names to access
the fields anyway. Also, you must use `IndexDataType.HASH` for the `On()`
option of `FTCreateParams` when you create the index. The code below shows these
changes with a new index called `hash-idx:users`, which is otherwise the same as
the `idx:users` index used for JSON documents in the previous examples.

First, delete any existing index called `hash-idx:users` and any keys that start with `huser:`.

Foundational: Clean up existing hash indexes and data before creating new indexes

**Difficulty:** Beginner

**Available in:** Java (Synchronous - Jedis)

##### Java (Synchronous - Jedis)

```java
        try {jedis.ftDropIndex("hash-idx:users");} catch (JedisDataException j){}
        jedis.del("huser:1", "huser:2", "huser:3");
```



Now create the new index:

Foundational: Create a search index for hash documents with field definitions and key prefix filtering

**Difficulty:** Intermediate

**Available in:** Java (Synchronous - Jedis)

##### Java (Synchronous - Jedis)

```java
        SchemaField[] hashSchema = {
            TextField.of("name"),
            TextField.of("city"),
            NumericField.of("age")
        };

        String hashCreateResult = jedis.ftCreate("hash-idx:users",
            FTCreateParams.createParams()
                .on(IndexDataType.HASH)
                .addPrefix("huser:"),
                hashSchema
        );

        System.out.println(hashCreateResult); // >>> OK
```



Use [`hset()`](https://redis.io/docs/latest/commands/hset) to add the hash
documents instead of [`jsonSet()`](https://redis.io/docs/latest/commands/json.set).

Foundational: Store hash documents in Redis with automatic indexing based on key prefix

**Difficulty:** Beginner

**Available in:** Java (Synchronous - Jedis)

##### Java (Synchronous - Jedis)

```java
        Map<String, String> user1Info = new HashMap<>();
        user1Info.put("name", "Paul John");
        user1Info.put("email", "paul.john@example.com");
        user1Info.put("age", "42");
        user1Info.put("city", "London");
        long huser1Set = jedis.hset("huser:1", user1Info);
        
        System.out.println(huser1Set); // >>> 4

        Map<String, String> user2Info = new HashMap<>();
        user2Info.put("name", "Eden Zamir");
        user2Info.put("email", "eden.zamir@example.com");
        user2Info.put("age", "29");
        user2Info.put("city", "Tel Aviv");
        long huser2Set = jedis.hset("huser:2", user2Info);
        
        System.out.println(huser2Set); // >>> 4

        Map<String, String> user3Info = new HashMap<>();
        user3Info.put("name", "Paul Zamir");
        user3Info.put("email", "paul.zamir@example.com");
        user3Info.put("age", "35");
        user3Info.put("city", "Tel Aviv");
        long huser3Set = jedis.hset("huser:3", user3Info);
        
        System.out.println(huser3Set); // >>> 4
```



The query commands work the same here for hash as they do for JSON (but
the name of the hash index is different). The results are returned in
a `List` of `Document` objects, as with JSON:

Query with filters: Search hash documents using text matching and numeric range filters (same as JSON queries)

**Difficulty:** Intermediate

**Available in:** Java (Synchronous - Jedis)

##### Java (Synchronous - Jedis)

```java
        SearchResult findPaulHashResult = jedis.ftSearch("hash-idx:users",
             "Paul @age:[30 40]"
        );
        
        System.out.println(findPaulHashResult.getTotalResults()); // >>> 1

        List<Document> paulHashDocs = findPaulHashResult.getDocuments();

        for (Document doc: paulHashDocs) {
            System.out.println(doc.getId());
        }
        // >>> user:3
```



## More information

See the [Redis Search](https://redis.io/docs/latest/develop/ai/search-and-query) docs
for a full description of all query features with examples.

