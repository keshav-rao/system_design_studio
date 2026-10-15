# Redis vector sets

```json metadata
{
  "schema_version": 2,
  "title": "Redis vector sets",
  "description": "Introduction to Redis vector sets",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"endianness-considerations-for-fp32-format","title":"Endianness considerations for FP32 format"},{"children":[{"id":"basic-operations","title":"Basic operations"},{"id":"vector-similarity-search","title":"Vector similarity search"}],"id":"examples","title":"Examples"},{"id":"more-information","title":"More information"}]}

,
  "codeExamples": [{"codetabsId":"vecset_tutorial-stepvadd","commands":[{"name":"VADD"},{"acl_categories":["@keyspace","@read","@fast"],"complexity":"O(1)","name":"TYPE"}],"description":"Foundational: Use VADD to create a new vector set and populate it with vectors","difficulty":"beginner","id":"vadd","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_vecset_tutorial-stepvadd"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_vecset_tutorial-stepvadd"},{"id":"Node-js","panelId":"panel_Nodejs_vecset_tutorial-stepvadd"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_vecset_tutorial-stepvadd"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_vecset_tutorial-stepvadd"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_vecset_tutorial-stepvadd"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_vecset_tutorial-stepvadd"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_vecset_tutorial-stepvadd"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_vecset_tutorial-stepvadd"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_vecset_tutorial-stepvadd"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_vecset_tutorial-stepvadd"}]},{"buildsUpon":["vadd"],"codetabsId":"vecset_tutorial-stepvcardvdim","commands":[{"name":"VCARD"},{"name":"VDIM"}],"description":"Metadata retrieval: Use VCARD to get the number of elements and VDIM to get vector dimensions when you need to inspect vector set properties","difficulty":"beginner","id":"vcardvdim","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_vecset_tutorial-stepvcardvdim"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_vecset_tutorial-stepvcardvdim"},{"id":"Node-js","panelId":"panel_Nodejs_vecset_tutorial-stepvcardvdim"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_vecset_tutorial-stepvcardvdim"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_vecset_tutorial-stepvcardvdim"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_vecset_tutorial-stepvcardvdim"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_vecset_tutorial-stepvcardvdim"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_vecset_tutorial-stepvcardvdim"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_vecset_tutorial-stepvcardvdim"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_vecset_tutorial-stepvcardvdim"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_vecset_tutorial-stepvcardvdim"}]},{"buildsUpon":["vadd"],"codetabsId":"vecset_tutorial-stepvemb","commands":[{"name":"VEMB"}],"description":"Vector retrieval: Use VEMB to retrieve the approximate vector values of elements when you need to inspect the actual vector data stored in the set","difficulty":"beginner","id":"vemb","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_vecset_tutorial-stepvemb"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_vecset_tutorial-stepvemb"},{"id":"Node-js","panelId":"panel_Nodejs_vecset_tutorial-stepvemb"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_vecset_tutorial-stepvemb"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_vecset_tutorial-stepvemb"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_vecset_tutorial-stepvemb"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_vecset_tutorial-stepvemb"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_vecset_tutorial-stepvemb"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_vecset_tutorial-stepvemb"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_vecset_tutorial-stepvemb"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_vecset_tutorial-stepvemb"}]},{"buildsUpon":["vadd"],"codetabsId":"vecset_tutorial-stepvrem","commands":[{"name":"VADD"},{"name":"VCARD"},{"name":"VREM"}],"description":"Element removal: Use VREM to delete elements from a vector set when you need to remove vectors from the collection","difficulty":"beginner","id":"vrem","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_vecset_tutorial-stepvrem"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_vecset_tutorial-stepvrem"},{"id":"Node-js","panelId":"panel_Nodejs_vecset_tutorial-stepvrem"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_vecset_tutorial-stepvrem"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_vecset_tutorial-stepvrem"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_vecset_tutorial-stepvrem"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_vecset_tutorial-stepvrem"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_vecset_tutorial-stepvrem"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_vecset_tutorial-stepvrem"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_vecset_tutorial-stepvrem"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_vecset_tutorial-stepvrem"}]},{"buildsUpon":["vadd"],"codetabsId":"vecset_tutorial-stepattr","commands":[{"name":"VSETATTR"},{"name":"VGETATTR"}],"description":"Attribute management: Use VSETATTR to store JSON attributes on elements and VGETATTR to retrieve them when you need to associate metadata with vectors","difficulty":"beginner","id":"attr","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_vecset_tutorial-stepattr"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_vecset_tutorial-stepattr"},{"id":"Node-js","panelId":"panel_Nodejs_vecset_tutorial-stepattr"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_vecset_tutorial-stepattr"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_vecset_tutorial-stepattr"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_vecset_tutorial-stepattr"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_vecset_tutorial-stepattr"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_vecset_tutorial-stepattr"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_vecset_tutorial-stepattr"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_vecset_tutorial-stepattr"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_vecset_tutorial-stepattr"}]},{"buildsUpon":["vadd"],"codetabsId":"vecset_tutorial-stepvsim_basic","commands":[{"name":"VSIM"}],"description":"Similarity search: Use VSIM to find elements most similar to a query vector when you need to perform vector similarity searches","difficulty":"intermediate","id":"vsim_basic","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_vecset_tutorial-stepvsim_basic"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_vecset_tutorial-stepvsim_basic"},{"id":"Node-js","panelId":"panel_Nodejs_vecset_tutorial-stepvsim_basic"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_vecset_tutorial-stepvsim_basic"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_vecset_tutorial-stepvsim_basic"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_vecset_tutorial-stepvsim_basic"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_vecset_tutorial-stepvsim_basic"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_vecset_tutorial-stepvsim_basic"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_vecset_tutorial-stepvsim_basic"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_vecset_tutorial-stepvsim_basic"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_vecset_tutorial-stepvsim_basic"}]},{"buildsUpon":["vadd"],"codetabsId":"vecset_tutorial-stepvsim_options","commands":[{"name":"VSIM"}],"description":"Similarity with options: Use VSIM with ELE, WITHSCORES, and COUNT options to find similar elements with scores and limits when you need detailed similarity results","difficulty":"intermediate","id":"vsim_options","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_vecset_tutorial-stepvsim_options"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_vecset_tutorial-stepvsim_options"},{"id":"Node-js","panelId":"panel_Nodejs_vecset_tutorial-stepvsim_options"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_vecset_tutorial-stepvsim_options"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_vecset_tutorial-stepvsim_options"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_vecset_tutorial-stepvsim_options"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_vecset_tutorial-stepvsim_options"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_vecset_tutorial-stepvsim_options"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_vecset_tutorial-stepvsim_options"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_vecset_tutorial-stepvsim_options"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_vecset_tutorial-stepvsim_options"}]},{"buildsUpon":["vadd"],"codetabsId":"vecset_tutorial-stepvsim_filter","commands":[{"name":"VSETATTR"},{"name":"VSIM"}],"description":"Filtered similarity search: Use VSIM with FILTER option to apply attribute-based conditions to similarity results when you need to combine vector similarity with attribute filtering","difficulty":"advanced","id":"vsim_filter","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_vecset_tutorial-stepvsim_filter"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_vecset_tutorial-stepvsim_filter"},{"id":"Node-js","panelId":"panel_Nodejs_vecset_tutorial-stepvsim_filter"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_vecset_tutorial-stepvsim_filter"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_vecset_tutorial-stepvsim_filter"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_vecset_tutorial-stepvsim_filter"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_vecset_tutorial-stepvsim_filter"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_vecset_tutorial-stepvsim_filter"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_vecset_tutorial-stepvsim_filter"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_vecset_tutorial-stepvsim_filter"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_vecset_tutorial-stepvsim_filter"}]}]
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


### Vector set command summary

**13 commands in this group:**

[View all vector_set commands](https://redis.io/commands/?group=vector_set)

| Command | Summary | Complexity | Since |
|---------|---------|------------|-------|
| [VADD](https://redis.io/commands/vadd/) | Add one or more elements to a vector set, or update its vector if it already exists | N/A | 8.0.0 |
| [VCARD](https://redis.io/commands/vcard/) | Return the number of elements in a vector set | N/A | 8.0.0 |
| [VDIM](https://redis.io/commands/vdim/) | Return the dimension of vectors in the vector set | N/A | 8.0.0 |
| [VEMB](https://redis.io/commands/vemb/) | Return the vector associated with an element | N/A | 8.0.0 |
| [VGETATTR](https://redis.io/commands/vgetattr/) | Retrieve the JSON attributes of elements | N/A | 8.0.0 |
| [VINFO](https://redis.io/commands/vinfo/) | Return information about a vector set | N/A | 8.0.0 |
| [VISMEMBER](https://redis.io/commands/vismember/) | Check if an element exists in a vector set | N/A | 8.2.0 |
| [VLINKS](https://redis.io/commands/vlinks/) | Return the neighbors of an element at each layer in the HNSW graph | N/A | 8.0.0 |
| [VRANDMEMBER](https://redis.io/commands/vrandmember/) | Return one or multiple random members from a vector set | N/A | 8.0.0 |
| [VRANGE](https://redis.io/commands/vrange/) | Return vector set elements in a lex range | N/A | 8.4.0 |

#### Vector set command summary (part 2)

| Command | Summary | Complexity | Since |
|---------|---------|------------|-------|
| [VREM](https://redis.io/commands/vrem/) | Remove an element from a vector set | N/A | 8.0.0 |
| [VSETATTR](https://redis.io/commands/vsetattr/) | Associate or remove the JSON attributes of elements | N/A | 8.0.0 |
| [VSIM](https://redis.io/commands/vsim/) | Return elements by vector similarity | N/A | 8.0.0 |



Vector sets are a data type similar to sorted sets, but instead of a score, vector set elements have a string representation of a vector.
Vector sets allow you to add items to a set, and then either:

* retrieve a subset of items that are the most similar to a specified vector, or
* retrieve a subset of items that are the most similar to the vector of an element that is already part of the vector set.

Vector sets also provide for optional [filtered search](https://redis.io/docs/latest/develop/data-types/vector-sets/filtered-search). You can associate attributes with all or some elements in a vector set, and then use the `FILTER` option of the [`VSIM`](https://redis.io/docs/latest/commands/vsim) command to retrieve items similar to a given vector while applying simple mathematical filters to those attributes. Here's a sample filter: `".year > 1950"`.

## Endianness considerations for FP32 format

When using the FP32 blob format with vector set commands like [`VADD`](https://redis.io/docs/latest/commands/vadd) and [`VSIM`](https://redis.io/docs/latest/commands/vsim), the binary data must be encoded in little-endian byte order. This is important for cross-platform compatibility, as some ARM variants and other architectures may use different endianness.

If your platform uses big-endian or mixed-endian encoding, you have two options:
- Manually convert the byte order to little-endian before passing the blob to Redis.
- Use the `VALUES` syntax instead, which accepts floating-point numbers as strings and is platform-independent.

## Examples

The following examples give an overview of how to use vector sets. For clarity,
we will use a set of two-dimensional vectors that represent points in the
Cartesian coordinate plane. However, in real use cases, the vectors will typically
represent *text embeddings* and have hundreds of dimensions. See
[Redis for AI](https://redis.io/docs/latest/develop/ai) for more information about using text
embeddings.

The points we will use are A: (1.0, 1.0), B: (-1.0, -1.0), C: (-1.0, 1.0), D: (1.0. -1.0), and
E: (1.0, 0), shown in the diagram below.

![Example points on the coordinate plane.](https://redis.io/docs/latest/images/vecsets/VecSetExamplePoints.drawio.svg)

### Basic operations

Start by adding the point vectors to a set called `points` using
[`VADD`](https://redis.io/docs/latest/commands/vadd). This also creates the vector set object.
The [`TYPE`](https://redis.io/docs/latest/commands/type) command returns a type of `vectorset`
for this object.

Foundational: Use VADD to create a new vector set and populate it with vectors

**Commands:** VADD, TYPE

**Complexity:**
- TYPE: O(1)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> VADD points VALUES 2 1.0 1.0 pt:A
(integer) 1
> VADD points VALUES 2 -1.0 -1.0 pt:B
(integer) 1
> VADD points VALUES 2 -1.0 1.0 pt:C
(integer) 1
> VADD points VALUES 2 1.0 -1.0 pt:D
(integer) 1
> VADD points VALUES 2 1.0 0 pt:E
(integer) 1
> TYPE points
vectorset
```

