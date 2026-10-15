# Top-K

```json metadata
{
  "schema_version": 2,
  "title": "Top-K",
  "description": "Top-K is a probabilistic data structure that allows you to find the most frequent items in a data stream.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"use-case","title":"Use case"},{"id":"example","title":"Example"},{"id":"sizing","title":"Sizing"},{"id":"performance","title":"Performance"},{"id":"academic-sources","title":"Academic sources"},{"id":"references","title":"References"}]}

,
  "codeExamples": [{"codetabsId":"topk_tutorial-steptopk","commands":[{"acl_categories":["@write","@fast","@topk"],"complexity":"O(1)","name":"TOPK.RESERVE"},{"acl_categories":["@write","@topk"],"complexity":"O(n * k)","name":"TOPK.ADD"},{"acl_categories":["@read","@topk"],"complexity":"O(k*log(k)","name":"TOPK.LIST"},{"acl_categories":["@read","@topk"],"complexity":"O(n)","name":"TOPK.QUERY"}],"description":"Top-K operations: Use TOPK.RESERVE to initialize a sketch, TOPK.ADD to track item frequencies, TOPK.LIST to retrieve top items, and TOPK.QUERY to check membership when you need to identify the most frequent items in a data stream","difficulty":"intermediate","id":"topk","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_topk_tutorial-steptopk"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_topk_tutorial-steptopk"},{"id":"Node-js","panelId":"panel_Nodejs_topk_tutorial-steptopk"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_topk_tutorial-steptopk"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_topk_tutorial-steptopk"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_topk_tutorial-steptopk"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_topk_tutorial-steptopk"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_topk_tutorial-steptopk"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_topk_tutorial-steptopk"}]}]
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


### Top-K command summary

**7 commands in this group:**

[View all topk commands](https://redis.io/commands/?group=topk)

| Command | Summary | Complexity | Since |
|---------|---------|------------|-------|
| [TOPK.ADD](https://redis.io/commands/topk.add/) | Adds an item to a Top-k sketch. Multiple items can be added at the same time. | O(n * k) where n is the number of items and k i... | 2.0.0 |
| [TOPK.COUNT](https://redis.io/commands/topk.count/) | Return the count for one or more items are in a sketch | O(n) where n is the number of items | 2.0.0 |
| [TOPK.INCRBY](https://redis.io/commands/topk.incrby/) | Increases the count of one or more items by increment | O(n * k * incr) where n is the number of items,... | 2.0.0 |
| [TOPK.INFO](https://redis.io/commands/topk.info/) | Returns information about a sketch | O(1) | 2.0.0 |
| [TOPK.LIST](https://redis.io/commands/topk.list/) | Return the full list of items in Top-K sketch. | O(k*log(k)) where k is the value of top-k | 2.0.0 |
| [TOPK.QUERY](https://redis.io/commands/topk.query/) | Checks whether one or more items are in a sketch | O(n) where n is the number of items | 2.0.0 |
| [TOPK.RESERVE](https://redis.io/commands/topk.reserve/) | Initializes a Top-K sketch with specified parameters | O(1) | 2.0.0 |



Top K is a probabilistic data structure in Redis Open Source used to estimate the `K` highest-rank elements from a stream.

"Highest-rank" in this case means "elements with a highest number or score attached to them", where the score can be a count of how many times the element has appeared in the stream - thus making the data structure perfect for finding the elements with the highest frequency in a stream.
One very common application is detecting network anomalies and DDoS attacks where Top K can answer the question: Is there a sudden increase in the flux of requests to the same address or from the same IP?
 
There is, indeed, some overlap with the functionality of Count-Min Sketch, but the two data structures have their differences and should be applied for different use cases. 

The Redis Open Source implementation of Top-K is based on the [HeavyKeepers](https://www.usenix.org/conference/atc18/presentation/gong) algorithm presented by Junzhi Gong et al. It discards some older approaches like "count-all" and "admit-all-count-some" in favour of a "**count-with-exponential-decay**" strategy which is biased against mouse (small) flows and has a limited impact on elephant (large) flows. This implementation uses two data structures in tandem: a hash table that holds the probabilistic counts (much like the Count-Min Sketch), and a min heap that holds the `K` items with the highest counts. This ensures high accuracy with shorter execution times than previous probabilistic algorithms allowed, while keeping memory utilization to a fraction of what is typically required by a Sorted Set. It has the additional benefit of being able to get real time notifications when elements are added or removed from the Top K list. 

## Use case

**Trending hashtags (social media platforms, news distribution networks)** 

This application answers these questions: 

- What are the K hashtags people have mentioned the most in the last X hours? 
- What are the K news with highest read/view count today? 

Data flow is the incoming social media posts from which you parse out the different hashtags. 

The [`TOPK.LIST`](https://redis.io/docs/latest/commands/topk.list) command has a time complexity of `O(K*log(k))` so if `K` is small, there is no need to keep a separate set or sorted set of all the hashtags. You can query directly from the Top K itself. 

## Example

This example will show you how to track key words used "bike" when shopping online; e.g., "bike store" and "bike handlebars". Proceed as follows.
​
* Use [`TOPK.RESERVE`](https://redis.io/docs/latest/commands/topk.reserve) to initialize a top K sketch with specific parameters. Note: the `width`, `depth`, and `decay_constant` parameters can be omitted, as they will be set to the default values 7, 8, and 0.9, respectively, if not present.
​
 ```
 > TOPK.RESERVE key k width depth decay_constant
 ```
 
 * Use [`TOPK.ADD`](https://redis.io/docs/latest/commands/topk.add) to add items to the sketch. As you can see, multiple items can be added at the same time. If an item is returned when adding additional items, it means that item was demoted out of the min heap of the top items, below it will mean the returned item is no longer in the top 5, otherwise `nil` is returned. This allows dynamic heavy-hitter detection of items being entered or expelled from top K list.
​
In the example below, "pedals" displaces "handlebars", which is returned after "pedals" is added. Also note that the addition of both "store" and "seat" a second time don't return anything, as they're already in the top K.
 
 * Use [`TOPK.LIST`](https://redis.io/docs/latest/commands/topk.list) to list the items entered thus far.
​
 * Use [`TOPK.QUERY`](https://redis.io/docs/latest/commands/topk.query) to see if an item is on the top K list. Just like [`TOPK.ADD`](https://redis.io/docs/latest/commands/topk.add) multiple items can be queried at the same time.
Top-K operations: Use TOPK.RESERVE to initialize a sketch, TOPK.ADD to track item frequencies, TOPK.LIST to retrieve top items, and TOPK.QUERY to check membership when you need to identify the most frequent items in a data stream

**Difficulty:** Intermediate

**Commands:** TOPK.RESERVE, TOPK.ADD, TOPK.LIST, TOPK.QUERY

**Complexity:**
- TOPK.RESERVE: O(1)
- TOPK.ADD: O(n * k)
- TOPK.LIST: O(k*log(k)
- TOPK.QUERY: O(n)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python

##### Redis CLI

```
> TOPK.RESERVE bikes:keywords 5 2000 7 0.925
OK
> TOPK.ADD bikes:keywords store seat handlebars handles pedals tires store seat
1) (nil)
2) (nil)
3) (nil)
4) (nil)
5) (nil)
6) "handlebars"
7) (nil)
8) (nil)
> TOPK.LIST bikes:keywords
1) "store"
2) "seat"
3) "pedals"
4) "tires"
5) "handles"
> TOPK.QUERY bikes:keywords store handlebars
1) (integer) 1
2) (integer) 0
```

##### C#

```csharp
        bool res1 = db.TOPK().Reserve("bikes:keywords", 5, 2000, 7, 0.925);
        Console.WriteLine(res1);    // >>> True

        RedisResult[]? res2 = db.TOPK().Add("bikes:keywords",
                "store",
                "seat",
                "handlebars",
                "handles",
                "pedals",
                "tires",
                "store",
                "seat"
        );

        if (res2 is not null)
        {
            Console.WriteLine(string.Join(", ", string.Join(", ", res2.Select(r => $"{(r.IsNull ? "Null" : r)}"))));
            // >>> Null, Null, Null, Null, Null, handlebars, Null, Null
        }

        RedisResult[] res3 = db.TOPK().List("bikes:keywords");

        if (res3 is not null)
        {
            Console.WriteLine(string.Join(", ", string.Join(", ", res3.Select(r => $"{(r.IsNull ? "Null" : r)}"))));
            // >>> store, seat, pedals, tires, handles
        }

        bool[] res4 = db.TOPK().Query("bikes:keywords", "store", "handlebars");
        Console.WriteLine(string.Join(", ", res4)); // >>> True, False
