# HMGET

```json metadata
{
  "schema_version": 2,
  "title": "HMGET",
  "description": "Returns the values of all fields in a hash.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"},{"display_text":"field","multiple":true,"name":"field","type":"string"}],
  "syntax_fmt": "HMGET key field [field ...]",
  "complexity": "O(N) where N is the number of fields being requested.",
  "group": "hash",
  "command_flags": ["readonly","fast"],
  "acl_categories": ["@read","@hash","@fast"],
  "since": "2.0.0",
  "arity": -3,
  "key_specs": [{"RO":true,"access":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": [{"codetabsId":"cmds_hash-stephmget","commands":[{"acl_categories":["@write","@hash","@fast"],"complexity":"O(1)","name":"HSET"},{"acl_categories":["@read","@hash","@fast"],"complexity":"O(N)","name":"HMGET"}],"description":"Foundational: Retrieve multiple field values from a hash using HMGET (returns nil if field or key doesn\u0026amp;#39;t exist)","difficulty":"beginner","id":"hmget","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_cmds_hash-stephmget"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_cmds_hash-stephmget"},{"id":"Node-js","panelId":"panel_Nodejs_cmds_hash-stephmget"},{"clientId":"ioredis","clientName":"ioredis","id":"ioredis","langId":"javascript","panelId":"panel_ioredis_cmds_hash-stephmget"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_cmds_hash-stephmget"},{"clientId":"lettuce","clientName":"Lettuce","id":"Lettuce-Sync","langId":"java","panelId":"panel_Lettuce-Sync_cmds_hash-stephmget"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_cmds_hash-stephmget"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_cmds_hash-stephmget"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_cmds_hash-stephmget"},{"clientId":"hiredis","clientName":"hiredis","id":"C","langId":"c","panelId":"panel_C_cmds_hash-stephmget"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_cmds_hash-stephmget"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_cmds_hash-stephmget"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_cmds_hash-stephmget"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_cmds_hash-stephmget"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_cmds_hash-stephmget"}]}]
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

Returns the values associated with the specified `fields` in the hash stored at
`key`.

For every `field` that does not exist in the hash, a `nil` value is returned.
Because non-existing keys are treated as empty hashes, running `HMGET` against
a non-existing `key` will return a list of `nil` values.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key that holds the hash.

</details>

<details open><summary><code>field [field ...]</code></summary>

One or more fields whose values to retrieve.

</details>

## Examples

Foundational: Retrieve multiple field values from a hash using HMGET (returns nil if field or key doesn't exist)

**Difficulty:** Beginner

**Commands:** HSET, HMGET

**Complexity:**
- HSET: O(1)
- HMGET: O(N)

**Available in:** Redis CLI, C, C#, Go, Java, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> HSET myhash field1 "Hello"
(integer) 1
> HSET myhash field2 "World"
(integer) 1
> HMGET myhash field1 field2 nofield
1) "Hello"
2) "World"
3) (nil)
```

##### C

```c
    redisReply *reply;

    // Set up hash with fields
    reply = redisCommand(c, "HSET %s %s %s %s %s",
        "myhash", "field1", "Hello", "field2", "World");
    freeReplyObject(reply);

    // Get multiple fields at once
    reply = redisCommand(c, "HMGET %s %s %s %s",
        "myhash", "field1", "field2", "nofield");

    printf("HMGET myhash field1 field2 nofield:\n");
    for (size_t i = 0; i < reply->elements; i++) {
        if (reply->element[i]->type == REDIS_REPLY_NIL) {
            printf("  [%zu]: null\n", i);
        } else {
            printf("  [%zu]: %s\n", i, reply->element[i]->str);
        }
    }
    // >>> [0]: Hello
    // >>> [1]: World
    // >>> [2]: null
```

##### C#

```csharp
        db.HashSet("myhash",
            [
                new("field1", "Hello"),
                new("field2", "World")
            ]
        );

        RedisValue[] hmgetResult = db.HashGet("myhash", new RedisValue[] { "field1", "field2", "nofield" });
        Console.WriteLine(string.Join(", ", hmgetResult.Select(v => v.IsNull ? "null" : v.ToString())));
        // >>> Hello, World, null
```

##### Go

```go
	rdb.HSet(ctx, "myhash", "field1", "Hello", "field2", "World")

	hmgetResult, err := rdb.HMGet(ctx, "myhash", "field1", "field2", "nofield").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(hmgetResult) // >>> [Hello World <nil>]
```

##### Java

```java
            Map<String, String> hmgetFields = new HashMap<>();
            hmgetFields.put("field1", "Hello");
            hmgetFields.put("field2", "World");

            syncCommands.hset("myhash", hmgetFields);

            // `hmget` returns a `KeyValue` for each field you ask for, in the
            // order you asked for them. A field that doesn't exist comes back
            // as an empty `KeyValue`.
            List<KeyValue<String, String>> res13 = syncCommands.hmget("myhash", "field1", "field2", "nofield");
            System.out.println(res13);
            // >>> [KeyValue[field1, Hello], KeyValue[field2, World], KeyValue[nofield].empty]
```

##### Java (Asynchronous - Lettuce)

