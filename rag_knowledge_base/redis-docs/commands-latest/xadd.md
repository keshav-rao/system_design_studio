# XADD

```json metadata
{
  "schema_version": 2,
  "title": "XADD",
  "description": "Appends a new message to a stream. Creates the key if it doesn't exist.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"key_spec_index":0,"name":"key","type":"key"},{"name":"nomkstream","optional":true,"since":"6.2.0","token":"NOMKSTREAM","type":"pure-token"},{"arguments":[{"name":"keepref","token":"KEEPREF","type":"pure-token"},{"name":"delref","token":"DELREF","type":"pure-token"},{"name":"acked","token":"ACKED","type":"pure-token"}],"name":"condition","optional":true,"type":"oneof"},{"arguments":[{"display_text":"producer-id","name":"pid","token":"IDMPAUTO","type":"string"},{"arguments":[{"display_text":"producer-id","name":"pid","type":"string"},{"display_text":"idempotent-id","name":"iid","type":"string"}],"name":"idmp","token":"IDMP","type":"block"}],"name":"idmp","optional":true,"since":"8.6.0","type":"oneof"},{"arguments":[{"arguments":[{"name":"maxlen","token":"MAXLEN","type":"pure-token"},{"name":"minid","since":"6.2.0","token":"MINID","type":"pure-token"}],"name":"strategy","type":"oneof"},{"arguments":[{"name":"equal","token":"=","type":"pure-token"},{"name":"approximately","token":"~","type":"pure-token"}],"name":"operator","optional":true,"type":"oneof"},{"name":"threshold","type":"string"},{"name":"count","optional":true,"since":"6.2.0","token":"LIMIT","type":"integer"}],"name":"trim","optional":true,"type":"block"},{"arguments":[{"name":"auto-id","token":"*","type":"pure-token"},{"name":"id","type":"string"}],"name":"id-selector","type":"oneof"},{"arguments":[{"name":"field","type":"string"},{"name":"value","type":"string"}],"multiple":true,"name":"data","type":"block"}],
  "syntax_fmt": "XADD key [NOMKSTREAM] [KEEPREF | DELREF | ACKED]\n  [IDMPAUTO producer-id | IDMP producer-id idempotent-id]\n  [\u003cMAXLEN | MINID\u003e [= | ~] threshold [LIMIT count]] \u003c* | id\u003e\n  field value [field value ...]",
  "complexity": "O(1) when adding a new entry, O(N) when trimming where N being the number of entries evicted.",
  "group": "stream",
  "command_flags": ["write","denyoom","fast"],
  "acl_categories": ["@write","@stream","@fast"],
  "since": "5.0.0",
  "arity": -5,
  "key_specs": [{"begin_search":{"index":{"pos":1}},"find_keys":{"range":{"lastkey":0,"limit":0},"type":"range"},"notes":"UPDATE instead of INSERT because of the optional trimming feature"}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"children":[{"id":"idempotent-message-processing-examples","title":"Idempotent message processing examples"}],"id":"examples","title":"Examples"},{"children":[{"id":"specifying-a-stream-id-as-an-argument","title":"Specifying a Stream ID as an argument"},{"id":"capped-streams","title":"Capped streams"},{"id":"additional-information-about-streams","title":"Additional information about streams"}],"id":"details","title":"Details"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": [{"codetabsId":"cmds_stream-stepxadd1","commands":[{"acl_categories":["@write","@stream","@fast"],"complexity":"O(1)","name":"XADD"},{"acl_categories":["@read","@stream","@fast"],"complexity":"O(1)","name":"XLEN"},{"acl_categories":["@read","@stream","@slow"],"complexity":"O(N)","name":"XRANGE"}],"description":"Basic XADD: Add entries to a stream with auto-generated IDs, check stream the stream size, and read entries","difficulty":"beginner","id":"xadd1","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_cmds_stream-stepxadd1"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_cmds_stream-stepxadd1"},{"id":"Node-js","panelId":"panel_Nodejs_cmds_stream-stepxadd1"},{"clientId":"ioredis","clientName":"ioredis","id":"ioredis","langId":"javascript","panelId":"panel_ioredis_cmds_stream-stepxadd1"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_cmds_stream-stepxadd1"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_cmds_stream-stepxadd1"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_cmds_stream-stepxadd1"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_cmds_stream-stepxadd1"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_cmds_stream-stepxadd1"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_cmds_stream-stepxadd1"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_cmds_stream-stepxadd1"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_cmds_stream-stepxadd1"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_cmds_stream-stepxadd1"}]},{"codetabsId":"cmds_stream-stepxadd2","commands":[{"acl_categories":["@write","@stream","@fast"],"complexity":"O(1)","name":"XADD"},{"acl_categories":["@write","@stream","@fast"],"complexity":"O(1)","name":"XCFGSET"}],"description":"Idempotent XADD (Redis 8.6\u0026#43;): Use IDMP and IDMPAUTO for at-most-once message delivery, preventing duplicate entries","difficulty":"intermediate","id":"xadd2","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_cmds_stream-stepxadd2"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_cmds_stream-stepxadd2"},{"id":"Node-js","panelId":"panel_Nodejs_cmds_stream-stepxadd2"},{"clientId":"ioredis","clientName":"ioredis","id":"ioredis","langId":"javascript","panelId":"panel_ioredis_cmds_stream-stepxadd2"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_cmds_stream-stepxadd2"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_cmds_stream-stepxadd2"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_cmds_stream-stepxadd2"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_cmds_stream-stepxadd2"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_cmds_stream-stepxadd2"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_cmds_stream-stepxadd2"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_cmds_stream-stepxadd2"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_cmds_stream-stepxadd2"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_cmds_stream-stepxadd2"}]}]
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

Appends the specified stream entry to the stream at the specified `key`.
If the key does not exist, `XADD` will create a new key with the given stream value as a side effect of running this command.
You can turn off key creation with the `NOMKSTREAM` option.

## Required arguments

<details open>
<summary><code>key</code></summary>

The name of the stream key.
</details>

<details open>
<summary><code>id</code></summary>

The stream entry ID. Use `*` to auto-generate a unique ID, or specify a well-formed ID in the format `<ms>-<seq>` (for example, `1526919030474-55`).
</details>

<details open>
<summary><code>field value [field value ...]</code></summary>

One or more field-value pairs that make up the stream entry. You must provide at least one field-value pair.
</details>

## Optional arguments

<details open>
<summary><code>NOMKSTREAM</code></summary>

Prevents the creation of a new stream if the key does not exist. Available since Redis 6.2.0.
</details>

<details open>
<summary><code>IDMPAUTO producer-id | IDMP producer-id idempotent-id</code></summary>

Enables idempotent message processing (at-most-once production) to prevent duplicate entries. Available since Redis 8.6.

- `IDMPAUTO producer-id`: Automatically generates a unique idempotent ID (iid) for the specified producer-id. Redis tracks this iid to prevent duplicate messages from the same producer-id.
- `IDMP producer-id idempotent-id`: Uses the specified idempotent-id for the given producer-id. If this producer-id/idempotent-id combination was already used, the command returns the ID of the original entry instead of creating a duplicate.

The producer-id identifies the source of the message, while the idempotent-id ensures uniqueness within that producer-id's message stream. Redis maintains an internal map of recent producer-id/idempotent-id combinations to detect and prevent duplicates.

Both modes can only be specified when the entry ID is `*` (auto-generated).

Use [`XCFGSET`](https://redis.io/docs/latest/commands/xcfgset) to configure how long idempotent IDs are retained (`IDMP-DURATION`) and the maximum number tracked per producer (`IDMP-MAXSIZE`).

See [Idempotent message processing](https://redis.io/docs/latest/develop/data-types/streams/idempotency) for more information.

</details>

<details open>
<summary><code>KEEPREF | DELREF | ACKED</code></summary>

Specifies how to handle consumer group references when trimming. If there are no consumer groups, these arguments have no effect. Available since Redis 8.2.

If no option is specified, `KEEPREF` is used by default. Unlike the `XDELEX` and `XACKDEL` commands where one of these options is required, here they are optional to maintain backward compatibility:

- `KEEPREF` (default): When trimming, removes entries from the stream according to the specified strategy (`MAXLEN` or `MINID`), regardless of whether they are referenced by any consumer groups, but preserves existing references to these entries in all consumer groups' PEL (Pending Entries List).
- `DELREF`: When trimming, removes entries from the stream according to the specified strategy and also removes all references to these entries from all consumer groups' PEL.
- `ACKED`: When trimming, only removes entries that were read and acknowledged by all consumer groups. Note that if the number of referenced entries is larger than `MAXLEN`, trimming will still stop at the limit.
</details>

<details open>
<summary><code>MAXLEN | MINID [= | ~] threshold [LIMIT count]></code></summary>

Trims the stream to maintain a specific size or remove old entries:

<details open>
<summary><code>MAXLEN | MINID</code></summary>

The trimming strategy:
- `MAXLEN`: Evicts entries as long as the stream's length exceeds the specified threshold
- `MINID`: Evicts entries with IDs lower than the specified threshold (available since Redis 6.2.0)
</details>

<details open>
<summary><code>= | ~</code></summary>

The trimming operator:
- `=`: Exact trimming (default) - trims to the exact threshold
- `~`: Approximate trimming - more efficient, may leave slightly more entries than the threshold
</details>

<details open>
<summary><code>threshold</code></summary>

The trimming threshold:
- For `MAXLEN`: `threshold` is a non-negative integer specifying the maximum number of entries that may remain in the stream after trimming. Redis enforces this by removing the oldest entries - that is, the entries with the lowest stream IDs - so that only the newest entries are kept.
- For `MINID`: `threshold` is a stream ID. All entries whose IDs are less than `threshold` are trimmed. All entries with IDs greater than or equal to `threshold` are kept.
</details>

<details open>
<summary><code>LIMIT count</code></summary>

Limits the number of entries to examine during trimming. Available since Redis 6.2.0. When not specified, Redis uses a default value of 100 * the number of entries in a macro node. Specifying 0 disables the limiting mechanism entirely.
</details>

</details>
  
Each entry consists of a list of field-value pairs.
Redis stores the field-value pairs in the same order you provide them.
Commands that read the stream, such as [`XRANGE`](https://redis.io/docs/latest/commands/xrange) or [`XREAD`](https://redis.io/docs/latest/commands/xread), return the fields and values in exactly the same order you added them with `XADD`.

> [!NOTE]
> `XADD` is the only Redis command that can add data to a stream. However,
> other commands, such as [`XDEL`](https://redis.io/docs/latest/commands/xdel) and [`XTRIM`](https://redis.io/docs/latest/commands/xtrim), can
> remove data from a stream.

## Examples

Basic XADD: Add entries to a stream with auto-generated IDs, check stream the stream size, and read entries

**Difficulty:** Beginner

**Commands:** XADD, XLEN, XRANGE

**Complexity:**
- XADD: O(1)
- XLEN: O(1)
- XRANGE: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> XADD mystream * name Sara surname OConnor
"4378417975-0"
> XADD mystream * field1 value1 field2 value2 field3 value3
"4378417976-0"
> XLEN mystream
(integer) 2
> XRANGE mystream - +
1) 1) "1774378417975-0"
   2) 1) "name"
      2) "Sara"
      3) "surname"
      4) "OConnor"
2) 1) "1774378417976-0"
   2) 1) "field1"
      2) "value1"
      3) "field2"
      4) "value2"
      5) "field3"
      6) "value3"
```

##### C#

```csharp
        var res1 = db.StreamAdd("mystream", new NameValueEntry[] {
            new NameValueEntry("name", "Sara"),
            new NameValueEntry("surname", "OConnor")
        });
        Console.WriteLine(res1);  // >>> 1726055713866-0

        var res2 = db.StreamAdd("mystream", new NameValueEntry[] {
            new NameValueEntry("field1", "value1"),
            new NameValueEntry("field2", "value2"),
            new NameValueEntry("field3", "value3")
        });
        Console.WriteLine(res2);  // >>> 1726055713866-1

        var res3 = db.StreamLength("mystream");
        Console.WriteLine(res3);  // >>> 2

        var res4 = db.StreamRange("mystream", "-", "+");
        foreach (var entry in res4)
        {
            Console.WriteLine($"{entry.Id} -> {string.Join(", ", entry.Values.Select(v => $"{v.Name}={v.Value}"))}");
        }
        // >>> 1726055713866-0 -> name=Sara, surname=OConnor
        // >>> 1726055713866-1 -> field1=value1, field2=value2, field3=value3
```

##### Go

```go
	res1, err := rdb.XAdd(ctx, &redis.XAddArgs{
		Stream: "mystream",
		Values: map[string]interface{}{
			"name":    "Sara",
			"surname": "OConnor",
		},
	}).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1 != "") // >>> true

	res2, err := rdb.XAdd(ctx, &redis.XAddArgs{
		Stream: "mystream",
		Values: map[string]interface{}{
			"field1": "value1",
			"field2": "value2",
			"field3": "value3",
		},
	}).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2 != "") // >>> true

	res3, err := rdb.XLen(ctx, "mystream").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3) // >>> 2

	res4, err := rdb.XRange(ctx, "mystream", "-", "+").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(len(res4)) // >>> 2
```

