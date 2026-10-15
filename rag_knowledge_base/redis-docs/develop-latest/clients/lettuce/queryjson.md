# Index and query documents

```json metadata
{
  "schema_version": 2,
  "title": "Index and query documents",
  "description": "Learn how to use Redis Search with JSON and hash documents.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "topics": ["Redis Search","JSON","hash"],
  "relatedPages": ["/develop/clients/lettuce/vecsearch","/develop/ai/search-and-query"],
  "scope": "example",
  "tableOfContents": {"sections":[{"id":"initialize","title":"Initialize"},{"id":"create-data","title":"Create data"},{"id":"add-the-index","title":"Add the index"},{"id":"add-the-data","title":"Add the data"},{"id":"query-the-data","title":"Query the data"},{"id":"differences-with-hash-documents","title":"Differences with hash documents"},{"id":"more-information","title":"More information"}]}

,
  "codeExamples": [{"codetabsId":"lettuce_home_json-stepimport","description":"Foundational: Import required Lettuce and JSON libraries for querying JSON documents","difficulty":"beginner","id":"import","languages":[{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_lettuce_home_json-stepimport"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_lettuce_home_json-stepimport"}]},{"codetabsId":"lettuce_home_json-stepcreate_data","description":"Foundational: Define sample JSON data structures for users with fields like name, age, and city","difficulty":"beginner","id":"create_data","languages":[{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_lettuce_home_json-stepcreate_data"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_lettuce_home_json-stepcreate_data"}]},{"codetabsId":"lettuce_home_json-stepconnect","description":"Foundational: Establish a connection to Redis for executing search and query operations","difficulty":"beginner","id":"connect","languages":[{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_lettuce_home_json-stepconnect"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_lettuce_home_json-stepconnect"}]},{"codetabsId":"lettuce_home_json-stepmake_index","description":"Foundational: Create a search index on JSON documents with field mappings and aliases for efficient querying","difficulty":"intermediate","id":"make_index","languages":[{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_lettuce_home_json-stepmake_index"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_lettuce_home_json-stepmake_index"}]},{"codetabsId":"lettuce_home_json-stepadd_data","description":"Foundational: Store JSON documents in Redis using the JSON.SET command with keys matching the index prefix","difficulty":"beginner","id":"add_data","languages":[{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_lettuce_home_json-stepadd_data"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_lettuce_home_json-stepadd_data"}]},{"codetabsId":"lettuce_home_json-stepquery1","description":"Query data: Execute a full-text search combined with numeric range filtering to find matching documents","difficulty":"intermediate","id":"query1","languages":[{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_lettuce_home_json-stepquery1"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_lettuce_home_json-stepquery1"}]},{"codetabsId":"lettuce_home_json-stepquery2","description":"Restrict query results: Use query options to project specific fields from search results, reducing data transfer","difficulty":"intermediate","id":"query2","languages":[{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_lettuce_home_json-stepquery2"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_lettuce_home_json-stepquery2"}]},{"codetabsId":"lettuce_home_json-stepquery3","description":"Aggregation: Use aggregation queries to group and count results, performing server-side data analysis","difficulty":"advanced","id":"query3","languages":[{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_lettuce_home_json-stepquery3"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_lettuce_home_json-stepquery3"}]},{"codetabsId":"lettuce_home_json-stepmake_hash_index","description":"Foundational: Create a search index on hash documents with TargetType.HASH configuration","difficulty":"intermediate","id":"make_hash_index","languages":[{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_lettuce_home_json-stepmake_hash_index"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_lettuce_home_json-stepmake_hash_index"}]},{"codetabsId":"lettuce_home_json-stepadd_hash_data","description":"Foundational: Store hash documents in Redis using HSET command with keys matching the index prefix","difficulty":"beginner","id":"add_hash_data","languages":[{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_lettuce_home_json-stepadd_hash_data"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_lettuce_home_json-stepadd_hash_data"}]},{"codetabsId":"lettuce_home_json-stepquery1_hash","description":"Query data: Execute the same search query on hash documents as you would on JSON documents","difficulty":"intermediate","id":"query1_hash","languages":[{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_lettuce_home_json-stepquery1_hash"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_lettuce_home_json-stepquery1_hash"}]}]
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

## Initialize

Make sure that you have [Redis Open Source](https://redis.io/docs/latest/operate/oss_and_stack)
or another Redis server available. Also install the
[Lettuce](https://redis.io/docs/latest/develop/clients/lettuce) client library if you
haven't already done so.

Add the following dependencies. All of them are applicable to both JSON and hash,
except for the `JsonParser`, `JsonPath`, and `JsonObject` classes.

Foundational: Import required Lettuce and JSON libraries for querying JSON documents

**Difficulty:** Beginner

**Available in:** Java (Asynchronous - Lettuce), Java (Reactive - Lettuce)

##### Java (Asynchronous - Lettuce)

```java
import io.lettuce.core.*;