```

##### Go

```go
	res1, err := rdb.TopKReserve(ctx, "bikes:keywords", 5).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // >>> OK

	res2, err := rdb.TopKAdd(ctx, "bikes:keywords",
		"store",
		"seat",
		"handlebars",
		"handles",
		"pedals",
		"tires",
		"store",
		"seat",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2) // >>> [     handlebars  ]

	res3, err := rdb.TopKList(ctx, "bikes:keywords").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3) // [store seat pedals tires handles]

	res4, err := rdb.TopKQuery(ctx, "bikes:keywords", "store", "handlebars").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4) // [true false]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> topKExample = asyncCommands
                    .topKReserve("bikes:keywords", 5L,
                            TopKReserveArgs.Builder.width(2000L).depth(7L).decay(0.925))
                    .thenCompose(res1 -> {
                        System.out.println(res1);
                        // >>> OK
                        return asyncCommands.topKAdd("bikes:keywords",
                                "store", "seat", "handlebars", "handles", "pedals",
                                "tires", "store", "seat");
                    })
                    .thenCompose(res2 -> {
                        System.out.println(res2);
                        // >>> [null, null, null, null, null, handlebars, null, null]
                        return asyncCommands.topKList("bikes:keywords");
                    })
                    .thenCompose(res3 -> {
                        System.out.println(res3);
                        // >>> [store, seat, pedals, tires, handles]
                        return asyncCommands.topKQuery("bikes:keywords", "store", "handlebars");
                    })
                    .thenAccept(res4 -> {
                        System.out.println(res4);
                        // >>> [true, false]
                    })
                    .toCompletableFuture();

            topKExample.join();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> topKExample = reactiveCommands
                    .topKReserve("bikes:keywords", 5L,
                            TopKReserveArgs.Builder.width(2000L).depth(7L).decay(0.925))
                    .doOnNext(res1 -> {
                        System.out.println(res1);
                        // >>> OK
                    })
                    .thenMany(reactiveCommands.topKAdd("bikes:keywords",
                            "store", "seat", "handlebars", "handles", "pedals",
                            "tires", "store", "seat"))
                    .collectList()
                    .doOnNext(res2 -> {
                        System.out.println(res2);
                        // >>> [Value.empty, Value.empty, Value.empty, Value.empty, Value.empty, Value[handlebars], Value.empty, Value.empty]
                    })
                    .thenMany(reactiveCommands.topKList("bikes:keywords"))
                    .collectList()
                    .doOnNext(res3 -> {
                        System.out.println(res3);
                        // >>> [store, seat, pedals, tires, handles]
                    })
                    .thenMany(reactiveCommands.topKQuery("bikes:keywords", "store", "handlebars"))
                    .collectList()
                    .doOnNext(res4 -> {
                        System.out.println(res4);
                        // >>> [true, false]
                    })
                    .then();

            topKExample.block();
