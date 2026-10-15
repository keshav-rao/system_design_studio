# Redis Strings

```json metadata
{
  "schema_version": 2,
  "title": "Redis Strings",
  "description": "Introduction to Redis strings",
  "categories": ["docs","develop","stack","oss","rs","rc","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"strings-as-counters","title":"Strings as counters"},{"id":"limits","title":"Limits"},{"id":"bitwise-and-bitfield-operations","title":"Bitwise and bitfield operations"},{"id":"performance","title":"Performance"},{"id":"alternatives","title":"Alternatives"},{"id":"learn-more","title":"Learn more"}]}

,
  "codeExamples": [{"codetabsId":"set_tutorial-stepset_get","commands":[{"acl_categories":["@write","@string","@slow"],"complexity":"O(1)","name":"SET"},{"acl_categories":["@read","@string","@fast"],"complexity":"O(1)","name":"GET"}],"description":"Foundational: Set and retrieve string values using SET and GET (overwrites existing values)","difficulty":"beginner","id":"set_get","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_set_tutorial-stepset_get"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_set_tutorial-stepset_get"},{"id":"Node-js","panelId":"panel_Nodejs_set_tutorial-stepset_get"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_set_tutorial-stepset_get"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_set_tutorial-stepset_get"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_set_tutorial-stepset_get"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_set_tutorial-stepset_get"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_set_tutorial-stepset_get"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_set_tutorial-stepset_get"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_set_tutorial-stepset_get"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_set_tutorial-stepset_get"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_set_tutorial-stepset_get"}]},{"buildsUpon":["set_get"],"codetabsId":"set_tutorial-stepsetnx_xx","commands":[{"acl_categories":["@write","@string","@slow"],"complexity":"O(1)","name":"SET"}],"description":"Conditional SET operations: Use NX and XX options to set a key only if it doesn\u0026amp;#39;t exist yet, or only if it already exists","difficulty":"intermediate","id":"setnx_xx","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_set_tutorial-stepsetnx_xx"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_set_tutorial-stepsetnx_xx"},{"id":"Node-js","panelId":"panel_Nodejs_set_tutorial-stepsetnx_xx"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_set_tutorial-stepsetnx_xx"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_set_tutorial-stepsetnx_xx"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_set_tutorial-stepsetnx_xx"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_set_tutorial-stepsetnx_xx"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_set_tutorial-stepsetnx_xx"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_set_tutorial-stepsetnx_xx"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_set_tutorial-stepsetnx_xx"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_set_tutorial-stepsetnx_xx"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_set_tutorial-stepsetnx_xx"}]},{"buildsUpon":["setnx_xx"],"codetabsId":"set_tutorial-stepcas_cad","commands":[{"acl_categories":["@write","@string","@slow"],"complexity":"O(1)","name":"SET"},{"acl_categories":["@read","@string","@fast"],"complexity":"O(1)","name":"GET"},{"acl_categories":["@write","@string","@fast"],"complexity":"O(1)","name":"DELEX"}],"description":"Compare-and-swap and compare-and-delete: Use the IFEQ option with SET and DELEX to update or delete a key only if its value hasn\u0026amp;#39;t changed since you read it","difficulty":"intermediate","id":"cas_cad","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_set_tutorial-stepcas_cad"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_set_tutorial-stepcas_cad"},{"id":"Node-js","panelId":"panel_Nodejs_set_tutorial-stepcas_cad"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_set_tutorial-stepcas_cad"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_set_tutorial-stepcas_cad"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_set_tutorial-stepcas_cad"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_set_tutorial-stepcas_cad"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_set_tutorial-stepcas_cad"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_set_tutorial-stepcas_cad"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_set_tutorial-stepcas_cad"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_set_tutorial-stepcas_cad"}]},{"buildsUpon":["set_get"],"codetabsId":"set_tutorial-stepmset","commands":[{"acl_categories":["@write","@string","@slow"],"complexity":"O(N)","name":"MSET"},{"acl_categories":["@read","@string","@fast"],"complexity":"O(N)","name":"MGET"}],"description":"Set and retrieve multiple values using MSET and MGET when you need to reduce round trips to the server","difficulty":"beginner","id":"mset","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_set_tutorial-stepmset"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_set_tutorial-stepmset"},{"id":"Node-js","panelId":"panel_Nodejs_set_tutorial-stepmset"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_set_tutorial-stepmset"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_set_tutorial-stepmset"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_set_tutorial-stepmset"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_set_tutorial-stepmset"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_set_tutorial-stepmset"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_set_tutorial-stepmset"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_set_tutorial-stepmset"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_set_tutorial-stepmset"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_set_tutorial-stepmset"}]},{"buildsUpon":["set_get"],"codetabsId":"set_tutorial-stepincr","commands":[{"acl_categories":["@write","@string","@slow"],"complexity":"O(1)","name":"SET"},{"acl_categories":["@write","@string","@fast"],"complexity":"O(1)","name":"INCR"},{"acl_categories":["@write","@string","@fast"],"complexity":"O(1)","name":"INCRBY"}],"description":"Atomic counters: Increment string values using INCR and INCRBY when you need thread-safe operations (initializes to 0 if key doesn\u0026amp;#39;t exist)","difficulty":"beginner","id":"incr","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_set_tutorial-stepincr"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_set_tutorial-stepincr"},{"id":"Node-js","panelId":"panel_Nodejs_set_tutorial-stepincr"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_set_tutorial-stepincr"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_set_tutorial-stepincr"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_set_tutorial-stepincr"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_set_tutorial-stepincr"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_set_tutorial-stepincr"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_set_tutorial-stepincr"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_set_tutorial-stepincr"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_set_tutorial-stepincr"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_set_tutorial-stepincr"}]}]
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


### String command summary

**26 commands in this group:**

[View all string commands](https://redis.io/commands/?group=string)

| Command | Summary | Complexity | Since |
|---------|---------|------------|-------|
| [APPEND](https://redis.io/commands/append/) | Appends a string to the value of a key. Creates the key if it doesn't exist. | O(1). The amortized time complexity is O(1) ass... | 2.0.0 |
| [DECR](https://redis.io/commands/decr/) | Decrements the integer value of a key by one. Uses 0 as initial value if the key doesn't exist. | O(1) | 1.0.0 |
| [DECRBY](https://redis.io/commands/decrby/) | Decrements a number from the integer value of a key. Uses 0 as initial value if the key doesn't exist. | O(1) | 1.0.0 |
| [DELEX](https://redis.io/commands/delex/) | Conditionally removes the specified key based on value or digest comparison. | O(1) for IFEQ/IFNE, O(N) for IFDEQ/IFDNE where ... | 8.4.0 |
| [DIGEST](https://redis.io/commands/digest/) | Returns the XXH3 hash of a string value. | O(N) where N is the length of the string value. | 8.4.0 |
| [GET](https://redis.io/commands/get/) | Returns the string value of a key. | O(1) | 1.0.0 |
| [GETDEL](https://redis.io/commands/getdel/) | Returns the string value of a key after deleting the key. | O(1) | 6.2.0 |
| [GETEX](https://redis.io/commands/getex/) | Returns the string value of a key after setting its expiration time. | O(1) | 6.2.0 |
| [GETRANGE](https://redis.io/commands/getrange/) | Returns a substring of the string stored at a key. | O(N) where N is the length of the returned stri... | 2.4.0 |
| [GETSET](https://redis.io/commands/getset/) | Returns the previous string value of a key after setting it to a new value. | O(1) | 1.0.0 |

#### String command summary (part 2)

| Command | Summary | Complexity | Since |
|---------|---------|------------|-------|
| [INCR](https://redis.io/commands/incr/) | Increments the integer value of a key by one. Uses 0 as initial value if the key doesn't exist. | O(1) | 1.0.0 |
| [INCRBY](https://redis.io/commands/incrby/) | Increments the integer value of a key by a number. Uses 0 as initial value if the key doesn't exist. | O(1) | 1.0.0 |
| [INCRBYFLOAT](https://redis.io/commands/incrbyfloat/) | Increment the floating point value of a key by a number. Uses 0 as initial value if the key doesn't exist. | O(1) | 2.6.0 |
| [INCREX](https://redis.io/commands/increx/) | Increments the numeric value of a key by a number and sets its expiration time. Uses 0 as initial value if the key doesn't exist. | O(1) | 8.8.0 |
| [LCS](https://redis.io/commands/lcs/) | Finds the longest common substring. | O(N*M) where N and M are the lengths of s1 and ... | 7.0.0 |
| [MGET](https://redis.io/commands/mget/) | Atomically returns the string values of one or more keys. | O(N) where N is the number of keys to retrieve. | 1.0.0 |
| [MSET](https://redis.io/commands/mset/) | Atomically creates or modifies the string values of one or more keys. | O(N) where N is the number of keys to set. | 1.0.1 |
| [MSETEX](https://redis.io/commands/msetex/) | Atomically sets multiple string keys with a shared expiration in a single operation. Supports flexible argument parsing where condition and expiration flags can appear in any order. | O(N) where N is the number of keys to set. | 8.4.0 |
| [MSETNX](https://redis.io/commands/msetnx/) | Atomically modifies the string values of one or more keys only when all keys don't exist. | O(N) where N is the number of keys to set. | 1.0.1 |
| [PSETEX](https://redis.io/commands/psetex/) | Sets both string value and expiration time in milliseconds of a key. The key is created if it doesn't exist. | O(1) | 2.6.0 |

#### String command summary (part 3)

| Command | Summary | Complexity | Since |
|---------|---------|------------|-------|
| [SET](https://redis.io/commands/set/) | Sets the string value of a key, ignoring its type. The key is created if it doesn't exist. | O(1) | 1.0.0 |
| [SETEX](https://redis.io/commands/setex/) | Sets the string value and expiration time of a key. Creates the key if it doesn't exist. | O(1) | 2.0.0 |
| [SETNX](https://redis.io/commands/setnx/) | Set the string value of a key only when the key doesn't exist. | O(1) | 1.0.0 |
| [SETRANGE](https://redis.io/commands/setrange/) | Overwrites a part of a string value with another by an offset. Creates the key if it doesn't exist. | O(1), not counting the time taken to copy the n... | 2.2.0 |
| [STRLEN](https://redis.io/commands/strlen/) | Returns the length of a string value. | O(1) | 2.2.0 |
| [SUBSTR](https://redis.io/commands/substr/) | Returns a substring from a string value. | O(N) where N is the length of the returned stri... | 1.0.0 |



Redis strings store sequences of bytes, including text, serialized objects, and binary arrays.
As such, strings are the simplest type of value you can associate with a Redis key.
They're often used for caching, but they support additional functionality that lets you implement counters and perform bitwise operations, too.

Since Redis keys are strings, when we use the string type as a value too,
we are mapping a string to another string. The string data type is useful
for a number of use cases, like caching HTML fragments or pages.

Foundational: Set and retrieve string values using SET and GET (overwrites existing values)

**Commands:** SET, GET

**Complexity:**
- SET: O(1)
- GET: O(1)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> SET bike:1 Deimos
OK
> GET bike:1
"Deimos"
```