import io.lettuce.core.api.async.RedisAsyncCommands;
import io.lettuce.core.api.async.RediSearchAsyncCommands;
import io.lettuce.core.search.arguments.*;
import io.lettuce.core.search.arguments.AggregateArgs.*;
import io.lettuce.core.search.SearchReply;
import io.lettuce.core.search.AggregationReply;

import io.lettuce.core.json.JsonParser;
import io.lettuce.core.json.JsonObject;
import io.lettuce.core.json.JsonPath;

import io.lettuce.core.api.StatefulRedisConnection;

import java.util.*;
import java.util.concurrent.CompletableFuture;
```

##### Java (Reactive - Lettuce)

```java
import io.lettuce.core.*;

import io.lettuce.core.api.reactive.RedisReactiveCommands;
import io.lettuce.core.api.reactive.RediSearchReactiveCommands;
import io.lettuce.core.search.arguments.*;
import io.lettuce.core.search.arguments.AggregateArgs.*;
import io.lettuce.core.search.SearchReply;
import io.lettuce.core.search.AggregationReply;

import io.lettuce.core.json.JsonParser;
import io.lettuce.core.json.JsonObject;
import io.lettuce.core.json.JsonPath;

import io.lettuce.core.api.StatefulRedisConnection;

import java.util.*;
import reactor.core.publisher.Mono;
```



## Create data

Create some test data to add to the database:

Foundational: Define sample JSON data structures for users with fields like name, age, and city

**Difficulty:** Beginner

**Available in:** Java (Asynchronous - Lettuce), Java (Reactive - Lettuce)

##### Java (Asynchronous - Lettuce)

```java
            JsonParser parser = asyncCommands.getJsonParser();

            JsonObject user1 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul John\""))
                    .put("email", parser.createJsonValue("\"paul.john@example.com\"")).put("age", parser.createJsonValue("42"))
                    .put("city", parser.createJsonValue("\"London\""));

            JsonObject user2 = parser.createJsonObject().put("name", parser.createJsonValue("\"Eden Zamir\""))
                    .put("email", parser.createJsonValue("\"eden.zamir@example.com\"")).put("age", parser.createJsonValue("29"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            JsonObject user3 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul Zamir\""))
                    .put("email", parser.createJsonValue("\"paul.zamir@example.com\"")).put("age", parser.createJsonValue("35"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));
```

##### Java (Reactive - Lettuce)

```java
            JsonParser parser = reactiveCommands.getJsonParser();
            JsonObject user1 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul John\""))
                    .put("email", parser.createJsonValue("\"paul.john@example.com\"")).put("age", parser.createJsonValue("42"))
                    .put("city", parser.createJsonValue("\"London\""));

            JsonObject user2 = parser.createJsonObject().put("name", parser.createJsonValue("\"Eden Zamir\""))
                    .put("email", parser.createJsonValue("\"eden.zamir@example.com\"")).put("age", parser.createJsonValue("29"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            JsonObject user3 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul Zamir\""))
                    .put("email", parser.createJsonValue("\"paul.zamir@example.com\"")).put("age", parser.createJsonValue("35"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));
