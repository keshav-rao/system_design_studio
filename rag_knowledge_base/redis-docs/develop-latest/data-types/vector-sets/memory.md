# Memory optimization

```json metadata
{
  "schema_version": 2,
  "title": "Memory optimization",
  "description": "Learn how to optimize memory consumption in Redis vector sets",
  "categories": ["docs","develop","stack","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"overview","title":"Overview"},{"id":"quantization-modes","title":"Quantization modes"},{"id":"graph-structure-memory","title":"Graph structure memory"},{"id":"attribute-and-label-size","title":"Attribute and label size"},{"id":"vector-dimension","title":"Vector dimension"},{"id":"summary","title":"Summary"},{"id":"see-also","title":"See also"}]}

,
  "codeExamples": [{"codetabsId":"vecset_tutorial-stepadd_reduce","commands":[{"name":"VDIM"}],"description":"Dimension reduction: Use the REDUCE option with VADD to apply random projection and reduce vector dimensions when you need to optimize memory usage while maintaining search quality","difficulty":"advanced","id":"add_reduce","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_vecset_tutorial-stepadd_reduce"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_vecset_tutorial-stepadd_reduce"},{"id":"Node-js","panelId":"panel_Nodejs_vecset_tutorial-stepadd_reduce"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_vecset_tutorial-stepadd_reduce"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_vecset_tutorial-stepadd_reduce"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_vecset_tutorial-stepadd_reduce"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_vecset_tutorial-stepadd_reduce"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_vecset_tutorial-stepadd_reduce"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_vecset_tutorial-stepadd_reduce"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_vecset_tutorial-stepadd_reduce"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_vecset_tutorial-stepadd_reduce"}]}]
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


## Overview

Redis vector sets are efficient, but vector similarity indexing and graph traversal require memory tradeoffs. This guide helps you manage memory use through quantization, graph tuning, and attribute choices.

## Quantization modes

Vector sets support three quantization levels:

| Mode       | Memory usage  | Recall | Notes                           |
|------------|---------------|--------|---------------------------------|
| `Q8`       | 4x smaller    | High   | Default, fast and accurate      |
| `BIN`      | 32x smaller   | Lower  | Fastest, best for coarse search |
| `NOQUANT`  | Full size     | Highest| Best precision, slowest         |

Use `Q8` unless your use case demands either ultra-precision (use `NOQUANT`) or ultra-efficiency (use `BIN`).

## Graph structure memory

HNSW graphs store multiple connections per node. Each node:

- Has an average of `M * 2 + M * 0.33` pointers (default M = 16).
- Stores pointers using 8 bytes each.
- Allocates ~1.33 layers per node.

> A single node with M = 64 may consume ~1 KB in links alone.

To reduce memory:

- Lower `M` to shrink per-node connections.
- Avoid unnecessarily large values for `M` unless recall needs to be improved.

## Attribute and label size

Each node stores:

- A string label (element name)
- Optional JSON attribute string

Tips:

- Use short, fixed-length strings for labels.
- Keep attribute JSON minimal and flat. For example, use `{"year":2020}` instead of nested data.

## Vector dimension

High-dimensional vectors increase storage:

- 300 components at `FP32` = 1200 bytes/vector
- 300 components at `Q8` = 300 bytes/vector

You can reduce this using the `REDUCE` option during [`VADD`](https://redis.io/docs/latest/commands/vadd), which applies [random projection](https://en.wikipedia.org/wiki/Random_projection):

Dimension reduction: Use the REDUCE option with VADD to apply random projection and reduce vector dimensions when you need to optimize memory usage while maintaining search quality

**Difficulty:** Advanced

**Commands:** VDIM

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
>VADD setNotReduced VALUES 300 ... element
(integer) 1
> VDIM setNotReduced
(integer) 300

>VADD setReduced REDUCE 100 VALUES 300 ... element
(integer) 1
> VDIM setReduced
(integer) 100
```

##### C#

