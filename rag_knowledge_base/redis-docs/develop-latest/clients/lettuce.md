# Lettuce guide (Java)

```json metadata
{
  "schema_version": 2,
  "title": "Lettuce guide (Java)",
  "description": "Connect your Lettuce application to a Redis database",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"install","title":"Install"},{"id":"connect-and-test","title":"Connect and test"},{"id":"more-information","title":"More information"}]}

,
  "codeExamples": [{"codetabsId":"landing-stepimport","description":"Foundational: Import required Lettuce classes for synchronous Redis connections","difficulty":"beginner","id":"import","languages":[{"clientId":"lettuce","clientName":"Lettuce","id":"Lettuce-Sync","langId":"java","panelId":"panel_Lettuce-Sync_landing-stepimport"}]},{"codetabsId":"landing-stepconnect","description":"Foundational: Establish a synchronous connection to a Redis server using Lettuce","difficulty":"beginner","id":"connect","languages":[{"clientId":"lettuce","clientName":"Lettuce","id":"Lettuce-Sync","langId":"java","panelId":"panel_Lettuce-Sync_landing-stepconnect"}]},{"codetabsId":"landing-stepset_get_string","description":"Foundational: Set and retrieve string values using SET and GET commands to verify the connection works","difficulty":"beginner","id":"set_get_string","languages":[{"clientId":"lettuce","clientName":"Lettuce","id":"Lettuce-Sync","langId":"java","panelId":"panel_Lettuce-Sync_landing-stepset_get_string"}]},{"codetabsId":"landing-stepclose","description":"Foundational: Properly close the Lettuce connection to release resources","difficulty":"beginner","id":"close","languages":[{"clientId":"lettuce","clientName":"Lettuce","id":"Lettuce-Sync","langId":"java","panelId":"panel_Lettuce-Sync_landing-stepclose"}]}]
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


[Lettuce](https://github.com/redis/lettuce/tree/main/src/main) is an advanced Java client for Redis
that supports synchronous, asynchronous, and reactive connections.
If you only need synchronous connections then you may find the other Java client
[Jedis](https://redis.io/docs/latest/develop/clients/jedis) easier to use.

The sections below explain how to install `Lettuce` and connect your application
to a Redis database.

`Lettuce` requires a running Redis server. See [here](https://redis.io/docs/latest/operate/oss_and_stack/install) for Redis Open Source installation instructions.

## Install

To include Lettuce as a dependency in your application, edit the appropriate dependency file as shown below.

If you use Maven, add the following dependency to your `pom.xml`:

```xml
<dependency>
    <groupId>io.lettuce</groupId>
    <artifactId>lettuce-core</artifactId>
    <version>6.7.1.RELEASE</version> <!-- Check for the latest version on Maven Central -->
</dependency>
```

If you use Gradle, include this line in your `build.gradle` file:

```
dependencies {
    compileOnly 'io.lettuce:lettuce-core:6.7.1.RELEASE'
}
```

If you wish to use the JAR files directly, download the latest Lettuce and, optionally, Apache Commons Pool2 JAR files from Maven Central or any other Maven repository.

To build from source, see the instructions on the [Lettuce source code GitHub repo](https://github.com/lettuce-io/lettuce-core).

## Connect and test

Connect to a local server using the following code. First, import
the required classes.

Foundational: Import required Lettuce classes for synchronous Redis connections

**Difficulty:** Beginner

**Available in:** Java

##### Java

```java
import io.lettuce.core.*;
import io.lettuce.core.api.StatefulRedisConnection;
import io.lettuce.core.api.sync.RedisCommands;
```



Use the following code to connect to the server.

Foundational: Establish a synchronous connection to a Redis server using Lettuce

**Difficulty:** Beginner

**Available in:** Java

##### Java

```java
        RedisURI uri = RedisURI.Builder
                .redis("localhost", 6379)
                .build();

        RedisClient client = RedisClient.create(uri);
        StatefulRedisConnection<String, String> connection = client.connect();
        RedisCommands<String, String> commands = connection.sync();
```



Test the connection by storing and retrieving a simple string.

Foundational: Set and retrieve string values using SET and GET commands to verify the connection works

**Difficulty:** Beginner

**Available in:** Java

##### Java

```java
        commands.set("foo", "bar");
        String result = commands.get("foo");
        System.out.println(result); // >>> bar
```



Close the connection when you're done.

Foundational: Properly close the Lettuce connection to release resources

**Difficulty:** Beginner

**Available in:** Java

##### Java

```java
        connection.close();
        client.shutdown();
```



## More information

The [Lettuce reference guide](https://redis.github.io/lettuce/) has more examples
and an API reference. You may also be interested in the
[Project Reactor](https://projectreactor.io/) library that Lettuce uses.

See also the other pages in this section for more information and examples:

