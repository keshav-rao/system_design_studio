# HLEN

```json metadata
{
  "schema_version": 2,
  "title": "HLEN",
  "description": "Returns the number of fields in a hash.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"}],
  "syntax_fmt": "HLEN key",
  "complexity": "O(1)",
  "group": "hash",
  "command_flags": ["readonly","fast"],
  "acl_categories": ["@read","@hash","@fast"],
  "since": "2.0.0",
  "arity": 2,
  "key_specs": [{"RO":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": [{"codetabsId":"cmds_hash-stephlen","commands":[{"acl_categories":["@write","@hash","@fast"],"complexity":"O(1)","name":"HSET"},{"acl_categories":["@read","@hash","@fast"],"complexity":"O(1)","name":"HLEN"}],"description":"Foundational: Count the fields in a hash with HLEN when you need a hash\u0026amp;#39;s size without transferring its contents","difficulty":"beginner","id":"hlen","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_cmds_hash-stephlen"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_cmds_hash-stephlen"},{"id":"Node-js","panelId":"panel_Nodejs_cmds_hash-stephlen"},{"clientId":"ioredis","clientName":"ioredis","id":"ioredis","langId":"javascript","panelId":"panel_ioredis_cmds_hash-stephlen"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_cmds_hash-stephlen"},{"clientId":"lettuce","clientName":"Lettuce","id":"Lettuce-Sync","langId":"java","panelId":"panel_Lettuce-Sync_cmds_hash-stephlen"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_cmds_hash-stephlen"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_cmds_hash-stephlen"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_cmds_hash-stephlen"},{"clientId":"hiredis","clientName":"hiredis","id":"C","langId":"c","panelId":"panel_C_cmds_hash-stephlen"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_cmds_hash-stephlen"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_cmds_hash-stephlen"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_cmds_hash-stephlen"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_cmds_hash-stephlen"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_cmds_hash-stephlen"}]}]
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

Returns the number of fields contained in the hash stored at `key`.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key that holds the hash.

</details>

## Examples

Foundational: Count the fields in a hash with HLEN when you need a hash's size without transferring its contents

**Difficulty:** Beginner

**Commands:** HSET, HLEN

**Complexity:**
- HSET: O(1)
- HLEN: O(1)

**Available in:** Redis CLI, C, C#, Go, Java, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
redis> HSET myhash field1 "Hello"
(integer) 1
redis> HSET myhash field2 "World"
(integer) 1
redis> HLEN myhash
(integer) 2
```

##### C

```c
    // Add two new fields to the hash
    reply = redisCommand(c, "HSET %s %s %s", "myhash", "field1", "Hello");
    printf("HSET myhash field1 Hello: %lld\n", reply->integer); // >>> 1
    freeReplyObject(reply);

    reply = redisCommand(c, "HSET %s %s %s", "myhash", "field2", "World");
    printf("HSET myhash field2 World: %lld\n", reply->integer); // >>> 1
    freeReplyObject(reply);

    // Count the fields in the hash
    reply = redisCommand(c, "HLEN %s", "myhash");
    printf("HLEN myhash: %lld\n", reply->integer); // >>> 2
    freeReplyObject(reply);
```

##### C#

```csharp
        bool hlenRes1 = db.HashSet("myhash", "field1", "Hello");
        Console.WriteLine(hlenRes1);    // >>> True

        bool hlenRes2 = db.HashSet("myhash", "field2", "World");
        Console.WriteLine(hlenRes2);    // >>> True

        long hlenRes3 = db.HashLength("myhash");
        Console.WriteLine(hlenRes3);    // >>> 2
```

##### Go

```go
	hlen1, err := rdb.HSet(ctx, "myhash", "field1", "Hello").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(hlen1) // >>> 1

	hlen2, err := rdb.HSet(ctx, "myhash", "field2", "World").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(hlen2) // >>> 1

	hlen3, err := rdb.HLen(ctx, "myhash").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(hlen3) // >>> 2
```

##### Java

```java
            // `hset` returns true because `field1` is a new field.
            boolean res19 = syncCommands.hset("myhash", "field1", "Hello");
            System.out.println(res19); // >>> true

            // `hset` returns true because `field2` is also a new field.
            boolean res20 = syncCommands.hset("myhash", "field2", "World");
            System.out.println(res20); // >>> true

            Long res21 = syncCommands.hlen("myhash");
            System.out.println(res21); // >>> 2
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> hLenExample = asyncCommands.hset("myhash", "field1", "Hello").thenCompose(res1 -> {
                // `hset` returns true because `field1` is a new field.
                System.out.println(res1); // >>> true
                return asyncCommands.hset("myhash", "field2", "World");
            }).thenCompose(res2 -> {
                // `hset` returns true because `field2` is also a new field.
                System.out.println(res2); // >>> true
                return asyncCommands.hlen("myhash");
            }).thenAccept(res3 -> {
                System.out.println(res3); // >>> 2
            }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Boolean> hLenExample1 = reactiveCommands.hset("myhash", "field1", "Hello").doOnNext(result -> {
                System.out.println(result); // >>> true
            });

            hLenExample1.block();

            Mono<Boolean> hLenExample2 = reactiveCommands.hset("myhash", "field2", "World").doOnNext(result -> {
                System.out.println(result); // >>> true
            });

            hLenExample2.block();

            Mono<Long> hLenExample3 = reactiveCommands.hlen("myhash").doOnNext(result -> {
                System.out.println(result); // >>> 2
            });
```

