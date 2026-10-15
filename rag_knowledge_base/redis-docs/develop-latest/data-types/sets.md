# Redis sets

```json metadata
{
  "schema_version": 2,
  "title": "Redis sets",
  "description": "Introduction to Redis sets",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"examples","title":"Examples"},{"id":"tutorial","title":"Tutorial"},{"id":"limits","title":"Limits"},{"id":"performance","title":"Performance"},{"id":"alternatives","title":"Alternatives"},{"id":"learn-more","title":"Learn more"}]}

,
  "codeExamples": [{"codetabsId":"sets_tutorial-stepsadd","commands":[{"acl_categories":["@write","@set","@fast"],"complexity":"O(1)","name":"SADD"}],"description":"Foundational: Add members to a set using SADD when you need to store unique items (duplicates are silently ignored)","difficulty":"beginner","id":"sadd","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_sets_tutorial-stepsadd"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_sets_tutorial-stepsadd"},{"id":"Node-js","panelId":"panel_Nodejs_sets_tutorial-stepsadd"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_sets_tutorial-stepsadd"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_sets_tutorial-stepsadd"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_sets_tutorial-stepsadd"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_sets_tutorial-stepsadd"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_sets_tutorial-stepsadd"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_sets_tutorial-stepsadd"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_sets_tutorial-stepsadd"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_sets_tutorial-stepsadd"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_sets_tutorial-stepsadd"}]},{"buildsUpon":["sadd"],"codetabsId":"sets_tutorial-stepsismember","commands":[{"acl_categories":["@read","@set","@fast"],"complexity":"O(1)","name":"SISMEMBER"}],"description":"Foundational: Test set membership using SISMEMBER when you need O(1) lookups (much faster than checking a list)","difficulty":"beginner","id":"sismember","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_sets_tutorial-stepsismember"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_sets_tutorial-stepsismember"},{"id":"Node-js","panelId":"panel_Nodejs_sets_tutorial-stepsismember"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_sets_tutorial-stepsismember"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_sets_tutorial-stepsismember"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_sets_tutorial-stepsismember"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_sets_tutorial-stepsismember"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_sets_tutorial-stepsismember"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_sets_tutorial-stepsismember"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_sets_tutorial-stepsismember"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_sets_tutorial-stepsismember"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_sets_tutorial-stepsismember"}]},{"buildsUpon":["sadd"],"codetabsId":"sets_tutorial-stepsinter","commands":[{"acl_categories":["@read","@set","@slow"],"complexity":"O(N*M)","name":"SINTER"}],"description":"Set intersection: Find common members across multiple sets using SINTER when you need to identify shared items (e.g., users in multiple groups)","difficulty":"intermediate","id":"sinter","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_sets_tutorial-stepsinter"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_sets_tutorial-stepsinter"},{"id":"Node-js","panelId":"panel_Nodejs_sets_tutorial-stepsinter"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_sets_tutorial-stepsinter"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_sets_tutorial-stepsinter"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_sets_tutorial-stepsinter"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_sets_tutorial-stepsinter"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_sets_tutorial-stepsinter"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_sets_tutorial-stepsinter"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_sets_tutorial-stepsinter"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_sets_tutorial-stepsinter"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_sets_tutorial-stepsinter"}]},{"buildsUpon":["sadd"],"codetabsId":"sets_tutorial-stepscard","commands":[{"acl_categories":["@read","@set","@fast"],"complexity":"O(1)","name":"SCARD"}],"description":"Foundational: Get the cardinality of a set using SCARD when you need to count unique items efficiently","difficulty":"beginner","id":"scard","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_sets_tutorial-stepscard"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_sets_tutorial-stepscard"},{"id":"Node-js","panelId":"panel_Nodejs_sets_tutorial-stepscard"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_sets_tutorial-stepscard"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_sets_tutorial-stepscard"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_sets_tutorial-stepscard"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_sets_tutorial-stepscard"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_sets_tutorial-stepscard"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_sets_tutorial-stepscard"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_sets_tutorial-stepscard"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_sets_tutorial-stepscard"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_sets_tutorial-stepscard"}]},{"buildsUpon":["sadd"],"codetabsId":"sets_tutorial-stepsadd_smembers","commands":[{"acl_categories":["@keyspace","@write","@slow"],"complexity":"O(N)","name":"DEL"},{"acl_categories":["@write","@set","@fast"],"complexity":"O(1)","name":"SADD"},{"acl_categories":["@read","@set","@slow"],"complexity":"O(N)","name":"SMEMBERS"}],"description":"Foundational: Retrieve all members from a set using SMEMBERS when you need the complete set (note: order is not guaranteed)","difficulty":"beginner","id":"sadd_smembers","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_sets_tutorial-stepsadd_smembers"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_sets_tutorial-stepsadd_smembers"},{"id":"Node-js","panelId":"panel_Nodejs_sets_tutorial-stepsadd_smembers"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_sets_tutorial-stepsadd_smembers"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_sets_tutorial-stepsadd_smembers"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_sets_tutorial-stepsadd_smembers"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_sets_tutorial-stepsadd_smembers"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_sets_tutorial-stepsadd_smembers"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_sets_tutorial-stepsadd_smembers"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_sets_tutorial-stepsadd_smembers"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_sets_tutorial-stepsadd_smembers"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_sets_tutorial-stepsadd_smembers"}]},{"buildsUpon":["sismember"],"codetabsId":"sets_tutorial-stepsmismember","commands":[{"acl_categories":["@keyspace","@write","@slow"],"complexity":"O(N)","name":"DEL"},{"acl_categories":["@write","@set","@fast"],"complexity":"O(1)","name":"SADD"},{"acl_categories":["@read","@set","@fast"],"complexity":"O(1)","name":"SISMEMBER"},{"acl_categories":["@read","@set","@fast"],"complexity":"O(N)","name":"SMISMEMBER"}],"description":"Batch membership checks: Test multiple items at once using SMISMEMBER when you need to reduce round trips to the server","difficulty":"intermediate","id":"smismember","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_sets_tutorial-stepsmismember"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_sets_tutorial-stepsmismember"},{"id":"Node-js","panelId":"panel_Nodejs_sets_tutorial-stepsmismember"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_sets_tutorial-stepsmismember"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_sets_tutorial-stepsmismember"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_sets_tutorial-stepsmismember"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_sets_tutorial-stepsmismember"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_sets_tutorial-stepsmismember"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_sets_tutorial-stepsmismember"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_sets_tutorial-stepsmismember"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_sets_tutorial-stepsmismember"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_sets_tutorial-stepsmismember"}]},{"buildsUpon":["sadd"],"codetabsId":"sets_tutorial-stepsdiff","commands":[{"acl_categories":["@keyspace","@write","@slow"],"complexity":"O(N)","name":"DEL"},{"acl_categories":["@write","@set","@fast"],"complexity":"O(1)","name":"SADD"},{"acl_categories":["@read","@set","@slow"],"complexity":"O(N)","name":"SDIFF"}],"description":"Set difference: Find members in one set but not in others using SDIFF when you need to exclude items (warning: argument order matters)","difficulty":"intermediate","id":"sdiff","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_sets_tutorial-stepsdiff"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_sets_tutorial-stepsdiff"},{"id":"Node-js","panelId":"panel_Nodejs_sets_tutorial-stepsdiff"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_sets_tutorial-stepsdiff"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_sets_tutorial-stepsdiff"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_sets_tutorial-stepsdiff"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_sets_tutorial-stepsdiff"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_sets_tutorial-stepsdiff"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_sets_tutorial-stepsdiff"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_sets_tutorial-stepsdiff"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_sets_tutorial-stepsdiff"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_sets_tutorial-stepsdiff"}]},{"buildsUpon":["sinter","sdiff"],"codetabsId":"sets_tutorial-stepmultisets","commands":[{"acl_categories":["@keyspace","@write","@slow"],"complexity":"O(N)","name":"DEL"},{"acl_categories":["@write","@set","@fast"],"complexity":"O(1)","name":"SADD"},{"acl_categories":["@read","@set","@slow"],"complexity":"O(N*M)","name":"SINTER"},{"acl_categories":["@read","@set","@slow"],"complexity":"O(N)","name":"SUNION"},{"acl_categories":["@read","@set","@slow"],"complexity":"O(N)","name":"SDIFF"}],"description":"Advanced pattern: Combine SINTER, SUNION, and SDIFF to analyze complex relationships when you need to precompute set algebra across multiple datasets","difficulty":"advanced","id":"multisets","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_sets_tutorial-stepmultisets"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_sets_tutorial-stepmultisets"},{"id":"Node-js","panelId":"panel_Nodejs_sets_tutorial-stepmultisets"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_sets_tutorial-stepmultisets"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_sets_tutorial-stepmultisets"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_sets_tutorial-stepmultisets"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_sets_tutorial-stepmultisets"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_sets_tutorial-stepmultisets"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_sets_tutorial-stepmultisets"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_sets_tutorial-stepmultisets"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_sets_tutorial-stepmultisets"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_sets_tutorial-stepmultisets"}]},{"buildsUpon":["sadd"],"codetabsId":"sets_tutorial-stepsrem","commands":[{"acl_categories":["@keyspace","@write","@slow"],"complexity":"O(N)","name":"DEL"},{"acl_categories":["@write","@set","@fast"],"complexity":"O(1)","name":"SADD"},{"acl_categories":["@write","@set","@fast"],"complexity":"O(N)","name":"SREM"},{"acl_categories":["@write","@set","@fast"],"name":"SPOP"},{"acl_categories":["@read","@set","@slow"],"complexity":"O(N)","name":"SMEMBERS"},{"acl_categories":["@read","@set","@slow"],"name":"SRANDMEMBER"}],"description":"Removal strategies: Use SREM for targeted removal, SPOP for random removal, or SRANDMEMBER to inspect without modifying when you need flexible deletion patterns","difficulty":"intermediate","id":"srem","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_sets_tutorial-stepsrem"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_sets_tutorial-stepsrem"},{"id":"Node-js","panelId":"panel_Nodejs_sets_tutorial-stepsrem"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_sets_tutorial-stepsrem"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_sets_tutorial-stepsrem"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_sets_tutorial-stepsrem"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_sets_tutorial-stepsrem"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_sets_tutorial-stepsrem"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_sets_tutorial-stepsrem"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_sets_tutorial-stepsrem"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_sets_tutorial-stepsrem"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_sets_tutorial-stepsrem"}]}]
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


### Set command summary

**19 commands in this group:**

[View all set commands](https://redis.io/commands/?group=set)

| Command | Summary | Complexity | Since |
|---------|---------|------------|-------|
| [SADD](https://redis.io/commands/sadd/) | Adds one or more members to a set. Creates the key if it doesn't exist. | O(1) for each element added, so O(N) to add N e... | 1.0.0 |
| [SCARD](https://redis.io/commands/scard/) | Returns the number of members in a set. | O(1) | 1.0.0 |
| [SDIFF](https://redis.io/commands/sdiff/) | Returns the difference of multiple sets. | O(N) where N is the total number of elements in... | 1.0.0 |
| [SDIFFCARD](https://redis.io/commands/sdiffcard/) | Returns the number of members of the difference between the first set and all successive sets. | O(N) where N is the total number of elements in... | 8.10.0 |
| [SDIFFSTORE](https://redis.io/commands/sdiffstore/) | Stores the difference of multiple sets in a key. | O(N) where N is the total number of elements in... | 1.0.0 |
| [SINTER](https://redis.io/commands/sinter/) | Returns the intersect of multiple sets. | O(N*M) worst case where N is the cardinality of... | 1.0.0 |
| [SINTERCARD](https://redis.io/commands/sintercard/) | Returns the number of members of the intersect of multiple sets. | O(N*M) worst case where N is the cardinality of... | 7.0.0 |
| [SINTERSTORE](https://redis.io/commands/sinterstore/) | Stores the intersect of multiple sets in a key. | O(N*M) worst case where N is the cardinality of... | 1.0.0 |
| [SISMEMBER](https://redis.io/commands/sismember/) | Determines whether a member belongs to a set. | O(1) | 1.0.0 |
| [SMEMBERS](https://redis.io/commands/smembers/) | Returns all members of a set. | O(N) where N is the set cardinality. | 1.0.0 |

#### Set command summary (part 2)

| Command | Summary | Complexity | Since |
|---------|---------|------------|-------|
| [SMISMEMBER](https://redis.io/commands/smismember/) | Determines whether multiple members belong to a set. | O(N) where N is the number of elements being ch... | 6.2.0 |
| [SMOVE](https://redis.io/commands/smove/) | Moves a member from one set to another. | O(1) | 1.0.0 |
| [SPOP](https://redis.io/commands/spop/) | Returns one or more random members from a set after removing them. Deletes the set if the last member was popped. | Without the count argument O(1), otherwise O(N)... | 1.0.0 |
| [SRANDMEMBER](https://redis.io/commands/srandmember/) | Get one or multiple random members from a set | Without the count argument O(1), otherwise O(N)... | 1.0.0 |
| [SREM](https://redis.io/commands/srem/) | Removes one or more members from a set. Deletes the set if the last member was removed. | O(N) where N is the number of members to be rem... | 1.0.0 |
| [SSCAN](https://redis.io/commands/sscan/) | Iterates over members of a set. | O(1) for every call. O(N) for a complete iterat... | 2.8.0 |
| [SUNION](https://redis.io/commands/sunion/) | Returns the union of multiple sets. | O(N) where N is the total number of elements in... | 1.0.0 |
| [SUNIONCARD](https://redis.io/commands/sunioncard/) | Returns the number of members of the union of multiple sets. | O(N) where N is the total number of elements in... | 8.10.0 |
| [SUNIONSTORE](https://redis.io/commands/sunionstore/) | Stores the union of multiple sets in a key. | O(N) where N is the total number of elements in... | 1.0.0 |



A Redis set is an unordered collection of unique strings (members).
You can use Redis sets to efficiently:

* Track unique items (e.g., track all unique IP addresses accessing a given blog post).
* Represent relations (e.g., the set of all users with a given role).
* Perform common set operations such as intersection, unions, and differences.

## Examples

* Store the sets of bikes racing in France and the USA. Note that
if you add a member that already exists, it will be ignored.
Foundational: Add members to a set using SADD when you need to store unique items (duplicates are silently ignored)

**Difficulty:** Beginner

**Commands:** SADD

**Complexity:**
- SADD: O(1)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> SADD bikes:racing:france bike:1
(integer) 1
> SADD bikes:racing:france bike:1
(integer) 0
> SADD bikes:racing:france bike:2 bike:3
(integer) 2
> SADD bikes:racing:usa bike:1 bike:4
(integer) 2
```

