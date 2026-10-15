# Count-min sketch

```json metadata
{
  "schema_version": 2,
  "title": "Count-min sketch",
  "description": "Count-min sketch is a probabilistic data structure that estimates the frequency of an element in a data stream.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"use-cases","title":"Use cases"},{"id":"examples","title":"Examples"},{"children":[{"id":"1-error","title":"1. Error"},{"id":"2-probability","title":"2. Probability"}],"id":"sizing","title":"Sizing"},{"id":"performance","title":"Performance"},{"id":"academic-sources","title":"Academic sources"},{"id":"references","title":"References"}]}

,
  "codeExamples": [{"codetabsId":"cms_tutorial-stepcms","commands":[{"acl_categories":["@write","@fast","@cms"],"complexity":"O(1)","name":"CMS.INITBYPROB"},{"acl_categories":["@write","@cms"],"complexity":"O(n)","name":"CMS.INCRBY"},{"acl_categories":["@read","@cms"],"complexity":"O(n)","name":"CMS.QUERY"},{"acl_categories":["@read","@fast","@cms"],"complexity":"O(1)","name":"CMS.INFO"}],"description":"Count-min sketch operations: Use CMS.INITBYPROB to create a sketch, CMS.INCRBY to increment element counts, CMS.QUERY to estimate frequencies, and CMS.INFO to inspect sketch properties when you need to estimate element frequencies in a data stream","difficulty":"intermediate","id":"cms","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_cms_tutorial-stepcms"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_cms_tutorial-stepcms"},{"id":"Node-js","panelId":"panel_Nodejs_cms_tutorial-stepcms"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_cms_tutorial-stepcms"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_cms_tutorial-stepcms"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_cms_tutorial-stepcms"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_cms_tutorial-stepcms"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_cms_tutorial-stepcms"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_cms_tutorial-stepcms"}]}]
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


### Count-min sketch command summary

**6 commands in this group:**

[View all cms commands](https://redis.io/commands/?group=cms)

| Command | Summary | Complexity | Since |
|---------|---------|------------|-------|
| [CMS.INCRBY](https://redis.io/commands/cms.incrby/) | Increases the count of one or more items by increment, which may be negative | O(n) where n is the number of items | 2.0.0 |
| [CMS.INFO](https://redis.io/commands/cms.info/) | Returns information about a sketch | O(1) | 2.0.0 |
| [CMS.INITBYDIM](https://redis.io/commands/cms.initbydim/) | Initializes a Count-Min Sketch to dimensions specified by user | O(1) | 2.0.0 |
| [CMS.INITBYPROB](https://redis.io/commands/cms.initbyprob/) | Initializes a Count-Min Sketch to accommodate requested tolerances. | O(1) | 2.0.0 |
| [CMS.MERGE](https://redis.io/commands/cms.merge/) | Merges several sketches into one sketch | O(n) where n is the number of sketches | 2.0.0 |
| [CMS.QUERY](https://redis.io/commands/cms.query/) | Returns the count for one or more items in a sketch | O(n) where n is the number of items | 2.0.0 |



Count-Min Sketch is a probabilistic data structure in Redis Open Source that can be used to estimate the frequency of events/elements in a stream of data.

It uses a sub-linear space at the expense of over-counting some events due to collisions. It consumes a stream of events/elements and keeps estimated counters of their frequency.

It is very important to know that the results coming from a Count-Min sketch lower than a certain threshold (determined by the error_rate) should be ignored and often even approximated to zero. So Count-Min sketch is indeed a data-structure for counting frequencies of elements in a stream, but it's only useful for higher counts. Very low counts should be ignored as noise.

## Use cases

**Products (retail, online shops)** 

This application answers this question: What was the sales volume (on a certain day) for a product? 

Use one Count-Min sketch created per day (period). Every product sale goes into the CMS. The CMS give reasonably accurate results for the products that contribute the most toward the sales. Products with low percentage of the total sales are ignored. 

## Examples
Assume you select an error rate of 0.1% (0.001) with a certainty of 99.8% (0.998). This means you have an error probability of 0.2% (0.002). Your sketch strives to keep the error within 0.1% of the total count of all elements you've added. There's a 0.2% chance the error might exceed this—like when an element below the threshold overlaps with one above it. When you add a few items to the CMS and evaluate their frequency, remember that in such a small sample, collisions are rare, as seen with other probabilistic data structures.

Count-min sketch operations: Use CMS.INITBYPROB to create a sketch, CMS.INCRBY to increment element counts, CMS.QUERY to estimate frequencies, and CMS.INFO to inspect sketch properties when you need to estimate element frequencies in a data stream

**Difficulty:** Intermediate

**Commands:** CMS.INITBYPROB, CMS.INCRBY, CMS.QUERY, CMS.INFO

**Complexity:**
- CMS.INITBYPROB: O(1)
- CMS.INCRBY: O(n)
- CMS.QUERY: O(n)
- CMS.INFO: O(1)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python

##### Redis CLI

```
> CMS.INITBYPROB bikes:profit 0.001 0.002
OK
> CMS.INCRBY bikes:profit "Smokey Mountain Striker" 100
1) (integer) 100
> CMS.INCRBY bikes:profit "Rocky Mountain Racer" 200 "Cloudy City Cruiser" 150
1) (integer) 200
2) (integer) 150
> CMS.QUERY bikes:profit "Smokey Mountain Striker" "Rocky Mountain Racer" "Cloudy City Cruiser" "Terrible Bike Name"
1) (integer) 100
2) (integer) 200
3) (integer) 150
4) (integer) 0
> CMS.INFO bikes:profit
1) width
2) (integer) 2000
3) depth
4) (integer) 9
5) count
6) (integer) 450
```

##### C#

```csharp
        bool res1 = db.CMS().InitByProb("bikes:profit", 0.001, 0.002);
        Console.WriteLine(res1);    // >>> True

        long res2 = db.CMS().IncrBy("bikes:profit", "Smoky Mountain Striker", 100);
        Console.WriteLine(res2);    // >>> 100

        long[] res3 = db.CMS().IncrBy("bikes:profit",
            [
                new("Rocky Mountain Racer", 200),
                new("Cloudy City Cruiser", 150)
            ]
        );
        Console.WriteLine(string.Join(", ", res3)); // >>> 200, 150

        long[] res4 = db.CMS().Query("bikes:profit", new RedisValue[] { "Smoky Mountain Striker" });
        Console.WriteLine(string.Join(", ", res4)); // >>> 100

        CmsInformation res5 = db.CMS().Info("bikes:profit");
        Console.WriteLine($"Width: {res5.Width}, Depth: {res5.Depth}, Count: {res5.Count}");
        // >>> Width: 2000, Depth: 9, Count: 450