##### Java (Asynchronous - Lettuce)

```java
            Map<String, String> entry1 = new HashMap<>();
            entry1.put("name", "Sara");
            entry1.put("surname", "OConnor");

            CompletableFuture<Void> xadd1Ops = asyncCommands.xadd("mystream", entry1)
                .thenCompose(res1 -> {
                    System.out.println(res1); // >>> 1726055713866-0
                    Map<String, String> entry2 = new HashMap<>();
                    entry2.put("field1", "value1");
                    entry2.put("field2", "value2");
                    entry2.put("field3", "value3");
                    return asyncCommands.xadd("mystream", entry2);
                })
                .thenCompose(res2 -> {
                    System.out.println(res2); // >>> 1726055713866-1
                    return asyncCommands.xlen("mystream");
                })
                .thenCompose(res3 -> {
                    System.out.println(res3); // >>> 2
                    return asyncCommands.xrange("mystream", Range.unbounded());
                })
                .thenAccept(res4 -> {
                    for (var entry : res4) {
                        System.out.println(entry.getId() + " -> " + entry.getBody());
                    }
                    // >>> 1726055713866-0 -> {name=Sara, surname=OConnor}
                    // >>> 1726055713866-1 -> {field1=value1, field2=value2, field3=value3}
                })
                .toCompletableFuture();

            xadd1Ops.join();
```

##### Java (Reactive - Lettuce)

```java
            Map<String, String> entry1 = new HashMap<>();
            entry1.put("name", "Sara");
            entry1.put("surname", "OConnor");

            Mono<String> addEntry1 = reactiveCommands.xadd("mystream", entry1)
                .doOnNext(res1 -> {
                    System.out.println(res1); // >>> 1726055713866-0
                });

            addEntry1.block();

            Map<String, String> entry2 = new HashMap<>();
            entry2.put("field1", "value1");
            entry2.put("field2", "value2");
            entry2.put("field3", "value3");

            Mono<String> addEntry2 = reactiveCommands.xadd("mystream", entry2)
                .doOnNext(res2 -> {
                    System.out.println(res2); // >>> 1726055713866-1
                });

            addEntry2.block();

            Mono<Long> getLen = reactiveCommands.xlen("mystream")
                .doOnNext(res3 -> {
                    System.out.println(res3); // >>> 2
                });

            getLen.block();

            Mono<List<StreamMessage<String, String>>> getRange = reactiveCommands
                .xrange("mystream", Range.unbounded())
                .collectList()
                .doOnNext(res4 -> {
                    for (var entry : res4) {
                        System.out.println(entry.getId() + " -> " + entry.getBody());
                    }
                    // >>> 1726055713866-0 -> {name=Sara, surname=OConnor}
                    // >>> 1726055713866-1 -> {field1=value1, field2=value2, field3=value3}
                });

            getRange.block();
```

##### Java (Synchronous - Jedis)

```java
        Map<String, String> entry1 = new HashMap<>();
        entry1.put("name", "Sara");
        entry1.put("surname", "OConnor");
        StreamEntryID res1 = jedis.xadd("mystream", entry1, XAddParams.xAddParams());
        System.out.println(res1); // >>> 1726055713866-0

        Map<String, String> entry2 = new HashMap<>();
        entry2.put("field1", "value1");
        entry2.put("field2", "value2");
        entry2.put("field3", "value3");
        StreamEntryID res2 = jedis.xadd("mystream", entry2, XAddParams.xAddParams());
        System.out.println(res2); // >>> 1726055713866-1

        long res3 = jedis.xlen("mystream");
        System.out.println(res3); // >>> 2

        List<StreamEntry> res4 = jedis.xrange("mystream", "-", "+");
        for (StreamEntry entry : res4) {
            System.out.println(entry.getID() + " -> " + entry.getFields());
        }
        // >>> 1726055713866-0 -> {name=Sara, surname=OConnor}
        // >>> 1726055713866-1 -> {field1=value1, field2=value2, field3=value3}
```

##### JavaScript (Node.js)

```javascript
const res1 = await client.xAdd('mystream', '*', {
  'name': 'Sara',
  'surname': 'OConnor'
});
console.log(res1); // >>> 1726055713866-0

const res2 = await client.xAdd('mystream', '*', {
  'field1': 'value1',
  'field2': 'value2',
  'field3': 'value3'
});
console.log(res2); // >>> 1726055713866-1

const res3 = await client.xLen('mystream');
console.log(res3); // >>> 2

const res4 = await client.xRange('mystream', '-', '+');
console.log(res4);
// >>> [
//   { id: '1726055713866-0', message: { name: 'Sara', surname: 'OConnor' } },
//   { id: '1726055713866-1', message: { field1: 'value1', field2: 'value2', field3: 'value3' } }
// ]
```

##### JavaScript (Node.js)

```javascript
const res1 = await redis.xadd('mystream', '*', 'name', 'Sara', 'surname', 'OConnor');
console.log(res1); // >>> 1726055713866-0

const res2 = await redis.xadd('mystream', '*', 'field1', 'value1', 'field2', 'value2', 'field3', 'value3');
console.log(res2); // >>> 1726055713866-1

const res3 = await redis.xlen('mystream');
console.log(res3); // >>> 2

const res4 = await redis.xrange('mystream', '-', '+');
console.log(res4);
// >>> [
//   ['1726055713866-0', ['name', 'Sara', 'surname', 'OConnor']],
//   ['1726055713866-1', ['field1', 'value1', 'field2', 'value2', 'field3', 'value3']]
// ]
```

