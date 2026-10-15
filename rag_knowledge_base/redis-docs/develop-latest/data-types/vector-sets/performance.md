# Performance

```json metadata
{
  "schema_version": 2,
  "title": "Performance",
  "description": "Learn how Redis vector sets behave under load and how to optimize for speed and recall",
  "categories": ["docs","develop","stack","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"query-performance","title":"Query performance"},{"id":"insertion-performance","title":"Insertion performance"},{"id":"quantization-effects","title":"Quantization effects"},{"id":"deletion-performance","title":"Deletion performance"},{"id":"save-and-load-performance","title":"Save and load performance"},{"id":"summary-of-tuning-tips","title":"Summary of tuning tips"},{"id":"see-also","title":"See also"}]}

,
  "codeExamples": [{"codetabsId":"vecset_tutorial-stepadd_quant","commands":[{"name":"VADD"},{"name":"VEMB"}],"description":"Quantization modes: Compare Q8, NOQUANT, and BIN quantization modes using VADD and VEMB to understand the tradeoffs between precision, memory, and performance","difficulty":"advanced","id":"add_quant","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_vecset_tutorial-stepadd_quant"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_vecset_tutorial-stepadd_quant"},{"id":"Node-js","panelId":"panel_Nodejs_vecset_tutorial-stepadd_quant"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_vecset_tutorial-stepadd_quant"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_vecset_tutorial-stepadd_quant"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_vecset_tutorial-stepadd_quant"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_vecset_tutorial-stepadd_quant"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_vecset_tutorial-stepadd_quant"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_vecset_tutorial-stepadd_quant"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_vecset_tutorial-stepadd_quant"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_vecset_tutorial-stepadd_quant"}]}]
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


## Query performance

Vector similarity queries using the [`VSIM`](https://redis.io/docs/latest/commands/vsim) are threaded by default. Redis uses up to 32 threads to process these queries in parallel.

- `VSIM` performance scales nearly linearly with available CPU cores.
- Expect ~50,000 similarity queries per second for a 3M-item set with 300-dim vectors using int8 quantization.
- Performance depends heavily on the `EF` parameter:
  - Higher `EF` improves recall, but slows down search.
  - Lower `EF` returns faster results with reduced accuracy.

## Insertion performance

Inserting vectors with the [`VADD`](https://redis.io/docs/latest/commands/vadd) command is more computationally expensive than querying:

- Insertion is single-threaded by default.
- Use the `CAS` option to offload candidate graph search to a background thread.
- Expect a few thousand insertions per second on a single node.

## Quantization effects

Quantization greatly impacts both speed and memory:

- `Q8` (default): 4x smaller than `FP32`, high recall, high speed
- `BIN` (binary): 32x smaller than `FP32`, lower recall, fastest search
- `NOQUANT` (`FP32`): Full precision, slower performance, highest memory use

Use the quantization mode that best fits your tradeoff between precision and efficiency.
The examples below show how the different modes affect a simple vector.
Note that even with `NOQUANT` mode, the values change slightly,
due to floating point rounding.

Quantization modes: Compare Q8, NOQUANT, and BIN quantization modes using VADD and VEMB to understand the tradeoffs between precision, memory, and performance

**Difficulty:** Advanced

**Commands:** VADD, VEMB

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> VADD quantSetQ8 VALUES 2 1.262185 1.958231 quantElement Q8
(integer) 1
> VEMB quantSetQ8 quantElement
1) "1.2643694877624512"
2) "1.958230972290039"

> VADD quantSetNoQ VALUES 2 1.262185 1.958231 quantElement NOQUANT
(integer) 1
> VEMB quantSetNoQ quantElement
1) "1.262184977531433"
2) "1.958230972290039"

> VADD quantSetBin VALUES 2 1.262185 1.958231 quantElement BIN
(integer) 1
> VEMB quantSetBin quantElement
1) "1"
2) "1"
```

##### C#

