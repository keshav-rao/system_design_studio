# DEL

```json metadata
{
  "schema_version": 2,
  "title": "DEL",
  "description": "Deletes one or more keys.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"multiple":true,"name":"key","type":"key"}],
  "syntax_fmt": "DEL key [key ...]",
  "complexity": "O(N) where N is the number of keys that will be removed. When a key to remove holds a value other than a string, the individual complexity for this key is O(M) where M is the number of elements in the list, set, sorted set or hash. Removing a single key that holds a string value is O(1).",
  "group": "generic",
  "command_flags": ["write"],
  "acl_categories": ["@keyspace","@write","@slow"],
  "since": "1.0.0",
  "arity": -2,
  "key_specs": [{"RM":true,"begin_search":{"spec":{"index":1},"type":"index"},"delete":true,"find_keys":{"spec":{"keystep":1,"lastkey":-1,"limit":0},"type":"range"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": [{"codetabsId":"cmds_generic-stepdel","commands":[{"acl_categories":["@write","@string","@slow"],"complexity":"O(1)","name":"SET"},{"acl_categories":["@keyspace","@write","@slow"],"complexity":"O(N)","name":"DEL"}],"description":"Foundational: Delete one or more keys using DEL (ignores non-existent keys, returns count of deleted keys)","difficulty":"beginner","id":"del","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_cmds_generic-stepdel"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_cmds_generic-stepdel"},{"id":"Node-js","panelId":"panel_Nodejs_cmds_generic-stepdel"},{"clientId":"ioredis","clientName":"ioredis","id":"ioredis","langId":"javascript","panelId":"panel_ioredis_cmds_generic-stepdel"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_cmds_generic-stepdel"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_cmds_generic-stepdel"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_cmds_generic-stepdel"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_cmds_generic-stepdel"},{"clientId":"hiredis","clientName":"hiredis","id":"C","langId":"c","panelId":"panel_C_cmds_generic-stepdel"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_cmds_generic-stepdel"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_cmds_generic-stepdel"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_cmds_generic-stepdel"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_cmds_generic-stepdel"}]}]
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


Removes the specified keys.
A key is ignored if it does not exist.

## Required arguments

<details open><summary><code>key [key ...]</code></summary>

One or more keys to delete.

</details>

## Examples

Foundational: Delete one or more keys using DEL (ignores non-existent keys, returns count of deleted keys)

**Difficulty:** Beginner

**Commands:** SET, DEL

**Complexity:**
- SET: O(1)
- DEL: O(N)

**Available in:** Redis CLI, C, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), JavaScript (Node.js), PHP, Python, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> SET key1 "Hello"
OK
> SET key2 "World"
OK
> DEL key1 key2 key3
(integer) 2
```

##### C

```c
    reply = redisCommand(c, "SET key1 Hello");
    printf("%s\n", reply->str);
    // >>> OK
    freeReplyObject(reply);

    reply = redisCommand(c, "SET key2 World");
    printf("%s\n", reply->str);
    // >>> OK
    freeReplyObject(reply);

    reply = redisCommand(c, "DEL key1 key2 key3");
    printf("%lld\n", reply->integer);
    // >>> 2
    freeReplyObject(reply);
```

##### C#

```csharp
        bool delResult1 = db.StringSet("key1", "Hello");
        Console.WriteLine(delResult1);  // >>> true

        bool delResult2 = db.StringSet("key2", "World");
        Console.WriteLine(delResult2);  // >>> true

        long delResult3 = db.KeyDelete(["key1", "key2", "key3"]);
        Console.WriteLine(delResult3);  // >>> 2
```

##### Go