##### JavaScript (Node.js)

```javascript
const res1 = await client.xAdd('mystream', '*', {
  'name': 'Sara',
  'surname': 'OConnor'
});
console.log(res1); // >>> 1726055713866-0

const res2 = await client.xAdd('mystream', '*', {
  'field1': 'value1',
  'field2': 'value2',
  'field3': 'value3'
});
console.log(res2); // >>> 1726055713866-1

const res3 = await client.xLen('mystream');
console.log(res3); // >>> 2

const res4 = await client.xRange('mystream', '-', '+');
console.log(res4);
// >>> [
//   { id: '1726055713866-0', message: { name: 'Sara', surname: 'OConnor' } },
//   { id: '1726055713866-1', message: { field1: 'value1', field2: 'value2', field3: 'value3' } }
// ]
```

##### JavaScript (Node.js)

```javascript
const res1 = await redis.xadd('mystream', '*', 'name', 'Sara', 'surname', 'OConnor');
console.log(res1); // >>> 1726055713866-0

const res2 = await redis.xadd('mystream', '*', 'field1', 'value1', 'field2', 'value2', 'field3', 'value3');
console.log(res2); // >>> 1726055713866-1

const res3 = await redis.xlen('mystream');
console.log(res3); // >>> 2

const res4 = await redis.xrange('mystream', '-', '+');
console.log(res4);
// >>> [
//   ['1726055713866-0', ['name', 'Sara', 'surname', 'OConnor']],
//   ['1726055713866-1', ['field1', 'value1', 'field2', 'value2', 'field3', 'value3']]
// ]
```

##### PHP

```php
        $res1 = $redis->xadd('mystream', ['name' => 'Sara', 'surname' => 'OConnor']);
        echo $res1 . PHP_EOL; // >>> 1726055713866-0

        $res2 = $redis->xadd('mystream', ['field1' => 'value1', 'field2' => 'value2', 'field3' => 'value3']);
        echo $res2 . PHP_EOL; // >>> 1726055713866-1

        $res3 = $redis->xlen('mystream');
        echo $res3 . PHP_EOL; // >>> 2

        $res4 = $redis->xrange('mystream', '-', '+');
        foreach ($res4 as $id => $fields) {
            echo $id . ' -> ' . json_encode($fields) . PHP_EOL;
        }
        // >>> 1726055713866-0 -> {"name":"Sara","surname":"OConnor"}
        // >>> 1726055713866-1 -> {"field1":"value1","field2":"value2","field3":"value3"}
```

##### Python

```python
res1 = r.xadd("mystream", {"name": "Sara", "surname": "OConnor"})
print(res1)  # >>> 1726055713866-0

res2 = r.xadd("mystream", {"field1": "value1", "field2": "value2", "field3": "value3"})
print(res2)  # >>> 1726055713866-1

res3 = r.xlen("mystream")
print(res3)  # >>> 2

res4 = r.xrange("mystream", "-", "+")
print(res4)
# >>> [
#   ('1726055713866-0', {'name': 'Sara', 'surname': 'OConnor'}),
#   ('1726055713866-1', {'field1': 'value1', 'field2': 'value2', 'field3': 'value3'})
# ]
```

##### Ruby

```ruby
res1 = r.xadd('mystream', { 'name' => 'Sara', 'surname' => 'OConnor' })
puts res1 # >>> 1726055713866-0

res2 = r.xadd('mystream', { 'field1' => 'value1', 'field2' => 'value2', 'field3' => 'value3' })
puts res2 # >>> 1726055713866-1

res3 = r.xlen('mystream')
puts res3 # >>> 2

res4 = r.xrange('mystream', '-', '+')
puts res4.inspect
# >>> [
#   ["1726055713866-0", {"name"=>"Sara", "surname"=>"OConnor"}],
#   ["1726055713866-1", {"field1"=>"value1", "field2"=>"value2", "field3"=>"value3"}]
# ]
```

##### Rust (Asynchronous)

```rust
        let client = redis::Client::open("redis://127.0.0.1/").unwrap();
        let mut con = client.get_multiplexed_async_connection().await.unwrap();


        let res1: String = redis::cmd("XADD")
            .arg("mystream")
            .arg("*")
            .arg("name")
            .arg("Sara")
            .arg("surname")
            .arg("OConnor")
            .query_async(&mut con)
            .await
            .unwrap();
        println!("XADD result: {}", res1); // >>> 1726055713866-0

        let res2: String = redis::cmd("XADD")
            .arg("mystream")
            .arg("*")
            .arg("field1")
            .arg("value1")
            .arg("field2")
            .arg("value2")
            .arg("field3")
            .arg("value3")
            .query_async(&mut con)
            .await
            .unwrap();
        println!("XADD result: {}", res2); // >>> 1726055713866-1

        let res3: i64 = con.xlen("mystream").await.unwrap();
        println!("XLEN result: {}", res3); // >>> 2

        let res4: redis::streams::StreamRangeReply = con.xrange_all("mystream").await.unwrap();
        for entry in &res4.ids {
            println!("{} -> {:?}", entry.id, entry.map);
        }
        // >>> 1726055713866-0 -> {"name": "Sara", "surname": "OConnor"}
        // >>> 1726055713866-1 -> {"field1": "value1", "field2": "value2", "field3": "value3"}
```

##### Rust (Synchronous)

```rust
        let client = redis::Client::open("redis://127.0.0.1/").unwrap();
        let mut con = client.get_connection().unwrap();


        let res1: String = redis::cmd("XADD")
            .arg("mystream")
            .arg("*")
            .arg("name")
            .arg("Sara")
            .arg("surname")
            .arg("OConnor")
            .query(&mut con)
            .unwrap();
        println!("XADD result: {}", res1); // >>> 1726055713866-0

        let res2: String = redis::cmd("XADD")
            .arg("mystream")
            .arg("*")
            .arg("field1")
            .arg("value1")
            .arg("field2")
            .arg("value2")
            .arg("field3")
            .arg("value3")
            .query(&mut con)
            .unwrap();
        println!("XADD result: {}", res2); // >>> 1726055713866-1

        let res3: i64 = con.xlen("mystream").unwrap();
        println!("XLEN result: {}", res3); // >>> 2

        let res4: redis::streams::StreamRangeReply = con.xrange_all("mystream").unwrap();
        for entry in &res4.ids {
            println!("{} -> {:?}", entry.id, entry.map);
        }
        // >>> 1726055713866-0 -> {"name": "Sara", "surname": "OConnor"}
        // >>> 1726055713866-1 -> {"field1": "value1", "field2": "value2", "field3": "value3"}
```