##### C#

```csharp
        bool r1 = db.VectorSetAdd("points", VectorSetAddRequest.Member("pt:A", new float[] { 1f, 1f }, null));
        Console.WriteLine(r1); // >>> True

        bool r2 = db.VectorSetAdd("points", VectorSetAddRequest.Member("pt:B", new float[] { -1f, -1f }, null));
        Console.WriteLine(r2); // >>> True

        bool r3 = db.VectorSetAdd("points", VectorSetAddRequest.Member("pt:C", new float[] { -1f, 1f }, null));
        Console.WriteLine(r3); // >>> True

        bool r4 = db.VectorSetAdd("points", VectorSetAddRequest.Member("pt:D", new float[] { 1f, -1f }, null));
        Console.WriteLine(r4); // >>> True

        bool r5 = db.VectorSetAdd("points", VectorSetAddRequest.Member("pt:E", new float[] { 1f, 0f }, null));
        Console.WriteLine(r5); // >>> True
```

##### Go

```go
	res1, err := rdb.VAdd(ctx, "points", "pt:A",
		&redis.VectorValues{Val: []float64{1.0, 1.0}},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // >>> true

	res2, err := rdb.VAdd(ctx, "points", "pt:B",
		&redis.VectorValues{Val: []float64{-1.0, -1.0}},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2) // >>> true

	res3, err := rdb.VAdd(ctx, "points", "pt:C",
		&redis.VectorValues{Val: []float64{-1.0, 1.0}},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3) // >>> true

	res4, err := rdb.VAdd(ctx, "points", "pt:D",
		&redis.VectorValues{Val: []float64{1.0, -1.0}},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4) // >>> true

	res5, err := rdb.VAdd(ctx, "points", "pt:E",
		&redis.VectorValues{Val: []float64{1.0, 0.0}},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res5) // >>> true

	res6, err := rdb.Type(ctx, "points").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res6) // >>> vectorset
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Boolean> addPointA = asyncCommands.vadd("points", "pt:A", 1.0, 1.0).thenApply(result -> {
                System.out.println(result); // >>> true
                return result;
            }).toCompletableFuture();

            CompletableFuture<Boolean> addPointB = asyncCommands.vadd("points", "pt:B", -1.0, -1.0).thenApply(result -> {
                System.out.println(result); // >>> true
                return result;
            }).toCompletableFuture();

            CompletableFuture<Boolean> addPointC = asyncCommands.vadd("points", "pt:C", -1.0, 1.0).thenApply(result -> {
                System.out.println(result); // >>> true
                return result;
            }).toCompletableFuture();

            CompletableFuture<Boolean> addPointD = asyncCommands.vadd("points", "pt:D", 1.0, -1.0).thenApply(result -> {
                System.out.println(result); // >>> true
                return result;
            }).toCompletableFuture();

            CompletableFuture<Boolean> addPointE = asyncCommands.vadd("points", "pt:E", 1.0, 0.0).thenApply(result -> {
                System.out.println(result); // >>> true
                return result;
            }).toCompletableFuture();

            // Chain checkDataType after all vadd operations complete
            CompletableFuture<Void> vaddOperations = CompletableFuture
                    .allOf(addPointA, addPointB, addPointC, addPointD, addPointE)
                    .thenCompose(ignored -> asyncCommands.type("points")).thenAccept(result -> {
                        System.out.println(result); // >>> vectorset
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Boolean> addPointA = reactiveCommands.vadd("points", "pt:A", 1.0, 1.0).doOnNext(result -> {
                System.out.println(result); // >>> true
            });

            Mono<Boolean> addPointB = reactiveCommands.vadd("points", "pt:B", -1.0, -1.0).doOnNext(result -> {
                System.out.println(result); // >>> true
            });

            Mono<Boolean> addPointC = reactiveCommands.vadd("points", "pt:C", -1.0, 1.0).doOnNext(result -> {
                System.out.println(result); // >>> true
            });

            Mono<Boolean> addPointD = reactiveCommands.vadd("points", "pt:D", 1.0, -1.0).doOnNext(result -> {
                System.out.println(result); // >>> true
            });

            Mono<Boolean> addPointE = reactiveCommands.vadd("points", "pt:E", 1.0, 0.0).doOnNext(result -> {
                System.out.println(result); // >>> true
            });

            Mono<Void> vaddOperations = Mono.when(addPointA, addPointB, addPointC, addPointD, addPointE)
                    .then(reactiveCommands.type("points")).doOnNext(result -> {
                        System.out.println(result); // >>> vectorset
                    }).then();
```

##### Java (Synchronous - Jedis)

```java
      boolean res1 = jedis.vadd("points", new float[] { 1.0f, 1.0f }, "pt:A");
      System.out.println(res1); // >>> true

      boolean res2 = jedis.vadd("points", new float[] { -1.0f, -1.0f }, "pt:B");
      System.out.println(res2); // >>> true

      boolean res3 = jedis.vadd("points", new float[] { -1.0f, 1.0f }, "pt:C");
      System.out.println(res3); // >>> true

      boolean res4 = jedis.vadd("points", new float[] { 1.0f, -1.0f }, "pt:D");
      System.out.println(res4); // >>> true

      boolean res5 = jedis.vadd("points", new float[] { 1.0f, 0.0f }, "pt:E");
      System.out.println(res5); // >>> true

      String res6 = jedis.type("points");
      System.out.println(res6); // >>> vectorset
```

##### JavaScript (Node.js)

```javascript
const res1 = await client.vAdd("points", [1.0, 1.0], "pt:A");
console.log(res1);  // >>> true

const res2 = await client.vAdd("points", [-1.0, -1.0], "pt:B");
console.log(res2);  // >>> true

const res3 = await client.vAdd("points", [-1.0, 1.0], "pt:C");
console.log(res3);  // >>> true

const res4 = await client.vAdd("points", [1.0, -1.0], "pt:D");
console.log(res4);  // >>> true

const res5 = await client.vAdd("points", [1.0, 0], "pt:E");
console.log(res5);  // >>> true

const res6 = await client.type("points");
console.log(res6);  // >>> vectorset
```

##### PHP

```php
        $res1 = $r->vadd('points', [1.0, 1.0], 'pt:A');
        echo $res1 . PHP_EOL;
        // >>> 1

        $res2 = $r->vadd('points', [-1.0, -1.0], 'pt:B');
        echo $res2 . PHP_EOL;
        // >>> 1

        $res3 = $r->vadd('points', [-1.0, 1.0], 'pt:C');
        echo $res3 . PHP_EOL;
        // >>> 1

        $res4 = $r->vadd('points', [1.0, -1.0], 'pt:D');
        echo $res4 . PHP_EOL;
        // >>> 1

        $res5 = $r->vadd('points', [1.0, 0.0], 'pt:E');
        echo $res5 . PHP_EOL;
        // >>> 1

        $res6 = $r->type('points');
        echo $res6 . PHP_EOL;
        // >>> vectorset
```

##### Python

```python
res1 = r.vset().vadd("points", [1.0, 1.0], "pt:A")
print(res1)  # >>> 1

res2 = r.vset().vadd("points", [-1.0, -1.0], "pt:B")
print(res2)  # >>> 1

res3 = r.vset().vadd("points", [-1.0, 1.0], "pt:C")
print(res3)  # >>> 1

res4 = r.vset().vadd("points", [1.0, -1.0], "pt:D")
print(res4)  # >>> 1

res5 = r.vset().vadd("points", [1.0, 0], "pt:E")
print(res5)  # >>> 1

res6 = r.type("points")
print(res6)  # >>> vectorset
```

##### Rust (Asynchronous)

