# Bloom filter

```json metadata
{
  "schema_version": 2,
  "title": "Bloom filter",
  "description": "Bloom filters are a probabilistic data structure that checks for presence of an item in a set",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"use-cases","title":"Use cases"},{"id":"example","title":"Example"},{"children":[{"id":"total-size-of-a-bloom-filter","title":"Total size of a Bloom filter"}],"id":"reserving-bloom-filters","title":"Reserving Bloom filters"},{"id":"bloom-vs-cuckoo-filters","title":"Bloom vs. Cuckoo filters"},{"id":"performance","title":"Performance"},{"id":"academic-sources","title":"Academic sources"},{"children":[{"id":"webinars","title":"Webinars"},{"id":"blog-posts","title":"Blog posts"}],"id":"references","title":"References"}]}

,
  "codeExamples": [{"codetabsId":"bf_tutorial-stepbloom","commands":[{"acl_categories":["@write","@fast","@bloom"],"complexity":"O(1)","name":"BF.RESERVE"},{"acl_categories":["@write","@bloom"],"complexity":"O(k)","name":"BF.ADD"},{"acl_categories":["@read","@bloom"],"complexity":"O(k)","name":"BF.EXISTS"},{"acl_categories":["@write","@bloom"],"complexity":"O(k * n)","name":"BF.MADD"},{"acl_categories":["@read","@bloom"],"complexity":"O(k * n)","name":"BF.MEXISTS"}],"description":"Bloom filter operations: Use BF.RESERVE to create a filter, BF.ADD and BF.MADD to add items, and BF.EXISTS and BF.MEXISTS to check membership when you need space-efficient probabilistic set membership testing","difficulty":"intermediate","id":"bloom","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_bf_tutorial-stepbloom"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_bf_tutorial-stepbloom"},{"id":"Node-js","panelId":"panel_Nodejs_bf_tutorial-stepbloom"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_bf_tutorial-stepbloom"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_bf_tutorial-stepbloom"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_bf_tutorial-stepbloom"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_bf_tutorial-stepbloom"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_bf_tutorial-stepbloom"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_bf_tutorial-stepbloom"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_bf_tutorial-stepbloom"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_bf_tutorial-stepbloom"}]}]
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


### Bloom filter command summary

**11 commands in this group:**

[View all bf commands](https://redis.io/commands/?group=bf)

| Command | Summary | Complexity | Since |
|---------|---------|------------|-------|
| [BF.ADD](https://redis.io/commands/bf.add/) | Adds an item to a Bloom Filter | O(k), where k is the number of hash functions u... | 1.0.0 |
| [BF.CARD](https://redis.io/commands/bf.card/) | Returns the cardinality of a Bloom filter | O(1) | 2.4.4 |
| [BF.DEBUG](https://redis.io/commands/bf.debug/) | Returns internal debug information about a Bloom Filter | O(n), where n is the number of sub-filters | 1.0.0 |
| [BF.EXISTS](https://redis.io/commands/bf.exists/) | Checks whether an item exists in a Bloom Filter | O(k), where k is the number of hash functions u... | 1.0.0 |
| [BF.INFO](https://redis.io/commands/bf.info/) | Returns information about a Bloom Filter | O(1) | 1.0.0 |
| [BF.INSERT](https://redis.io/commands/bf.insert/) | Adds one or more items to a Bloom Filter. A filter will be created if it does not exist | O(k * n), where k is the number of hash functio... | 1.0.0 |
| [BF.LOADCHUNK](https://redis.io/commands/bf.loadchunk/) | Restores a filter previously saved using SCANDUMP | O(n), where n is the capacity | 1.0.0 |
| [BF.MADD](https://redis.io/commands/bf.madd/) | Adds one or more items to a Bloom Filter. A filter will be created if it does not exist | O(k * n), where k is the number of hash functio... | 1.0.0 |
| [BF.MEXISTS](https://redis.io/commands/bf.mexists/) | Checks whether one or more items exist in a Bloom Filter | O(k * n), where k is the number of hash functio... | 1.0.0 |
| [BF.RESERVE](https://redis.io/commands/bf.reserve/) | Creates a new Bloom Filter | O(1) | 1.0.0 |

#### Bloom filter command summary (part 2)

| Command | Summary | Complexity | Since |
|---------|---------|------------|-------|
| [BF.SCANDUMP](https://redis.io/commands/bf.scandump/) | Begins an incremental save of the bloom filter | O(n), where n is the capacity | 1.0.0 |



A Bloom filter is a probabilistic data structure in Redis Open Source that enables you to check if an element is present in a set using a very small memory space of a fixed size.

Instead of storing all the items in a set, a Bloom Filter stores only the items' hashed representations, thus sacrificing some precision. The trade-off is that Bloom Filters are very space-efficient and fast.

A Bloom filter can guarantee the absence of an item from a set, but it can only give an estimation about its presence. So when it responds that an item is not present in a set (a negative answer), you can be sure that indeed is the case. But one out of every N positive answers will be wrong. Even though it looks unusual at first glance, this kind of uncertainty still has its place in computer science. There are many cases out there where a negative answer will prevent more costly operations, for example checking if a username has been taken, if a credit card has been reported as stolen, if a user has already seen an ad and much more.

## Use cases

**Financial fraud detection (finance)**

This application answers the question, "Has the user paid from this location before?", thus checking for suspicious activity in their users' shopping habits.
 
Use one Bloom filter per user, checked for every transaction. Provide an extremely fast response (local latency). Replicate in different regions in case the user moves. Prevent decreasing performance with scale.  

Using the Redis Bloom filter for this type of application provides these benefits: 

- Fast transaction completion 
- Decreased possibility for transaction to break in case of network partitions (connection needs to be kept open for a shorter time) 
- Extra layer of security for both credit card owners and retailers

Other questions a Bloom filter can help answer in the finance industry are: 

- Has the user ever made purchases in this category of products/services? 
- Do I need to skip some security steps when the user is buying with a vetted online shop (big retailers like Amazon, Apple app store...)? 
- Has this credit card been reported as lost/stolen? An additional benefit of using a Bloom filter in the last case is that financial organizations can exchange their lists of stolen/blocked credit card numbers without revealing the numbers themselves. 

**Ad placement (retail, advertising)**

This application answers these questions: 

- Has the user already seen this ad? 
- Has the user already bought this product?

Use a Bloom filter for every user, storing all bought products. The recommendation engine suggests a new product and checks if the product is in the user's Bloom filter. 

- If no, the ad is shown to the user and is added to the Bloom filter. 
- If yes, the process restarts and repeats until it finds a product that is not present in the filter. 

Using the Redis Bloom filter for this type of application provides these benefits: 

- Cost efficient way to a customized near real-time experience 
- No need to invest in expensive infrastructure  

**Check if a username is taken (SaaS, content publishing platforms)** 

This application answers this question: Has this username/email/domain name/slug already been used?
 
Use a Bloom filter for every username that has signed up. A new user types in the desired username. The app checks if the username exists in the Bloom filter. 

- If no, the user is created and the username is added to the Bloom filter. 
- If yes, the app can decide to either check the main database or reject the username. 

The query time stays the same at scale. 

Using the Redis Bloom filter for this type of application provides these benefits: 

- Very fast and efficient way to do a common operation 
- No need to invest in expensive infrastructure  

## Example

Consider a bike manufacturer that makes a million different kinds of bikes and you'd like to avoid using a duplicate model name in new models. A Bloom filter can be used to detect duplicates. In the example that follows,  you'll create a filter with space for a million entries and with a 0.1% error rate. Add one model name and check if it exists. Then add multiple model names and check if they exist.


Bloom filter operations: Use BF.RESERVE to create a filter, BF.ADD and BF.MADD to add items, and BF.EXISTS and BF.MEXISTS to check membership when you need space-efficient probabilistic set membership testing

**Difficulty:** Intermediate

**Commands:** BF.RESERVE, BF.ADD, BF.EXISTS, BF.MADD, BF.MEXISTS

**Complexity:**
- BF.RESERVE: O(1)
- BF.ADD: O(k)
- BF.EXISTS: O(k)
- BF.MADD: O(k * n)
- BF.MEXISTS: O(k * n)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> BF.RESERVE bikes:models 0.001 1000000
OK
> BF.ADD bikes:models "Smoky Mountain Striker"
(integer) 1
> BF.EXISTS bikes:models "Smoky Mountain Striker"
(integer) 1
> BF.MADD bikes:models "Rocky Mountain Racer" "Cloudy City Cruiser" "Windy City Wippet"
1) (integer) 1
2) (integer) 1
3) (integer) 1
> BF.MEXISTS bikes:models "Rocky Mountain Racer" "Cloudy City Cruiser" "Windy City Wippet"
1) (integer) 1
2) (integer) 1
3) (integer) 1
```

##### C#

```csharp
        bool res1 = db.BF().Reserve("bikes:models", 0.01, 1000);
        Console.WriteLine(res1);    // >>> True

        bool res2 = db.BF().Add("bikes:models", "Smoky Mountain Striker");
        Console.WriteLine(res2);    // >>> True

        bool res3 = db.BF().Exists("bikes:models", "Smoky Mountain Striker");
        Console.WriteLine(res3);    // >>> True

        bool[] res4 = db.BF().MAdd("bikes:models", new RedisValue[]{
            "Rocky Mountain Racer",
            "Cloudy City Cruiser",
            "Windy City Wippet"
        });
        Console.WriteLine(string.Join(", ", res4)); // >>> True, True, True

        bool[] res5 = db.BF().MExists("bikes:models", [
            "Rocky Mountain Racer",
            "Cloudy City Cruiser",
            "Windy City Wippet"
        ]);
        Console.WriteLine(string.Join(", ", res5)); // >>> True, True, True
```

##### Go

```go
	res1, err := rdb.BFReserve(ctx, "bikes:models", 0.01, 1000).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // >>> OK

	res2, err := rdb.BFAdd(ctx, "bikes:models", "Smoky Mountain Striker").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2) // >>> true

	res3, err := rdb.BFExists(ctx, "bikes:models", "Smoky Mountain Striker").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3) // >>> true

	res4, err := rdb.BFMAdd(ctx, "bikes:models",
		"Rocky Mountain Racer",
		"Cloudy City Cruiser",
		"Windy City Wippet",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4) // >>> [true true true]

	res5, err := rdb.BFMExists(ctx, "bikes:models",
		"Rocky Mountain Racer",
		"Cloudy City Cruiser",
		"Windy City Wippet",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res5) // >>> [true true true]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> bloomExample = asyncCommands
                    .bfReserve("bikes:models", 0.01, 1000)
                    .thenCompose(res1 -> {
                        System.out.println(res1);
                        // >>> OK
                        return asyncCommands.bfAdd("bikes:models", "Smoky Mountain Striker");
                    })
                    .thenCompose(res2 -> {
                        System.out.println(res2);
                        // >>> true
                        return asyncCommands.bfExists("bikes:models", "Smoky Mountain Striker");
                    })
                    .thenCompose(res3 -> {
                        System.out.println(res3);
                        // >>> true
                        return asyncCommands.bfMAdd("bikes:models",
                                "Rocky Mountain Racer",
                                "Cloudy City Cruiser",
                                "Windy City Wippet");
                    })
                    .thenCompose(res4 -> {
                        System.out.println(res4);
                        // >>> [true, true, true]
                        return asyncCommands.bfMExists("bikes:models",
                                "Rocky Mountain Racer",
                                "Cloudy City Cruiser",
                                "Windy City Wippet");
                    })
                    .thenAccept(res5 -> {
                        System.out.println(res5);
                        // >>> [true, true, true]
                    })
                    .toCompletableFuture();

            bloomExample.join();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> bloomExample = reactiveCommands
                    .bfReserve("bikes:models", 0.01, 1000)
                    .doOnNext(res1 -> {
                        System.out.println(res1);
                        // >>> OK
                    })
                    .then(reactiveCommands.bfAdd("bikes:models", "Smoky Mountain Striker"))
                    .doOnNext(res2 -> {
                        System.out.println(res2);
                        // >>> true
                    })
                    .then(reactiveCommands.bfExists("bikes:models", "Smoky Mountain Striker"))
                    .doOnNext(res3 -> {
                        System.out.println(res3);
                        // >>> true
                    })
                    .thenMany(reactiveCommands.bfMAdd("bikes:models",
                            "Rocky Mountain Racer",
                            "Cloudy City Cruiser",
                            "Windy City Wippet"))
                    .map(Value::getValue)
                    .collectList()
                    .doOnNext(res4 -> {
                        System.out.println(res4);
                        // >>> [true, true, true]
                    })
                    .thenMany(reactiveCommands.bfMExists("bikes:models",
                            "Rocky Mountain Racer",
                            "Cloudy City Cruiser",
                            "Windy City Wippet"))
                    .collectList()
                    .doOnNext(res5 -> {
                        System.out.println(res5);
                        // >>> [true, true, true]
                    })
                    .then();

            bloomExample.block();
```