```

##### Java (Synchronous - Jedis)

```java
        String res1 = jedis.topkReserve("bikes:keywords", 5L, 2000L, 7L, 0.925D);
        System.out.println(res1); // >>> True

        List<String> res2 = jedis.topkAdd("bikes:keywords",
                "store",
                "seat",
                "handlebars",
                "handles",
                "pedals",
                "tires",
                "store",
                "seat");

        System.out.println(res2); // >>> [None, None, None, None, None, 'handlebars', None, None]

        List<String> res3 = jedis.topkList("bikes:keywords");
        System.out.println(res3); // >>> ['store', 'seat', 'pedals', 'tires', 'handles']

        List<Boolean> res4 = jedis.topkQuery("bikes:keywords", "store", "handlebars");
        System.out.println(res4); // >>> [1, 0]
```

##### JavaScript (Node.js)

```javascript
const res1 = await client.topK.reserve('bikes:keywords', 5, {
    width: 2000,
    depth: 7,
    decay: 0.925
});
console.log(res1);  // >>> OK

const res2 = await client.topK.add('bikes:keywords', [
  'store',
  'seat',
  'handlebars',
  'handles',
  'pedals',
  'tires',
  'store',
  'seat'
]);
console.log(res2);  // >>> [null, null, null, null, null, 'handlebars', null, null]