```

##### Go

```go
	res1, err := rdb.CMSInitByProb(ctx, "bikes:profit", 0.001, 0.002).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // >>> OK

	res2, err := rdb.CMSIncrBy(ctx, "bikes:profit",
		"Smoky Mountain Striker", 100,
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2) // >>> [100]

	res3, err := rdb.CMSIncrBy(ctx, "bikes:profit",
		"Rocky Mountain Racer", 200,
		"Cloudy City Cruiser", 150,
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3) // >>> [200 150]

	res4, err := rdb.CMSQuery(ctx, "bikes:profit",
		"Smoky Mountain Striker",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4) // >>> [100]

	res5, err := rdb.CMSInfo(ctx, "bikes:profit").Result()

	if err != nil {
		panic(err)
	}

	fmt.Printf("Width: %v, Depth: %v, Count: %v",
		res5.Width, res5.Depth, res5.Count)
	// >>> Width: 2000, Depth: 9, Count: 450
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> cmsExample = asyncCommands
                    .cmsInitByProb("bikes:profit", 0.001, 0.002)
                    .thenCompose(res1 -> {
                        System.out.println(res1);
                        // >>> OK
                        return asyncCommands.cmsIncrBy("bikes:profit",
                                IncrementPair.of("Smoky Mountain Striker", 100L));
                    })
                    .thenCompose(res2 -> {
                        System.out.println(res2);
                        // >>> [100]
                        return asyncCommands.cmsIncrBy("bikes:profit",
                                IncrementPair.of("Rocky Mountain Racer", 200L),
                                IncrementPair.of("Cloudy City Cruiser", 150L));
                    })
                    .thenCompose(res3 -> {
                        System.out.println(res3);
                        // >>> [200, 150]
                        return asyncCommands.cmsQuery("bikes:profit", "Smoky Mountain Striker");
                    })
                    .thenCompose(res4 -> {
                        System.out.println(res4);
                        // >>> [100]
                        return asyncCommands.cmsInfo("bikes:profit");
                    })
                    .thenAccept(res5 -> {
                        System.out.println(res5.getWidth() + " " + res5.getDepth() + " " + res5.getCount());
                        // >>> 2000 9 450
                    })
                    .toCompletableFuture();

            cmsExample.join();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> cmsExample = reactiveCommands
                    .cmsInitByProb("bikes:profit", 0.001, 0.002)
                    .doOnNext(res1 -> {
                        System.out.println(res1);
                        // >>> OK
                    })
                    .thenMany(reactiveCommands.cmsIncrBy("bikes:profit",
                            IncrementPair.of("Smoky Mountain Striker", 100L)))
                    .collectList()
                    .doOnNext(res2 -> {
                        System.out.println(res2);
                        // >>> [100]
                    })
                    .thenMany(reactiveCommands.cmsIncrBy("bikes:profit",
                            IncrementPair.of("Rocky Mountain Racer", 200L),
                            IncrementPair.of("Cloudy City Cruiser", 150L)))
                    .collectList()
                    .doOnNext(res3 -> {
                        System.out.println(res3);
                        // >>> [200, 150]
                    })
                    .thenMany(reactiveCommands.cmsQuery("bikes:profit", "Smoky Mountain Striker"))
                    .collectList()
                    .doOnNext(res4 -> {
                        System.out.println(res4);
                        // >>> [100]
                    })
                    .then(reactiveCommands.cmsInfo("bikes:profit"))
                    .doOnNext(res5 -> {
                        System.out.println(res5.getWidth() + " " + res5.getDepth() + " " + res5.getCount());
                        // >>> 2000 9 450
                    })
                    .then();

            cmsExample.block();
