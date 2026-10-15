# HEXPIRE

```json metadata
{
  "schema_version": 2,
  "title": "HEXPIRE",
  "description": "Set expiration for hash fields using relative time to expire (seconds)",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"},{"display_text":"seconds","name":"seconds","type":"integer"},{"arguments":[{"display_text":"nx","name":"nx","token":"NX","type":"pure-token"},{"display_text":"xx","name":"xx","token":"XX","type":"pure-token"},{"display_text":"gt","name":"gt","token":"GT","type":"pure-token"},{"display_text":"lt","name":"lt","token":"LT","type":"pure-token"}],"name":"condition","optional":true,"type":"oneof"},{"arguments":[{"display_text":"numfields","name":"numfields","type":"integer"},{"display_text":"field","multiple":true,"name":"field","type":"string"}],"name":"fields","token":"FIELDS","type":"block"}],
  "syntax_fmt": "HEXPIRE key seconds [NX | XX | GT | LT] FIELDS numfields field\n  [field ...]",
  "complexity": "O(N) where N is the number of specified fields",
  "group": "hash",
  "command_flags": ["write","denyoom","fast"],
  "acl_categories": ["@write","@hash","@fast"],
  "since": "7.4.0",
  "arity": -6,
  "key_specs": [{"RW":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"},"update":true}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"refreshing-expires","title":"Refreshing expires"},{"id":"redis-search-and-field-expiration","title":"Redis Search and field expiration"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": [{"codetabsId":"cmds_hash-stephexpire","commands":[{"acl_categories":["@write","@hash","@fast"],"complexity":"O(N)","name":"HEXPIRE"},{"acl_categories":["@write","@hash","@fast"],"complexity":"O(1)","name":"HSET"},{"acl_categories":["@read","@hash","@slow"],"complexity":"O(N)","name":"HGETALL"}],"description":"Field expiration: Set TTL on individual hash fields using HEXPIRE with conditional options (NX, XX, GT, LT) when you need fine-grained control over field lifecycle","difficulty":"intermediate","id":"hexpire","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_cmds_hash-stephexpire"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_cmds_hash-stephexpire"},{"id":"Node-js","panelId":"panel_Nodejs_cmds_hash-stephexpire"},{"clientId":"ioredis","clientName":"ioredis","id":"ioredis","langId":"javascript","panelId":"panel_ioredis_cmds_hash-stephexpire"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_cmds_hash-stephexpire"},{"clientId":"lettuce","clientName":"Lettuce","id":"Lettuce-Sync","langId":"java","panelId":"panel_Lettuce-Sync_cmds_hash-stephexpire"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_cmds_hash-stephexpire"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_cmds_hash-stephexpire"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_cmds_hash-stephexpire"},{"clientId":"hiredis","clientName":"hiredis","id":"C","langId":"c","panelId":"panel_C_cmds_hash-stephexpire"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_cmds_hash-stephexpire"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_cmds_hash-stephexpire"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_cmds_hash-stephexpire"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_cmds_hash-stephexpire"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_cmds_hash-stephexpire"}]}]
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

Set an expiration (TTL or time to live) on one or more fields of a given hash key. You must specify at least one field.
Field(s) will automatically be deleted from the hash key when their TTLs expire.

Field expirations will only be cleared by commands that delete or overwrite the
contents of the hash fields, including [`HDEL`](https://redis.io/docs/latest/commands/hdel) and [`HSET`](https://redis.io/docs/latest/commands/hset)
commands.
This means that all the operations that conceptually _alter_ the value stored at a hash key's field without replacing it with a new one will leave the TTL untouched.

You can clear the TTL using the [`HPERSIST`](https://redis.io/docs/latest/commands/hpersist) command, which turns the hash field back into a persistent field.

Note that calling `HEXPIRE`/[`HPEXPIRE`](https://redis.io/docs/latest/commands/hpexpire) with a zero TTL or
[`HEXPIREAT`](https://redis.io/docs/latest/commands/hexpireat)/[`HPEXPIREAT`](https://redis.io/docs/latest/commands/hpexpireat) with a time in the past will result in the hash field being deleted.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key that holds the hash.

</details>

<details open><summary><code>seconds</code></summary>

The time to live, in seconds. Each specified field is deleted after this many seconds.

</details>

<details open><summary><code>FIELDS numfields field [field ...]</code></summary>

The hash fields to set expiration for. `numfields` is the number of fields, followed by that many field names.

</details>

## Optional arguments

The following options modify the command's behavior. They are mutually exclusive.

<details open><summary><code>NX</code></summary>

For each specified field, set expiration only when the field has no expiration.

</details>

<details open><summary><code>XX</code></summary>

For each specified field, set expiration only when the field has an existing expiration.

</details>

<details open><summary><code>GT</code></summary>

For each specified field, set expiration only when the new expiration is greater than the current one. A non-volatile field is treated as an infinite TTL for the purposes of `GT`.

</details>

<details open><summary><code>LT</code></summary>

For each specified field, set expiration only when the new expiration is less than the current one. A non-volatile field is treated as an infinite TTL for the purposes of `LT`.

</details>

## Refreshing expires

You can call `HEXPIRE` using as argument a field that already has an
existing TTL set.
In this case, the time to live is _updated_ to the new value.

## Redis Search and field expiration

Starting with Redis 8, Redis Search has enhanced behavior when handling expiring hash fields. For detailed information about how [`FT.SEARCH`](https://redis.io/docs/latest/commands/ft.search) and [`FT.AGGREGATE`](https://redis.io/docs/latest/commands/ft.aggregate) commands interact with expiring hash fields, see [Key and field expiration behavior](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/expiration).

## Examples

Field expiration: Set TTL on individual hash fields using HEXPIRE with conditional options (NX, XX, GT, LT) when you need fine-grained control over field lifecycle

**Difficulty:** Intermediate

**Commands:** HEXPIRE, HSET, HGETALL

**Complexity:**
- HEXPIRE: O(N)
- HSET: O(1)
- HGETALL: O(N)

**Available in:** Redis CLI, C, C#, Go, Java, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> HEXPIRE no-key 20 NX FIELDS 2 field1 field2
1) (integer) -2
2) (integer) -2
> HSET mykey field1 "hello" field2 "world"
(integer) 2
> HEXPIRE mykey 10 FIELDS 3 field1 field2 field3
1) (integer) 1
2) (integer) 1
3) (integer) -2
> HGETALL mykey
```