```rust
        if let Ok(res) = r
            .vadd(
                "points",
                VectorAddInput::Values(EmbeddingInput::Float64(&[1.0, 1.0])),
                "pt:A",
            )
            .await
        {
            let res: bool = res;
            println!("{res}"); // >>> true
        }

        if let Ok(res) = r
            .vadd(
                "points",
                VectorAddInput::Values(EmbeddingInput::Float64(&[-1.0, -1.0])),
                "pt:B",
            )
            .await
        {
            let res: bool = res;
            println!("{res}"); // >>> true
        }

        if let Ok(res) = r
            .vadd(
                "points",
                VectorAddInput::Values(EmbeddingInput::Float64(&[-1.0, 1.0])),
                "pt:C",
            )
            .await
        {
            let res: bool = res;
            println!("{res}"); // >>> true
        }

        if let Ok(res) = r
            .vadd(
                "points",
                VectorAddInput::Values(EmbeddingInput::Float64(&[1.0, -1.0])),
                "pt:D",
            )
            .await
        {
            let res: bool = res;
            println!("{res}"); // >>> true
        }

        if let Ok(res) = r
            .vadd(
                "points",
                VectorAddInput::Values(EmbeddingInput::Float64(&[1.0, 0.0])),
                "pt:E",
            )
            .await
        {
            let res: bool = res;
            println!("{res}"); // >>> true
        }

        let res: String = cmd("TYPE")
            .arg("points")
            .query_async(&mut r)
            .await
            .expect("TYPE points should succeed");
        println!("{res}"); // >>> vectorset
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.vadd(
            "points",
            VectorAddInput::Values(EmbeddingInput::Float64(&[1.0, 1.0])),
            "pt:A",
        ) {
            let res: bool = res;
            println!("{res}"); // >>> true
        }

        if let Ok(res) = r.vadd(
            "points",
            VectorAddInput::Values(EmbeddingInput::Float64(&[-1.0, -1.0])),
            "pt:B",
        ) {
            let res: bool = res;
            println!("{res}"); // >>> true
        }

        if let Ok(res) = r.vadd(
            "points",
            VectorAddInput::Values(EmbeddingInput::Float64(&[-1.0, 1.0])),
            "pt:C",
        ) {
            let res: bool = res;
            println!("{res}"); // >>> true
        }

        if let Ok(res) = r.vadd(
            "points",
            VectorAddInput::Values(EmbeddingInput::Float64(&[1.0, -1.0])),
            "pt:D",
        ) {
            let res: bool = res;
            println!("{res}"); // >>> true
        }

        if let Ok(res) = r.vadd(
            "points",
            VectorAddInput::Values(EmbeddingInput::Float64(&[1.0, 0.0])),
            "pt:E",
        ) {
            let res: bool = res;
            println!("{res}"); // >>> true
        }

        let res: String = cmd("TYPE")
            .arg("points")
            .query(&mut r)
            .expect("TYPE points should succeed");
        println!("{res}"); // >>> vectorset
```




