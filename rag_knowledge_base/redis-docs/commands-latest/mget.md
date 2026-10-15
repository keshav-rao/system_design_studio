# MGET

```json metadata
{
  "schema_version": 2,
  "title": "MGET",
  "description": "Atomically returns the string values of one or more keys.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"multiple":true,"name":"key","type":"key"}],
  "syntax_fmt": "MGET key [key ...]",
  "complexity": "O(N) where N is the number of keys to retrieve.",
  "group": "string",
  "command_flags": ["readonly","fast"],
  "acl_categories": ["@read","@string","@fast"],
  "since": "1.0.0",
  "arity": -2,
  "key_specs": [{"RO":true,"access":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":-1,"limit":0},"type":"range"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": [{"codetabsId":"cmds_string-stepmget","commands":[{"acl_categories":["@write","@string","@slow"],"complexity":"O(1)","name":"SET"},{"acl_categories":["@read","@string","@fast"],"complexity":"O(N)","name":"MGET"}],"description":"Returns the values of all specified keys.","difficulty":"beginner","id":"mget","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_cmds_string-stepmget"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_cmds_string-stepmget"},{"id":"Node-js","panelId":"panel_Nodejs_cmds_string-stepmget"},{"clientId":"ioredis","clientName":"ioredis","id":"ioredis","langId":"javascript","panelId":"panel_ioredis_cmds_string-stepmget"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_cmds_string-stepmget"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_cmds_string-stepmget"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_cmds_string-stepmget"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_cmds_string-stepmget"},{"clientId":"hiredis","clientName":"hiredis","id":"C","langId":"c","panelId":"panel_C_cmds_string-stepmget"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_cmds_string-stepmget"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_cmds_string-stepmget"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_cmds_string-stepmget"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_cmds_string-stepmget"}]}]
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

> [!NOTE]
> This command's behavior varies in clustered Redis environments. See the [multi-key operations](https://redis.io/docs/latest/develop/using-commands/multi-key-operations) page for more information.

Returns the values of all specified keys.
For every key that does not hold a string value or does not exist, `nil` is returned.
Because of this, the operation never fails.

## Required arguments

<details open><summary><code>key [key ...]</code></summary>

One or more keys whose values to retrieve.

</details>

## Examples

Returns the values of all specified keys.

**Difficulty:** Beginner

**Commands:** SET, MGET

**Complexity:**
- SET: O(1)
- MGET: O(N)

**Available in:** Redis CLI, C, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), JavaScript (Node.js), PHP, Python, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> SET key1 "Hello"
OK
> SET key2 "World"
OK
> MGET key1 key2 nonexisting
1) "Hello"
2) "World"
3) (nil)
```

##### C

```c
    redisReply *reply = redisCommand(c, "SET key1 Hello");
    freeReplyObject(reply);

    reply = redisCommand(c, "SET key2 World");
    freeReplyObject(reply);

    reply = redisCommand(c, "MGET key1 key2 nonexisting");

    for (size_t i = 0; i < reply->elements; i++) {
        if (i > 0) {
            printf(", ");
        }

        if (reply->element[i]->type == REDIS_REPLY_NIL) {
            printf("null");
        } else {
            printf("%s", reply->element[i]->str);
        }
    }
    printf("\n");
    // >>> Hello, World, null
```

##### C#

```csharp
        bool mgetResult1 = db.StringSet("key1", "Hello");
        bool mgetResult2 = db.StringSet("key2", "World");

        RedisValue[] mgetResult3 = db.StringGet(new RedisKey[] { "key1", "key2", "nonexisting" });
        Console.WriteLine(string.Join(", ", mgetResult3.Select(v => v.IsNull ? "null" : v.ToString())));
        // >>> Hello, World, null

```

##### Go

