# Cuckoo filter

```json metadata
{
  "schema_version": 2,
  "title": "Cuckoo filter",
  "description": "Cuckoo filters are a probabilistic data structure that checks for presence of an element in a set",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"use-cases","title":"Use cases"},{"id":"examples","title":"Examples"},{"id":"bloom-vs-cuckoo-filters","title":"Bloom vs. Cuckoo filters"},{"children":[{"id":"choosing-the-capacity--capacity","title":"Choosing the capacity (capacity)"},{"id":"choosing-the-bucket-size-bucketsize","title":"Choosing the bucket size (BUCKETSIZE)"},{"id":"choosing-the-scaling-factor-expansion","title":"Choosing the scaling factor (EXPANSION)"},{"id":"choosing-the-maximum-number-of-iterations-maxiterations","title":"Choosing the maximum number of iterations (MAXITERATIONS)"},{"id":"interesting-facts","title":"Interesting facts:"}],"id":"sizing-cuckoo-filters","title":"Sizing Cuckoo filters"},{"id":"performance","title":"Performance"},{"id":"academic-sources","title":"Academic sources"}]}

,
  "codeExamples": [{"codetabsId":"cuckoo_tutorial-stepcuckoo","commands":[{"acl_categories":["@write","@fast","@cuckoo"],"complexity":"O(1)","name":"CF.RESERVE"},{"acl_categories":["@write","@cuckoo"],"complexity":"O(k + i)","name":"CF.ADD"},{"acl_categories":["@read","@cuckoo"],"complexity":"O(k)","name":"CF.EXISTS"},{"acl_categories":["@write","@cuckoo"],"complexity":"O(k)","name":"CF.DEL"}],"description":"Cuckoo filter operations: Use CF.RESERVE to create a filter, CF.ADD to add items, CF.EXISTS to check membership, and CF.DEL to remove items when you need space-efficient probabilistic set membership testing with deletion support","difficulty":"intermediate","id":"cuckoo","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_cuckoo_tutorial-stepcuckoo"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_cuckoo_tutorial-stepcuckoo"},{"id":"Node-js","panelId":"panel_Nodejs_cuckoo_tutorial-stepcuckoo"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_cuckoo_tutorial-stepcuckoo"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_cuckoo_tutorial-stepcuckoo"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_cuckoo_tutorial-stepcuckoo"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_cuckoo_tutorial-stepcuckoo"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_cuckoo_tutorial-stepcuckoo"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_cuckoo_tutorial-stepcuckoo"}]}]
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


### Cuckoo filter command summary

**13 commands in this group:**

[View all cf commands](https://redis.io/commands/?group=cf)

| Command | Summary | Complexity | Since |
|---------|---------|------------|-------|
| [CF.ADD](https://redis.io/commands/cf.add/) | Adds an item to a Cuckoo Filter | O(k + i), where k is the number of sub-filters ... | 1.0.0 |
| [CF.ADDNX](https://redis.io/commands/cf.addnx/) | Adds an item to a Cuckoo Filter if the item did not exist previously. | O(k + i), where k is the number of sub-filters ... | 1.0.0 |
| [CF.COUNT](https://redis.io/commands/cf.count/) | Return the number of times an item might be in a Cuckoo Filter | O(k), where k is the number of sub-filters | 1.0.0 |
| [CF.DEBUG](https://redis.io/commands/cf.debug/) | Returns internal debug information about a Cuckoo Filter | O(1) | 1.0.0 |
| [CF.DEL](https://redis.io/commands/cf.del/) | Deletes an item from a Cuckoo Filter | O(k), where k is the number of sub-filters | 1.0.0 |
| [CF.EXISTS](https://redis.io/commands/cf.exists/) | Checks whether one or more items exist in a Cuckoo Filter | O(k), where k is the number of sub-filters | 1.0.0 |
| [CF.INFO](https://redis.io/commands/cf.info/) | Returns information about a Cuckoo Filter | O(1) | 1.0.0 |
| [CF.INSERT](https://redis.io/commands/cf.insert/) | Adds one or more items to a Cuckoo Filter. A filter will be created if it does not exist | O(n * (k + i)), where n is the number of items,... | 1.0.0 |
| [CF.INSERTNX](https://redis.io/commands/cf.insertnx/) | Adds one or more items to a Cuckoo Filter if the items did not exist previously. A filter will be created if it does not exist | O(n * (k + i)), where n is the number of items,... | 1.0.0 |
| [CF.LOADCHUNK](https://redis.io/commands/cf.loadchunk/) | Restores a filter previously saved using SCANDUMP | O(n), where n is the capacity | 1.0.0 |

#### Cuckoo filter command summary (part 2)

| Command | Summary | Complexity | Since |
|---------|---------|------------|-------|
| [CF.MEXISTS](https://redis.io/commands/cf.mexists/) | Checks whether one or more items exist in a Cuckoo Filter | O(k * n), where k is the number of sub-filters ... | 1.0.0 |
| [CF.RESERVE](https://redis.io/commands/cf.reserve/) | Creates a new Cuckoo Filter | O(1) | 1.0.0 |
| [CF.SCANDUMP](https://redis.io/commands/cf.scandump/) | Begins an incremental save of the bloom filter | O(n), where n is the capacity | 1.0.0 |



A Cuckoo filter, just like a Bloom filter, is a probabilistic data structure in Redis Open Source that enables you to check if an element is present in a set in a very fast and space efficient way, while also allowing for deletions and showing better performance than Bloom in some scenarios.

While the Bloom filter is a bit array with flipped bits at positions decided by the hash function, a Cuckoo filter is an array of buckets, storing fingerprints of the values in one of the buckets at positions decided by the two hash functions. A membership query for item `x` searches the possible buckets for the fingerprint of `x`, and returns true if an identical fingerprint is found. A cuckoo filter's fingerprint size will directly determine the false positive rate.


## Use cases

**Targeted ad campaigns (advertising, retail)** 

This application answers this question: Has the user signed up for this campaign yet?

Use a Cuckoo filter for every campaign, populated with targeted users' ids. On every visit, the user id is checked against one of the Cuckoo filters. 

- If yes, the user has not signed up for campaign. Show the ad.
- If the user clicks ad and signs up, remove the user id from that Cuckoo filter. 
- If no, the user has signed up for that campaign. Try the next ad/Cuckoo filter. 
 
**Discount code/coupon validation (retail, online shops)** 

This application answers this question: Has this discount code/coupon been used yet?

Use a Cuckoo filter populated with all discount codes/coupons. On every try, the entered code is checked against the filter. 

- If no, the coupon is not valid. 
- If yes, the coupon can be valid. Check the main database. If valid, remove from Cuckoo filter as `used`.

Note> In addition to these two cases, Cuckoo filters serve very well all the Bloom filter use cases.

## Examples

> You'll learn how to create an empty cuckoo filter with an initial capacity for 1,000 items, add items, check their existence, and remove them. Even though the [`CF.ADD`](https://redis.io/docs/latest/commands/cf.add) command can create a new filter if one isn't present, it might not be optimally sized for your needs. It's better to use the [`CF.RESERVE`](https://redis.io/docs/latest/commands/cf.reserve) command to set up a filter with your preferred capacity.

Cuckoo filter operations: Use CF.RESERVE to create a filter, CF.ADD to add items, CF.EXISTS to check membership, and CF.DEL to remove items when you need space-efficient probabilistic set membership testing with deletion support

**Difficulty:** Intermediate

**Commands:** CF.RESERVE, CF.ADD, CF.EXISTS, CF.DEL

**Complexity:**
- CF.RESERVE: O(1)
- CF.ADD: O(k + i)
- CF.EXISTS: O(k)
- CF.DEL: O(k)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python

##### Redis CLI

```
> CF.RESERVE bikes:models 1000
OK
> CF.ADD bikes:models "Smoky Mountain Striker"
(integer) 1
> CF.EXISTS bikes:models "Smoky Mountain Striker"
(integer) 1
> CF.EXISTS bikes:models "Terrible Bike Name"
(integer) 0
> CF.DEL bikes:models "Smoky Mountain Striker"
(integer) 1
```

##### C#

```csharp
        bool res1 = db.CF().Reserve("bikes:models", 1000000);
        Console.WriteLine(res1);    // >>> True

        bool res2 = db.CF().Add("bikes:models", "Smoky Mountain Striker");
        Console.WriteLine(res2);    // >>> True

        bool res3 = db.CF().Exists("bikes:models", "Smoky Mountain Striker");
        Console.WriteLine(res3);    // >>> True

        bool res4 = db.CF().Exists("bikes:models", "Terrible Bike Name");
        Console.WriteLine(res4);    // >>> False

        bool res5 = db.CF().Del("bikes:models", "Smoky Mountain Striker");
        Console.WriteLine(res5);    // >>> True