##### Java (Synchronous - Jedis)

```java
        String res1 = jedis.bfReserve("bikes:models", 0.01, 1000);
        System.out.println(res1); // >>> OK


        boolean res2 = jedis.bfAdd("bikes:models", "Smoky Mountain Striker");
        System.out.println(res2); // >>> True

        boolean res3 = jedis.bfExists("bikes:models", "Smoky Mountain Striker");
        System.out.println(res3); // >>> True

        List<Boolean> res4 = jedis.bfMAdd("bikes:models",
                "Rocky Mountain Racer",
                "Cloudy City Cruiser",
                "Windy City Wippet");
        System.out.println(res4); // >>> [True, True, True]

        List<Boolean> res5 = jedis.bfMExists("bikes:models",
                "Rocky Mountain Racer",
                "Cloudy City Cruiser",
                "Windy City Wippet");
        System.out.println(res5); // >>> [True, True, True]
```

##### JavaScript (Node.js)

```javascript
const res1 = await client.bf.reserve('bikes:models', 0.01, 1000);
console.log(res1);  // >>> OK

const res2 = await client.bf.add('bikes:models', 'Smoky Mountain Striker');
console.log(res2);  // >>> true

const res3 = await client.bf.exists('bikes:models', 'Smoky Mountain Striker');
console.log(res3);  // >>> true

const res4 = await client.bf.mAdd('bikes:models', [
  'Rocky Mountain Racer',
  'Cloudy City Cruiser',
  'Windy City Wippet'
]);
console.log(res4);  // >>> [true, true, true]

const res5 = await client.bf.mExists('bikes:models', [
  'Rocky Mountain Racer',
  'Cloudy City Cruiser',
  'Windy City Wippet'
]);
console.log(res5);  // >>> [true, true, true]
```