```csharp
        float[] values = Enumerable.Range(0, 300).Select(x => (float)(x / 299.0)).ToArray();
        bool addedNotReduced = db.VectorSetAdd("setNotReduced", VectorSetAddRequest.Member("element", values, null));
        Console.WriteLine(addedNotReduced); // >>> True
        Console.WriteLine(db.VectorSetDimension("setNotReduced")); // >>> 300

        VectorSetAddRequest addReduced = VectorSetAddRequest.Member("element", values, null);
        addReduced.ReducedDimensions = 100;
        bool addedReduced = db.VectorSetAdd("setReduced", addReduced);
        Console.WriteLine(addedReduced); // >>> True
        Console.WriteLine(db.VectorSetDimension("setReduced")); // >>> 100
```

##### Go

```go
	// Create a vector with 300 dimensions
	values := make([]float64, 300)

	for i := 0; i < 300; i++ {
		values[i] = float64(i) / 299
	}

	vecLarge := &redis.VectorValues{Val: values}

	// Add without reduction
	res1, err := rdb.VAdd(ctx, "setNotReduced", "element", vecLarge).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // >>> true

	dim1, err := rdb.VDim(ctx, "setNotReduced").Result()

	if err != nil {
		panic(err)
	}

	fmt.Printf("Dimension without reduction: %d\n", dim1)
	// >>> Dimension without reduction: 300

	// Add with reduction to 100 dimensions
	res2, err := rdb.VAddWithArgs(ctx, "setReduced", "element", vecLarge,
		&redis.VAddArgs{
			Reduce: 100,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2) // >>> true

	dim2, err := rdb.VDim(ctx, "setReduced").Result()

	if err != nil {
		panic(err)
	}

	fmt.Printf("Dimension after reduction: %d\n", dim2)
	// >>> Dimension after reduction: 100
```

##### Java (Asynchronous - Lettuce)

```java
            // Create a list of 300 arbitrary values.
            Double[] values = new Double[300];
            for (int i = 0; i < 300; i++) {
                values[i] = (double) i / 299;
            }

            CompletableFuture<Void> dimensionalityReductionOperations = asyncCommands.vadd("setNotReduced", "element", values)
                    .thenCompose(result -> {
                        System.out.println(result); // >>> true
                        return asyncCommands.vdim("setNotReduced");
                    }).thenCompose(result -> {
                        System.out.println(result); // >>> 300
                        return asyncCommands.vadd("setReduced", 100, "element", values);
                    }).thenCompose(result -> {
                        System.out.println(result); // >>> true
                        return asyncCommands.vdim("setReduced");
                    }).thenAccept(result -> {
                        System.out.println(result); // >>> 100
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            // Create a list of 300 arbitrary values.
            Double[] values = new Double[300];
            for (int i = 0; i < 300; i++) {
                values[i] = (double) i / 299;
            }

            Mono<Void> dimensionalityReductionOperations = reactiveCommands.vadd("setNotReduced", "element", values)
                    .doOnNext(result -> {
                        System.out.println(result); // >>> true
                    }).flatMap(result -> reactiveCommands.vdim("setNotReduced")).doOnNext(result -> {
                        System.out.println(result); // >>> 300
                    }).flatMap(result -> reactiveCommands.vadd("setReduced", 100, "element", values)).doOnNext(result -> {
                        System.out.println(result); // >>> true
                    }).flatMap(result -> reactiveCommands.vdim("setReduced")).doOnNext(result -> {
                        System.out.println(result); // >>> 100
                    }).then();
```

##### Java (Synchronous - Jedis)

```java
      float[] values = new float[300];
      for (int i = 0; i < 300; i++)
        values[i] = i / 299.0f;

      boolean res37 = jedis.vadd("setNotReduced", values, "element");
      System.out.println(res37); // >>> true

      long res38 = jedis.vdim("setNotReduced");
      System.out.println(res38); // >>> 300

      boolean res39 = jedis.vadd("setReduced", values, "element", 100, new VAddParams());
      System.out.println(res39); // >>> true

      long res40 = jedis.vdim("setReduced");
      System.out.println(res40); // >>> 100
```

##### JavaScript (Node.js)

