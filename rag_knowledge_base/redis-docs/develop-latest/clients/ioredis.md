# ioredis guide (JavaScript)

```json metadata
{
  "schema_version": 2,
  "title": "ioredis guide (JavaScript)",
  "description": "Connect your Node.js/JavaScript application to a Redis database",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"install","title":"Install"},{"id":"connect-and-test","title":"Connect and test"},{"id":"more-information","title":"More information"}]}

,
  "codeExamples": [{"codetabsId":"landing-stepconnect","difficulty":"beginner","id":"connect","languages":[{"clientId":"ioredis","clientName":"ioredis","id":"ioredis","langId":"javascript","panelId":"panel_ioredis_landing-stepconnect"}]},{"codetabsId":"landing-stepset_get_string","difficulty":"beginner","id":"set_get_string","languages":[{"clientId":"ioredis","clientName":"ioredis","id":"ioredis","langId":"javascript","panelId":"panel_ioredis_landing-stepset_get_string"}]},{"codetabsId":"landing-stepset_get_hash","difficulty":"beginner","id":"set_get_hash","languages":[{"clientId":"ioredis","clientName":"ioredis","id":"ioredis","langId":"javascript","panelId":"panel_ioredis_landing-stepset_get_hash"}]},{"codetabsId":"landing-stepclose","difficulty":"beginner","id":"close","languages":[{"clientId":"ioredis","clientName":"ioredis","id":"ioredis","langId":"javascript","panelId":"panel_ioredis_landing-stepclose"}]}]
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


[`ioredis`](https://github.com/redis/ioredis) is a Redis client for Node.js/JavaScript.
The sections below explain how to install `ioredis` and connect your application
to a Redis database.

> [!NOTE]
> Redis actively maintains and supports `ioredis` since it is in widespread use, but
> for new projects, we recommend using our newer Node.js client
> [`node-redis`](https://redis.io/docs/latest/develop/clients/nodejs). See
> [Migrate from ioredis](https://redis.io/docs/latest/develop/clients/nodejs/migration)
> if you are interested in converting an existing `ioredis` project to `node-redis`.

`ioredis` requires a running Redis server. See [here](https://redis.io/docs/latest/operate/oss_and_stack/install) for Redis Open Source installation instructions.

## Install

To install `ioredis`, run:

```bash
npm install ioredis
```

## Connect and test

Connect to localhost on port 6379. 

**Available in:** JavaScript (Node.js)

##### JavaScript (Node.js)

```javascript
import { Redis } from 'ioredis';

const redis = new Redis();
```



Store and retrieve a simple string.

**Available in:** JavaScript (Node.js)

##### JavaScript (Node.js)

```javascript
await redis.set('key', 'value');
const value = await redis.get('key');
console.log(value); // >>> value
```



Store and retrieve a map.

**Available in:** JavaScript (Node.js)

##### JavaScript (Node.js)

```javascript
await redis.hset('user-session:123', {
    name: 'John',
    surname: 'Smith',
    company: 'Redis',
    age: 29
});

const userSession = await redis.hgetall('user-session:123');
console.log(JSON.stringify(userSession, null, 2));
/* >>>
{
  "surname": "Smith",
  "name": "John",
  "company": "Redis",
  "age": "29"
}
 */
```



When you have finished using a connection, close it with `client.quit()`.

**Available in:** JavaScript (Node.js)

##### JavaScript (Node.js)

```javascript
redis.disconnect();
```



## More information

The [Github repository](https://github.com/redis/ioredis) has useful
information, including [API docs](https://redis.github.io/ioredis/index.html)
and a set of [code examples](https://github.com/redis/ioredis/tree/main/examples).