##### PHP

```php
        $res1 = $r->bfreserve('bikes:models', 0.01, 1000);
        echo $res1 . PHP_EOL;
        // >>> OK

        $res2 = $r->bfadd('bikes:models', 'Smoky Mountain Striker');
        echo $res2 . PHP_EOL;
        // >>> 1

        $res3 = $r->bfexists('bikes:models', 'Smoky Mountain Striker');
        echo $res3 . PHP_EOL;
        // >>> 1

        $res4 = $r->bfmadd(
            'bikes:models',
            'Rocky Mountain Racer',
            'Cloudy City Cruiser',
            'Windy City Wippet'
        );
        echo json_encode($res4) . PHP_EOL;
        // >>> [1,1,1]

        $res5 = $r->bfmexists(
            'bikes:models',
            'Rocky Mountain Racer',
            'Cloudy City Cruiser',
            'Windy City Wippet'
        );
        echo json_encode($res5) . PHP_EOL;
        // >>> [1,1,1]
```

##### Python

```python
res1 = r.bf().reserve("bikes:models", 0.01, 1000)
print(res1)  # >>> True

res2 = r.bf().add("bikes:models", "Smoky Mountain Striker")
print(res2)  # >>> True

res3 = r.bf().exists("bikes:models", "Smoky Mountain Striker")
print(res3)  # >>> True

res4 = r.bf().madd(
    "bikes:models",
    "Rocky Mountain Racer",
    "Cloudy City Cruiser",
    "Windy City Wippet",
)
print(res4)  # >>> [True, True, True]

res5 = r.bf().mexists(
    "bikes:models",
    "Rocky Mountain Racer",
    "Cloudy City Cruiser",
    "Windy City Wippet",
)
print(res5)  # >>> [True, True, True]
```