##### C

```c
    reply = redisCommand(c, "HSET myhash field1 Hello field2 World");
    freeReplyObject(reply);

    // HEXPIRE needs the field count before the field names.
    reply = redisCommand(c, "HEXPIRE myhash 10 FIELDS 2 field1 field2");
    for (size_t i = 0; i < reply->elements; i++) {
        printf("%lld\n", reply->element[i]->integer);
    }
    // >>> 1
    // >>> 1
    freeReplyObject(reply);

    reply = redisCommand(c, "HTTL myhash FIELDS 2 field1 field2");
    for (size_t i = 0; i < reply->elements; i++) {
        printf("%lld\n", reply->element[i]->integer);
    }
    // >>> 10
    // >>> 10
    freeReplyObject(reply);

    // -2 means the field does not exist.
    reply = redisCommand(c, "HEXPIRE myhash 10 FIELDS 1 nonexistent");
    printf("%lld\n", reply->element[0]->integer);
    // >>> -2
    freeReplyObject(reply);
```

##### C#

```csharp
        // Set up hash with fields
        db.HashSet("myhash",
            [
                new("field1", "Hello"),
                new("field2", "World")
            ]
        );

        ExpireResult[] hexpireRes1 = db.HashFieldExpire(
            "myhash",
            new RedisValue[] { "field1", "field2" },
            TimeSpan.FromSeconds(10)
        );
        Console.WriteLine(string.Join(", ", hexpireRes1));
        // >>> Success, Success

        long[] hexpireRes2 = db.HashFieldGetTimeToLive(
            "myhash",
            new RedisValue[] { "field1", "field2" }
        );
        Console.WriteLine(string.Join(", ", hexpireRes2));
        // >>> 10, 10 (approximately)

        // Try to set expiration on non-existent field
        ExpireResult[] hexpireRes3 = db.HashFieldExpire(
            "myhash",
            new RedisValue[] { "nonexistent" },
            TimeSpan.FromSeconds(10)
        );
        Console.WriteLine(string.Join(", ", hexpireRes3));
        // >>> NoSuchField
```

##### Go

```go
	// Set up hash with fields
	rdb.HSet(ctx, "myhash", "field1", "Hello", "field2", "World")

	// Set expiration on hash fields
	res1, err := rdb.HExpire(ctx, "myhash", 10*time.Second, "field1", "field2").Result()

	if err != nil {
		fmt.Println(err)
	}

	fmt.Println(res1) // >>> [1 1]

	// Check TTL of the fields
	res2, err := rdb.HTTL(ctx, "myhash", "field1", "field2").Result()

	if err != nil {
		fmt.Println(err)
	}

	fmt.Println(len(res2)) // >>> 2

	// Try to set expiration on non-existent field
	res3, err := rdb.HExpire(ctx, "myhash", 10*time.Second, "nonexistent").Result()

	if err != nil {
		fmt.Println(err)
	}

	fmt.Println(res3) // >>> [-2]

	// Clean up
	rdb.Del(ctx, "myhash")
```

