# HyperLogLog

```json metadata
{
  "schema_version": 2,
  "title": "HyperLogLog",
  "description": "HyperLogLog is a probabilistic data structure that estimates the cardinality of a set.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"use-cases","title":"Use cases"},{"id":"performance","title":"Performance"},{"id":"limits","title":"Limits"},{"id":"learn-more","title":"Learn more"}]}

,
  "codeExamples": [{"codetabsId":"hll_tutorial-steppfadd","commands":[{"acl_categories":["@write","@hyperloglog","@fast"],"complexity":"O(1)","name":"PFADD"},{"acl_categories":["@read","@hyperloglog","@slow"],"complexity":"O(1)","name":"PFCOUNT"},{"acl_categories":["@write","@hyperloglog","@slow"],"complexity":"O(N)","name":"PFMERGE"}],"description":"HyperLogLog operations: Use PFADD to add items to a HyperLogLog, PFCOUNT to estimate cardinality, and PFMERGE to combine HyperLogLogs when you need space-efficient cardinality estimation","difficulty":"intermediate","id":"pfadd","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_hll_tutorial-steppfadd"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_hll_tutorial-steppfadd"},{"id":"Node-js","panelId":"panel_Nodejs_hll_tutorial-steppfadd"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_hll_tutorial-steppfadd"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_hll_tutorial-steppfadd"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_hll_tutorial-steppfadd"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_hll_tutorial-steppfadd"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_hll_tutorial-steppfadd"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_hll_tutorial-steppfadd"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_hll_tutorial-steppfadd"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_hll_tutorial-steppfadd"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_hll_tutorial-steppfadd"}]}]
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


### HyperLogLog command summary

**5 commands in this group:**

[View all hyperloglog commands](https://redis.io/commands/?group=hyperloglog)

| Command | Summary | Complexity | Since |
|---------|---------|------------|-------|
| [PFADD](https://redis.io/commands/pfadd/) | Adds elements to a HyperLogLog key. Creates the key if it doesn't exist. | O(1) to add every element. | 2.8.9 |
| [PFCOUNT](https://redis.io/commands/pfcount/) | Returns the approximated cardinality of the set(s) observed by the HyperLogLog key(s). | O(1) with a very small average constant time wh... | 2.8.9 |
| [PFDEBUG](https://redis.io/commands/pfdebug/) | Internal commands for debugging HyperLogLog values. | N/A | 2.8.9 |
| [PFMERGE](https://redis.io/commands/pfmerge/) | Merges one or more HyperLogLog values into a single key. | O(N) to merge N HyperLogLogs, but with high con... | 2.8.9 |
| [PFSELFTEST](https://redis.io/commands/pfselftest/) | An internal command for testing HyperLogLog values. | N/A | 2.8.9 |



HyperLogLog is a probabilistic data structure that estimates the cardinality of a set, trading perfect accuracy for efficient space utilization. The Redis implementation uses up to 12 KB of memory and provides a standard error rate of 0.81%.

Counting unique items usually requires an amount of memory
proportional to the number of items you want to count, because you need
to remember the elements you have already seen in the past in order to avoid
counting them multiple times. However, a set of algorithms exist that trade 
memory for precision: they return an estimated measure with a standard error, 
which, in the case of the Redis implementation for HyperLogLog, is less than 1%.
The magic of this algorithm is that you no longer need to use an amount of memory
proportional to the number of items counted, and instead can use a
constant amount of memory; 12k bytes in the worst case, or a lot less if your
HyperLogLog (We'll just call them HLL from now) has seen very few elements.

HLLs in Redis, while technically a different data structure, are encoded
as a Redis string, so you can call [`GET`](https://redis.io/docs/latest/commands/get) to serialize a HLL, and [`SET`](https://redis.io/docs/latest/commands/set)
to deserialize it back to the server.

Conceptually the HLL API is like using Sets to do the same task. You would
[`SADD`](https://redis.io/docs/latest/commands/sadd) every observed element into a set, and would use [`SCARD`](https://redis.io/docs/latest/commands/scard) to check the
number of elements inside the set, which are unique since [`SADD`](https://redis.io/docs/latest/commands/sadd) will not
re-add an existing element.

While you don't really *add items* into an HLL, because the data structure
only contains a state that does not include actual elements, the API is the
same:

* Every time you see a new element, you add it to the count with [`PFADD`](https://redis.io/docs/latest/commands/pfadd).
* When you want to retrieve the current approximation of unique elements added using the [`PFADD`](https://redis.io/docs/latest/commands/pfadd) command, you can use the [`PFCOUNT`](https://redis.io/docs/latest/commands/pfcount) command. If you need to merge two different HLLs, the [`PFMERGE`](https://redis.io/docs/latest/commands/pfmerge) command is available. Since HLLs provide approximate counts of unique elements, the result of the merge will give you an approximation of the number of unique elements across both source HLLs.

HyperLogLog operations: Use PFADD to add items to a HyperLogLog, PFCOUNT to estimate cardinality, and PFMERGE to combine HyperLogLogs when you need space-efficient cardinality estimation

**Difficulty:** Intermediate

**Commands:** PFADD, PFCOUNT, PFMERGE

**Complexity:**
- PFADD: O(1)
- PFCOUNT: O(1)
- PFMERGE: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> PFADD bikes Hyperion Deimos Phoebe Quaoar
(integer) 1
> PFCOUNT bikes
(integer) 4
> PFADD commuter_bikes Salacia Mimas Quaoar
(integer) 1
> PFMERGE all_bikes bikes commuter_bikes
OK
> PFCOUNT all_bikes
(integer) 6
```