```csharp
        VectorSetAddRequest addInt8 = VectorSetAddRequest.Member("quantElement", new float[] { 1.262185f, 1.958231f }, null);
        addInt8.Quantization = VectorSetQuantization.Int8;
        bool q8Added = db.VectorSetAdd("quantSetQ8", addInt8);
        Console.WriteLine(q8Added); // >>> True
        using (Lease<float>? eInt8 = db.VectorSetGetApproximateVector("quantSetQ8", "quantElement"))
        {
            Span<float> v = eInt8!.Span;
            Console.WriteLine($"Q8: [{v[0]}, {v[1]}]");
            // >>> Q8: [1.2643694877624512, 1.958230972290039]
        }

        VectorSetAddRequest addNone = VectorSetAddRequest.Member("quantElement", new float[] { 1.262185f, 1.958231f }, null);
        addNone.Quantization = VectorSetQuantization.None;
        bool noQuantAdded = db.VectorSetAdd("quantSetNoQ", addNone);
        Console.WriteLine(noQuantAdded); // >>> True
        using (Lease<float>? eNone = db.VectorSetGetApproximateVector("quantSetNoQ", "quantElement"))
        {
            Span<float> v = eNone!.Span;
            Console.WriteLine($"NOQUANT: [{v[0]}, {v[1]}]");
            // >>> NOQUANT: [1.262184977531433, 1.958230972290039]
        }

        VectorSetAddRequest addBinary = VectorSetAddRequest.Member("quantElement", new float[] { 1.262185f, 1.958231f }, null);
        addBinary.Quantization = VectorSetQuantization.Binary;
        bool binAdded = db.VectorSetAdd("quantSetBin", addBinary);
        Console.WriteLine(binAdded); // >>> True
        using (Lease<float>? eBinary = db.VectorSetGetApproximateVector("quantSetBin", "quantElement"))
        {
            Span<float> v = eBinary!.Span;
            Console.WriteLine($"BIN: [{v[0]}, {v[1]}]");
            // >>> BIN: [1, 1]
        }
```

##### Go

```go
	// Add with Q8 quantization
	vecQ := &redis.VectorValues{Val: []float64{1.262185, 1.958231}}

	res1, err := rdb.VAddWithArgs(ctx, "quantSetQ8", "quantElement", vecQ,
		&redis.VAddArgs{
			Q8: true,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // >>> true

	embQ8, err := rdb.VEmb(ctx, "quantSetQ8", "quantElement", false).Result()

	if err != nil {
		panic(err)
	}

	fmt.Printf("Q8 embedding: %v\n", embQ8)
	// >>> Q8 embedding: [1.2621850967407227 1.9582309722900391]

	// Add with NOQUANT option
	res2, err := rdb.VAddWithArgs(ctx, "quantSetNoQ", "quantElement", vecQ,
		&redis.VAddArgs{
			NoQuant: true,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2) // >>> true

	embNoQ, err := rdb.VEmb(ctx, "quantSetNoQ", "quantElement", false).Result()

	if err != nil {
		panic(err)
	}

	fmt.Printf("NOQUANT embedding: %v\n", embNoQ)
	// >>> NOQUANT embedding: [1.262185 1.958231]

	// Add with BIN quantization
	res3, err := rdb.VAddWithArgs(ctx, "quantSetBin", "quantElement", vecQ,
		&redis.VAddArgs{
			Bin: true,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3) // >>> true

	embBin, err := rdb.VEmb(ctx, "quantSetBin", "quantElement", false).Result()

	if err != nil {
		panic(err)
	}

	fmt.Printf("BIN embedding: %v\n", embBin)
	// >>> BIN embedding: [1 1]
```

##### Java (Asynchronous - Lettuce)