##### Java (Synchronous - Jedis)

```java
        // `hset` returns 1 because `field1` is a new field.
        long hLenResult1 = jedis.hset("myhash", "field1", "Hello");
        System.out.println(hLenResult1);    // >>> 1

        // `hset` returns 1 because `field2` is also a new field.
        long hLenResult2 = jedis.hset("myhash", "field2", "World");
        System.out.println(hLenResult2);    // >>> 1

        long hLenResult3 = jedis.hlen("myhash");
        System.out.println(hLenResult3);    // >>> 2
```

##### JavaScript (Node.js)

```javascript
const res17 = await client.hSet('myhash', 'field1', 'Hello')
console.log(res17) // 1

const res18 = await client.hSet('myhash', 'field2', 'World')
console.log(res18) // 1

const res19 = await client.hLen('myhash')
console.log(res19) // 2

```

##### JavaScript (Node.js)

```javascript
const hlenSet1 = await redis.hset('myhash', 'field1', 'Hello');
console.log(hlenSet1); // >>> 1

const hlenSet2 = await redis.hset('myhash', 'field2', 'World');
console.log(hlenSet2); // >>> 1

const hlenResult = await redis.hlen('myhash');
console.log(hlenResult); // >>> 2
```

##### JavaScript (Node.js)

```javascript
const res17 = await client.hSet('myhash', 'field1', 'Hello')
console.log(res17) // 1

const res18 = await client.hSet('myhash', 'field2', 'World')
console.log(res18) // 1

const res19 = await client.hLen('myhash')
console.log(res19) // 2

```

##### JavaScript (Node.js)

```javascript
const hlenSet1 = await redis.hset('myhash', 'field1', 'Hello');
console.log(hlenSet1); // >>> 1

const hlenSet2 = await redis.hset('myhash', 'field2', 'World');
console.log(hlenSet2); // >>> 1

const hlenResult = await redis.hlen('myhash');
console.log(hlenResult); // >>> 2
```

##### PHP

```php

        $hLenResult1 = $this->redis->hset('myhash', 'field1', 'Hello');
        echo "HSET myhash field1 Hello: " . $hLenResult1 . "\n"; // >>> 1

        $hLenResult2 = $this->redis->hset('myhash', 'field2', 'World');
        echo "HSET myhash field2 World: " . $hLenResult2 . "\n"; // >>> 1

        $hLenResult3 = $this->redis->hlen('myhash');
        echo "HLEN myhash: " . $hLenResult3 . "\n"; // >>> 2
```

##### Python

```python
res15 = r.hset("myhash", "field1", "Hello")
print(res15)
# >>> 1

res16 = r.hset("myhash", "field2", "World")
print(res16)
# >>> 1

res17 = r.hlen("myhash")
print(res17)
# >>> 2

```

##### Ruby

```ruby
res19 = r.hset('myhash', 'field1', 'Hello')
puts res19 # >>> 1

res20 = r.hset('myhash', 'field2', 'World')
puts res20 # >>> 1

res21 = r.hlen('myhash')
puts res21 # >>> 2
```

##### Rust (Asynchronous)

```rust
        match r.hset("myhash", "field1", "Hello").await {
            Ok(res15) => {
                let res15: i32 = res15;
                println!("{res15}");    // >>> 1
            },
            Err(e) => {
                println!("Error setting hash field: {e}");
                return;
            }
        }

        match r.hset("myhash", "field2", "World").await {
            Ok(res16) => {
                let res16: i32 = res16;
                println!("{res16}");    // >>> 1
            },
            Err(e) => {
                println!("Error setting hash field: {e}");
                return;
            }
        }

        match r.hlen("myhash").await {
            Ok(res17) => {
                let res17: usize = res17;
                println!("{res17}");    // >>> 2
            },
            Err(e) => {
                println!("Error getting hash length: {e}");
                return;
            }
        }

```

##### Rust (Synchronous)

```rust
        match r.hset("myhash", "field1", "Hello") {
            Ok(hlen1) => {
                let hlen1: i32 = hlen1;
                println!("{hlen1}");    // >>> 1
            },
            Err(e) => {
                println!("Error setting hash field: {e}");
                return;
            }
        }

        match r.hset("myhash", "field2", "World") {
            Ok(hlen2) => {
                let hlen2: i32 = hlen2;
                println!("{hlen2}");    // >>> 1
            },
            Err(e) => {
                println!("Error setting hash field: {e}");
                return;
            }
        }

        match r.hlen("myhash") {
            Ok(hlen3) => {
                let hlen3: usize = hlen3;
                println!("{hlen3}");    // >>> 2
            },
            Err(e) => {
                println!("Error getting hash length: {e}");
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

[Integer reply](../../develop/reference/protocol-spec#integers): the number of fields in the hash, or 0 when the key does not exist.

**RESP3:**

[Integer reply](../../develop/reference/protocol-spec#integers): the number of the fields in the hash, or 0 when the key does not exist.



