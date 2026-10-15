# HOTKEYS

```json metadata
{
  "schema_version": 2,
  "title": "HOTKEYS",
  "description": "A container for hotkeys tracking commands.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "HOTKEYS",
  "complexity": "Depends on subcommand.",
  "group": "server",
  "acl_categories": ["@slow"],
  "since": "8.6.0",
  "arity": -2,
  "tableOfContents": {"sections":[{"id":"usage","title":"Usage"},{"id":"example","title":"Example"}]}

,
  "codeExamples": [{"codetabsId":"cmds_hotkeys-stephotkeys","commands":[{"acl_categories":["@slow"],"complexity":"Depends on subcommand","name":"HOTKEYS"},{"acl_categories":["@read","@string","@fast"],"complexity":"O(1)","name":"GET"},{"acl_categories":["@admin","@slow","@dangerous"],"complexity":"O(1)","name":"HOTKEYS RESET"}],"description":"Profiling: Find the keys that use the most CPU time and network bandwidth using HOTKEYS START, GET, STOP, and RESET (only one tracking session can run at a time)","difficulty":"intermediate","id":"hotkeys","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_cmds_hotkeys-stephotkeys"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_cmds_hotkeys-stephotkeys"},{"id":"Node-js","panelId":"panel_Nodejs_cmds_hotkeys-stephotkeys"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_cmds_hotkeys-stephotkeys"},{"clientId":"lettuce","clientName":"Lettuce","id":"Lettuce-Sync","langId":"java","panelId":"panel_Lettuce-Sync_cmds_hotkeys-stephotkeys"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_cmds_hotkeys-stephotkeys"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_cmds_hotkeys-stephotkeys"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_cmds_hotkeys-stephotkeys"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_cmds_hotkeys-stephotkeys"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_cmds_hotkeys-stephotkeys"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_cmds_hotkeys-stephotkeys"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_cmds_hotkeys-stephotkeys"}]}]
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


This is a container command for hotkeys tracking commands that provides a method for identifying hotkeys inside a Redis server during a specified tracking time period.

Hotkeys in this context are defined by two metrics:
* Percentage of CPU time spent on the key from the total time during the tracking period.
* Percentage of network bytes (input + output) used for the key from the total network bytes used by Redis during the tracking period.

## Usage

The general workflow is for the user to initiate a hotkeys tracking process which should run for some time. The keys' metrics are recorded inside a probabilistic data structure, after which the user is able to fetch the top K metrics.

Available subcommands:

- [`HOTKEYS START`](https://redis.io/docs/latest/commands/hotkeys-start) - Starts hotkeys tracking with specified metrics.
- [`HOTKEYS STOP`](https://redis.io/docs/latest/commands/hotkeys-stop) - Stops hotkeys tracking but preserves data.
- [`HOTKEYS GET`](https://redis.io/docs/latest/commands/hotkeys-get) - Returns tracking results and metadata.
- [`HOTKEYS RESET`](https://redis.io/docs/latest/commands/hotkeys-reset) - Releases resources used for tracking.

## Example

The following example tracks keys by CPU time and network bytes, reads the results while tracking is active, and then stops tracking and releases its resources.

The redis-py and go-redis cluster clients, and redis-rs async cluster connections, don't support `HOTKEYS`. With these clients, connect directly to a single node instead.

Profiling: Find the keys that use the most CPU time and network bandwidth using HOTKEYS START, GET, STOP, and RESET (only one tracking session can run at a time)

**Difficulty:** Intermediate

**Commands:** HOTKEYS, GET, HOTKEYS RESET

**Complexity:**
- HOTKEYS: Depends on subcommand
- GET: O(1)
- HOTKEYS RESET: O(1)

**Available in:** Redis CLI, C#, Go, Java, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> HOTKEYS START METRICS 2 CPU NET COUNT 10
OK
> GET product:1
"Laptop"
> GET product:1
"Laptop"
> GET product:2
"Phone"
> HOTKEYS GET
1)  1) "tracking-active"
    2) (integer) 1
    3) "sample-ratio"
    4) (integer) 1
    5) "selected-slots"
    6) 1) 1) (integer) 0
          2) (integer) 16383
    7) "all-commands-all-slots-us"
    8) (integer) 27
    9) "net-bytes-all-commands-all-slots"
   10) (integer) 119
   11) "collection-start-time-unix-ms"
   12) (integer) 1791553768375
   13) "collection-duration-ms"
   14) (integer) 44
   15) "total-cpu-time-user-ms"
   16) (integer) 2
   17) "total-cpu-time-sys-ms"
   18) (integer) 0
   19) "total-net-bytes"
   20) (integer) 119
   21) "by-cpu-time-us"
   22) 1) "product:1"
       2) (integer) 24
       3) "product:2"
       4) (integer) 3
   23) "by-net-bytes"
   24) 1) "product:1"
       2) (integer) 80
       3) "product:2"
       4) (integer) 39
> HOTKEYS STOP
OK
> HOTKEYS RESET
OK
```