##### C#

```csharp
        var res1 = db.StringSet("bike:1", "Deimos");
        Console.WriteLine(res1); // true
        var res2 = db.StringGet("bike:1");
        Console.WriteLine(res2); // Deimos
```

##### Go

```go
	res1, err := rdb.Set(ctx, "bike:1", "Deimos", 0).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // >>> OK

	res2, err := rdb.Get(ctx, "bike:1").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2) // >>> Deimos
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> setAndGet = asyncCommands.set("bike:1", "Deimos").thenCompose(v -> {
                System.out.println(v); // >>> OK
                return asyncCommands.get("bike:1");
            })
                    .thenAccept(System.out::println) // >>> Deimos
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> setAndGet = reactiveCommands.set("bike:1", "Deimos").doOnNext(v -> {
                System.out.println(v); // OK
            }).flatMap(v -> reactiveCommands.get("bike:1")).doOnNext(res -> {
                System.out.println(res); // Deimos
            }).then();
```

##### Java (Synchronous - Jedis)

```java
      String res1 = jedis.set("bike:1", "Deimos");
      System.out.println(res1); // OK
      String res2 = jedis.get("bike:1");
      System.out.println(res2); // Deimos
```

##### JavaScript (Node.js)

```javascript
const res1 = await client.set("bike:1", "Deimos");
console.log(res1);  // OK
const res2 = await client.get("bike:1");
console.log(res2);  // Deimos
```