### Idempotent message processing examples

Idempotent XADD (Redis 8.6+): Use IDMP and IDMPAUTO for at-most-once message delivery, preventing duplicate entries

**Difficulty:** Intermediate

**Commands:** XADD, XCFGSET

**Complexity:**
- XADD: O(1)
- XCFGSET: O(1)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> XADD mystream IDMP producer1 msg1 * field value
"1774378417976-0"
> XADD mystream IDMP producer1 msg1 * field different_value
"1774378417976-0"
> XADD mystream IDMPAUTO producer2 * field value
"1774378417977-0"
> XADD mystream IDMPAUTO producer2 * field value
"1774378417977-0"
> XCFGSET mystream IDMP-DURATION 300 IDMP-MAXSIZE 1000
OK
```

##### C#

```csharp
        // Note: IDMP is a Redis 8.6 feature - using Execute for raw command access
        var res5 = db.Execute("XADD", "mystream", "IDMP", "producer1", "msg1", "*", "field", "value");
        Console.WriteLine(res5);  // >>> 1726055713867-0

        // Attempting to add the same message again with IDMP returns the original entry ID
        var res6 = db.Execute("XADD", "mystream", "IDMP", "producer1", "msg1", "*", "field", "different_value");
        Console.WriteLine(res6);  // >>> 1726055713867-0 (same ID as res5, message was deduplicated)

        var res7 = db.Execute("XADD", "mystream", "IDMPAUTO", "producer2", "*", "field", "value");
        Console.WriteLine(res7);  // >>> 1726055713867-1

        // Auto-generated idempotent ID prevents duplicates for same producer+content
        var res8 = db.Execute("XADD", "mystream", "IDMPAUTO", "producer2", "*", "field", "value");
        Console.WriteLine(res8);  // >>> 1726055713867-1 (same ID as res7, duplicate detected)

        // Configure idempotent message processing settings
        var res9 = db.Execute("XCFGSET", "mystream", "IDMP-DURATION", "300", "IDMP-MAXSIZE", "1000");
        Console.WriteLine(res9);  // >>> OK
```

##### Go

```go
	res5, err := rdb.XAdd(ctx, &redis.XAddArgs{
		Stream:       "mystream",
		Values:       map[string]interface{}{"field": "value"},
		ProducerID:   "producer1",
		IdempotentID: "msg1",
	}).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res5 != "") // >>> true

	// Attempting to add the same message again with IDMP returns the original entry ID
	res6, err := rdb.XAdd(ctx, &redis.XAddArgs{
		Stream:       "mystream",
		Values:       map[string]interface{}{"field": "different_value"},
		ProducerID:   "producer1",
		IdempotentID: "msg1",
	}).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res5 == res6) // >>> true (same ID, message was deduplicated)

	res7, err := rdb.XAdd(ctx, &redis.XAddArgs{
		Stream:         "mystream",
		Values:         map[string]interface{}{"field": "value"},
		ProducerID:     "producer2",
		IdempotentAuto: true,
	}).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res7 != "") // >>> true

	// Auto-generated idempotent ID prevents duplicates for same producer+content
	res8, err := rdb.XAdd(ctx, &redis.XAddArgs{
		Stream:         "mystream",
		Values:         map[string]interface{}{"field": "value"},
		ProducerID:     "producer2",
		IdempotentAuto: true,
	}).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res7 == res8) // >>> true (same ID, duplicate detected)

	// Configure idempotent message processing settings
	res9, err := rdb.XCfgSet(ctx, &redis.XCfgSetArgs{
		Stream:   "mystream",
		Duration: 300,  // 300 seconds
		MaxSize:  1000, // 1000 idempotent IDs
	}).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res9) // >>> OK
```

##### Java (Asynchronous - Lettuce)

```java
            Map<String, String> idmpEntry1 = new HashMap<>();
            idmpEntry1.put("field", "value");

            CompletableFuture<Void> xadd2Ops = asyncCommands.xadd(
                    "mystream",
                    XAddArgs.Builder.idmp("producer1", "msg1"),
                    idmpEntry1)
                .thenCompose(res5 -> {
                    System.out.println(res5); // >>> 1726055713867-0
                    // Attempting to add same message again with IDMP returns original entry ID
                    Map<String, String> idmpEntry2 = new HashMap<>();
                    idmpEntry2.put("field", "different_value");
                    return asyncCommands.xadd("mystream",
                        XAddArgs.Builder.idmp("producer1", "msg1"), idmpEntry2);
                })
                .thenCompose(res6 -> {
                    System.out.println(res6); // >>> 1726055713867-0 (deduplicated)
                    Map<String, String> idmpAutoEntry1 = new HashMap<>();
                    idmpAutoEntry1.put("field", "value");
                    return asyncCommands.xadd("mystream",
                        XAddArgs.Builder.idmpAuto("producer2"), idmpAutoEntry1);
                })
                .thenCompose(res7 -> {
                    System.out.println(res7); // >>> 1726055713867-1
                    Map<String, String> idmpAutoEntry2 = new HashMap<>();
                    idmpAutoEntry2.put("field", "value");
                    return asyncCommands.xadd("mystream",
                        XAddArgs.Builder.idmpAuto("producer2"), idmpAutoEntry2);
                })
                .thenAccept(res8 -> {
                    System.out.println(res8); // >>> 1726055713867-1 (duplicate detected)
                })
                .toCompletableFuture();

            xadd2Ops.join();