Get the number of elements in the set (also known as the *cardinality* of the set)
using [`VCARD`](https://redis.io/docs/latest/commands/vcard) and the number of dimensions of
the vectors using [`VDIM`](https://redis.io/docs/latest/commands/vdim):

Metadata retrieval: Use VCARD to get the number of elements and VDIM to get vector dimensions when you need to inspect vector set properties

**Builds upon:** vadd

**Commands:** VCARD, VDIM

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> VCARD points
(integer) 5
> VDIM points
(integer) 2
```

##### C#

```csharp
        long card = db.VectorSetLength("points");
        Console.WriteLine(card); // >>> 5

        int dim = db.VectorSetDimension("points");
        Console.WriteLine(dim); // >>> 2
```

##### Go

```go
	res7, err := rdb.VCard(ctx, "points").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res7) // >>> 5

	res8, err := rdb.VDim(ctx, "points").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res8) // >>> 2
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> getCardinality = asyncCommands.vcard("points").thenAccept(result -> {
                System.out.println(result); // >>> 5
            }).toCompletableFuture();

            CompletableFuture<Void> getDimensions = asyncCommands.vdim("points").thenAccept(result -> {
                System.out.println(result); // >>> 2
            }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Long> getCardinality = reactiveCommands.vcard("points").doOnNext(result -> {
                System.out.println(result); // >>> 5
            });

            Mono<Long> getDimensions = reactiveCommands.vdim("points").doOnNext(result -> {
                System.out.println(result); // >>> 2
            });
```

##### Java (Synchronous - Jedis)

```java
      long res7 = jedis.vcard("points");
      System.out.println(res7); // >>> 5

      long res8 = jedis.vdim("points");
      System.out.println(res8); // >>> 2
```

##### JavaScript (Node.js)

```javascript
const res7 = await client.vCard("points");
console.log(res7);  // >>> 5

const res8 = await client.vDim("points");
console.log(res8);  // >>> 2
```

##### PHP

```php
        $res7 = $r->vcard('points');
        echo $res7 . PHP_EOL;
        // >>> 5

        $res8 = $r->vdim('points');
        echo $res8 . PHP_EOL;
        // >>> 2
```

##### Python

```python
res7 = r.vset().vcard("points")
print(res7)  # >>> 5

res8 = r.vset().vdim("points")
print(res8)  # >>> 2
```

##### Rust (Asynchronous)

```rust
        if let Ok(res) = r.vcard("points").await {
            let res: usize = res;
            println!("{res}"); // >>> 5
        }

        if let Ok(res) = r.vdim("points").await {
            let res: usize = res;
            println!("{res}"); // >>> 2
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.vcard("points") {
            let res: usize = res;
            println!("{res}"); // >>> 5
        }

        if let Ok(res) = r.vdim("points") {
            let res: usize = res;
            println!("{res}"); // >>> 2
        }
```



Get the coordinate values from the elements using [`VEMB`](https://redis.io/docs/latest/commands/vemb).
Note that the values will not typically be the exact values you supplied when you added
the vector because
[quantization](https://redis.io/docs/latest/develop/data-types/vector-sets/performance#quantization-effects)
is applied to improve performance.

Vector retrieval: Use VEMB to retrieve the approximate vector values of elements when you need to inspect the actual vector data stored in the set

**Builds upon:** vadd

**Commands:** VEMB

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> VEMB points pt:A
1) "0.9999999403953552"
2) "0.9999999403953552"
> VEMB points pt:B
1) "-0.9999999403953552"
2) "-0.9999999403953552"
> VEMB points pt:C
1) "-0.9999999403953552"
2) "0.9999999403953552"
> VEMB points pt:D
1) "0.9999999403953552"
2) "-0.9999999403953552"
> VEMB points pt:E
1) "1"
2) "0"
```

##### C#

```csharp
        using (Lease<float>? eA = db.VectorSetGetApproximateVector("points", "pt:A"))
        {
            Span<float> a = eA!.Span;
            Console.WriteLine($"[{a[0]}, {a[1]}]"); // >>> [0.9999999403953552, 0.9999999403953552]
        }
        using (Lease<float>? eB = db.VectorSetGetApproximateVector("points", "pt:B"))
        {
            Span<float> b = eB!.Span;
            Console.WriteLine($"[{b[0]}, {b[1]}]"); // >>> [-0.9999999403953552, -0.9999999403953552]
        }
        using (Lease<float>? eC = db.VectorSetGetApproximateVector("points", "pt:C"))
        {
            Span<float> c = eC!.Span;
            Console.WriteLine($"[{c[0]}, {c[1]}]"); // >>> [-0.9999999403953552, 0.9999999403953552]
        }
        using (Lease<float>? eD = db.VectorSetGetApproximateVector("points", "pt:D"))
        {
            Span<float> d = eD!.Span;
            Console.WriteLine($"[{d[0]}, {d[1]}]"); // >>> [0.9999999403953552, -0.9999999403953552]
        }
        using (Lease<float>? eE = db.VectorSetGetApproximateVector("points", "pt:E"))
        {
            Span<float> e = eE!.Span;
            Console.WriteLine($"[{e[0]}, {e[1]}]"); // >>> [1, 0]
        }
```

##### Go

```go
	res9, err := rdb.VEmb(ctx, "points", "pt:A", false).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res9) // >>> [0.9999999403953552 0.9999999403953552]

	res10, err := rdb.VEmb(ctx, "points", "pt:B", false).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res10) // >>> [-0.9999999403953552 -0.9999999403953552]

	res11, err := rdb.VEmb(ctx, "points", "pt:C", false).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res11) // >>> [-0.9999999403953552 0.9999999403953552]

	res12, err := rdb.VEmb(ctx, "points", "pt:D", false).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res12) // >>> [0.9999999403953552 -0.9999999403953552]

	res13, err := rdb.VEmb(ctx, "points", "pt:E", false).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res13) // >>> [1 0]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> getEmbeddingA = asyncCommands.vemb("points", "pt:A").thenAccept(result -> {
                System.out.println(result); // >>> [0.9999999403953552, 0.9999999403953552]
            }).toCompletableFuture();

            CompletableFuture<Void> getEmbeddingB = asyncCommands.vemb("points", "pt:B").thenAccept(result -> {
                System.out.println(result); // >>> [-0.9999999403953552, -0.9999999403953552]
            }).toCompletableFuture();

            CompletableFuture<Void> getEmbeddingC = asyncCommands.vemb("points", "pt:C").thenAccept(result -> {
                System.out.println(result); // >>> [-0.9999999403953552, 0.9999999403953552]
            }).toCompletableFuture();

            CompletableFuture<Void> getEmbeddingD = asyncCommands.vemb("points", "pt:D").thenAccept(result -> {
                System.out.println(result); // >>> [0.9999999403953552, -0.9999999403953552]
            }).toCompletableFuture();

            CompletableFuture<Void> getEmbeddingE = asyncCommands.vemb("points", "pt:E").thenAccept(result -> {
                System.out.println(result); // >>> [1.0, 0.0]
            }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<java.util.List<Double>> getEmbeddingA = reactiveCommands.vemb("points", "pt:A").collectList()
                    .doOnNext(result -> {
                        System.out.println(result); // >>> [0.9999999403953552, 0.9999999403953552]
                    });

            Mono<java.util.List<Double>> getEmbeddingB = reactiveCommands.vemb("points", "pt:B").collectList()
                    .doOnNext(result -> {
                        System.out.println(result); // >>> [-0.9999999403953552, -0.9999999403953552]
                    });

            Mono<java.util.List<Double>> getEmbeddingC = reactiveCommands.vemb("points", "pt:C").collectList()
                    .doOnNext(result -> {
                        System.out.println(result); // >>> [-0.9999999403953552, 0.9999999403953552]
                    });

            Mono<java.util.List<Double>> getEmbeddingD = reactiveCommands.vemb("points", "pt:D").collectList()
                    .doOnNext(result -> {
                        System.out.println(result); // >>> [0.9999999403953552, -0.9999999403953552]
                    });

            Mono<java.util.List<Double>> getEmbeddingE = reactiveCommands.vemb("points", "pt:E").collectList()
                    .doOnNext(result -> {
                        System.out.println(result); // >>> [1.0, 0.0]
                    });
```

##### Java (Synchronous - Jedis)

```java
      List<Double> res9 = jedis.vemb("points", "pt:A");
      System.out.println(res9); // >>> [0.9999999..., 0.9999999...]

      List<Double> res10 = jedis.vemb("points", "pt:B");
      System.out.println(res10); // >>> [-0.9999999..., -0.9999999...]

      List<Double> res11 = jedis.vemb("points", "pt:C");
      System.out.println(res11); // >>> [-0.9999999..., 0.9999999...]

      List<Double> res12 = jedis.vemb("points", "pt:D");
      System.out.println(res12); // >>> [0.9999999..., -0.9999999...]

      List<Double> res13 = jedis.vemb("points", "pt:E");
      System.out.println(res13); // >>> [1, 0]
```

##### JavaScript (Node.js)

```javascript
const res9 = await client.vEmb("points", "pt:A");
console.log(res9);  // >>> [0.9999999403953552, 0.9999999403953552]

const res10 = await client.vEmb("points", "pt:B");
console.log(res10);  // >>> [-0.9999999403953552, -0.9999999403953552]

const res11 = await client.vEmb("points", "pt:C");
console.log(res11);  // >>> [-0.9999999403953552, 0.9999999403953552]

const res12 = await client.vEmb("points", "pt:D");
console.log(res12);  // >>> [0.9999999403953552, -0.9999999403953552]

const res13 = await client.vEmb("points", "pt:E");
console.log(res13);  // >>> [1, 0]
```

##### PHP

```php
        $res9 = $r->vemb('points', 'pt:A');
        echo json_encode($res9) . PHP_EOL;
        // >>> [0.9999999403953552, 0.9999999403953552]

        $res10 = $r->vemb('points', 'pt:B');
        echo json_encode($res10) . PHP_EOL;
        // >>> [-0.9999999403953552, -0.9999999403953552]

        $res11 = $r->vemb('points', 'pt:C');
        echo json_encode($res11) . PHP_EOL;
        // >>> [-0.9999999403953552, 0.9999999403953552]

        $res12 = $r->vemb('points', 'pt:D');
        echo json_encode($res12) . PHP_EOL;
        // >>> [0.9999999403953552, -0.9999999403953552]

        $res13 = $r->vemb('points', 'pt:E');
        echo json_encode($res13) . PHP_EOL;
        // >>> [1,0]
```

##### Python

```python
res9 = r.vset().vemb("points", "pt:A")
print(res9)  # >>> [0.9999999403953552, 0.9999999403953552]

res10 = r.vset().vemb("points", "pt:B")
print(res10)  # >>> [-0.9999999403953552, -0.9999999403953552]

res11 = r.vset().vemb("points", "pt:C")
print(res11)  # >>> [-0.9999999403953552, 0.9999999403953552]

res12 = r.vset().vemb("points", "pt:D")
print(res12)  # >>> [0.9999999403953552, -0.9999999403953552]

res13 = r.vset().vemb("points", "pt:E")
print(res13)  # >>> [1, 0]
```

##### Rust (Asynchronous)

```rust
        if let Ok(res) = r.vemb("points", "pt:A").await {
            let res: Vec<f64> = res;
            println!("{res:?}");
            // >>> [0.9999999403953552, 0.9999999403953552]
        }

        if let Ok(res) = r.vemb("points", "pt:B").await {
            let res: Vec<f64> = res;
            println!("{res:?}");
            // >>> [-0.9999999403953552, -0.9999999403953552]
        }

        if let Ok(res) = r.vemb("points", "pt:C").await {
            let res: Vec<f64> = res;
            println!("{res:?}");
            // >>> [-0.9999999403953552, 0.9999999403953552]
        }

        if let Ok(res) = r.vemb("points", "pt:D").await {
            let res: Vec<f64> = res;
            println!("{res:?}");
            // >>> [0.9999999403953552, -0.9999999403953552]
        }

        if let Ok(res) = r.vemb("points", "pt:E").await {
            let res: Vec<f64> = res;
            println!("{res:?}"); // >>> [1.0, 0.0]
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.vemb("points", "pt:A") {
            let res: Vec<f64> = res;
            println!("{res:?}");
            // >>> [0.9999999403953552, 0.9999999403953552]
        }

        if let Ok(res) = r.vemb("points", "pt:B") {
            let res: Vec<f64> = res;
            println!("{res:?}");
            // >>> [-0.9999999403953552, -0.9999999403953552]
        }

        if let Ok(res) = r.vemb("points", "pt:C") {
            let res: Vec<f64> = res;
            println!("{res:?}");
            // >>> [-0.9999999403953552, 0.9999999403953552]
        }

        if let Ok(res) = r.vemb("points", "pt:D") {
            let res: Vec<f64> = res;
            println!("{res:?}");
            // >>> [0.9999999403953552, -0.9999999403953552]
        }

        if let Ok(res) = r.vemb("points", "pt:E") {
            let res: Vec<f64> = res;
            println!("{res:?}"); // >>> [1.0, 0.0]
        }
```



Remove an unwanted element with [`VREM`](https://redis.io/docs/latest/commands/vrem)

Element removal: Use VREM to delete elements from a vector set when you need to remove vectors from the collection

**Builds upon:** vadd

**Commands:** VADD, VCARD, VREM

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> VADD points VALUES 2 0 0 pt:F
(integer) 1
> VCARD points
(integer) 6
> VREM points pt:F
(integer) 1
> VCARD points
(integer) 5
```

##### C#

```csharp
        bool addF = db.VectorSetAdd("points", VectorSetAddRequest.Member("pt:F", new float[] { 0f, 0f }, null));
        Console.WriteLine(addF); // >>> True

        long card1 = db.VectorSetLength("points");
        Console.WriteLine(card1); // >>> 6

        bool remF = db.VectorSetRemove("points", "pt:F");
        Console.WriteLine(remF); // >>> True

        long card2 = db.VectorSetLength("points");
        Console.WriteLine(card2); // >>> 5
```

##### Go

```go
	res18, err := rdb.VAdd(ctx, "points", "pt:F",
		&redis.VectorValues{Val: []float64{0.0, 0.0}},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res18) // >>> true

	res19, err := rdb.VCard(ctx, "points").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res19) // >>> 6

	res20, err := rdb.VRem(ctx, "points", "pt:F").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res20) // >>> true

	res21, err := rdb.VCard(ctx, "points").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res21) // >>> 5
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> addTempPointF = asyncCommands.vadd("points", "pt:F", 0.0, 0.0).thenAccept(result -> {
                System.out.println(result); // >>> true
            }).toCompletableFuture();

            CompletableFuture<Void> checkCardinalityBefore = asyncCommands.vcard("points").thenAccept(result -> {
                System.out.println(result); // >>> 6
            }).toCompletableFuture();

            CompletableFuture<Void> removePointF = asyncCommands.vrem("points", "pt:F").thenAccept(result -> {
                System.out.println(result); // >>> true
            }).toCompletableFuture();

            CompletableFuture<Void> checkCardinalityAfter = asyncCommands.vcard("points").thenAccept(result -> {
                System.out.println(result); // >>> 5
            }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Boolean> addTempPointF = reactiveCommands.vadd("points", "pt:F", 0.0, 0.0).doOnNext(result -> {
                System.out.println(result); // >>> true
            });

            Mono<Long> checkCardinalityBefore = reactiveCommands.vcard("points").doOnNext(result -> {
                System.out.println(result); // >>> 6
            });

            Mono<Boolean> removePointF = reactiveCommands.vrem("points", "pt:F").doOnNext(result -> {
                System.out.println(result); // >>> true
            });

            Mono<Long> checkCardinalityAfter = reactiveCommands.vcard("points").doOnNext(result -> {
                System.out.println(result); // >>> 5
            });
```

##### Java (Synchronous - Jedis)

```java
      boolean res18 = jedis.vadd("points", new float[] { 0.0f, 0.0f }, "pt:F");
      System.out.println(res18); // >>> true

      long res19 = jedis.vcard("points");
      System.out.println(res19); // >>> 6

      boolean res20 = jedis.vrem("points", "pt:F");
      System.out.println(res20); // >>> true

      long res21 = jedis.vcard("points");
      System.out.println(res21); // >>> 5
```

##### JavaScript (Node.js)

```javascript
const res18 = await client.vAdd("points", [0, 0], "pt:F");
console.log(res18);  // >>> true

const res19 = await client.vCard("points");
console.log(res19);  // >>> 6

const res20 = await client.vRem("points", "pt:F");
console.log(res20);  // >>> true

const res21 = await client.vCard("points");
console.log(res21);  // >>> 5
```

##### PHP

```php
        $res18 = $r->vadd('points', [0, 0], 'pt:F');
        echo $res18 . PHP_EOL;
        // >>> 1

        $res19 = $r->vcard('points');
        echo $res19 . PHP_EOL;
        // >>> 6

        $res20 = $r->vrem('points', 'pt:F');
        echo $res20 . PHP_EOL;
        // >>> 1

        $res21 = $r->vcard('points');
        echo $res21 . PHP_EOL;
        // >>> 5
```

##### Python

```python
res18 = r.vset().vadd("points", [0, 0], "pt:F")
print(res18)  # >>> 1

res19 = r.vset().vcard("points")
print(res19)  # >>> 6

res20 = r.vset().vrem("points", "pt:F")
print(res20)  # >>> 1

res21 = r.vset().vcard("points")
print(res21)  # >>> 5
```

##### Rust (Asynchronous)

```rust
        if let Ok(res) = r
            .vadd(
                "points",
                VectorAddInput::Values(EmbeddingInput::String(&["0", "0"])),
                "pt:F",
            )
            .await
        {
            let res: bool = res;
            println!("{res}"); // >>> true
        }

        if let Ok(res) = r.vcard("points").await {
            let res: usize = res;
            println!("{res}"); // >>> 6
        }

        if let Ok(res) = r.vrem("points", "pt:F").await {
            let res: bool = res;
            println!("{res}"); // >>> true
        }

        if let Ok(res) = r.vcard("points").await {
            let res: usize = res;
            println!("{res}"); // >>> 5
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.vadd(
            "points",
            VectorAddInput::Values(EmbeddingInput::String(&["0", "0"])),
            "pt:F",
        ) {
            let res: bool = res;
            println!("{res}"); // >>> true
        }

        if let Ok(res) = r.vcard("points") {
            let res: usize = res;
            println!("{res}"); // >>> 6
        }

        if let Ok(res) = r.vrem("points", "pt:F") {
            let res: bool = res;
            println!("{res}"); // >>> true
        }

        if let Ok(res) = r.vcard("points") {
            let res: usize = res;
            println!("{res}"); // >>> 5
        }
```



Set and retrieve an element's JSON attribute data using
[`VSETATTR`](https://redis.io/docs/latest/commands/vsetattr)
and [`VGETATTR`](https://redis.io/docs/latest/commands/vgetattr). You can also pass an empty string
to `VSETATTR` to delete the attribute data:

Attribute management: Use VSETATTR to store JSON attributes on elements and VGETATTR to retrieve them when you need to associate metadata with vectors

**Builds upon:** vadd

**Commands:** VSETATTR, VGETATTR

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> VSETATTR points pt:A "{\"name\": \"Point A\", \"description\": \"First point added\"}"
(integer) 1
> VGETATTR points pt:A
"{\"name\": \"Point A\", \"description\": \"First point added\"}"
> VSETATTR points pt:A ""
(integer) 1
> VGETATTR points pt:A
(nil)
```

##### C#

```csharp
        string attrJson = "{\"name\":\"Point A\",\"description\":\"First point added\"}";
        bool setAttr1 = db.VectorSetSetAttributesJson("points", "pt:A", attrJson);
        Console.WriteLine(setAttr1); // >>> True

        string? getAttr1 = db.VectorSetGetAttributesJson("points", "pt:A");
        Console.WriteLine(getAttr1); // >>> {"name":"Point A","description":"First point added"}

        bool clearAttr = db.VectorSetSetAttributesJson("points", "pt:A", "");
        Console.WriteLine(clearAttr); // >>> True

        string? getAttr2 = db.VectorSetGetAttributesJson("points", "pt:A");
        Console.WriteLine(getAttr2 is null ? "None" : getAttr2); // >>> None
```

##### Go

```go
	attrs := map[string]interface{}{
		"name":        "Point A",
		"description": "First point added",
	}

	res14, err := rdb.VSetAttr(ctx, "points", "pt:A", attrs).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res14) // >>> true

	res15, err := rdb.VGetAttr(ctx, "points", "pt:A").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res15)
	// >>> {"description":"First point added","name":"Point A"}

	res16, err := rdb.VClearAttributes(ctx, "points", "pt:A").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res16) // >>> true

	// `VGetAttr()` returns an error if the attribute doesn't exist.
	_, err = rdb.VGetAttr(ctx, "points", "pt:A").Result()

	if err != nil {
		fmt.Println(err)
	}
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> setAttributeA = asyncCommands
                    .vsetattr("points", "pt:A", "{\"name\": \"Point A\", \"description\": \"First point added\"}")
                    .thenAccept(result -> {
                        System.out.println(result); // >>> true
                    }).toCompletableFuture();

            CompletableFuture<Void> getAttributeA = asyncCommands.vgetattr("points", "pt:A").thenAccept(result -> {
                System.out.println(result); // >>> {"name": "Point A", "description": "First point added"}
            }).toCompletableFuture();

            CompletableFuture<Void> clearAttributeA = asyncCommands.vsetattr("points", "pt:A", "").thenAccept(result -> {
                System.out.println(result); // >>> true
            }).toCompletableFuture();

            CompletableFuture<Void> verifyAttributeCleared = asyncCommands.vgetattr("points", "pt:A").thenAccept(result -> {
                System.out.println(result); // >>> null
            }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Boolean> setAttributeA = reactiveCommands
                    .vsetattr("points", "pt:A", "{\"name\": \"Point A\", \"description\": \"First point added\"}")
                    .doOnNext(result -> {
                        System.out.println(result); // >>> true
                    });

            Mono<String> getAttributeA = reactiveCommands.vgetattr("points", "pt:A").doOnNext(result -> {
                System.out.println(result); // >>> {"name": "Point A", "description": "First point added"}
            });

            Mono<Boolean> clearAttributeA = reactiveCommands.vsetattr("points", "pt:A", "").doOnNext(result -> {
                System.out.println(result); // >>> true
            });

            Mono<String> verifyAttributeCleared = reactiveCommands.vgetattr("points", "pt:A").doOnNext(result -> {
                System.out.println(result); // >>> null
            });
```

##### Java (Synchronous - Jedis)

```java
      boolean res14 = jedis.vsetattr("points", "pt:A",
        "{\"name\":\"Point A\",\"description\":\"First point added\"}");
      System.out.println(res14); // >>> true

      String res15 = jedis.vgetattr("points", "pt:A");
      System.out.println(res15);
      // >>> {"name":"Point A","description":"First point added"}

      boolean res16 = jedis.vsetattr("points", "pt:A", "");
      System.out.println(res16); // >>> true

      String res17 = jedis.vgetattr("points", "pt:A");
      System.out.println(res17); // >>> null
```

##### JavaScript (Node.js)

```javascript
const res14 = await client.vSetAttr("points", "pt:A", {
  name: "Point A",
  description: "First point added"
});
console.log(res14);  // >>> true

const res15 = await client.vGetAttr("points", "pt:A");
console.log(res15);
// >>> {name: 'Point A', description: 'First point added'}

const res16 = await client.vSetAttr("points", "pt:A", "");
console.log(res16);  // >>> true

const res17 = await client.vGetAttr("points", "pt:A");
console.log(res17);  // >>> null
```

##### PHP

```php
        $res14 = $r->vsetattr('points', 'pt:A', '{
            "name": "Point A",
            "description": "First point added"
        }');
        echo $res14 . PHP_EOL;
        // >>> 1

        $res15 = $r->vgetattr('points', 'pt:A');
        echo json_encode($res15) . PHP_EOL;
        // >>> {"name":"Point A","description":"First point added"}

        $res16 = $r->vsetattr('points', 'pt:A', '');
        echo $res16 . PHP_EOL;
        // >>> 1

        $res17 = $r->vgetattr('points', 'pt:A');
        echo json_encode($res17) . PHP_EOL;
        // >>> null
```

##### Python

```python
res14 = r.vset().vsetattr("points", "pt:A", {
    "name": "Point A",
    "description": "First point added"
})
print(res14)  # >>> 1

res15 = r.vset().vgetattr("points", "pt:A")
print(res15)
# >>> {'name': 'Point A', 'description': 'First point added'}

res16 = r.vset().vsetattr("points", "pt:A", "")
print(res16)  # >>> 1

res17 = r.vset().vgetattr("points", "pt:A")
print(res17)  # >>> None
```

##### Rust (Asynchronous)

```rust
        let res: bool = cmd("VSETATTR")
            .arg("points")
            .arg("pt:A")
            .arg("{\"name\":\"Point A\",\"description\":\"First point added\"}")
            .query_async(&mut r)
            .await
            .expect("VSETATTR should succeed");
        println!("{res}"); // >>> true

        if let Ok(res) = r.vgetattr("points", "pt:A").await {
            let res: Option<String> = res;
            println!(
                "{}",
                res.clone().unwrap_or_else(|| "None".to_string())
            );
            // >>> {"name":"Point A","description":"First point added"}
        }

        let res: bool = cmd("VSETATTR")
            .arg("points")
            .arg("pt:A")
            .arg("")
            .query_async(&mut r)
            .await
            .expect("VSETATTR clear should succeed");
        println!("{res}"); // >>> true

        if let Ok(res) = r.vgetattr("points", "pt:A").await {
            let res: Option<String> = res;
            println!(
                "{}",
                res.clone().unwrap_or_else(|| "None".to_string())
            ); // >>> None
        }
```

##### Rust (Synchronous)

```rust
        let res: bool = cmd("VSETATTR")
            .arg("points")
            .arg("pt:A")
            .arg("{\"name\":\"Point A\",\"description\":\"First point added\"}")
            .query(&mut r)
            .expect("VSETATTR should succeed");
        println!("{res}"); // >>> true

        if let Ok(res) = r.vgetattr("points", "pt:A") {
            let res: Option<String> = res;
            println!(
                "{}",
                res.clone().unwrap_or_else(|| "None".to_string())
            );
            // >>> {"name":"Point A","description":"First point added"}
        }

        let res: bool = cmd("VSETATTR")
            .arg("points")
            .arg("pt:A")
            .arg("")
            .query(&mut r)
            .expect("VSETATTR clear should succeed");
        println!("{res}"); // >>> true

        if let Ok(res) = r.vgetattr("points", "pt:A") {
            let res: Option<String> = res;
            println!(
                "{}",
                res.clone().unwrap_or_else(|| "None".to_string())
            ); // >>> None
        }
```



### Vector similarity search

Use [`VSIM`](https://redis.io/docs/latest/commands/vsim) to rank the points in order of their vector distance from a sample point:

Similarity search: Use VSIM to find elements most similar to a query vector when you need to perform vector similarity searches

**Difficulty:** Intermediate

**Builds upon:** vadd

**Commands:** VSIM

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> VSIM points values 2 0.9 0.1
1) "pt:E"
2) "pt:A"
3) "pt:D"
4) "pt:C"
5) "pt:B"
```

##### C#

```csharp
        VectorSetSimilaritySearchRequest qBasic = VectorSetSimilaritySearchRequest.ByVector(new float[] { 0.9f, 0.1f });
        using (Lease<VectorSetSimilaritySearchResult>? res = db.VectorSetSimilaritySearch("points", qBasic))
        {
            VectorSetSimilaritySearchResult[] items = res!.Span.ToArray();
            string[] ordered = items.Select(x => (string?)x.Member).Where(s => s is not null).Select(s => s!).ToArray();
            Console.WriteLine("[" + string.Join(", ", ordered.Select(s => $"'{s}'")) + "]");
            // >>> ['pt:E', 'pt:A', 'pt:D', 'pt:C', 'pt:B']
        }