```



## Add the index

Connect to your Redis database. The code below shows the most
basic connection but see
[Connect to the server](https://redis.io/docs/latest/develop/clients/lettuce/connect)
to learn more about the available connection options.

Foundational: Establish a connection to Redis for executing search and query operations

**Difficulty:** Beginner

**Available in:** Java (Asynchronous - Lettuce), Java (Reactive - Lettuce)

##### Java (Asynchronous - Lettuce)

```java
        RedisClient redisClient = RedisClient.create("redis://localhost:6379");

        try (StatefulRedisConnection<String, String> connection = redisClient.connect()) {
            RedisAsyncCommands<String, String> asyncCommands = connection.async();
            RediSearchAsyncCommands<String, String> searchCommands = connection.async();
            // ...
```

##### Java (Reactive - Lettuce)

```java
        RedisClient redisClient = RedisClient.create("redis://localhost:6379");

        try (StatefulRedisConnection<String, String> connection = redisClient.connect()) {
            RedisReactiveCommands<String, String> reactiveCommands = connection.reactive();
            RediSearchReactiveCommands<String, String> searchCommands = connection.reactive();
            // ...
```



Create an index. In this example, only JSON documents with the key prefix `user:` are indexed. For more information, see [Query syntax](https://redis.io/docs/latest/develop/ai/search-and-query/query).

Foundational: Create a search index on JSON documents with field mappings and aliases for efficient querying

**Difficulty:** Intermediate

**Available in:** Java (Asynchronous - Lettuce), Java (Reactive - Lettuce)

##### Java (Asynchronous - Lettuce)

```java
            List<FieldArgs<String>> schema = Arrays.asList(TextFieldArgs.<String> builder().name("$.name").as("name").build(),
                    NumericFieldArgs.<String> builder().name("$.age").as("age").build(),
                    TagFieldArgs.<String> builder().name("$.city").as("city").build());

            CreateArgs<String, String> createArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.JSON)
                    .withPrefix("user:").build();

            CompletableFuture<Void> make_index = searchCommands.ftCreate("idx:users", createArgs, schema)
                    .thenAccept(System.out::println) // >>> OK
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            List<FieldArgs<String>> schema = Arrays.asList(TextFieldArgs.<String> builder().name("$.name").as("name").build(),
                    NumericFieldArgs.<String> builder().name("$.age").as("age").build(),
                    TagFieldArgs.<String> builder().name("$.city").as("city").build());

            CreateArgs<String, String> createArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.JSON)
                    .withPrefix("user:").build();

            Mono<Void> make_index = searchCommands.ftCreate("idx:users", createArgs, schema).doOnNext(res -> {
                System.out.println(res); // >>> OK
            }).then();
```



## Add the data

Add the three sets of user data to the database as
[JSON](https://redis.io/docs/latest/develop/data-types/json) objects.
If you use keys with the `user:` prefix then Redis will index the
objects automatically as you add them:

Foundational: Store JSON documents in Redis using the JSON.SET command with keys matching the index prefix

**Difficulty:** Beginner

**Available in:** Java (Asynchronous - Lettuce), Java (Reactive - Lettuce)

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<String> addUser1 = asyncCommands.jsonSet("user:1", JsonPath.ROOT_PATH, user1).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<String> addUser2 = asyncCommands.jsonSet("user:2", JsonPath.ROOT_PATH, user2).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<String> addUser3 = asyncCommands.jsonSet("user:3", JsonPath.ROOT_PATH, user3).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<String> addUser1 = reactiveCommands.jsonSet("user:1", JsonPath.ROOT_PATH, user1).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<String> addUser2 = reactiveCommands.jsonSet("user:2", JsonPath.ROOT_PATH, user2).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<String> addUser3 = reactiveCommands.jsonSet("user:3", JsonPath.ROOT_PATH, user3).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });
```



## Query the data