```

##### Go

```go
	res1, err := rdb.CFReserve(ctx, "bikes:models", 1000000).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // >>> OK

	res2, err := rdb.CFAdd(ctx, "bikes:models", "Smoky Mountain Striker").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2) // >>> true

	res3, err := rdb.CFExists(ctx, "bikes:models", "Smoky Mountain Striker").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3) // >>> true

	res4, err := rdb.CFExists(ctx, "bikes:models", "Terrible Bike Name").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4) // >>> false

	res5, err := rdb.CFDel(ctx, "bikes:models", "Smoky Mountain Striker").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res5) // >>> true
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> cuckooExample = asyncCommands
                    .cfReserve("bikes:models", 1000000L)
                    .thenCompose(res1 -> {
                        System.out.println(res1);
                        // >>> OK
                        return asyncCommands.cfAdd("bikes:models", "Smoky Mountain Striker");
                    })
                    .thenCompose(res2 -> {
                        System.out.println(res2);
                        // >>> true
                        return asyncCommands.cfExists("bikes:models", "Smoky Mountain Striker");
                    })
                    .thenCompose(res3 -> {
                        System.out.println(res3);
                        // >>> true
                        return asyncCommands.cfExists("bikes:models", "Terrible Bike Name");
                    })
                    .thenCompose(res4 -> {
                        System.out.println(res4);
                        // >>> false
                        return asyncCommands.cfDel("bikes:models", "Smoky Mountain Striker");
                    })
                    .thenAccept(res5 -> {
                        System.out.println(res5);
                        // >>> true
                    })
                    .toCompletableFuture();

            cuckooExample.join();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> cuckooExample = reactiveCommands
                    .cfReserve("bikes:models", 1000000L)
                    .doOnNext(res1 -> {
                        System.out.println(res1);
                        // >>> OK
                    })
                    .then(reactiveCommands.cfAdd("bikes:models", "Smoky Mountain Striker"))
                    .doOnNext(res2 -> {
                        System.out.println(res2);
                        // >>> true
                    })
                    .then(reactiveCommands.cfExists("bikes:models", "Smoky Mountain Striker"))
                    .doOnNext(res3 -> {
                        System.out.println(res3);
                        // >>> true
                    })
                    .then(reactiveCommands.cfExists("bikes:models", "Terrible Bike Name"))
                    .doOnNext(res4 -> {
                        System.out.println(res4);
                        // >>> false
                    })
                    .then(reactiveCommands.cfDel("bikes:models", "Smoky Mountain Striker"))
                    .doOnNext(res5 -> {
                        System.out.println(res5);
                        // >>> true
                    })
                    .then();

            cuckooExample.block();
