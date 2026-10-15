# Redis bitmaps

```json metadata
{
  "schema_version": 2,
  "title": "Redis bitmaps",
  "description": "Introduction to Redis bitmaps",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"example","title":"Example"},{"children":[{"id":"bitwise-operations","title":"Bitwise operations"}],"id":"bit-operations","title":"Bit Operations"},{"id":"split-bitmaps-into-multiple-keys","title":"Split bitmaps into multiple keys"},{"id":"performance","title":"Performance"},{"id":"learn-more","title":"Learn more"}]}

,
  "codeExamples": [{"codetabsId":"bitmap_tutorial-stepping","commands":[{"acl_categories":["@write","@bitmap","@slow"],"complexity":"O(1)","name":"SETBIT"},{"acl_categories":["@read","@bitmap","@fast"],"complexity":"O(1)","name":"GETBIT"}],"description":"Foundational: Set and get individual bits using SETBIT and GETBIT to track binary states","difficulty":"beginner","id":"ping","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_bitmap_tutorial-stepping"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_bitmap_tutorial-stepping"},{"id":"Node-js","panelId":"panel_Nodejs_bitmap_tutorial-stepping"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_bitmap_tutorial-stepping"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_bitmap_tutorial-stepping"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_bitmap_tutorial-stepping"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_bitmap_tutorial-stepping"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_bitmap_tutorial-stepping"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_bitmap_tutorial-stepping"}]},{"buildsUpon":["ping"],"codetabsId":"bitmap_tutorial-stepbitcount","commands":[{"acl_categories":["@read","@bitmap","@slow"],"complexity":"O(N)","name":"BITCOUNT"}],"description":"Bit counting: Use BITCOUNT to count the number of set bits in a bitmap when you need to get population counts","difficulty":"beginner","id":"bitcount","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_bitmap_tutorial-stepbitcount"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_bitmap_tutorial-stepbitcount"},{"id":"Node-js","panelId":"panel_Nodejs_bitmap_tutorial-stepbitcount"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_bitmap_tutorial-stepbitcount"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_bitmap_tutorial-stepbitcount"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_bitmap_tutorial-stepbitcount"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_bitmap_tutorial-stepbitcount"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_bitmap_tutorial-stepbitcount"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_bitmap_tutorial-stepbitcount"}]},{"buildsUpon":["ping"],"codetabsId":"bitmap_tutorial-stepbitop_setup","commands":[{"acl_categories":["@write","@bitmap","@slow"],"complexity":"O(1)","name":"SETBIT"},{"acl_categories":["@read","@string","@fast"],"complexity":"O(1)","name":"GET"}],"description":"Setup for bitwise operations: Create multiple bitmaps using SETBIT to prepare for demonstrating bitwise operations","difficulty":"intermediate","id":"bitop_setup","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_bitmap_tutorial-stepbitop_setup"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_bitmap_tutorial-stepbitop_setup"},{"id":"Node-js","panelId":"panel_Nodejs_bitmap_tutorial-stepbitop_setup"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_bitmap_tutorial-stepbitop_setup"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_bitmap_tutorial-stepbitop_setup"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_bitmap_tutorial-stepbitop_setup"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_bitmap_tutorial-stepbitop_setup"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_bitmap_tutorial-stepbitop_setup"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_bitmap_tutorial-stepbitop_setup"}]},{"buildsUpon":["bitop_setup"],"codetabsId":"bitmap_tutorial-stepbitop_and","commands":[{"acl_categories":["@write","@bitmap","@slow"],"complexity":"O(N)","name":"BITOP"},{"acl_categories":["@read","@string","@fast"],"complexity":"O(1)","name":"GET"}],"description":"AND operation: Use BITOP AND to find bits set in all source bitmaps when you need to find common bits across multiple sets","difficulty":"intermediate","id":"bitop_and","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_bitmap_tutorial-stepbitop_and"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_bitmap_tutorial-stepbitop_and"},{"id":"Node-js","panelId":"panel_Nodejs_bitmap_tutorial-stepbitop_and"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_bitmap_tutorial-stepbitop_and"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_bitmap_tutorial-stepbitop_and"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_bitmap_tutorial-stepbitop_and"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_bitmap_tutorial-stepbitop_and"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_bitmap_tutorial-stepbitop_and"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_bitmap_tutorial-stepbitop_and"}]},{"buildsUpon":["bitop_setup"],"codetabsId":"bitmap_tutorial-stepbitop_or","commands":[{"acl_categories":["@write","@bitmap","@slow"],"complexity":"O(N)","name":"BITOP"},{"acl_categories":["@read","@string","@fast"],"complexity":"O(1)","name":"GET"}],"description":"OR operation: Use BITOP OR to find bits set in at least one source bitmap when you need to combine multiple sets","difficulty":"intermediate","id":"bitop_or","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_bitmap_tutorial-stepbitop_or"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_bitmap_tutorial-stepbitop_or"},{"id":"Node-js","panelId":"panel_Nodejs_bitmap_tutorial-stepbitop_or"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_bitmap_tutorial-stepbitop_or"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_bitmap_tutorial-stepbitop_or"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_bitmap_tutorial-stepbitop_or"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_bitmap_tutorial-stepbitop_or"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_bitmap_tutorial-stepbitop_or"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_bitmap_tutorial-stepbitop_or"}]},{"buildsUpon":["bitop_setup"],"codetabsId":"bitmap_tutorial-stepbitop_xor","commands":[{"acl_categories":["@write","@bitmap","@slow"],"complexity":"O(N)","name":"BITOP"},{"acl_categories":["@read","@string","@fast"],"complexity":"O(1)","name":"GET"}],"description":"XOR operation: Use BITOP XOR to find bits that differ between bitmaps when you need to identify differences","difficulty":"intermediate","id":"bitop_xor","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_bitmap_tutorial-stepbitop_xor"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_bitmap_tutorial-stepbitop_xor"},{"id":"Node-js","panelId":"panel_Nodejs_bitmap_tutorial-stepbitop_xor"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_bitmap_tutorial-stepbitop_xor"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_bitmap_tutorial-stepbitop_xor"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_bitmap_tutorial-stepbitop_xor"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_bitmap_tutorial-stepbitop_xor"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_bitmap_tutorial-stepbitop_xor"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_bitmap_tutorial-stepbitop_xor"}]},{"buildsUpon":["bitop_setup"],"codetabsId":"bitmap_tutorial-stepbitop_not","commands":[{"acl_categories":["@write","@bitmap","@slow"],"complexity":"O(N)","name":"BITOP"},{"acl_categories":["@read","@string","@fast"],"complexity":"O(1)","name":"GET"}],"description":"NOT operation: Use BITOP NOT to invert all bits in a bitmap when you need to negate a set","difficulty":"intermediate","id":"bitop_not","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_bitmap_tutorial-stepbitop_not"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_bitmap_tutorial-stepbitop_not"},{"id":"Node-js","panelId":"panel_Nodejs_bitmap_tutorial-stepbitop_not"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_bitmap_tutorial-stepbitop_not"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_bitmap_tutorial-stepbitop_not"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_bitmap_tutorial-stepbitop_not"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_bitmap_tutorial-stepbitop_not"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_bitmap_tutorial-stepbitop_not"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_bitmap_tutorial-stepbitop_not"}]},{"buildsUpon":["bitop_setup"],"codetabsId":"bitmap_tutorial-stepbitop_diff","commands":[{"acl_categories":["@write","@bitmap","@slow"],"complexity":"O(N)","name":"BITOP"},{"acl_categories":["@read","@string","@fast"],"complexity":"O(1)","name":"GET"}],"description":"DIFF operation: Use BITOP DIFF to find bits set in the first bitmap but not in others when you need set difference","difficulty":"advanced","id":"bitop_diff","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_bitmap_tutorial-stepbitop_diff"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_bitmap_tutorial-stepbitop_diff"},{"id":"Node-js","panelId":"panel_Nodejs_bitmap_tutorial-stepbitop_diff"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_bitmap_tutorial-stepbitop_diff"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_bitmap_tutorial-stepbitop_diff"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_bitmap_tutorial-stepbitop_diff"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_bitmap_tutorial-stepbitop_diff"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_bitmap_tutorial-stepbitop_diff"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_bitmap_tutorial-stepbitop_diff"}]},{"buildsUpon":["bitop_setup"],"codetabsId":"bitmap_tutorial-stepbitop_diff1","commands":[{"acl_categories":["@write","@bitmap","@slow"],"complexity":"O(N)","name":"BITOP"},{"acl_categories":["@read","@string","@fast"],"complexity":"O(1)","name":"GET"}],"description":"DIFF1 operation: Use BITOP DIFF1 to find bits not in the first bitmap but in at least one other when you need inverse difference","difficulty":"advanced","id":"bitop_diff1","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_bitmap_tutorial-stepbitop_diff1"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_bitmap_tutorial-stepbitop_diff1"},{"id":"Node-js","panelId":"panel_Nodejs_bitmap_tutorial-stepbitop_diff1"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_bitmap_tutorial-stepbitop_diff1"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_bitmap_tutorial-stepbitop_diff1"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_bitmap_tutorial-stepbitop_diff1"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_bitmap_tutorial-stepbitop_diff1"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_bitmap_tutorial-stepbitop_diff1"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_bitmap_tutorial-stepbitop_diff1"}]},{"buildsUpon":["bitop_setup"],"codetabsId":"bitmap_tutorial-stepbitop_andor","commands":[{"acl_categories":["@write","@bitmap","@slow"],"complexity":"O(N)","name":"BITOP"},{"acl_categories":["@read","@string","@fast"],"complexity":"O(1)","name":"GET"}],"description":"ANDOR operation: Use BITOP ANDOR to find bits in the first bitmap and at least one other when you need intersection with union","difficulty":"advanced","id":"bitop_andor","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_bitmap_tutorial-stepbitop_andor"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_bitmap_tutorial-stepbitop_andor"},{"id":"Node-js","panelId":"panel_Nodejs_bitmap_tutorial-stepbitop_andor"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_bitmap_tutorial-stepbitop_andor"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_bitmap_tutorial-stepbitop_andor"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_bitmap_tutorial-stepbitop_andor"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_bitmap_tutorial-stepbitop_andor"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_bitmap_tutorial-stepbitop_andor"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_bitmap_tutorial-stepbitop_andor"}]},{"buildsUpon":["bitop_setup"],"codetabsId":"bitmap_tutorial-stepbitop_one","commands":[{"acl_categories":["@write","@bitmap","@slow"],"complexity":"O(N)","name":"BITOP"},{"acl_categories":["@read","@string","@fast"],"complexity":"O(1)","name":"GET"}],"description":"ONE operation: Use BITOP ONE to find bits set in exactly one bitmap when you need exclusive membership","difficulty":"advanced","id":"bitop_one","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_bitmap_tutorial-stepbitop_one"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_bitmap_tutorial-stepbitop_one"},{"id":"Node-js","panelId":"panel_Nodejs_bitmap_tutorial-stepbitop_one"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_bitmap_tutorial-stepbitop_one"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_bitmap_tutorial-stepbitop_one"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_bitmap_tutorial-stepbitop_one"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_bitmap_tutorial-stepbitop_one"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_bitmap_tutorial-stepbitop_one"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_bitmap_tutorial-stepbitop_one"}]}]
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


### Bitmap/bitfield command summary

**7 commands in this group:**

[View all bitmap commands](https://redis.io/commands/?group=bitmap)

| Command | Summary | Complexity | Since |
|---------|---------|------------|-------|
| [BITCOUNT](https://redis.io/commands/bitcount/) | Counts the number of set bits (population counting) in a string. | O(N) | 2.6.0 |
| [BITFIELD](https://redis.io/commands/bitfield/) | Performs arbitrary bitfield integer operations on strings. | O(1) for each subcommand specified | 3.2.0 |
| [BITFIELD_RO](https://redis.io/commands/bitfield_ro/) | Performs arbitrary read-only bitfield integer operations on strings. | O(1) for each subcommand specified | 6.0.0 |
| [BITOP](https://redis.io/commands/bitop/) | Performs bitwise operations on multiple strings, and stores the result. | O(N) | 2.6.0 |
| [BITPOS](https://redis.io/commands/bitpos/) | Finds the first set (1) or clear (0) bit in a string. | O(N) | 2.8.7 |
| [GETBIT](https://redis.io/commands/getbit/) | Returns a bit value by offset. | O(1) | 2.2.0 |
| [SETBIT](https://redis.io/commands/setbit/) | Sets or clears the bit at offset of the string value. Creates the key if it doesn't exist. | O(1) | 2.2.0 |



Bitmaps are not an actual data type, but a set of bit-oriented operations
defined on the String type which is treated like a bit vector.
Since strings are binary safe blobs and their maximum length is 512 MB,
they are suitable to set up to 2^32 different bits.

You can perform bitwise operations on one or more strings.
Some examples of bitmap use cases include:

* Efficient set representations for cases where the members of a set correspond to the integers 0-N.
* Object permissions, where each bit represents a particular permission, similar to the way that file systems store permissions.

## Example

Suppose you have 1000 cyclists racing through the country-side, with sensors on their bikes labeled 0-999.
You want to quickly determine whether a given sensor has pinged a tracking server within the hour to check in on a rider. 

You can represent this scenario using a bitmap whose key references the current hour.

* Rider 123 pings the server on January 1, 2024 within the 00:00 hour. You can then confirm that rider 123 pinged the server. You can also check to see if rider 456 has pinged the server for that same hour.

Foundational: Set and get individual bits using SETBIT and GETBIT to track binary states

**Commands:** SETBIT, GETBIT

**Complexity:**
- SETBIT: O(1)
- GETBIT: O(1)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python

##### Redis CLI

```
> SETBIT pings:2024-01-01-00:00 123 1
(integer) 0
> GETBIT pings:2024-01-01-00:00 123
1
> GETBIT pings:2024-01-01-00:00 456
0
```

##### C#

```csharp
        bool res1 = db.StringSetBit("pings:2024-01-01-00:00", 123, true);
        Console.WriteLine(res1);    // >>> 0

        bool res2 = db.StringGetBit("pings:2024-01-01-00:00", 123);
        Console.WriteLine(res2);    // >>> True

        bool res3 = db.StringGetBit("pings:2024-01-01-00:00", 456);
        Console.WriteLine(res3);    // >>> False