##### C#

```csharp
        long res1 = db.SetAdd("bikes:racing:france", ["bike:1"]);
        Console.WriteLine(res1);    // >>> 1

        long res2 = db.SetAdd("bikes:racing:france", ["bike:1"]);
        Console.WriteLine(res2);    // >>> 0

        long res3 = db.SetAdd("bikes:racing:france", ["bike:2", "bike:3"]);
        Console.WriteLine(res3);    // >>> 2

        long res4 = db.SetAdd("bikes:racing:usa", ["bike:1", "bike:4"]);
        Console.WriteLine(res4);    // >>> 2
```

##### Go

```go
	res1, err := rdb.SAdd(ctx, "bikes:racing:france", "bike:1").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // >>> 1

	res2, err := rdb.SAdd(ctx, "bikes:racing:france", "bike:1").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2) // >>> 0

	res3, err := rdb.SAdd(ctx, "bikes:racing:france", "bike:2", "bike:3").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3) // >>> 2

	res4, err := rdb.SAdd(ctx, "bikes:racing:usa", "bike:1", "bike:4").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4) // >>> 2
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> sAdd = asyncCommands.sadd("bikes:racing:france", "bike:1").thenCompose(res1 -> {
                System.out.println(res1); // >>> 1
                return asyncCommands.sadd("bikes:racing:france", "bike:1");
            }).thenCompose(res2 -> {
                System.out.println(res2); // >>> 0
                return asyncCommands.sadd("bikes:racing:france", "bike:2", "bike:3");
            }).thenCompose(res3 -> {
                System.out.println(res3); // >>> 2
                return asyncCommands.sadd("bikes:racing:usa", "bike:1", "bike:4");
            }).thenAccept(res4 -> {
                System.out.println(res4); // >>> 2
            }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> sAdd = reactiveCommands.sadd("bikes:racing:france", "bike:1").doOnNext(result -> {
                System.out.println(result); // >>> 1
            }).flatMap(v -> reactiveCommands.sadd("bikes:racing:france", "bike:1")).doOnNext(result -> {
                System.out.println(result); // >>> 0
            }).flatMap(v -> reactiveCommands.sadd("bikes:racing:france", "bike:2", "bike:3")).doOnNext(result -> {
                System.out.println(result); // >>> 2
            }).flatMap(v -> reactiveCommands.sadd("bikes:racing:usa", "bike:1", "bike:4")).doOnNext(result -> {
                System.out.println(result); // >>> 2
            }).then();
```

##### Java (Synchronous - Jedis)

```java
        long res1 = jedis.sadd("bikes:racing:france", "bike:1");
        System.out.println(res1);  // >>> 1

        long res2 = jedis.sadd("bikes:racing:france", "bike:1");
        System.out.println(res2);  // >>> 0

        long res3 = jedis.sadd("bikes:racing:france", "bike:2", "bike:3");
        System.out.println(res3);  // >>> 2

        long res4 = jedis.sadd("bikes:racing:usa", "bike:1", "bike:4");
        System.out.println(res4);  // >>> 2
```

##### JavaScript (Node.js)

```javascript
const res1 = await client.sAdd('bikes:racing:france', 'bike:1')
console.log(res1)  // >>> 1

const res2 = await client.sAdd('bikes:racing:france', 'bike:1')
console.log(res2)  // >>> 0
const res3 = await client.sAdd('bikes:racing:france', ['bike:2', 'bike:3'])
console.log(res3)  // >>> 2
const res4 = await client.sAdd('bikes:racing:usa', ['bike:1', 'bike:4'])
console.log(res4)  // >>> 2
```

##### PHP

```php
        $res1 = $r->sadd('bikes:racing:france', ['bike:1']);
        echo $res1 . PHP_EOL;
        // >>> 1

        $res2 = $r->sadd('bikes:racing:france', ['bike:1']);
        echo $res2 . PHP_EOL;
        // >>> 0

        $res3 = $r->sadd('bikes:racing:france', ['bike:2', 'bike:3']);
        echo $res3 . PHP_EOL;
        // >>> 2

        $res4 = $r->sadd('bikes:racing:usa', ['bike:1', 'bike:4']);
        echo $res4 . PHP_EOL;
        // >>> 2
```

##### Python

```python
res1 = r.sadd("bikes:racing:france", "bike:1")
print(res1)  # >>> 1

res2 = r.sadd("bikes:racing:france", "bike:1")
print(res2)  # >>> 0

res3 = r.sadd("bikes:racing:france", "bike:2", "bike:3")
print(res3)  # >>> 2

res4 = r.sadd("bikes:racing:usa", "bike:1", "bike:4")
print(res4)  # >>> 2
```

##### Ruby

```ruby
res1 = r.sadd('bikes:racing:france', ['bike:1'])
puts res1 # >>> 1

res2 = r.sadd('bikes:racing:france', ['bike:1'])
puts res2 # >>> 0

res3 = r.sadd('bikes:racing:france', ['bike:2', 'bike:3'])
puts res3 # >>> 2

res4 = r.sadd('bikes:racing:usa', ['bike:1', 'bike:4'])
puts res4 # >>> 2
```

##### Rust (Asynchronous)