```

##### Java (Synchronous - Jedis)

```java
        String res1 = jedis.cfReserve("bikes:models", 1000000);
        System.out.println(res1); // >>> OK


        boolean res2 = jedis.cfAdd("bikes:models", "Smoky Mountain Striker");
        System.out.println(res2); // >>> True

        boolean res3 = jedis.cfExists("bikes:models", "Smoky Mountain Striker");
        System.out.println(res3); // >>> True

        boolean res4 = jedis.cfExists("bikes:models", "Terrible Bike Name");
        System.out.println(res4); // >>> False

        boolean res5 = jedis.cfDel("bikes:models", "Smoky Mountain Striker");
        System.out.println(res5); // >>> True

```

##### JavaScript (Node.js)

```javascript
const res1 = await client.cf.reserve('bikes:models', 1000000);
console.log(res1);  // >>> OK

const res2 = await client.cf.add('bikes:models', 'Smoky Mountain Striker');
console.log(res2);  // >>> true

const res3 = await client.cf.exists('bikes:models', 'Smoky Mountain Striker');
console.log(res3);  // >>> true

const res4 = await client.cf.exists('bikes:models', 'Terrible Bike Name');
console.log(res4);  // >>> false

const res5 = await client.cf.del('bikes:models', 'Smoky Mountain Striker');
console.log(res5);  // >>> true
```

##### PHP

```php
        $res1 = $r->cfreserve('bikes:models', 1000000);
        echo $res1 . PHP_EOL;
        // >>> OK

        $res2 = $r->cfadd('bikes:models', 'Smoky Mountain Striker');
        echo $res2 . PHP_EOL;
        // >>> 1

        $res3 = $r->cfexists('bikes:models', 'Smoky Mountain Striker');
        echo $res3 . PHP_EOL;
        // >>> 1

        $res4 = $r->cfexists('bikes:models', 'Terrible Bike Name');
        echo $res4 . PHP_EOL;
        // >>> 0

        $res5 = $r->cfdel('bikes:models', 'Smoky Mountain Striker');
        echo $res5 . PHP_EOL;
        // >>> 1
```

##### Python

```python
res1 = r.cf().reserve("bikes:models", 1000000)
print(res1)  # >>> True

res2 = r.cf().add("bikes:models", "Smoky Mountain Striker")
print(res2)  # >>> 1

res3 = r.cf().exists("bikes:models", "Smoky Mountain Striker")
print(res3)  # >>> 1

res4 = r.cf().exists("bikes:models", "Terrible Bike Name")
print(res4)  # >>> 0