const res3 = await client.topK.list('bikes:keywords');
console.log(res3);  // >>> ['store', 'seat', 'pedals', 'tires', 'handles']

const res4 = await client.topK.query('bikes:keywords', ['store', 'handlebars']);
console.log(res4);  // >>> [true, false]
```

##### PHP

```php
        $res1 = $r->topkreserve('bikes:keywords', 5, 2000, 7, 0.925);
        echo $res1 . PHP_EOL;
        // >>> OK

        $res2 = $r->topkadd(
            'bikes:keywords',
            'store',
            'seat',
            'handlebars',
            'handles',
            'pedals',
            'tires',
            'store',
            'seat',
        );
        echo json_encode($res2) . PHP_EOL;
        // >>> [null,null,null,null,null,"handlebars",null,null]

        $res3 = $r->topklist('bikes:keywords');
        echo json_encode($res3) . PHP_EOL;
        // >>> ["store","seat","pedals","tires","handles"]

        $res4 = $r->topkquery('bikes:keywords', 'store', 'handlebars');
        echo json_encode($res4) . PHP_EOL;
        // >>> [1,0]
```

##### Python

```python
"""
Code samples for Top-K pages:
    https://redis.io/docs/latest/develop/data-types/probabilistic/top-k/
"""

import redis

r = redis.Redis(decode_responses=True)


res1 = r.topk().reserve("bikes:keywords", 5, 2000, 7, 0.925)
print(res1)  # >>> True

res2 = r.topk().add(
    "bikes:keywords",
    "store",
    "seat",
    "handlebars",
    "handles",
    "pedals",
    "tires",
    "store",
    "seat",
)
print(res2)  # >>> [None, None, None, None, None, 'handlebars', None, None]

res3 = r.topk().list("bikes:keywords")
print(res3)  # >>> ['store', 'seat', 'pedals', 'tires', 'handles']

res4 = r.topk().query("bikes:keywords", "store", "handlebars")
print(res4)  # >>> [1, 0]

```



## Sizing

Choosing the size for a Top K sketch is relatively easy, because the only two parameters you need to set are a direct function of the number of elements (K) you want to keep in your list.

If you start by knowing your desired `k` you can easily derive the width and depth:

```
width = k*log(k)
depth =  log(k)  # but a minimum of 5
```

For the `decay_constant` you can use the value `0.9` which has been found as optimal in many cases, but you can experiment with different values and find what works best for your use case.

## Performance
Insertion in a top-k has time complexity of O(K + depth) ≈ O(K) and lookup has time complexity of O(K), where K is the number of top elements to be kept in the list and depth is the number of hash functions used.


## Academic sources
- [HeavyKeeper: An Accurate Algorithm for Finding Top-k Elephant Flows.](https://yangtonghome.github.io/uploads/HeavyKeeper_ToN.pdf)

## References
- [Meet Top-K: an Awesome Probabilistic Addition to Redis](https://redis.com/blog/meet-top-k-awesome-probabilistic-addition-redis/)