```javascript
// Create a list of 300 arbitrary values.
const values = Array.from({length: 300}, (_, x) => x / 299);

const res37 = await client.vAdd("setNotReduced", values, "element");
console.log(res37);  // >>> true

const res38 = await client.vDim("setNotReduced");
console.log(res38);  // >>> 300

const res39 = await client.vAdd("setReduced", values, "element", {
  REDUCE: 100
});
console.log(res39);  // >>> true

const res40 = await client.vDim("setReduced");
console.log(res40);  // >>> 100
```

##### PHP

```php
        $values = array();

        for ($i = 0; $i < 300; $i++) {
            $values[] = $i / 299.0;
        }

        $res37 = $r->vadd('setNotReduced', $values, 'element');
        echo $res37 . PHP_EOL;
        // >>> 1

        $res38 = $r->vdim('setNotReduced');
        echo $res38 . PHP_EOL;
        // >>> 300

        $res39 = $r->vadd('setReduced', $values, 'element', 100);
        echo $res39 . PHP_EOL;
        // >>> 1

        $res40 = $r->vdim('setReduced');
        echo $res40 . PHP_EOL;
        // >>> 100
```

##### Python

```python
# Create a list of 300 arbitrary values.
values = [x / 299 for x in range(300)]

res37 = r.vset().vadd(
    "setNotReduced",
    values,
    "element"
)
print(res37)  # >>> 1

res38 = r.vset().vdim("setNotReduced")
print(res38)  # >>> 300

res39 = r.vset().vadd(
    "setReduced",
    values,
    "element",
    reduce_dim=100
)
print(res39)  # >>> 1

res40 = r.vset().vdim("setReduced")  # >>> 100
print(res40)
```

##### Rust (Asynchronous)

```rust
        let values: Vec<f64> = (0..300).map(|i| i as f64 / 299.0).collect();

        if let Ok(res) = r
            .vadd(
                "setNotReduced",
                VectorAddInput::Values(EmbeddingInput::Float64(&values)),
                "element",
            )
            .await
        {
            let res: bool = res;
            println!("{res}"); // >>> true
        }

        if let Ok(res) = r.vdim("setNotReduced").await {
            let res: usize = res;
            println!("{res}"); // >>> 300
        }

        let opts = VAddOptions::default().set_reduction_dimension(100);
        if let Ok(res) = r
            .vadd_options(
                "setReduced",
                VectorAddInput::Values(EmbeddingInput::Float64(&values)),
                "element",
                &opts,
            )
            .await
        {
            let res: bool = res;
            println!("{res}"); // >>> true
        }

        if let Ok(res) = r.vdim("setReduced").await {
            let res: usize = res;
            println!("{res}"); // >>> 100
        }
```

##### Rust (Synchronous)

```rust
        let values: Vec<f64> = (0..300).map(|i| i as f64 / 299.0).collect();

        if let Ok(res) = r.vadd(
            "setNotReduced",
            VectorAddInput::Values(EmbeddingInput::Float64(&values)),
            "element",
        ) {
            let res: bool = res;
            println!("{res}"); // >>> true
        }

        if let Ok(res) = r.vdim("setNotReduced") {
            let res: usize = res;
            println!("{res}"); // >>> 300
        }

        let opts = VAddOptions::default().set_reduction_dimension(100);
        if let Ok(res) = r.vadd_options(
            "setReduced",
            VectorAddInput::Values(EmbeddingInput::Float64(&values)),
            "element",
            &opts,
        ) {
            let res: bool = res;
            println!("{res}"); // >>> true
        }

        if let Ok(res) = r.vdim("setReduced") {
            let res: usize = res;
            println!("{res}"); // >>> 100
        }
```



This projects a 300-dimensional vector into 100 dimensions, reducing size and improving speed at the cost of some recall.

## Summary

| Strategy            | Effect                                   |
|---------------------|------------------------------------------|
| Use `Q8`            | Best tradeoff for most use cases         |
| Use `BIN`           | Minimal memory, fastest search           |
| Lower `M`           | Shrinks HNSW link graph size             |
| Reduce dimensions   | Cuts memory per vector                   |
| Minimize JSON       | Smaller attributes, less memory per node |

## See also

- [Performance](https://redis.io/docs/latest/develop/data-types/vector-sets/performance)
- [Scalability](https://redis.io/docs/latest/develop/data-types/vector-sets/scalability)