```java
            Map<String, String> hmgetExampleParams = new HashMap<>();
            hmgetExampleParams.put("field1", "Hello");
            hmgetExampleParams.put("field2", "World");

            CompletableFuture<Void> hmgetExample = asyncCommands.hset("myhash", hmgetExampleParams).thenCompose(res1 -> {
                return asyncCommands.hmget("myhash", "field1", "field2", "nofield");
            }).thenAccept(res2 -> {
                System.out.println(res2); // >>> [KeyValue[field1, Hello], KeyValue[field2, World], KeyValue[nofield].empty]
            }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Map<String, String> hmgetExampleParams = new HashMap<>();
            hmgetExampleParams.put("field1", "Hello");
            hmgetExampleParams.put("field2", "World");

            Mono<Long> hmgetExample1 = reactiveCommands.hset("myhash", hmgetExampleParams);

            hmgetExample1.block();

            Flux<KeyValue<String, String>> hmgetExample2 = reactiveCommands.hmget("myhash", "field1", "field2", "nofield")
                    .doOnNext(result -> {
                        System.out.println(result);
                        // >>> KeyValue[field1, Hello]
                        // >>> KeyValue[field2, World]
                        // >>> KeyValue[nofield].empty
                    });
```

##### Java (Synchronous - Jedis)

```java
        Map<String, String> hmgetExampleParams = new HashMap<>();
        hmgetExampleParams.put("field1", "Hello");
        hmgetExampleParams.put("field2", "World");

        jedis.hset("myhash", hmgetExampleParams);

        List<String> hmgetResult = jedis.hmget("myhash", "field1", "field2", "nofield");
        System.out.println(hmgetResult);    // >>> [Hello, World, null]
```

##### JavaScript (Node.js)

```javascript
await client.hSet('myhash', { field1: 'Hello', field2: 'World' });

const hmgetResult = await client.hmGet('myhash', ['field1', 'field2', 'nofield']);
console.log(hmgetResult); // ['Hello', 'World', null]

```

##### JavaScript (Node.js)

```javascript
await redis.hset('myhash', { field1: 'Hello', field2: 'World' });

const hmgetResult = await redis.hmget('myhash', 'field1', 'field2', 'nofield');
console.log(hmgetResult); // >>> ['Hello', 'World', null]
```

##### JavaScript (Node.js)

```javascript
await client.hSet('myhash', { field1: 'Hello', field2: 'World' });

const hmgetResult = await client.hmGet('myhash', ['field1', 'field2', 'nofield']);
console.log(hmgetResult); // ['Hello', 'World', null]

```

##### JavaScript (Node.js)

```javascript
await redis.hset('myhash', { field1: 'Hello', field2: 'World' });

const hmgetResult = await redis.hmget('myhash', 'field1', 'field2', 'nofield');
console.log(hmgetResult); // >>> ['Hello', 'World', null]
```

##### PHP

```php
        $this->redis->hmset('myhash', ['field1' => 'Hello', 'field2' => 'World']);

        $hmgetResult = $this->redis->hmget('myhash', ['field1', 'field2', 'nofield']);
        echo "HMGET myhash field1 field2 nofield: ";
        print_r($hmgetResult);
        // >>> Array ( [0] => Hello [1] => World [2] => )
```

##### Python

```python
r.hset("myhash", mapping={"field1": "Hello", "field2": "World"})

hmget_result = r.hmget("myhash", ["field1", "field2", "nofield"])
print(hmget_result)  # >>> ['Hello', 'World', None]

```

##### Ruby

```ruby
r.hset('myhash', { 'field1' => 'Hello', 'field2' => 'World' })

res13 = r.hmget('myhash', 'field1', 'field2', 'nofield')
puts res13.inspect # >>> ["Hello", "World", nil]
```

##### Rust (Asynchronous)

```rust
        let hash_fields = [
            ("field1", "Hello"),
            ("field2", "World"),
        ];

        if let Ok(_) = r.hset_multiple::<&str, &str, &str, String>("myhash", &hash_fields).await {
            // Fields set successfully
        }

        match r.hmget::<&str, &[&str], Vec<Option<String>>>("myhash", &["field1", "field2", "nofield"]).await {
            Ok(hmget_result) => {
                println!("{:?}", hmget_result);    // >>> [Some("Hello"), Some("World"), None]
            },
            Err(e) => {
                println!("Error getting hash fields: {e}");
                return;
            }
        }

```

##### Rust (Synchronous)

```rust
        let hash_fields = [
            ("field1", "Hello"),
            ("field2", "World"),
        ];

        if let Ok(_) = r.hset_multiple::<&str, &str, &str, String>("myhash", &hash_fields) {
            // Fields set successfully
        }

        match r.hmget::<&str, &[&str], Vec<Option<String>>>("myhash", &["field1", "field2", "nofield"]) {
            Ok(hmget_result) => {
                println!("{:?}", hmget_result);    // >>> [Some("Hello"), Some("World"), None]
            },
            Err(e) => {
                println!("Error getting hash fields: {e}");
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

[Array reply](../../develop/reference/protocol-spec#arrays): a list of values associated with the given fields, in the same order as they are requested.

**RESP3:**

[Array reply](../../develop/reference/protocol-spec#arrays): a list of values associated with the given fields, in the same order as they are requested.