```rust
        if let Ok(res) = r.sadd("bikes:racing:france", "bike:1").await {
            let res: usize = res;
            println!("{res}"); // >>> 1
        }

        if let Ok(res) = r.sadd("bikes:racing:france", "bike:1").await {
            let res: usize = res;
            println!("{res}"); // >>> 0
        }

        if let Ok(res) = r.sadd("bikes:racing:france", &["bike:2", "bike:3"]).await {
            let res: usize = res;
            println!("{res}"); // >>> 2
        }

        if let Ok(res) = r.sadd("bikes:racing:usa", &["bike:1", "bike:4"]).await {
            let res: usize = res;
            println!("{res}"); // >>> 2
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.sadd("bikes:racing:france", "bike:1") {
            let res: usize = res;
            println!("{res}"); // >>> 1
        }

        if let Ok(res) = r.sadd("bikes:racing:france", "bike:1") {
            let res: usize = res;
            println!("{res}"); // >>> 0
        }

        if let Ok(res) = r.sadd("bikes:racing:france", &["bike:2", "bike:3"]) {
            let res: usize = res;
            println!("{res}"); // >>> 2
        }

        if let Ok(res) = r.sadd("bikes:racing:usa", &["bike:1", "bike:4"]) {
            let res: usize = res;
            println!("{res}"); // >>> 2
        }
```



* Check whether bike:1 or bike:2 are racing in the US.
Foundational: Test set membership using SISMEMBER when you need O(1) lookups (much faster than checking a list)

**Difficulty:** Beginner

**Builds upon:** sadd

**Commands:** SISMEMBER

**Complexity:**
- SISMEMBER: O(1)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> SISMEMBER bikes:racing:usa bike:1
(integer) 1
> SISMEMBER bikes:racing:usa bike:2
(integer) 0
```

##### C#

```csharp
        bool res5 = db.SetContains("bikes:racing:france", "bike:1");
        Console.WriteLine(res5);    // >>> True

        bool res6 = db.SetContains("bikes:racing:usa", "bike:2");
        Console.WriteLine(res6);    // >>> False
```

##### Go

```go
	res5, err := rdb.SIsMember(ctx, "bikes:racing:usa", "bike:1").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res5) // >>> true

	res6, err := rdb.SIsMember(ctx, "bikes:racing:usa", "bike:2").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res6) // >>> false
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> sIsMember = asyncCommands.sismember("bikes:racing:usa", "bike:1").thenCompose(res5 -> {
                System.out.println(res5); // >>> true
                return asyncCommands.sismember("bikes:racing:usa", "bike:2");
            }).thenAccept(res6 -> {
                System.out.println(res6); // >>> false
            }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Boolean> sIsMember1 = reactiveCommands.sismember("bikes:racing:usa", "bike:1").doOnNext(result -> {
                System.out.println(result); // >>> true
            });

            Mono<Boolean> sIsMember2 = reactiveCommands.sismember("bikes:racing:usa", "bike:2").doOnNext(result -> {
                System.out.println(result); // >>> false
            });
```

##### Java (Synchronous - Jedis)

```java
        jedis.sadd("bikes:racing:france", "bike:1", "bike:2", "bike:3");
        jedis.sadd("bikes:racing:usa", "bike:1", "bike:4");

        boolean res5 = jedis.sismember("bikes:racing:usa", "bike:1");
        System.out.println(res5);  // >>> true

        boolean res6 = jedis.sismember("bikes:racing:usa", "bike:2");
        System.out.println(res6);  // >>> false
```

##### JavaScript (Node.js)

```javascript
await client.del('bikes:racing:france')
await client.del('bikes:racing:usa')
await client.sAdd('bikes:racing:france', ['bike:1', 'bike:2', 'bike:3'])
await client.sAdd('bikes:racing:usa', ['bike:1', 'bike:4'])
const res5 = await client.sIsMember('bikes:racing:usa', 'bike:1')
console.log(res5)  // >>> 1

const res6 = await client.sIsMember('bikes:racing:usa', 'bike:2')
console.log(res6)  // >>> 0
```

##### PHP

```php
        $res5 = $r->sismember('bikes:racing:usa', 'bike:1');
        echo $res5 . PHP_EOL;
        // >>> 1

        $res6 = $r->sismember('bikes:racing:usa', 'bike:2');
        echo $res6 . PHP_EOL;
        // >>> 0
```

##### Python

```python
r.sadd("bikes:racing:france", "bike:1", "bike:2", "bike:3")
r.sadd("bikes:racing:usa", "bike:1", "bike:4")
res5 = r.sismember("bikes:racing:usa", "bike:1")
print(res5)  # >>> 1

res6 = r.sismember("bikes:racing:usa", "bike:2")
print(res6)  # >>> 0
```

##### Ruby

```ruby
r.del('bikes:racing:france', 'bikes:racing:usa')
r.sadd('bikes:racing:france', ['bike:1', 'bike:2', 'bike:3'])
r.sadd('bikes:racing:usa', ['bike:1', 'bike:4'])
res5 = r.sismember('bikes:racing:usa', 'bike:1')
puts res5 # >>> true

res6 = r.sismember('bikes:racing:usa', 'bike:2')
puts res6 # >>> false
```

##### Rust (Asynchronous)

```rust
        if let Ok(res) = r.sismember("bikes:racing:usa", "bike:1").await {
            let res: bool = res;
            println!("{}", i32::from(res)); // >>> 1
        }

        if let Ok(res) = r.sismember("bikes:racing:usa", "bike:2").await {
            let res: bool = res;
            println!("{}", i32::from(res)); // >>> 0
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.sismember("bikes:racing:usa", "bike:1") {
            let res: bool = res;
            println!("{}", i32::from(res)); // >>> 1
        }

        if let Ok(res) = r.sismember("bikes:racing:usa", "bike:2") {
            let res: bool = res;
            println!("{}", i32::from(res)); // >>> 0
        }
```



* Which bikes are competing in both races?
Set intersection: Find common members across multiple sets using SINTER when you need to identify shared items (e.g., users in multiple groups)

**Difficulty:** Intermediate

**Builds upon:** sadd

**Commands:** SINTER

**Complexity:**
- SINTER: O(N*M)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> SINTER bikes:racing:france bikes:racing:usa
1) "bike:1"
```

##### C#

```csharp
        long res7 = db.SetAdd("{bikes:racing}:france", ["bike:1", "bike:2", "bike:3"]);
        long res8 = db.SetAdd("{bikes:racing}:usa", ["bike:1", "bike:4"]);

        RedisValue[] res9 = db.SetCombine(SetOperation.Intersect, ["{bikes:racing}:france", "{bikes:racing}:usa"]);
        Console.WriteLine(string.Join(", ", res9)); // >>> bike:1
```

##### Go

```go
	res7, err := rdb.SInter(ctx, "bikes:racing:france", "bikes:racing:usa").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res7) // >>> [bike:1]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> sInter = asyncCommands.sinter("bikes:racing:france", "bikes:racing:usa")
                    .thenAccept(res7 -> {
                        System.out.println(res7); // >>> [bike:1]
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<List<String>> sInter = reactiveCommands.sinter("bikes:racing:france", "bikes:racing:usa").collectList()
                    .doOnNext(result -> {
                        System.out.println(result); // >>> [bike:1]
                    });
```

##### Java (Synchronous - Jedis)

```java
        jedis.sadd("bikes:racing:france", "bike:1", "bike:2", "bike:3");
        jedis.sadd("bikes:racing:usa", "bike:1", "bike:4");

        Set<String> res7 = jedis.sinter("bikes:racing:france", "bikes:racing:usa");
        System.out.println(res7);  // >>> [bike:1]
```

##### JavaScript (Node.js)

```javascript
await client.del('bikes:racing:france')
await client.del('bikes:racing:usa')
await client.sAdd('bikes:racing:france', ['bike:1', 'bike:2', 'bike:3'])
await client.sAdd('bikes:racing:usa', ['bike:1', 'bike:4'])
const res7 = await client.sInter(['bikes:racing:france', 'bikes:racing:usa'])
console.log(res7)  // >>> ['bike:1']
```

##### PHP

```php
        $res7 = $r->sinter(['bikes:racing:france', 'bikes:racing:usa']);
        echo json_encode($res7) . PHP_EOL;
        // >>> ["bike:1"]
```

##### Python

```python
r.sadd("bikes:racing:france", "bike:1", "bike:2", "bike:3")
r.sadd("bikes:racing:usa", "bike:1", "bike:4")
res7 = r.sinter("bikes:racing:france", "bikes:racing:usa")
print(res7)  # >>> {'bike:1'}
```

##### Ruby

```ruby
r.del('bikes:racing:france', 'bikes:racing:usa')
r.sadd('bikes:racing:france', ['bike:1', 'bike:2', 'bike:3'])
r.sadd('bikes:racing:usa', ['bike:1', 'bike:4'])
res7 = r.sinter('bikes:racing:france', 'bikes:racing:usa')
puts res7.inspect # >>> ["bike:1"]
```

##### Rust (Asynchronous)

```rust
        if let Ok(res) = r.sinter(&["bikes:racing:france", "bikes:racing:usa"]).await {
            let res: HashSet<String> = res;
            let res = sorted_set(res);
            println!("{res:?}"); // >>> ["bike:1"]
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.sinter(&["bikes:racing:france", "bikes:racing:usa"]) {
            let res: HashSet<String> = res;
            let res = sorted_set(res);
            println!("{res:?}"); // >>> ["bike:1"]
        }
```



* How many bikes are racing in France?
Foundational: Get the cardinality of a set using SCARD when you need to count unique items efficiently

**Difficulty:** Beginner

**Builds upon:** sadd

**Commands:** SCARD

**Complexity:**
- SCARD: O(1)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> SCARD bikes:racing:france
(integer) 3
```

##### C#

```csharp
        long res10 = db.SetAdd("bikes:racing:france", ["bike:1", "bike:2", "bike:3"]);
        long res11 = db.SetLength("bikes:racing:france");
        Console.WriteLine(res11);   // >>> 3
```

##### Go

```go
	res8, err := rdb.SCard(ctx, "bikes:racing:france").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res8) // >>> 3
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> sCard = asyncCommands.scard("bikes:racing:france").thenAccept(res8 -> {
                System.out.println(res8); // >>> 3
            }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Long> sCard = reactiveCommands.scard("bikes:racing:france").doOnNext(result -> {
                System.out.println(result); // >>> 3
            });
```

##### Java (Synchronous - Jedis)

```java
        jedis.sadd("bikes:racing:france", "bike:1", "bike:2", "bike:3");

        long res8 = jedis.scard("bikes:racing:france");
        System.out.println(res8);  // >>> 3
```

##### JavaScript (Node.js)

```javascript
await client.del('bikes:racing:france')
await client.sAdd('bikes:racing:france', ['bike:1', 'bike:2', 'bike:3'])
const res8 = await client.sCard('bikes:racing:france')
console.log(res8)  // >>> 3
```

##### PHP

```php
        $res8 = $r->scard('bikes:racing:france');
        echo $res8 . PHP_EOL;
        // >>> 3
```

##### Python

```python
r.sadd("bikes:racing:france", "bike:1", "bike:2", "bike:3")
res8 = r.scard("bikes:racing:france")
print(res8)  # >>> 3
```

##### Ruby

```ruby
r.del('bikes:racing:france')
r.sadd('bikes:racing:france', ['bike:1', 'bike:2', 'bike:3'])
res8 = r.scard('bikes:racing:france')
puts res8 # >>> 3
```

##### Rust (Asynchronous)

```rust
        if let Ok(res) = r.scard("bikes:racing:france").await {
            let res: usize = res;
            println!("{res}"); // >>> 3
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.scard("bikes:racing:france") {
            let res: usize = res;
            println!("{res}"); // >>> 3
        }
```



## Tutorial

The [`SADD`](https://redis.io/docs/latest/commands/sadd) command adds new elements to a set. It's also possible
to do a number of other operations against sets like testing if a given element
already exists, performing the intersection, union or difference between
multiple sets, and so forth.

Foundational: Retrieve all members from a set using SMEMBERS when you need the complete set (note: order is not guaranteed)

**Difficulty:** Beginner

**Builds upon:** sadd

**Commands:** DEL, SADD, SMEMBERS

**Complexity:**
- DEL: O(N)
- SADD: O(1)
- SMEMBERS: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> DEL bikes:racing:france
(integer) 1
> SADD bikes:racing:france bike:1 bike:2 bike:3
(integer) 3
> SMEMBERS bikes:racing:france
1) "bike:3"
2) "bike:1"
3) "bike:2"
```

##### C#

```csharp
        db.KeyDelete("bikes:racing:france");

        long res12 = db.SetAdd("bikes:racing:france", ["bike:1", "bike:2", "bike:3"]);
        RedisValue[] res13 = db.SetMembers("bikes:racing:france");
        Console.WriteLine(string.Join(", ", res13));    // >>> bike:3, bike:2, bike:1
```

##### Go

```go
	rdb.Del(ctx, "bikes:racing:france")

	res9, err := rdb.SAdd(ctx, "bikes:racing:france", "bike:1", "bike:2", "bike:3").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res9) // >>> 3

	res10, err := rdb.SMembers(ctx, "bikes:racing:france").Result()

	if err != nil {
		panic(err)
	}

	// Sort the strings in the slice to make sure the output is lexicographical
	sort.Strings(res10)

	fmt.Println(res10) // >>> [bike:1 bike:2 bike:3]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> sAddSMembers = asyncCommands.sadd("bikes:racing:france", "bike:1", "bike:2", "bike:3")
                    .thenCompose(res9 -> {
                        System.out.println(res9); // >>> 3
                        return asyncCommands.smembers("bikes:racing:france");
                    }).thenAccept(res10 -> {
                        System.out.println(res10); // >>> [bike:1, bike:2, bike:3]
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> sAddSMembers = reactiveCommands.sadd("bikes:racing:france", "bike:1", "bike:2", "bike:3")
                    .doOnNext(result -> {
                        System.out.println(result); // >>> 3
                    }).flatMap(v -> reactiveCommands.smembers("bikes:racing:france").collectList()).doOnNext(result -> {
                        System.out.println(result); // >>> [bike:1, bike:2, bike:3]
                    }).then();
```

##### Java (Synchronous - Jedis)

```java
        jedis.del("bikes:racing:france");

        long res9 = jedis.sadd("bikes:racing:france", "bike:1", "bike:2", "bike:3");
        System.out.println(res9);  // >>> 3

        Set<String> res10 = jedis.smembers("bikes:racing:france");
        System.out.println(res10);  // >>> [bike:1, bike:2, bike:3]
```

##### JavaScript (Node.js)

```javascript
await client.del('bikes:racing:france')

const res9 = await client.sAdd('bikes:racing:france', ['bike:1', 'bike:2', 'bike:3'])
console.log(res9)  // >>> 3

const res10 = await client.sMembers('bikes:racing:france')
console.log(res10)  // >>> ['bike:1', 'bike:2', 'bike:3']
```

##### PHP

```php
        $r->del('bikes:racing:france');

        $res9 = $r->sadd('bikes:racing:france', ['bike:1', 'bike:2', 'bike:3']);
        echo $res9 . PHP_EOL;
        // >>> 3

        $res10 = $r->smembers('bikes:racing:france');
        sort($res10);
        echo json_encode($res10) . PHP_EOL;
        // >>> ["bike:1","bike:2","bike:3"]
```

##### Python

```python
r.delete("bikes:racing:france")

res9 = r.sadd("bikes:racing:france", "bike:1", "bike:2", "bike:3")
print(res9)  # >>> 3

res10 = r.smembers("bikes:racing:france")
print(res10)  # >>> {'bike:1', 'bike:2', 'bike:3'}
```

##### Ruby

```ruby
r.del('bikes:racing:france')

res9 = r.sadd('bikes:racing:france', ['bike:1', 'bike:2', 'bike:3'])
puts res9 # >>> 3

res10 = r.smembers('bikes:racing:france')
puts res10.sort.inspect # >>> ["bike:1", "bike:2", "bike:3"]
```

##### Rust (Asynchronous)

```rust
        let _: usize = r.del("bikes:racing:france").await.unwrap_or(0);

        if let Ok(res) = r.sadd("bikes:racing:france", &["bike:1", "bike:2", "bike:3"]).await {
            let res: usize = res;
            println!("{res}"); // >>> 3
        }

        if let Ok(res) = r.smembers("bikes:racing:france").await {
            let res: HashSet<String> = res;
            let res = sorted_set(res);
            println!("{res:?}"); // >>> ["bike:1", "bike:2", "bike:3"]
        }
```

##### Rust (Synchronous)

```rust
        let _: usize = r.del("bikes:racing:france").unwrap_or(0);

        if let Ok(res) = r.sadd("bikes:racing:france", &["bike:1", "bike:2", "bike:3"]) {
            let res: usize = res;
            println!("{res}"); // >>> 3
        }

        if let Ok(res) = r.smembers("bikes:racing:france") {
            let res: HashSet<String> = res;
            let res = sorted_set(res);
            println!("{res:?}"); // >>> ["bike:1", "bike:2", "bike:3"]
        }
```



Here I've added three elements to my set and told Redis to return all the
elements. There is no order guarantee with a set. Redis is free to return the
elements in any order at every call.

Redis has commands to test for set membership. These commands can be used on single as well as multiple items:

Batch membership checks: Test multiple items at once using SMISMEMBER when you need to reduce round trips to the server

**Difficulty:** Intermediate

**Builds upon:** sismember

**Commands:** DEL, SADD, SISMEMBER, SMISMEMBER

**Complexity:**
- DEL: O(N)
- SADD: O(1)
- SISMEMBER: O(1)
- SMISMEMBER: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
# Recreate the France racing set so this example runs on its own.
> DEL bikes:racing:france
(integer) 1
> SADD bikes:racing:france bike:1 bike:2 bike:3
(integer) 3
> SISMEMBER bikes:racing:france bike:1
(integer) 1
> SMISMEMBER bikes:racing:france bike:2 bike:3 bike:4
1) (integer) 1
2) (integer) 1
3) (integer) 0
```

##### C#

```csharp
        // Recreate the set so this example runs on its own.
        db.KeyDelete("bikes:racing:france");
        db.SetAdd("bikes:racing:france", ["bike:1", "bike:2", "bike:3"]);

        bool res14 = db.SetContains("bikes:racing:france", "bike:1");
        Console.WriteLine(res14);   // >>> true

        bool[] res15 = db.SetContains("bikes:racing:france", ["bike:2", "bike:3", "bike:4"]);
        Console.WriteLine(string.Join(", ", res15));    // >>> True, True, False