```

##### Go

```go
	res22, err := rdb.VSim(ctx, "points",
		&redis.VectorValues{Val: []float64{0.9, 0.1}},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res22) // >>> [pt:E pt:A pt:D pt:C pt:B]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> basicSimilaritySearch = asyncCommands.vsim("points", 0.9, 0.1).thenAccept(result -> {
                System.out.println(result); // >>> [pt:E, pt:A, pt:D, pt:C, pt:B]
            }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<java.util.List<String>> basicSimilaritySearch = reactiveCommands.vsim("points", 0.9, 0.1).collectList()
                    .doOnNext(result -> {
                        System.out.println(result); // >>> [pt:E, pt:A, pt:D, pt:C, pt:B]
                    });
```

##### Java (Synchronous - Jedis)

```java
      List<String> res22 = jedis.vsim("points", new float[] { 0.9f, 0.1f });
      System.out.println(res22);
      // >>> ["pt:E", "pt:A", "pt:D", "pt:C", "pt:B"]
```

##### JavaScript (Node.js)

```javascript
const res22 = await client.vSim("points", [0.9, 0.1]);
console.log(res22);
// >>> ['pt:E', 'pt:A', 'pt:D', 'pt:C', 'pt:B']
```

##### PHP

```php
        $res22 = $r->vsim('points', [0.9, 0.1]);
        echo json_encode($res22) . PHP_EOL;
        // >>> ["pt:E","pt:A","pt:D","pt:C","pt:B"]