```

##### Go

```go
	res1, err := rdb.SetBit(ctx, "pings:2024-01-01-00:00", 123, 1).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // >>> 0

	res2, err := rdb.GetBit(ctx, "pings:2024-01-01-00:00", 123).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2) // >>> 1

	res3, err := rdb.GetBit(ctx, "pings:2024-01-01-00:00", 456).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3) // >>> 0
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> ping = async.setbit("pings:2024-01-01-00:00", 123, 1).thenCompose(res1 -> {
                System.out.println(res1); // >>> 0
                return async.getbit("pings:2024-01-01-00:00", 123);
            }).thenCompose(res2 -> {
                System.out.println(res2); // >>> 1
                return async.getbit("pings:2024-01-01-00:00", 456);
            }).thenAccept(res3 -> {
                System.out.println(res3); // >>> 0
            }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> ping = reactive.setbit("pings:2024-01-01-00:00", 123, 1).doOnNext(res1 -> {
                System.out.println(res1); // >>> 0
            }).flatMap(v -> reactive.getbit("pings:2024-01-01-00:00", 123)).doOnNext(res2 -> {
                System.out.println(res2); // >>> 1
            }).flatMap(v -> reactive.getbit("pings:2024-01-01-00:00", 456)).doOnNext(res3 -> {
                System.out.println(res3); // >>> 0
            }).then();
```

##### Java (Synchronous - Jedis)

```java
        boolean res1 = jedis.setbit("pings:2024-01-01-00:00", 123, true);
        System.out.println(res1); // >>> false

        boolean res2 = jedis.getbit("pings:2024-01-01-00:00", 123);
        System.out.println(res2); // >>> true

        boolean res3 = jedis.getbit("pings:2024-01-01-00:00", 456);
        System.out.println(res3); // >>> false
```

##### JavaScript (Node.js)

```javascript
const res1 = await client.setBit("pings:2024-01-01-00:00", 123, 1)
console.log(res1)  // >>> 0

const res2 = await client.getBit("pings:2024-01-01-00:00", 123)
console.log(res2)  // >>> 1

const res3 = await client.getBit("pings:2024-01-01-00:00", 456)
console.log(res3)  // >>> 0
```

##### PHP

```php
        $res1 = $r->setbit('pings:2024-01-01-00:00', 123, 1);
        echo $res1 . PHP_EOL;
        // >>> 0

        $res2 = $r->getbit('pings:2024-01-01-00:00', 123);
        echo $res2 . PHP_EOL;
        // >>> 1

        $res3 = $r->getbit('pings:2024-01-01-00:00', 456);
        echo $res3 . PHP_EOL;
        // >>> 0
```

##### Python

```python
res1 = r.setbit("pings:2024-01-01-00:00", 123, 1)
print(res1)  # >>> 0

res2 = r.getbit("pings:2024-01-01-00:00", 123)
print(res2)  # >>> 1

res3 = r.getbit("pings:2024-01-01-00:00", 456)
print(res3)  # >>> 0
```




## Bit Operations

Bit operations are divided into two groups: constant-time single bit
operations, like setting a bit to 1 or 0, or getting its value, and
operations on groups of bits, for example counting the number of set
bits in a given range of bits (e.g., population counting).

One of the biggest advantages of bitmaps is that they often provide
extreme space savings when storing information. For example in a system
where different users are represented by incremental user IDs, it is possible
to remember a single bit information (for example, knowing whether
a user wants to receive a newsletter) of 4 billion users using just 512 MB of memory.

The [`SETBIT`](https://redis.io/docs/latest/commands/setbit) command takes as its first argument the bit number, and as its second
argument the value to set the bit to, which is 1 or 0. The command
automatically enlarges the string if the addressed bit is outside the
current string length.

[`GETBIT`](https://redis.io/docs/latest/commands/getbit) just returns the value of the bit at the specified index.
Out of range bits (addressing a bit that is outside the length of the string
stored into the target key) are always considered to be zero.

There are three commands operating on group of bits:

1. [`BITOP`](https://redis.io/docs/latest/commands/bitop) performs bit-wise operations between different strings. The provided operators are `AND`, `OR`, `XOR`, `NOT`, `DIFF`, `DIFF1`, `ANDOR`, and `ONE`.
2. [`BITCOUNT`](https://redis.io/docs/latest/commands/bitcount) performs population counting, reporting the number of bits set to 1.
3. [`BITPOS`](https://redis.io/docs/latest/commands/bitpos) finds the first bit having the specified value of 0 or 1.

Both [`BITPOS`](https://redis.io/docs/latest/commands/bitpos) and [`BITCOUNT`](https://redis.io/docs/latest/commands/bitcount) are able to operate with byte ranges of the
string, instead of running for the whole length of the string. We can trivially see the number of bits that have been set in a bitmap.

Bit counting: Use BITCOUNT to count the number of set bits in a bitmap when you need to get population counts

**Builds upon:** ping

**Commands:** BITCOUNT

**Complexity:**
- BITCOUNT: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python

##### Redis CLI

```
> BITCOUNT pings:2024-01-01-00:00
(integer) 1
```

##### C#

```csharp
        bool res4 = db.StringSetBit("pings:2024-01-01-00:00", 123, true);
        long res5 = db.StringBitCount("pings:2024-01-01-00:00");
        Console.WriteLine(res5);    // >>> 1
```

##### Go

```go
	res4, err := rdb.BitCount(ctx, "pings:2024-01-01-00:00",
		&redis.BitCount{
			Start: 0,
			End:   456,
		}).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4) // >>> 1
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> bitcount = async.bitcount("pings:2024-01-01-00:00").thenAccept(res4 -> {
                System.out.println(res4); // >>> 1
            }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> bitcount = reactive.bitcount("pings:2024-01-01-00:00").doOnNext(res4 -> {
                System.out.println(res4); // >>> 1
            }).then();
```

##### Java (Synchronous - Jedis)

```java
        long res4 = jedis.bitcount("pings:2024-01-01-00:00");
        System.out.println(res4); // >>> 1
```

##### JavaScript (Node.js)

```javascript
await client.setBit("pings:2024-01-01-00:00", 123, 1)
const res4 = await client.bitCount("pings:2024-01-01-00:00")
console.log(res4)  // >>> 1
```

##### PHP

```php
        // Ensure the bit is set
        $r->setbit('pings:2024-01-01-00:00', 123, 1);
        $res4 = $r->bitcount('pings:2024-01-01-00:00');
        echo $res4 . PHP_EOL;
        // >>> 1
```

##### Python

```python
r.setbit("pings:2024-01-01-00:00", 123, 1)
res4 = r.bitcount("pings:2024-01-01-00:00")
print(res4)  # >>> 1
```



For example imagine you want to know the longest streak of daily visits of
your web site users. You start counting days starting from zero, that is the
day you made your web site public, and set a bit with [`SETBIT`](https://redis.io/docs/latest/commands/setbit) every time
the user visits the web site. As a bit index you simply take the current unix
time, subtract the initial offset, and divide by the number of seconds in a day
(normally, 3600\*24).

This way for each user you have a small string containing the visit
information for each day. With [`BITCOUNT`](https://redis.io/docs/latest/commands/bitcount) it is possible to easily get
the number of days a given user visited the web site, while with
a few [`BITPOS`](https://redis.io/docs/latest/commands/bitpos) calls, or simply fetching and analyzing the bitmap client-side,
it is possible to easily compute the longest streak.

### Bitwise operations

The [`BITOP`](https://redis.io/docs/latest/commands/bitop) command performs bitwise
operations over two or more source keys, storing the result in a destination key.

The examples below show the available operations using three keys: `A` (with bit pattern
`11011000`), `B` (`00011001`), and `C` (`01101100`).

![Bitop setup](https://redis.io/docs/latest/images/dev/bitmap/BitopSetup.svg)

Numbering the bits from left to right, starting at zero, the following `SETBIT` commands 
will create these bitmaps:

Setup for bitwise operations: Create multiple bitmaps using SETBIT to prepare for demonstrating bitwise operations

**Difficulty:** Intermediate

**Builds upon:** ping

**Commands:** SETBIT, GET

**Complexity:**
- SETBIT: O(1)
- GET: O(1)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python

##### Redis CLI

```
> SETBIT A 0 1
(integer) 0
> SETBIT A 1 1
(integer) 0
> SETBIT A 3 1
(integer) 0
> SETBIT A 4 1
(integer) 0
> GET A
"\xd8"
# Hex value: 0xd8 = 0b11011000

> SETBIT B 3 1
(integer) 0
> SETBIT B 4 1
(integer) 0
> SETBIT B 7 1
(integer) 0
> GET B
"\x19"
# Hex value: 0x19 = 0b00011001

> SETBIT C 1 1
(integer) 0
> SETBIT C 2 1
(integer) 0
> SETBIT C 4 1
(integer) 0
> SETBIT C 5 1
(integer) 0
> GET C
"l"
# ASCII "l" = hex 0x6c = 0b01101100
```

##### C#

```csharp

        // Bitwise operations are not supported in NRedisStack.

```

##### Go

```go
	rdb.SetBit(ctx, "A", 0, 1)
	rdb.SetBit(ctx, "A", 1, 1)
	rdb.SetBit(ctx, "A", 3, 1)
	rdb.SetBit(ctx, "A", 4, 1)
	ba, _ := rdb.Get(ctx, "A").Bytes()
	fmt.Printf("%08b\n", ba[0])
	// >>> 11011000

	rdb.SetBit(ctx, "B", 3, 1)
	rdb.SetBit(ctx, "B", 4, 1)
	rdb.SetBit(ctx, "B", 7, 1)
	bb, _ := rdb.Get(ctx, "B").Bytes()
	fmt.Printf("%08b\n", bb[0])
	// >>> 00011001

	rdb.SetBit(ctx, "C", 1, 1)
	rdb.SetBit(ctx, "C", 2, 1)
	rdb.SetBit(ctx, "C", 4, 1)
	rdb.SetBit(ctx, "C", 5, 1)
	bc, _ := rdb.Get(ctx, "C").Bytes()
	fmt.Printf("%08b\n", bc[0])
	// >>> 01101100
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> setup = async.setbit("A", 0, 1).thenCompose(v -> async.setbit("A", 1, 1))
                    .thenCompose(v -> async.setbit("A", 3, 1)).thenCompose(v -> async.setbit("A", 4, 1))
                    .thenCompose(v -> async.setbit("B", 3, 1)).thenCompose(v -> async.setbit("B", 4, 1))
                    .thenCompose(v -> async.setbit("B", 7, 1)).thenCompose(v -> async.setbit("C", 1, 1))
                    .thenCompose(v -> async.setbit("C", 2, 1)).thenCompose(v -> async.setbit("C", 4, 1))
                    .thenCompose(v -> async.setbit("C", 5, 1)).thenCompose(v -> asyncBytes.get("A".getBytes()))
                    .thenApply(res -> {
                        byte b = (res != null && res.length > 0) ? res[0] : 0;
                        String bitsA = String.format("%8s", Integer.toBinaryString(b & 0xFF)).replace(' ', '0');
                        System.out.println(bitsA); // >>> 11011000
                        return bitsA;
                    }).thenCompose(v -> asyncBytes.get("B".getBytes())).thenApply(res -> {
                        byte b = (res != null && res.length > 0) ? res[0] : 0;
                        String bitsB = String.format("%8s", Integer.toBinaryString(b & 0xFF)).replace(' ', '0');
                        System.out.println(bitsB); // >>> 00011001
                        return bitsB;
                    })
                    // Print C
                    .thenCompose(v -> asyncBytes.get("C".getBytes())).thenAccept(res -> {
                        byte b = (res != null && res.length > 0) ? res[0] : 0;
                        String bitsC = String.format("%8s", Integer.toBinaryString(b & 0xFF)).replace(' ', '0');
                        System.out.println(bitsC); // >>> 01101100
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> setup = reactive.setbit("A", 0, 1).then(reactive.setbit("A", 1, 1)).then(reactive.setbit("A", 3, 1))
                    .then(reactive.setbit("A", 4, 1)).then(reactive.setbit("B", 3, 1)).then(reactive.setbit("B", 4, 1))
                    .then(reactive.setbit("B", 7, 1)).then(reactive.setbit("C", 1, 1)).then(reactive.setbit("C", 2, 1))
                    .then(reactive.setbit("C", 4, 1)).then(reactive.setbit("C", 5, 1)).then(reactiveBytes.get("A".getBytes()))
                    .doOnNext(res -> {
                        byte b = (res != null && res.length > 0) ? res[0] : 0;
                        String bitsA = String.format("%8s", Integer.toBinaryString(b & 0xFF)).replace(' ', '0');
                        System.out.println(bitsA); // >>> 11011000
                    }).then(reactiveBytes.get("B".getBytes())).doOnNext(res -> {
                        byte b = (res != null && res.length > 0) ? res[0] : 0;
                        String bitsB = String.format("%8s", Integer.toBinaryString(b & 0xFF)).replace(' ', '0');
                        System.out.println(bitsB); // >>> 00011001
                    }).then(reactiveBytes.get("C".getBytes())).doOnNext(res -> {
                        byte b = (res != null && res.length > 0) ? res[0] : 0;
                        String bitsC = String.format("%8s", Integer.toBinaryString(b & 0xFF)).replace(' ', '0');
                        System.out.println(bitsC); // >>> 01101100
                    }).then();
```

##### Java (Synchronous - Jedis)

```java
        jedis.setbit("A", 0, true);
        jedis.setbit("A", 1, true);
        jedis.setbit("A", 3, true);
        jedis.setbit("A", 4, true);

        byte[] res5 = jedis.get("A".getBytes());
        System.out.println(String.format("%8s", Integer.toBinaryString(res5[0] & 0xFF)).replace(' ', '0'));
        // >>> 11011000

        jedis.setbit("B", 3, true);
        jedis.setbit("B", 4, true);
        jedis.setbit("B", 7, true);

        byte[] res6 = jedis.get("B".getBytes());
        System.out.println(String.format("%8s", Integer.toBinaryString(res6[0] & 0xFF)).replace(' ', '0'));
        // >>> 00011001

        jedis.setbit("C", 1, true);
        jedis.setbit("C", 2, true);
        jedis.setbit("C", 4, true);
        jedis.setbit("C", 5, true);

        byte[] res7 = jedis.get("C".getBytes());
        System.out.println(String.format("%8s", Integer.toBinaryString(res7[0] & 0xFF)).replace(' ', '0'));
        // >>> 01101100
```

##### JavaScript (Node.js)

```javascript
await client.setBit("A", 0, 1)
await client.setBit("A", 1, 1)
await client.setBit("A", 3, 1)
await client.setBit("A", 4, 1)

const res5 = await client.get("A")
console.log(res5.readUInt8(0).toString(2).padStart(8, '0'))
// >>> 11011000

await client.setBit("B", 3, 1)
await client.setBit("B", 4, 1)
await client.setBit("B", 7, 1)

const res6 = await client.get("B")
console.log(res6.readUInt8(0).toString(2).padStart(8, '0'))
// >>> 00011001

await client.setBit("C", 1, 1)
await client.setBit("C", 2, 1)
await client.setBit("C", 4, 1)
await client.setBit("C", 5, 1)

const res7 = await client.get("C")
console.log(res7.readUInt8(0).toString(2).padStart(8, '0'))
// >>> 01101100
```

##### PHP

```php
        $r->setbit('A', 0, 1);
        $r->setbit('A', 1, 1);
        $r->setbit('A', 3, 1);
        $r->setbit('A', 4, 1);

        $res5 = $r->get('A');
        echo str_pad(decbin(ord($res5)), 8, '0', STR_PAD_LEFT) . PHP_EOL;
        // >>> 11011000

        $r->setbit('B', 3, 1);
        $r->setbit('B', 4, 1);
        $r->setbit('B', 7, 1);

        $res6 = $r->get('B');
        echo str_pad(decbin(ord($res6)), 8, '0', STR_PAD_LEFT) . PHP_EOL;
        // >>> 00011001

        $r->setbit('C', 1, 1);
        $r->setbit('C', 2, 1);
        $r->setbit('C', 4, 1);
        $r->setbit('C', 5, 1);

        $res7 = $r->get('C');
        echo str_pad(decbin(ord($res7)), 8, '0', STR_PAD_LEFT) . PHP_EOL;
        // >>> 01101100
```

##### Python

```python
r.setbit("A", 0, 1)
r.setbit("A", 1, 1)
r.setbit("A", 3, 1)
r.setbit("A", 4, 1)

res5 = r.get("A")
print("{:08b}".format(int.from_bytes(res5, "big")))
# >>> 11011000

r.setbit("B", 3, 1)
r.setbit("B", 4, 1)
r.setbit("B", 7, 1)

res6 = r.get("B")
print("{:08b}".format(int.from_bytes(res6, "big")))
# >>> 00011001

r.setbit("C", 1, 1)
r.setbit("C", 2, 1)
r.setbit("C", 4, 1)
r.setbit("C", 5, 1)

res7 = r.get("C")
print("{:08b}".format(int.from_bytes(res7, "big")))
# >>> 01101100
```



#### `AND`

Set a bit in the destination key to 1 only if it is set in all the source keys.

![Bitop AND](https://redis.io/docs/latest/images/dev/bitmap/BitopAnd.svg)

AND operation: Use BITOP AND to find bits set in all source bitmaps when you need to find common bits across multiple sets

**Difficulty:** Intermediate

**Builds upon:** bitop_setup

**Commands:** BITOP, GET

**Complexity:**
- BITOP: O(N)
- GET: O(1)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python

##### Redis CLI

```
> BITOP AND R A B C
(integer) 1
> GET R
"\b"
# ASCII "\b" (backspace) = hex 0x08 = 0b00001000
```

##### C#

```csharp

        // Bitwise operations are not supported in NRedisStack.

```

##### Go

```go
	rdb.BitOpAnd(ctx, "R", "A", "B", "C")
	br, _ := rdb.Get(ctx, "R").Bytes()
	fmt.Printf("%08b\n", br[0])
	// >>> 00001000
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> andOp = async.bitopAnd("R", "A", "B", "C")
                    .thenCompose(len -> asyncBytes.get("R".getBytes())).thenAccept(res -> {
                        byte b = (res != null && res.length > 0) ? res[0] : 0;
                        String bits = String.format("%8s", Integer.toBinaryString(b & 0xFF)).replace(' ', '0');
                        System.out.println(bits); // >>> 00001000
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> andOp = reactive.bitopAnd("R", "A", "B", "C").then(reactiveBytes.get("R".getBytes())).doOnNext(res -> {
                byte b = (res != null && res.length > 0) ? res[0] : 0;
                String bits = String.format("%8s", Integer.toBinaryString(b & 0xFF)).replace(' ', '0');
                System.out.println(bits); // >>> 00001000
            }).then();
```

##### Java (Synchronous - Jedis)

```java
        jedis.bitop(BitOP.AND, "R", "A", "B", "C");
        byte[] res8 = jedis.get("R".getBytes());
        System.out.println(String.format("%8s", Integer.toBinaryString(res8[0] & 0xFF)).replace(' ', '0'));
        // >>> 00001000
```

##### JavaScript (Node.js)

```javascript
await client.bitOp("AND", "R", ["A", "B", "C"])
const res8 = await client.get("R")
console.log(res8.readUInt8(0).toString(2).padStart(8, '0'))
// >>> 00001000
```

##### PHP

```php
        $r->bitop('AND', 'R', 'A', 'B', 'C');
        $res8 = $r->get('R');
        echo str_pad(decbin(ord($res8)), 8, '0', STR_PAD_LEFT) . PHP_EOL;
        // >>> 00001000
```

##### Python

```python
r.bitop("AND", "R", "A", "B", "C")
res8 = r.get("R")
print("{:08b}".format(int.from_bytes(res8, "big")))
# >>> 00001000
```



#### `OR`
Set a bit in the destination key to 1 if it is set in at least one of the source keys.

![Bitop OR](https://redis.io/docs/latest/images/dev/bitmap/BitopOr.svg)

OR operation: Use BITOP OR to find bits set in at least one source bitmap when you need to combine multiple sets

**Difficulty:** Intermediate

**Builds upon:** bitop_setup

**Commands:** BITOP, GET

**Complexity:**
- BITOP: O(N)
- GET: O(1)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python

##### Redis CLI

```
> BITOP OR R A B C
(integer) 1
> GET R
"\xfd"
# Hex value: 0xfd = 0b11111101
```

##### C#

```csharp

        // Bitwise operations are not supported in NRedisStack.

```

##### Go

```go
	rdb.BitOpOr(ctx, "R", "A", "B", "C")
	br, _ = rdb.Get(ctx, "R").Bytes()
	fmt.Printf("%08b\n", br[0])
	// >>> 11111101
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> orOp = async.bitopOr("R", "A", "B", "C").thenCompose(len -> asyncBytes.get("R".getBytes()))
                    .thenAccept(res -> {
                        byte b = (res != null && res.length > 0) ? res[0] : 0;
                        String bits = String.format("%8s", Integer.toBinaryString(b & 0xFF)).replace(' ', '0');
                        System.out.println(bits); // >>> 11111101
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> orOp = reactive.bitopOr("R", "A", "B", "C").then(reactiveBytes.get("R".getBytes())).doOnNext(res -> {
                byte b = (res != null && res.length > 0) ? res[0] : 0;
                String bits = String.format("%8s", Integer.toBinaryString(b & 0xFF)).replace(' ', '0');
                System.out.println(bits); // >>> 11111101
            }).then();
```

##### Java (Synchronous - Jedis)

```java
        jedis.bitop(BitOP.OR, "R", "A", "B", "C");
        byte[] res9 = jedis.get("R".getBytes());
        System.out.println(String.format("%8s", Integer.toBinaryString(res9[0] & 0xFF)).replace(' ', '0'));
        // >>> 11111101
```

##### JavaScript (Node.js)

```javascript
await client.bitOp("OR", "R", ["A", "B", "C"])
const res9 = await client.get("R")
console.log(res9.readUInt8(0).toString(2).padStart(8, '0'))
// >>> 11111101
```

##### PHP

```php
        $r->bitop('OR', 'R', 'A', 'B', 'C');
        $res9 = $r->get('R');
        echo str_pad(decbin(ord($res9)), 8, '0', STR_PAD_LEFT) . PHP_EOL;
        // >>> 11111101
```

##### Python

```python
r.bitop("OR", "R", "A", "B", "C")
res9 = r.get("R")
print("{:08b}".format(int.from_bytes(res9, "big")))
# >>> 11111101
```



#### `XOR`

For two source keys, set a bit in the destination key to 1 if the value of the bit is 
different in the two keys. For three or more source keys, the result of XORing the first two 
keys is then XORed with the next key, and so forth.

![Bitop XOR](https://redis.io/docs/latest/images/dev/bitmap/BitopXor.svg)

XOR operation: Use BITOP XOR to find bits that differ between bitmaps when you need to identify differences

**Difficulty:** Intermediate

**Builds upon:** bitop_setup

**Commands:** BITOP, GET

**Complexity:**
- BITOP: O(N)
- GET: O(1)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python

##### Redis CLI

```
> BITOP XOR R A B
(integer) 1
> GET R
"\xc1"
# Hex value: 0xc1 = 0b11000001
```

##### C#

```csharp

        // Bitwise operations are not supported in NRedisStack.

```

##### Go

```go
	rdb.BitOpXor(ctx, "R", "A", "B")
	br, _ = rdb.Get(ctx, "R").Bytes()
	fmt.Printf("%08b\n", br[0])
	// >>> 11000001
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> xorOp = async.bitopXor("R", "A", "B").thenCompose(len -> asyncBytes.get("R".getBytes()))
                    .thenAccept(res -> {
                        byte b = (res != null && res.length > 0) ? res[0] : 0;
                        String bits = String.format("%8s", Integer.toBinaryString(b & 0xFF)).replace(' ', '0');
                        System.out.println(bits); // >>> 11000001
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> xorOp = reactive.bitopXor("R", "A", "B").then(reactiveBytes.get("R".getBytes())).doOnNext(res -> {
                byte b = (res != null && res.length > 0) ? res[0] : 0;
                String bits = String.format("%8s", Integer.toBinaryString(b & 0xFF)).replace(' ', '0');
                System.out.println(bits); // >>> 11000001
            }).then();
```

##### Java (Synchronous - Jedis)

```java
        jedis.bitop(BitOP.XOR, "R", "A", "B");
        byte[] res10 = jedis.get("R".getBytes());
        System.out.println(String.format("%8s", Integer.toBinaryString(res10[0] & 0xFF)).replace(' ', '0'));
        // >>> 11000001
```

##### JavaScript (Node.js)

```javascript
await client.bitOp("XOR", "R", ["A", "B"]) // XOR uses two keys here
const res10 = await client.get("R")
console.log(res10.readUInt8(0).toString(2).padStart(8, '0'))
// >>> 11000001
```

##### PHP

```php
        $r->bitop('XOR', 'R', 'A', 'B');
        $res10 = $r->get('R');
        echo str_pad(decbin(ord($res10)), 8, '0', STR_PAD_LEFT) . PHP_EOL;
        // >>> 11000001
```

##### Python

```python
r.bitop("XOR", "R", "A", "B")
res10 = r.get("R")
print("{:08b}".format(int.from_bytes(res10, "big")))
# >>> 11000001
```



#### `NOT`

Set a bit in the destination key to 1 if it is not set in the source key (this
is the only unary operator).

![Bitop NOT](https://redis.io/docs/latest/images/dev/bitmap/BitopNot.svg)

NOT operation: Use BITOP NOT to invert all bits in a bitmap when you need to negate a set

**Difficulty:** Intermediate

**Builds upon:** bitop_setup

**Commands:** BITOP, GET

**Complexity:**
- BITOP: O(N)
- GET: O(1)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python

##### Redis CLI

```
> BITOP NOT R A
(integer) 1
> GET R
"'"
# ASCII "'" (single quote) = hex 0x27 = 0b00100111
```

##### C#

```csharp

        // Bitwise operations are not supported in NRedisStack.

```

##### Go

```go
	rdb.BitOpNot(ctx, "R", "A")
	br, _ = rdb.Get(ctx, "R").Bytes()
	fmt.Printf("%08b\n", br[0])
	// >>> 00100111
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> notOp = async.bitopNot("R", "A").thenCompose(len -> asyncBytes.get("R".getBytes()))
                    .thenAccept(res -> {
                        byte b = (res != null && res.length > 0) ? res[0] : 0;
                        String bits = String.format("%8s", Integer.toBinaryString(b & 0xFF)).replace(' ', '0');
                        System.out.println(bits); // >>> 00100111
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> notOp = reactive.bitopNot("R", "A").then(reactiveBytes.get("R".getBytes())).doOnNext(res -> {
                byte b = (res != null && res.length > 0) ? res[0] : 0;
                String bits = String.format("%8s", Integer.toBinaryString(b & 0xFF)).replace(' ', '0');
                System.out.println(bits); // >>> 00100111
            }).then();
```

##### Java (Synchronous - Jedis)

```java
        jedis.bitop(BitOP.NOT, "R", "A");
        byte[] res11 = jedis.get("R".getBytes());
        System.out.println(String.format("%8s", Integer.toBinaryString(res11[0] & 0xFF)).replace(' ', '0'));
        // >>> 00100111
```

##### JavaScript (Node.js)

```javascript
await client.bitOp("NOT", "R", "A")
const res11 = await client.get("R")
console.log(res11.readUInt8(0).toString(2).padStart(8, '0'))
// >>> 00100111
```

##### PHP

```php
        $r->bitop('NOT', 'R', 'A');
        $res11 = $r->get('R');
        echo str_pad(decbin(ord($res11)), 8, '0', STR_PAD_LEFT) . PHP_EOL;
        // >>> 00100111
```

##### Python

```python
r.bitop("NOT", "R", "A")
res11 = r.get("R")
print("{:08b}".format(int.from_bytes(res11, "big")))
# >>> 00100111
```



#### `DIFF`

Set a bit in the destination key to 1 if it is set in the first source key, but not in any 
of the other source keys.

![Bitop DIFF](https://redis.io/docs/latest/images/dev/bitmap/BitopDiff.svg)

DIFF operation: Use BITOP DIFF to find bits set in the first bitmap but not in others when you need set difference

**Difficulty:** Advanced

**Builds upon:** bitop_setup

**Commands:** BITOP, GET

**Complexity:**
- BITOP: O(N)
- GET: O(1)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python

##### Redis CLI

```
> BITOP DIFF R A B C
(integer) 1
> GET R
"\x80"
# Hex value: 0x80 = 0b10000000
```

##### C#

```csharp

        // Bitwise operations are not supported in NRedisStack.

```

##### Go

```go
	rdb.BitOpDiff(ctx, "R", "A", "B", "C")
	br, _ = rdb.Get(ctx, "R").Bytes()
	fmt.Printf("%08b\n", br[0])
	// >>> 10000000
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> diffOp = async.bitopDiff("R", "A", "B", "C")
                    .thenCompose(len -> asyncBytes.get("R".getBytes())).thenAccept(res -> {
                        byte b = (res != null && res.length > 0) ? res[0] : 0;
                        String bits = String.format("%8s", Integer.toBinaryString(b & 0xFF)).replace(' ', '0');
                        System.out.println(bits); // >>> 10000000
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> diffOp = reactive.bitopDiff("R", "A", "B", "C").then(reactiveBytes.get("R".getBytes())).doOnNext(res -> {
                byte b = (res != null && res.length > 0) ? res[0] : 0;
                String bits = String.format("%8s", Integer.toBinaryString(b & 0xFF)).replace(' ', '0');
                System.out.println(bits); // >>> 10000000
            }).then();
```

##### Java (Synchronous - Jedis)

```java
        jedis.bitop(BitOP.DIFF, "R", "A", "B", "C");
        byte[] res12 = jedis.get("R".getBytes());
        System.out.println(String.format("%8s", Integer.toBinaryString(res12[0] & 0xFF)).replace(' ', '0'));
        // >>> 10000000
```

##### JavaScript (Node.js)

```javascript
await client.bitOp("DIFF", "R", ["A", "B", "C"])
const res12 = await client.get("R")
console.log(res12.readUInt8(0).toString(2).padStart(8, '0'))
// >>> 10000000
```

##### PHP

```php
        $r->bitop('DIFF', 'R', 'A', 'B', 'C');
        $res12 = $r->get('R');
        echo str_pad(decbin(ord($res12)), 8, '0', STR_PAD_LEFT) . PHP_EOL;
        // >>> 10000000
```

##### Python

```python
r.bitop("DIFF", "R", "A", "B", "C")
res12 = r.get("R")
print("{:08b}".format(int.from_bytes(res12, "big")))
# >>> 10000000
```



#### `DIFF1`

Set a bit in the destination key to 1 if it is not set in the first source key, 
but set in at least one of the other source keys.

![Bitop DIFF1](https://redis.io/docs/latest/images/dev/bitmap/BitopDiff1.svg)

DIFF1 operation: Use BITOP DIFF1 to find bits not in the first bitmap but in at least one other when you need inverse difference

**Difficulty:** Advanced

**Builds upon:** bitop_setup

**Commands:** BITOP, GET

**Complexity:**
- BITOP: O(N)
- GET: O(1)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python

##### Redis CLI

```
> BITOP DIFF1 R A B C
(integer) 1
> GET R
"%"
# ASCII "%" (percent) = hex 0x25 = 0b00100101
```

##### C#

```csharp

        // Bitwise operations are not supported in NRedisStack.

```

##### Go

```go
	rdb.BitOpDiff1(ctx, "R", "A", "B", "C")
	br, _ = rdb.Get(ctx, "R").Bytes()
	fmt.Printf("%08b\n", br[0])
	// >>> 00100101
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> diff1Op = async.bitopDiff1("R", "A", "B", "C")
                    .thenCompose(len -> asyncBytes.get("R".getBytes())).thenAccept(res -> {
                        byte b = (res != null && res.length > 0) ? res[0] : 0;
                        String bits = String.format("%8s", Integer.toBinaryString(b & 0xFF)).replace(' ', '0');
                        System.out.println(bits); // >>> 00100101
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> diff1Op = reactive.bitopDiff1("R", "A", "B", "C").then(reactiveBytes.get("R".getBytes()))
                    .doOnNext(res -> {
                        byte b = (res != null && res.length > 0) ? res[0] : 0;
                        String bits = String.format("%8s", Integer.toBinaryString(b & 0xFF)).replace(' ', '0');
                        System.out.println(bits); // >>> 00100101
                    }).then();
```

##### Java (Synchronous - Jedis)

```java
        jedis.bitop(BitOP.DIFF1, "R", "A", "B", "C");
        byte[] res13 = jedis.get("R".getBytes());
        System.out.println(String.format("%8s", Integer.toBinaryString(res13[0] & 0xFF)).replace(' ', '0'));
        // >>> 00100101
```

##### JavaScript (Node.js)

```javascript
await client.bitOp("DIFF1", "R", ["A", "B", "C"])
const res13 = await client.get("R")
console.log(res13.readUInt8(0).toString(2).padStart(8, '0'))
// >>> 00100101
```

##### PHP

```php
        $r->bitop('DIFF1', 'R', 'A', 'B', 'C');
        $res13 = $r->get('R');
        echo str_pad(decbin(ord($res13)), 8, '0', STR_PAD_LEFT) . PHP_EOL;
        // >>> 00100101
```

##### Python

```python
r.bitop("DIFF1", "R", "A", "B", "C")
res13 = r.get("R")
print("{:08b}".format(int.from_bytes(res13, "big")))
# >>> 00100101
```



#### `ANDOR`

Set a bit in the destination key to 1 if it is set in the first source key and also in at least one of the other source keys.

![Bitop ANDOR](https://redis.io/docs/latest/images/dev/bitmap/BitopAndOr.svg)

ANDOR operation: Use BITOP ANDOR to find bits in the first bitmap and at least one other when you need intersection with union

**Difficulty:** Advanced

**Builds upon:** bitop_setup

**Commands:** BITOP, GET

**Complexity:**
- BITOP: O(N)
- GET: O(1)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python

##### Redis CLI

```
> BITOP ANDOR R A B C
(integer) 1
> GET R
"X"
# ASCII "X" = hex 0x58 = 0b01011000
```

##### C#

```csharp

        // Bitwise operations are not supported in NRedisStack.

```

##### Go

```go
	rdb.BitOpAndOr(ctx, "R", "A", "B", "C")
	br, _ = rdb.Get(ctx, "R").Bytes()
	fmt.Printf("%08b\n", br[0])
	// >>> 01011000
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> andorOp = async.bitopAndor("R", "A", "B", "C")
                    .thenCompose(len -> asyncBytes.get("R".getBytes())).thenAccept(res -> {
                        byte b = (res != null && res.length > 0) ? res[0] : 0;
                        String bits = String.format("%8s", Integer.toBinaryString(b & 0xFF)).replace(' ', '0');
                        System.out.println(bits); // >>> 01011000
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> andorOp = reactive.bitopAndor("R", "A", "B", "C").then(reactiveBytes.get("R".getBytes()))
                    .doOnNext(res -> {
                        byte b = (res != null && res.length > 0) ? res[0] : 0;
                        String bits = String.format("%8s", Integer.toBinaryString(b & 0xFF)).replace(' ', '0');
                        System.out.println(bits); // >>> 01011000
                    }).then();
```

##### Java (Synchronous - Jedis)

```java
        jedis.bitop(BitOP.ANDOR, "R", "A", "B", "C");
        byte[] res14 = jedis.get("R".getBytes());
        System.out.println(String.format("%8s", Integer.toBinaryString(res14[0] & 0xFF)).replace(' ', '0'));
        // >>> 01011000
```

##### JavaScript (Node.js)

```javascript
await client.bitOp("ANDOR", "R", ["A", "B", "C"])
const res14 = await client.get("R")
console.log(res14.readUInt8(0).toString(2).padStart(8, '0'))
// >>> 01011000
```

##### PHP

```php
        $r->bitop('ANDOR', 'R', 'A', 'B', 'C');
        $res14 = $r->get('R');
        echo str_pad(decbin(ord($res14)), 8, '0', STR_PAD_LEFT) . PHP_EOL;
        // >>> 01011000
```

##### Python

```python
r.bitop("ANDOR", "R", "A", "B", "C")
res14 = r.get("R")
print("{:08b}".format(int.from_bytes(res14, "big")))
# >>> 01011000
```



#### `ONE`

Set a bit in the destination key to 1 if it is set in exactly one of the source keys.

![Bitop ONE](https://redis.io/docs/latest/images/dev/bitmap/BitopOne.svg)

ONE operation: Use BITOP ONE to find bits set in exactly one bitmap when you need exclusive membership

**Difficulty:** Advanced

**Builds upon:** bitop_setup

**Commands:** BITOP, GET

**Complexity:**
- BITOP: O(N)
- GET: O(1)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python

##### Redis CLI

```
> BITOP ONE R A B C
(integer) 1
> GET R
"\xa5"
# Hex value: 0xa5 = 0b10100101
```

##### C#

```csharp

        // Bitwise operations are not supported in NRedisStack.

```

##### Go

```go
	rdb.BitOpOne(ctx, "R", "A", "B", "C")
	br, _ = rdb.Get(ctx, "R").Bytes()
	fmt.Printf("%08b\n", br[0])
	// >>> 10100101
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> oneOp = async.bitopOne("R", "A", "B", "C")
                    .thenCompose(len -> asyncBytes.get("R".getBytes())).thenAccept(res -> {
                        byte b = (res != null && res.length > 0) ? res[0] : 0;
                        String bits = String.format("%8s", Integer.toBinaryString(b & 0xFF)).replace(' ', '0');
                        System.out.println(bits); // >>> 10100101
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> oneOp = reactive.bitopOne("R", "A", "B", "C").then(reactiveBytes.get("R".getBytes())).doOnNext(res -> {
                byte b = (res != null && res.length > 0) ? res[0] : 0;
                String bits = String.format("%8s", Integer.toBinaryString(b & 0xFF)).replace(' ', '0');
                System.out.println(bits); // >>> 10100101
            }).then();
```

##### Java (Synchronous - Jedis)

```java
        jedis.bitop(BitOP.ONE, "R", "A", "B", "C");
        byte[] res15 = jedis.get("R".getBytes());
        System.out.println(String.format("%8s", Integer.toBinaryString(res15[0] & 0xFF)).replace(' ', '0'));
        // >>> 10100101
```

##### JavaScript (Node.js)

```javascript
await client.bitOp("ONE", "R", ["A", "B", "C"])
const res15 = await client.get("R")
console.log(res15.readUInt8(0).toString(2).padStart(8, '0'))
// >>> 10100101
```

##### PHP

```php
        $r->bitop('ONE', 'R', 'A', 'B', 'C');
        $res15 = $r->get('R');
        echo str_pad(decbin(ord($res15)), 8, '0', STR_PAD_LEFT) . PHP_EOL;
        // >>> 10100101
```

##### Python

```python
r.bitop("ONE", "R", "A", "B", "C")
res15 = r.get("R")
print("{:08b}".format(int.from_bytes(res15, "big")))
# >>> 10100101
```



## Split bitmaps into multiple keys

Bitmaps are trivial to split into multiple keys, for example for
the sake of sharding the data set and because in general it is better to
avoid working with huge keys. To split a bitmap across different keys
instead of setting all the bits into a key, a trivial strategy is just
to store M bits per key and obtain the key name with `bit-number/M` and
the Nth bit to address inside the key with `bit-number MOD M`.

## Performance

[`SETBIT`](https://redis.io/docs/latest/commands/setbit) and [`GETBIT`](https://redis.io/docs/latest/commands/getbit) are O(1).
[`BITOP`](https://redis.io/docs/latest/commands/bitop) is O(n), where _n_ is the length of the longest string in the comparison.

## Learn more

* [Redis Bitmaps Explained](https://www.youtube.com/watch?v=oj8LdJQjhJo) teaches you how to use bitmaps for map exploration in an online game. 
* [Redis University's RU101](https://university.redis.com/courses/ru101/) covers Redis bitmaps in detail.