```

##### Java (Reactive - Lettuce)

```java
            Map<String, String> idmpEntry1 = new HashMap<>();
            idmpEntry1.put("field", "value");

            Mono<String> addIdmp1 = reactiveCommands.xadd(
                    "mystream",
                    XAddArgs.Builder.idmp("producer1", "msg1"),
                    idmpEntry1)
                .doOnNext(res5 -> {
                    System.out.println(res5); // >>> 1726055713867-0
                });

            addIdmp1.block();

            // Attempting to add the same message again with IDMP returns the original entry ID
            Map<String, String> idmpEntry2 = new HashMap<>();
            idmpEntry2.put("field", "different_value");

            Mono<String> addIdmp2 = reactiveCommands.xadd(
                    "mystream",
                    XAddArgs.Builder.idmp("producer1", "msg1"),
                    idmpEntry2)
                .doOnNext(res6 -> {
                    System.out.println(res6); // >>> 1726055713867-0 (deduplicated)
                });

            addIdmp2.block();

            Map<String, String> idmpAutoEntry1 = new HashMap<>();
            idmpAutoEntry1.put("field", "value");

            Mono<String> addIdmpAuto1 = reactiveCommands.xadd(
                    "mystream",
                    XAddArgs.Builder.idmpAuto("producer2"),
                    idmpAutoEntry1)
                .doOnNext(res7 -> {
                    System.out.println(res7); // >>> 1726055713867-1
                });

            addIdmpAuto1.block();

            // Auto-generated idempotent ID prevents duplicates for same producer+content
            Map<String, String> idmpAutoEntry2 = new HashMap<>();
            idmpAutoEntry2.put("field", "value");

            Mono<String> addIdmpAuto2 = reactiveCommands.xadd(
                    "mystream",
                    XAddArgs.Builder.idmpAuto("producer2"),
                    idmpAutoEntry2)
                .doOnNext(res8 -> {
                    System.out.println(res8); // >>> 1726055713867-1 (duplicate detected)
                });

            addIdmpAuto2.block();
```

##### Java (Synchronous - Jedis)

```java
        Map<String, String> idmpEntry1 = new HashMap<>();
        idmpEntry1.put("field", "value");
        StreamEntryID res5 = jedis.xadd("mystream", idmpEntry1, 
            XAddParams.xAddParams().idmp("producer1", "msg1"));
        System.out.println(res5); // >>> 1726055713867-0

        // Attempting to add the same message again with IDMP returns the original entry ID
        Map<String, String> idmpEntry2 = new HashMap<>();
        idmpEntry2.put("field", "different_value");
        StreamEntryID res6 = jedis.xadd("mystream", idmpEntry2,
            XAddParams.xAddParams().idmp("producer1", "msg1"));
        System.out.println(res6); // >>> 1726055713867-0 (same ID as res5, message was deduplicated)

        Map<String, String> idmpAutoEntry1 = new HashMap<>();
        idmpAutoEntry1.put("field", "value");
        StreamEntryID res7 = jedis.xadd("mystream", idmpAutoEntry1,
            XAddParams.xAddParams().idmpAuto("producer2"));
        System.out.println(res7); // >>> 1726055713867-1

        // Auto-generated idempotent ID prevents duplicates for same producer+content
        Map<String, String> idmpAutoEntry2 = new HashMap<>();
        idmpAutoEntry2.put("field", "value");
        StreamEntryID res8 = jedis.xadd("mystream", idmpAutoEntry2,
            XAddParams.xAddParams().idmpAuto("producer2"));
        System.out.println(res8); // >>> 1726055713867-1 (same ID as res7, duplicate detected)

        // Configure idempotent message processing settings
        String res9 = jedis.xcfgset("mystream",
            XCfgSetParams.xCfgSetParams().idmpDuration(300).idmpMaxsize(1000));
        System.out.println(res9); // >>> OK
```

##### JavaScript (Node.js)

```javascript
const res5 = await client.xAdd('mystream', '*', { 'field': 'value' }, {
  IDMP: { pid: 'producer1', iid: 'msg1' }
});
console.log(res5); // >>> 1726055713867-0

// Attempting to add the same message again with IDMP returns the original entry ID
const res6 = await client.xAdd('mystream', '*', { 'field': 'different_value' }, {
  IDMP: { pid: 'producer1', iid: 'msg1' }
});
console.log(res6); // >>> 1726055713867-0 (same ID as res5, message was deduplicated)

const res7 = await client.xAdd('mystream', '*', { 'field': 'value' }, {
  IDMPAUTO: { pid: 'producer2' }
});
console.log(res7); // >>> 1726055713867-1

// Auto-generated idempotent ID prevents duplicates for same producer+content
const res8 = await client.xAdd('mystream', '*', { 'field': 'value' }, {
  IDMPAUTO: { pid: 'producer2' }
});
console.log(res8); // >>> 1726055713867-1 (same ID as res7, duplicate detected)

// Configure idempotent message processing settings
const res9 = await client.xCfgSet('mystream', {
  IDMP_DURATION: 300,
  IDMP_MAXSIZE: 1000
});
console.log(res9); // >>> OK
```

##### JavaScript (Node.js)

```javascript
const res5 = await redis.call('XADD', 'mystream', 'IDMP', 'producer1', 'msg1', '*', 'field', 'value');
console.log(res5); // >>> 1726055713867-0

// Attempting to add the same message again with IDMP returns the original entry ID
const res6 = await redis.call('XADD', 'mystream', 'IDMP', 'producer1', 'msg1', '*', 'field', 'different_value');
console.log(res6); // >>> 1726055713867-0 (same ID as res5, message was deduplicated)

const res7 = await redis.call('XADD', 'mystream', 'IDMPAUTO', 'producer2', '*', 'field', 'value');
console.log(res7); // >>> 1726055713867-1

// Auto-generated idempotent ID prevents duplicates for same producer+content
const res8 = await redis.call('XADD', 'mystream', 'IDMPAUTO', 'producer2', '*', 'field', 'value');
console.log(res8); // >>> 1726055713867-1 (same ID as res7, duplicate detected)

// Configure idempotent message processing settings
const res9 = await redis.call('XCFGSET', 'mystream', 'IDMP-DURATION', 300, 'IDMP-MAXSIZE', 1000);
console.log(res9); // >>> OK
```

##### JavaScript (Node.js)

```javascript
const res5 = await client.xAdd('mystream', '*', { 'field': 'value' }, {
  IDMP: { pid: 'producer1', iid: 'msg1' }
});
console.log(res5); // >>> 1726055713867-0

// Attempting to add the same message again with IDMP returns the original entry ID
const res6 = await client.xAdd('mystream', '*', { 'field': 'different_value' }, {
  IDMP: { pid: 'producer1', iid: 'msg1' }
});
console.log(res6); // >>> 1726055713867-0 (same ID as res5, message was deduplicated)