##### Rust (Asynchronous)

```rust
        let _: () = r
            .bf_reserve("bikes:models", 0.001, 1_000_000)
            .await
            .expect("Failed to reserve Bloom filter");
        println!("OK"); // >>> OK

        let res1: bool = r
            .bf_add("bikes:models", "Smoky Mountain Striker")
            .await
            .expect("Failed to add item to Bloom filter");
        println!("{res1}"); // >>> true

        let res2: bool = r
            .bf_exists("bikes:models", "Smoky Mountain Striker")
            .await
            .expect("Failed to check item in Bloom filter");
        println!("{res2}"); // >>> true

        let res3: Vec<bool> = r
            .bf_madd(
                "bikes:models",
                &[
                    "Rocky Mountain Racer",
                    "Cloudy City Cruiser",
                    "Windy City Wippet",
                ],
            )
            .await
            .expect("Failed to add items to Bloom filter");
        println!("{res3:?}"); // >>> [true, true, true]

        let res4: Vec<bool> = r
            .bf_mexists(
                "bikes:models",
                &[
                    "Rocky Mountain Racer",
                    "Cloudy City Cruiser",
                    "Windy City Wippet",
                ],
            )
            .await
            .expect("Failed to check items in Bloom filter");
        println!("{res4:?}"); // >>> [true, true, true]
```

##### Rust (Synchronous)

```rust
        let _: () = r
            .bf_reserve("bikes:models", 0.001, 1_000_000)
            .expect("Failed to reserve Bloom filter");
        println!("OK"); // >>> OK

        let res1: bool = r
            .bf_add("bikes:models", "Smoky Mountain Striker")
            .expect("Failed to add item to Bloom filter");
        println!("{res1}"); // >>> true

        let res2: bool = r
            .bf_exists("bikes:models", "Smoky Mountain Striker")
            .expect("Failed to check item in Bloom filter");
        println!("{res2}"); // >>> true

        let res3: Vec<bool> = r
            .bf_madd(
                "bikes:models",
                &[
                    "Rocky Mountain Racer",
                    "Cloudy City Cruiser",
                    "Windy City Wippet",
                ],
            )
            .expect("Failed to add items to Bloom filter");
        println!("{res3:?}"); // >>> [true, true, true]

        let res4: Vec<bool> = r
            .bf_mexists(
                "bikes:models",
                &[
                    "Rocky Mountain Racer",
                    "Cloudy City Cruiser",
                    "Windy City Wippet",
                ],
            )
            .expect("Failed to check items in Bloom filter");
        println!("{res4:?}"); // >>> [true, true, true]
```



Note: there is always a chance that even with just a few items, there could be a false positive, meaning an item could "exist" even though it has not been explicitly added to the Bloom filter. For a more in depth understanding of the probabilistic nature of a Bloom filter, check out the blog posts linked at the bottom of this page.

## Reserving Bloom filters
With the Redis Bloom filter, most of the sizing work is done for you: 

```
BF.RESERVE {key} {error_rate} {capacity} [EXPANSION expansion] [NONSCALING]
```

#### 1. False positives rate (`error_rate`)
The rate is a decimal value between 0 and 1. For example, for a desired false positive rate of 0.1% (1 in 1000), error_rate should be set to 0.001.

