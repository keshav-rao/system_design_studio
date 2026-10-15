# t-digest

```json metadata
{
  "schema_version": 2,
  "title": "t-digest",
  "description": "t-digest is a probabilistic data structure that allows you to estimate the percentile of a data stream.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"what-is-t-digest","title":"What is t-digest?"},{"id":"use-cases","title":"Use cases"},{"id":"examples","title":"Examples"},{"id":"academic-sources","title":"Academic sources"},{"id":"references","title":"References"}]}

,
  "codeExamples": [{"codetabsId":"tdigest_tutorial-steptdig_start","commands":[{"acl_categories":["@write","@fast","@tdigest"],"complexity":"O(1)","name":"TDIGEST.CREATE"},{"acl_categories":["@write","@tdigest"],"complexity":"O(N)","name":"TDIGEST.ADD"}],"description":"t-digest creation and data addition: Use TDIGEST.CREATE to initialize a sketch and TDIGEST.ADD to insert values when you need to build a percentile estimation data structure","difficulty":"beginner","id":"tdig_start","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_tdigest_tutorial-steptdig_start"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_tdigest_tutorial-steptdig_start"},{"id":"Node-js","panelId":"panel_Nodejs_tdigest_tutorial-steptdig_start"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_tdigest_tutorial-steptdig_start"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_tdigest_tutorial-steptdig_start"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_tdigest_tutorial-steptdig_start"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_tdigest_tutorial-steptdig_start"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_tdigest_tutorial-steptdig_start"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_tdigest_tutorial-steptdig_start"}]},{"buildsUpon":["tdig_start"],"codetabsId":"tdigest_tutorial-steptdig_cdf","commands":[{"acl_categories":["@write","@fast","@tdigest"],"complexity":"O(1)","name":"TDIGEST.CREATE"},{"acl_categories":["@write","@tdigest"],"complexity":"O(N)","name":"TDIGEST.ADD"},{"acl_categories":["@read","@fast","@tdigest"],"complexity":"O(N)","name":"TDIGEST.CDF"},{"acl_categories":["@read","@fast","@tdigest"],"complexity":"O(N)","name":"TDIGEST.RANK"}],"description":"Percentile rank estimation: Use TDIGEST.CDF to estimate the fraction of values below a threshold and TDIGEST.RANK to estimate the rank of values when you need to determine percentile positions","difficulty":"intermediate","id":"tdig_cdf","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_tdigest_tutorial-steptdig_cdf"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_tdigest_tutorial-steptdig_cdf"},{"id":"Node-js","panelId":"panel_Nodejs_tdigest_tutorial-steptdig_cdf"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_tdigest_tutorial-steptdig_cdf"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_tdigest_tutorial-steptdig_cdf"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_tdigest_tutorial-steptdig_cdf"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_tdigest_tutorial-steptdig_cdf"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_tdigest_tutorial-steptdig_cdf"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_tdigest_tutorial-steptdig_cdf"}]},{"buildsUpon":["tdig_cdf"],"codetabsId":"tdigest_tutorial-steptdig_quant","commands":[{"acl_categories":["@read","@fast","@tdigest"],"complexity":"O(N)","name":"TDIGEST.QUANTILE"},{"acl_categories":["@read","@fast","@tdigest"],"complexity":"O(N)","name":"TDIGEST.BYRANK"}],"description":"Quantile and rank value estimation: Use TDIGEST.QUANTILE to find values at specific percentiles and TDIGEST.BYRANK to find values by rank when you need to retrieve percentile values from a sketch","difficulty":"intermediate","id":"tdig_quant","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_tdigest_tutorial-steptdig_quant"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_tdigest_tutorial-steptdig_quant"},{"id":"Node-js","panelId":"panel_Nodejs_tdigest_tutorial-steptdig_quant"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_tdigest_tutorial-steptdig_quant"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_tdigest_tutorial-steptdig_quant"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_tdigest_tutorial-steptdig_quant"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_tdigest_tutorial-steptdig_quant"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_tdigest_tutorial-steptdig_quant"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_tdigest_tutorial-steptdig_quant"}]},{"buildsUpon":["tdig_cdf"],"codetabsId":"tdigest_tutorial-steptdig_min","commands":[{"acl_categories":["@read","@fast","@tdigest"],"complexity":"O(1)","name":"TDIGEST.MIN"},{"acl_categories":["@read","@fast","@tdigest"],"complexity":"O(1)","name":"TDIGEST.MAX"}],"description":"Sketch metadata retrieval: Use TDIGEST.MIN and TDIGEST.MAX to retrieve the minimum and maximum values in a sketch when you need to inspect the bounds of your data","difficulty":"beginner","id":"tdig_min","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_tdigest_tutorial-steptdig_min"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_tdigest_tutorial-steptdig_min"},{"id":"Node-js","panelId":"panel_Nodejs_tdigest_tutorial-steptdig_min"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_tdigest_tutorial-steptdig_min"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_tdigest_tutorial-steptdig_min"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_tdigest_tutorial-steptdig_min"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_tdigest_tutorial-steptdig_min"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_tdigest_tutorial-steptdig_min"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_tdigest_tutorial-steptdig_min"}]},{"buildsUpon":["tdig_cdf"],"codetabsId":"tdigest_tutorial-steptdig_reset","commands":[{"acl_categories":["@write","@fast","@tdigest"],"complexity":"O(1)","name":"TDIGEST.RESET"}],"description":"Sketch reset: Use TDIGEST.RESET to clear all data from a sketch when you need to reuse a sketch for new data","difficulty":"beginner","id":"tdig_reset","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_tdigest_tutorial-steptdig_reset"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_tdigest_tutorial-steptdig_reset"},{"id":"Node-js","panelId":"panel_Nodejs_tdigest_tutorial-steptdig_reset"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_tdigest_tutorial-steptdig_reset"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_tdigest_tutorial-steptdig_reset"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_tdigest_tutorial-steptdig_reset"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_tdigest_tutorial-steptdig_reset"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_tdigest_tutorial-steptdig_reset"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_tdigest_tutorial-steptdig_reset"}]}]
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


### t-digest command summary

**14 commands in this group:**

[View all tdigest commands](https://redis.io/commands/?group=tdigest)

| Command | Summary | Complexity | Since |
|---------|---------|------------|-------|
| [TDIGEST.ADD](https://redis.io/commands/tdigest.add/) | Adds one or more observations to a t-digest sketch | O(N), where N is the number of samples to add | 2.4.0 |
| [TDIGEST.BYRANK](https://redis.io/commands/tdigest.byrank/) | Returns, for each input rank, an estimation of the value (floating-point) with that rank | O(N) where N is the number of ranks specified | 2.4.0 |
| [TDIGEST.BYREVRANK](https://redis.io/commands/tdigest.byrevrank/) | Returns, for each input reverse rank, an estimation of the value (floating-point) with that reverse rank | O(N) where N is the number of reverse ranks spe... | 2.4.0 |
| [TDIGEST.CDF](https://redis.io/commands/tdigest.cdf/) | Returns, for each input value, an estimation of the floating-point fraction of (observations smaller than the given value + half the observations equal to the given value). Multiple fractions can be retrieved in a single call. | O(N) where N is the number of values specified. | 2.4.0 |
| [TDIGEST.CREATE](https://redis.io/commands/tdigest.create/) | Allocates memory and initializes a new t-digest sketch | O(1) | 2.4.0 |
| [TDIGEST.INFO](https://redis.io/commands/tdigest.info/) | Returns information and statistics about a t-digest sketch | O(1) | 2.4.0 |
| [TDIGEST.MAX](https://redis.io/commands/tdigest.max/) | Returns the maximum observation value from a t-digest sketch | O(1) | 2.4.0 |
| [TDIGEST.MERGE](https://redis.io/commands/tdigest.merge/) | Merges multiple t-digest sketches into a single sketch | O(N*K), where N is the number of centroids and ... | 2.4.0 |
| [TDIGEST.MIN](https://redis.io/commands/tdigest.min/) | Returns the minimum observation value from a t-digest sketch | O(1) | 2.4.0 |
| [TDIGEST.QUANTILE](https://redis.io/commands/tdigest.quantile/) | Returns, for each input fraction, an estimation of the value (floating point) that is smaller than the given fraction of observations | O(N) where N is the number of quantiles specified. | 2.4.0 |

#### t-digest command summary (part 2)

| Command | Summary | Complexity | Since |
|---------|---------|------------|-------|
| [TDIGEST.RANK](https://redis.io/commands/tdigest.rank/) | Returns, for each input value (floating-point), the estimated rank of the value (the number of observations in the sketch that are smaller than the value + half the number of observations that are equal to the value) | O(N) where N is the number of values specified. | 2.4.0 |
| [TDIGEST.RESET](https://redis.io/commands/tdigest.reset/) | Resets a t-digest sketch: empty the sketch and re-initializes it. | O(1) | 2.4.0 |
| [TDIGEST.REVRANK](https://redis.io/commands/tdigest.revrank/) | Returns, for each input value (floating-point), the estimated reverse rank of the value (the number of observations in the sketch that are larger than the value + half the number of observations that are equal to the value) | O(N) where N is the number of values specified. | 2.4.0 |
| [TDIGEST.TRIMMED_MEAN](https://redis.io/commands/tdigest.trimmed_mean/) | Returns an estimation of the mean value from the sketch, excluding observation values outside the low and high cutoff quantiles | O(N) where N is the number of centroids | 2.4.0 |



The t-digest is a sketch data structure in Redis Open Source for estimating percentiles from a data stream or a large dataset using a compact sketch.

It can answer questions like:
- Which fraction of the values in the data stream are smaller than a given value?
- How many values in the data stream are smaller than a given value?
- What's the highest value that's smaller than *p* percent of the values in the data stream? (what is the p-percentile value)?


## What is t-digest?

t-digest is a data structure that will estimate a percentile point without having to store and order all the data points in a set. For example: to answer the question "What's the average latency for 99% of my database operations" we would have to store the average latency for every user, order the values, cut out the last 1% and only then find the average value of all the rest. This kind of process is costly not just in terms of the processing needed to order those values but also in terms of the space needed to store them. Those are precisely the problems t-digest solves.

t-digest can also be used to estimate other values related to percentiles, like trimmed means.   

> A **trimmed mean** is the mean value from the sketch, excluding observation values outside the low and high cutoff percentiles. For example, a 0.1 trimmed mean is the mean value of the sketch, excluding the lowest 10% and the highest 10% of the values.

## Use cases

**Hardware/software monitoring**

You measure your online server response latency, and you like to query:

- What are the 50th, 90th, and 99th percentiles of the measured latencies?

- Which fraction of the measured latencies are less than 25 milliseconds?

- What is the mean latency, ignoring outliers? or What is the mean latency between the 10th and the 90th percentile?

**Online gaming**

Millions of people are playing a game on your online gaming platform, and you want to give the following information to each player?

- Your score is better than x percent of the game sessions played.

- There were about y game sessions where people scored larger than you.

- To have a better score than 90% of the games played, your score should be z.

**Network traffic monitoring**

You measure the IP packets transferred over your network each second and try to detect denial-of-service attacks by asking:

- Does the number of packets in the last second exceed 99% of previously observed values?

- How many packets do I expect to see under _normal_ network conditions? 
(Answer: between x and y, where x represents the 1st percentile and y represents the 99th percentile).

**Predictive maintenance**

- Was the measured parameter (noise level, current consumption, etc.) irregular? (not within the [1st percentile...99th percentile] range)?

- To which values should I set my alerts?


## Examples

In the following example, you'll create a t-digest with a compression of 100 and add items to it. The `COMPRESSION` argument is used to specify the tradeoff between accuracy and memory consumption. The default value is 100. Higher values mean more accuracy. Note: unlike some of the other probabilistic data structures, the [`TDIGEST.ADD`](https://redis.io/docs/latest/commands/tdigest.add) command will not create a new structure if the key does not exist.

t-digest creation and data addition: Use TDIGEST.CREATE to initialize a sketch and TDIGEST.ADD to insert values when you need to build a percentile estimation data structure

**Commands:** TDIGEST.CREATE, TDIGEST.ADD

**Complexity:**
- TDIGEST.CREATE: O(1)
- TDIGEST.ADD: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python

##### Redis CLI

```
> TDIGEST.CREATE bikes:sales COMPRESSION 100
OK
> TDIGEST.ADD bikes:sales 21
OK
> TDIGEST.ADD bikes:sales 150 95 75 34
OK
```

##### C#

```csharp
        bool res1 = db.TDIGEST().Create("bikes:sales", 100);
        Console.WriteLine(res1);    // >>> True

        bool res2 = db.TDIGEST().Add("bikes:sales", 21);
        Console.WriteLine(res2);    // >>> True

        bool res3 = db.TDIGEST().Add("bikes:sales", 150, 95, 75, 34);
        Console.WriteLine(res3);    // >>> true
```

##### Go

```go
	res1, err := rdb.TDigestCreate(ctx, "bikes:sales").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // >>> OK

	res2, err := rdb.TDigestAdd(ctx, "bikes:sales", 21).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2) // >>> OK

	res3, err := rdb.TDigestAdd(ctx, "bikes:sales",
		150, 95, 75, 34,
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3) // >>> OK

```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> tdigStartExample = asyncCommands
                    .tdigestCreate("bikes:sales", 100L)
                    .thenCompose(res1 -> {
                        System.out.println(res1);
                        // >>> OK
                        return asyncCommands.tdigestAdd("bikes:sales", 21);
                    })
                    .thenCompose(res2 -> {
                        System.out.println(res2);
                        // >>> OK
                        return asyncCommands.tdigestAdd("bikes:sales", 150, 95, 75, 34);
                    })
                    .thenAccept(res3 -> {
                        System.out.println(res3);
                        // >>> OK
                    })
                    .toCompletableFuture();

            tdigStartExample.join();
```

##### Java (Reactive - Lettuce)

```java
            String res1 = reactiveCommands.tdigestCreate("bikes:sales", 100L).block();
            System.out.println(res1);
            // >>> OK

            String res2 = reactiveCommands.tdigestAdd("bikes:sales", 21).block();
            System.out.println(res2);
            // >>> OK

            String res3 = reactiveCommands.tdigestAdd("bikes:sales", 150, 95, 75, 34).block();
            System.out.println(res3);
            // >>> OK
```