```

##### Java (Synchronous - Jedis)

```java
    String res1 = jedis.cmsInitByProb("bikes:profit", 0.001d, 0.002d);
    System.out.println(res1); // >>> OK

    long res2 = jedis.cmsIncrBy("bikes:profit", "Smoky Mountain Striker", 100L);
    System.out.println(res2); // >>> 100

    List<Long> res3 = jedis.cmsIncrBy("bikes:profit", new HashMap<String, Long>() {{
      put("Rocky Mountain Racer", 200L);
      put("Cloudy City Cruiser", 150L);
    }});
    System.out.println(res3); // >>> [200, 150]

    List<Long> res4 = jedis.cmsQuery("bikes:profit", "Smoky Mountain Striker");
    System.out.println(res4); // >>> [100]

    Map<String, Object> res5 = jedis.cmsInfo("bikes:profit");
    System.out.println(res5.get("width") + " " + res5.get("depth") + " " + res5.get("count")); // >>> 2000 9 450
```

##### JavaScript (Node.js)

```javascript
const res1 = await client.cms.initByProb('bikes:profit', 0.001, 0.002);
console.log(res1);  // >>> OK

const res2 = await client.cms.incrBy('bikes:profit', {
    item: 'Smoky Mountain Striker',
    incrementBy: 100
});
console.log(res2);  // >>> [100]

const res3 = await client.cms.incrBy('bikes:profit', [
  {
    item: 'Rocky Mountain Racer',
    incrementBy: 200
  },
  {
    item: 'Cloudy City Cruiser',
    incrementBy: 150
  }
]);
console.log(res3);  // >>> [200, 150]

const res4 = await client.cms.query('bikes:profit', 'Smoky Mountain Striker');
console.log(res4);  // >>> [100]