```java
            VAddArgs q8Args = VAddArgs.Builder.quantizationType(QuantizationType.Q8);
            CompletableFuture<Void> quantizationOperations = asyncCommands
                    .vadd("quantSetQ8", "quantElement", q8Args, 1.262185, 1.958231).thenCompose(result -> {
                        System.out.println(result); // >>> true
                        return asyncCommands.vemb("quantSetQ8", "quantElement");
                    }).thenCompose(result -> {
                        System.out.println("Q8: " + result); // >>> Q8: [1.2643694877624512, 1.958230972290039]

                        VAddArgs noQuantArgs = VAddArgs.Builder.quantizationType(QuantizationType.NO_QUANTIZATION);
                        return asyncCommands.vadd("quantSetNoQ", "quantElement", noQuantArgs, 1.262185, 1.958231);
                    }).thenCompose(result -> {
                        System.out.println(result); // >>> true
                        return asyncCommands.vemb("quantSetNoQ", "quantElement");
                    }).thenCompose(result -> {
                        System.out.println("NOQUANT: " + result); // >>> NOQUANT: [1.262184977531433, 1.958230972290039]

                        VAddArgs binArgs = VAddArgs.Builder.quantizationType(QuantizationType.BINARY);
                        return asyncCommands.vadd("quantSetBin", "quantElement", binArgs, 1.262185, 1.958231);
                    }).thenCompose(result -> {
                        System.out.println(result); // >>> true
                        return asyncCommands.vemb("quantSetBin", "quantElement");
                    }).thenAccept(result -> {
                        System.out.println("BIN: " + result); // >>> BIN: [1.0, 1.0]
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            VAddArgs q8Args = VAddArgs.Builder.quantizationType(QuantizationType.Q8);
            Mono<Void> quantizationOperations = reactiveCommands.vadd("quantSetQ8", "quantElement", q8Args, 1.262185, 1.958231)
                    .doOnNext(result -> {
                        System.out.println(result); // >>> true
                    }).flatMap(result -> reactiveCommands.vemb("quantSetQ8", "quantElement").collectList()).doOnNext(result -> {
                        System.out.println("Q8: " + result); // >>> Q8: [1.2643694877624512, 1.958230972290039]
                    }).flatMap(result -> {
                        VAddArgs noQuantArgs = VAddArgs.Builder.quantizationType(QuantizationType.NO_QUANTIZATION);
                        return reactiveCommands.vadd("quantSetNoQ", "quantElement", noQuantArgs, 1.262185, 1.958231);
                    }).doOnNext(result -> {
                        System.out.println(result); // >>> true
                    }).flatMap(result -> reactiveCommands.vemb("quantSetNoQ", "quantElement").collectList())
                    .doOnNext(result -> {
                        System.out.println("NOQUANT: " + result); // >>> NOQUANT: [1.262184977531433, 1.958230972290039]
                    }).flatMap(result -> {
                        VAddArgs binArgs = VAddArgs.Builder.quantizationType(QuantizationType.BINARY);
                        return reactiveCommands.vadd("quantSetBin", "quantElement", binArgs, 1.262185, 1.958231);
                    }).doOnNext(result -> {
                        System.out.println(result); // >>> true
                    }).flatMap(result -> reactiveCommands.vemb("quantSetBin", "quantElement").collectList())
                    .doOnNext(result -> {
                        System.out.println("BIN: " + result); // >>> BIN: [1.0, 1.0]
                    }).then();
```

##### Java (Synchronous - Jedis)

```java
      boolean res31 = jedis.vadd("quantSetQ8", new float[] { 1.262185f, 1.958231f }, "quantElement",
        new VAddParams().q8());
      System.out.println(res31); // >>> true

      List<Double> res32 = jedis.vemb("quantSetQ8", "quantElement");
      System.out.println("Q8: " + res32);
      // >>> Q8: [~1.264, ~1.958]

      boolean res33 = jedis.vadd("quantSetNoQ", new float[] { 1.262185f, 1.958231f },
        "quantElement", new VAddParams().noQuant());
      System.out.println(res33); // >>> true

      List<Double> res34 = jedis.vemb("quantSetNoQ", "quantElement");
      System.out.println("NOQUANT: " + res34);
      // >>> NOQUANT: [~1.262185, ~1.958231]

      boolean res35 = jedis.vadd("quantSetBin", new float[] { 1.262185f, 1.958231f },
        "quantElement", new VAddParams().bin());
      System.out.println(res35); // >>> true

      List<Double> res36 = jedis.vemb("quantSetBin", "quantElement");
      System.out.println("BIN: " + res36);
      // >>> BIN: [1, 1]
```

##### JavaScript (Node.js)

