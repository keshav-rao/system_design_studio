# HGETALL

```json metadata
{
  "schema_version": 2,
  "title": "HGETALL",
  "description": "Returns all fields and values in a hash.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"}],
  "syntax_fmt": "HGETALL key",
  "complexity": "O(N) where N is the size of the hash.",
  "group": "hash",
  "command_flags": ["readonly"],
  "acl_categories": ["@read","@hash","@slow"],
  "since": "2.0.0",
  "arity": 2,
  "key_specs": [{"RO":true,"access":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": [{"codetabsId":"cmds_hash-stephgetall","commands":[{"acl_categories":["@write","@hash","@fast"],"complexity":"O(1)","name":"HSET"},{"acl_categories":["@read","@hash","@slow"],"complexity":"O(N)","name":"HGETALL"}],"description":"Foundational: Retrieve all fields and values from a hash using HGETALL (returns alternating field-value pairs, useful for loading entire hash data)","difficulty":"beginner","id":"hgetall","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_cmds_hash-stephgetall"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_cmds_hash-stephgetall"},{"id":"Node-js","panelId":"panel_Nodejs_cmds_hash-stephgetall"},{"clientId":"ioredis","clientName":"ioredis","id":"ioredis","langId":"javascript","panelId":"panel_ioredis_cmds_hash-stephgetall"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_cmds_hash-stephgetall"},{"clientId":"lettuce","clientName":"Lettuce","id":"Lettuce-Sync","langId":"java","panelId":"panel_Lettuce-Sync_cmds_hash-stephgetall"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_cmds_hash-stephgetall"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_cmds_hash-stephgetall"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_cmds_hash-stephgetall"},{"clientId":"hiredis","clientName":"hiredis","id":"C","langId":"c","panelId":"panel_C_cmds_hash-stephgetall"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_cmds_hash-stephgetall"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_cmds_hash-stephgetall"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_cmds_hash-stephgetall"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_cmds_hash-stephgetall"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_cmds_hash-stephgetall"}]}]
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

Returns all fields and values of the hash stored at `key`.
In the returned value, every field name is followed by its value, so the length
of the reply is twice the size of the hash.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key that holds the hash.

</details>

## Examples

Foundational: Retrieve all fields and values from a hash using HGETALL (returns alternating field-value pairs, useful for loading entire hash data)

**Difficulty:** Beginner

**Commands:** HSET, HGETALL

**Complexity:**
- HSET: O(1)
- HGETALL: O(N)

**Available in:** Redis CLI, C, C#, Go, Java, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
redis> HSET myhash field1 "Hello"
(integer) 1
redis> HSET myhash field2 "World"
(integer) 1
redis> HGETALL myhash
1) "field1"
2) "Hello"
3) "field2"
4) "World"
```

##### C

```c
    reply = redisCommand(c, "HSET myhash field1 Hello field2 World");
    freeReplyObject(reply);

    reply = redisCommand(c, "HGETALL myhash");
    for (size_t i = 0; i < reply->elements; i += 2) {
        printf("%s=%s\n", reply->element[i]->str, reply->element[i + 1]->str);
    }
    // >>> field1=Hello
    // >>> field2=World
    freeReplyObject(reply);
```

##### C#

```csharp
        db.HashSet("myhash",
            [
                new("field1", "Hello"),
                new("field2", "World")
            ]
        );

        HashEntry[] hGetAllResult = db.HashGetAll("myhash");
        Array.Sort(hGetAllResult, (a1, a2) => a1.Name.CompareTo(a2.Name));
        Console.WriteLine(
            string.Join(", ", hGetAllResult.Select(e => $"{e.Name}: {e.Value}"))
        );
        // >>> field1: Hello, field2: World
```

##### Go

```go
	hGetAllResult1, err := rdb.HSet(ctx, "myhash",
		"field1", "Hello",
		"field2", "World",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(hGetAllResult1) // >>> 2

	hGetAllResult2, err := rdb.HGetAll(ctx, "myhash").Result()

	if err != nil {
		panic(err)
	}

	keys := make([]string, 0, len(hGetAllResult2))

	for key, _ := range hGetAllResult2 {
		keys = append(keys, key)
	}

	sort.Strings(keys)

	for _, key := range keys {
		fmt.Printf("Key: %v, value: %v\n", key, hGetAllResult2[key])
	}
	// >>> Key: field1, value: Hello
	// >>> Key: field2, value: World
```

##### Java

```java
            Map<String, String> hGetAllFields = new HashMap<>();
            hGetAllFields.put("field1", "Hello");
            hGetAllFields.put("field2", "World");

            syncCommands.hset("myhash", hGetAllFields);

            // `hgetall` returns a `Map`, whose iteration order isn't
            // guaranteed. Wrap it in a `TreeMap` to sort the fields by name.
            Map<String, String> res14 = syncCommands.hgetall("myhash");
            System.out.println(new TreeMap<>(res14));
            // >>> {field1=Hello, field2=World}
```