```

##### Python

```python
res22 = r.vset().vsim("points", [0.9, 0.1])
print(res22)
# >>> ['pt:E', 'pt:A', 'pt:D', 'pt:C', 'pt:B']
```

##### Rust (Asynchronous)

```rust
        if let Ok(res) = r
            .vsim(
                "points",
                VectorSimilaritySearchInput::Values(EmbeddingInput::Float64(&[0.9, 0.1])),
            )
            .await
        {
            let res: Value = res;
            if let Value::Array(items) = res {
                let view: Vec<String> = items
                    .into_iter()
                    .map(|item| match item {
                        Value::BulkString(bytes) => String::from_utf8(bytes).expect("utf8"),
                        Value::SimpleString(s) => s,
                        other => panic!("Unexpected VSIM item: {other:?}"),
                    })
                    .collect();
                println!("{view:?}");
                // >>> ["pt:E", "pt:A", "pt:D", "pt:C", "pt:B"]
            }
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.vsim(
            "points",
            VectorSimilaritySearchInput::Values(EmbeddingInput::Float64(&[0.9, 0.1])),
        ) {
            let res: Value = res;
            if let Value::Array(items) = res {
                let view: Vec<String> = items
                    .into_iter()
                    .map(|item| match item {
                        Value::BulkString(bytes) => String::from_utf8(bytes).expect("utf8"),
                        Value::SimpleString(s) => s,
                        other => panic!("Unexpected VSIM item: {other:?}"),
                    })
                    .collect();
                println!("{view:?}");
                // >>> ["pt:E", "pt:A", "pt:D", "pt:C", "pt:B"]
            }
        }
```



Find the four elements that are closest to point A and show their distance "scores":

Similarity with options: Use VSIM with ELE, WITHSCORES, and COUNT options to find similar elements with scores and limits when you need detailed similarity results

**Difficulty:** Intermediate

**Builds upon:** vadd

**Commands:** VSIM

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> VSIM points ELE pt:A WITHSCORES COUNT 4
1) "pt:A"
2) "1"
3) "pt:E"
4) "0.8535534143447876"
5) "pt:C"
6) "0.5"
7) "pt:D"
8) "0.5"
```

##### C#

```csharp
        VectorSetSimilaritySearchRequest qOpts = VectorSetSimilaritySearchRequest.ByMember("pt:A");
        qOpts.WithScores = true;
        qOpts.Count = 4;
        using (Lease<VectorSetSimilaritySearchResult>? res = db.VectorSetSimilaritySearch("points", qOpts))
        {
            VectorSetSimilaritySearchResult[] items = res!.Span.ToArray();
            Dictionary<string, double> dict = items
                .Select(i => new { Key = (string?)i.Member, i.Score })
                .Where(x => x.Key is not null)
                .ToDictionary(x => x.Key!, x => x.Score);
            Console.WriteLine("{" + string.Join(", ", dict.Select(kv => $"'{kv.Key}': {kv.Value}")) + "}");
            // >>> {'pt:A': 1.0, 'pt:E': 0.8535534143447876, 'pt:D': 0.5, 'pt:C': 0.5}
        }
```

##### Go

```go
	res23, err := rdb.VSimWithArgsWithScores(
		ctx,
		"points",
		&redis.VectorRef{Name: "pt:A"},
		&redis.VSimArgs{Count: 4},
	).Result()

	if err != nil {
		panic(err)
	}

	sort.Slice(res23, func(i, j int) bool {
		return res23[i].Name < res23[j].Name
	})

	fmt.Println(res23)
	// >>> [{pt:A 1} {pt:C 0.5} {pt:D 0.5} {pt:E 0.8535534143447876}]
```

##### Java (Asynchronous - Lettuce)

```java
            VSimArgs vsimArgs = new VSimArgs();
            vsimArgs.count(4L);
            CompletableFuture<Void> similaritySearchWithScore = asyncCommands.vsimWithScore("points", vsimArgs, "pt:A")
                    .thenAccept(result -> {
                        System.out.println(result); // >>> {pt:A=1.0, pt:E=0.8535534143447876, pt:D=0.5, pt:C=0.5}
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            VSimArgs vsimArgs = new VSimArgs();
            vsimArgs.count(4L);
            Mono<java.util.Map<String, Double>> similaritySearchWithScore = reactiveCommands
                    .vsimWithScore("points", vsimArgs, "pt:A").doOnNext(result -> {
                        System.out.println(result); // >>> {pt:A=1.0, pt:E=0.8535534143447876, pt:D=0.5, pt:C=0.5}
                    });
```

##### Java (Synchronous - Jedis)

```java
      Map<String, Double> res23 = jedis.vsimByElementWithScores("points", "pt:A",
        new VSimParams().count(4));
      System.out.println(res23);
      // >>> {pt:A=1.0, pt:E≈0.85355, pt:D=0.5, pt:C=0.5}
```

##### JavaScript (Node.js)

```javascript
const res23 = await client.vSimWithScores("points", "pt:A", { COUNT: 4 });
console.log(res23);
// >>> {pt:A: 1.0, pt:E: 0.8535534143447876, pt:D: 0.5, pt:C: 0.5}
```

##### PHP

```php
        // Returns an array of elements with their scores:
        //      ['pt:A' => 1.0, 'pt:E' => 0.8535534143447876,...
        $res23 = $r->vsim(
            'points', 'pt:A', true,true, 4,
        );
        echo json_encode($res23) . PHP_EOL;
        // >>> {'pt:A': 1.0, 'pt:E': 0.8535534143447876, 'pt:D': 0.5, 'pt:C': 0.5}
```

##### Python

```python
res23 = r.vset().vsim(
    "points", "pt:A",
    with_scores=True,
    count=4
)
print(res23)
# >>> {'pt:A': 1.0, 'pt:E': 0.8535534143447876, 'pt:D': 0.5, 'pt:C': 0.5}
```

##### Rust (Asynchronous)

```rust
        let opts = VSimOptions::default().set_with_scores(true).set_count(4);
        if let Ok(res) = r
            .vsim_options("points", VectorSimilaritySearchInput::Element("pt:A"), &opts)
            .await
        {
            let res: Value = res;
            let mut view: Vec<(String, f64)> = match res {
                Value::Array(items) => items
                    .chunks(2)
                    .map(|chunk| {
                        let member = match &chunk[0] {
                            Value::BulkString(bytes) => {
                                String::from_utf8(bytes.clone()).expect("utf8")
                            }
                            Value::SimpleString(s) => s.clone(),
                            other => panic!("Unexpected member format: {other:?}"),
                        };
                        let score = match &chunk[1] {
                            Value::BulkString(bytes) => String::from_utf8(bytes.clone())
                                .expect("utf8")
                                .parse::<f64>()
                                .expect("score"),
                            Value::SimpleString(s) => s.parse::<f64>().expect("score"),
                            Value::Double(v) => *v,
                            Value::Int(v) => *v as f64,
                            other => panic!("Unexpected score format: {other:?}"),
                        };
                        (member, score)
                    })
                    .collect(),
                Value::Map(items) => items
                    .into_iter()
                    .map(|(member, score)| {
                        let member = match member {
                            Value::BulkString(bytes) => String::from_utf8(bytes).expect("utf8"),
                            Value::SimpleString(s) => s,
                            other => panic!("Unexpected member format: {other:?}"),
                        };
                        let score = match score {
                            Value::BulkString(bytes) => String::from_utf8(bytes)
                                .expect("utf8")
                                .parse::<f64>()
                                .expect("score"),
                            Value::SimpleString(s) => s.parse::<f64>().expect("score"),
                            Value::Double(v) => v,
                            Value::Int(v) => v as f64,
                            other => panic!("Unexpected score format: {other:?}"),
                        };
                        (member, score)
                    })
                    .collect(),
                other => panic!("Unexpected VSIM WITHSCORES response: {other:?}"),
            };
            view.sort_by(|a, b| {
                b.1.partial_cmp(&a.1)
                    .unwrap_or(std::cmp::Ordering::Equal)
                    .then_with(|| b.0.cmp(&a.0))
            });
            println!("{view:?}");
            // >>> [("pt:A", 1.0), ("pt:E", 0.8535534143447876), ("pt:D", 0.5), ("pt:C", 0.5)]
        }
```

##### Rust (Synchronous)

```rust
        let opts = VSimOptions::default().set_with_scores(true).set_count(4);
        if let Ok(res) =
            r.vsim_options("points", VectorSimilaritySearchInput::Element("pt:A"), &opts)
        {
            let res: Value = res;
            let mut view: Vec<(String, f64)> = match res {
                Value::Array(items) => items
                    .chunks(2)
                    .map(|chunk| {
                        let member = match &chunk[0] {
                            Value::BulkString(bytes) => {
                                String::from_utf8(bytes.clone()).expect("utf8")
                            }
                            Value::SimpleString(s) => s.clone(),
                            other => panic!("Unexpected member format: {other:?}"),
                        };
                        let score = match &chunk[1] {
                            Value::BulkString(bytes) => String::from_utf8(bytes.clone())
                                .expect("utf8")
                                .parse::<f64>()
                                .expect("score"),
                            Value::SimpleString(s) => s.parse::<f64>().expect("score"),
                            Value::Double(v) => *v,
                            Value::Int(v) => *v as f64,
                            other => panic!("Unexpected score format: {other:?}"),
                        };
                        (member, score)
                    })
                    .collect(),
                Value::Map(items) => items
                    .into_iter()
                    .map(|(member, score)| {
                        let member = match member {
                            Value::BulkString(bytes) => String::from_utf8(bytes).expect("utf8"),
                            Value::SimpleString(s) => s,
                            other => panic!("Unexpected member format: {other:?}"),
                        };
                        let score = match score {
                            Value::BulkString(bytes) => String::from_utf8(bytes)
                                .expect("utf8")
                                .parse::<f64>()
                                .expect("score"),
                            Value::SimpleString(s) => s.parse::<f64>().expect("score"),
                            Value::Double(v) => v,
                            Value::Int(v) => v as f64,
                            other => panic!("Unexpected score format: {other:?}"),
                        };
                        (member, score)
                    })
                    .collect(),
                other => panic!("Unexpected VSIM WITHSCORES response: {other:?}"),
            };
            view.sort_by(|a, b| {
                b.1.partial_cmp(&a.1)
                    .unwrap_or(std::cmp::Ordering::Equal)
                    .then_with(|| b.0.cmp(&a.0))
            });
            println!("{view:?}");
            // >>> [("pt:A", 1.0), ("pt:E", 0.8535534143447876), ("pt:D", 0.5), ("pt:C", 0.5)]
        }
```



Add some JSON attributes and use
[filter expressions](https://redis.io/docs/latest/develop/data-types/vector-sets/filtered-search)
to include them in the search:

Filtered similarity search: Use VSIM with FILTER option to apply attribute-based conditions to similarity results when you need to combine vector similarity with attribute filtering

**Difficulty:** Advanced

**Builds upon:** vadd

**Commands:** VSETATTR, VSIM

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> VSETATTR points pt:A "{\"size\":\"large\",\"price\": 18.99}"
(integer) 1
> VSETATTR points pt:B "{\"size\":\"large\",\"price\": 35.99}"
(integer) 1
> VSETATTR points pt:C "{\"size\":\"large\",\"price\": 25.99}"
(integer) 1
> VSETATTR points pt:D "{\"size\":\"small\",\"price\": 21.00}"
(integer) 1
> VSETATTR points pt:E "{\"size\":\"small\",\"price\": 17.75}"
(integer) 1

# Return elements in order of distance from point A whose
# `size` attribute is `large`.
> VSIM points ELE pt:A FILTER '.size == "large"'
1) "pt:A"
2) "pt:C"
3) "pt:B"