const res7 = await client.xAdd('mystream', '*', { 'field': 'value' }, {
  IDMPAUTO: { pid: 'producer2' }
});
console.log(res7); // >>> 1726055713867-1

// Auto-generated idempotent ID prevents duplicates for same producer+content
const res8 = await client.xAdd('mystream', '*', { 'field': 'value' }, {
  IDMPAUTO: { pid: 'producer2' }
});
console.log(res8); // >>> 1726055713867-1 (same ID as res7, duplicate detected)

// Configure idempotent message processing settings
const res9 = await client.xCfgSet('mystream', {
  IDMP_DURATION: 300,
  IDMP_MAXSIZE: 1000
});
console.log(res9); // >>> OK
```

##### JavaScript (Node.js)

```javascript
const res5 = await redis.call('XADD', 'mystream', 'IDMP', 'producer1', 'msg1', '*', 'field', 'value');
console.log(res5); // >>> 1726055713867-0

// Attempting to add the same message again with IDMP returns the original entry ID
const res6 = await redis.call('XADD', 'mystream', 'IDMP', 'producer1', 'msg1', '*', 'field', 'different_value');
console.log(res6); // >>> 1726055713867-0 (same ID as res5, message was deduplicated)

const res7 = await redis.call('XADD', 'mystream', 'IDMPAUTO', 'producer2', '*', 'field', 'value');
console.log(res7); // >>> 1726055713867-1

// Auto-generated idempotent ID prevents duplicates for same producer+content
const res8 = await redis.call('XADD', 'mystream', 'IDMPAUTO', 'producer2', '*', 'field', 'value');
console.log(res8); // >>> 1726055713867-1 (same ID as res7, duplicate detected)

// Configure idempotent message processing settings
const res9 = await redis.call('XCFGSET', 'mystream', 'IDMP-DURATION', 300, 'IDMP-MAXSIZE', 1000);
console.log(res9); // >>> OK
```

##### PHP

```php
        $res5 = $redis->xadd('mystream', ['field' => 'value'], '*', ['idmp' => ['producer1', 'msg1']]);
        echo $res5 . PHP_EOL; // >>> 1726055713867-0

        // Attempting to add the same message again with IDMP returns the original entry ID
        $res6 = $redis->xadd('mystream', ['field' => 'different_value'], '*', ['idmp' => ['producer1', 'msg1']]);
        echo $res6 . PHP_EOL; // >>> 1726055713867-0 (same ID as res5, message was deduplicated)

        $res7 = $redis->xadd('mystream', ['field' => 'value'], '*', ['idmpauto' => 'producer2']);
        echo $res7 . PHP_EOL; // >>> 1726055713867-1

        // Auto-generated idempotent ID prevents duplicates for same producer+content
        $res8 = $redis->xadd('mystream', ['field' => 'value'], '*', ['idmpauto' => 'producer2']);
        echo $res8 . PHP_EOL; // >>> 1726055713867-1 (same ID as res7, duplicate detected)

        // Configure idempotent message processing settings
        $res9 = $redis->xcfgset('mystream', 300, 1000);
        echo $res9 . PHP_EOL; // >>> OK
```

##### Python

```python
res5 = r.xadd("mystream", {"field": "value"}, idmp=("producer1", b"msg1"))
print(res5)  # >>> 1726055713867-0

# Attempting to add the same message again with IDMP returns the original entry ID
res6 = r.xadd("mystream", {"field": "different_value"}, idmp=("producer1", b"msg1"))
print(res6)  # >>> 1726055713867-0 (same ID as res5, message was deduplicated)

res7 = r.xadd("mystream", {"field": "value"}, idmpauto="producer2")
print(res7)  # >>> 1726055713867-1

# Auto-generated idempotent ID prevents duplicates for same producer+content
res8 = r.xadd("mystream", {"field": "value"}, idmpauto="producer2")
print(res8)  # >>> 1726055713867-1 (same ID as res7, duplicate detected)

# Configure idempotent message processing settings
res9 = r.xcfgset("mystream", idmp_duration=300, idmp_maxsize=1000)
print(res9)  # >>> True
```

##### Ruby

```ruby
res5 = r.call('XADD', 'mystream', 'IDMP', 'producer1', 'msg1', '*', 'field', 'value')
puts res5 # >>> 1726055713867-0

# Attempting to add the same message again with IDMP returns the original entry ID
res6 = r.call('XADD', 'mystream', 'IDMP', 'producer1', 'msg1', '*', 'field', 'different_value')
puts res6 # >>> 1726055713867-0 (same ID as res5, message was deduplicated)

res7 = r.call('XADD', 'mystream', 'IDMPAUTO', 'producer2', '*', 'field', 'value')
puts res7 # >>> 1726055713867-1

# Auto-generated idempotent ID prevents duplicates for same producer+content
res8 = r.call('XADD', 'mystream', 'IDMPAUTO', 'producer2', '*', 'field', 'value')
puts res8 # >>> 1726055713867-1 (same ID as res7, duplicate detected)

# Configure idempotent message processing settings
res9 = r.call('XCFGSET', 'mystream', 'IDMP-DURATION', 300, 'IDMP-MAXSIZE', 1000)
puts res9 # >>> OK
```

##### Rust (Asynchronous)

```rust
        // Note: IDMP is a Redis 8.6 feature - using raw commands
        let res5: String = redis::cmd("XADD")
            .arg("idmpstream")
            .arg("IDMP")
            .arg("producer1")
            .arg("msg1")
            .arg("*")
            .arg("field")
            .arg("value")
            .query_async(&mut con)
            .await
            .unwrap();
        println!("XADD IDMP result: {}", res5); // >>> 1726055713867-0

        // Attempting to add the same message again with IDMP returns the original entry ID
        let res6: String = redis::cmd("XADD")
            .arg("idmpstream")
            .arg("IDMP")
            .arg("producer1")
            .arg("msg1")
            .arg("*")
            .arg("field")
            .arg("different_value")
            .query_async(&mut con)
            .await
            .unwrap();
        println!("XADD IDMP result: {}", res6); // >>> 1726055713867-0 (deduplicated)

        let res7: String = redis::cmd("XADD")
            .arg("idmpstream")
            .arg("IDMPAUTO")
            .arg("producer2")
            .arg("*")
            .arg("field")
            .arg("value")
            .query_async(&mut con)
            .await
            .unwrap();
        println!("XADD IDMPAUTO result: {}", res7); // >>> 1726055713867-1

        // Auto-generated idempotent ID prevents duplicates for same producer+content
        let res8: String = redis::cmd("XADD")
            .arg("idmpstream")
            .arg("IDMPAUTO")
            .arg("producer2")
            .arg("*")
            .arg("field")
            .arg("value")
            .query_async(&mut con)
            .await
            .unwrap();
        println!("XADD IDMPAUTO result: {}", res8); // >>> 1726055713867-1 (duplicate detected)

        // Configure idempotent message processing settings
        let res9: String = redis::cmd("XCFGSET")
            .arg("idmpstream")
            .arg("IDMP-DURATION")
            .arg("300")
            .arg("IDMP-MAXSIZE")
            .arg("1000")
            .query_async(&mut con)
            .await
            .unwrap();
        println!("XCFGSET result: {}", res9); // >>> OK