##### PHP

```php
        $res1 = $r->set('bike:1', 'Deimos');
        echo "$res1" . PHP_EOL;
        // >>> OK

        $res2 = $r->get('bike:1');
        echo "$res2" . PHP_EOL;
        // >>> Deimos
```

##### Python

```python
res1 = r.set("bike:1", "Deimos")
print(res1)  # True
res2 = r.get("bike:1")
print(res2)  # Deimos
```

##### Ruby

```ruby
res1 = r.set('bike:1', 'Deimos')
puts res1 # >>> OK

res2 = r.get('bike:1')
puts res2 # >>> Deimos
```

##### Rust (Asynchronous)

```rust
        if let Ok(res) = r.set("bike:1", "Deimos").await {
            let res: String = res;
            println!("{res}");    // >>> OK
        }

        match r.get("bike:1").await {
            Ok(res) => {
                let res: String = res;
                println!("{res}");   // >>> Deimos
            },
            Err(e) => {
                println!("Error getting foo: {e}");
                return;
            }
        };
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.set("bike:1", "Deimos") {
            let res: String = res;
            println!("{res}");    // >>> OK
        }

        match r.get("bike:1") {
            Ok(res) => {
                let res: String = res;
                println!("{res}");   // >>> Deimos
            },
            Err(e) => {
                println!("Error getting bike:1: {e}");
                return;
            }
        };
```