res5 = r.cf().delete("bikes:models", "Smoky Mountain Striker")
print(res5)  # >>> 1
```



## Bloom vs. Cuckoo filters
Bloom filters typically exhibit better performance and scalability when inserting
items (so if you're often adding items to your dataset, then a Bloom filter may be ideal).
Cuckoo filters are quicker on check operations and also allow deletions.

## Sizing Cuckoo filters

These are the main parameters and features of a cuckoo filter:

- `p` target false positive rate  
- `f` fingerprint length in bits
- `α` fill rate or load factor (0≤α≤1)
- `b` number of entries per bucket
- `m` number of buckets
- `n` number of items
- `C` average bits per item

Let's start by remembering that a cuckoo filter bucket can have multiple entries (where each entry stores one fingerprint). If we end up having all entries occupied with a fingerprint then we won't have empty slots to save new elements and the filter will be declared full, that's why we should always maintain a certain percentage of our cuckoo filter free.  
As a result of this the "real" memory cost of an item should include that overhead in addition to the fingerprint size. If `α` is the load factor (fingerprint size / total filter size) and `f` is the number of bits in an entry the amortised space cost `f/α bits`.

When you initialise a new filter you are asked to choose its capacity and bucket size. 

```
CF.RESERVE {key} {capacity} [BUCKETSIZE bucketSize] [MAXITERATIONS maxIterations]
[EXPANSION expansion]
``` 

### Choosing the capacity  (`capacity`)

The capacity of a Cuckoo filter is calculated as

```
capacity = n*f/α
```
where `n` is the number of elements you expect to have in your filter, `f` is the fingerprint length in bits which is set to `8` and `α` is the fill factor. So in order to get your filter capacity you must first choose a fill factor. The fill factor will determine the density of your data and of course the memory. 
The capacity will be rounded up to the next "power of two (2<sup>n</sup>)" number.

> Please note that inserting repeated items in a cuckoo filter will try to add them multiple times causing your filter to fill up

Because of how Cuckoo Filters work, the filter is likely to declare itself full before capacity is reached and therefore fill rate will likely never reach 100%.


### Choosing the bucket size (`BUCKETSIZE`)
Number of items in each bucket. A higher bucket size value improves the fill rate but also causes a higher error rate and slightly slower performance.

```
error_rate = (buckets * hash_functions)/2^fingerprint_size = (buckets*2)/256
```

When bucket size of 1 is used the fill rate is 55% and false positive error rate is 2/256 ≈ 0.78% **which is the minimal false positive rate you can achieve**. Larger buckets increase the error rate linearly but improve the fill rate of the filter. For example, a bucket size of 3 yields a 2.34% error rate and an 80% fill rate. Bucket size of 4 yields a 3.12% error rate and a 95% fill rate. 

### Choosing the scaling factor (`EXPANSION`)

When the filter self-declares itself full, it will auto-expand by generating additional sub-filters at the cost of reduced performance and increased error rate. The new sub-filter is created with size of the previous sub-filter multiplied by `EXPANSION` (chosen on filter creation). Like bucket size, additional sub-filters grow the error rate linearly (the compound error is a sum of all subfilters' errors). The size of the new sub-filter is the size of the last sub-filter multiplied by expansion and this is something very important to keep in mind. If you know you'll have to scale at some point it's better to choose a higher expansion value. The default is [`cf-expansion-factor`](https://redis.io/docs/latest/develop/data-types/probabilistic/configuration#cf-expansion-factor).

Maybe you're wondering "Why would I create a smaller filter with a high expansion rate if I know I'm going to scale anyway?"; the answer is: for cases where you need to keep many filters (let's say a filter per user, or per product) and most of them will stay small, but some with more activity will have to scale. 

The expansion factor will be rounded up to the next "power of two (2<sup>n</sup>)" number.

### Choosing the maximum number of iterations (`MAXITERATIONS`)
`MAXITERATIONS` dictates the number of attempts to find a slot for the incoming fingerprint. Once the filter gets full, a high MAXITERATIONS value will slow down insertions. The default value is [`cf-max-iterations`](https://redis.io/docs/latest/develop/data-types/probabilistic/configuration#cf-max-iterations).

### Interesting facts: 
- Unused capacity in prior sub-filters is automatically used when possible. 
- The filter can grow up to [`cf-max-expansions`](https://redis.io/docs/latest/develop/data-types/probabilistic/configuration#cf-max-expansions) times.
- You can delete items to stay within filter limits instead of rebuilding
- Adding the same element multiple times will create multiple entries, thus filling up your filter.


## Performance
Adding an element to a Cuckoo filter has a time complexity of O(1).

Similarly, checking for an element and deleting an element also has a time complexity of O(1).



## Academic sources
- [Cuckoo Filter: Practically Better Than Bloom](https://www.cs.cmu.edu/~dga/papers/cuckoo-conext2014.pdf)