```javascript
const res31 = await client.vAdd("quantSetQ8", [1.262185, 1.958231], "quantElement", {
  QUANT: 'Q8'
});
console.log(res31);  // >>> true

const res32 = await client.vEmb("quantSetQ8", "quantElement");
console.log(`Q8: ${res32}`);
// >>> Q8: [1.2643694877624512, 1.958230972290039]

const res33 = await client.vAdd("quantSetNoQ", [1.262185, 1.958231], "quantElement", {
  QUANT: 'NOQUANT'
});
console.log(res33);  // >>> true

const res34 = await client.vEmb("quantSetNoQ", "quantElement");
console.log(`NOQUANT: ${res34}`);
// >>> NOQUANT: [1.262184977531433, 1.958230972290039]

const res35 = await client.vAdd("quantSetBin", [1.262185, 1.958231], "quantElement", {
  QUANT: 'BIN'
});
console.log(res35);  // >>> true

const res36 = await client.vEmb("quantSetBin", "quantElement");
console.log(`BIN: ${res36}`);
// >>> BIN: [1, 1]
```

##### PHP

```php
        $res31 = $r->vadd('quantSetQ8', [1.262185, 1.958231], 'quantElement', null, false,
            Predis\Command\Redis\VADD::QUANT_Q8
        );
        echo $res31 . PHP_EOL;
        // >>> 1

        $res32 = $r->vemb('quantSetQ8', 'quantElement');
        echo json_encode($res32) . PHP_EOL;
        // >>> [1.2643694877624512, 1.958230972290039]

        $res33 = $r->vadd('quantSetNoQ', [1.262185, 1.958231], 'quantElement', null, false,
            Predis\Command\Redis\VADD::QUANT_NOQUANT
        );
        echo $res33 . PHP_EOL;
        // >>> 1

        $res34 = $r->vemb('quantSetNoQ', 'quantElement');
        echo json_encode($res34) . PHP_EOL;
        // >>> [1.262184977531433, 1.958230972290039]

        $res35 = $r->vadd('quantSetBin', [1.262185, 1.958231], 'quantElement', null, false,
            Predis\Command\Redis\VADD::QUANT_BIN
        );
        echo $res35 . PHP_EOL;
        // >>> 1

        $res36 = $r->vemb('quantSetBin', 'quantElement');
        echo json_encode($res36) . PHP_EOL;
        // >>> [1, 1]
```

##### Python

```python
# Import `QuantizationOptions` enum using:
#
# from redis.commands.vectorset.commands import (
#   QuantizationOptions
# )
res31 = r.vset().vadd(
    "quantSetQ8", [1.262185, 1.958231],
    "quantElement",
    quantization=QuantizationOptions.Q8
)
print(res31)  # >>> 1

res32 = r.vset().vemb("quantSetQ8", "quantElement")
print(f"Q8: {res32}")
# >>> Q8: [1.2643694877624512, 1.958230972290039]

res33 = r.vset().vadd(
    "quantSetNoQ", [1.262185, 1.958231],
    "quantElement",
    quantization=QuantizationOptions.NOQUANT
)
print(res33)  # >>> 1

res34 = r.vset().vemb("quantSetNoQ", "quantElement")
print(f"NOQUANT: {res34}")
# >>> NOQUANT: [1.262184977531433, 1.958230972290039]

res35 = r.vset().vadd(
    "quantSetBin", [1.262185, 1.958231],
    "quantElement",
    quantization=QuantizationOptions.BIN
)
print(res35)  # >>> 1

res36 = r.vset().vemb("quantSetBin", "quantElement")
print(f"BIN: {res36}")
# >>> BIN: [1, 1]
```

##### Rust (Asynchronous)