```

##### Go

```go
	res11, err := rdb.SIsMember(ctx, "bikes:racing:france", "bike:1").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res11) // >>> true

	res12, err := rdb.SMIsMember(ctx, "bikes:racing:france", "bike:2", "bike:3", "bike:4").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res12) // >>> [true true false]
```

##### Java (Asynchronous - Lettuce)

```java
            // Recreate the set so this example runs on its own. The chain is
            // ordered, so the DEL + SADD complete before the reads below.
            CompletableFuture<Void> sMIsMember = asyncCommands.del("bikes:racing:france")
                    .thenCompose(d -> asyncCommands.sadd("bikes:racing:france", "bike:1", "bike:2", "bike:3"))
                    .thenCompose(a -> asyncCommands.sismember("bikes:racing:france", "bike:1")).thenCompose(res11 -> {
                        System.out.println(res11); // >>> true
                        return asyncCommands.smismember("bikes:racing:france", "bike:2", "bike:3", "bike:4");
                    }).thenAccept(res12 -> {
                        System.out.println(res12); // >>> [true, true, false]
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            // Recreate the set so this example runs on its own. Block it
            // sequentially: a DEL inside the shared Mono.when() below would
            // race the sibling reads on the same key.
            reactiveCommands.del("bikes:racing:france")
                    .then(reactiveCommands.sadd("bikes:racing:france", "bike:1", "bike:2", "bike:3"))
                    .block();

            Mono<Boolean> sIsMember3 = reactiveCommands.sismember("bikes:racing:france", "bike:1").doOnNext(result -> {
                System.out.println(result); // >>> true
            });

            Mono<List<Boolean>> sMIsMember = reactiveCommands.smismember("bikes:racing:france", "bike:2", "bike:3", "bike:4")
                    .collectList().doOnNext(result -> {
                        System.out.println(result); // >>> [true, true, false]
                    });
```

##### Java (Synchronous - Jedis)

```java
        // Recreate the set so this example runs on its own.
        jedis.del("bikes:racing:france");
        jedis.sadd("bikes:racing:france", "bike:1", "bike:2", "bike:3");

        boolean res11 = jedis.sismember("bikes:racing:france", "bike:1");
        System.out.println(res11);  // >>> true

        List<Boolean> res12 = jedis.smismember("bikes:racing:france", "bike:2", "bike:3", "bike:4");
        System.out.println(res12);  // >>> [true,true,false]
```

##### JavaScript (Node.js)

```javascript
// Recreate the set so this example runs on its own.
await client.del('bikes:racing:france')
await client.sAdd('bikes:racing:france', ['bike:1', 'bike:2', 'bike:3'])

const res11 = await client.sIsMember('bikes:racing:france', 'bike:1')
console.log(res11)  // >>> 1

const res12 = await client.smIsMember('bikes:racing:france', ['bike:2', 'bike:3', 'bike:4'])
console.log(res12)  // >>> [1, 1, 0]
```

##### PHP

```php
        // Recreate the set so this example runs on its own.
        $r->del('bikes:racing:france');
        $r->sadd('bikes:racing:france', 'bike:1', 'bike:2', 'bike:3');

        $res11 = $r->sismember('bikes:racing:france', 'bike:1');
        echo $res11 . PHP_EOL;
        // >>> 1

        $res12 = $r->smismember('bikes:racing:france', 'bike:2', 'bike:3', 'bike:4');
        echo json_encode($res12) . PHP_EOL;
        // >>> [1,1,0]
```

##### Python

```python
# Recreate the set so this example runs on its own.
r.delete("bikes:racing:france")
r.sadd("bikes:racing:france", "bike:1", "bike:2", "bike:3")

res11 = r.sismember("bikes:racing:france", "bike:1")
print(res11)  # >>> 1

res12 = r.smismember("bikes:racing:france", "bike:2", "bike:3", "bike:4")
print(res12)  # >>> [1, 1, 0]
```

##### Ruby

```ruby
# Recreate the set so this example runs on its own.
r.del('bikes:racing:france')
r.sadd('bikes:racing:france', ['bike:1', 'bike:2', 'bike:3'])

res11 = r.sismember('bikes:racing:france', 'bike:1')
puts res11 # >>> true

res12 = r.smismember('bikes:racing:france', 'bike:2', 'bike:3', 'bike:4')
puts res12.inspect # >>> [true, true, false]
```

##### Rust (Asynchronous)

```rust
        // Recreate the set so this example runs on its own.
        let _: usize = r.del("bikes:racing:france").await.unwrap_or(0);
        let _: usize = r
            .sadd("bikes:racing:france", &["bike:1", "bike:2", "bike:3"])
            .await
            .unwrap_or(0);

        if let Ok(res) = r.sismember("bikes:racing:france", "bike:1").await {
            let res: bool = res;
            println!("{}", i32::from(res)); // >>> 1
        }

        if let Ok(res) = r
            .smismember("bikes:racing:france", &["bike:2", "bike:3", "bike:4"])
            .await
        {
            let res: Vec<bool> = res;
            let res: Vec<i32> = res.into_iter().map(i32::from).collect();
            println!("{res:?}"); // >>> [1, 1, 0]
        }
```

##### Rust (Synchronous)

```rust
        // Recreate the set so this example runs on its own.
        let _: usize = r.del("bikes:racing:france").unwrap_or(0);
        let _: usize = r
            .sadd("bikes:racing:france", &["bike:1", "bike:2", "bike:3"])
            .unwrap_or(0);

        if let Ok(res) = r.sismember("bikes:racing:france", "bike:1") {
            let res: bool = res;
            println!("{}", i32::from(res)); // >>> 1
        }

        if let Ok(res) = r.smismember("bikes:racing:france", &["bike:2", "bike:3", "bike:4"]) {
            let res: Vec<bool> = res;
            let res: Vec<i32> = res.into_iter().map(i32::from).collect();
            println!("{res:?}"); // >>> [1, 1, 0]
        }
```



We can also find the difference between two sets. For instance, we may want
to know which bikes are racing in France but not in the USA:

Set difference: Find members in one set but not in others using SDIFF when you need to exclude items (warning: argument order matters)

**Difficulty:** Intermediate

**Builds upon:** sadd

**Commands:** DEL, SADD, SDIFF

**Complexity:**
- DEL: O(N)
- SADD: O(1)
- SDIFF: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> DEL bikes:racing:usa
(integer) 1
> SADD bikes:racing:usa bike:1 bike:4
(integer) 2
> SDIFF bikes:racing:france bikes:racing:usa
1) "bike:3"
2) "bike:2"
```

##### C#

```csharp
        long res16 = db.SetAdd("{bikes:racing}:france", ["bike:1", "bike:2", "bike:3"]);
        long res17 = db.SetAdd("{bikes:racing}:usa", ["bike:1", "bike:4"]);
        RedisValue[] res18 = db.SetCombine(SetOperation.Difference, ["{bikes:racing}:france", "{bikes:racing}:usa"]);
        Console.WriteLine(string.Join(", ", res18));    // >>> bike:2, bike:3
```

##### Go

```go
	_, err := rdb.SAdd(ctx, "bikes:racing:france", "bike:1", "bike:2", "bike:3").Result()

	if err != nil {
		panic(err)
	}

	_, err = rdb.SAdd(ctx, "bikes:racing:usa", "bike:1", "bike:4").Result()

	res13, err := rdb.SDiff(ctx, "bikes:racing:france", "bikes:racing:usa").Result()

	if err != nil {
		panic(err)
	}

	// Sort the strings in the slice to make sure the output is lexicographical
	sort.Strings(res13)

	fmt.Println(res13) // >>> [bike:2 bike:3]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> sDiff = asyncCommands.sdiff("bikes:racing:france", "bikes:racing:usa")
                    .thenAccept(res13 -> {
                        System.out.println(res13); // >>> [bike:2, bike:3]
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<List<String>> sDiff = reactiveCommands.sdiff("bikes:racing:france", "bikes:racing:usa").collectList()
                    .doOnNext(result -> {
                        System.out.println(result); // >>> [bike:2, bike:3]
                    });
```

##### Java (Synchronous - Jedis)

```java
        jedis.sadd("bikes:racing:france", "bike:1", "bike:2", "bike:3");
        jedis.sadd("bikes:racing:usa", "bike:1", "bike:4");

        Set<String> res13 = jedis.sdiff("bikes:racing:france", "bikes:racing:usa");
        System.out.println(res13);  // >>> [bike:2, bike:3]

```

##### JavaScript (Node.js)

```javascript
await client.del('bikes:racing:france')
await client.del('bikes:racing:usa')

await client.sAdd('bikes:racing:france', ['bike:1', 'bike:2', 'bike:3'])
await client.sAdd('bikes:racing:usa', ['bike:1', 'bike:4'])
const res13 = await client.sDiff(['bikes:racing:france', 'bikes:racing:usa'])
console.log(res13)  // >>> [ 'bike:2', 'bike:3' ]
```

##### PHP

```php
        $r->sadd('bikes:racing:france', ['bike:1', 'bike:2', 'bike:3']);
        $r->sadd('bikes:racing:usa', ['bike:1', 'bike:4']);

        $res13 = $r->sdiff(['bikes:racing:france', 'bikes:racing:usa']);
        sort($res13);
        echo json_encode($res13) . PHP_EOL;
        // >>> ["bike:2","bike:3"]
```

##### Python

```python
r.sadd("bikes:racing:france", "bike:1", "bike:2", "bike:3")
r.sadd("bikes:racing:usa", "bike:1", "bike:4")

res13 = r.sdiff("bikes:racing:france", "bikes:racing:usa")
print(res13)  # >>> {'bike:2', 'bike:3'}
```

##### Ruby

```ruby
r.sadd('bikes:racing:france', ['bike:1', 'bike:2', 'bike:3'])
r.sadd('bikes:racing:usa', ['bike:1', 'bike:4'])

res13 = r.sdiff('bikes:racing:france', 'bikes:racing:usa')
puts res13.sort.inspect # >>> ["bike:2", "bike:3"]
```

##### Rust (Asynchronous)

```rust
        let _: usize = r.del("bikes:racing:france").await.unwrap_or(0);
        let _: usize = r.del("bikes:racing:usa").await.unwrap_or(0);
        let _: usize = r
            .sadd("bikes:racing:france", &["bike:1", "bike:2", "bike:3"])
            .await
            .unwrap_or(0);
        let _: usize = r
            .sadd("bikes:racing:usa", &["bike:1", "bike:4"])
            .await
            .unwrap_or(0);

        if let Ok(res) = r.sdiff(&["bikes:racing:france", "bikes:racing:usa"]).await {
            let res: HashSet<String> = res;
            let res = sorted_set(res);
            println!("{res:?}"); // >>> ["bike:2", "bike:3"]
        }
```

##### Rust (Synchronous)

```rust
        let _: usize = r.del("bikes:racing:france").unwrap_or(0);
        let _: usize = r.del("bikes:racing:usa").unwrap_or(0);
        let _: usize = r.sadd("bikes:racing:france", &["bike:1", "bike:2", "bike:3"]).unwrap_or(0);
        let _: usize = r.sadd("bikes:racing:usa", &["bike:1", "bike:4"]).unwrap_or(0);

        if let Ok(res) = r.sdiff(&["bikes:racing:france", "bikes:racing:usa"]) {
            let res: HashSet<String> = res;
            let res = sorted_set(res);
            println!("{res:?}"); // >>> ["bike:2", "bike:3"]
        }
```



There are other non trivial operations that are still easy to implement
using the right Redis commands. For instance we may want a list of all the
bikes racing in France, the USA, and some other races. We can do this using
the [`SINTER`](https://redis.io/docs/latest/commands/sinter) command, which performs the intersection between different
sets. In addition to intersection you can also perform
unions, difference, and more. For example 
if we add a third race we can see some of these commands in action:

Advanced pattern: Combine SINTER, SUNION, and SDIFF to analyze complex relationships when you need to precompute set algebra across multiple datasets

**Difficulty:** Advanced

**Builds upon:** sinter, sdiff

**Commands:** DEL, SADD, SINTER, SUNION, SDIFF

**Complexity:**
- DEL: O(N)
- SADD: O(1)
- SINTER: O(N*M)
- SUNION: O(N)
- SDIFF: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> DEL bikes:racing:france bikes:racing:usa bikes:racing:italy
(integer) 2
> SADD bikes:racing:france bike:1 bike:2 bike:3
(integer) 3
> SADD bikes:racing:usa bike:1 bike:4
(integer) 2
> SADD bikes:racing:italy bike:1 bike:2 bike:3 bike:4
(integer) 4
> SINTER bikes:racing:france bikes:racing:usa bikes:racing:italy
1) "bike:1"
> SUNION bikes:racing:france bikes:racing:usa bikes:racing:italy
1) "bike:2"
2) "bike:1"
3) "bike:4"
4) "bike:3"
> SDIFF bikes:racing:france bikes:racing:usa bikes:racing:italy
(empty array)
> SDIFF bikes:racing:france bikes:racing:usa
1) "bike:3"
2) "bike:2"
> SDIFF bikes:racing:usa bikes:racing:france
1) "bike:4"
```

##### C#

```csharp
        db.KeyDelete("{bikes:racing}:france");
        db.KeyDelete("{bikes:racing}:usa");
        db.KeyDelete("{bikes:racing}:italy");

        long res19 = db.SetAdd("{bikes:racing}:france", ["bike:1", "bike:2", "bike:3"]);
        long res20 = db.SetAdd("{bikes:racing}:usa", ["bike:1", "bike:4"]);
        long res21 = db.SetAdd("{bikes:racing}:italy", ["bike:1", "bike:2", "bike:3", "bike:4"]);

        RedisValue[] res22 = db.SetCombine(SetOperation.Intersect, ["{bikes:racing}:france", "{bikes:racing}:usa", "{bikes:racing}:italy"
        ]);
        Console.WriteLine(string.Join(", ", res22));    // >>> bike:1

        RedisValue[] res23 = db.SetCombine(SetOperation.Union, ["{bikes:racing}:france", "{bikes:racing}:usa", "{bikes:racing}:italy"
        ]);
        Console.WriteLine(string.Join(", ", res23));    // >>> bike:1, bike:2, bike:3, bike:4

        RedisValue[] res24 = db.SetCombine(SetOperation.Difference, ["{bikes:racing}:france", "{bikes:racing}:usa", "{bikes:racing}:italy"
        ]);
        Console.WriteLine(string.Join(", ", res24));    // >>> <empty set>

        RedisValue[] res25 = db.SetCombine(SetOperation.Difference, ["{bikes:racing}:usa", "{bikes:racing}:france"]);
        Console.WriteLine(string.Join(", ", res25));    // >>> bike:4

        RedisValue[] res26 = db.SetCombine(SetOperation.Difference, ["{bikes:racing}:france", "{bikes:racing}:usa"]);
        Console.WriteLine(string.Join(", ", res26));    // >>> bike:2, bike:3