```go
	if err := rdb.Set(ctx, "key1", "Hello", 0).Err(); err != nil {
		panic(err)
	}

	if err := rdb.Set(ctx, "key2", "World", 0).Err(); err != nil {
		panic(err)
	}

	mgetResult, err := rdb.MGet(ctx, "key1", "key2", "nonexisting").Result()
	if err != nil {
		panic(err)
	}

	fmt.Println(mgetResult) // >>> [Hello World <nil>]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> mgetExample = asyncCommands.set("key1", "Hello")
                    .thenCompose(res1 -> asyncCommands.set("key2", "World"))
                    .thenCompose(res2 -> asyncCommands.mget("key1", "key2", "nonexisting"))
                    .thenAccept(res3 -> {
                        System.out.println(res3);
                        // >>> [KeyValue[key1, Hello], KeyValue[key2, World], KeyValue[nonexisting].empty]
                    })
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> mgetExample = reactiveCommands.set("key1", "Hello")
                    .flatMap(res1 -> reactiveCommands.set("key2", "World"))
                    .flatMap(res2 -> reactiveCommands.mget("key1", "key2", "nonexisting").collectList())
                    .doOnNext(res3 -> {
                        System.out.println(res3);
                        // >>> [KeyValue[key1, Hello], KeyValue[key2, World], KeyValue[nonexisting].empty]
                    })
                    .then();
```

##### Java (Synchronous - Jedis)

```java
        String mgetResult1 = jedis.set("key1", "Hello");
        System.out.println(mgetResult1);    // >>> OK

        String mgetResult2 = jedis.set("key2", "World");
        System.out.println(mgetResult2);    // >>> OK

        java.util.List<String> mgetResult3 = jedis.mget("key1", "key2", "nonexisting");
        System.out.println(mgetResult3);    // >>> [Hello, World, null]
```

##### JavaScript (Node.js)

```javascript
await client.set('key1', 'Hello');
await client.set('key2', 'World');

const mgetResult = await client.mGet(['key1', 'key2', 'nonexisting']);
console.log(mgetResult); // >>> [ 'Hello', 'World', null ]
```

##### JavaScript (Node.js)

```javascript
await redis.set('key1', 'Hello');
await redis.set('key2', 'World');

const mgetResult = await redis.mget('key1', 'key2', 'nonexisting');
console.log(mgetResult); // >>> ['Hello', 'World', null]
```

##### JavaScript (Node.js)

```javascript
await client.set('key1', 'Hello');
await client.set('key2', 'World');

const mgetResult = await client.mGet(['key1', 'key2', 'nonexisting']);
console.log(mgetResult); // >>> [ 'Hello', 'World', null ]
```

##### JavaScript (Node.js)

```javascript
await redis.set('key1', 'Hello');
await redis.set('key2', 'World');

const mgetResult = await redis.mget('key1', 'key2', 'nonexisting');
console.log(mgetResult); // >>> ['Hello', 'World', null]
```

##### PHP

```php
        $r->set('key1', 'Hello');
        $r->set('key2', 'World');

        $mgetResult = $r->mget(['key1', 'key2', 'nonexisting']);
        echo json_encode($mgetResult) . PHP_EOL; // >>> ["Hello","World",null]
```

##### Python

```python
r.set("key1", "Hello")
r.set("key2", "World")

mget_result = r.mget("key1", "key2", "nonexisting")
print(mget_result)
# >>> ['Hello', 'World', None]
```

##### Rust (Asynchronous)

```rust
        if let Ok(res) = r.set("key1", "Hello").await {
            let _: String = res;
        }

        if let Ok(res) = r.set("key2", "World").await {
            let _: String = res;
        }

        match r.mget(&["key1", "key2", "nonexisting"]).await {
            Ok(mget_result) => {
                let mget_result: Vec<Option<String>> = mget_result;
                println!("{mget_result:?}");    // >>> [Some("Hello"), Some("World"), None]
            }
            Err(e) => {
                println!("Error getting values: {e}");
            }
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.set("key1", "Hello") {
            let _: String = res;
        }

        if let Ok(res) = r.set("key2", "World") {
            let _: String = res;
        }

        match r.mget(&["key1", "key2", "nonexisting"]) {
            Ok(mget_result) => {
                let mget_result: Vec<Option<String>> = mget_result;
                println!("{mget_result:?}");    // >>> [Some("Hello"), Some("World"), None]
            }
            Err(e) => {
                println!("Error getting values: {e}");
            }
        }
```



## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Array reply](../../develop/reference/protocol-spec#arrays): a list of values at the specified keys.

**RESP3:**

[Array reply](../../develop/reference/protocol-spec#arrays): a list of values at the specified keys.