#### 2. Expected capacity (`capacity`)
This is the number of items you expect having in your filter in total and is trivial when you have a static set but it becomes more challenging when your set grows over time. It's important to get the number right because if you **oversize** - you'll end up wasting memory. If you **undersize**, the filter will fill up and a new one will have to be stacked on top of it (sub-filter stacking). In the cases when a filter consists of multiple sub-filters stacked on top of each other latency for adds stays the same, but the latency for presence checks increases. The reason for this is the way the checks work: a regular check would first be performed on the top (latest) filter and if a negative answer is returned the next one is checked and so on. That's where the added latency comes from.

#### 3. Scaling (`EXPANSION`)
Adding an item to a Bloom filter never fails due to the data structure "filling up". Instead, the error rate starts to grow. To keep the error close to the one set on filter initialization, the Bloom filter will auto-scale, meaning, when capacity is reached, an additional sub-filter will be created.  
 The size of the new sub-filter is the size of the last sub-filter multiplied by `EXPANSION`. If the number of items to be stored in the filter is unknown, we recommend that you use an expansion of 2 or more to reduce the number of sub-filters. Otherwise, we recommend that you use an expansion of 1 to reduce memory consumption. The default expansion value is 2. 
 
 The filter will keep adding more hash functions for every new sub-filter in order to keep your desired error rate. 

Maybe you're wondering "Why would I create a smaller filter with a high expansion rate if I know I'm going to scale anyway?"; the answer is: for cases where you need to keep many filters (let's say a filter per user, or per product) and most of them will stay small, but some with more activity will have to scale. 

#### 4. `NONSCALING`
If you know you're not going to scale use the `NONSCALING` flag because that way the filter will use one hash function less. Just remember that if you ever do reach the initially assigned capacity - your error rate will start to grow.


### Total size of a Bloom filter
The actual memory used by a Bloom filter is a function of the chosen error rate:

The optimal number of hash functions is `ceil(-ln(error_rate) / ln(2))`.

The required number of bits per item, given the desired `error_rate` and the optimal number of hash functions, is `-ln(error_rate) / ln(2)^2`. Hence, the required number of bits in the filter is `capacity * -ln(error_rate) / ln(2)^2`.

* **1%**    error rate requires  7 hash functions and  9.585 bits per item.
* **0.1%**  error rate requires 10 hash functions and 14.378 bits per item.
* **0.01%** error rate requires 14 hash functions and 19.170 bits per item.

Just as a comparison, when using a Redis set for membership testing the memory needed is:

```
memory_with_sets = capacity*(192b + value)
```

For a set of IP addresses, for example, we would have around 40 bytes (320 bits) per item - considerably higher than the 19.170 bits we need for a Bloom filter with a 0.01% false positives rate.


## Bloom vs. Cuckoo filters
Bloom filters typically exhibit better performance and scalability when inserting
items (so if you're often adding items to your dataset, then a Bloom filter may be ideal).
Cuckoo filters are quicker on check operations and also allow deletions.


## Performance

Insertion in a Bloom filter is O(K), where `k` is the number of hash functions. 

Checking for an item is O(K) or O(K*n) for stacked filters, where n is the number of stacked filters.


## Academic sources
- [Space/Time Trade-offs in Hash Coding with Allowable Errors](http://www.dragonwins.com/domains/getteched/bbc/literature/Bloom70.pdf) by Burton H. Bloom.
- [Scalable Bloom Filters](https://gsd.di.uminho.pt/members/cbm/ps/dbloom.pdf)

## References
### Webinars
1. [Probabilistic Data Structures - The most useful thing in Redis you probably aren't using](https://youtu.be/dq-0xagF7v8?t=102)

### Blog posts
1. [RedisBloom Quick Start Tutorial](https://docs.redis.com/latest/modules/redisbloom/redisbloom-quickstart/)
1. [Developing with Bloom Filters](https://redis.io/blog/bloom-filter/)
1. [RedisBloom on Redis Software](https://redis.com/redis-enterprise/redis-bloom/)
1. [Probably and No: Redis, RedisBloom, and Bloom Filters](https://redis.com/blog/redis-redisbloom-bloom-filters/)