##### C#

```csharp
        // Track the 10 hottest keys by CPU time and network bytes.
        server.HotKeysStart(metrics: HotKeysMetrics.Cpu | HotKeysMetrics.Network, count: 10);

        // Generate some traffic. In production, this is your application's workload.
        for (int i = 0; i < 100; i++)
        {
            db.StringGet("product:1");
        }

        for (int i = 0; i < 10; i++)
        {
            db.StringGet("product:2");
        }

        db.StringGet("product:3");

        HotKeysResult res2 = server.HotKeysGet();
        Console.WriteLine(res2.TrackingActive); // >>> True

        var byNet = res2.NetworkBytesByKey.ToArray();
        Console.WriteLine(string.Join(", ", byNet.Select(k => $"{k.Key}: {k.Bytes}")));
        // >>> product:1: 4000, product:2: 390, product:3: 40

        bool res3 = server.HotKeysStop();
        Console.WriteLine(res3); // >>> True

        server.HotKeysReset();
```

##### Go

```go
	// Track the 10 hottest keys by CPU time and network bytes.
	res1, err := rdb.HotKeysStart(ctx, &redis.HotKeysStartArgs{
		Metrics: []redis.HotKeysMetric{redis.HotKeysMetricCPU, redis.HotKeysMetricNET},
		Count:   10,
	}).Result()
	if err != nil {
		panic(err)
	}
	fmt.Println(res1) // >>> OK

	// Generate some traffic. In production, this is your application's workload.
	for i := 0; i < 100; i++ {
		rdb.Get(ctx, "product:1")
	}

	for i := 0; i < 10; i++ {
		rdb.Get(ctx, "product:2")
	}

	rdb.Get(ctx, "product:3")

	res2, err := rdb.HotKeysGet(ctx).Result()
	if err != nil {
		panic(err)
	}
	fmt.Println(res2.TrackingActive) // >>> true

	fmt.Println(res2.ByNetBytes)
	// >>> [{product:1 4000} {product:2 390} {product:3 40}]

	res3, err := rdb.HotKeysStop(ctx).Result()
	if err != nil {
		panic(err)
	}
	fmt.Println(res3) // >>> OK

	res4, err := rdb.HotKeysReset(ctx).Result()
	if err != nil {
		panic(err)
	}
	fmt.Println(res4) // >>> OK
```

##### Java

```java
            // Track the 10 hottest keys by CPU time and network bytes.
            String res1 = syncCommands.hotkeysStart(
                    HotkeysArgs.Builder.metrics(HotkeysArgs.Metric.CPU, HotkeysArgs.Metric.NET).count(10));
            System.out.println(res1); // >>> OK

            // Generate some traffic. In production, this is your application's workload.
            for (int i = 0; i < 100; i++) {
                syncCommands.get("product:1");
            }

            for (int i = 0; i < 10; i++) {
                syncCommands.get("product:2");
            }

            syncCommands.get("product:3");

            HotkeysReply res2 = syncCommands.hotkeysGet();
            System.out.println(res2.isTrackingActive()); // >>> true

            Map<String, Long> byNet = res2.getByNetBytes();
            System.out.println(byNet);
            // >>> {product:1=4000, product:2=390, product:3=40}


            String res3 = syncCommands.hotkeysStop();
            System.out.println(res3); // >>> OK

            String res4 = syncCommands.hotkeysReset();
            System.out.println(res4); // >>> OK
```

##### Java (Asynchronous - Lettuce)

```java
            // Track the 10 hottest keys by CPU time and network bytes.
            CompletableFuture<Void> hotkeysExample = asyncCommands.hotkeysStart(
                    HotkeysArgs.Builder.metrics(HotkeysArgs.Metric.CPU, HotkeysArgs.Metric.NET).count(10))
                    .thenCompose(res1 -> {
                        System.out.println(res1); // >>> OK

                        // Generate some traffic. In production, this is your application's workload.
                        List<CompletableFuture<String>> traffic = new ArrayList<>();
                        for (int i = 0; i < 100; i++) {
                            traffic.add(asyncCommands.get("product:1").toCompletableFuture());
                        }

                        for (int i = 0; i < 10; i++) {
                            traffic.add(asyncCommands.get("product:2").toCompletableFuture());
                        }

                        traffic.add(asyncCommands.get("product:3").toCompletableFuture());

                        return CompletableFuture.allOf(traffic.toArray(new CompletableFuture[0]));
                    })
                    .thenCompose(v -> asyncCommands.hotkeysGet())
                    .thenCompose(res2 -> {
                        System.out.println(res2.isTrackingActive()); // >>> true

                        System.out.println(res2.getByNetBytes());
                        // >>> {product:1=4000, product:2=390, product:3=40}


                        return asyncCommands.hotkeysStop();
                    })
                    .thenCompose(res3 -> {
                        System.out.println(res3); // >>> OK

                        return asyncCommands.hotkeysReset();
                    })
                    .thenAccept(res4 -> {
                        System.out.println(res4); // >>> OK
                    })
                    .toCompletableFuture();

            hotkeysExample.join();
```