##### Java

```java
            // Set up a hash with two fields.
            Map<String, String> hExpireFields = new HashMap<>();
            hExpireFields.put("field1", "Hello");
            hExpireFields.put("field2", "World");

            syncCommands.hset("myhash", hExpireFields);

            // Set the expiration of both fields. `hexpire` returns a status
            // code for each field, where 1 means the expiration was set.
            List<Long> res16 = syncCommands.hexpire("myhash", 10, "field1", "field2");
            System.out.println(res16); // >>> [1, 1]

            // Check the time to live of the fields.
            List<Long> res17 = syncCommands.httl("myhash", "field1", "field2");
            System.out.println(res17); // >>> [10, 10]

            // Try to set the expiration of a field that doesn't exist.
            // The status code -2 means there's no such field.
            List<Long> res18 = syncCommands.hexpire("myhash", 10, "nonexistent");
            System.out.println(res18); // >>> [-2]
```

##### Java (Asynchronous - Lettuce)

```java
            // Set up hash with fields
            Map<String, String> hExpireExampleParams = new HashMap<>();
            hExpireExampleParams.put("field1", "Hello");
            hExpireExampleParams.put("field2", "World");

            CompletableFuture<Void> hExpireExample = asyncCommands.hset("myhash", hExpireExampleParams).thenCompose(res1 -> {
                // Set expiration on hash fields
                return asyncCommands.hexpire("myhash", 10, "field1", "field2");
            }).thenCompose(res2 -> {
                System.out.println(res2);
                // >>> [1, 1]
                // Check TTL of the fields
                return asyncCommands.httl("myhash", "field1", "field2");
            }).thenCompose(res3 -> {
                System.out.println(res3.size());
                // >>> 2
                // Try to set expiration on non-existent field
                return asyncCommands.hexpire("myhash", 10, "nonexistent");
            })
                    .thenAccept(System.out::println)
                    // >>> -2
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            // Set up hash with fields
            Map<String, String> hExpireExampleParams = new HashMap<>();
            hExpireExampleParams.put("field1", "Hello");
            hExpireExampleParams.put("field2", "World");

            Mono<Long> hExpireExample1 = reactiveCommands.hset("myhash", hExpireExampleParams).doOnNext(result -> {
            });

            hExpireExample1.block();

            // Set expiration on hash fields
            Mono<List<Long>> hExpireExample2 = reactiveCommands.hexpire("myhash", 10, "field1", "field2").collectList().doOnNext(result -> {
                System.out.println(result);
                // >>> [1, 1]
            });

            hExpireExample2.block();

            // Check TTL of the fields
            Mono<List<Long>> hExpireExample3 = reactiveCommands.httl("myhash", "field1", "field2").collectList().doOnNext(result -> {
                System.out.println(result.size());
                // >>> 2
            });

            hExpireExample3.block();

            // Try to set expiration on non-existent field
            Mono<List<Long>> hExpireExample4 = reactiveCommands.hexpire("myhash", 10, "nonexistent").collectList().doOnNext(result -> {
                System.out.println(result);
                // >>> [-2]
            });
```

##### Java (Synchronous - Jedis)

```java
        // Set up hash with fields
        Map<String, String> hExpireExampleParams = new HashMap<>();
        hExpireExampleParams.put("field1", "Hello");
        hExpireExampleParams.put("field2", "World");
        jedis.hset("myhash", hExpireExampleParams);

        // Set expiration on hash fields
        List<Long> hExpireResult1 = jedis.hexpire("myhash", 10, "field1", "field2");
        System.out.println(hExpireResult1); // >>> [1, 1]

        // Check TTL of the fields
        List<Long> hExpireResult2 = jedis.httl("myhash", "field1", "field2");
        System.out.println(hExpireResult2.size()); // >>> 2

        // Try to set expiration on non-existent field
        List<Long> hExpireResult3 = jedis.hexpire("myhash", 10, "nonexistent");
        System.out.println(hExpireResult3); // >>> [-2]
```

##### JavaScript (Node.js)

```javascript
// Set up hash with fields
await client.hSet('myhash', {
  'field1': 'Hello',
  'field2': 'World'
})

// Set expiration on hash fields
const res14 = await client.hExpire('myhash', ['field1', 'field2'], 10)
console.log(res14) // [1, 1]

// Check TTL of the fields
const res15 = await client.hTTL('myhash', ['field1', 'field2'])
console.log(res15) // [10, 10] (or close to 10)

// Try to set expiration on non-existent field
const res16 = await client.hExpire('myhash', ['nonexistent'], 10)
console.log(res16) // [-2]

```