##### Java (Asynchronous - Lettuce)

```java
            Map<String, String> hGetAllExampleParams = new HashMap<>();
            hGetAllExampleParams.put("field1", "Hello");
            hGetAllExampleParams.put("field2", "World");

            CompletableFuture<Void> hGetAllExample = asyncCommands.hset("myhash", hGetAllExampleParams).thenCompose(res1 -> {
                return asyncCommands.hgetall("myhash");
            }).thenAccept(res2 -> {
                System.out.println(res2);
                // >>> {field1=Hello, field2=World}
            }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Map<String, String> hGetAllExampleParams = new HashMap<>();
            hGetAllExampleParams.put("field1", "Hello");
            hGetAllExampleParams.put("field2", "World");

            Mono<Long> hGetAllExample1 = reactiveCommands.hset("myhash", hGetAllExampleParams).doOnNext(result -> {
            });

            hGetAllExample1.block();

            Mono<Map<String, String>> hGetAllExample2 = reactiveCommands.hgetall("myhash").collectMap(
                    KeyValue::getKey, KeyValue::getValue
            ).doOnNext(result -> {
                System.out.println(result);
                // >>> {field1=Hello, field2=World}
            });
```

##### Java (Synchronous - Jedis)

```java
        Map<String, String> hGetAllExampleParams = new HashMap<>();
        hGetAllExampleParams.put("field1", "Hello");
        hGetAllExampleParams.put("field2", "World");

        long hGetAllResult1 = jedis.hset("myhash", hGetAllExampleParams);
        System.out.println(hGetAllResult1); // >>> 2

        Map<String, String> hGetAllResult2 = jedis.hgetAll("myhash");
        System.out.println(
            hGetAllResult2.entrySet().stream()
                    .sorted((s1, s2)-> s1.getKey().compareTo(s2.getKey()))
                    .collect(toList())
                    .toString()
        );
        // >>> [field1=Hello, field2=World]
```

##### JavaScript (Node.js)

```javascript
const res10 = await client.hSet(
  'myhash',
  {
    'field1': 'Hello',
    'field2': 'World'
  }
)

const res11 = await client.hGetAll('myhash')
console.log(res11) // [Object: null prototype] { field1: 'Hello', field2: 'World' }

```

##### JavaScript (Node.js)

```javascript
await redis.hset('myhash', { field1: 'Hello', field2: 'World' });

const hgetallRes = await redis.hgetall('myhash');
console.log(hgetallRes); // >>> { field1: 'Hello', field2: 'World' }
```

##### JavaScript (Node.js)

```javascript
const res10 = await client.hSet(
  'myhash',
  {
    'field1': 'Hello',
    'field2': 'World'
  }
)

const res11 = await client.hGetAll('myhash')
console.log(res11) // [Object: null prototype] { field1: 'Hello', field2: 'World' }

```

##### JavaScript (Node.js)

```javascript
await redis.hset('myhash', { field1: 'Hello', field2: 'World' });

const hgetallRes = await redis.hgetall('myhash');
console.log(hgetallRes); // >>> { field1: 'Hello', field2: 'World' }
```

##### PHP

```php
        $hGetAllResult1 = $this->redis->hmset('myhash', ['field1' => 'Hello', 'field2' => 'World']);
        echo "HMSET myhash field1 Hello field2 World: " . ($hGetAllResult1 ? 'OK' : 'FAIL') . "\n"; // >>> OK

        $hGetAllResult2 = $this->redis->hgetall('myhash');
        echo "HGETALL myhash: " . json_encode($hGetAllResult2) . "\n"; // >>> {"field1":"Hello","field2":"World"}
```

##### Python

```python
res10 = r.hset("myhash", mapping={"field1": "Hello", "field2": "World"})

res11 = r.hgetall("myhash")
print(res11) # >>> { "field1": "Hello", "field2": "World" }

```

##### Ruby

```ruby
r.hset('myhash', { 'field1' => 'Hello', 'field2' => 'World' })

res14 = r.hgetall('myhash')
puts res14.inspect # >>> {"field1"=>"Hello", "field2"=>"World"}
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

        match r.hgetall("myhash").await {
            Ok(res11) => {
                let res11: HashMap<String, String> = res11;
                println!("{res11:?}");    // >>> {"field1": "Hello", "field2": "World"}
            },
            Err(e) => {
                println!("Error getting all hash fields: {e}");
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

        match r.hgetall("myhash") {
            Ok(res11) => {
                let res11: HashMap<String, String> = res11;
                println!("{res11:?}");    // >>> {"field1": "Hello", "field2": "World"}
            },
            Err(e) => {
                println!("Error getting all hash fields: {e}");
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

[Array reply](../../develop/reference/protocol-spec#arrays): a list of fields and their values, or an empty list when key does not exist.

**RESP3:**

[Map reply](../../develop/reference/protocol-spec#maps): a map of fields and their values, or an empty list when key does not exist.