# Return elements in order of distance from point A whose size is
# `large` and whose price is greater than 20.00.
> VSIM points ELE pt:A FILTER '.size == "large" && .price > 20.00'
1) "pt:C"
2) "pt:B"
```

##### C#

```csharp
        bool okA = db.VectorSetSetAttributesJson("points", "pt:A", "{\"size\":\"large\",\"price\":18.99}");
        Console.WriteLine(okA); // >>> True
        bool okB = db.VectorSetSetAttributesJson("points", "pt:B", "{\"size\":\"large\",\"price\":35.99}");
        Console.WriteLine(okB); // >>> True
        bool okC = db.VectorSetSetAttributesJson("points", "pt:C", "{\"size\":\"large\",\"price\":25.99}");
        Console.WriteLine(okC); // >>> True
        bool okD = db.VectorSetSetAttributesJson("points", "pt:D", "{\"size\":\"small\",\"price\":21.00}");
        Console.WriteLine(okD); // >>> True
        bool okE = db.VectorSetSetAttributesJson("points", "pt:E", "{\"size\":\"small\",\"price\":17.75}");
        Console.WriteLine(okE); // >>> True

        VectorSetSimilaritySearchRequest qFilt1 = VectorSetSimilaritySearchRequest.ByMember("pt:A");
        qFilt1.FilterExpression = ".size == \"large\"";
        using (Lease<VectorSetSimilaritySearchResult>? res = db.VectorSetSimilaritySearch("points", qFilt1))
        {
            string[] ids = res!.Span.ToArray()
                .Select(i => (string?)i.Member)
                .Where(s => s is not null)
                .Select(s => s!)
                .ToArray();
            Console.WriteLine("[" + string.Join(", ", ids.Select(s => $"'{s}'")) + "]");
            // >>> ['pt:A', 'pt:C', 'pt:B']

        }

        VectorSetSimilaritySearchRequest qFilt2 = VectorSetSimilaritySearchRequest.ByMember("pt:A");
        qFilt2.FilterExpression = ".size == \"large\" && .price > 20.00";
        using (Lease<VectorSetSimilaritySearchResult>? res = db.VectorSetSimilaritySearch("points", qFilt2))
        {
            string[] ids = res!.Span.ToArray()
                .Select(i => (string?)i.Member)
                .Where(s => s is not null)
                .Select(s => s!)
                .ToArray();
            Console.WriteLine("[" + string.Join(", ", ids.Select(s => $"'{s}'")) + "]");
            // >>> ['pt:C', 'pt:B']
        }
