# HDEL

```json metadata
{
  "schema_version": 2,
  "title": "HDEL",
  "description": "Deletes one or more fields and their values from a hash. Deletes the hash if no fields remain.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"},{"display_text":"field","multiple":true,"name":"field","type":"string"}],
  "syntax_fmt": "HDEL key field [field ...]",
  "complexity": "O(N) where N is the number of fields to be removed.",
  "group": "hash",
  "command_flags": ["write","fast"],
  "acl_categories": ["@write","@hash","@fast"],
  "since": "2.0.0",
  "arity": -3,
  "key_specs": [{"RW":true,"begin_search":{"spec":{"index":1},"type":"index"},"delete":true,"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": [{"codetabsId":"cmds_hash-stephdel","commands":[{"acl_categories":["@write","@hash","@fast"],"complexity":"O(1)","name":"HSET"},{"acl_categories":["@write","@hash","@fast"],"complexity":"O(N)","name":"HDEL"}],"description":"Foundational: Delete one or more fields from a hash using HDEL (returns count of deleted fields, ignores non-existent fields)","difficulty":"beginner","id":"hdel","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_cmds_hash-stephdel"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_cmds_hash-stephdel"},{"id":"Node-js","panelId":"panel_Nodejs_cmds_hash-stephdel"},{"clientId":"ioredis","clientName":"ioredis","id":"ioredis","langId":"javascript","panelId":"panel_ioredis_cmds_hash-stephdel"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_cmds_hash-stephdel"},{"clientId":"lettuce","clientName":"Lettuce","id":"Lettuce-Sync","langId":"java","panelId":"panel_Lettuce-Sync_cmds_hash-stephdel"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_cmds_hash-stephdel"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_cmds_hash-stephdel"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_cmds_hash-stephdel"},{"clientId":"hiredis","clientName":"hiredis","id":"C","langId":"c","panelId":"panel_C_cmds_hash-stephdel"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_cmds_hash-stephdel"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_cmds_hash-stephdel"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_cmds_hash-stephdel"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_cmds_hash-stephdel"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_cmds_hash-stephdel"}]}]
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

Removes the specified fields from the hash stored at `key`.
Specified fields that do not exist within this hash are ignored.
Deletes the hash if no fields remain.
If `key` does not exist, it is treated as an empty hash and this command returns
`0`.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key that holds the hash.

</details>

<details open><summary><code>field [field ...]</code></summary>

One or more fields to delete from the hash.

</details>

## Examples

Foundational: Delete one or more fields from a hash using HDEL (returns count of deleted fields, ignores non-existent fields)

**Difficulty:** Beginner

**Commands:** HSET, HDEL

**Complexity:**
- HSET: O(1)
- HDEL: O(N)

**Available in:** Redis CLI, C, C#, Go, Java, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> HSET myhash field1 "foo"
(integer) 1
> HDEL myhash field1
(integer) 1
> HDEL myhash field2
(integer) 0
```

##### C

```c
    reply = redisCommand(c, "HSET myhash field1 foo");
    printf("%lld\n", reply->integer);
    // >>> 1
    freeReplyObject(reply);

    reply = redisCommand(c, "HDEL myhash field1");
    printf("%lld\n", reply->integer);
    // >>> 1
    freeReplyObject(reply);

    // Deleting a field that is not there removes nothing.
    reply = redisCommand(c, "HDEL myhash field2");
    printf("%lld\n", reply->integer);
    // >>> 0
    freeReplyObject(reply);
```

##### C#

```csharp
        bool hdelRes1 = db.HashSet("myhash", "field1", "foo");

        RedisValue hdelRes2 = db.HashDelete("myhash", "field1");
        Console.WriteLine(hdelRes2);    // >>> 1

        RedisValue hdelRes3 = db.HashDelete("myhash", "field1");
        Console.WriteLine(hdelRes3);    // >>> 0
```

##### Go