const res5 = await client.cms.info('bikes:profit');
console.log(res5.width, res5.depth, res5.count);  // >>> 2000 9 450
```

##### PHP

```php
        $res1 = $r->cmsinitbyprob('bikes:profit', 0.001, 0.002);
        echo $res1 . PHP_EOL;
        // >>> OK

        $res2 = $r->cmsincrby('bikes:profit', 'Smoky Mountain Striker', 100);
        echo json_encode($res2) . PHP_EOL;
        // >>> [100]

        $res3 = $r->cmsincrby(
            'bikes:profit',
            'Rocky Mountain Racer', 200,
            'Cloudy City Cruiser', 150
        );
        echo json_encode($res3) . PHP_EOL;
        // >>> [200,150]

        $res4 = $r->cmsquery('bikes:profit', 'Smoky Mountain Striker');
        echo json_encode($res4) . PHP_EOL;
        // >>> [100]

        $res5 = $r->cmsinfo('bikes:profit');
        echo $res5['width'] . ' ' . $res5['depth'] . ' ' . $res5['count'] . PHP_EOL;
        // >>> 2000 9 450
```

##### Python

```python
res1 = r.cms().initbyprob("bikes:profit", 0.001, 0.002)
print(res1)  # >>> True

res2 = r.cms().incrby("bikes:profit", ["Smoky Mountain Striker"], [100])
print(res2)  # >>> [100]

res3 = r.cms().incrby(
    "bikes:profit", ["Rocky Mountain Racer", "Cloudy City Cruiser"], [200, 150]
)
print(res3)  # >>> [200, 150]

res4 = r.cms().query("bikes:profit", "Smoky Mountain Striker")
print(res4)  # >>> [100]

res5 = r.cms().info("bikes:profit")
print(res5.width, res5.depth, res5.count)  # >>> 2000 9 450
```



##### Example 1:
If we had a uniform distribution of 1000 elements where each has a count of around 500 the threshold would be 500: 

```
threshold = error * total_count  = 0.001 * (1000*500) = 500
```

This shows that a CMS is maybe not the best data structure to count frequency of a uniformly distributed stream.
Let's try decreasing the error to 0.01%:

```
threshold = error * total_count  = 0.0001 * (1000*500) = 100
```
This threshold looks more acceptable already, but it means we will need a bigger sketch width `w = 2/error = 20 000` and consequently - more memory.

##### Example 2:
In another example let's imagine a normal (gaussian) distribution where we have 1000 elements, out of which 800 will have a summed count of 400K (with an average count of 500) and 200 elements will have a much higher summed count of 1.6M (with an average count of 8000), making them the heavy hitters (elephant flow). The threshold after "populating" the sketch with all the 1000 elements would be:

```
threshold = error * total_count = 0.001 * 2M = 2000
```

This threshold seems to be sitting comfortably between the 2 average counts 500 and 8000 so the initial chosen error rate should be working well for this case.


## Sizing

Even though the Count-Min sketch is similar to Bloom filter in many ways, its sizing is considerably more complex. The initialisation command receives only two sizing parameters, but you have to understand them thoroughly if you want to have a usable sketch.

```
CMS.INITBYPROB key error probability
```

### 1. Error

The `error` parameter will determine the width `w` of your sketch and the probability will determine the number of hash functions (depth `d`). The error rate we choose will determine the threshold above which we can trust the result from the sketch. The correlation is:
```
threshold = error * total_count 
```
or
```
error = threshold/total_count
```

where `total_count` is the sum of the count of all elements that can be obtained from the `count` key of the result of the [`CMS.INFO`](https://redis.io/docs/latest/commands/cms.info) command and is of course dynamic - it changes with every new increment in the sketch. At creation time you can approximate the `total_count` ratio as a product of the average count you'll be expecting in the sketch and the average number of elements.

Since the threshold is a function of the total count in the filter it's very important to note that it will grow as  the count grows, but knowing the total count we can always dynamically calculate the threshold. If a result is below it - it can be discarded.

  
### 2. Probability
  
`probability` in this data structure represents the chance of an element that has a count below the threshold to collide with elements that had a count above the threshold on all sketches/depths thus returning a min-count of a frequently occurring element instead of its own.



## Performance
Adding, updating and querying for elements in a CMS has a time complexity O(1).


## Academic sources
- [An Improved Data Stream Summary: The Count-Min Sketch and its Applications](http://dimacs.rutgers.edu/~graham/pubs/papers/cm-full.pdf)

## References
- [Count-Min Sketch: The Art and Science of Estimating Stuff](https://redis.com/blog/count-min-sketch-the-art-and-science-of-estimating-stuff/)