```

##### Rust (Synchronous)

```rust
        // Note: IDMP is a Redis 8.6 feature - using raw commands
        let res5: String = redis::cmd("XADD")
            .arg("idmpstream")
            .arg("IDMP")
            .arg("producer1")
            .arg("msg1")
            .arg("*")
            .arg("field")
            .arg("value")
            .query(&mut con)
            .unwrap();
        println!("XADD IDMP result: {}", res5); // >>> 1726055713867-0

        // Attempting to add the same message again with IDMP returns the original entry ID
        let res6: String = redis::cmd("XADD")
            .arg("idmpstream")
            .arg("IDMP")
            .arg("producer1")
            .arg("msg1")
            .arg("*")
            .arg("field")
            .arg("different_value")
            .query(&mut con)
            .unwrap();
        println!("XADD IDMP result: {}", res6); // >>> 1726055713867-0 (deduplicated)

        let res7: String = redis::cmd("XADD")
            .arg("idmpstream")
            .arg("IDMPAUTO")
            .arg("producer2")
            .arg("*")
            .arg("field")
            .arg("value")
            .query(&mut con)
            .unwrap();
        println!("XADD IDMPAUTO result: {}", res7); // >>> 1726055713867-1

        // Auto-generated idempotent ID prevents duplicates for same producer+content
        let res8: String = redis::cmd("XADD")
            .arg("idmpstream")
            .arg("IDMPAUTO")
            .arg("producer2")
            .arg("*")
            .arg("field")
            .arg("value")
            .query(&mut con)
            .unwrap();
        println!("XADD IDMPAUTO result: {}", res8); // >>> 1726055713867-1 (duplicate detected)

        // Configure idempotent message processing settings
        let res9: String = redis::cmd("XCFGSET")
            .arg("idmpstream")
            .arg("IDMP-DURATION")
            .arg("300")
            .arg("IDMP-MAXSIZE")
            .arg("1000")
            .query(&mut con)
            .unwrap();
        println!("XCFGSET result: {}", res9); // >>> OK
```



## Details

### Specifying a Stream ID as an argument

A stream entry ID identifies a specific entry inside a stream.

`XADD` auto-generates a unique ID for you if you specify the `*` character (asterisk) as the ID argument. However, you can also specify a well-formed ID to add the new entry with that exact ID, though this is useful only in rare cases.

Specify IDs using two numbers separated by a `-` character:

    1526919030474-55

Both numbers are 64-bit integers. When Redis auto-generates an ID, the
first part is the Unix time in milliseconds of the Redis instance generating
the ID. The second part is a sequence number used to
distinguish IDs generated in the same millisecond.

You can also specify an incomplete ID that consists only of the milliseconds part, which Redis interprets as a zero value for the sequence part.
To have only the sequence part automatically generated, specify the milliseconds part followed by the `-` separator and the `*` character:

```
> XADD mystream 1526919030474-55 message "Hello,"
"1526919030474-55"
> XADD mystream 1526919030474-* message " World!"
"1526919030474-56"
```

Redis guarantees that IDs are always incremental: the ID of any entry you insert will be greater than any previous ID, so entries are totally ordered inside a stream. To guarantee this property, if the current top ID in the stream has a time greater than the current local time of the instance, Redis uses the top entry time instead and increments the sequence part of the ID. This may happen when, for instance, the local clock jumps backward, or after a failover when the new master has a different absolute time.

When you specify an explicit ID to `XADD`, the minimum valid ID is `0-1`, and you *must* specify an ID that is greater than any other ID currently inside the stream, otherwise the command fails and returns an error. Specifying explicit IDs is usually useful only if you have another system generating unique IDs (for instance an SQL table) and you want the Redis stream IDs to match those from your other system.

### Capped streams

`XADD` incorporates the same semantics as the [`XTRIM`](https://redis.io/docs/latest/commands/xtrim) command - refer to its documentation page for more information.
This allows you to add new entries and keep the stream's size in check with a single call to `XADD`, effectively capping the stream with an arbitrary threshold.
Although exact trimming is possible and is the default, due to the internal representation of streams, it is more efficient to add an entry and trim the stream with `XADD` using **almost exact** trimming (the `~` argument).

For example, calling `XADD` in the following form:

    XADD mystream MAXLEN ~ 1000 * ... entry fields here ...

This adds a new entry but also evicts old entries so that the stream contains only 1000 entries, or at most a few tens more.

### Additional information about streams

For more information about Redis streams, see the
[introduction to Redis Streams document](https://redis.io/docs/latest/develop/data-types/streams).

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): The ID of the added entry. The ID is the one automatically generated if an asterisk (`*`) is passed as the _id_ argument, otherwise the command just returns the same ID specified by the user during insertion. When using IDMP and a duplicate is detected, returns the ID of the original entry.
* [Nil reply](../../develop/reference/protocol-spec#bulk-strings): if the NOMKSTREAM option is given and the key doesn't exist.

**RESP3:**

One of the following:
* [Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): The ID of the added entry. The ID is the one automatically generated if an asterisk (`*`) is passed as the _id_ argument, otherwise the command just returns the same ID specified by the user during insertion. When using IDMP and a duplicate is detected, returns the ID of the original entry.
* [Null reply](../../develop/reference/protocol-spec#nulls): if the NOMKSTREAM option is given and the key doesn't exist.



