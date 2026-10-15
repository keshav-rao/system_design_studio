# FLUSHALL

```json metadata
{
  "schema_version": 2,
  "title": "FLUSHALL",
  "description": "Removes all keys from all databases.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"arguments":[{"display_text":"async","name":"async","since":"4.0.0","token":"ASYNC","type":"pure-token"},{"display_text":"sync","name":"sync","since":"6.2.0","token":"SYNC","type":"pure-token"}],"name":"flush-type","optional":true,"type":"oneof"}],
  "syntax_fmt": "FLUSHALL [ASYNC | SYNC]",
  "complexity": "O(N) where N is the total number of keys in all databases",
  "group": "server",
  "command_flags": ["write"],
  "acl_categories": ["@keyspace","@write","@slow","@dangerous"],
  "since": "1.0.0",
  "arity": -1,
  "tableOfContents": {"sections":[{"id":"optional-arguments","title":"Optional arguments"},{"id":"details","title":"Details"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": [{"codetabsId":"cmds_servermgmt-stepflushall","description":"Full delete: Delete all keys from all databases using FLUSHALL (dangerous operation, supports ASYNC/SYNC modes, clears RDB file)","difficulty":"advanced","id":"flushall","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_cmds_servermgmt-stepflushall"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_cmds_servermgmt-stepflushall"},{"id":"Node-js","panelId":"panel_Nodejs_cmds_servermgmt-stepflushall"},{"clientId":"ioredis","clientName":"ioredis","id":"ioredis","langId":"javascript","panelId":"panel_ioredis_cmds_servermgmt-stepflushall"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_cmds_servermgmt-stepflushall"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_cmds_servermgmt-stepflushall"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_cmds_servermgmt-stepflushall"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_cmds_servermgmt-stepflushall"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_cmds_servermgmt-stepflushall"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_cmds_servermgmt-stepflushall"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_cmds_servermgmt-stepflushall"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_cmds_servermgmt-stepflushall"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_cmds_servermgmt-stepflushall"}]}]
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


Delete all the keys of all the existing databases, not just the currently selected one.
This command never fails.

By default, `FLUSHALL` will synchronously flush all the databases.
Starting with Redis 6.2, setting the `lazyfree-lazy-user-flush` configuration directive to `yes` changes the default flush mode to asynchronous.

Full delete: Delete all keys from all databases using FLUSHALL (dangerous operation, supports ASYNC/SYNC modes, clears RDB file)

**Difficulty:** Advanced

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
FLUSHALL SYNC
```

##### C#

```csharp
        server.FlushAllDatabases();

        var res2 = server.Keys(pattern: "*").ToArray();
        Console.WriteLine(res2.Length); // >>> 0
```

##### Go

```go
	flushAllResult1, err := rdb.FlushAll(ctx).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(flushAllResult1) // >>> OK

	flushAllResult2, err := rdb.Keys(ctx, "*").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(flushAllResult2) // >>> []
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> flushallExample = asyncCommands.flushall()
                    .thenCompose(res1 -> {
                        System.out.println(res1); // >>> OK
                        return asyncCommands.keys("*");
                    }).thenAccept(res2 -> {
                        System.out.println(res2); // >>> []
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> flushallExample = reactiveCommands.flushall()
                    .doOnNext(res1 -> {
                        System.out.println(res1); // >>> OK
                    })
                    .then(reactiveCommands.keys("*").collectList())
                    .doOnNext(res2 -> {
                        System.out.println(res2); // >>> []
                    })
                    .then();
```

##### Java (Synchronous - Jedis)

```java
        String flushAllResult1 = jedis.flushAll();
        System.out.println(flushAllResult1); // >>> OK

        Set<String> flushAllResult2 = jedis.keys("*");
        System.out.println(flushAllResult2); // >>> []
```

##### JavaScript (Node.js)

```javascript
const res1 = await client.flushAll('SYNC'); // or ASYNC
console.log(res1); // OK

const res2 = await client.keys('*');
console.log(res2); // []

```

##### JavaScript (Node.js)

```javascript
const res1 = await redis.flushall(); // or flushall('ASYNC')
console.log(res1); // >>> OK

const res2 = await redis.keys('*');
console.log(res2); // >>> []
```

##### JavaScript (Node.js)

```javascript
const res1 = await client.flushAll('SYNC'); // or ASYNC
console.log(res1); // OK

const res2 = await client.keys('*');
console.log(res2); // []

```

##### JavaScript (Node.js)

```javascript
const res1 = await redis.flushall(); // or flushall('ASYNC')
console.log(res1); // >>> OK

const res2 = await redis.keys('*');
console.log(res2); // >>> []
```

##### PHP

```php
        $res1 = $r->flushall();
        echo $res1 . PHP_EOL; // >>> OK

        $res2 = $r->keys('*');
        echo json_encode($res2) . PHP_EOL; // >>> []
```

##### Python

```python
res1 = r.flushall(asynchronous=False)
print(res1) # >>> True

res2 = r.keys()
print(res2) # >>> []

```

##### Ruby

```ruby
res1 = r.flushall # or r.flushall(async: true)
puts res1 # >>> OK

res2 = r.keys('*')
puts res2.inspect # >>> []
```

##### Rust (Asynchronous)

```rust
        let _: () = r.flushall().await.expect("Failed to flushall");

        match r.keys("*").await {
            Ok(res2) => {
                let res2: Vec<String> = res2;
                println!("{res2:?}"); // >>> []
            }
            Err(e) => println!("Error getting keys: {e}"),
        }
```

##### Rust (Synchronous)

```rust
        let _: () = r.flushall().expect("Failed to flushall");

        match r.keys("*") {
            Ok(res2) => {
                let res2: Vec<String> = res2;
                println!("{res2:?}"); // >>> []
            }
            Err(e) => println!("Error getting keys: {e}"),
        }
```



## Optional arguments

<details open><summary><code>ASYNC | SYNC</code></summary>

Flush asynchronously (`ASYNC`) or synchronously (`SYNC`). The default is set by the `lazyfree-lazy-user-flush` configuration directive.

</details>

## Details

* An asynchronous `FLUSHALL` command only deletes keys that were present at the time the command was invoked. Keys created during an asynchronous flush will be unaffected.
* This command does not delete functions.
* Other than emptying all databases (similar to `FLUSHDB`), this command clears the RDB persistence file, aborts any snapshot that is in progress, and, if the `save` config is enabled, saves an empty RDB file.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active\*</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | \*Can use the [Active-Active flush API request](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/crdbs/flush). |

## Return information

**RESP2:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.

**RESP3:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.