You can now use the index to search the JSON objects. The
[query](https://redis.io/docs/latest/develop/ai/search-and-query/query)
below searches for objects that have the text "Paul" in any field
and have an `age` value in the range 30 to 40:

Query data: Execute a full-text search combined with numeric range filtering to find matching documents

**Difficulty:** Intermediate

**Available in:** Java (Asynchronous - Lettuce), Java (Reactive - Lettuce)

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<SearchReply<String, String>> query1 = searchCommands.ftSearch("idx:users", "Paul @age:[30 40]")
                    .thenApply(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> user:3
                        return res;
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<SearchReply<String, String>> query1 = searchCommands.ftSearch("idx:users", "Paul @age:[30 40]")
                    .doOnNext(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> user:3
                    });
```



Specify query options to return only the `city` field:

Restrict query results: Use query options to project specific fields from search results, reducing data transfer

**Difficulty:** Intermediate

**Available in:** Java (Asynchronous - Lettuce), Java (Reactive - Lettuce)

##### Java (Asynchronous - Lettuce)

```java
            SearchArgs<String, String> query2Args = SearchArgs.<String, String> builder().returnField("city").build();
            CompletableFuture<SearchReply<String, String>> query2 = searchCommands.ftSearch("idx:users", "Paul", query2Args)
                    .thenApply(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.printf("ID: %s, City: %s\n", result.getId(), result.getFields().get("city"));
                        });
                        // >>> ID: user:1, City: London
                        // >>> ID: user:3, City: Tel Aviv
                        return res;
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            SearchArgs<String, String> query2Args = SearchArgs.<String, String> builder().returnField("city").build();

            Mono<SearchReply<String, String>> query2 = searchCommands.ftSearch("idx:users", "Paul", query2Args)
                    .doOnNext(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.printf("ID: %s, City: %s\n", result.getId(), result.getFields().get("city"));
                        });
                        // >>> ID: user:1, City: London
                        // >>> ID: user:3, City: Tel Aviv
                    });
```



Use an
[aggregation query](https://redis.io/docs/latest/develop/ai/search-and-query/query/aggregation)
to count all users in each city.

Aggregation: Use aggregation queries to group and count results, performing server-side data analysis

**Difficulty:** Advanced

**Available in:** Java (Asynchronous - Lettuce), Java (Reactive - Lettuce)

##### Java (Asynchronous - Lettuce)

```java
            AggregateArgs<String, String> aggArgs = AggregateArgs.<String, String> builder()
                    .groupBy(GroupBy.<String, String> of("@city").reduce(Reducer.<String, String> count().as("count"))).build();
            CompletableFuture<AggregationReply<String, String>> query3 = searchCommands.ftAggregate("idx:users", "*", aggArgs)
                    .thenApply(res -> {
                        List<SearchReply<String, String>> replies = res.getReplies();
                        replies.forEach(reply -> {
                            reply.getResults().forEach(result -> {
                                System.out.printf("City: %s, Count: %s\n", result.getFields().get("city"),
                                        result.getFields().get("count"));
                            });
                            // >>> City: London, Count: 1
                            // >>> City: Tel Aviv, Count: 2
                        });
                        return res;
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            AggregateArgs<String, String> aggArgs = AggregateArgs.<String, String> builder()
                    .groupBy(GroupBy.<String, String> of("@city").reduce(Reducer.<String, String> count().as("count"))).build();

            Mono<AggregationReply<String, String>> query3 = searchCommands.ftAggregate("idx:users", "*", aggArgs)
                    .doOnNext(res -> {
                        List<SearchReply<String, String>> replies = res.getReplies();
                        replies.forEach(reply -> {
                            reply.getResults().forEach(result -> {
                                System.out.printf("City: %s, Count: %s\n", result.getFields().get("city"),
                                        result.getFields().get("count"));
                            });
                            // >>> City: London, Count: 1
                            // >>> City: Tel Aviv, Count: 2
                        });
                    });
```



## Differences with hash documents

Indexing for hash documents is very similar to JSON indexing but you
need to specify some slightly different options.

When you create the schema for a hash index, you don't need to
add aliases for the fields, since you use the basic names to access
the fields. Also, you must use `CreateArgs.TargetType.HASH` for the `On()`
option of `CreateArgs` when you create the index. The code below shows these
changes with a new index called `hash-idx:users`, which is otherwise the same as
the `idx:users` index used for JSON documents in the previous examples.

Foundational: Create a search index on hash documents with TargetType.HASH configuration

**Difficulty:** Intermediate

**Available in:** Java (Asynchronous - Lettuce), Java (Reactive - Lettuce)

##### Java (Asynchronous - Lettuce)

```java
            List<FieldArgs<String>> hashSchema = Arrays.asList(TextFieldArgs.<String> builder().name("name").build(),
                    NumericFieldArgs.<String> builder().name("age").build(),
                    TagFieldArgs.<String> builder().name("city").build());

            CreateArgs<String, String> hashCreateArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.HASH)
                    .withPrefix("huser:").build();

            CompletableFuture<Void> makeHashIndex = searchCommands.ftCreate("hash-idx:users", hashCreateArgs, hashSchema)
                    .thenAccept(System.out::println) // >>> OK
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            List<FieldArgs<String>> hashSchema = Arrays.asList(TextFieldArgs.<String> builder().name("name").build(),
                    NumericFieldArgs.<String> builder().name("age").build(),
                    TagFieldArgs.<String> builder().name("city").build());

            CreateArgs<String, String> hashCreateArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.HASH)
                    .withPrefix("huser:").build();

            Mono<String> makeHashIndex = searchCommands.ftCreate("hash-idx:users", hashCreateArgs, hashSchema).doOnNext(res -> {
                System.out.println(res); // >>> OK
            });