```go
	hdel1, err := rdb.HSet(ctx, "myhash", "field1", "foo").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(hdel1) // >>> 1

	hdel2, err := rdb.HDel(ctx, "myhash", "field1").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(hdel2) // >>> 1

	hdel3, err := rdb.HDel(ctx, "myhash", "field2").Result()

	if err != nil {
		fmt.Println(err)
	}

	fmt.Println(hdel3) // >>> 0
```

##### Java

```java
            // `hset` returns true because `field1` is a new field.
            boolean res1 = syncCommands.hset("myhash", "field1", "foo");
            System.out.println(res1); // >>> true

            Long res2 = syncCommands.hdel("myhash", "field1");
            System.out.println(res2); // >>> 1

            // `hdel` returns 0 because `field2` doesn't exist.
            Long res3 = syncCommands.hdel("myhash", "field2");
            System.out.println(res3); // >>> 0
```

##### Java (Asynchronous - Lettuce)

```java
            Map<String, String> hDelExampleParams = new HashMap<>();
            hDelExampleParams.put("field1", "foo");

            CompletableFuture<Void> hDelExample = asyncCommands.hset("myhash", hDelExampleParams).thenCompose(res1 -> {
                System.out.println(res1); // >>> 1
                return asyncCommands.hdel("myhash", "field1");
            }).thenCompose(res2 -> {
                System.out.println(res2); // >>> 1
                return asyncCommands.hdel("myhash", "field2");
            }).thenAccept(res3 -> {
                System.out.println(res3); // >>> 0
            }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Map<String, String> hDelExampleParams = new HashMap<>();
            hDelExampleParams.put("field1", "foo");

            Mono<Long> hDelExample1 = reactiveCommands.hset("myhash", hDelExampleParams).doOnNext(result -> {
                System.out.println(result); // >>> 1
            });

            hDelExample1.block();

            Mono<Long> hDelExample2 = reactiveCommands.hdel("myhash", "field1").doOnNext(result -> {
                System.out.println(result); // >>> 1
            });

            hDelExample2.block();

            Mono<Long> hDelExample3 = reactiveCommands.hdel("myhash", "field2").doOnNext(result -> {
                System.out.println(result); // >>> 0
            });
```

##### Java (Synchronous - Jedis)

```java
        Map<String, String> hDelExampleParams = new HashMap<>();
        hDelExampleParams.put("field1", "foo");

        long hDelResult1 = jedis.hset("myhash", hDelExampleParams);
        System.out.println(hDelResult1);    // >>> 1

        long hDelResult2 = jedis.hdel("myhash", "field1");
        System.out.println(hDelResult2);    // >>> 1

        long hDelResult3 = jedis.hdel("myhash", "field2");
        System.out.println(hDelResult3);    // >>> 0
```

##### JavaScript (Node.js)

```javascript
const hDel1 = await client.hSet('myhash', 'field1', 'Hello')
console.log(hDel1) // 1

const hDel2 = await client.hDel('myhash', 'field1')
console.log(hDel2) // 1

const hDel3 = await client.hDel('myhash', 'field2')
console.log(hDel3) // 0

```

##### JavaScript (Node.js)

```javascript
const hdelRes1 = await redis.hset('myhash', 'field1', 'foo');
console.log(hdelRes1); // >>> 1

const hdelRes2 = await redis.hdel('myhash', 'field1');
console.log(hdelRes2); // >>> 1

// Deleting a field that is not there removes nothing.
const hdelRes3 = await redis.hdel('myhash', 'field2');
console.log(hdelRes3); // >>> 0
```

##### JavaScript (Node.js)

```javascript
const hDel1 = await client.hSet('myhash', 'field1', 'Hello')
console.log(hDel1) // 1

const hDel2 = await client.hDel('myhash', 'field1')
console.log(hDel2) // 1

const hDel3 = await client.hDel('myhash', 'field2')
console.log(hDel3) // 0

```

##### JavaScript (Node.js)