```rust
        let opts = VAddOptions::default().set_quantization(VectorQuantization::Q8);
        if let Ok(res) = r
            .vadd_options(
                "quantSetQ8",
                VectorAddInput::Values(EmbeddingInput::Float64(&[1.262185, 1.958231])),
                "quantElement",
                &opts,
            )
            .await
        {
            let res: bool = res;
            println!("{res}"); // >>> true
        }

        if let Ok(res) = r.vemb("quantSetQ8", "quantElement").await {
            let res: Vec<f64> = res;
            println!("{res:?}");
            // >>> [1.2643694877624512, 1.958230972290039]
        }

        let opts = VAddOptions::default().set_quantization(VectorQuantization::NoQuant);
        if let Ok(res) = r
            .vadd_options(
                "quantSetNoQ",
                VectorAddInput::Values(EmbeddingInput::Float64(&[1.262185, 1.958231])),
                "quantElement",
                &opts,
            )
            .await
        {
            let res: bool = res;
            println!("{res}"); // >>> true
        }

        if let Ok(res) = r.vemb("quantSetNoQ", "quantElement").await {
            let res: Vec<f64> = res;
            println!("{res:?}");
            // >>> [1.262184977531433, 1.958230972290039]
        }

        let opts = VAddOptions::default().set_quantization(VectorQuantization::Bin);
        if let Ok(res) = r
            .vadd_options(
                "quantSetBin",
                VectorAddInput::Values(EmbeddingInput::Float64(&[1.262185, 1.958231])),
                "quantElement",
                &opts,
            )
            .await
        {
            let res: bool = res;
            println!("{res}"); // >>> true
        }

        if let Ok(res) = r.vemb("quantSetBin", "quantElement").await {
            let res: Vec<f64> = res;
            println!("{res:?}"); // >>> [1.0, 1.0]
        }
```

##### Rust (Synchronous)

```rust
        let opts = VAddOptions::default().set_quantization(VectorQuantization::Q8);
        if let Ok(res) = r.vadd_options(
            "quantSetQ8",
            VectorAddInput::Values(EmbeddingInput::Float64(&[1.262185, 1.958231])),
            "quantElement",
            &opts,
        ) {
            let res: bool = res;
            println!("{res}"); // >>> true
        }

        if let Ok(res) = r.vemb("quantSetQ8", "quantElement") {
            let res: Vec<f64> = res;
            println!("{res:?}");
            // >>> [1.2643694877624512, 1.958230972290039]
        }

        let opts = VAddOptions::default().set_quantization(VectorQuantization::NoQuant);
        if let Ok(res) = r.vadd_options(
            "quantSetNoQ",
            VectorAddInput::Values(EmbeddingInput::Float64(&[1.262185, 1.958231])),
            "quantElement",
            &opts,
        ) {
            let res: bool = res;
            println!("{res}"); // >>> true
        }

        if let Ok(res) = r.vemb("quantSetNoQ", "quantElement") {
            let res: Vec<f64> = res;
            println!("{res:?}");
            // >>> [1.262184977531433, 1.958230972290039]
        }

        let opts = VAddOptions::default().set_quantization(VectorQuantization::Bin);
        if let Ok(res) = r.vadd_options(
            "quantSetBin",
            VectorAddInput::Values(EmbeddingInput::Float64(&[1.262185, 1.958231])),
            "quantElement",
            &opts,
        ) {
            let res: bool = res;
            println!("{res}"); // >>> true
        }

        if let Ok(res) = r.vemb("quantSetBin", "quantElement") {
            let res: Vec<f64> = res;
            println!("{res:?}"); // >>> [1.0, 1.0]
        }
```



## Deletion performance

Deleting large vector sets using the [`DEL`](https://redis.io/docs/latest/commands/del) can cause latency spikes:

- Redis must unlink and restructure many graph nodes.
- Latency is most noticeable when deleting millions of elements.

## Save and load performance

Vector sets save and load the full HNSW graph structure:

- When reloading from disk is fast and there's no need to rebuild the graph.

Example: A 3M vector set with 300 components loads in ~15 seconds.

## Summary of tuning tips

| Factor     | Effect on performance               | Tip                                            |
|------------|-------------------------------------|------------------------------------------------|
| `EF`       | Slower queries but higher recall    | Start low (for example, 200) and tune upward           |
| `M`        | More memory per node, better recall | Use defaults unless recall is too low          |
| Quant type | Binary is fastest, `FP32` is slowest| Use `Q8` or `BIN` unless full precision needed |
| `CAS`      | Faster insertions with threading    | Use when high write throughput is needed       |

## See also

- [Memory usage](https://redis.io/docs/latest/develop/data-types/vector-sets/memory)
- [Scalability](https://redis.io/docs/latest/develop/data-types/vector-sets/scalability)
- [Filtered search](https://redis.io/docs/latest/develop/data-types/vector-sets/filtered-search)

