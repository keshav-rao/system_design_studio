# Jedis guide (Java)

```json metadata
{
  "schema_version": 2,
  "title": "Jedis guide (Java)",
  "description": "Connect your Java application to a Redis database",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"install","title":"Install"},{"id":"connect-and-test","title":"Connect and test"},{"id":"more-information","title":"More information"}]}

,
  "codeExamples": [{"codetabsId":"landing-stepimport","description":"Foundational: Import required Jedis classes for Redis client functionality","difficulty":"beginner","id":"import","languages":[{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_landing-stepimport"}]},{"codetabsId":"landing-stepconnect","description":"Foundational: Connect to a Redis server and establish a client connection","difficulty":"beginner","id":"connect","languages":[{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_landing-stepconnect"}]},{"codetabsId":"landing-stepset_get_string","description":"Foundational: Set and retrieve string values using SET and GET commands","difficulty":"beginner","id":"set_get_string","languages":[{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_landing-stepset_get_string"}]},{"codetabsId":"landing-stepset_get_hash","description":"Foundational: Store and retrieve hash data structures using HSET and HGETALL","difficulty":"beginner","id":"set_get_hash","languages":[{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_landing-stepset_get_hash"}]},{"codetabsId":"landing-stepclose","description":"Foundational: Properly close a Redis client connection to release resources","difficulty":"beginner","id":"close","languages":[{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_landing-stepclose"}]}]
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


[Jedis](https://github.com/redis/jedis) is a synchronous Java client for Redis.
Use [Lettuce](https://redis.io/docs/latest/develop/clients/lettuce) if you need
a more advanced Java client that also supports asynchronous and reactive connections.
The sections below explain how to install `Jedis` and connect your application
to a Redis database.

> [!NOTE]
> Jedis 7.2.0 introduced a new client connection API:
>
> | New API class | Replaces | Use case |
> | :-- | :-- | :-- |
> | `RedisClient` | `UnifiedJedis`, `JedisPool`, `JedisPooled` | Single connection (with connection pooling) |
> | `RedisClusterClient` | `JedisCluster` | Redis Cluster connections |
> | `RedisSentinelClient` | `JedisSentinelPool` | Redis Sentinel connections |
>
> The old client classes are now considered deprecated.

`Jedis` requires a running Redis server. See [here](https://redis.io/docs/latest/operate/oss_and_stack/install) for Redis Open Source installation instructions.

## Install

To include `Jedis` as a dependency in your application, edit the dependency file, as follows.

* If you use **Maven**:   

  ```xml
  <dependency>
      <groupId>redis.clients</groupId>
      <artifactId>jedis</artifactId>
      <version>7.2.0</version>
  </dependency>
  ```

* If you use **Gradle**: 

  ```
  repositories {
      mavenCentral()
  }
  //...
  dependencies {
      implementation 'redis.clients:jedis:7.2.0'
      //...
  }
  ```

* If you use the JAR files, download the latest Jedis and Apache Commons Pool2 JAR files from [Maven Central](https://central.sonatype.com/) or any other Maven repository.

* Build from [source](https://github.com/redis/jedis)


## Connect and test

Add the following imports to your source file:

Foundational: Import required Jedis classes for Redis client functionality

**Difficulty:** Beginner

**Available in:** Java (Synchronous - Jedis)

##### Java (Synchronous - Jedis)

```java
import redis.clients.jedis.RedisClient;
import java.util.HashMap;
import java.util.Map;
```



Connect to localhost on port 6379:

Foundational: Connect to a Redis server and establish a client connection

**Difficulty:** Beginner

**Available in:** Java (Synchronous - Jedis)

##### Java (Synchronous - Jedis)

```java
        RedisClient jedis = new RedisClient("redis://localhost:6379");
```



After you have connected, you can check the connection by storing and
retrieving a simple [string](https://redis.io/docs/latest/develop/data-types/strings) value:

Foundational: Set and retrieve string values using SET and GET commands

**Difficulty:** Beginner

**Available in:** Java (Synchronous - Jedis)

##### Java (Synchronous - Jedis)

```java
        String res1 = jedis.set("bike:1", "Deimos");
        System.out.println(res1); // >>> OK

        String res2 = jedis.get("bike:1");
        System.out.println(res2); // >>> Deimos
```



Store and retrieve a [hash](https://redis.io/docs/latest/develop/data-types/hashes):

Foundational: Store and retrieve hash data structures using HSET and HGETALL

**Difficulty:** Beginner

**Available in:** Java (Synchronous - Jedis)

##### Java (Synchronous - Jedis)

```java
        Map<String, String> hash = new HashMap<>();
        hash.put("name", "John");
        hash.put("surname", "Smith");
        hash.put("company", "Redis");
        hash.put("age", "29");

        Long res3 = jedis.hset("user-session:123", hash);
        System.out.println(res3); // >>> 4

        Map<String, String> res4 = jedis.hgetAll("user-session:123");
        System.out.println(res4);
        // >>> {name=John, surname=Smith, company=Redis, age=29}
```



Close the connection when you're done:

Foundational: Properly close a Redis client connection to release resources

**Difficulty:** Beginner

**Available in:** Java (Synchronous - Jedis)

##### Java (Synchronous - Jedis)

```java
        jedis.close();
```



## More information

`Jedis` has a complete [API reference](https://www.javadoc.io/doc/redis.clients/jedis/latest/index.html) available on [javadoc.io/](https://javadoc.io/).
The `Jedis` [GitHub repository](https://github.com/redis/jedis) also has useful docs
and examples including a page about handling
[failover with Jedis](https://github.com/redis/jedis/blob/master/docs/failover.md)

See also the other pages in this section for more information and examples:

