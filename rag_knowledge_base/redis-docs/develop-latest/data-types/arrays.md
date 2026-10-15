# Redis arrays

```json metadata
{
  "schema_version": 2,
  "title": "Redis arrays",
  "description": "Introduction to Redis arrays",
  "categories": ["docs","develop","stack","oss","rs","rc","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"basic-usage","title":"Basic usage"},{"id":"array-length-vs-element-count","title":"Array length vs. element count"},{"id":"reading-ranges","title":"Reading ranges"},{"id":"sequential-insertion","title":"Sequential insertion"},{"id":"ring-buffer-mode","title":"Ring buffer mode"},{"id":"aggregate-operations","title":"Aggregate operations"},{"id":"searching-elements","title":"Searching elements"},{"id":"deleting-elements","title":"Deleting elements"},{"id":"introspection","title":"Introspection"},{"id":"configuration","title":"Configuration"},{"id":"performance","title":"Performance"},{"id":"alternatives","title":"Alternatives"},{"id":"limits","title":"Limits"}]}

,
  "codeExamples": [{"codetabsId":"arrays_tutorial-steparset_arget","commands":[{"acl_categories":["@write","@array","@fast"],"complexity":"O(N)","name":"ARSET"},{"acl_categories":["@read","@array","@fast"],"complexity":"O(1)","name":"ARGET"}],"description":"Write contiguous values with ARSET and read a single index with ARGET; an unset index returns nil","difficulty":"beginner","id":"arset_arget","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_arrays_tutorial-steparset_arget"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_arrays_tutorial-steparset_arget"},{"id":"Node-js","panelId":"panel_Nodejs_arrays_tutorial-steparset_arget"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_arrays_tutorial-steparset_arget"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_arrays_tutorial-steparset_arget"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_arrays_tutorial-steparset_arget"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_arrays_tutorial-steparset_arget"}]},{"codetabsId":"arrays_tutorial-steparmset_armget","commands":[{"acl_categories":["@write","@array","@fast"],"complexity":"O(N)","name":"ARMSET"},{"acl_categories":["@read","@array","@fast"],"complexity":"O(N)","name":"ARMGET"}],"description":"Write to arbitrary, non-contiguous indexes with ARMSET and read several indexes in one round trip with ARMGET","difficulty":"beginner","id":"armset_armget","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_arrays_tutorial-steparmset_armget"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_arrays_tutorial-steparmset_armget"},{"id":"Node-js","panelId":"panel_Nodejs_arrays_tutorial-steparmset_armget"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_arrays_tutorial-steparmset_armget"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_arrays_tutorial-steparmset_armget"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_arrays_tutorial-steparmset_armget"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_arrays_tutorial-steparmset_armget"}]},{"codetabsId":"arrays_tutorial-steplen_count","commands":[{"acl_categories":["@write","@array","@fast"],"complexity":"O(N)","name":"ARSET"},{"acl_categories":["@read","@array","@fast"],"complexity":"O(1)","name":"ARLEN"},{"acl_categories":["@read","@array","@fast"],"complexity":"O(1)","name":"ARCOUNT"}],"description":"Compare the logical length (ARLEN) with the number of non-empty elements (ARCOUNT) for a sparse array","difficulty":"beginner","id":"len_count","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_arrays_tutorial-steplen_count"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_arrays_tutorial-steplen_count"},{"id":"Node-js","panelId":"panel_Nodejs_arrays_tutorial-steplen_count"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_arrays_tutorial-steplen_count"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_arrays_tutorial-steplen_count"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_arrays_tutorial-steplen_count"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_arrays_tutorial-steplen_count"}]},{"codetabsId":"arrays_tutorial-stepargetrange","commands":[{"acl_categories":["@write","@array","@fast"],"complexity":"O(N)","name":"ARMSET"},{"acl_categories":["@read","@array","@slow"],"complexity":"O(N)","name":"ARGETRANGE"}],"description":"Read every position in a range with ARGETRANGE, including empty slots returned as nil","difficulty":"beginner","id":"argetrange","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_arrays_tutorial-stepargetrange"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_arrays_tutorial-stepargetrange"},{"id":"Node-js","panelId":"panel_Nodejs_arrays_tutorial-stepargetrange"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_arrays_tutorial-stepargetrange"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_arrays_tutorial-stepargetrange"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_arrays_tutorial-stepargetrange"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_arrays_tutorial-stepargetrange"}]},{"buildsUpon":["argetrange"],"codetabsId":"arrays_tutorial-steparscan","commands":[{"acl_categories":["@read","@array","@slow"],"complexity":"O(P)","name":"ARSCAN"}],"description":"Iterate only the elements that exist with ARSCAN, retrieving each index alongside its value","difficulty":"beginner","id":"arscan","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_arrays_tutorial-steparscan"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_arrays_tutorial-steparscan"},{"id":"Node-js","panelId":"panel_Nodejs_arrays_tutorial-steparscan"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_arrays_tutorial-steparscan"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_arrays_tutorial-steparscan"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_arrays_tutorial-steparscan"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_arrays_tutorial-steparscan"}]},{"codetabsId":"arrays_tutorial-steparinsert","commands":[{"acl_categories":["@write","@array","@fast"],"complexity":"O(N)","name":"ARINSERT"},{"acl_categories":["@read","@array","@fast"],"complexity":"O(1)","name":"ARNEXT"},{"acl_categories":["@write","@array","@fast"],"complexity":"O(1)","name":"ARSEEK"}],"description":"Append values with ARINSERT using an auto-advancing cursor, inspect it with ARNEXT, and reposition it with ARSEEK","difficulty":"beginner","id":"arinsert","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_arrays_tutorial-steparinsert"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_arrays_tutorial-steparinsert"},{"id":"Node-js","panelId":"panel_Nodejs_arrays_tutorial-steparinsert"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_arrays_tutorial-steparinsert"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_arrays_tutorial-steparinsert"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_arrays_tutorial-steparinsert"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_arrays_tutorial-steparinsert"}]},{"codetabsId":"arrays_tutorial-steparring","commands":[{"acl_categories":["@write","@array","@slow"],"complexity":"O(M)","name":"ARRING"},{"acl_categories":["@read","@array","@fast"],"complexity":"O(1)","name":"ARGET"}],"description":"Use ARRING to maintain a fixed-size circular buffer that wraps and overwrites the oldest entry once full","difficulty":"beginner","id":"arring","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_arrays_tutorial-steparring"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_arrays_tutorial-steparring"},{"id":"Node-js","panelId":"panel_Nodejs_arrays_tutorial-steparring"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_arrays_tutorial-steparring"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_arrays_tutorial-steparring"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_arrays_tutorial-steparring"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_arrays_tutorial-steparring"}]},{"buildsUpon":["arring"],"codetabsId":"arrays_tutorial-steparlastitems","commands":[{"acl_categories":["@read","@array","@slow"],"complexity":"O(N)","name":"ARLASTITEMS"}],"description":"Retrieve the N most recently inserted elements with ARLASTITEMS, optionally reversing the order with REV","difficulty":"beginner","id":"arlastitems","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_arrays_tutorial-steparlastitems"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_arrays_tutorial-steparlastitems"},{"id":"Node-js","panelId":"panel_Nodejs_arrays_tutorial-steparlastitems"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_arrays_tutorial-steparlastitems"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_arrays_tutorial-steparlastitems"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_arrays_tutorial-steparlastitems"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_arrays_tutorial-steparlastitems"}]},{"codetabsId":"arrays_tutorial-steparop","commands":[{"acl_categories":["@write","@array","@fast"],"complexity":"O(N)","name":"ARMSET"},{"acl_categories":["@read","@array","@slow"],"complexity":"O(P)","name":"AROP"}],"description":"Run a single-pass aggregate over a contiguous range with AROP, such as SUM, MAX, or a MATCH count","difficulty":"beginner","id":"arop","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_arrays_tutorial-steparop"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_arrays_tutorial-steparop"},{"id":"Node-js","panelId":"panel_Nodejs_arrays_tutorial-steparop"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_arrays_tutorial-steparop"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_arrays_tutorial-steparop"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_arrays_tutorial-steparop"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_arrays_tutorial-steparop"}]},{"codetabsId":"arrays_tutorial-stepargrep","commands":[{"acl_categories":["@keyspace","@write","@slow"],"complexity":"O(N)","name":"DEL"},{"acl_categories":["@write","@array","@fast"],"complexity":"O(N)","name":"ARMSET"},{"acl_categories":["@read","@array","@slow"],"complexity":"O(P * C)","name":"ARGREP"}],"description":"Find elements matching textual predicates (EXACT, MATCH, GLOB, RE) with ARGREP, combined with AND or OR","difficulty":"beginner","id":"argrep","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_arrays_tutorial-stepargrep"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_arrays_tutorial-stepargrep"},{"id":"Node-js","panelId":"panel_Nodejs_arrays_tutorial-stepargrep"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_arrays_tutorial-stepargrep"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_arrays_tutorial-stepargrep"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_arrays_tutorial-stepargrep"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_arrays_tutorial-stepargrep"}]},{"buildsUpon":["arop"],"codetabsId":"arrays_tutorial-stepardel","commands":[{"acl_categories":["@write","@array","@fast"],"complexity":"O(N)","name":"ARDEL"},{"acl_categories":["@write","@array","@slow"],"name":"ARDELRANGE"}],"description":"Delete elements by index with ARDEL or remove a whole index range with ARDELRANGE","difficulty":"beginner","id":"ardel","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_arrays_tutorial-stepardel"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_arrays_tutorial-stepardel"},{"id":"Node-js","panelId":"panel_Nodejs_arrays_tutorial-stepardel"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_arrays_tutorial-stepardel"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_arrays_tutorial-stepardel"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_arrays_tutorial-stepardel"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_arrays_tutorial-stepardel"}]}]
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


### Array command summary

**18 commands in this group:**

[View all array commands](https://redis.io/commands/?group=array)

| Command | Summary | Complexity | Since |
|---------|---------|------------|-------|
| [ARCOUNT](https://redis.io/commands/arcount/) | Returns the number of non-empty elements in an array. | O(1) | 8.8.0 |
| [ARDEL](https://redis.io/commands/ardel/) | Deletes elements at the specified indices in an array. | O(N) where N is the number of indices to delete | 8.8.0 |
| [ARDELRANGE](https://redis.io/commands/ardelrange/) | Deletes elements in one or more ranges. | Proportional to the number of existing elements... | 8.8.0 |
| [ARGET](https://redis.io/commands/arget/) | Gets the value at an index in an array. | O(1) | 8.8.0 |
| [ARGETRANGE](https://redis.io/commands/argetrange/) | Gets values in a range of indices. | O(N) where N is the range length | 8.8.0 |
| [ARGREP](https://redis.io/commands/argrep/) | Searches array elements in a range using textual predicates. | O(P * C) where P is the number of visited posit... | 8.8.0 |
| [ARINFO](https://redis.io/commands/arinfo/) | Returns metadata about an array. | O(1), or O(N) with FULL option where N is the n... | 8.8.0 |
| [ARINSERT](https://redis.io/commands/arinsert/) | Inserts one or more values at consecutive indices. | O(N) where N is the number of values | 8.8.0 |
| [ARLASTITEMS](https://redis.io/commands/arlastitems/) | Returns the most recently inserted elements. | O(N) where N is the count | 8.8.0 |
| [ARLEN](https://redis.io/commands/arlen/) | Returns the length of an array (max index + 1). | O(1) | 8.8.0 |

#### Array command summary (part 2)

| Command | Summary | Complexity | Since |
|---------|---------|------------|-------|
| [ARMGET](https://redis.io/commands/armget/) | Gets values at multiple indices in an array. | O(N) where N is the number of indices | 8.8.0 |
| [ARMSET](https://redis.io/commands/armset/) | Sets multiple index-value pairs in an array. | O(N) where N is the number of pairs | 8.8.0 |
| [ARNEXT](https://redis.io/commands/arnext/) | Returns the next index ARINSERT would use. | O(1) | 8.8.0 |
| [AROP](https://redis.io/commands/arop/) | Performs aggregate operations on array elements in a range. | O(P) where P is visited positions in touched sl... | 8.8.0 |
| [ARRING](https://redis.io/commands/arring/) | Inserts values into a ring buffer of specified size, wrapping and truncating as needed. | O(M) normally, O(N+M) on ring resize, where N i... | 8.8.0 |
| [ARSCAN](https://redis.io/commands/arscan/) | Iterates existing elements in a range, returning index-value pairs. | O(P) where P is visited positions in touched sl... | 8.8.0 |
| [ARSEEK](https://redis.io/commands/arseek/) | Sets the ARINSERT / ARRING cursor to a specific index. | O(1) | 8.8.0 |
| [ARSET](https://redis.io/commands/arset/) | Sets one or more contiguous values starting at an index in an array. | O(N) where N is the number of values | 8.8.0 |



Redis arrays are sparse, index-addressable data structures that map integer indexes (in the range 0 to 2⁶⁴−1) to string values. Unlike lists, elements are accessed directly by index rather than by position in a sequence, and you can set any index without allocating the gaps between occupied slots. This makes arrays well-suited for timestamped event logs, ring buffers over streaming measurements, sliding-window analytics, and other workloads that involve sparse or high-index access patterns.

## Basic usage

Use [`ARSET`](https://redis.io/docs/latest/commands/arset) to write one or more contiguous values starting at a given index, and [`ARGET`](https://redis.io/docs/latest/commands/arget) to read the value at an index. Accessing an unset index returns a nil reply.

Write contiguous values with ARSET and read a single index with ARGET; an unset index returns nil

**Commands:** ARSET, ARGET

**Complexity:**
- ARSET: O(N)
- ARGET: O(1)

**Available in:** Redis CLI, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), JavaScript (Node.js), PHP, Python

##### Redis CLI

```
> ARSET events:1 0 "login" "click" "purchase"
(integer) 3
> ARGET events:1 0
"login"
> ARGET events:1 999
(nil)
```

##### Go

```go
	setRes, err := rdb.ARSet(ctx, "events:1", 0, "login", "click", "purchase").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(setRes) // >>> 3

	getRes, err := rdb.ARGet(ctx, "events:1", 0).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(getRes) // >>> login

	missing, err := rdb.ARGet(ctx, "events:1", 999).Result()

	if err == redis.Nil {
		fmt.Println("<nil>") // >>> <nil>
	} else if err != nil {
		panic(err)
	} else {
		fmt.Println(missing)
	}
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> arsetArgetExample = asyncCommands
                    .arset("events:1", 0, "login", "click", "purchase")
                    .thenCompose(res1 -> {
                        System.out.println(res1);
                        // >>> 3
                        return asyncCommands.arget("events:1", 0);
                    })
                    .thenCompose(res2 -> {
                        System.out.println(res2);
                        // >>> login
                        return asyncCommands.arget("events:1", 999);
                    })
                    .thenAccept(res3 -> {
                        System.out.println(res3);
                        // >>> null
                    })
                    .toCompletableFuture();

            arsetArgetExample.join();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Long> arsetArget1 = reactiveCommands.arset("events:1", 0, "login", "click", "purchase")
                    .doOnNext(result -> {
                        System.out.println(result); // >>> 3
                    });

            arsetArget1.block();

            Mono<String> arsetArget2 = reactiveCommands.arget("events:1", 0).doOnNext(result -> {
                System.out.println(result); // >>> login
            });

            arsetArget2.block();

            Mono<Optional<String>> arsetArget3 = reactiveCommands.arget("events:1", 999)
                    .map(Optional::of)
                    .defaultIfEmpty(Optional.empty())
                    .doOnNext(result -> {
                        System.out.println(result.orElse(null)); // >>> null
                    });

            arsetArget3.block();
```

##### JavaScript (Node.js)

```javascript
const setResult = await client.arSet('events:1', 0, ['login', 'click', 'purchase']);
console.log(setResult); // >>> 3

const getResult = await client.arGet('events:1', 0);
console.log(getResult); // >>> login

const missingResult = await client.arGet('events:1', 999);
console.log(missingResult); // >>> null
```

##### PHP

```php
        $res1 = $redis->arset('events:1', 0, ['login', 'click', 'purchase']);
        echo $res1 . PHP_EOL; // >>> 3

        $res2 = $redis->arget('events:1', 0);
        echo $res2 . PHP_EOL; // >>> login

        $res3 = $redis->arget('events:1', 999);
        echo var_export($res3, true) . PHP_EOL; // >>> NULL
```

##### Python

```python
res1 = r.arset("events:1", 0, "login", "click", "purchase")
print(res1)
# >>> 3

res2 = r.arget("events:1", 0)
print(res2)
# >>> login

res3 = r.arget("events:1", 999)
print(res3)
# >>> None
```



To write values at arbitrary, non-contiguous indexes, use [`ARMSET`](https://redis.io/docs/latest/commands/armset). To read several indexes in one round trip, use [`ARMGET`](https://redis.io/docs/latest/commands/armget):

Write to arbitrary, non-contiguous indexes with ARMSET and read several indexes in one round trip with ARMGET

**Commands:** ARMSET, ARMGET

**Complexity:**
- ARMSET: O(N)
- ARMGET: O(N)

**Available in:** Redis CLI, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), JavaScript (Node.js), PHP, Python

##### Redis CLI

```
> ARMSET metrics 0 "10" 5 "20" 100 "30"
(integer) 3
> ARMGET metrics 0 5 100 999
1) "10"
2) "20"
3) "30"
4) (nil)
```

##### Go

```go
	msetRes, err := rdb.ARMSet(ctx, "metrics",
		redis.AREntry{Index: 0, Value: "10"},
		redis.AREntry{Index: 5, Value: "20"},
		redis.AREntry{Index: 100, Value: "30"},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(msetRes) // >>> 3

	mgetRes, err := rdb.ARMGet(ctx, "metrics", 0, 5, 100, 999).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(mgetRes) // >>> [10 20 30 <nil>]
```

##### Java (Asynchronous - Lettuce)

```java
            Map<Long, String> metricsValues = new HashMap<>();
            metricsValues.put(0L, "10");
            metricsValues.put(5L, "20");
            metricsValues.put(100L, "30");

            CompletableFuture<Void> armsetArmgetExample = asyncCommands
                    .armset("metrics", metricsValues)
                    .thenCompose(res1 -> {
                        System.out.println(res1);
                        // >>> 3
                        return asyncCommands.armget("metrics", 0, 5, 100, 999);
                    })
                    .thenAccept(res2 -> {
                        System.out.println(res2);
                        // >>> [10, 20, 30, null]
                    })
                    .toCompletableFuture();

            armsetArmgetExample.join();
```

##### Java (Reactive - Lettuce)

```java
            Map<Long, String> armsetParams = new HashMap<>();
            armsetParams.put(0L, "10");
            armsetParams.put(5L, "20");
            armsetParams.put(100L, "30");

            Mono<Long> armsetArmget1 = reactiveCommands.armset("metrics", armsetParams).doOnNext(result -> {
                System.out.println(result); // >>> 3
            });

            armsetArmget1.block();

            Mono<List<String>> armsetArmget2 = reactiveCommands.armget("metrics", 0, 5, 100, 999)
                    .collectList()
                    .map(values -> values.stream()
                            .map(value -> value.getValueOrElse(null))
                            .collect(Collectors.toList()))
                    .doOnNext(result -> {
                        System.out.println(result); // >>> [10, 20, 30, null]
                    });

            armsetArmget2.block();
```

##### JavaScript (Node.js)

```javascript
const mSetResult = await client.arMSet('metrics', { 0: '10', 5: '20', 100: '30' });
console.log(mSetResult); // >>> 3

const mGetResult = await client.arMGet('metrics', [0, 5, 100, 999]);
console.log(mGetResult); // >>> [ '10', '20', '30', null ]
```

##### PHP

```php
        $res1 = $redis->armset('metrics', [0 => '10', 5 => '20', 100 => '30']);
        echo $res1 . PHP_EOL; // >>> 3

        $res2 = $redis->armget('metrics', [0, 5, 100, 999]);
        echo json_encode($res2) . PHP_EOL; // >>> ["10","20","30",null]
```

##### Python

```python
res4 = r.armset("metrics", {0: "10", 5: "20", 100: "30"})
print(res4)
# >>> 3

res5 = r.armget("metrics", 0, 5, 100, 999)
print(res5)
# >>> ['10', '20', '30', None]
```



## Array length vs. element count

Redis arrays expose two distinct size measurements:

- [`ARLEN`](https://redis.io/docs/latest/commands/arlen) returns the *logical length*: the highest set index plus one.
- [`ARCOUNT`](https://redis.io/docs/latest/commands/arcount) returns the number of *non-empty* elements.

For a sparse array, these values can differ substantially:

Compare the logical length (ARLEN) with the number of non-empty elements (ARCOUNT) for a sparse array

**Commands:** ARSET, ARLEN, ARCOUNT

**Complexity:**
- ARSET: O(N)
- ARLEN: O(1)
- ARCOUNT: O(1)

**Available in:** Redis CLI, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), JavaScript (Node.js), PHP, Python

##### Redis CLI

```
> ARSET sparse 0 "a"
(integer) 1
> ARSET sparse 1000000 "b"
(integer) 1
> ARLEN sparse
(integer) 1000001
> ARCOUNT sparse
(integer) 2
```

##### Go

```go
	set1, err := rdb.ARSet(ctx, "sparse", 0, "a").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(set1) // >>> 1

	set2, err := rdb.ARSet(ctx, "sparse", 1000000, "b").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(set2) // >>> 1

	lenRes, err := rdb.ARLen(ctx, "sparse").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(lenRes) // >>> 1000001

	countRes, err := rdb.ARCount(ctx, "sparse").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(countRes) // >>> 2
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> lenCountExample = asyncCommands
                    .arset("sparse", 0, "a")
                    .thenCompose(res1 -> {
                        System.out.println(res1);
                        // >>> 1
                        return asyncCommands.arset("sparse", 1000000, "b");
                    })
                    .thenCompose(res2 -> {
                        System.out.println(res2);
                        // >>> 1
                        return asyncCommands.arlen("sparse");
                    })
                    .thenCompose(res3 -> {
                        System.out.println(res3);
                        // >>> 1000001
                        return asyncCommands.arcount("sparse");
                    })
                    .thenAccept(res4 -> {
                        System.out.println(res4);
                        // >>> 2
                    })
                    .toCompletableFuture();

            lenCountExample.join();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Long> lenCount1 = reactiveCommands.arset("sparse", 0, "a").doOnNext(result -> {
                System.out.println(result); // >>> 1
            });

            lenCount1.block();

            Mono<Long> lenCount2 = reactiveCommands.arset("sparse", 1000000, "b").doOnNext(result -> {
                System.out.println(result); // >>> 1
            });

            lenCount2.block();

            Mono<Long> lenCount3 = reactiveCommands.arlen("sparse").doOnNext(result -> {
                System.out.println(result); // >>> 1000001
            });

            lenCount3.block();

            Mono<Long> lenCount4 = reactiveCommands.arcount("sparse").doOnNext(result -> {
                System.out.println(result); // >>> 2
            });

            lenCount4.block();
```

##### JavaScript (Node.js)

```javascript
const setA = await client.arSet('sparse', 0, 'a');
console.log(setA); // >>> 1

const setB = await client.arSet('sparse', 1000000, 'b');
console.log(setB); // >>> 1

const lenResult = await client.arLen('sparse');
console.log(lenResult); // >>> 1000001

const countResult = await client.arCount('sparse');
console.log(countResult); // >>> 2
```

##### PHP

```php
        $res1 = $redis->arset('sparse', 0, 'a');
        echo $res1 . PHP_EOL; // >>> 1

        $res2 = $redis->arset('sparse', 1000000, 'b');
        echo $res2 . PHP_EOL; // >>> 1

        $res3 = $redis->arlen('sparse');
        echo $res3 . PHP_EOL; // >>> 1000001

        $res4 = $redis->arcount('sparse');
        echo $res4 . PHP_EOL; // >>> 2
```

##### Python

```python
res6 = r.arset("sparse", 0, "a")
print(res6)
# >>> 1

res7 = r.arset("sparse", 1000000, "b")
print(res7)
# >>> 1

res8 = r.arlen("sparse")
print(res8)
# >>> 1000001

res9 = r.arcount("sparse")
print(res9)
# >>> 2
```



## Reading ranges

[`ARGETRANGE`](https://redis.io/docs/latest/commands/argetrange) returns every position in a range—including empty slots as nil—in index order. Reversing `start` and `end` reverses the direction:

Read every position in a range with ARGETRANGE, including empty slots returned as nil

**Commands:** ARMSET, ARGETRANGE

**Complexity:**
- ARMSET: O(N)
- ARGETRANGE: O(N)

**Available in:** Redis CLI, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), JavaScript (Node.js), PHP, Python

##### Redis CLI

```
> ARMSET seq 0 "a" 1 "b" 3 "d"
(integer) 3
> ARGETRANGE seq 0 3
1) "a"
2) "b"
3) (nil)
4) "d"
```

##### Go

```go
	msetRes, err := rdb.ARMSet(ctx, "seq",
		redis.AREntry{Index: 0, Value: "a"},
		redis.AREntry{Index: 1, Value: "b"},
		redis.AREntry{Index: 3, Value: "d"},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(msetRes) // >>> 3

	rangeRes, err := rdb.ARGetRange(ctx, "seq", 0, 3).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(rangeRes) // >>> [a b <nil> d]
```

##### Java (Asynchronous - Lettuce)

```java
            Map<Long, String> seqRangeValues = new HashMap<>();
            seqRangeValues.put(0L, "a");
            seqRangeValues.put(1L, "b");
            seqRangeValues.put(3L, "d");

            CompletableFuture<Void> argetrangeExample = asyncCommands
                    .armset("seq", seqRangeValues)
                    .thenCompose(res1 -> {
                        System.out.println(res1);
                        // >>> 3
                        return asyncCommands.argetrange("seq", 0, 3);
                    })
                    .thenAccept(res2 -> {
                        System.out.println(res2);
                        // >>> [a, b, null, d]
                    })
                    .toCompletableFuture();

            argetrangeExample.join();
```

##### Java (Reactive - Lettuce)

```java
            Map<Long, String> argetrangeParams = new HashMap<>();
            argetrangeParams.put(0L, "a");
            argetrangeParams.put(1L, "b");
            argetrangeParams.put(3L, "d");

            Mono<Long> argetrange1 = reactiveCommands.armset("seq", argetrangeParams).doOnNext(result -> {
                System.out.println(result); // >>> 3
            });

            argetrange1.block();

            Mono<List<String>> argetrange2 = reactiveCommands.argetrange("seq", 0, 3)
                    .collectList()
                    .map(values -> values.stream()
                            .map(value -> value.getValueOrElse(null))
                            .collect(Collectors.toList()))
                    .doOnNext(result -> {
                        System.out.println(result); // >>> [a, b, null, d]
                    });

            argetrange2.block();
```

##### JavaScript (Node.js)

```javascript
const rangeSetResult = await client.arMSet('seq', { 0: 'a', 1: 'b', 3: 'd' });
console.log(rangeSetResult); // >>> 3

const rangeResult = await client.arGetRange('seq', 0, 3);
console.log(rangeResult); // >>> [ 'a', 'b', null, 'd' ]
```

##### PHP

```php
        $res1 = $redis->armset('seq', [0 => 'a', 1 => 'b', 3 => 'd']);
        echo $res1 . PHP_EOL; // >>> 3

        $res2 = $redis->argetrange('seq', 0, 3);
        echo json_encode($res2) . PHP_EOL; // >>> ["a","b",null,"d"]
```

##### Python

```python
res10 = r.armset("seq", {0: "a", 1: "b", 3: "d"})
print(res10)
# >>> 3

res11 = r.argetrange("seq", 0, 3)
print(res11)
# >>> ['a', 'b', None, 'd']
```



To iterate only the elements that exist and retrieve their indexes alongside their values, use [`ARSCAN`](https://redis.io/docs/latest/commands/arscan). It skips empty slots and returns an array of index-value pairs, with an optional `LIMIT` to cap the result size:

Iterate only the elements that exist with ARSCAN, retrieving each index alongside its value

**Builds upon:** argetrange

**Commands:** ARSCAN

**Complexity:**
- ARSCAN: O(P)

**Available in:** Redis CLI, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), JavaScript (Node.js), PHP, Python

##### Redis CLI

```
> ARSCAN seq 0 3
1) 1) (integer) 0
   2) "a"
2) 1) (integer) 1
   2) "b"
3) 1) (integer) 3
   2) "d"
```

##### Go

```go
	msetRes, err := rdb.ARMSet(ctx, "seq",
		redis.AREntry{Index: 0, Value: "a"},
		redis.AREntry{Index: 1, Value: "b"},
		redis.AREntry{Index: 3, Value: "d"},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(msetRes) // >>> 3

	scanRes, err := rdb.ARScan(ctx, "seq", 0, 3, nil).Result()

	if err != nil {
		panic(err)
	}

	for _, entry := range scanRes {
		fmt.Printf("%d -> %s\n", entry.Index, entry.Value)
	}
	// >>> 0 -> a
	// >>> 1 -> b
	// >>> 3 -> d
```

##### Java (Asynchronous - Lettuce)

```java
            Map<Long, String> seqScanValues = new HashMap<>();
            seqScanValues.put(0L, "a");
            seqScanValues.put(1L, "b");
            seqScanValues.put(3L, "d");

            CompletableFuture<Void> arscanExample = asyncCommands
                    .armset("seq", seqScanValues)
                    .thenCompose(res1 -> {
                        System.out.println(res1);
                        // >>> 3
                        return asyncCommands.arscan("seq", 0, 3);
                    })
                    .thenAccept(res2 -> {
                        for (IndexedValue<String> pair : res2) {
                            System.out.println(pair.getIndex() + " -> " + pair.getValue());
                        }
                        // >>> 0 -> a
                        // >>> 1 -> b
                        // >>> 3 -> d
                    })
                    .toCompletableFuture();

            arscanExample.join();
```

##### Java (Reactive - Lettuce)

```java
            Map<Long, String> arscanParams = new HashMap<>();
            arscanParams.put(0L, "a");
            arscanParams.put(1L, "b");
            arscanParams.put(3L, "d");

            Mono<Long> arscan1 = reactiveCommands.armset("seq", arscanParams).doOnNext(result -> {
                System.out.println(result); // >>> 3
            });

            arscan1.block();

            Mono<List<IndexedValue<String>>> arscan2 = reactiveCommands.arscan("seq", 0, 3)
                    .doOnNext(entry -> {
                        System.out.println(entry.getIndex() + " -> " + entry.getValue());
                        // >>> 0 -> a
                        // >>> 1 -> b
                        // >>> 3 -> d
                    })
                    .collectList()
            ;

            arscan2.block();
```

##### JavaScript (Node.js)

```javascript
const scanSetResult = await client.arMSet('seq', { 0: 'a', 1: 'b', 3: 'd' });
console.log(scanSetResult); // >>> 3

const scanResult = await client.arScan('seq', 0, 3);
for (const { index, value } of scanResult) {
  console.log(`${index} -> ${value}`);
}
// >>> 0 -> a
// >>> 1 -> b
// >>> 3 -> d
```

##### PHP

```php
        $res1 = $redis->armset('seq', [0 => 'a', 1 => 'b', 3 => 'd']);
        echo $res1 . PHP_EOL; // >>> 3

        $res2 = $redis->arscan('seq', 0, 3);
        foreach ($res2 as $pair) {
            echo $pair[0] . ' -> ' . $pair[1] . PHP_EOL;
        }
        // >>> 0 -> a
        // >>> 1 -> b
        // >>> 3 -> d
```

##### Python

```python
res12 = r.armset("seq", {0: "a", 1: "b", 3: "d"})
print(res12)
# >>> 3

res13 = r.arscan("seq", 0, 3)
for index, value in res13:
    print(f"{index} -> {value}")
# >>> 0 -> a
# >>> 1 -> b
# >>> 3 -> d
```



## Sequential insertion

[`ARINSERT`](https://redis.io/docs/latest/commands/arinsert) appends values using an internal cursor that advances automatically after each call. Use [`ARNEXT`](https://redis.io/docs/latest/commands/arnext) to inspect where the next insert would land, and [`ARSEEK`](https://redis.io/docs/latest/commands/arseek) to reposition the cursor:

Append values with ARINSERT using an auto-advancing cursor, inspect it with ARNEXT, and reposition it with ARSEEK

**Commands:** ARINSERT, ARNEXT, ARSEEK

**Complexity:**
- ARINSERT: O(N)
- ARNEXT: O(1)
- ARSEEK: O(1)

**Available in:** Redis CLI, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), JavaScript (Node.js), PHP, Python

##### Redis CLI

```
> ARINSERT log "event1"
(integer) 0
> ARINSERT log "event2"
(integer) 1
> ARNEXT log
(integer) 2
> ARSEEK log 10
(integer) 1
> ARINSERT log "event3"
(integer) 10
```

##### Go

```go
	ins1, err := rdb.ARInsert(ctx, "log", "event1").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(ins1) // >>> 0

	ins2, err := rdb.ARInsert(ctx, "log", "event2").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(ins2) // >>> 1

	nextRes, err := rdb.ARNext(ctx, "log").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(nextRes) // >>> 2

	seekRes, err := rdb.ARSeek(ctx, "log", 10).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(seekRes) // >>> 1

	ins3, err := rdb.ARInsert(ctx, "log", "event3").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(ins3) // >>> 10
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> arinsertExample = asyncCommands
                    .arinsert("log", "event1")
                    .thenCompose(res1 -> {
                        System.out.println(res1);
                        // >>> 0
                        return asyncCommands.arinsert("log", "event2");
                    })
                    .thenCompose(res2 -> {
                        System.out.println(res2);
                        // >>> 1
                        return asyncCommands.arnext("log");
                    })
                    .thenCompose(res3 -> {
                        System.out.println(res3);
                        // >>> 2
                        return asyncCommands.arseek("log", 10);
                    })
                    .thenCompose(res4 -> {
                        System.out.println(res4);
                        // >>> 1
                        return asyncCommands.arinsert("log", "event3");
                    })
                    .thenAccept(res5 -> {
                        System.out.println(res5);
                        // >>> 10
                    })
                    .toCompletableFuture();

            arinsertExample.join();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Long> arinsert1 = reactiveCommands.arinsert("log", "event1").doOnNext(result -> {
                System.out.println(result); // >>> 0
            });

            arinsert1.block();

            Mono<Long> arinsert2 = reactiveCommands.arinsert("log", "event2").doOnNext(result -> {
                System.out.println(result); // >>> 1
            });

            arinsert2.block();

            Mono<Long> arinsert3 = reactiveCommands.arnext("log").doOnNext(result -> {
                System.out.println(result); // >>> 2
            });

            arinsert3.block();

            Mono<Long> arinsert4 = reactiveCommands.arseek("log", 10).doOnNext(result -> {
                System.out.println(result); // >>> 1
            });

            arinsert4.block();

            Mono<Long> arinsert5 = reactiveCommands.arinsert("log", "event3").doOnNext(result -> {
                System.out.println(result); // >>> 10
            });

            arinsert5.block();
```

##### JavaScript (Node.js)

```javascript
const insert1 = await client.arInsert('log', 'event1');
console.log(insert1); // >>> 0

const insert2 = await client.arInsert('log', 'event2');
console.log(insert2); // >>> 1

const nextResult = await client.arNext('log');
console.log(nextResult); // >>> 2

const seekResult = await client.arSeek('log', 10);
console.log(seekResult); // >>> 1

const insert3 = await client.arInsert('log', 'event3');
console.log(insert3); // >>> 10
```

##### PHP

```php
        $res1 = $redis->arinsert('log', 'event1');
        echo $res1 . PHP_EOL; // >>> 0

        $res2 = $redis->arinsert('log', 'event2');
        echo $res2 . PHP_EOL; // >>> 1

        $res3 = $redis->arnext('log');
        echo $res3 . PHP_EOL; // >>> 2

        $res4 = $redis->arseek('log', 10);
        echo $res4 . PHP_EOL; // >>> 1

        $res5 = $redis->arinsert('log', 'event3');
        echo $res5 . PHP_EOL; // >>> 10
```

##### Python

```python
res14 = r.arinsert("log", "event1")
print(res14)
# >>> 0

res15 = r.arinsert("log", "event2")
print(res15)
# >>> 1

res16 = r.arnext("log")
print(res16)
# >>> 2

res17 = r.arseek("log", 10)
print(res17)
# >>> 1

res18 = r.arinsert("log", "event3")
print(res18)
# >>> 10
```



## Ring buffer mode

[`ARRING`](https://redis.io/docs/latest/commands/arring) turns an array into a fixed-size circular buffer. Each call inserts a value at `insert_idx % size`, wrapping back to index `0` once the window is full and overwriting the oldest entry:

Use ARRING to maintain a fixed-size circular buffer that wraps and overwrites the oldest entry once full

**Commands:** ARRING, ARGET

**Complexity:**
- ARRING: O(M)
- ARGET: O(1)

**Available in:** Redis CLI, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), JavaScript (Node.js), PHP, Python

##### Redis CLI

```
> ARRING readings 3 "v0"
(integer) 0
> ARRING readings 3 "v1"
(integer) 1
> ARRING readings 3 "v2"
(integer) 2
> ARRING readings 3 "v3"
(integer) 0
> ARGET readings 0
"v3"
```

##### Go

```go
	ring0, err := rdb.ARRing(ctx, "readings", 3, "v0").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(ring0) // >>> 0

	ring1, err := rdb.ARRing(ctx, "readings", 3, "v1").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(ring1) // >>> 1

	ring2, err := rdb.ARRing(ctx, "readings", 3, "v2").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(ring2) // >>> 2

	ring3, err := rdb.ARRing(ctx, "readings", 3, "v3").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(ring3) // >>> 0

	getRes, err := rdb.ARGet(ctx, "readings", 0).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(getRes) // >>> v3
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> arringExample = asyncCommands
                    .arring("readings", 3, "v0")
                    .thenCompose(res1 -> {
                        System.out.println(res1);
                        // >>> 0
                        return asyncCommands.arring("readings", 3, "v1");
                    })
                    .thenCompose(res2 -> {
                        System.out.println(res2);
                        // >>> 1
                        return asyncCommands.arring("readings", 3, "v2");
                    })
                    .thenCompose(res3 -> {
                        System.out.println(res3);
                        // >>> 2
                        return asyncCommands.arring("readings", 3, "v3");
                    })
                    .thenCompose(res4 -> {
                        System.out.println(res4);
                        // >>> 0
                        return asyncCommands.arget("readings", 0);
                    })
                    .thenAccept(res5 -> {
                        System.out.println(res5);
                        // >>> v3
                    })
                    .toCompletableFuture();

            arringExample.join();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Long> arring1 = reactiveCommands.arring("readings", 3, "v0").doOnNext(result -> {
                System.out.println(result); // >>> 0
            });

            arring1.block();

            Mono<Long> arring2 = reactiveCommands.arring("readings", 3, "v1").doOnNext(result -> {
                System.out.println(result); // >>> 1
            });

            arring2.block();

            Mono<Long> arring3 = reactiveCommands.arring("readings", 3, "v2").doOnNext(result -> {
                System.out.println(result); // >>> 2
            });

            arring3.block();

            Mono<Long> arring4 = reactiveCommands.arring("readings", 3, "v3").doOnNext(result -> {
                System.out.println(result); // >>> 0
            });

            arring4.block();

            Mono<String> arring5 = reactiveCommands.arget("readings", 0).doOnNext(result -> {
                System.out.println(result); // >>> v3
            });

            arring5.block();
```

##### JavaScript (Node.js)

```javascript
const ring0 = await client.arRing('readings', 3, 'v0');
console.log(ring0); // >>> 0

const ring1 = await client.arRing('readings', 3, 'v1');
console.log(ring1); // >>> 1

const ring2 = await client.arRing('readings', 3, 'v2');
console.log(ring2); // >>> 2

const ring3 = await client.arRing('readings', 3, 'v3');
console.log(ring3); // >>> 0

const ringGet = await client.arGet('readings', 0);
console.log(ringGet); // >>> v3
```

##### PHP

```php
        $res1 = $redis->arring('readings', 3, 'v0');
        echo $res1 . PHP_EOL; // >>> 0

        $res2 = $redis->arring('readings', 3, 'v1');
        echo $res2 . PHP_EOL; // >>> 1

        $res3 = $redis->arring('readings', 3, 'v2');
        echo $res3 . PHP_EOL; // >>> 2

        $res4 = $redis->arring('readings', 3, 'v3');
        echo $res4 . PHP_EOL; // >>> 0

        $res5 = $redis->arget('readings', 0);
        echo $res5 . PHP_EOL; // >>> v3
```

##### Python

```python
res19 = r.arring("readings", 3, "v0")
print(res19)
# >>> 0

res20 = r.arring("readings", 3, "v1")
print(res20)
# >>> 1

res21 = r.arring("readings", 3, "v2")
print(res21)
# >>> 2

res22 = r.arring("readings", 3, "v3")
print(res22)
# >>> 0

res23 = r.arget("readings", 0)
print(res23)
# >>> v3
```



[`ARLASTITEMS`](https://redis.io/docs/latest/commands/arlastitems) retrieves the *N* most recently inserted elements in chronological order. Pass the `REV` flag to reverse the order:

Retrieve the N most recently inserted elements with ARLASTITEMS, optionally reversing the order with REV

**Builds upon:** arring

**Commands:** ARLASTITEMS

**Complexity:**
- ARLASTITEMS: O(N)

**Available in:** Redis CLI, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), JavaScript (Node.js), PHP, Python

##### Redis CLI

```
> ARLASTITEMS readings 3
1) "v1"
2) "v2"
3) "v3"
> ARLASTITEMS readings 3 REV
1) "v3"
2) "v2"
3) "v1"
```

##### Go

```go
	// Set up the ring: insert v0, v1, v2, v3 into a size-3 ring.
	for _, v := range []string{"v0", "v1", "v2", "v3"} {
		if err := rdb.ARRing(ctx, "readings", 3, v).Err(); err != nil {
			panic(err)
		}
	}

	lastRes, err := rdb.ARLastItems(ctx, "readings", 3, false).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(lastRes) // >>> [v1 v2 v3]

	lastRevRes, err := rdb.ARLastItems(ctx, "readings", 3, true).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(lastRevRes) // >>> [v3 v2 v1]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> arlastitemsExample = asyncCommands
                    .arring("readings", 3, "v0")
                    .thenCompose(res1 -> asyncCommands.arring("readings", 3, "v1"))
                    .thenCompose(res2 -> asyncCommands.arring("readings", 3, "v2"))
                    .thenCompose(res3 -> asyncCommands.arring("readings", 3, "v3"))
                    .thenCompose(res4 -> asyncCommands.arlastitems("readings", 3))
                    .thenCompose(res5 -> {
                        System.out.println(res5);
                        // >>> [v1, v2, v3]
                        return asyncCommands.arlastitems("readings", 3, true);
                    })
                    .thenAccept(res6 -> {
                        System.out.println(res6);
                        // >>> [v3, v2, v1]
                    })
                    .toCompletableFuture();

            arlastitemsExample.join();
```

##### Java (Reactive - Lettuce)

```java
            // Set up the ring: insert v0, v1, v2, v3 into a size-3 ring.
            reactiveCommands.arring("readings", 3, "v0").block();
            reactiveCommands.arring("readings", 3, "v1").block();
            reactiveCommands.arring("readings", 3, "v2").block();
            reactiveCommands.arring("readings", 3, "v3").block();

            Mono<List<String>> arlastitems1 = reactiveCommands.arlastitems("readings", 3).collectList()
                    .doOnNext(result -> {
                        System.out.println(result); // >>> [v1, v2, v3]
                    });

            arlastitems1.block();

            Mono<List<String>> arlastitems2 = reactiveCommands.arlastitems("readings", 3, true).collectList()
                    .doOnNext(result -> {
                        System.out.println(result); // >>> [v3, v2, v1]
                    });

            arlastitems2.block();
```

##### JavaScript (Node.js)

```javascript
await client.arRing('readings', 3, 'v0');
await client.arRing('readings', 3, 'v1');
await client.arRing('readings', 3, 'v2');
await client.arRing('readings', 3, 'v3');

const lastItems = await client.arLastItems('readings', 3);
console.log(lastItems); // >>> [ 'v1', 'v2', 'v3' ]

const lastItemsRev = await client.arLastItems('readings', 3, { REV: true });
console.log(lastItemsRev); // >>> [ 'v3', 'v2', 'v1' ]
```

##### PHP

```php
        $redis->arring('readings', 3, 'v0');
        $redis->arring('readings', 3, 'v1');
        $redis->arring('readings', 3, 'v2');
        $redis->arring('readings', 3, 'v3');

        $res1 = $redis->arlastitems('readings', 3);
        echo json_encode($res1) . PHP_EOL; // >>> ["v1","v2","v3"]

        $res2 = $redis->arlastitems('readings', 3, true);
        echo json_encode($res2) . PHP_EOL; // >>> ["v3","v2","v1"]
```

##### Python

```python
r.arring("readings", 3, "v0")
r.arring("readings", 3, "v1")
r.arring("readings", 3, "v2")
r.arring("readings", 3, "v3")

res24 = r.arlastitems("readings", 3)
print(res24)
# >>> ['v1', 'v2', 'v3']

res25 = r.arlastitems("readings", 3, rev=True)
print(res25)
# >>> ['v3', 'v2', 'v1']
```



## Aggregate operations

[`AROP`](https://redis.io/docs/latest/commands/arop) performs a single-pass aggregate over a contiguous range of elements:

| Operation | Description |
|-----------|-------------|
| `SUM` | Sum of numeric values |
| `MIN` | Minimum numeric value |
| `MAX` | Maximum numeric value |
| `AND` / `OR` / `XOR` | Bitwise operation on integer values |
| `MATCH value` | Count of elements equal to `value` |
| `USED` | Count of non-empty elements in the range |

Run a single-pass aggregate over a contiguous range with AROP, such as SUM, MAX, or a MATCH count

**Commands:** ARMSET, AROP

**Complexity:**
- ARMSET: O(N)
- AROP: O(P)

**Available in:** Redis CLI, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), JavaScript (Node.js), PHP, Python

##### Redis CLI

```
> ARMSET scores 0 "10" 1 "20" 2 "30"
(integer) 3
> AROP scores 0 2 SUM
"60"
> AROP scores 0 2 MAX
"30"
> AROP scores 0 2 MATCH "10"
(integer) 1
```

##### Go

```go
	msetRes, err := rdb.ARMSet(ctx, "scores",
		redis.AREntry{Index: 0, Value: "10"},
		redis.AREntry{Index: 1, Value: "20"},
		redis.AREntry{Index: 2, Value: "30"},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(msetRes) // >>> 3

	sumRes, err := rdb.AROpSum(ctx, "scores", 0, 2).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(sumRes) // >>> 60

	maxRes, err := rdb.AROpMax(ctx, "scores", 0, 2).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(maxRes) // >>> 30

	matchRes, err := rdb.AROpMatch(ctx, "scores", 0, 2, "10").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(matchRes) // >>> 1
```

##### Java (Asynchronous - Lettuce)

```java
            Map<Long, String> aropScores = new HashMap<>();
            aropScores.put(0L, "10");
            aropScores.put(1L, "20");
            aropScores.put(2L, "30");

            CompletableFuture<Void> aropExample = asyncCommands
                    .armset("scores", aropScores)
                    .thenCompose(res1 -> {
                        System.out.println(res1);
                        // >>> 3
                        return asyncCommands.aropAggregate("scores", 0, 2, ArAggregateType.SUM);
                    })
                    .thenCompose(res2 -> {
                        System.out.println(res2);
                        // >>> 60
                        return asyncCommands.aropAggregate("scores", 0, 2, ArAggregateType.MAX);
                    })
                    .thenCompose(res3 -> {
                        System.out.println(res3);
                        // >>> 30
                        return asyncCommands.aropCount("scores", 0, 2, "10");
                    })
                    .thenAccept(res4 -> {
                        System.out.println(res4);
                        // >>> 1
                    })
                    .toCompletableFuture();

            aropExample.join();
```

##### Java (Reactive - Lettuce)

```java
            Map<Long, String> aropParams = new HashMap<>();
            aropParams.put(0L, "10");
            aropParams.put(1L, "20");
            aropParams.put(2L, "30");

            Mono<Long> arop1 = reactiveCommands.armset("scores", aropParams).doOnNext(result -> {
                System.out.println(result); // >>> 3
            });

            arop1.block();

            Mono<String> arop2 = reactiveCommands.aropAggregate("scores", 0, 2, ArAggregateType.SUM)
                    .doOnNext(result -> {
                        System.out.println(result); // >>> 60
                    });

            arop2.block();

            Mono<String> arop3 = reactiveCommands.aropAggregate("scores", 0, 2, ArAggregateType.MAX)
                    .doOnNext(result -> {
                        System.out.println(result); // >>> 30
                    });

            arop3.block();

            Mono<Long> arop4 = reactiveCommands.aropCount("scores", 0, 2, "10").doOnNext(result -> {
                System.out.println(result); // >>> 1
            });

            arop4.block();
```

##### JavaScript (Node.js)

```javascript
const opSetResult = await client.arMSet('scores', { 0: '10', 1: '20', 2: '30' });
console.log(opSetResult); // >>> 3

const sumResult = await client.arOp('scores', 0, 2, 'SUM');
console.log(sumResult); // >>> 60

const maxResult = await client.arOp('scores', 0, 2, 'MAX');
console.log(maxResult); // >>> 30

const matchResult = await client.arOp('scores', 0, 2, 'MATCH', '10');
console.log(matchResult); // >>> 1
```

##### PHP

```php
        $res1 = $redis->armset('scores', [0 => '10', 1 => '20', 2 => '30']);
        echo $res1 . PHP_EOL; // >>> 3

        $res2 = $redis->arop('scores', 0, 2, 'SUM');
        echo $res2 . PHP_EOL; // >>> 60

        $res3 = $redis->arop('scores', 0, 2, 'MAX');
        echo $res3 . PHP_EOL; // >>> 30

        $res4 = $redis->arop('scores', 0, 2, 'MATCH', '10');
        echo $res4 . PHP_EOL; // >>> 1
```

##### Python

```python
res26 = r.armset("scores", {0: "10", 1: "20", 2: "30"})
print(res26)
# >>> 3

res27 = r.arop("scores", 0, 2, ArrayAggregateOperations.SUM)
print(res27)
# >>> 60

res28 = r.arop("scores", 0, 2, ArrayAggregateOperations.MAX)
print(res28)
# >>> 30

res29 = r.arop("scores", 0, 2, ArrayAggregateOperations.MATCH, value="10")
print(res29)
# >>> 1
```



## Searching elements

[`ARGREP`](https://redis.io/docs/latest/commands/argrep) finds elements in a range whose values match one or more textual predicates and returns their indexes. Empty slots are skipped. Four predicate forms are supported: `EXACT` (full equality), `MATCH` (substring), `GLOB` (the same wildcard syntax as [`SCAN`](https://redis.io/docs/latest/commands/scan) `MATCH`), and `RE` (regular expression). Multiple predicates are combined with `OR` by default, or with `AND` when the option is given. Pass `NOCASE` for case-insensitive comparisons, `WITHVALUES` to return matching values alongside their indexes, and `LIMIT` to cap the number of matches.

This is particularly useful when an array stores line-indexed text such as a log file, where each element holds one line:

Find elements matching textual predicates (EXACT, MATCH, GLOB, RE) with ARGREP, combined with AND or OR

**Commands:** DEL, ARMSET, ARGREP

**Complexity:**
- DEL: O(N)
- ARMSET: O(N)
- ARGREP: O(P * C)

**Available in:** Redis CLI, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), JavaScript (Node.js), PHP, Python

##### Redis CLI

```
> DEL log
(integer) 1
> ARMSET log 0 "boot: ok" 1 "warn: disk" 2 "ERROR: cpu" 3 "info: ready" 4 "error: net"
(integer) 5
> ARGREP log - + MATCH "error" NOCASE
1) (integer) 2
2) (integer) 4
> ARGREP log 0 4 GLOB "warn:*" OR GLOB "error:*" WITHVALUES
1) 1) (integer) 1
   2) "warn: disk"
2) 1) (integer) 4
   2) "error: net"
```

##### Go

```go
	msetRes, err := rdb.ARMSet(ctx, "log",
		redis.AREntry{Index: 0, Value: "boot: ok"},
		redis.AREntry{Index: 1, Value: "warn: disk"},
		redis.AREntry{Index: 2, Value: "ERROR: cpu"},
		redis.AREntry{Index: 3, Value: "info: ready"},
		redis.AREntry{Index: 4, Value: "error: net"},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(msetRes) // >>> 5

	// Case-insensitive match for "error".
	grepRes, err := rdb.ARGrep(ctx, "log", "0", "4", &redis.ARGrepArgs{
		Predicates: []redis.ARGrepPredicate{
			{Type: redis.ARGrepMatch, Value: "error"},
		},
		NoCase: true,
	}).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(grepRes) // >>> [2 4]

	// Two GLOB predicates combined with the default OR, returning values too.
	grepValsRes, err := rdb.ARGrepWithValues(ctx, "log", "0", "4", &redis.ARGrepArgs{
		Predicates: []redis.ARGrepPredicate{
			{Type: redis.ARGrepGlob, Value: "warn:*"},
			{Type: redis.ARGrepGlob, Value: "error:*"},
		},
	}).Result()

	if err != nil {
		panic(err)
	}

	for _, entry := range grepValsRes {
		fmt.Printf("%d -> %s\n", entry.Index, entry.Value)
	}
	// >>> 1 -> warn: disk
	// >>> 4 -> error: net
```

##### Java (Asynchronous - Lettuce)

```java
            Map<Long, String> argrepLog = new HashMap<>();
            argrepLog.put(0L, "boot: ok");
            argrepLog.put(1L, "warn: disk");
            argrepLog.put(2L, "ERROR: cpu");
            argrepLog.put(3L, "info: ready");
            argrepLog.put(4L, "error: net");

            CompletableFuture<Void> argrepExample = asyncCommands
                    .armset("log", argrepLog)
                    .thenCompose(res1 -> {
                        System.out.println(res1);
                        // >>> 5
                        return asyncCommands.argrep("log",
                                ArGrepArgs.range(0, 4).match("error").nocase());
                    })
                    .thenCompose(res2 -> {
                        System.out.println(res2);
                        // >>> [2, 4]
                        return asyncCommands.argrepWithValues("log",
                                ArGrepArgs.range(0, 4).glob("warn:*").glob("error:*"));
                    })
                    .thenAccept(res3 -> {
                        for (IndexedValue<String> pair : res3) {
                            System.out.println(pair.getIndex() + " -> " + pair.getValue());
                        }
                        // >>> 1 -> warn: disk
                        // >>> 4 -> error: net
                    })
                    .toCompletableFuture();

            argrepExample.join();
```

##### Java (Reactive - Lettuce)

```java
            Map<Long, String> argrepParams = new HashMap<>();
            argrepParams.put(0L, "boot: ok");
            argrepParams.put(1L, "warn: disk");
            argrepParams.put(2L, "ERROR: cpu");
            argrepParams.put(3L, "info: ready");
            argrepParams.put(4L, "error: net");

            Mono<Long> argrep1 = reactiveCommands.armset("log", argrepParams).doOnNext(result -> {
                System.out.println(result); // >>> 5
            });

            argrep1.block();

            Mono<List<Long>> argrep2 = reactiveCommands.argrep("log", ArGrepArgs.range(0, 4).match("error").nocase())
                    .collectList()
                    .doOnNext(result -> {
                        System.out.println(result); // >>> [2, 4]
                    });

            argrep2.block();

            Mono<List<IndexedValue<String>>> argrep3 = reactiveCommands
                    .argrepWithValues("log", ArGrepArgs.range(0, 4).glob("warn:*").glob("error:*"))
                    .doOnNext(entry -> {
                        System.out.println(entry.getIndex() + " -> " + entry.getValue());
                        // >>> 1 -> warn: disk
                        // >>> 4 -> error: net
                    })
                    .collectList()
            ;

            argrep3.block();
```

##### JavaScript (Node.js)

```javascript
const grepSetResult = await client.arMSet('log', {
  0: 'boot: ok',
  1: 'warn: disk',
  2: 'ERROR: cpu',
  3: 'info: ready',
  4: 'error: net'
});
console.log(grepSetResult); // >>> 5

const grepResult = await client.arGrep(
  'log',
  0,
  4,
  [['MATCH', 'error']],
  { NOCASE: true }
);
console.log(grepResult); // >>> [ 2, 4 ]

const grepWithValues = await client.arGrepWithValues(
  'log',
  0,
  4,
  [['GLOB', 'warn:*'], ['GLOB', 'error:*']],
  { COMBINATOR: 'OR' }
);
for (const { index, value } of grepWithValues) {
  console.log(`${index} -> ${value}`);
}
// >>> 1 -> warn: disk
// >>> 4 -> error: net
```

##### PHP

```php
        $res1 = $redis->armset('log', [
            0 => 'boot: ok',
            1 => 'warn: disk',
            2 => 'ERROR: cpu',
            3 => 'info: ready',
            4 => 'error: net',
        ]);
        echo $res1 . PHP_EOL; // >>> 5

        // Predicates are [type, value] pairs. Positional argument order is:
        // (key, start, end, predicates, combinator, limit, withValues, noCase)
        $res2 = $redis->argrep('log', 0, 4, [['MATCH', 'error']], null, null, false, true);
        echo json_encode($res2) . PHP_EOL; // >>> [2,4]

        $res3 = $redis->argrep(
            'log',
            0,
            4,
            [['GLOB', 'warn:*'], ['GLOB', 'error:*']],
            'OR',
            null,
            true
        );
        foreach ($res3 as $pair) {
            echo $pair[0] . ' -> ' . $pair[1] . PHP_EOL;
        }
        // >>> 1 -> warn: disk
        // >>> 4 -> error: net
```

##### Python

```python
res30 = r.armset(
    "log",
    {
        0: "boot: ok",
        1: "warn: disk",
        2: "ERROR: cpu",
        3: "info: ready",
        4: "error: net",
    },
)
print(res30)
# >>> 5

res31 = r.argrep(
    "log",
    0,
    4,
    [(ArrayPredicateType.MATCH, "error")],
    nocase=True,
)
print(res31)
# >>> [2, 4]

res32 = r.argrep(
    "log",
    0,
    4,
    [
        (ArrayPredicateType.GLOB, "warn:*"),
        (ArrayPredicateType.GLOB, "error:*"),
    ],
    combinator=ArrayPredicateCombinator.OR,
    withvalues=True,
)
print(res32)
# >>> [[1, 'warn: disk'], [4, 'error: net']]
```



The special values `-` and `+` denote the first and last index of the array. Combined with [ring buffer mode](#ring-buffer-mode), this lets a fixed-size array hold the most recent *N* log lines and be searched in place.

## Deleting elements

[`ARDEL`](https://redis.io/docs/latest/commands/ardel) deletes one or more elements by index and returns the count of elements actually removed. [`ARDELRANGE`](https://redis.io/docs/latest/commands/ardelrange) removes all elements within an index range; reversing `start` and `end` is supported:

Delete elements by index with ARDEL or remove a whole index range with ARDELRANGE

**Builds upon:** arop

**Commands:** ARDEL, ARDELRANGE

**Complexity:**
- ARDEL: O(N)

**Available in:** Redis CLI, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), JavaScript (Node.js), PHP, Python

##### Redis CLI

```
> ARDEL scores 1
(integer) 1
> ARDELRANGE scores 0 2
(integer) 2
```

##### Go

```go
	msetRes, err := rdb.ARMSet(ctx, "scores",
		redis.AREntry{Index: 0, Value: "10"},
		redis.AREntry{Index: 1, Value: "20"},
		redis.AREntry{Index: 2, Value: "30"},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(msetRes) // >>> 3

	delRes, err := rdb.ARDel(ctx, "scores", 1).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(delRes) // >>> 1

	delRangeRes, err := rdb.ARDelRange(ctx, "scores", redis.ARRange{Start: 0, End: 2}).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(delRangeRes) // >>> 2
```

##### Java (Asynchronous - Lettuce)

```java
            Map<Long, String> ardelScores = new HashMap<>();
            ardelScores.put(0L, "10");
            ardelScores.put(1L, "20");
            ardelScores.put(2L, "30");

            CompletableFuture<Void> ardelExample = asyncCommands
                    .armset("scores", ardelScores)
                    .thenCompose(res1 -> {
                        System.out.println(res1);
                        // >>> 3
                        return asyncCommands.ardel("scores", 1);
                    })
                    .thenCompose(res2 -> {
                        System.out.println(res2);
                        // >>> 1
                        return asyncCommands.ardelrange("scores", 0, 2);
                    })
                    .thenAccept(res3 -> {
                        System.out.println(res3);
                        // >>> 2
                    })
                    .toCompletableFuture();

            ardelExample.join();
```

##### Java (Reactive - Lettuce)

```java
            Map<Long, String> ardelParams = new HashMap<>();
            ardelParams.put(0L, "10");
            ardelParams.put(1L, "20");
            ardelParams.put(2L, "30");

            Mono<Long> ardel1 = reactiveCommands.armset("scores", ardelParams).doOnNext(result -> {
                System.out.println(result); // >>> 3
            });

            ardel1.block();

            Mono<Long> ardel2 = reactiveCommands.ardel("scores", 1).doOnNext(result -> {
                System.out.println(result); // >>> 1
            });

            ardel2.block();

            Mono<Long> ardel3 = reactiveCommands.ardelrange("scores", 0, 2).doOnNext(result -> {
                System.out.println(result); // >>> 2
            });

            ardel3.block();
```

##### JavaScript (Node.js)

```javascript
const delSetResult = await client.arMSet('scores', { 0: '10', 1: '20', 2: '30' });
console.log(delSetResult); // >>> 3

const delResult = await client.arDel('scores', 1);
console.log(delResult); // >>> 1

const delRangeResult = await client.arDelRange('scores', [[0, 2]]);
console.log(delRangeResult); // >>> 2
```

##### PHP

```php
        $res1 = $redis->armset('scores', [0 => '10', 1 => '20', 2 => '30']);
        echo $res1 . PHP_EOL; // >>> 3

        $res2 = $redis->ardel('scores', 1);
        echo $res2 . PHP_EOL; // >>> 1

        $res3 = $redis->ardelrange('scores', 0, 2);
        echo $res3 . PHP_EOL; // >>> 2
```

##### Python

```python
res33 = r.armset("scores", {0: "10", 1: "20", 2: "30"})
print(res33)
# >>> 3

res34 = r.ardel("scores", 1)
print(res34)
# >>> 1

res35 = r.ardelrange("scores", (0, 2))
print(res35)
# >>> 2
```



Deleting the last remaining element removes the key entirely.

## Introspection

[`ARINFO`](https://redis.io/docs/latest/commands/arinfo) returns metadata about an array's internal structure, including its logical length, element count, and next insert index. Pass the `FULL` option to include per-slice statistics such as fill rates and counts of dense versus sparse slices:

```
> ARINFO readings
 1) "len"
 2) (integer) 3
 3) "count"
 4) (integer) 3
 5) "next-insert-index"
 6) (integer) 0
...
```

## Configuration

The following configuration parameters affect array behavior:
- `array-slice-size`
- `array-sparse-kmax`
- `array-sparse-kmin`

See the [Redis configuration page](https://redis.io/docs/latest/operate/oss_and_stack/management/config) for details.

## Performance

Most array commands are O(1), including [`ARSET`](https://redis.io/docs/latest/commands/arset), [`ARGET`](https://redis.io/docs/latest/commands/arget), [`ARDEL`](https://redis.io/docs/latest/commands/ardel), [`ARINSERT`](https://redis.io/docs/latest/commands/arinsert), [`ARNEXT`](https://redis.io/docs/latest/commands/arnext), [`ARSEEK`](https://redis.io/docs/latest/commands/arseek), [`ARCOUNT`](https://redis.io/docs/latest/commands/arcount), and [`ARLEN`](https://redis.io/docs/latest/commands/arlen). Operations that touch N elements—such as [`ARGETRANGE`](https://redis.io/docs/latest/commands/argetrange), [`ARSCAN`](https://redis.io/docs/latest/commands/arscan), [`ARDELRANGE`](https://redis.io/docs/latest/commands/ardelrange), [`AROP`](https://redis.io/docs/latest/commands/arop), and [`ARLASTITEMS`](https://redis.io/docs/latest/commands/arlastitems)—are O(N). The underlying sliced-array encoding handles both dense and sparse access patterns efficiently, so large index gaps consume very little memory.

## Alternatives

Arrays complement rather than replace the other Redis collection types:

- Use [Redis lists](https://redis.io/docs/latest/develop/data-types/lists) when you need push/pop operations at either end, or when you need to insert elements between existing ones.
- Use [Redis hashes](https://redis.io/docs/latest/develop/data-types/hashes) when values are addressed by field name rather than by numeric index.
- Use [Redis streams](https://redis.io/docs/latest/develop/data-types/streams) when you need an append-only event log with consumer groups and acknowledgements.

## Limits

[`ARGETRANGE`](https://redis.io/docs/latest/commands/argetrange) enforces a hard limit of 1,000,000 elements per call to guard against accidentally large range reads.