##### Java (Reactive - Lettuce)

```java
            // Track the 10 hottest keys by CPU time and network bytes.
            Mono<Void> hotkeysExample = reactiveCommands.hotkeysStart(
                    HotkeysArgs.Builder.metrics(HotkeysArgs.Metric.CPU, HotkeysArgs.Metric.NET).count(10))
                    .doOnNext(res1 -> {
                        System.out.println(res1); // >>> OK
                    })
                    // Generate some traffic. In production, this is your application's workload.
                    .thenMany(Flux.range(0, 100).flatMap(i -> reactiveCommands.get("product:1")))
                    .thenMany(Flux.range(0, 10).flatMap(i -> reactiveCommands.get("product:2")))
                    .then(reactiveCommands.get("product:3"))
                    .then(reactiveCommands.hotkeysGet())
                    .doOnNext(res2 -> {
                        System.out.println(res2.isTrackingActive()); // >>> true

                        System.out.println(res2.getByNetBytes());
                        // >>> {product:1=4000, product:2=390, product:3=40}

                    })
                    .then(reactiveCommands.hotkeysStop())
                    .doOnNext(res3 -> {
                        System.out.println(res3); // >>> OK
                    })
                    .then(reactiveCommands.hotkeysReset())
                    .doOnNext(res4 -> {
                        System.out.println(res4); // >>> OK
                    })
                    .then();

            hotkeysExample.block();
```

##### Java (Synchronous - Jedis)

```java
        // Track the 10 hottest keys by CPU time and network bytes.
        String res1 = jedis.hotkeysStart(
            HotkeysParams.hotkeysParams()
                .metrics(HotkeysMetric.CPU, HotkeysMetric.NET)
                .count(10)
        );
        System.out.println(res1); // >>> OK

        // Generate some traffic. In production, this is your application's workload.
        for (int i = 0; i < 100; i++) {
            jedis.get("product:1");
        }

        for (int i = 0; i < 10; i++) {
            jedis.get("product:2");
        }

        jedis.get("product:3");

        HotkeysInfo res2 = jedis.hotkeysGet();
        System.out.println(res2.isTrackingActive()); // >>> true

        Map<String, Long> byNet = res2.getByNetBytes();
        System.out.println(byNet);
        // >>> {product:1=4000, product:2=390, product:3=40}

        String res3 = jedis.hotkeysStop();
        System.out.println(res3); // >>> OK

        String res4 = jedis.hotkeysReset();
        System.out.println(res4); // >>> OK
```

##### JavaScript (Node.js)

```javascript
// Track the 10 hottest keys by CPU time and network bytes.
const res1 = await client.hotkeysStart({
    METRICS: { count: 2, CPU: true, NET: true },
    COUNT: 10
});
console.log(res1); // >>> OK

// Generate some traffic. In production, this is your application's workload.
for (let i = 0; i < 100; i++) {
    await client.get('product:1');
}

for (let i = 0; i < 10; i++) {
    await client.get('product:2');
}

await client.get('product:3');

const res2 = await client.hotkeysGet();
console.log(res2.trackingActive); // >>> 1

const byNet = res2.byNetBytes.map(({ key, value }) => [key, value]);
console.log(byNet);
// >>> [ [ 'product:1', 4000 ], [ 'product:2', 390 ], [ 'product:3', 40 ] ]

const res3 = await client.hotkeysStop();
console.log(res3); // >>> OK

const res4 = await client.hotkeysReset();
console.log(res4); // >>> OK
```

##### PHP

```php
        // Track the 10 hottest keys by CPU time and network bytes.
        $res1 = $r->hotkeys->start([\Predis\Command\Container\HOTKEYS::CPU, \Predis\Command\Container\HOTKEYS::NET], 10);
        echo $res1 . PHP_EOL; // >>> OK

        // Generate some traffic. In production, this is your application's workload.
        for ($i = 0; $i < 100; $i++) {
            $r->get('product:1');
        }

        for ($i = 0; $i < 10; $i++) {
            $r->get('product:2');
        }

        $r->get('product:3');

        $res2 = $r->hotkeys->get()[0];
        echo $res2['tracking-active'] . PHP_EOL; // >>> 1

        $byNet = $res2['by-net-bytes'];
        echo json_encode(array_chunk($byNet, 2)) . PHP_EOL;
        // >>> [["product:1",4000],["product:2",390],["product:3",40]]

        $res3 = $r->hotkeys->stop();
        echo $res3 . PHP_EOL; // >>> OK

        $res4 = $r->hotkeys->reset();
        echo $res4 . PHP_EOL; // >>> OK
```