```javascript
const hdelRes1 = await redis.hset('myhash', 'field1', 'foo');
console.log(hdelRes1); // >>> 1

const hdelRes2 = await redis.hdel('myhash', 'field1');
console.log(hdelRes2); // >>> 1

// Deleting a field that is not there removes nothing.
const hdelRes3 = await redis.hdel('myhash', 'field2');
console.log(hdelRes3); // >>> 0
```

##### PHP

```php
        $hDelResult1 = $this->redis->hset('myhash', 'field1', 'foo');
        echo "HSET myhash field1 foo: " . $hDelResult1 . "\n"; // >>> 1

        $hDelResult2 = $this->redis->hdel('myhash', 'field1');
        echo "HDEL myhash field1: " . $hDelResult2 . "\n"; // >>> 1

        $hDelResult3 = $this->redis->hdel('myhash', 'field2');
        echo "HDEL myhash field2: " . $hDelResult3 . "\n"; // >>> 0
```

##### Python

```python
hdel1 = r.hset("myhash", "field1", "foo")
print(hdel1)
# >>> 1

hdel2 = r.hdel("myhash", "field1")
print(hdel2)
# >>> 1

hdel3 = r.hdel("myhash", "field2")
print(hdel3)
# >>> 0

```

##### Ruby

```ruby
res1 = r.hset('myhash', 'field1', 'foo')
puts res1 # >>> 1

res2 = r.hdel('myhash', 'field1')
puts res2 # >>> 1

res3 = r.hdel('myhash', 'field2')
puts res3 # >>> 0
```

##### Rust (Asynchronous)

```rust
        match r.hset("myhash", "field1", "foo").await {
            Ok(hdel1) => {
                let hdel1: i32 = hdel1;
                println!("{hdel1}");    // >>> 1
            },
            Err(e) => {
                println!("Error setting hash field: {e}");
                return;
            }
        }

        match r.hdel("myhash", "field1").await {
            Ok(hdel2) => {
                let hdel2: Option<i32> = hdel2;
                match hdel2 {
                    Some(value) => {
                        println!("{value}");    // >>> 1
                    },
                    None => {
                        println!("None");
                    }
                }
            },
            Err(e) => {
                println!("Error getting hash field: {e}");
                return;
            }
        }

        match r.hdel("myhash", "field2").await {
            Ok(hdel3) => {
                let hdel3: Option<i32> = hdel3;
                match hdel3 {
                    Some(value) => {
                        println!("{value}");    // >>> 0
                    },
                    None => {
                        println!("None");
                    }
                }
            },
            Err(e) => {
                println!("Error getting hash field: {e}");
                return;
            }
        }

```

##### Rust (Synchronous)

```rust
        match r.hset("myhash", "field1", "foo") {
            Ok(hdel1) => {
                let hdel1: i32 = hdel1;
                println!("{hdel1}");    // >>> 1
            },
            Err(e) => {
                println!("Error setting hash field: {e}");
                return;
            }
        }

        match r.hdel("myhash", "field1") {
            Ok(hdel2) => {
                let hdel2: Option<i32> = hdel2;
                match hdel2 {
                    Some(value) => {
                        println!("{value}");    // >>> 1
                    },
                    None => {
                        println!("None");
                    }
                }
            },
            Err(e) => {
                println!("Error getting hash field: {e}");
                return;
            }
        }

        match r.hdel("myhash", "field2") {
            Ok(hdel3) => {
                let hdel3: Option<i32> = hdel3;
                match hdel3 {
                    Some(value) => {
                        println!("{value}");    // >>> 0
                    },
                    None => {
                        println!("None");
                    }
                }
            },
            Err(e) => {
                println!("Error getting hash field: {e}");
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

[Integer reply](../../develop/reference/protocol-spec#integers): the number of fields that were removed from the hash, excluding any specified but non-existing fields.

**RESP3:**

[Integer reply](../../develop/reference/protocol-spec#integers): The number of fields that were removed from the hash, excluding any specified but non-existing fields.