```

##### Go

```go
	rdb.Del(ctx, "bikes:racing:france")
	rdb.Del(ctx, "bikes:racing:usa")
	rdb.Del(ctx, "bikes:racing:italy")

	_, err := rdb.SAdd(ctx, "bikes:racing:france", "bike:1", "bike:2", "bike:3").Result()

	if err != nil {
		panic(err)
	}

	_, err = rdb.SAdd(ctx, "bikes:racing:usa", "bike:1", "bike:4").Result()

	if err != nil {
		panic(err)
	}

	_, err = rdb.SAdd(ctx, "bikes:racing:italy", "bike:1", "bike:2", "bike:3", "bike:4").Result()

	if err != nil {
		panic(err)
	}

	res14, err := rdb.SInter(ctx, "bikes:racing:france", "bikes:racing:usa", "bikes:racing:italy").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res14) // >>> [bike:1]

	res15, err := rdb.SUnion(ctx, "bikes:racing:france", "bikes:racing:usa", "bikes:racing:italy").Result()

	if err != nil {
		panic(err)
	}

	// Sort the strings in the slice to make sure the output is lexicographical
	sort.Strings(res15)

	fmt.Println(res15) // >>> [bike:1 bike:2 bike:3 bike:4]

	res16, err := rdb.SDiff(ctx, "bikes:racing:france", "bikes:racing:usa", "bikes:racing:italy").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res16) // >>> []

	res17, err := rdb.SDiff(ctx, "bikes:racing:usa", "bikes:racing:france").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res17) // >>> [bike:4]

	res18, err := rdb.SDiff(ctx, "bikes:racing:france", "bikes:racing:usa").Result()

	if err != nil {
		panic(err)
	}

	// Sort the strings in the slice to make sure the output is lexicographical
	sort.Strings(res18)

	fmt.Println(res18) // >>> [bike:2 bike:3]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> multisets = asyncCommands.sadd("bikes:racing:france", "bike:1", "bike:2", "bike:3")
                    .thenCompose(res14 -> {
                        System.out.println(res14); // >>> 0
                        return asyncCommands.sadd("bikes:racing:usa", "bike:1", "bike:4");
                    }).thenCompose(res15 -> {
                        System.out.println(res15); // >>> 0
                        return asyncCommands.sadd("bikes:racing:italy", "bike:1", "bike:2", "bike:3", "bike:4");
                    }).thenCompose(res16 -> {
                        System.out.println(res16); // >>> 4
                        return asyncCommands.sinter("bikes:racing:france", "bikes:racing:usa", "bikes:racing:italy");
                    }).thenCompose(res17 -> {
                        System.out.println(res17); // >>> [bike:1]
                        return asyncCommands.sunion("bikes:racing:france", "bikes:racing:usa", "bikes:racing:italy");
                    }).thenCompose(res18 -> {
                        System.out.println(res18); // >>> [bike:1, bike:2, bike:3, bike:4]
                        return asyncCommands.sdiff("bikes:racing:france", "bikes:racing:usa", "bikes:racing:italy");
                    }).thenCompose(res19 -> {
                        System.out.println(res19); // >>> []
                        return asyncCommands.sdiff("bikes:racing:usa", "bikes:racing:france");
                    }).thenCompose(res20 -> {
                        System.out.println(res20); // >>> [bike:4]
                        return asyncCommands.sdiff("bikes:racing:france", "bikes:racing:usa");
                    }).thenAccept(res21 -> {
                        System.out.println(res21); // >>> [bike:2, bike:3]
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> add3sets = reactiveCommands.sadd("bikes:racing:france", "bike:1", "bike:2", "bike:3")
                    .doOnNext(result -> {
                        System.out.println(result); // >>> 0
                    }).flatMap(v -> reactiveCommands.sadd("bikes:racing:usa", "bike:1", "bike:4")).doOnNext(result -> {
                        System.out.println(result); // >>> 0
                    }).flatMap(v -> reactiveCommands.sadd("bikes:racing:italy", "bike:1", "bike:2", "bike:3", "bike:4"))
                    .doOnNext(result -> {
                        System.out.println(result); // >>> 4,
                    }).then();
            add3sets.block();

            Mono<List<String>> multisets1 = reactiveCommands
                    .sinter("bikes:racing:france", "bikes:racing:usa", "bikes:racing:italy").collectList().doOnNext(result -> {
                        System.out.println(result); // >>> [bike:1]
                    });

            Mono<List<String>> multisets2 = reactiveCommands
                    .sunion("bikes:racing:france", "bikes:racing:usa", "bikes:racing:italy").collectList().doOnNext(result -> {
                        System.out.println(result); // >>> [bike:1, bike:2, bike:3, bike:4]
                    });

            Mono<List<String>> multisets3 = reactiveCommands
                    .sdiff("bikes:racing:france", "bikes:racing:usa", "bikes:racing:italy").collectList().doOnNext(result -> {
                        System.out.println(result); // >>> []
                    });

            Mono<List<String>> multisets4 = reactiveCommands.sdiff("bikes:racing:usa", "bikes:racing:france").collectList()
                    .doOnNext(result -> {
                        System.out.println(result); // >>> [bike:4]
                    });

            Mono<List<String>> multisets5 = reactiveCommands.sdiff("bikes:racing:france", "bikes:racing:usa").collectList()
                    .doOnNext(result -> {
                        System.out.println(result); // >>> [bike:2, bike:3]
                    });
```

##### Java (Synchronous - Jedis)

```java
        jedis.del("bikes:racing:france");
        jedis.del("bikes:racing:usa");
        jedis.del("bikes:racing:italy");

        jedis.sadd("bikes:racing:france", "bike:1", "bike:2", "bike:3");
        jedis.sadd("bikes:racing:usa", "bike:1", "bike:4");
        jedis.sadd("bikes:racing:italy", "bike:1", "bike:2", "bike:3", "bike:4");

        Set<String> res14 = jedis.sinter("bikes:racing:france", "bikes:racing:usa", "bikes:racing:italy");
        System.out.println(res14);  // >>> [bike:1]

        Set<String> res15 = jedis.sunion("bikes:racing:france", "bikes:racing:usa", "bikes:racing:italy");
        System.out.println(res15);  // >>> [bike:1, bike:2, bike:3, bike:4]

        Set<String> res16 = jedis.sdiff("bikes:racing:france", "bikes:racing:usa", "bikes:racing:italy");
        System.out.println(res16);  // >>> []

        Set<String> res17 = jedis.sdiff("bikes:racing:usa", "bikes:racing:france");
        System.out.println(res17);  // >>> [bike:4]

        Set<String> res18 = jedis.sdiff("bikes:racing:france", "bikes:racing:usa");
        System.out.println(res18);  // >>> [bike:2, bike:3]

```

##### JavaScript (Node.js)

```javascript
await client.del('bikes:racing:france')
await client.del('bikes:racing:usa')
await client.del('bikes:racing:italy')

await client.sAdd('bikes:racing:france', ['bike:1', 'bike:2', 'bike:3'])
await client.sAdd('bikes:racing:usa', ['bike:1', 'bike:4'])
await client.sAdd('bikes:racing:italy', ['bike:1', 'bike:2', 'bike:3', 'bike:4'])

const res14 = await client.sInter(
  ['bikes:racing:france', 'bikes:racing:usa', 'bikes:racing:italy']
)
console.log(res14)  // >>> ['bike:1']

const res15 = await client.sUnion(
  ['bikes:racing:france', 'bikes:racing:usa', 'bikes:racing:italy']
)
console.log(res15)  // >>> ['bike:1', 'bike:2', 'bike:3', 'bike:4']

const res16 = await client.sDiff(['bikes:racing:france', 'bikes:racing:usa', 'bikes:racing:italy'])
console.log(res16)  // >>> []

const res17 = await client.sDiff(['bikes:racing:usa', 'bikes:racing:france'])
console.log(res17)  // >>> ['bike:4']

const res18 = await client.sDiff(['bikes:racing:france', 'bikes:racing:usa'])
console.log(res18)  // >>> ['bike:2', 'bike:3']
```

##### PHP

```php
        $r->del('bikes:racing:france');
        $r->del('bikes:racing:usa');
        $r->del('bikes:racing:italy');
            
        $r->sadd('bikes:racing:france', ['bike:1', 'bike:2', 'bike:3']);
        $r->sadd('bikes:racing:usa', ['bike:1', 'bike:4']);
        $r->sadd('bikes:racing:italy', ['bike:1', 'bike:2', 'bike:3', 'bike:4']);

        $res14 = $r->sinter(['bikes:racing:france', 'bikes:racing:usa', 'bikes:racing:italy']);
        echo json_encode($res14) . PHP_EOL;
        // >>> ["bike:1"]

        $res15 = $r->sunion(['bikes:racing:france', 'bikes:racing:usa', 'bikes:racing:italy']);
        sort($res15);
        echo json_encode($res15) . PHP_EOL;
        // >>> ["bike:1","bike:2","bike:3","bike:4"]

        $res16 = $r->sdiff(['bikes:racing:france', 'bikes:racing:usa', 'bikes:racing:italy']);
        echo json_encode($res16) . PHP_EOL;
        // >>> []

        $res17 = $r->sdiff(['bikes:racing:usa', 'bikes:racing:france']);
        echo json_encode($res17) . PHP_EOL;
        // >>> ["bike:4"]

        $res18 = $r->sdiff(['bikes:racing:france', 'bikes:racing:usa']);
        sort($res18);
        echo json_encode($res18) . PHP_EOL;
        // >>> ["bike:2","bike:3"]
```

##### Python

```python
r.delete("bikes:racing:france")
r.delete("bikes:racing:usa")
r.delete("bikes:racing:italy")

r.sadd("bikes:racing:france", "bike:1", "bike:2", "bike:3")
r.sadd("bikes:racing:usa", "bike:1", "bike:4")
r.sadd("bikes:racing:italy", "bike:1", "bike:2", "bike:3", "bike:4")

res13 = r.sinter("bikes:racing:france", "bikes:racing:usa", "bikes:racing:italy")
print(res13)  # >>> {'bike:1'}

res14 = r.sunion("bikes:racing:france", "bikes:racing:usa", "bikes:racing:italy")
print(res14)  # >>> {'bike:1', 'bike:2', 'bike:3', 'bike:4'}

res15 = r.sdiff("bikes:racing:france", "bikes:racing:usa", "bikes:racing:italy")
print(res15)  # >>> set()

res16 = r.sdiff("bikes:racing:usa", "bikes:racing:france")
print(res16)  # >>> {'bike:4'}

res17 = r.sdiff("bikes:racing:france", "bikes:racing:usa")
print(res17)  # >>> {'bike:2', 'bike:3'}
```

##### Ruby

```ruby
r.del('bikes:racing:france', 'bikes:racing:usa', 'bikes:racing:italy')

r.sadd('bikes:racing:france', ['bike:1', 'bike:2', 'bike:3'])
r.sadd('bikes:racing:usa', ['bike:1', 'bike:4'])
r.sadd('bikes:racing:italy', ['bike:1', 'bike:2', 'bike:3', 'bike:4'])

res14 = r.sinter('bikes:racing:france', 'bikes:racing:usa', 'bikes:racing:italy')
puts res14.inspect # >>> ["bike:1"]

res15 = r.sunion('bikes:racing:france', 'bikes:racing:usa', 'bikes:racing:italy')
puts res15.sort.inspect # >>> ["bike:1", "bike:2", "bike:3", "bike:4"]

res16 = r.sdiff('bikes:racing:france', 'bikes:racing:usa', 'bikes:racing:italy')
puts res16.inspect # >>> []

res17 = r.sdiff('bikes:racing:france', 'bikes:racing:usa')
puts res17.sort.inspect # >>> ["bike:2", "bike:3"]

res18 = r.sdiff('bikes:racing:usa', 'bikes:racing:france')
puts res18.inspect # >>> ["bike:4"]
```

##### Rust (Asynchronous)

```rust
        let _: usize = r
            .del(&["bikes:racing:france", "bikes:racing:usa", "bikes:racing:italy"])
            .await
            .unwrap_or(0);
        let _: usize = r
            .sadd("bikes:racing:france", &["bike:1", "bike:2", "bike:3"])
            .await
            .unwrap_or(0);
        let _: usize = r
            .sadd("bikes:racing:usa", &["bike:1", "bike:4"])
            .await
            .unwrap_or(0);
        let _: usize = r
            .sadd("bikes:racing:italy", &["bike:1", "bike:2", "bike:3", "bike:4"])
            .await
            .unwrap_or(0);

        if let Ok(res) = r
            .sinter(&["bikes:racing:france", "bikes:racing:usa", "bikes:racing:italy"])
            .await
        {
            let res: HashSet<String> = res;
            let res = sorted_set(res);
            println!("{res:?}"); // >>> ["bike:1"]
        }

        if let Ok(res) = r
            .sunion(&["bikes:racing:france", "bikes:racing:usa", "bikes:racing:italy"])
            .await
        {
            let res: HashSet<String> = res;
            let res = sorted_set(res);
            println!("{res:?}"); // >>> ["bike:1", "bike:2", "bike:3", "bike:4"]
        }

        if let Ok(res) = r
            .sdiff(&["bikes:racing:france", "bikes:racing:usa", "bikes:racing:italy"])
            .await
        {
            let res: HashSet<String> = res;
            let res = sorted_set(res);
            println!("{res:?}"); // >>> []
        }

        if let Ok(res) = r.sdiff(&["bikes:racing:france", "bikes:racing:usa"]).await {
            let res: HashSet<String> = res;
            let res = sorted_set(res);
            println!("{res:?}"); // >>> ["bike:2", "bike:3"]
        }

        if let Ok(res) = r.sdiff(&["bikes:racing:usa", "bikes:racing:france"]).await {
            let res: HashSet<String> = res;
            let res = sorted_set(res);
            println!("{res:?}"); // >>> ["bike:4"]
        }
```

##### Rust (Synchronous)

```rust
        let _: usize = r.del(&["bikes:racing:france", "bikes:racing:usa", "bikes:racing:italy"]).unwrap_or(0);
        let _: usize = r.sadd("bikes:racing:france", &["bike:1", "bike:2", "bike:3"]).unwrap_or(0);
        let _: usize = r.sadd("bikes:racing:usa", &["bike:1", "bike:4"]).unwrap_or(0);
        let _: usize = r.sadd("bikes:racing:italy", &["bike:1", "bike:2", "bike:3", "bike:4"]).unwrap_or(0);

        if let Ok(res) =
            r.sinter(&["bikes:racing:france", "bikes:racing:usa", "bikes:racing:italy"])
        {
            let res: HashSet<String> = res;
            let res = sorted_set(res);
            println!("{res:?}"); // >>> ["bike:1"]
        }

        if let Ok(res) =
            r.sunion(&["bikes:racing:france", "bikes:racing:usa", "bikes:racing:italy"])
        {
            let res: HashSet<String> = res;
            let res = sorted_set(res);
            println!("{res:?}"); // >>> ["bike:1", "bike:2", "bike:3", "bike:4"]
        }

        if let Ok(res) =
            r.sdiff(&["bikes:racing:france", "bikes:racing:usa", "bikes:racing:italy"])
        {
            let res: HashSet<String> = res;
            let res = sorted_set(res);
            println!("{res:?}"); // >>> []
        }

        if let Ok(res) = r.sdiff(&["bikes:racing:france", "bikes:racing:usa"]) {
            let res: HashSet<String> = res;
            let res = sorted_set(res);
            println!("{res:?}"); // >>> ["bike:2", "bike:3"]
        }

        if let Ok(res) = r.sdiff(&["bikes:racing:usa", "bikes:racing:france"]) {
            let res: HashSet<String> = res;
            let res = sorted_set(res);
            println!("{res:?}"); // >>> ["bike:4"]
        }
```



You'll note that the [`SDIFF`](https://redis.io/docs/latest/commands/sdiff) command returns an empty array when the
difference between all sets is empty. You'll also note that the order of sets
passed to [`SDIFF`](https://redis.io/docs/latest/commands/sdiff) matters, since the difference is not commutative.

When you want to remove items from a set, you can use the [`SREM`](https://redis.io/docs/latest/commands/srem) command to
remove one or more items from a set, or you can use the [`SPOP`](https://redis.io/docs/latest/commands/spop) command to
remove a random item from a set. You can also _return_ a random item from a
set without removing it using the [`SRANDMEMBER`](https://redis.io/docs/latest/commands/srandmember) command:

Removal strategies: Use SREM for targeted removal, SPOP for random removal, or SRANDMEMBER to inspect without modifying when you need flexible deletion patterns

**Difficulty:** Intermediate

**Builds upon:** sadd

**Commands:** DEL, SADD, SREM, SPOP, SMEMBERS, SRANDMEMBER

**Complexity:**
- DEL: O(N)
- SADD: O(1)
- SREM: O(N)
- SMEMBERS: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> DEL bikes:racing:france
(integer) 1
> SADD bikes:racing:france bike:1 bike:2 bike:3 bike:4 bike:5
(integer) 5
> SREM bikes:racing:france bike:1
(integer) 1
> SPOP bikes:racing:france
"bike:3"
> SMEMBERS bikes:racing:france
1) "bike:2"
2) "bike:4"
3) "bike:5"
> SRANDMEMBER bikes:racing:france
"bike:2"
```

##### C#

```csharp
        db.KeyDelete("bikes:racing:france");

        long res27 = db.SetAdd("bikes:racing:france", ["bike:1", "bike:2", "bike:3", "bike:4", "bike:5"]);

        bool res28 = db.SetRemove("bikes:racing:france", "bike:1");
        Console.WriteLine(res28);   // >>> True

        RedisValue res29 = db.SetPop("bikes:racing:france");
        Console.WriteLine(res29);   // >>> bike:3

        RedisValue[] res30 = db.SetMembers("bikes:racing:france");
        Console.WriteLine(string.Join(", ", res30));    // >>> bike:2, bike:4, bike:5

        RedisValue res31 = db.SetRandomMember("bikes:racing:france");
        Console.WriteLine(res31);   // >>> bike:4
```

##### Go

```go
	rdb.Del(ctx, "bikes:racing:france")

	_, err := rdb.SAdd(ctx, "bikes:racing:france", "bike:1", "bike:2", "bike:3", "bike:4", "bike:5").Result()

	if err != nil {
		panic(err)
	}

	res19, err := rdb.SRem(ctx, "bikes:racing:france", "bike:1").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res19) // >>> 1

	res20, err := rdb.SPop(ctx, "bikes:racing:france").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res20) // >>> <random element>

	res21, err := rdb.SMembers(ctx, "bikes:racing:france").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res21) // >>> <remaining elements>

	res22, err := rdb.SRandMember(ctx, "bikes:racing:france").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res22) // >>> <random element>
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> sRem = asyncCommands
                    .sadd("bikes:racing:france", "bike:1", "bike:2", "bike:3", "bike:4", "bike:5").thenCompose(res22 -> {
                        System.out.println(res22); // >>> 2
                        return asyncCommands.srem("bikes:racing:france", "bike:1");
                    }).thenCompose(res23 -> {
                        System.out.println(res23); // >>> 1
                        return asyncCommands.spop("bikes:racing:france");
                    }).thenCompose(res24 -> {
                        System.out.println(res24); // >>> bike:3 (for example)
                        return asyncCommands.smembers("bikes:racing:france");
                    }).thenCompose(res25 -> {
                        System.out.println(res25); // >>> [bike:2, bike:4, bike:5] (for example)
                        return asyncCommands.srandmember("bikes:racing:france");
                    }).thenAccept(res26 -> {
                        System.out.println(res26); // >>> bike:4 (for example)
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> sRem = reactiveCommands.sadd("bikes:racing:france", "bike:1", "bike:2", "bike:3", "bike:4", "bike:5")
                    .doOnNext(result -> {
                        System.out.println(result); // >>> 2
                    }).flatMap(v -> reactiveCommands.srem("bikes:racing:france", "bike:1")).doOnNext(result -> {
                        System.out.println(result); // >>> 1
                    }).flatMap(v -> reactiveCommands.spop("bikes:racing:france")).doOnNext(result -> {
                        System.out.println(result); // >>> bike:3 (for example)
                    }).flatMap(v -> reactiveCommands.smembers("bikes:racing:france").collectList()).doOnNext(result -> {
                        System.out.println(result); // >>> [bike:2, bike:4, bike:5] (for example)
                    }).flatMap(v -> reactiveCommands.srandmember("bikes:racing:france")).doOnNext(result -> {
                        System.out.println(result); // >>> bike:4 (for example)
                    }).then();
```

##### Java (Synchronous - Jedis)

```java
        jedis.del("bikes:racing:france");
        jedis.sadd("bikes:racing:france", "bike:1", "bike:2", "bike:3", "bike:4", "bike:5");

        long res19 = jedis.srem("bikes:racing:france", "bike:1");
        System.out.println(res18);  // >>> 1

        String res20 = jedis.spop("bikes:racing:france");
        System.out.println(res20);  // >>> bike:3

        Set<String> res21 = jedis.smembers("bikes:racing:france");
        System.out.println(res21);  // >>> [bike:2, bike:4, bike:5]

        String res22 = jedis.srandmember("bikes:racing:france");
        System.out.println(res22);  // >>> bike:4
```

##### JavaScript (Node.js)

```javascript
await client.del('bikes:racing:france')

await client.sAdd('bikes:racing:france', ['bike:1', 'bike:2', 'bike:3', 'bike:4', 'bike:5'])

const res19 = await client.sRem('bikes:racing:france', 'bike:1')
console.log(res19)  // >>> 1

const res20 = await client.sPop('bikes:racing:france')
console.log(res20)  // >>> bike:3 or other random value

const res21 = await client.sMembers('bikes:racing:france')
console.log(res21)  // >>> ['bike:2', 'bike:4', 'bike:5']; depends on previous result

const res22 = await client.sRandMember('bikes:racing:france')
console.log(res22)  // >>> bike:4 or other random value
```

##### PHP

```php
        $r->del('bikes:racing:france');

        $r->sadd('bikes:racing:france', ['bike:1', 'bike:2', 'bike:3', 'bike:4', 'bike:5']);

        $res19 = $r->srem('bikes:racing:france', ['bike:1']);
        echo $res19 . PHP_EOL;
        // >>> 1

        $res20 = $r->spop('bikes:racing:france');
        echo $res20 . PHP_EOL;
        // >>> bike:3 (for example)

        $res21 = $r->smembers('bikes:racing:france');
        sort($res21);
        echo json_encode($res21) . PHP_EOL;
        // >>> ["bike:2","bike:4","bike:5"]

        $res22 = $r->srandmember('bikes:racing:france');
        echo $res22 . PHP_EOL;
        // >>> bike:4 (for example)

```

##### Python

```python
r.delete("bikes:racing:france")

r.sadd("bikes:racing:france", "bike:1", "bike:2", "bike:3", "bike:4", "bike:5")

res18 = r.srem("bikes:racing:france", "bike:1")
print(res18)  # >>> 1

res19 = r.spop("bikes:racing:france")
print(res19)  # >>> bike:3

res20 = r.smembers("bikes:racing:france")
print(res20)  # >>> {'bike:2', 'bike:4', 'bike:5'}

res21 = r.srandmember("bikes:racing:france")
print(res21)  # >>> bike:4
```

##### Ruby

```ruby
r.del('bikes:racing:france')

r.sadd('bikes:racing:france', ['bike:1', 'bike:2', 'bike:3', 'bike:4', 'bike:5'])

res19 = r.srem('bikes:racing:france', ['bike:1'])
puts res19 # >>> 1

res20 = r.spop('bikes:racing:france')
puts res20 # >>> bike:3, for example

res21 = r.smembers('bikes:racing:france')
puts res21.sort.inspect # >>> Remaining members, in no particular order

res22 = r.srandmember('bikes:racing:france')
puts res22 # >>> bike:4, for example
```

##### Rust (Asynchronous)

```rust
        let _: usize = r.del("bikes:racing:france").await.unwrap_or(0);
        let _: usize = r
            .sadd(
                "bikes:racing:france",
                &["bike:1", "bike:2", "bike:3", "bike:4", "bike:5"],
            )
            .await
            .unwrap_or(0);

        if let Ok(res) = r.srem("bikes:racing:france", "bike:1").await {
            let res: usize = res;
            println!("{res}"); // >>> 1
        }

        if let Ok(res) = r.spop("bikes:racing:france").await {
            let res: Option<String> = res;
            match res {
                Some(res) => println!("{res}"), // >>> bike:3 (for example)
                None => println!("(nil)"),
            }
        }

        if let Ok(res) = r.smembers("bikes:racing:france").await {
            let res: HashSet<String> = res;
            let res = sorted_set(res);
            println!("{res:?}"); // >>> ["bike:2", "bike:4", "bike:5"] (for example)
        }

        if let Ok(res) = r.srandmember("bikes:racing:france").await {
            let res: Option<String> = res;
            match res {
                Some(res) => println!("{res}"), // >>> bike:4 (for example)
                None => println!("(nil)"),
            }
        }
```

##### Rust (Synchronous)

```rust
        let _: usize = r.del("bikes:racing:france").unwrap_or(0);
        let _: usize = r
            .sadd(
                "bikes:racing:france",
                &["bike:1", "bike:2", "bike:3", "bike:4", "bike:5"],
            )
            .unwrap_or(0);

        if let Ok(res) = r.srem("bikes:racing:france", "bike:1") {
            let res: usize = res;
            println!("{res}"); // >>> 1
        }

        if let Ok(res) = r.spop("bikes:racing:france") {
            let res: Option<String> = res;
            match res {
                Some(res) => println!("{res}"), // >>> bike:3 (for example)
                None => println!("(nil)"),
            }
        }

        if let Ok(res) = r.smembers("bikes:racing:france") {
            let res: HashSet<String> = res;
            let res = sorted_set(res);
            println!("{res:?}"); // >>> ["bike:2", "bike:4", "bike:5"] (for example)
        }

        if let Ok(res) = r.srandmember("bikes:racing:france") {
            let res: Option<String> = res;
            match res {
                Some(res) => println!("{res}"), // >>> bike:4 (for example)
                None => println!("(nil)"),
            }
        }
```



## Limits

The max size of a Redis set is 2^32 - 1 (4,294,967,295) members.

## Performance

Most set operations, including adding, removing, and checking whether an item is a set member, are O(1).
This means that they're highly efficient.
However, for large sets with hundreds of thousands of members or more, you should exercise caution when running the [`SMEMBERS`](https://redis.io/docs/latest/commands/smembers) command.
This command is O(n) and returns the entire set in a single response. 
As an alternative, consider the [`SSCAN`](https://redis.io/docs/latest/commands/sscan), which lets you retrieve all members of a set iteratively.

## Alternatives

Sets membership checks on large datasets (or on streaming data) can use a lot of memory.
If you're concerned about memory usage and don't need perfect precision, consider a [Bloom filter or Cuckoo filter](https://redis.io/docs/latest/develop/data-types/probabilistic/bloom-filter) as an alternative to a set.

Redis sets are frequently used as a kind of index.
If you need to index and query your data, consider the [JSON](https://redis.io/docs/latest/develop/data-types/json) data type and the [Redis Search](https://redis.io/docs/latest/develop/ai/search-and-query) features.

## Learn more

* [Redis Sets Explained](https://www.youtube.com/watch?v=PKdCppSNTGQ) and [Redis Sets Elaborated](https://www.youtube.com/watch?v=aRw5ME_5kMY) are two short but thorough video explainers covering Redis sets.
* [Redis University's RU101](https://university.redis.com/courses/ru101/) explores Redis sets in detail.