##### C#

```csharp
        bool res1 = db.HyperLogLogAdd("{bikes}", ["Hyperion", "Deimos", "Phoebe", "Quaoar"]);
        Console.WriteLine(res1);    // >>> True

        long res2 = db.HyperLogLogLength("{bikes}");
        Console.WriteLine(res2);    // >>> 4

        bool res3 = db.HyperLogLogAdd("commuter_{bikes}", ["Salacia", "Mimas", "Quaoar"]);
        Console.WriteLine(res3);    // >>> True

        db.HyperLogLogMerge("all_{bikes}", "{bikes}", "commuter_{bikes}");
        long res4 = db.HyperLogLogLength("all_{bikes}");
        Console.WriteLine(res4);    // >>> 6
```

##### Go

```go
	res1, err := rdb.PFAdd(ctx, "bikes", "Hyperion", "Deimos", "Phoebe", "Quaoar").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // 1

	res2, err := rdb.PFCount(ctx, "bikes").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2) // 4

	res3, err := rdb.PFAdd(ctx, "commuter_bikes", "Salacia", "Mimas", "Quaoar").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3) // 1

	res4, err := rdb.PFMerge(ctx, "all_bikes", "bikes", "commuter_bikes").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4) // OK

	res5, err := rdb.PFCount(ctx, "all_bikes").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res5) // 6
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> pfaddExample = asyncCommands
                    .pfadd("bikes", "Hyperion", "Deimos", "Phoebe", "Quaoar")
                    .thenCompose(res1 -> {
                        System.out.println(res1);
                        // >>> 1
                        return asyncCommands.pfcount("bikes");
                    })
                    .thenCompose(res2 -> {
                        System.out.println(res2);
                        // >>> 4
                        return asyncCommands.pfadd("commuter_bikes", "Salacia", "Mimas", "Quaoar");
                    })
                    .thenCompose(res3 -> {
                        System.out.println(res3);
                        // >>> 1
                        return asyncCommands.pfmerge("all_bikes", "bikes", "commuter_bikes");
                    })
                    .thenCompose(res4 -> {
                        System.out.println(res4);
                        // >>> OK
                        return asyncCommands.pfcount("all_bikes");
                    })
                    .thenAccept(res5 -> {
                        System.out.println(res5);
                        // >>> 6
                    })
                    .toCompletableFuture();

            pfaddExample.join();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> pfaddExample = reactiveCommands
                    .pfadd("bikes", "Hyperion", "Deimos", "Phoebe", "Quaoar")
                    .doOnNext(res1 -> {
                        System.out.println(res1);
                        // >>> 1
                    })
                    .then(reactiveCommands.pfcount("bikes"))
                    .doOnNext(res2 -> {
                        System.out.println(res2);
                        // >>> 4
                    })
                    .then(reactiveCommands.pfadd("commuter_bikes", "Salacia", "Mimas", "Quaoar"))
                    .doOnNext(res3 -> {
                        System.out.println(res3);
                        // >>> 1
                    })
                    .then(reactiveCommands.pfmerge("all_bikes", "bikes", "commuter_bikes"))
                    .doOnNext(res4 -> {
                        System.out.println(res4);
                        // >>> OK
                    })
                    .then(reactiveCommands.pfcount("all_bikes"))
                    .doOnNext(res5 -> {
                        System.out.println(res5);
                        // >>> 6
                    })
                    .then();

            pfaddExample.block();
```