As you can see using the [`SET`](https://redis.io/docs/latest/commands/set) and the [`GET`](https://redis.io/docs/latest/commands/get) commands are the way we set
and retrieve a string value. Note that [`SET`](https://redis.io/docs/latest/commands/set) will replace any existing value
already stored into the key, in the case that the key already exists, even if
the key is associated with a non-string value. So [`SET`](https://redis.io/docs/latest/commands/set) performs an assignment.

Values can be strings (including binary data) of every kind, for instance you
can store a jpeg image inside a value. A value can't be bigger than 512 MB.

The [`SET`](https://redis.io/docs/latest/commands/set) command has interesting options that are provided as additional
arguments. For example, I may ask [`SET`](https://redis.io/docs/latest/commands/set) to fail if the key already exists,
or the opposite, that it only succeed if the key already exists:

Conditional SET operations: Use NX and XX options to set a key only if it doesn't exist yet, or only if it already exists

**Difficulty:** Intermediate

**Builds upon:** set_get

**Commands:** SET

**Complexity:**
- SET: O(1)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
# Recreate the bike:1 key so this example runs on its own.
> SET bike:1 Deimos
OK
> SET bike:1 bike NX
(nil)
> SET bike:1 bike XX
OK
```

##### C#

```csharp
        // Recreate the bike:1 key so this example runs on its own.
        db.StringSet("bike:1", "Deimos");

        var res3 = db.StringSet("bike:1", "bike", when: When.NotExists);
        Console.WriteLine(res3); // false
        Console.WriteLine(db.StringGet("bike:1"));
        var res4 = db.StringSet("bike:1", "bike", when: When.Exists);
        Console.WriteLine(res4); // true
```

##### Go

```go
	// Recreate the bike:1 key so this example runs on its own.
	rdb.Set(ctx, "bike:1", "Deimos", 0)

	res3, err := rdb.SetNX(ctx, "bike:1", "bike", 0).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3) // >>> false

	res4, err := rdb.Get(ctx, "bike:1").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4) // >>> Deimos

	res5, err := rdb.SetXX(ctx, "bike:1", "bike", 0).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res5) // >>> OK
```

##### Java (Asynchronous - Lettuce)

```java
            // Recreate the bike:1 key so this example runs on its own.
            CompletableFuture<Void> setnx = asyncCommands.set("bike:1", "Deimos")
                    .thenCompose(setup -> asyncCommands.setnx("bike:1", "bike")).thenCompose(v -> {
                        System.out.println(v); // >>> false (because key already exists)
                        return asyncCommands.get("bike:1");
                    })
                    .thenAccept(System.out::println) // >>> Deimos (value is unchanged)
                    .toCompletableFuture();
            setnx.join();

            // set the value to "bike" if it already exists
            CompletableFuture<Void> setxx = asyncCommands.set("bike:1", "bike", SetArgs.Builder.xx())
                    .thenAccept(System.out::println) // >>> OK
                    .toCompletableFuture();
            setxx.join();
```

##### Java (Reactive - Lettuce)

```java
            // Recreate the bike:1 key so this example runs on its own.
            Mono<Void> setnx = reactiveCommands.set("bike:1", "Deimos")
                    .flatMap(setup -> reactiveCommands.setnx("bike:1", "bike")).doOnNext(v -> {
                        System.out.println(v); // false (because key already exists)
                    }).flatMap(v -> reactiveCommands.get("bike:1")).doOnNext(res -> {
                        System.out.println(res); // Deimos (value is unchanged)
                    }).then();

            Mono<Void> setxx = reactiveCommands.set("bike:1", "bike", SetArgs.Builder.xx()).doOnNext(res -> {
                System.out.println(res); // OK
            }).then();
```

##### Java (Synchronous - Jedis)

```java
      // Recreate the bike:1 key so this example runs on its own.
      jedis.set("bike:1", "Deimos");

      Long res3 = jedis.setnx("bike:1", "bike");
      System.out.println(res3); // 0 (because key already exists)
      System.out.println(jedis.get("bike:1")); // Deimos (value is unchanged)
      String res4 = jedis.set("bike:1", "bike", SetParams.setParams().xx()); // set the value to "bike" if it
      // already
      // exists
      System.out.println(res4); // OK
```

##### JavaScript (Node.js)

```javascript
// Recreate the bike:1 key so this example runs on its own.
await client.set("bike:1", "Deimos");

const res3 = await client.set("bike:1", "bike", {'NX': true});
console.log(res3);  // null
console.log(await client.get("bike:1"));  // Deimos
const res4 = await client.set("bike:1", "bike", {'XX': true});
console.log(res4);  // OK
```

##### PHP

```php
        // Recreate the bike:1 key so this example runs on its own.
        $r->set('bike:1', 'Deimos');

        $res3 = $r->set('bike:1', 'bike', 'nx');
        echo var_export($res3, true) . PHP_EOL;
        // >>> NULL
        
        echo $r->get('bike:1') . PHP_EOL;
        // >>> Deimos

        $res4 = $r->set('bike:1', 'bike', 'xx');
        echo "$res4" . PHP_EOL;
        // >>> OK
```

##### Python

```python
# Recreate the bike:1 key so this example runs on its own.
r.set("bike:1", "Deimos")

res3 = r.set("bike:1", "bike", nx=True)
print(res3)  # None
print(r.get("bike:1"))  # Deimos
res4 = r.set("bike:1", "bike", xx=True)
print(res4)  # True
```

##### Ruby

```ruby
# Recreate the bike:1 key so this example runs on its own.
r.set('bike:1', 'Deimos')

res3 = r.set('bike:1', 'bike', nx: true)
puts res3 # >>> false

puts r.get('bike:1') # >>> Deimos

res4 = r.set('bike:1', 'bike', xx: true)
puts res4 # >>> true
```

##### Rust (Asynchronous)

```rust
        // Recreate the bike:1 key so this example runs on its own.
        let _: () = r.set("bike:1", "Deimos").await.expect("Failed to set");

        if let Ok(res) = r.set_options("bike:1", "bike", redis::SetOptions::default().conditional_set(ExistenceCheck::NX)).await {
            let res: bool = res;
            println!("{res}");    // >>> false
        }

        match r.get("bike:1").await {
            Ok(res) => {
                let res: String = res;
                println!("{res}");   // >>> Deimos
            },
            Err(e) => {
                println!("Error getting foo: {e}");
                return;
            }
        };

        if let Ok(res) = r.set_options("bike:1", "bike", redis::SetOptions::default().conditional_set(ExistenceCheck::XX)).await {
            let res: String = res;
            println!("{res}");    // >>> OK
        }

        match r.get("bike:1").await {
            Ok(res) => {
                let res: String = res;
                println!("{res}");   // >>> bike
            },
            Err(e) => {
                println!("Error getting foo: {e}");
                return;
            }
        };
```

##### Rust (Synchronous)

```rust
        // Recreate the bike:1 key so this example runs on its own.
        let _: () = r.set("bike:1", "Deimos").expect("Failed to set");

        if let Ok(res) = r.set_options("bike:1", "bike", redis::SetOptions::default().conditional_set(ExistenceCheck::NX)) {
            let res: bool = res;
            println!("{res}");    // >>> false
        }

        match r.get("bike:1") {
            Ok(res) => {
                let res: String = res;
                println!("{res}");   // >>> Deimos
            },
            Err(e) => {
                println!("Error getting bike:1: {e}");
                return;
            }
        };

        if let Ok(res) = r.set_options("bike:1", "bike", redis::SetOptions::default().conditional_set(ExistenceCheck::XX)) {
            let res: String = res;
            println!("{res}");    // >>> OK
        }
        
        match r.get("bike:1") {
            Ok(res) => {
                let res: String = res;
                println!("{res}");   // >>> bike
            },
            Err(e) => {
                println!("Error getting bike:1: {e}");
                return;
            }
        };
```



Starting with Redis 8.4, [`SET`](https://redis.io/docs/latest/commands/set) can also check the key's current value before it writes.
With the `IFEQ` option, `SET` succeeds only if the current value equals the one you pass.
This lets a client update a value it read earlier without overwriting a change that another client made in the meantime, a pattern known as compare-and-swap (CAS).
The [`DELEX`](https://redis.io/docs/latest/commands/delex) command applies the same check to deletion (compare-and-delete):

Compare-and-swap and compare-and-delete: Use the IFEQ option with SET and DELEX to update or delete a key only if its value hasn't changed since you read it

**Difficulty:** Intermediate

**Builds upon:** setnx_xx

**Commands:** SET, GET, DELEX

**Complexity:**
- SET: O(1)
- GET: O(1)
- DELEX: O(1)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> SET bike:1 Deimos
OK
> SET bike:1 Ares IFEQ Deimos
OK
> SET bike:1 Zeus IFEQ Deimos
(nil)
> GET bike:1
"Ares"
> DELEX bike:1 IFEQ Deimos
(integer) 0
> DELEX bike:1 IFEQ Ares
(integer) 1
```

##### C#

```csharp
        db.StringSet("bike:1", "Deimos");

        var res9 = db.StringSet("bike:1", "Ares", when: ValueCondition.Equal("Deimos"));
        Console.WriteLine(res9); // True
        var res10 = db.StringSet("bike:1", "Zeus", when: ValueCondition.Equal("Deimos"));
        Console.WriteLine(res10); // False
        Console.WriteLine(db.StringGet("bike:1")); // Ares

        var res11 = db.StringDelete("bike:1", ValueCondition.Equal("Deimos"));
        Console.WriteLine(res11); // False
        var res12 = db.StringDelete("bike:1", ValueCondition.Equal("Ares"));
        Console.WriteLine(res12); // True
```

##### Go

```go
	rdb.Set(ctx, "bike:1", "Deimos", 0)

	res11, err := rdb.SetIFEQ(ctx, "bike:1", "Ares", "Deimos", 0).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res11) // >>> OK

	// The value no longer matches, so SetIFEQ returns redis.Nil.
	_, err = rdb.SetIFEQ(ctx, "bike:1", "Zeus", "Deimos", 0).Result()

	if err != nil && err != redis.Nil {
		panic(err)
	}

	fmt.Println(err == redis.Nil) // >>> true

	res12, err := rdb.Get(ctx, "bike:1").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res12) // >>> Ares

	res13, err := rdb.DelExArgs(ctx, "bike:1", redis.DelExArgs{
		Mode: "IFEQ", MatchValue: "Deimos",
	}).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res13) // >>> 0

	res14, err := rdb.DelExArgs(ctx, "bike:1", redis.DelExArgs{
		Mode: "IFEQ", MatchValue: "Ares",
	}).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res14) // >>> 1
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> casCad = asyncCommands.set("bike:1", "Deimos")
                    .thenCompose(setup -> asyncCommands.set("bike:1", "Ares",
                            SetArgs.Builder.compareCondition(CompareCondition.valueEq("Deimos"))))
                    .thenCompose(v -> {
                        System.out.println(v); // >>> OK
                        return asyncCommands.set("bike:1", "Zeus",
                                SetArgs.Builder.compareCondition(CompareCondition.valueEq("Deimos")));
                    }).thenCompose(v -> {
                        System.out.println(v); // >>> null
                        return asyncCommands.get("bike:1");
                    }).thenCompose(v -> {
                        System.out.println(v); // >>> Ares
                        return asyncCommands.delex("bike:1", CompareCondition.valueEq("Deimos"));
                    }).thenCompose(v -> {
                        System.out.println(v); // >>> 0
                        return asyncCommands.delex("bike:1", CompareCondition.valueEq("Ares"));
                    })
                    .thenAccept(System.out::println) // >>> 1
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> casCad = reactiveCommands.set("bike:1", "Deimos")
                    .flatMap(setup -> reactiveCommands.set("bike:1", "Ares",
                            SetArgs.Builder.compareCondition(CompareCondition.valueEq("Deimos"))))
                    .doOnNext(res -> {
                        System.out.println(res); // OK
                    })
                    // A failed condition returns an empty Mono, so check for an element.
                    .flatMap(v -> reactiveCommands.set("bike:1", "Zeus",
                            SetArgs.Builder.compareCondition(CompareCondition.valueEq("Deimos"))).hasElement())
                    .doOnNext(res -> {
                        System.out.println(res); // false
                    }).flatMap(v -> reactiveCommands.get("bike:1")).doOnNext(res -> {
                        System.out.println(res); // Ares
                    }).flatMap(v -> reactiveCommands.delex("bike:1", CompareCondition.valueEq("Deimos")))
                    .doOnNext(res -> {
                        System.out.println(res); // 0
                    }).flatMap(v -> reactiveCommands.delex("bike:1", CompareCondition.valueEq("Ares")))
                    .doOnNext(res -> {
                        System.out.println(res); // 1
                    }).then();
```

##### Java (Synchronous - Jedis)

```java
      jedis.set("bike:1", "Deimos");

      String res9 = jedis.set("bike:1", "Ares",
          SetParams.setParams().condition(CompareCondition.valueEq("Deimos")));
      System.out.println(res9); // OK
      String res10 = jedis.set("bike:1", "Zeus",
          SetParams.setParams().condition(CompareCondition.valueEq("Deimos")));
      System.out.println(res10); // null
      System.out.println(jedis.get("bike:1")); // Ares

      long res11 = jedis.delex("bike:1", CompareCondition.valueEq("Deimos"));
      System.out.println(res11); // 0
      long res12 = jedis.delex("bike:1", CompareCondition.valueEq("Ares"));
      System.out.println(res12); // 1
```

##### JavaScript (Node.js)

```javascript
await client.set("bike:1", "Deimos");

const res9 = await client.set("bike:1", "Ares", {
  condition: 'IFEQ', matchValue: "Deimos"
});
console.log(res9);  // OK
const res10 = await client.set("bike:1", "Zeus", {
  condition: 'IFEQ', matchValue: "Deimos"
});
console.log(res10);  // null
console.log(await client.get("bike:1"));  // Ares

const res11 = await client.delEx("bike:1", {
  condition: 'IFEQ', matchValue: "Deimos"
});
console.log(res11);  // 0
const res12 = await client.delEx("bike:1", {
  condition: 'IFEQ', matchValue: "Ares"
});
console.log(res12);  // 1
```

##### PHP

```php
        $r->set('bike:1', 'Deimos');

        $res9 = $r->set('bike:1', 'Ares', null, null, 'IFEQ', 'Deimos');
        echo "$res9" . PHP_EOL;
        // >>> OK

        $res10 = $r->set('bike:1', 'Zeus', null, null, 'IFEQ', 'Deimos');
        echo var_export($res10, true) . PHP_EOL;
        // >>> NULL

        echo $r->get('bike:1') . PHP_EOL;
        // >>> Ares

        $res11 = $r->delex('bike:1', 'IFEQ', 'Deimos');
        echo "$res11" . PHP_EOL;
        // >>> 0

        $res12 = $r->delex('bike:1', 'IFEQ', 'Ares');
        echo "$res12" . PHP_EOL;
        // >>> 1
```

##### Python

```python
r.set("bike:1", "Deimos")

res9 = r.set("bike:1", "Ares", ifeq="Deimos")
print(res9)  # True
res10 = r.set("bike:1", "Zeus", ifeq="Deimos")
print(res10)  # None
print(r.get("bike:1"))  # Ares

res11 = r.delex("bike:1", ifeq="Deimos")
print(res11)  # 0
res12 = r.delex("bike:1", ifeq="Ares")
print(res12)  # 1
```

##### Rust (Asynchronous)

```rust
        let _: () = r.set("bike:1", "Deimos").await.expect("Failed to set");

        let res: Option<String> = r
            .set_options("bike:1", "Ares", redis::SetOptions::default().value_comparison(ValueComparison::ifeq("Deimos")))
            .await.expect("Failed to set");
        println!("{res:?}");    // >>> Some("OK")

        let res: Option<String> = r
            .set_options("bike:1", "Zeus", redis::SetOptions::default().value_comparison(ValueComparison::ifeq("Deimos")))
            .await.expect("Failed to set");
        println!("{res:?}");    // >>> None

        let res: String = r.get("bike:1").await.expect("Failed to get");
        println!("{res}");   // >>> Ares

        let res: usize = r.del_ex("bike:1", ValueComparison::ifeq("Deimos")).await.expect("Failed to delete");
        println!("{res}");    // >>> 0

        let res: usize = r.del_ex("bike:1", ValueComparison::ifeq("Ares")).await.expect("Failed to delete");
        println!("{res}");    // >>> 1
```

##### Rust (Synchronous)

```rust
        let _: () = r.set("bike:1", "Deimos").expect("Failed to set");

        let res: Option<String> = r
            .set_options("bike:1", "Ares", redis::SetOptions::default().value_comparison(ValueComparison::ifeq("Deimos")))
            .expect("Failed to set");
        println!("{res:?}");    // >>> Some("OK")

        let res: Option<String> = r
            .set_options("bike:1", "Zeus", redis::SetOptions::default().value_comparison(ValueComparison::ifeq("Deimos")))
            .expect("Failed to set");
        println!("{res:?}");    // >>> None

        let res: String = r.get("bike:1").expect("Failed to get");
        println!("{res}");   // >>> Ares

        let res: usize = r.del_ex("bike:1", ValueComparison::ifeq("Deimos")).expect("Failed to delete");
        println!("{res}");    // >>> 0

        let res: usize = r.del_ex("bike:1", ValueComparison::ifeq("Ares")).expect("Failed to delete");
        println!("{res}");    // >>> 1
```



The `IFNE` option reverses the check, and the `IFDEQ` and `IFDNE` options compare a hash digest of the value instead of the value itself.
Use [`DIGEST`](https://redis.io/docs/latest/commands/digest) to get the digest of a key's value.

There are a number of other commands for operating on strings. For example
the [`GETSET`](https://redis.io/docs/latest/commands/getset) command sets a key to a new value, returning the old value as the
result. You can use this command, for example, if you have a
system that increments a Redis key using [`INCR`](https://redis.io/docs/latest/commands/incr)
every time your web site receives a new visitor. You may want to collect this
information once every hour, without losing a single increment.
You can [`GETSET`](https://redis.io/docs/latest/commands/getset) the key, assigning it the new value of "0" and reading the
old value back.

The ability to set or retrieve the value of multiple keys in a single
command is also useful for reduced latency. For this reason there are
the [`MSET`](https://redis.io/docs/latest/commands/mset) and [`MGET`](https://redis.io/docs/latest/commands/mget) commands:

Set and retrieve multiple values using MSET and MGET when you need to reduce round trips to the server

**Builds upon:** set_get

**Commands:** MSET, MGET

**Complexity:**
- MSET: O(N)
- MGET: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> MSET bike:1 "Deimos" bike:2 "Ares" bike:3 "Vanth"
OK
> MGET bike:1 bike:2 bike:3
1) "Deimos"
2) "Ares"
3) "Vanth"
```

##### C#

```csharp
        var res5 = db.StringSet([
            new ("bike:1", "Deimos"), new("bike:2", "Ares"), new("bike:3", "Vanth")
        ]);
        Console.WriteLine(res5);
        var res6 = db.StringGet(["bike:1", "bike:2", "bike:3"]);
        Console.WriteLine(string.Join(", ", res6));
```

##### Go

```go
	res6, err := rdb.MSet(ctx, "bike:1", "Deimos", "bike:2", "Ares", "bike:3", "Vanth").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res6) // >>> OK

	res7, err := rdb.MGet(ctx, "bike:1", "bike:2", "bike:3").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res7) // >>> [Deimos Ares Vanth]
```

##### Java (Asynchronous - Lettuce)

```java
            Map<String, String> bikeMap = new HashMap<>();
            bikeMap.put("bike:1", "Deimos");
            bikeMap.put("bike:2", "Ares");
            bikeMap.put("bike:3", "Vanth");

            CompletableFuture<Void> mset = asyncCommands.mset(bikeMap).thenCompose(v -> {
                System.out.println(v); // >>> OK
                return asyncCommands.mget("bike:1", "bike:2", "bike:3");
            })
                    .thenAccept(System.out::println)
                    // >>> [KeyValue[bike:1, Deimos], KeyValue[bike:2, Ares], KeyValue[bike:3,
                    // Vanth]]
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Map<String, String> bikeMap = new HashMap<>();
            bikeMap.put("bike:1", "Deimos");
            bikeMap.put("bike:2", "Ares");
            bikeMap.put("bike:3", "Vanth");

            Mono<Void> mset = reactiveCommands.mset(bikeMap).doOnNext(System.out::println) // OK
                    .flatMap(v -> reactiveCommands.mget("bike:1", "bike:2", "bike:3").collectList()).doOnNext(res -> {
                        System.out.println(res); // [KeyValue[bike:1, Deimos], KeyValue[bike:2, Ares], KeyValue[bike:3, Vanth]]
                    }).then();
```

##### Java (Synchronous - Jedis)

```java
      String res5 = jedis.mset("bike:1", "Deimos", "bike:2", "Ares", "bike:3", "Vanth");
      System.out.println(res5); // OK
      List<String> res6 = jedis.mget("bike:1", "bike:2", "bike:3");
      System.out.println(res6); // [Deimos, Ares, Vanth]
```

##### JavaScript (Node.js)

```javascript
const res5 = await client.mSet([
  ["bike:1", "Deimos"],
  ["bike:2", "Ares"],
  ["bike:3", "Vanth"]
]);

console.log(res5);  // OK
const res6 = await client.mGet(["bike:1", "bike:2", "bike:3"]);
console.log(res6);  // ['Deimos', 'Ares', 'Vanth']
```

##### PHP

```php
        $res5 = $r->mset([
            'bike:1' => 'Deimos', 'bike:2' => 'Ares', 'bike:3' => 'Vanth'
        ]);
        echo "$res5" . PHP_EOL;
        // >>> OK

        $res6 = $r->mget(['bike:1', 'bike:2', 'bike:3']);
        echo json_encode($res6) . PHP_EOL;
        // >>> ["Deimos","Ares","Vanth"]
```

##### Python

```python
res5 = r.mset({"bike:1": "Deimos", "bike:2": "Ares", "bike:3": "Vanth"})
print(res5)  # True
res6 = r.mget(["bike:1", "bike:2", "bike:3"])
print(res6)  # ['Deimos', 'Ares', 'Vanth']
```

##### Ruby

```ruby
res5 = r.mset('bike:1', 'Deimos', 'bike:2', 'Ares', 'bike:3', 'Vanth')
puts res5 # >>> OK

res6 = r.mget('bike:1', 'bike:2', 'bike:3')
puts res6.inspect # >>> ["Deimos", "Ares", "Vanth"]
```

##### Rust (Asynchronous)

```rust
        if let Ok(res) = r.mset(&[("bike:1", "Deimos"), ("bike:2", "Ares"), ("bike:3", "Vanth")]).await {
            let res: String = res;
            println!("{res}");    // >>> OK
        }

        match r.mget(&["bike:1", "bike:2", "bike:3"]).await {
            Ok(res) => {
                let res: Vec<String> = res;
                println!("{res:?}");   // >>> ["Deimos", "Ares", "Vanth"]
            },
            Err(e) => {
                println!("Error getting foo: {e}");
                return;
            }
        };
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.mset(&[("bike:1", "Deimos"), ("bike:2", "Ares"), ("bike:3", "Vanth")]) {
            let res: String = res;
            println!("{res}");    // >>> OK
        }

        match r.mget(&["bike:1", "bike:2", "bike:3"]) {
            Ok(res) => {
                let res: Vec<String> = res;
                println!("{res:?}");   // >>> ["Deimos", "Ares", "Vanth"]
            },
            Err(e) => {
                println!("Error getting values: {e}");
                return;
            }
        };
```



When [`MGET`](https://redis.io/docs/latest/commands/mget) is used, Redis returns an array of values.

## Strings as counters
Even if strings are the basic values of Redis, there are interesting operations
you can perform with them. For instance, one is atomic increment:

Atomic counters: Increment string values using INCR and INCRBY when you need thread-safe operations (initializes to 0 if key doesn't exist)

**Builds upon:** set_get

**Commands:** SET, INCR, INCRBY

**Complexity:**
- SET: O(1)
- INCR: O(1)
- INCRBY: O(1)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> SET total_crashes 0
OK
> INCR total_crashes
(integer) 1
> INCRBY total_crashes 10
(integer) 11
```

##### C#

```csharp
        db.StringSet("total_crashes", 0);
        var res7 = db.StringIncrement("total_crashes");
        Console.WriteLine(res7); // 1
        var res8 = db.StringIncrement("total_crashes", 10);
        Console.WriteLine(res8);
```

##### Go

```go
	res8, err := rdb.Set(ctx, "total_crashes", "0", 0).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res8) // >>> OK

	res9, err := rdb.Incr(ctx, "total_crashes").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res9) // >>> 1

	res10, err := rdb.IncrBy(ctx, "total_crashes", 10).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res10) // >>> 11
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> incrby = asyncCommands.set("total_crashes", "0")
                    .thenCompose(v -> asyncCommands.incr("total_crashes")).thenCompose(v -> {
                        System.out.println(v); // >>> 1
                        return asyncCommands.incrby("total_crashes", 10);
                    })
                    .thenAccept(System.out::println) // >>> 11
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> incrby = reactiveCommands.set("total_crashes", "0").flatMap(v -> reactiveCommands.incr("total_crashes"))
                    .doOnNext(v -> {
                        System.out.println(v); // 1
                    }).flatMap(v -> reactiveCommands.incrby("total_crashes", 10)).doOnNext(res -> {
                        System.out.println(res); // 11
                    }).then();
```

##### Java (Synchronous - Jedis)

```java
      jedis.set("total_crashes", "0");
      Long res7 = jedis.incr("total_crashes");
      System.out.println(res7); // 1
      Long res8 = jedis.incrBy("total_crashes", 10);
      System.out.println(res8); // 11
```

##### JavaScript (Node.js)

```javascript
await client.set("total_crashes", 0);
const res7 = await client.incr("total_crashes");
console.log(res7); // 1
const res8 = await client.incrBy("total_crashes", 10);
console.log(res8); // 11
```

##### PHP

```php
        $r->set('total_crashes', 0);
        $res7 = $r->incr('total_crashes');
        echo "$res7" . PHP_EOL;
        // >>> 1

        $res8 = $r->incrby('total_crashes', 10);
        echo "$res8" . PHP_EOL;
        // >>> 11
```

##### Python

```python
r.set("total_crashes", 0)
res7 = r.incr("total_crashes")
print(res7)  # 1
res8 = r.incrby("total_crashes", 10)
print(res8)  # 11
```

##### Ruby

```ruby
r.set('total_crashes', 0)

res7 = r.incr('total_crashes')
puts res7 # >>> 1

res8 = r.incrby('total_crashes', 10)
puts res8 # >>> 11
```

##### Rust (Asynchronous)

```rust
        if let Ok(res) = r.set("total_crashes", 0).await {
            let res: String = res;
            println!("{res}");    // >>> OK
        }

        if let Ok(res) = r.incr("total_crashes", 1).await {
            let res: i32 = res;
            println!("{res}");    // >>> 1
        }

        if let Ok(res) = r.incr("total_crashes", 10).await {
            let res: i32 = res;
            println!("{res}");    // >>> 11
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.set("total_crashes", 0) {
            let res: String = res;
            println!("{res}");    // >>> OK
        }

        if let Ok(res) = r.incr("total_crashes", 1) {
            let res: i32 = res;
            println!("{res}");    // >>> 1
        }

        if let Ok(res) = r.incr("total_crashes", 10) {
            let res: i32 = res;
            println!("{res}");    // >>> 11
        }
```



The [`INCR`](https://redis.io/docs/latest/commands/incr) command parses the string value as an integer,
increments it by one, and finally sets the obtained value as the new value.
There are other similar commands like [`INCRBY`](https://redis.io/docs/latest/commands/incrby),
[`DECR`](https://redis.io/docs/latest/commands/decr) and [`DECRBY`](https://redis.io/docs/latest/commands/decrby). Internally it's
always the same command, acting in a slightly different way.

What does it mean that INCR is atomic?
That even multiple clients issuing INCR against
the same key will never enter into a race condition. For instance, it will never
happen that client 1 reads "10", client 2 reads "10" at the same time, both
increment to 11, and set the new value to 11. The final value will always be
12 and the read-increment-set operation is performed while all the other
clients are not executing a command at the same time.


## Limits

By default, a single Redis string can be a maximum of 512 MB.

## Bitwise and bitfield operations

To perform bitwise operations on a string, see the [bitmaps data type](https://redis.io/docs/latest/develop/data-types/strings/bitmaps) docs. To store and manipulate integer values within a string, see the [bitfields data type](https://redis.io/docs/latest/develop/data-types/strings/bitfields) docs.

## Performance

Most string operations are O(1), which means they're highly efficient.
However, be careful with the [`SUBSTR`](https://redis.io/docs/latest/commands/substr), [`GETRANGE`](https://redis.io/docs/latest/commands/getrange), and [`SETRANGE`](https://redis.io/docs/latest/commands/setrange) commands, which can be O(n).
These random-access string commands may cause performance issues when dealing with large strings.

## Alternatives

If you're storing structured data as a serialized string, you may also want to consider Redis [hashes](https://redis.io/docs/latest/develop/data-types/hashes) or [JSON](https://redis.io/docs/latest/develop/data-types/json).

## Learn more

* [Redis Strings Explained](https://www.youtube.com/watch?v=7CUt4yWeRQE) is a short, comprehensive video explainer on Redis strings.
* [Redis University's RU101](https://university.redis.com/courses/ru101/) covers Redis strings in detail.