```

##### Go

```go
	// Set attributes for filtering
	res24, err := rdb.VSetAttr(ctx, "points", "pt:A",
		map[string]interface{}{
			"size":  "large",
			"price": 18.99,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res24) // >>> true

	res25, err := rdb.VSetAttr(ctx, "points", "pt:B",
		map[string]interface{}{
			"size":  "large",
			"price": 35.99,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res25) // >>> true

	res26, err := rdb.VSetAttr(ctx, "points", "pt:C",
		map[string]interface{}{
			"size":  "large",
			"price": 25.99,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res26) // >>> true

	res27, err := rdb.VSetAttr(ctx, "points", "pt:D",
		map[string]interface{}{
			"size":  "small",
			"price": 21.00,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res27) // >>> true

	res28, err := rdb.VSetAttr(ctx, "points", "pt:E",
		map[string]interface{}{
			"size":  "small",
			"price": 17.75,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res28) // >>> true

	// Return elements in order of distance from point A whose
	// `size` attribute is `large`.
	res29, err := rdb.VSimWithArgs(ctx, "points",
		&redis.VectorRef{Name: "pt:A"},
		&redis.VSimArgs{Filter: `.size == "large"`},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res29) // >>> [pt:A pt:C pt:B]

	// Return elements in order of distance from point A whose size is
	// `large` and whose price is greater than 20.00.
	res30, err := rdb.VSimWithArgs(ctx, "points",
		&redis.VectorRef{Name: "pt:A"},
		&redis.VSimArgs{Filter: `.size == "large" && .price > 20.00`},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res30) // >>> [pt:C pt:B]

	res31, err := rdb.VIsMember(ctx, "points", "pt:A").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res31) // >>> true

	res32, err := rdb.VIsMember(ctx, "points", "pt:W").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res32) // >>> false

	res33, err := rdb.VSimWithArgsWithAttribs(ctx, "points",
		&redis.VectorRef{Name: "pt:A"},
		&redis.VSimArgs{Count: 1, Truth: true},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res33[0].Name, *res33[0].Attribs) // >>> pt:A {"price":18.99,"size":"large"}

	res34, err := rdb.VSimWithArgsWithScoresWithAttribs(ctx, "points",
		&redis.VectorRef{Name: "pt:A"},
		&redis.VSimArgs{Count: 1, Truth: true},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res34[0].Name, res34[0].Score, *res34[0].Attribs) // >>> pt:A 1 {"price":18.99,"size":"large"}
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> filteredSimilaritySearch = asyncCommands
                    .vsetattr("points", "pt:A", "{\"size\": \"large\", \"price\": 18.99}").thenCompose(result -> {
                        System.out.println(result); // >>> true
                        return asyncCommands.vsetattr("points", "pt:B", "{\"size\": \"large\", \"price\": 35.99}");
                    }).thenCompose(result -> {
                        System.out.println(result); // >>> true
                        return asyncCommands.vsetattr("points", "pt:C", "{\"size\": \"large\", \"price\": 25.99}");
                    }).thenCompose(result -> {
                        System.out.println(result); // >>> true
                        return asyncCommands.vsetattr("points", "pt:D", "{\"size\": \"small\", \"price\": 21.00}");
                    }).thenCompose(result -> {
                        System.out.println(result); // >>> true
                        return asyncCommands.vsetattr("points", "pt:E", "{\"size\": \"small\", \"price\": 17.75}");
                    }).thenCompose(result -> {
                        System.out.println(result); // >>> true

                        // Return elements in order of distance from point A whose size attribute is large.
                        VSimArgs filterArgs = new VSimArgs();
                        filterArgs.filter(".size == \"large\"");
                        return asyncCommands.vsim("points", filterArgs, "pt:A");
                    }).thenCompose(result -> {
                        System.out.println(result); // >>> [pt:A, pt:C, pt:B]

                        // Return elements in order of distance from point A whose size is large and price > 20.00.
                        VSimArgs filterArgs2 = new VSimArgs();
                        filterArgs2.filter(".size == \"large\" && .price > 20.00");
                        return asyncCommands.vsim("points", filterArgs2, "pt:A");
                    }).thenAccept(result -> {
                        System.out.println(result); // >>> [pt:C, pt:B]
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> filteredSimilaritySearch = reactiveCommands
                    .vsetattr("points", "pt:A", "{\"size\": \"large\", \"price\": 18.99}").doOnNext(result -> {
                        System.out.println(result); // >>> true
                    }).flatMap(result -> reactiveCommands.vsetattr("points", "pt:B", "{\"size\": \"large\", \"price\": 35.99}"))
                    .doOnNext(result -> {
                        System.out.println(result); // >>> true
                    }).flatMap(result -> reactiveCommands.vsetattr("points", "pt:C", "{\"size\": \"large\", \"price\": 25.99}"))
                    .doOnNext(result -> {
                        System.out.println(result); // >>> true
                    }).flatMap(result -> reactiveCommands.vsetattr("points", "pt:D", "{\"size\": \"small\", \"price\": 21.00}"))
                    .doOnNext(result -> {
                        System.out.println(result); // >>> true
                    }).flatMap(result -> reactiveCommands.vsetattr("points", "pt:E", "{\"size\": \"small\", \"price\": 17.75}"))
                    .doOnNext(result -> {
                        System.out.println(result); // >>> true
                    }).flatMap(result -> {
                        // Return elements in order of distance from point A whose size attribute is large.
                        VSimArgs filterArgs = new VSimArgs();
                        filterArgs.filter(".size == \"large\"");
                        return reactiveCommands.vsim("points", filterArgs, "pt:A").collectList();
                    }).doOnNext(result -> {
                        System.out.println(result); // >>> [pt:A, pt:C, pt:B]
                    }).flatMap(result -> {
                        // Return elements in order of distance from point A whose size is large and price > 20.00.
                        VSimArgs filterArgs2 = new VSimArgs();
                        filterArgs2.filter(".size == \"large\" && .price > 20.00");
                        return reactiveCommands.vsim("points", filterArgs2, "pt:A").collectList();
                    }).doOnNext(result -> {
                        System.out.println(result); // >>> [pt:C, pt:B]
                    }).then();
```

##### Java (Synchronous - Jedis)

```java
      boolean res24 = jedis.vsetattr("points", "pt:A", "{\"size\":\"large\",\"price\":18.99}");
      System.out.println(res24); // >>> true

      boolean res25 = jedis.vsetattr("points", "pt:B", "{\"size\":\"large\",\"price\":35.99}");
      System.out.println(res25); // >>> true

      boolean res26 = jedis.vsetattr("points", "pt:C", "{\"size\":\"large\",\"price\":25.99}");
      System.out.println(res26); // >>> true

      boolean res27 = jedis.vsetattr("points", "pt:D", "{\"size\":\"small\",\"price\":21.00}");
      System.out.println(res27); // >>> true

      boolean res28 = jedis.vsetattr("points", "pt:E", "{\"size\":\"small\",\"price\":17.75}");
      System.out.println(res28); // >>> true

      List<String> res29 = jedis.vsimByElement("points", "pt:A",
        new VSimParams().filter(".size == \"large\""));
      System.out.println(res29); // >>> ["pt:A", "pt:C", "pt:B"]

      List<String> res30 = jedis.vsimByElement("points", "pt:A",
        new VSimParams().filter(".size == \"large\" && .price > 20.00"));
      System.out.println(res30); // >>> ["pt:C", "pt:B"]
```

##### JavaScript (Node.js)

```javascript
const res24 = await client.vSetAttr("points", "pt:A", {
  size: "large",
  price: 18.99
});
console.log(res24);  // >>> true

const res25 = await client.vSetAttr("points", "pt:B", {
  size: "large",
  price: 35.99
});
console.log(res25);  // >>> true

const res26 = await client.vSetAttr("points", "pt:C", {
  size: "large",
  price: 25.99
});
console.log(res26);  // >>> true

const res27 = await client.vSetAttr("points", "pt:D", {
  size: "small",
  price: 21.00
});
console.log(res27);  // >>> true

const res28 = await client.vSetAttr("points", "pt:E", {
  size: "small",
  price: 17.75
});
console.log(res28);  // >>> true

// Return elements in order of distance from point A whose
// `size` attribute is `large`.
const res29 = await client.vSim("points", "pt:A", {
  FILTER: '.size == "large"'
});
console.log(res29);  // >>> ['pt:A', 'pt:C', 'pt:B']

// Return elements in order of distance from point A whose size is
// `large` and whose price is greater than 20.00.
const res30 = await client.vSim("points", "pt:A", {
  FILTER: '.size == "large" && .price > 20.00'
});
console.log(res30);  // >>> ['pt:C', 'pt:B']
```

##### PHP

```php
        $res24 = $r->vsetattr('points', 'pt:A', [
            'size' => 'large',
            'price' => 18.99
        ]);
        echo $res24 . PHP_EOL;
        // >>> 1

        $res25 = $r->vsetattr('points', 'pt:B', [
            'size' => 'large',
            'price' => 35.99
        ]);
        echo $res25 . PHP_EOL;
        // >>> 1

        $res26 = $r->vsetattr('points', 'pt:C', [
            'size' => 'large',
            'price' => 25.99
        ]);
        echo $res26 . PHP_EOL;
        // >>> 1

        $res27 = $r->vsetattr('points', 'pt:D', [
            'size' => 'small',
            'price' => 21.00
        ]);
        echo $res27 . PHP_EOL;
        // >>> 1

        $res28 = $r->vsetattr('points', 'pt:E', [
            'size' => 'small',
            'price' => 17.75
        ]);
        echo $res28 . PHP_EOL;
        // >>> 1

        // Return elements in order of distance from point A whose
        // `size` attribute is `large`.
        $res29 = $r->vsim(
            'points', 'pt:A',true, null, null, null, null,
            '.size == "large"'
        );
        echo json_encode($res29) . PHP_EOL;
        // >>> ["pt:A","pt:C","pt:B"]

        // Return elements in order of distance from point A whose size is
        // `large` and whose price is greater than 20.00.
        $res30 = $r->vsim(
            'points', 'pt:A',true, null, null, null, null,
            '.size == "large" && .price > 20.00'
        );
        echo json_encode($res30) . PHP_EOL;
        // >>> ["pt:C","pt:B"]
```

##### Python

```python
res24 = r.vset().vsetattr("points", "pt:A", {
    "size": "large",
    "price": 18.99
})
print(res24)  # >>> 1

res25 = r.vset().vsetattr("points", "pt:B", {
    "size": "large",
    "price": 35.99
})
print(res25)  # >>> 1

res26 = r.vset().vsetattr("points", "pt:C", {
    "size": "large",
    "price": 25.99
})
print(res26)  # >>> 1

res27 = r.vset().vsetattr("points", "pt:D", {
    "size": "small",
    "price": 21.00
})
print(res27)  # >>> 1

res28 = r.vset().vsetattr("points", "pt:E", {
    "size": "small",
    "price": 17.75
})
print(res28)  # >>> 1

# Return elements in order of distance from point A whose
# `size` attribute is `large`.
res29 = r.vset().vsim(
    "points", "pt:A",
    filter='.size == "large"'
)
print(res29)  # >>> ['pt:A', 'pt:C', 'pt:B']

# Return elements in order of distance from point A whose size is
# `large` and whose price is greater than 20.00.
res30 = r.vset().vsim(
    "points", "pt:A",
    filter='.size == "large" && .price > 20.00'
)
print(res30)  # >>> ['pt:C', 'pt:B']
```

##### Rust (Asynchronous)

```rust
        let res: bool = cmd("VSETATTR")
            .arg("points")
            .arg("pt:A")
            .arg("{\"size\":\"large\",\"price\":18.99}")
            .query_async(&mut r)
            .await
            .expect("VSETATTR A should succeed");
        println!("{res}"); // >>> true

        let res: bool = cmd("VSETATTR")
            .arg("points")
            .arg("pt:B")
            .arg("{\"size\":\"large\",\"price\":35.99}")
            .query_async(&mut r)
            .await
            .expect("VSETATTR B should succeed");
        println!("{res}"); // >>> true

        let res: bool = cmd("VSETATTR")
            .arg("points")
            .arg("pt:C")
            .arg("{\"size\":\"large\",\"price\":25.99}")
            .query_async(&mut r)
            .await
            .expect("VSETATTR C should succeed");
        println!("{res}"); // >>> true

        let res: bool = cmd("VSETATTR")
            .arg("points")
            .arg("pt:D")
            .arg("{\"size\":\"small\",\"price\":21.00}")
            .query_async(&mut r)
            .await
            .expect("VSETATTR D should succeed");
        println!("{res}"); // >>> true

        let res: bool = cmd("VSETATTR")
            .arg("points")
            .arg("pt:E")
            .arg("{\"size\":\"small\",\"price\":17.75}")
            .query_async(&mut r)
            .await
            .expect("VSETATTR E should succeed");
        println!("{res}"); // >>> true

        let opts = VSimOptions::default().set_filter_expression(".size == \"large\"");
        if let Ok(res) = r
            .vsim_options("points", VectorSimilaritySearchInput::Element("pt:A"), &opts)
            .await
        {
            let res: Value = res;
            if let Value::Array(items) = res {
                let view: Vec<String> = items
                    .into_iter()
                    .map(|item| match item {
                        Value::BulkString(bytes) => String::from_utf8(bytes).expect("utf8"),
                        Value::SimpleString(s) => s,
                        other => panic!("Unexpected VSIM item: {other:?}"),
                    })
                    .collect();
                println!("{view:?}");
                // >>> ["pt:A", "pt:C", "pt:B"]
            }
        }

        let opts = VSimOptions::default()
            .set_filter_expression(".size == \"large\" && .price > 20.00");
        if let Ok(res) = r
            .vsim_options("points", VectorSimilaritySearchInput::Element("pt:A"), &opts)
            .await
        {
            let res: Value = res;
            if let Value::Array(items) = res {
                let view: Vec<String> = items
                    .into_iter()
                    .map(|item| match item {
                        Value::BulkString(bytes) => String::from_utf8(bytes).expect("utf8"),
                        Value::SimpleString(s) => s,
                        other => panic!("Unexpected VSIM item: {other:?}"),
                    })
                    .collect();
                println!("{view:?}");
                // >>> ["pt:C", "pt:B"]
            }
        }
```

##### Rust (Synchronous)

```rust
        let res: bool = cmd("VSETATTR")
            .arg("points")
            .arg("pt:A")
            .arg("{\"size\":\"large\",\"price\":18.99}")
            .query(&mut r)
            .expect("VSETATTR A should succeed");
        println!("{res}"); // >>> true

        let res: bool = cmd("VSETATTR")
            .arg("points")
            .arg("pt:B")
            .arg("{\"size\":\"large\",\"price\":35.99}")
            .query(&mut r)
            .expect("VSETATTR B should succeed");
        println!("{res}"); // >>> true

        let res: bool = cmd("VSETATTR")
            .arg("points")
            .arg("pt:C")
            .arg("{\"size\":\"large\",\"price\":25.99}")
            .query(&mut r)
            .expect("VSETATTR C should succeed");
        println!("{res}"); // >>> true

        let res: bool = cmd("VSETATTR")
            .arg("points")
            .arg("pt:D")
            .arg("{\"size\":\"small\",\"price\":21.00}")
            .query(&mut r)
            .expect("VSETATTR D should succeed");
        println!("{res}"); // >>> true

        let res: bool = cmd("VSETATTR")
            .arg("points")
            .arg("pt:E")
            .arg("{\"size\":\"small\",\"price\":17.75}")
            .query(&mut r)
            .expect("VSETATTR E should succeed");
        println!("{res}"); // >>> true

        let opts = VSimOptions::default().set_filter_expression(".size == \"large\"");
        if let Ok(res) =
            r.vsim_options("points", VectorSimilaritySearchInput::Element("pt:A"), &opts)
        {
            let res: Value = res;
            if let Value::Array(items) = res {
                let view: Vec<String> = items
                    .into_iter()
                    .map(|item| match item {
                        Value::BulkString(bytes) => String::from_utf8(bytes).expect("utf8"),
                        Value::SimpleString(s) => s,
                        other => panic!("Unexpected VSIM item: {other:?}"),
                    })
                    .collect();
                println!("{view:?}");
                // >>> ["pt:A", "pt:C", "pt:B"]
            }
        }

        let opts = VSimOptions::default()
            .set_filter_expression(".size == \"large\" && .price > 20.00");
        if let Ok(res) =
            r.vsim_options("points", VectorSimilaritySearchInput::Element("pt:A"), &opts)
        {
            let res: Value = res;
            if let Value::Array(items) = res {
                let view: Vec<String> = items
                    .into_iter()
                    .map(|item| match item {
                        Value::BulkString(bytes) => String::from_utf8(bytes).expect("utf8"),
                        Value::SimpleString(s) => s,
                        other => panic!("Unexpected VSIM item: {other:?}"),
                    })
                    .collect();
                println!("{view:?}");
                // >>> ["pt:C", "pt:B"]
            }
        }
```


&nbsp;
> [!NOTE] Try it out
> Experiment with vector set commands interactively in the [Redis playground](https://redis.io/try/sandbox) — no installation required.

## More information

See the other pages in this section to learn more about the features
and performance parameters of vector sets.