##### Java (Synchronous - Jedis)

```java
        long res1 = jedis.pfadd("bikes", "Hyperion", "Deimos", "Phoebe", "Quaoar");
        System.out.println(res1); // >>> 1

        long res2 = jedis.pfcount("bikes");
        System.out.println(res2); // >>> 4

        long res3 = jedis.pfadd("commuter_bikes", "Salacia", "Mimas", "Quaoar");
        System.out.println(res3); // >>> 1

        String res4 = jedis.pfmerge("all_bikes", "bikes", "commuter_bikes");
        System.out.println(res4); // >>> OK


        long res5 = jedis.pfcount("all_bikes");
        System.out.println(res5); // >>> 6
```

##### JavaScript (Node.js)

```javascript
const res1 = await client.pfAdd('bikes', ['Hyperion', 'Deimos', 'Phoebe', 'Quaoar']);
console.log(res1);  // >>> 1

const res2 = await client.pfCount('bikes');
console.log(res2);  // >>> 4

const res3 = await client.pfAdd('commuter_bikes', ['Salacia', 'Mimas', 'Quaoar']);
console.log(res3);  // >>> 1

const res4 = await client.pfMerge('all_bikes', ['bikes', 'commuter_bikes']);
console.log(res4);  // >>> OK

const res5 = await client.pfCount('all_bikes');
console.log(res5);  // >>> 6
```

##### PHP

```php
        $res1 = $r->pfadd('bikes', ['Hyperion', 'Deimos', 'Phoebe', 'Quaoar']);
        echo $res1 . PHP_EOL;
        // >>> 1

        $res2 = $r->pfcount('bikes');
        echo $res2 . PHP_EOL;
        // >>> 4

        $res3 = $r->pfadd('commuter_bikes', ['Salacia', 'Mimas', 'Quaoar']);
        echo $res3 . PHP_EOL;
        // >>> 1

        $res4 = $r->pfmerge('all_bikes', 'bikes', 'commuter_bikes');
        echo $res4 . PHP_EOL;
        // >>> OK

        $res5 = $r->pfcount('all_bikes');
        echo $res5 . PHP_EOL;
        // >>> 6
```

##### Python

```python
res1 = r.pfadd("bikes", "Hyperion", "Deimos", "Phoebe", "Quaoar")
print(res1)  # >>> 1

res2 = r.pfcount("bikes")
print(res2)  # >>> 4

res3 = r.pfadd("commuter_bikes", "Salacia", "Mimas", "Quaoar")
print(res3)  # >>> 1

res4 = r.pfmerge("all_bikes", "bikes", "commuter_bikes")
print(res4)  # >>> True

res5 = r.pfcount("all_bikes")
print(res5)  # >>> 6
```