```



Use [`hset()`](https://redis.io/docs/latest/commands/hset) to add the hash
documents instead of [`jsonSet()`](https://redis.io/docs/latest/commands/json.set).

Foundational: Store hash documents in Redis using HSET command with keys matching the index prefix

**Difficulty:** Beginner

**Available in:** Java (Asynchronous - Lettuce), Java (Reactive - Lettuce)

##### Java (Asynchronous - Lettuce)

```java
            Map<String, String> huser1 = new HashMap<>();
            huser1.put("name", "Paul John");
            huser1.put("email", "paul.john@example.com");
            huser1.put("age", "42");
            huser1.put("city", "London");

            Map<String, String> huser2 = new HashMap<>();
            huser2.put("name", "Eden Zamir");
            huser2.put("email", "eden.zamir@example.com");
            huser2.put("age", "29");
            huser2.put("city", "Tel Aviv");

            Map<String, String> huser3 = new HashMap<>();
            huser3.put("name", "Paul Zamir");
            huser3.put("email", "paul.zamir@example.com");
            huser3.put("age", "35");
            huser3.put("city", "Tel Aviv");

            CompletableFuture<Long> addHashUser1 = asyncCommands.hset("huser:1", huser1).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<Long> addHashUser2 = asyncCommands.hset("huser:2", huser2).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<Long> addHashUser3 = asyncCommands.hset("huser:3", huser3).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Map<String, String> huser1 = new HashMap<>();
            huser1.put("name", "Paul John");
            huser1.put("email", "paul.john@example.com");
            huser1.put("age", "42");
            huser1.put("city", "London");

            Map<String, String> huser2 = new HashMap<>();
            huser2.put("name", "Eden Zamir");
            huser2.put("email", "eden.zamir@example.com");
            huser2.put("age", "29");
            huser2.put("city", "Tel Aviv");

            Map<String, String> huser3 = new HashMap<>();
            huser3.put("name", "Paul Zamir");
            huser3.put("email", "paul.zamir@example.com");
            huser3.put("age", "35");
            huser3.put("city", "Tel Aviv");

            Mono<Long> addHashUser1 = reactiveCommands.hset("huser:1", huser1).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<Long> addHashUser2 = reactiveCommands.hset("huser:2", huser2).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<Long> addHashUser3 = reactiveCommands.hset("huser:3", huser3).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });
```



The query commands work the same here for hash as they do for JSON (but
the name of the hash index is different). The results are returned in
a `List` of `SearchReply.SearchResult<String, String>` objects, as with JSON:

Query data: Execute the same search query on hash documents as you would on JSON documents

**Difficulty:** Intermediate

**Available in:** Java (Asynchronous - Lettuce), Java (Reactive - Lettuce)

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<SearchReply<String, String>> query1Hash = searchCommands
                    .ftSearch("hash-idx:users", "Paul @age:[30 40]").thenApply(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> huser:3
                        return res;
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<SearchReply<String, String>> query1Hash = searchCommands.ftSearch("hash-idx:users", "Paul @age:[30 40]")
                    .doOnNext(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> huser:3
                    });
```



## More information

See the [Redis Search](https://redis.io/docs/latest/develop/ai/search-and-query) docs
for a full description of all query features with examples.