##### Python

```python
from redis.commands.core import HotkeysMetricsTypes

# Track the 10 hottest keys by CPU time and network bytes.
res1 = r.hotkeys_start(
    metrics=[HotkeysMetricsTypes.CPU, HotkeysMetricsTypes.NET], count=10
)
print(res1)  # >>> OK

# Generate some traffic. In production, this is your application's workload.
for _ in range(100):
    r.get("product:1")

for _ in range(10):
    r.get("product:2")

r.get("product:3")

res2 = r.hotkeys_get()[0]
print(res2["tracking-active"])  # >>> 1

by_net = res2["by-net-bytes"]
print(list(zip(by_net[::2], by_net[1::2])))
# >>> [('product:1', 4000), ('product:2', 390), ('product:3', 40)]

res3 = r.hotkeys_stop()
print(res3)  # >>> OK

res4 = r.hotkeys_reset()
print(res4)  # >>> OK
```

##### Rust (Asynchronous)

```rust
        // Track the 10 hottest keys by CPU time and network bytes.
        let opts = HotkeysOptions::new_with_cpu()
            .and_net()
            .with_count(10)
            .expect("COUNT must be between 1 and 64");

        match r.hotkeys_start(opts).await {
            Ok(res1) => {
                println!("{res1:?}"); // >>> ()
            }
            Err(e) => println!("Error starting hotkeys tracking: {e}"),
        }

        // Generate some traffic. In production, this is your application's workload.
        for _ in 0..100 {
            let _: Result<String, _> = r.get("product:1").await;
        }

        for _ in 0..10 {
            let _: Result<String, _> = r.get("product:2").await;
        }

        let _: Result<String, _> = r.get("product:3").await;

        match r.hotkeys_get().await {
            Ok(Some(res2)) => {
                println!("{}", res2.tracking_active); // >>> true

                let by_net: Vec<(&str, u64)> = res2
                    .by_net_bytes
                    .iter()
                    .flatten()
                    .map(|entry| (entry.key.as_str(), entry.value))
                    .collect();
                println!("{by_net:?}");
                // >>> [("product:1", 4000), ("product:2", 390), ("product:3", 40)]
            }
            Ok(None) => {
                println!("No hotkeys tracking session");
            }
            Err(e) => println!("Error getting hotkeys: {e}"),
        }

        match r.hotkeys_stop().await {
            Ok(res3) => {
                println!("{res3}"); // >>> true
            }
            Err(e) => println!("Error stopping hotkeys tracking: {e}"),
        }

        match r.hotkeys_reset().await {
            Ok(res4) => {
                println!("{res4:?}"); // >>> ()
            }
            Err(e) => println!("Error resetting hotkeys: {e}"),
        }
```

##### Rust (Synchronous)

```rust
        // Track the 10 hottest keys by CPU time and network bytes.
        let opts = HotkeysOptions::new_with_cpu()
            .and_net()
            .with_count(10)
            .expect("COUNT must be between 1 and 64");

        match r.hotkeys_start(opts) {
            Ok(res1) => {
                println!("{res1:?}"); // >>> ()
            }
            Err(e) => println!("Error starting hotkeys tracking: {e}"),
        }

        // Generate some traffic. In production, this is your application's workload.
        for _ in 0..100 {
            let _: Result<String, _> = r.get("product:1");
        }

        for _ in 0..10 {
            let _: Result<String, _> = r.get("product:2");
        }

        let _: Result<String, _> = r.get("product:3");

        match r.hotkeys_get() {
            Ok(Some(res2)) => {
                println!("{}", res2.tracking_active); // >>> true

                let by_net: Vec<(&str, u64)> = res2
                    .by_net_bytes
                    .iter()
                    .flatten()
                    .map(|entry| (entry.key.as_str(), entry.value))
                    .collect();
                println!("{by_net:?}");
                // >>> [("product:1", 4000), ("product:2", 390), ("product:3", 40)]
            }
            Ok(None) => {
                println!("No hotkeys tracking session");
            }
            Err(e) => println!("Error getting hotkeys: {e}"),
        }

        match r.hotkeys_stop() {
            Ok(res3) => {
                println!("{res3}"); // >>> true
            }
            Err(e) => println!("Error stopping hotkeys tracking: {e}"),
        }

        match r.hotkeys_reset() {
            Ok(res4) => {
                println!("{res4:?}"); // >>> ()
            }
            Err(e) => println!("Error resetting hotkeys: {e}"),
        }
```