```go
	delResult1, err := rdb.Set(ctx, "key1", "Hello", 0).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(delResult1) // >>> OK

	delResult2, err := rdb.Set(ctx, "key2", "World", 0).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(delResult2) // >>> OK

	delResult3, err := rdb.Del(ctx, "key1", "key2", "key3").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(delResult3) // >>> 2
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> delExample = asyncCommands.set("key1", "Hello")
                    .thenCompose(r1 -> {
                        System.out.println(r1);              // >>> OK
                        return asyncCommands.set("key2", "World");
                    })
                    .thenCompose(r2 -> {
                        System.out.println(r2);              // >>> OK
                        return asyncCommands.del("key1", "key2", "key3");
                    })
                    .thenAccept(r3 -> {
                        System.out.println(r3);              // >>> 2
                    })
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> delExample = reactiveCommands.set("key1", "Hello")
                    .flatMap(r1 -> {
                        System.out.println(r1);              // >>> OK
                        return reactiveCommands.set("key2", "World");
                    })
                    .flatMap(r2 -> {
                        System.out.println(r2);              // >>> OK
                        return reactiveCommands.del("key1", "key2", "key3");
                    })
                    .doOnNext(r3 -> {
                        System.out.println(r3);              // >>> 2
                    })
                    .then();
```

##### Java (Synchronous - Jedis)

```java
        String delResult1 = jedis.set("key1", "Hello");
        System.out.println(delResult1); // >>> OK

        String delResult2 = jedis.set("key2", "World");
        System.out.println(delResult2); // >>> OK

        long delResult3 = jedis.del("key1", "key2", "key3");
        System.out.println(delResult3); // >>> 2
```

##### JavaScript (Node.js)

```javascript
const delRes1 = await client.set('key1', 'Hello');
console.log(delRes1); // OK

const delRes2 = await client.set('key2', 'World');
console.log(delRes2); // OK

const delRes3 = await client.del(['key1', 'key2', 'key3']);
console.log(delRes3); // 2
```

##### JavaScript (Node.js)

```javascript
console.log(await redis.set('key1', 'Hello')); // >>> OK
console.log(await redis.set('key2', 'World')); // >>> OK

const delResult = await redis.del('key1', 'key2', 'key3');
console.log(delResult); // >>> 2
```

##### JavaScript (Node.js)

```javascript
const delRes1 = await client.set('key1', 'Hello');
console.log(delRes1); // OK

const delRes2 = await client.set('key2', 'World');
console.log(delRes2); // OK

const delRes3 = await client.del(['key1', 'key2', 'key3']);
console.log(delRes3); // 2
```

##### JavaScript (Node.js)

```javascript
console.log(await redis.set('key1', 'Hello')); // >>> OK
console.log(await redis.set('key2', 'World')); // >>> OK

const delResult = await redis.del('key1', 'key2', 'key3');
console.log(delResult); // >>> 2
```

##### PHP

```php
        echo $r->set('key1', 'Hello') . PHP_EOL;             // >>> OK
        echo $r->set('key2', 'World') . PHP_EOL;             // >>> OK

        $delResult = $r->del('key1', 'key2', 'key3');
        echo $delResult . PHP_EOL;                           // >>> 2
```

##### Python

```python
res = r.set("key1", "Hello")
print(res)
# >>> True

res = r.set("key2", "World")
print(res)
# >>> True

res = r.delete("key1", "key2", "key3")
print(res)
# >>> 2
```

##### Rust (Asynchronous)

```rust
        if let Ok(res) = r.set("key1", "Hello").await {
            let res: String = res;
            println!("{res}");    // >>> OK
        }

        if let Ok(res) = r.set("key2", "World").await {
            let res: String = res;
            println!("{res}");    // >>> OK
        }

        match r.del(&["key1", "key2", "key3"]).await {
            Ok(res) => {
                let res: i32 = res;
                println!("{res}");    // >>> 2
            },
            Err(e) => {
                println!("Error deleting keys: {e}");
                return;
            }
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.set("key1", "Hello") {
            let res: String = res;
            println!("{res}");    // >>> OK
        }

        if let Ok(res) = r.set("key2", "World") {
            let res: String = res;
            println!("{res}");    // >>> OK
        }

        match r.del(&["key1", "key2", "key3"]) {
            Ok(res) => {
                let res: i32 = res;
                println!("{res}");    // >>> 2
            },
            Err(e) => {
                println!("Error deleting keys: {e}");
                return;
            }
        }
```



## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Integer reply](../../develop/reference/protocol-spec#integers): the number of keys that were removed.

**RESP3:**

[Integer reply](../../develop/reference/protocol-spec#integers): the number of keys that were removed.