##### Ruby

```ruby
res1 = r.pfadd('bikes', ['Hyperion', 'Deimos', 'Phoebe', 'Quaoar'])
puts res1 # >>> true

res2 = r.pfcount('bikes')
puts res2 # >>> 4

res3 = r.pfadd('commuter_bikes', ['Salacia', 'Mimas', 'Quaoar'])
puts res3 # >>> true

res4 = r.pfmerge('all_bikes', 'bikes', 'commuter_bikes')
puts res4 # >>> true

res5 = r.pfcount('all_bikes')
puts res5 # >>> 6
```

##### Rust (Asynchronous)

```rust
        let res1: bool = r
            .pfadd("bikes", &["Hyperion", "Deimos", "Phoebe", "Quaoar"])
            .await
            .expect("Failed to add bikes");
        println!("{res1}"); // >>> true

        let res2: usize = r.pfcount("bikes").await.expect("Failed to count bikes");
        println!("{res2}"); // >>> 4

        let res3: bool = r
            .pfadd("commuter_bikes", &["Salacia", "Mimas", "Quaoar"])
            .await
            .expect("Failed to add commuter bikes");
        println!("{res3}"); // >>> true

        let _: () = r
            .pfmerge("all_bikes", &["bikes", "commuter_bikes"])
            .await
            .expect("Failed to merge HyperLogLogs");
        println!("OK"); // >>> OK

        let res5: usize = r
            .pfcount("all_bikes")
            .await
            .expect("Failed to count all bikes");
        println!("{res5}"); // >>> 6

```

##### Rust (Synchronous)

```rust
        let res1: bool = r
            .pfadd("bikes", &["Hyperion", "Deimos", "Phoebe", "Quaoar"])
            .expect("Failed to add bikes");
        println!("{res1}"); // >>> true

        let res2: usize = r.pfcount("bikes").expect("Failed to count bikes");
        println!("{res2}"); // >>> 4

        let res3: bool = r
            .pfadd("commuter_bikes", &["Salacia", "Mimas", "Quaoar"])
            .expect("Failed to add commuter bikes");
        println!("{res3}"); // >>> true

        let _: () = r
            .pfmerge("all_bikes", &["bikes", "commuter_bikes"])
            .expect("Failed to merge HyperLogLogs");
        println!("OK"); // >>> OK

        let res5: usize = r.pfcount("all_bikes").expect("Failed to count all bikes");
        println!("{res5}"); // >>> 6

```



Some examples of use cases for this data structure is counting unique queries
performed by users in a search form every day, number of unique visitors to a web page and other similar cases.

Redis is also able to perform the union of HLLs, please check the
[full documentation](/commands?group=hyperloglog) for more information.

## Use cases

**Anonymous unique visits of a web page (SaaS, analytics tools)** 

This application answers these questions: 

- How many unique visits has this page had on this day? 
- How many unique users have played this song? 
- How many unique users have viewed this video? 

> [!NOTE]
>  
> Storing the IP address or any other kind of personal identifier is against the law in some countries, which makes it impossible to get unique visitor statistics on your website.

One HyperLogLog is created per page (video/song) per period, and every IP/identifier is added to it on every visit.

## Performance

Writing ([`PFADD`](https://redis.io/docs/latest/commands/pfadd)) to and reading from ([`PFCOUNT`](https://redis.io/docs/latest/commands/pfcount)) the HyperLogLog is done in constant time and space.
Merging HLLs is O(n), where _n_ is the number of sketches.

## Limits

The HyperLogLog can estimate the cardinality of sets with up to 18,446,744,073,709,551,616 (2^64) members.

## Learn more

* [Redis new data structure: the HyperLogLog](http://antirez.com/news/75) has a lot of details about the data structure and its implementation in Redis.
* [Redis HyperLogLog Explained](https://www.youtube.com/watch?v=MunL8nnwscQ) shows you how to use Redis HyperLogLog data structures to build a traffic heat map.