##### Java (Synchronous - Jedis)

```java
        String res1 = jedis.tdigestCreate("bikes:sales", 100);
        System.out.println(res1); // >>> True

        String res2 = jedis.tdigestAdd("bikes:sales", 21);
        System.out.println(res2); // >>> OK

        String res3 = jedis.tdigestAdd("bikes:sales", 150, 95, 75, 34);
        System.out.println(res3); // >>> OK
```

##### JavaScript (Node.js)

```javascript
const res1 = await client.tDigest.create('bikes:sales', 100);
console.log(res1);  // >>> OK

const res2 = await client.tDigest.add('bikes:sales', [21]);
console.log(res2);  // >>> OK

const res3 = await client.tDigest.add('bikes:sales', [150, 95, 75, 34]);
console.log(res3);  // >>> OK
```

##### PHP

```php
        $res1 = $r->tdigestcreate('bikes:sales', 100);
        echo $res1 . PHP_EOL;
        // >>> OK

        $res2 = $r->tdigestadd('bikes:sales', 21);
        echo $res2 . PHP_EOL;
        // >>> OK

        $res3 = $r->tdigestadd('bikes:sales', 150, 95, 75, 34);
        echo $res3 . PHP_EOL;
        // >>> OK
```

##### Python

```python
res1 = r.tdigest().create("bikes:sales", 100)
print(res1)  # >>> True

res2 = r.tdigest().add("bikes:sales", [21])
print(res2)  # >>> OK

res3 = r.tdigest().add("bikes:sales", [150, 95, 75, 34])
print(res3)  # >>> OK
```




You can repeat calling [TDIGEST.ADD](https://redis.io/docs/latest/commands/tdigest.add) whenever new observations are available

#### Estimating fractions or ranks by values

Another helpful feature in t-digest is CDF (definition of rank) which gives us the fraction of observations smaller or equal to a certain value. This command is very useful to answer questions like "*What's the percentage of observations with a value lower or equal to X*".

>More precisely, [`TDIGEST.CDF`](https://redis.io/docs/latest/commands/tdigest.cdf) will return the estimated fraction of observations in the sketch that are smaller than X plus half the number of observations that are equal to X. We can also use the [`TDIGEST.RANK`](https://redis.io/docs/latest/commands/tdigest.rank) command, which is very similar. Instead of returning a fraction, it returns the ----estimated---- rank of a value. The [`TDIGEST.RANK`](https://redis.io/docs/latest/commands/tdigest.rank) command is also variadic, meaning you can use a single command to retrieve estimations for one or more values.

Here's an example. Given a set of biker's ages, you can ask a question like "What's the percentage of bike racers that are younger than 50 years?"

Percentile rank estimation: Use TDIGEST.CDF to estimate the fraction of values below a threshold and TDIGEST.RANK to estimate the rank of values when you need to determine percentile positions

**Difficulty:** Intermediate

**Builds upon:** tdig_start

**Commands:** TDIGEST.CREATE, TDIGEST.ADD, TDIGEST.CDF, TDIGEST.RANK

**Complexity:**
- TDIGEST.CREATE: O(1)
- TDIGEST.ADD: O(N)
- TDIGEST.CDF: O(N)
- TDIGEST.RANK: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python

##### Redis CLI

```
> TDIGEST.CREATE racer_ages
OK
> TDIGEST.ADD racer_ages 45.88 44.2 58.03 19.76 39.84 69.28 50.97 25.41 19.27 85.71 42.63
OK
> TDIGEST.CDF racer_ages 50
1) "0.6363636363636364"
> TDIGEST.RANK racer_ages 50
1) (integer) 7
> TDIGEST.RANK racer_ages 50 40
1) (integer) 7
2) (integer) 4
```

##### C#

```csharp
        bool res4 = db.TDIGEST().Create("racer_ages");
        Console.WriteLine(res4);    // >>> True

        bool res5 = db.TDIGEST().Add("racer_ages",
            45.88,
            44.2,
            58.03,
            19.76,
            39.84,
            69.28,
            50.97,
            25.41,
            19.27,
            85.71,
            42.63
        );
        Console.WriteLine(res5);    // >>> True

        long[] res6 = db.TDIGEST().Rank("racer_ages", 50);
        Console.WriteLine(string.Join(", ", res6)); // >>> 7

        long[] res7 = db.TDIGEST().Rank("racer_ages", 50, 40);
        Console.WriteLine(string.Join(", ", res7)); // >>> 7, 4
```

##### Go

```go
	res4, err := rdb.TDigestCreate(ctx, "racer_ages").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4) // >>> OK

	res5, err := rdb.TDigestAdd(ctx, "racer_ages",
		45.88, 44.2, 58.03, 19.76, 39.84, 69.28,
		50.97, 25.41, 19.27, 85.71, 42.63,
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res5) // >>> OK

	res6, err := rdb.TDigestRank(ctx, "racer_ages", 50).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res6) // >>> [7]

	res7, err := rdb.TDigestRank(ctx, "racer_ages", 50, 40).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res7) // >>> [7 4]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> tdigCdfExample = asyncCommands
                    .tdigestCreate("racer_ages")
                    .thenCompose(res4 -> {
                        System.out.println(res4);
                        // >>> OK
                        return asyncCommands.tdigestAdd("racer_ages",
                                45.88, 44.2, 58.03, 19.76, 39.84, 69.28,
                                50.97, 25.41, 19.27, 85.71, 42.63);
                    })
                    .thenCompose(res5 -> {
                        System.out.println(res5);
                        // >>> OK
                        return asyncCommands.tdigestRank("racer_ages", 50);
                    })
                    .thenCompose(res6 -> {
                        System.out.println(res6);
                        // >>> [7]
                        return asyncCommands.tdigestRank("racer_ages", 50, 40);
                    })
                    .thenAccept(res7 -> {
                        System.out.println(res7);
                        // >>> [7, 4]
                    })
                    .toCompletableFuture();

            tdigCdfExample.join();
```

##### Java (Reactive - Lettuce)

```java
            String res4 = reactiveCommands.tdigestCreate("racer_ages").block();
            System.out.println(res4);
            // >>> OK

            String res5 = reactiveCommands.tdigestAdd("racer_ages",
                    45.88, 44.2, 58.03, 19.76, 39.84, 69.28,
                    50.97, 25.41, 19.27, 85.71, 42.63).block();
            System.out.println(res5);
            // >>> OK

            List<Long> res6 = reactiveCommands.tdigestRank("racer_ages", 50).collectList().block();
            System.out.println(res6);
            // >>> [7]

            List<Long> res7 = reactiveCommands.tdigestRank("racer_ages", 50, 40).collectList().block();
            System.out.println(res7);
            // >>> [7, 4]
```

##### Java (Synchronous - Jedis)

```java
        String res4 = jedis.tdigestCreate("racer_ages");
        System.out.println(res4); // >>> True

        String res5 = jedis.tdigestAdd("racer_ages", 45.88,
                44.2,
                58.03,
                19.76,
                39.84,
                69.28,
                50.97,
                25.41,
                19.27,
                85.71,
                42.63);
        System.out.println(res5); // >>> OK

        List<Long> res6 = jedis.tdigestRank("racer_ages", 50);
        System.out.println(res6); // >>> [7]

        List<Long> res7 = jedis.tdigestRank("racer_ages", 50, 40);
        System.out.println(res7); // >>> [7, 4]
```

##### JavaScript (Node.js)

```javascript
const res4 = await client.tDigest.create('racer_ages');
console.log(res4);  // >>> OK

const res5 = await client.tDigest.add('racer_ages', [
  45.88, 44.2, 58.03, 19.76, 39.84, 69.28, 50.97, 25.41, 19.27, 85.71, 42.63
]);
console.log(res5);  // >>> OK

const res6 = await client.tDigest.rank('racer_ages', [50]);
console.log(res6);  // >>> [7]

const res7 = await client.tDigest.rank('racer_ages', [50, 40]);
console.log(res7);  // >>> [7, 4]
```

##### PHP

```php
        $res4 = $r->tdigestcreate('racer_ages');
        echo $res4 . PHP_EOL;
        // >>> OK

        $res5 = $r->tdigestadd(
            'racer_ages',
            45.88,
            44.2,
            58.03,
            19.76,
            39.84,
            69.28,
            50.97,
            25.41,
            19.27,
            85.71,
            42.63
        );
        echo $res5 . PHP_EOL;
        // >>> OK

        $res6 = $r->tdigestrank('racer_ages', 50);
        echo json_encode($res6) . PHP_EOL;
        // >>> [7]

        $res7 = $r->tdigestrank('racer_ages', 50, 40);
        echo json_encode($res7) . PHP_EOL;
        // >>> [7,4]
```

##### Python

```python
res4 = r.tdigest().create("racer_ages")
print(res4)  # >>> True

res5 = r.tdigest().add(
    "racer_ages",
    [
        45.88,
        44.2,
        58.03,
        19.76,
        39.84,
        69.28,
        50.97,
        25.41,
        19.27,
        85.71,
        42.63,
    ],
)
print(res5)  # >>> OK

res6 = r.tdigest().rank("racer_ages", 50)
print(res6)  # >>> [7]

res7 = r.tdigest().rank("racer_ages", 50, 40)
print(res7)  # >>> [7, 4]
```




And lastly, `TDIGEST.REVRANK key value...` is similar to [TDIGEST.RANK](https://redis.io/docs/latest/commands/tdigest.rank), but returns, for each input value, an estimation of the number of (observations larger than a given value + half the observations equal to the given value).


#### Estimating values by fractions or ranks

`TDIGEST.QUANTILE key fraction...` returns, for each input fraction, an estimation of the value (floating point) that is smaller than the given fraction of observations. `TDIGEST.BYRANK key rank...` returns, for each input rank, an estimation of the value (floating point) with that rank.

Quantile and rank value estimation: Use TDIGEST.QUANTILE to find values at specific percentiles and TDIGEST.BYRANK to find values by rank when you need to retrieve percentile values from a sketch

**Difficulty:** Intermediate

**Builds upon:** tdig_cdf

**Commands:** TDIGEST.QUANTILE, TDIGEST.BYRANK

**Complexity:**
- TDIGEST.QUANTILE: O(N)
- TDIGEST.BYRANK: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python

##### Redis CLI

```
> TDIGEST.QUANTILE racer_ages .5
1) "44.2"
> TDIGEST.BYRANK racer_ages 4
1) "42.63"
```

##### C#

```csharp
        double[] res8 = db.TDIGEST().Quantile("racer_ages", 0.5); ;
        Console.WriteLine(string.Join(", ", res8)); // >>> 44.2

        double[] res9 = db.TDIGEST().ByRank("racer_ages", 4);
        Console.WriteLine(string.Join(", ", res9)); // >>> 42.63
```

##### Go

```go
	res8, err := rdb.TDigestQuantile(ctx, "racer_ages", 0.5).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res8) // >>> [44.2]

	res9, err := rdb.TDigestByRank(ctx, "racer_ages", 4).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res9) // >>> [42.63]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> tdigQuantExample = asyncCommands
                    .tdigestQuantile("racer_ages", 0.5)
                    .thenCompose(res8 -> {
                        System.out.println(res8);
                        // >>> [44.2]
                        return asyncCommands.tdigestByRank("racer_ages", 4L);
                    })
                    .thenAccept(res9 -> {
                        System.out.println(res9);
                        // >>> [42.63]
                    })
                    .toCompletableFuture();

            tdigQuantExample.join();
```

##### Java (Reactive - Lettuce)

```java
            List<Double> res8 = reactiveCommands.tdigestQuantile("racer_ages", 0.5).collectList().block();
            System.out.println(res8);
            // >>> [44.2]

            List<Double> res9 = reactiveCommands.tdigestByRank("racer_ages", 4L).collectList().block();
            System.out.println(res9);
            // >>> [42.63]
```

##### Java (Synchronous - Jedis)

```java
        List<Double> res8 = jedis.tdigestQuantile("racer_ages", 0.5);
        System.out.println(res8); // >>> [44.2]

        List<Double> res9 = jedis.tdigestByRank("racer_ages", 4);
        System.out.println(res9); // >>> [42.63]
```

##### JavaScript (Node.js)

```javascript
const res8 = await client.tDigest.quantile('racer_ages', [0.5]);
console.log(res8);  // >>> [44.2]

const res9 = await client.tDigest.byRank('racer_ages', [4]);
console.log(res9);  // >>> [42.63]
```

##### PHP

```php
        $res8 = $r->tdigestquantile('racer_ages', 0.5);
        echo json_encode($res8) . PHP_EOL;
        // >>> ["44.2"]

        $res9 = $r->tdigestbyrank('racer_ages', 4);
        echo json_encode($res9) . PHP_EOL;
        // >>> ["42.63"]
```

##### Python

```python
res8 = r.tdigest().quantile("racer_ages", 0.5)
print(res8)  # >>> [44.2]

res9 = r.tdigest().byrank("racer_ages", 4)
print(res9)  # >>> [42.63]
```



`TDIGEST.BYREVRANK key rank...` returns, for each input **reverse rank**, an estimation of the **value** (floating point) with that reverse rank.

#### Estimating trimmed mean

Use `TDIGEST.TRIMMED_MEAN key lowFraction highFraction` to retrieve an estimation of the mean value between the specified fractions.

This is especially useful for calculating the average value ignoring outliers. For example - calculating the average value between the 20th percentile and the 80th percentile.

#### Merging sketches

Sometimes it is useful to merge sketches. For example, suppose we measure latencies for 3 servers, and we want to calculate the 90%, 95%, and 99% latencies for all the servers combined.

`TDIGEST.MERGE destKey numKeys sourceKey... [COMPRESSION compression] [OVERRIDE]` merges multiple sketches into a single sketch.

If `destKey` does not exist - a new sketch is created.

If `destKey` is an existing sketch, its values are merged with the values of the source keys. To override the destination key contents, use `OVERRIDE`.

#### Retrieving sketch information

Use [`TDIGEST.MIN`](https://redis.io/docs/latest/commands/tdigest.min) and [`TDIGEST.MAX`](https://redis.io/docs/latest/commands/tdigest.max) to retrieve the minimal and maximal values in the sketch, respectively.

Sketch metadata retrieval: Use TDIGEST.MIN and TDIGEST.MAX to retrieve the minimum and maximum values in a sketch when you need to inspect the bounds of your data

**Builds upon:** tdig_cdf

**Commands:** TDIGEST.MIN, TDIGEST.MAX

**Complexity:**
- TDIGEST.MIN: O(1)
- TDIGEST.MAX: O(1)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python

##### Redis CLI

```
> TDIGEST.MIN racer_ages
"19.27"
> TDIGEST.MAX racer_ages
"85.71"
```

##### C#

```csharp
        double res10 = db.TDIGEST().Min("racer_ages");
        Console.WriteLine(res10);   // >>> 19.27

        double res11 = db.TDIGEST().Max("racer_ages");
        Console.WriteLine(res11);   // >>> 85.71
```

##### Go

```go
	res10, err := rdb.TDigestMin(ctx, "racer_ages").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res10) // >>> 19.27

	res11, err := rdb.TDigestMax(ctx, "racer_ages").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res11) // >>> 85.71
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> tdigMinExample = asyncCommands
                    .tdigestMin("racer_ages")
                    .thenCompose(res10 -> {
                        System.out.println(res10);
                        // >>> 19.27
                        return asyncCommands.tdigestMax("racer_ages");
                    })
                    .thenAccept(res11 -> {
                        System.out.println(res11);
                        // >>> 85.71
                    })
                    .toCompletableFuture();

            tdigMinExample.join();
```

##### Java (Reactive - Lettuce)

```java
            Double res10 = reactiveCommands.tdigestMin("racer_ages").block();
            System.out.println(res10);
            // >>> 19.27

            Double res11 = reactiveCommands.tdigestMax("racer_ages").block();
            System.out.println(res11);
            // >>> 85.71
```

##### Java (Synchronous - Jedis)

```java
        double res10 = jedis.tdigestMin("racer_ages");
        System.out.println(res10); // >>> 19.27

        double res11 = jedis.tdigestMax("racer_ages");
        System.out.println(res11); // >>> 85.71
```

##### JavaScript (Node.js)

```javascript
const res10 = await client.tDigest.min('racer_ages');
console.log(res10);  // >>> 19.27

const res11 = await client.tDigest.max('racer_ages');
console.log(res11);  // >>> 85.71
```

##### PHP

```php
        $res10 = $r->tdigestmin('racer_ages');
        echo $res10 . PHP_EOL;
        // >>> 19.27

        $res11 = $r->tdigestmax('racer_ages');
        echo $res11 . PHP_EOL;
        // >>> 85.71
```

##### Python

```python
res10 = r.tdigest().min("racer_ages")
print(res10)  # >>> 19.27

res11 = r.tdigest().max("racer_ages")
print(res11)  # >>> 85.71
```



Both return `nan` when the sketch is empty.

Both commands return accurate results and are equivalent to `TDIGEST.BYRANK racer_ages 0` and `TDIGEST.BYREVRANK racer_ages 0`, respectively.

Use `TDIGEST.INFO racer_ages` to retrieve some additional information about the sketch.

#### Resetting a sketch

Sketch reset: Use TDIGEST.RESET to clear all data from a sketch when you need to reuse a sketch for new data

**Builds upon:** tdig_cdf

**Commands:** TDIGEST.RESET

**Complexity:**
- TDIGEST.RESET: O(1)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python

##### Redis CLI

```
> TDIGEST.RESET racer_ages
OK
```

##### C#

```csharp
        bool res12 = db.TDIGEST().Reset("racer_ages");
        Console.WriteLine(res12);   // >>> True
```

##### Go

```go
	res12, err := rdb.TDigestReset(ctx, "racer_ages").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res12) // >>> OK
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> tdigResetExample = asyncCommands
                    .tdigestReset("racer_ages")
                    .thenAccept(res12 -> {
                        System.out.println(res12);
                        // >>> OK
                    })
                    .toCompletableFuture();

            tdigResetExample.join();
```

##### Java (Reactive - Lettuce)

```java
            String res12 = reactiveCommands.tdigestReset("racer_ages").block();
            System.out.println(res12);
            // >>> OK
```

##### Java (Synchronous - Jedis)

```java
        String res12 = jedis.tdigestReset("racer_ages");
        System.out.println(res12); // >>> OK
```

##### JavaScript (Node.js)

```javascript
const res12 = await client.tDigest.reset('racer_ages');
console.log(res12);  // >>> OK
```

##### PHP

```php
        $res12 = $r->tdigestreset('racer_ages');
        echo $res12 . PHP_EOL;
        // >>> OK
```

##### Python

```python
res12 = r.tdigest().reset("racer_ages")
print(res12)  # >>> OK
```



## Academic sources
- [The _t_-digest: Efficient estimates of distributions](https://www.sciencedirect.com/science/article/pii/S2665963820300403)

## References
- [t-digest: A New Probabilistic Data Structure in Redis Stack](https://redis.com/blog/t-digest-in-redis-stack/)