##### JavaScript (Node.js)

```javascript
await redis.hset('myhash', { field1: 'Hello', field2: 'World' });

const hexpireRes1 = await redis.hexpire('myhash', 10, 'FIELDS', 2, 'field1', 'field2');
console.log(hexpireRes1); // >>> [ 1, 1 ]

const hexpireRes2 = await redis.httl('myhash', 'FIELDS', 2, 'field1', 'field2');
console.log(hexpireRes2); // >>> [ 10, 10 ]

// -2 means the field does not exist.
const hexpireRes3 = await redis.hexpire('myhash', 10, 'FIELDS', 1, 'nonexistent');
console.log(hexpireRes3); // >>> [ -2 ]
```

##### JavaScript (Node.js)

```javascript
// Set up hash with fields
await client.hSet('myhash', {
  'field1': 'Hello',
  'field2': 'World'
})

// Set expiration on hash fields
const res14 = await client.hExpire('myhash', ['field1', 'field2'], 10)
console.log(res14) // [1, 1]

// Check TTL of the fields
const res15 = await client.hTTL('myhash', ['field1', 'field2'])
console.log(res15) // [10, 10] (or close to 10)

// Try to set expiration on non-existent field
const res16 = await client.hExpire('myhash', ['nonexistent'], 10)
console.log(res16) // [-2]

```

##### JavaScript (Node.js)

```javascript
await redis.hset('myhash', { field1: 'Hello', field2: 'World' });

const hexpireRes1 = await redis.hexpire('myhash', 10, 'FIELDS', 2, 'field1', 'field2');
console.log(hexpireRes1); // >>> [ 1, 1 ]

const hexpireRes2 = await redis.httl('myhash', 'FIELDS', 2, 'field1', 'field2');
console.log(hexpireRes2); // >>> [ 10, 10 ]

// -2 means the field does not exist.
const hexpireRes3 = await redis.hexpire('myhash', 10, 'FIELDS', 1, 'nonexistent');
console.log(hexpireRes3); // >>> [ -2 ]
```

##### PHP

```php

        // Set up hash with fields
        $hExpireResult1 = $this->redis->hmset('myhash', ['field1' => 'Hello', 'field2' => 'World']);
        echo "HMSET myhash field1 Hello field2 World: " . ($hExpireResult1 ? 'OK' : 'FAIL') . "\n"; // >>> OK

        // Set expiration on hash fields
        $hExpireResult2 = $this->redis->hexpire('myhash', 10, ['field1', 'field2']);
        echo "HEXPIRE myhash 10 FIELDS field1 field2: " . json_encode($hExpireResult2) . "\n"; // >>> [1,1]

        // Check TTL of the fields
        $hExpireResult3 = $this->redis->httl('myhash', ['field1', 'field2']);
        echo "HTTL myhash FIELDS field1 field2 count: " . count($hExpireResult3) . "\n"; // >>> 2

        // Try to set expiration on non-existent field
        $hExpireResult4 = $this->redis->hexpire('myhash', 10, ['nonexistent']);
        echo "HEXPIRE myhash 10 FIELDS nonexistent: " . json_encode($hExpireResult4) . "\n"; // >>> [-2]
```

##### Python

```python
# Set up hash with fields
r.hset("myhash", mapping={"field1": "Hello", "field2": "World"})

# Set expiration on hash fields
res12 = r.hexpire("myhash", 10, "field1", "field2")
print(res12)  # >>> [1, 1]

# Check TTL of the fields
res13 = r.httl("myhash", "field1", "field2")
print(res13)  # >>> [10, 10] (or close to 10)

# Try to set expiration on non-existent field
res14 = r.hexpire("myhash", 10, "nonexistent")
print(res14)  # >>> [-2]

```

##### Ruby

```ruby
# Set up a hash with two fields.
r.hset('myhash', { 'field1' => 'Hello', 'field2' => 'World' })

# Set an expiration on both fields.
res16 = r.hexpire('myhash', 10, 'field1', 'field2')
puts res16.inspect # >>> [1, 1]

# Check the TTL of the fields.
res17 = r.httl('myhash', 'field1', 'field2')
puts res17.inspect # >>> [10, 10]

# Try to set an expiration on a field that does not exist.
res18 = r.hexpire('myhash', 10, 'nonexistent')
puts res18.inspect # >>> [-2]
```

##### Rust (Asynchronous)

```rust
        // Set up hash with fields
        let hash_fields = vec![("field1", "Hello"), ("field2", "World")];
        if let Ok(res) = r.hset_multiple("myhash", &hash_fields).await {
            let res: String = res;
            println!("{res}");    // >>> OK
        }

        // Set expiration on hash fields
        match r.hexpire("myhash", 10, redis::ExpireOption::NONE, &["field1", "field2"]).await {
            Ok(res1) => {
                let res1: Vec<i32> = res1;
                println!("{:?}", res1);    // >>> [1, 1]
            },
            Err(e) => {
                println!("Error setting expiration: {e}");
                return;
            }
        }

        // Check TTL of the fields
        match r.httl("myhash", &["field1", "field2"]).await {
            Ok(res2) => {
                let res2: Vec<i32> = res2;
                println!("{}", res2.len());    // >>> 2
            },
            Err(e) => {
                println!("Error getting TTL: {e}");
                return;
            }
        }

        // Try to set expiration on non-existent field
        match r.hexpire("myhash", 10, redis::ExpireOption::NONE, &["nonexistent"]).await {
            Ok(res3) => {
                let res3: Vec<i32> = res3;
                println!("{:?}", res3);    // >>> [-2]
            },
            Err(e) => {
                println!("Error setting expiration on non-existent field: {e}");
                return;
            }
        }

```

##### Rust (Synchronous)

```rust
        // Set up hash with fields
        let hash_fields = vec![("field1", "Hello"), ("field2", "World")];
        if let Ok(res) = r.hset_multiple("myhash", &hash_fields) {
            let res: String = res;
            println!("{res}");    // >>> OK
        }

        // Set expiration on hash fields
        match r.hexpire("myhash", 10, redis::ExpireOption::NONE, &["field1", "field2"]) {
            Ok(res1) => {
                let res1: Vec<i32> = res1;
                println!("{:?}", res1);    // >>> [1, 1]
            },
            Err(e) => {
                println!("Error setting expiration: {e}");
                return;
            }
        }

        // Check TTL of the fields
        match r.httl("myhash", &["field1", "field2"]) {
            Ok(res2) => {
                let res2: Vec<i32> = res2;
                println!("{}", res2.len());    // >>> 2
            },
            Err(e) => {
                println!("Error getting TTL: {e}");
                return;
            }
        }

        // Try to set expiration on non-existent field
        match r.hexpire("myhash", 10, redis::ExpireOption::NONE, &["nonexistent"]) {
            Ok(res3) => {
                let res3: Vec<i32> = res3;
                println!("{:?}", res3);    // >>> [-2]
            },
            Err(e) => {
                println!("Error setting expiration on non-existent field: {e}");
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

One of the following:
* [Array reply](../../develop/reference/protocol-spec#arrays). For each field:
    - [Integer reply](../../develop/reference/protocol-spec#integers): `-2` if no such field exists in the provided hash key, or the provided key does not exist.
    - [Integer reply](../../develop/reference/protocol-spec#integers): `0` if the specified NX | XX | GT | LT condition has not been met.
    - [Integer reply](../../develop/reference/protocol-spec#integers): `1` if the expiration time was set/updated.
    - [Integer reply](../../develop/reference/protocol-spec#integers): `2` when `HEXPIRE`/`HPEXPIRE` is called with 0 seconds/milliseconds or when `HEXPIREAT`/`HPEXPIREAT` is called with a past Unix time in seconds/milliseconds.
* [Simple error reply](../../develop/reference/protocol-spec#simple-errors):
    - if parsing failed, mandatory arguments are missing, unknown arguments are specified, or argument values are of the wrong type or out of range.
    - if the provided key exists but is not a hash.

**RESP3:**

One of the following:
* [Array reply](../../develop/reference/protocol-spec#arrays). For each field:
    - [Integer reply](../../develop/reference/protocol-spec#integers): `-2` if no such field exists in the provided hash key, or the provided key does not exist.
    - [Integer reply](../../develop/reference/protocol-spec#integers): `0` if the specified NX | XX | GT | LT condition has not been met.
    - [Integer reply](../../develop/reference/protocol-spec#integers): `1` if the expiration time was set/updated.
    - [Integer reply](../../develop/reference/protocol-spec#integers): `2` when `HEXPIRE`/`HPEXPIRE` is called with 0 seconds/milliseconds or when `HEXPIREAT`/`HPEXPIREAT` is called with a past Unix time in seconds/milliseconds.
* [Simple error reply](../../develop/reference/protocol-spec#simple-errors):
    - if parsing failed, mandatory arguments are missing, unknown arguments are specified, or argument values are of the wrong type or out of range.
    - if the provided key exists but is not a hash.



