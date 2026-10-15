# SCAN

```json metadata
{
  "schema_version": 2,
  "title": "SCAN",
  "description": "Iterates over the key names in the database.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"cursor","name":"cursor","type":"integer"},{"display_text":"pattern","name":"pattern","optional":true,"token":"MATCH","type":"pattern"},{"display_text":"count","name":"count","optional":true,"token":"COUNT","type":"integer"},{"display_text":"type","name":"type","optional":true,"since":"6.0.0","token":"TYPE","type":"string"}],
  "syntax_fmt": "SCAN cursor [MATCH pattern] [COUNT count] [TYPE type]",
  "complexity": "O(1) for every call. O(N) for a complete iteration, including enough command calls for the cursor to return back to 0. N is the number of elements inside the collection.",
  "group": "generic",
  "command_flags": ["readonly"],
  "acl_categories": ["@keyspace","@read","@slow"],
  "since": "2.8.0",
  "arity": -2,
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"children":[{"id":"scan-basic-usage","title":"SCAN basic usage"},{"id":"return-value","title":"Return value"},{"id":"scan-guarantees","title":"Scan guarantees"},{"id":"number-of-elements-returned-at-every-scan-call","title":"Number of elements returned at every SCAN call"},{"id":"the-count-option","title":"The COUNT option"},{"id":"the-match-option","title":"The MATCH option"},{"id":"the-type-option","title":"The TYPE option"},{"id":"the-novalues-option","title":"The NOVALUES option"},{"id":"multiple-parallel-iterations","title":"Multiple parallel iterations"},{"id":"terminating-iterations-in-the-middle","title":"Terminating iterations in the middle"},{"id":"calling-scan-with-a-corrupted-cursor","title":"Calling SCAN with a corrupted cursor"},{"id":"guarantee-of-termination","title":"Guarantee of termination"},{"id":"why-scan-may-return-all-the-items-of-an-aggregate-data-type-in-a-single-call","title":"Why SCAN may return all the items of an aggregate data type in a single call?"},{"id":"further-reading","title":"Further reading"},{"id":"additional-examples","title":"Additional examples"}],"id":"details","title":"Details"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": [{"codetabsId":"cmds_generic-stepscan1","commands":[{"acl_categories":["@write","@set","@fast"],"complexity":"O(1)","name":"SADD"},{"acl_categories":["@read","@set","@slow"],"complexity":"O(1)","name":"SSCAN"}],"description":"Set iteration: Iterate set members with pattern matching using SSCAN MATCH (cursor-based iteration, non-blocking)","difficulty":"intermediate","id":"scan1","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_cmds_generic-stepscan1"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_cmds_generic-stepscan1"},{"id":"Node-js","panelId":"panel_Nodejs_cmds_generic-stepscan1"},{"clientId":"ioredis","clientName":"ioredis","id":"ioredis","langId":"javascript","panelId":"panel_ioredis_cmds_generic-stepscan1"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_cmds_generic-stepscan1"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_cmds_generic-stepscan1"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_cmds_generic-stepscan1"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_cmds_generic-stepscan1"},{"clientId":"hiredis","clientName":"hiredis","id":"C","langId":"c","panelId":"panel_C_cmds_generic-stepscan1"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_cmds_generic-stepscan1"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_cmds_generic-stepscan1"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_cmds_generic-stepscan1"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_cmds_generic-stepscan1"}]},{"codetabsId":"cmds_generic-stepscan2","commands":[{"acl_categories":["@keyspace","@read","@slow"],"complexity":"O(1)","name":"SCAN"}],"description":"Keyspace iteration: Iterate database keys with pattern matching using SCAN MATCH and COUNT (demonstrates cursor iteration with sparse results)","difficulty":"intermediate","id":"scan2","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_cmds_generic-stepscan2"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_cmds_generic-stepscan2"},{"id":"Node-js","panelId":"panel_Nodejs_cmds_generic-stepscan2"},{"clientId":"ioredis","clientName":"ioredis","id":"ioredis","langId":"javascript","panelId":"panel_ioredis_cmds_generic-stepscan2"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_cmds_generic-stepscan2"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_cmds_generic-stepscan2"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_cmds_generic-stepscan2"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_cmds_generic-stepscan2"},{"clientId":"hiredis","clientName":"hiredis","id":"C","langId":"c","panelId":"panel_C_cmds_generic-stepscan2"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_cmds_generic-stepscan2"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_cmds_generic-stepscan2"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_cmds_generic-stepscan2"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_cmds_generic-stepscan2"}]},{"codetabsId":"cmds_generic-stepscan3","commands":[{"acl_categories":["@write","@geo","@slow"],"complexity":"O(log(N)","name":"GEOADD"},{"acl_categories":["@write","@sortedset","@fast"],"complexity":"O(log(N)","name":"ZADD"},{"acl_categories":["@keyspace","@read","@fast"],"complexity":"O(1)","name":"TYPE"},{"acl_categories":["@keyspace","@read","@slow"],"complexity":"O(1)","name":"SCAN"}],"description":"Iterate keyspace by type: Iterate database keys filtered by type using SCAN TYPE (filters keys by data type, useful for type-specific operations)","difficulty":"intermediate","id":"scan3","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_cmds_generic-stepscan3"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_cmds_generic-stepscan3"},{"id":"Node-js","panelId":"panel_Nodejs_cmds_generic-stepscan3"},{"clientId":"ioredis","clientName":"ioredis","id":"ioredis","langId":"javascript","panelId":"panel_ioredis_cmds_generic-stepscan3"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_cmds_generic-stepscan3"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_cmds_generic-stepscan3"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_cmds_generic-stepscan3"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_cmds_generic-stepscan3"},{"clientId":"hiredis","clientName":"hiredis","id":"C","langId":"c","panelId":"panel_C_cmds_generic-stepscan3"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_cmds_generic-stepscan3"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_cmds_generic-stepscan3"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_cmds_generic-stepscan3"}]},{"codetabsId":"cmds_generic-stepscan4","commands":[{"acl_categories":["@write","@hash","@fast"],"complexity":"O(1)","name":"HSET"},{"acl_categories":["@read","@hash","@slow"],"complexity":"O(1)","name":"HSCAN"}],"description":"Hash iteration: Iterate hash fields with optional NOVALUES using HSCAN (returns field-value pairs or fields only)","difficulty":"intermediate","id":"scan4","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_cmds_generic-stepscan4"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_cmds_generic-stepscan4"},{"id":"Node-js","panelId":"panel_Nodejs_cmds_generic-stepscan4"},{"clientId":"ioredis","clientName":"ioredis","id":"ioredis","langId":"javascript","panelId":"panel_ioredis_cmds_generic-stepscan4"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_cmds_generic-stepscan4"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_cmds_generic-stepscan4"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_cmds_generic-stepscan4"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_cmds_generic-stepscan4"},{"clientId":"hiredis","clientName":"hiredis","id":"C","langId":"c","panelId":"panel_C_cmds_generic-stepscan4"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_cmds_generic-stepscan4"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_cmds_generic-stepscan4"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_cmds_generic-stepscan4"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_cmds_generic-stepscan4"}]}]
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

> [!NOTE]
> This command's behavior varies in clustered Redis environments. See the [multi-key operations](https://redis.io/docs/latest/develop/using-commands/multi-key-operations) page for more information.


The `SCAN` command and the closely related commands [`SSCAN`](https://redis.io/docs/latest/commands/sscan), [`HSCAN`](https://redis.io/docs/latest/commands/hscan) and [`ZSCAN`](https://redis.io/docs/latest/commands/zscan) are used in order to incrementally iterate over a collection of elements.

* `SCAN` iterates the set of keys in the currently selected Redis database.
* [`SSCAN`](https://redis.io/docs/latest/commands/sscan) iterates elements of Sets types.
* [`HSCAN`](https://redis.io/docs/latest/commands/hscan) iterates fields of Hash types and their associated values.
* [`ZSCAN`](https://redis.io/docs/latest/commands/zscan) iterates elements of Sorted Set types and their associated scores.

Since these commands allow for incremental iteration, returning only a small number of elements per call, they can be used in production without the downside of commands like [`KEYS`](https://redis.io/docs/latest/commands/keys) or [`SMEMBERS`](https://redis.io/docs/latest/commands/smembers) that may block the server for a long time (even several seconds) when called against big collections of keys or elements.

However while blocking commands like [`SMEMBERS`](https://redis.io/docs/latest/commands/smembers) are able to provide all the elements that are part of a Set in a given moment, The SCAN family of commands only offer limited guarantees about the returned elements since the collection that we incrementally iterate can change during the iteration process.

Note that `SCAN`, [`SSCAN`](https://redis.io/docs/latest/commands/sscan), [`HSCAN`](https://redis.io/docs/latest/commands/hscan) and [`ZSCAN`](https://redis.io/docs/latest/commands/zscan) all work very similarly, so this documentation covers all four commands. However an obvious difference is that in the case of [`SSCAN`](https://redis.io/docs/latest/commands/sscan), [`HSCAN`](https://redis.io/docs/latest/commands/hscan) and [`ZSCAN`](https://redis.io/docs/latest/commands/zscan) the first argument is the name of the key holding the Set, Hash or Sorted Set value. The `SCAN` command does not need any key name argument as it iterates keys in the current database, so the iterated object is the database itself.

## Required arguments

<details open><summary><code>cursor</code></summary>

The cursor value. Start an iteration with `0`, then use the cursor returned by each call as the argument to the next call.

</details>

## Optional arguments

<details open><summary><code>MATCH pattern</code></summary>

Only return keys matching the given glob-style pattern.

</details>

<details open><summary><code>COUNT count</code></summary>

A hint for the number of keys to return per iteration. The default is 10.

</details>

<details open><summary><code>TYPE type</code></summary>

Only return keys of the given type, such as `string`, `list`, or `set`.

</details>

## Details

### SCAN basic usage

SCAN is a cursor based iterator. This means that at every call of the command, the server returns an updated cursor that the user needs to use as the cursor argument in the next call.

An iteration starts when the cursor is set to 0, and terminates when the cursor returned by the server is 0. The following is an example of SCAN iteration:

```
> scan 0
1) "17"
2)  1) "key:12"
    2) "key:8"
    3) "key:4"
    4) "key:14"
    5) "key:16"
    6) "key:17"
    7) "key:15"
    8) "key:10"
    9) "key:3"
   10) "key:7"
   11) "key:1"
> scan 17
1) "0"
2) 1) "key:5"
   2) "key:18"
   3) "key:0"
   4) "key:2"
   5) "key:19"
   6) "key:13"
   7) "key:6"
   8) "key:9"
   9) "key:11"
```

In the example above, the first call uses zero as a cursor, to start the iteration. The second call uses the cursor returned by the previous call as the first element of the reply, that is, 17.

As you can see the **SCAN return value** is an array of two values: the first value is the new cursor to use in the next call, the second value is an array of elements.

Since in the second call the returned cursor is 0, the server signaled to the caller that the iteration finished, and the collection was completely explored. Starting an iteration with a cursor value of 0, and calling `SCAN` until the returned cursor is 0 again is called a **full iteration**.

### Return value

`SCAN`, [`SSCAN`](https://redis.io/docs/latest/commands/sscan), [`HSCAN`](https://redis.io/docs/latest/commands/hscan) and [`ZSCAN`](https://redis.io/docs/latest/commands/zscan) return a two element multi-bulk reply, where the first element is a string representing an unsigned 64 bit number (the cursor), and the second element is a multi-bulk with an array of elements.

* `SCAN` array of elements is a list of keys.
* [`SSCAN`](https://redis.io/docs/latest/commands/sscan) array of elements is a list of Set members.
* [`HSCAN`](https://redis.io/docs/latest/commands/hscan) array of elements contain two elements, a field and a value, for every returned element of the Hash.
* [`ZSCAN`](https://redis.io/docs/latest/commands/zscan) array of elements contain two elements, a member and its associated score, for every returned element of the Sorted Set.

### Scan guarantees

The `SCAN` command, and the other commands in the `SCAN` family, are able to provide to the user a set of guarantees associated to full iterations.

* A full iteration always retrieves all the elements that were present in the collection from the start to the end of a full iteration. This means that if a given element is inside the collection when an iteration is started, and is still there when an iteration terminates, then at some point `SCAN` returned it to the user.
* A full iteration never returns any element that was NOT present in the collection from the start to the end of a full iteration. So if an element was removed before the start of an iteration, and is never added back to the collection for all the time an iteration lasts, `SCAN` ensures that this element will never be returned.

However because `SCAN` has very little state associated (just the cursor) it has the following drawbacks:

* A given element may be returned multiple times. It is up to the application to handle the case of duplicated elements, for example only using the returned elements in order to perform operations that are safe when re-applied multiple times.
* Elements that were not constantly present in the collection during a full iteration, may be returned or not: it is undefined.

### Number of elements returned at every SCAN call

`SCAN` family functions do not guarantee that the number of elements returned per call are in a given range. The commands are also allowed to return zero elements, and the client should not consider the iteration complete as long as the returned cursor is not zero.

However the number of returned elements is reasonable, that is, in practical terms `SCAN` may return a maximum number of elements in the order of a few tens of elements when iterating a large collection, or may return all the elements of the collection in a single call when the iterated collection is small enough to be internally represented as an encoded data structure (this happens for small Sets, Hashes and Sorted Sets).

However there is a way for the user to tune the order of magnitude of the number of returned elements per call using the **COUNT** option.

### The COUNT option

While `SCAN` does not provide guarantees about the number of elements returned at every iteration, it is possible to empirically adjust the behavior of `SCAN` using the **COUNT** option. Basically with COUNT the user specifies the *amount of work that should be done at every call in order to retrieve elements from the collection*. This is **just a hint** for the implementation, however generally speaking this is what you could expect most of the times from the implementation.

* The default `COUNT` value is 10.
* When iterating the key space, or a Set, Hash or Sorted Set that is big enough to be represented by a hash table, assuming no **MATCH** option is used, the server will usually return *count* or a few more than *count* elements per call. Please check the *why SCAN may return all the elements at once* section later in this document.
* When iterating Sets encoded as intsets (small sets composed of just integers), or Hashes and Sorted Sets encoded as ziplists (small hashes and sets composed of small individual values), usually all the elements are returned in the first `SCAN` call regardless of the `COUNT` value.

Important: **there is no need to use the same COUNT value** for every iteration. The caller is free to change the count from one iteration to the other as required, as long as the cursor passed in the next call is the one obtained in the previous call to the command.

### The MATCH option

It is possible to only iterate elements matching a given glob-style pattern, similarly to the behavior of the [`KEYS`](https://redis.io/docs/latest/commands/keys) command that takes a pattern as its only argument.

To do so, just append the `MATCH <pattern>` arguments at the end of the `SCAN` command (it works with all the `SCAN` family commands).

This is an example of iteration using **MATCH**:

Set iteration: Iterate set members with pattern matching using SSCAN MATCH (cursor-based iteration, non-blocking)

**Difficulty:** Intermediate

**Commands:** SADD, SSCAN

**Complexity:**
- SADD: O(1)
- SSCAN: O(1)

**Available in:** Redis CLI, C, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), JavaScript (Node.js), PHP, Python, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> sadd myset 1 2 3 foo foobar feelsgood
(integer) 6
> sscan myset 0 match f*
1) "0"
2) 1) "foo"
   2) "feelsgood"
   3) "foobar"
```

##### C

```c
    reply = redisCommand(c, "SADD myset 1 2 3 foo foobar feelsgood");
    printf("%lld\n", reply->integer);
    // >>> 6
    freeReplyObject(reply);

    // SCAN-family replies are a two-element array: the next cursor, then the results.
    reply = redisCommand(c, "SSCAN myset 0 MATCH f*");
    printf("%zu\n", reply->element[1]->elements);
    // >>> 3
    freeReplyObject(reply);
```

##### C#

```csharp

```

##### Go

```go
	scan1Result1, err := rdb.SAdd(ctx, "myset", "1", "2", "3", "foo", "foobar", "feelsgood").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(scan1Result1) // >>> 6

	scan1Result2, _, err := rdb.SScan(ctx, "myset", 0, "f*", 0).Result()

	if err != nil {
		panic(err)
	}

	sort.Strings(scan1Result2)
	fmt.Println(scan1Result2) // >>> [feelsgood foo foobar]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> scan1Example = asyncCommands
                    .sadd("myset", "1", "2", "3", "foo", "foobar", "feelsgood")
                    .thenCompose(scan1Res1 -> {
                        System.out.println(scan1Res1);      // >>> 6
                        return asyncCommands.sscan("myset", ScanArgs.Builder.matches("f*"));
                    })
                    .thenAccept(scan1Res2 -> {
                        List<String> members = new java.util.ArrayList<>(scan1Res2.getValues());
                        Collections.sort(members);
                        System.out.println(members);        // >>> [feelsgood, foo, foobar]
                    })
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> scan1Example = reactiveCommands
                    .sadd("myset", "1", "2", "3", "foo", "foobar", "feelsgood")
                    .flatMap(scan1Res1 -> {
                        System.out.println(scan1Res1);      // >>> 6
                        return reactiveCommands.sscan("myset", ScanArgs.Builder.matches("f*"));
                    })
                    .doOnNext(scan1Res2 -> {
                        List<String> members = new java.util.ArrayList<>(scan1Res2.getValues());
                        Collections.sort(members);
                        System.out.println(members);        // >>> [feelsgood, foo, foobar]
                    })
                    .then();
```

##### Java (Synchronous - Jedis)

```java
        long scan1Result1 = jedis.sadd("myset", "1", "2", "3", "foo", "foobar", "feelsgood");
        System.out.println(scan1Result1); // >>> 6

        ScanResult<String> scan1Result2 = jedis.sscan(
                "myset", "0", new ScanParams().match("f*")
        );
        ArrayList<String> scan1Members = new ArrayList<>(scan1Result2.getResult());
        Collections.sort(scan1Members);
        System.out.println(scan1Members); // >>> [feelsgood, foo, foobar]
```

##### JavaScript (Node.js)

```javascript
const scan1Res1 = await client.sAdd('myset', ['1', '2', '3', 'foo', 'foobar', 'feelsgood']);
console.log(scan1Res1); // 6

let scan1Res2 = [];
for await (const values of client.sScanIterator('myset', { MATCH: 'f*' })) {
    scan1Res2 = scan1Res2.concat(values);
}
console.log(scan1Res2); // ['foo', 'foobar', 'feelsgood']
```

##### JavaScript (Node.js)

```javascript
const scan1Res1 = await redis.sadd('myset', '1', '2', '3', 'foo', 'foobar', 'feelsgood');
console.log(scan1Res1); // >>> 6

const [, scan1Members] = await redis.sscan('myset', 0, 'MATCH', 'f*');
console.log(scan1Members.sort()); // >>> ['feelsgood', 'foo', 'foobar']
```

##### JavaScript (Node.js)

```javascript
const scan1Res1 = await client.sAdd('myset', ['1', '2', '3', 'foo', 'foobar', 'feelsgood']);
console.log(scan1Res1); // 6

let scan1Res2 = [];
for await (const values of client.sScanIterator('myset', { MATCH: 'f*' })) {
    scan1Res2 = scan1Res2.concat(values);
}
console.log(scan1Res2); // ['foo', 'foobar', 'feelsgood']
```

##### JavaScript (Node.js)

```javascript
const scan1Res1 = await redis.sadd('myset', '1', '2', '3', 'foo', 'foobar', 'feelsgood');
console.log(scan1Res1); // >>> 6

const [, scan1Members] = await redis.sscan('myset', 0, 'MATCH', 'f*');
console.log(scan1Members.sort()); // >>> ['feelsgood', 'foo', 'foobar']
```

##### PHP

```php
        $scan1Result1 = $r->sadd('myset', ['1', '2', '3', 'foo', 'foobar', 'feelsgood']);
        echo $scan1Result1 . PHP_EOL;                       // >>> 6

        [$scan1Cursor, $scan1Members] = $r->sscan('myset', 0, ['MATCH' => 'f*']);
        sort($scan1Members);
        echo implode(', ', $scan1Members) . PHP_EOL;         // >>> feelsgood, foo, foobar
```

##### Python

```python
res = r.sadd("myset", *set([1, 2, 3, "foo", "foobar", "feelsgood"]))
print(res)
# >>> 6

res = list(r.sscan_iter("myset", match="f*"))
print(res)
# >>> ['foobar', 'foo', 'feelsgood']
```

##### Rust (Asynchronous)

```rust
        match r.sadd("myset", &["1", "2", "3", "foo", "foobar", "feelsgood"]).await {
            Ok(res) => {
                let res: i32 = res;
                println!("{res}");    // >>> 6
            },
            Err(e) => {
                println!("Error adding to set: {e}");
                return;
            }
        }

        let res = match r.sscan_match("myset", "f*").await {
            Ok(iter) => {
                let res: Vec<Result<String, _>> = iter.collect().await;
                res.into_iter().filter_map(|r| r.ok()).collect::<Vec<String>>()
            },
            Err(e) => {
                println!("Error scanning set: {e}");
                return;
            }
        };

        println!("{res:?}");    // >>> ["foo", "foobar", "feelsgood"]
```

##### Rust (Synchronous)

```rust
        match r.sadd("myset", &["1", "2", "3", "foo", "foobar", "feelsgood"]) {
            Ok(res) => {
                let res: i32 = res;
                println!("{res}");    // >>> 6
            },
            Err(e) => {
                println!("Error adding to set: {e}");
                return;
            }
        }

        match r.sscan_match("myset", "f*") {
            Ok(iter) => {
                let res: Vec<String> = iter.filter_map(|r| r.ok()).collect();
                println!("{res:?}");    // >>> ["foo", "foobar", "feelsgood"]
            },
            Err(e) => {
                println!("Error scanning set: {e}");
                return;
            }
        }
```



It is important to note that the **MATCH** filter is applied after elements are retrieved from the collection, just before returning data to the client. This means that if the pattern matches very little elements inside the collection, `SCAN` will likely return no elements in most iterations. An example is shown below:

Keyspace iteration: Iterate database keys with pattern matching using SCAN MATCH and COUNT (demonstrates cursor iteration with sparse results)

**Difficulty:** Intermediate

**Commands:** SCAN

**Complexity:**
- SCAN: O(1)

**Available in:** Redis CLI, C, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), JavaScript (Node.js), PHP, Python, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> scan 0 MATCH *11*
1) "288"
2) 1) "key:911"
> scan 288 MATCH *11*
1) "224"
2) (empty list or set)
> scan 224 MATCH *11*
1) "80"
2) (empty list or set)
> scan 80 MATCH *11*
1) "176"
2) (empty list or set)
> scan 176 MATCH *11* COUNT 1000
1) "0"
2)  1) "key:611"
    2) "key:711"
    3) "key:118"
    4) "key:117"
    5) "key:311"
    6) "key:112"
    7) "key:111"
    8) "key:110"
    9) "key:113"
   10) "key:211"
   11) "key:411"
   12) "key:115"
   13) "key:116"
   14) "key:114"
   15) "key:119"
   16) "key:811"
   17) "key:511"
   18) "key:11"
```

##### C

```c
    // MATCH is applied after elements are fetched, so with the default COUNT most
    // iterations return few keys or none at all.
    char cursor[64] = "0";

    for (int i = 0; i < 4; i++) {
        reply = redisCommand(c, "SCAN %s MATCH *11*", cursor);
        snprintf(cursor, sizeof(cursor), "%s", reply->element[0]->str);
        printf("%zu\n", reply->element[1]->elements);
        freeReplyObject(reply);
    }

    // A larger COUNT forces more scanning in a single iteration, so the remaining
    // matches arrive together. This continues from the cursor reached above.
    reply = redisCommand(c, "SCAN %s MATCH *11* COUNT 1000", cursor);
    printf("%zu\n", reply->element[1]->elements);
    // >>> 18
    freeReplyObject(reply);
```

##### C#

```csharp

```

##### Go

```go
	// MATCH is applied after elements are fetched, so with the default COUNT most
	// iterations return few keys or none at all.
	var scan2Cursor uint64
	var scan2Keys []string
	var err error
	scan2Total := 0

	for i := 0; i < 4; i++ {
		scan2Keys, scan2Cursor, err = rdb.Scan(ctx, scan2Cursor, "*11*", 0).Result()

		if err != nil {
			panic(err)
		}
		scan2Total += len(scan2Keys)
	}

	// A larger COUNT forces more scanning in a single iteration, so the remaining
	// matches arrive together. This continues from the cursor reached above.
	scan2Keys, _, err = rdb.Scan(ctx, scan2Cursor, "*11*", 1000).Result()

	if err != nil {
		panic(err)
	}
	scan2Total += len(scan2Keys)

	// The per-call split isn't guaranteed, but the cumulative total is.
	fmt.Println(scan2Total) // >>> 19
```

##### Java (Asynchronous - Lettuce)

```java

            // MATCH is applied after elements are fetched, so with the default COUNT most
            // iterations return few keys or none at all. Each iteration is awaited because
            // the next one needs the cursor this one returns.
            KeyScanCursor<String> scan2Cursor = asyncCommands
                    .scan(ScanArgs.Builder.matches("*11*")).toCompletableFuture().join();
            int scan2Total = scan2Cursor.getKeys().size();
            System.out.println(scan2Cursor.getKeys().size());

            for (int i = 0; i < 3; i++) {
                scan2Cursor = asyncCommands
                        .scan(scan2Cursor, ScanArgs.Builder.matches("*11*"))
                        .toCompletableFuture().join();
                scan2Total += scan2Cursor.getKeys().size();
                System.out.println(scan2Cursor.getKeys().size());
            }

            // A larger COUNT forces more scanning in a single iteration, so the remaining
            // matches arrive together. This continues from the cursor reached above.
            scan2Cursor = asyncCommands
                    .scan(scan2Cursor, ScanArgs.Builder.matches("*11*").limit(1000))
                    .toCompletableFuture().join();
            scan2Total += scan2Cursor.getKeys().size();
            System.out.println(scan2Cursor.getKeys().size());

            // The per-call split isn't guaranteed, but the cumulative total is.
            System.out.println(scan2Total);   // >>> 19
```

##### Java (Reactive - Lettuce)

```java

            // MATCH is applied after elements are fetched, so with the default COUNT most
            // iterations return few keys or none at all. Each iteration is subscribed to in
            // turn because the next one needs the cursor this one returns.
            KeyScanCursor<String> scan2Cursor = reactiveCommands
                    .scan(ScanArgs.Builder.matches("*11*")).block();
            int scan2Total = scan2Cursor.getKeys().size();
            System.out.println(scan2Cursor.getKeys().size());

            for (int i = 0; i < 3; i++) {
                scan2Cursor = reactiveCommands
                        .scan(scan2Cursor, ScanArgs.Builder.matches("*11*")).block();
                scan2Total += scan2Cursor.getKeys().size();
                System.out.println(scan2Cursor.getKeys().size());
            }

            // A larger COUNT forces more scanning in a single iteration, so the remaining
            // matches arrive together. This continues from the cursor reached above.
            scan2Cursor = reactiveCommands
                    .scan(scan2Cursor, ScanArgs.Builder.matches("*11*").limit(1000)).block();
            scan2Total += scan2Cursor.getKeys().size();
            System.out.println(scan2Cursor.getKeys().size());

            // The per-call split isn't guaranteed, but the cumulative total is.
            System.out.println(scan2Total);   // >>> 19
```

##### Java (Synchronous - Jedis)

```java

        // MATCH is applied after elements are fetched, so with the default COUNT most
        // iterations return few keys or none at all.
        String scan2Cursor = "0";
        ScanResult<String> scan2Result;
        int scan2Total = 0;

        for (int i = 0; i < 4; i++) {
            scan2Result = jedis.scan(scan2Cursor, new ScanParams().match("*11*"));
            scan2Cursor = scan2Result.getCursor();
            scan2Total += scan2Result.getResult().size();
            System.out.println(scan2Result.getResult().size());
        }

        // A larger COUNT forces more scanning in a single iteration, so the remaining
        // matches arrive together. This continues from the cursor reached above.
        scan2Result = jedis.scan(scan2Cursor, new ScanParams().match("*11*").count(1000));
        scan2Total += scan2Result.getResult().size();
        System.out.println(scan2Result.getResult().size());

        // The per-call split isn't guaranteed, but the cumulative total is.
        System.out.println(scan2Total); // >>> 19
```

##### JavaScript (Node.js)

```javascript

let cursor = '0';
let scanResult;
let total = 0;

scanResult = await client.scan(cursor, { MATCH: '*11*' });
total += scanResult.keys.length;
console.log(scanResult.cursor, scanResult.keys);

scanResult = await client.scan(scanResult.cursor, { MATCH: '*11*' });
total += scanResult.keys.length;
console.log(scanResult.cursor, scanResult.keys);

scanResult = await client.scan(scanResult.cursor, { MATCH: '*11*' });
total += scanResult.keys.length;
console.log(scanResult.cursor, scanResult.keys);

scanResult = await client.scan(scanResult.cursor, { MATCH: '*11*' });
total += scanResult.keys.length;
console.log(scanResult.cursor, scanResult.keys);

scanResult = await client.scan(scanResult.cursor, { MATCH: '*11*', COUNT: 1000 });
total += scanResult.keys.length;
console.log(scanResult.cursor, scanResult.keys);

// The per-call split isn't guaranteed, but the cumulative total is.
console.log(total);
// >>> 19
```

##### JavaScript (Node.js)

```javascript

// MATCH filters after the elements are fetched, so most iterations return nothing.
let [scan2Cursor, scan2Keys] = await redis.scan(0, 'MATCH', '*11*');
let scan2Total = scan2Keys.length;
console.log(scan2Keys.length);

for (let i = 0; i < 3; i++) {
  [scan2Cursor, scan2Keys] = await redis.scan(scan2Cursor, 'MATCH', '*11*');
  scan2Total += scan2Keys.length;
  console.log(scan2Keys.length);
}

// A larger COUNT forces more scanning in a single iteration, so the rest of the
// matches arrive together. The scan continues from the cursor reached above.
[scan2Cursor, scan2Keys] = await redis.scan(scan2Cursor, 'MATCH', '*11*', 'COUNT', 1000);
scan2Total += scan2Keys.length;
console.log(scan2Keys.length);

// The per-call split isn't guaranteed, but the cumulative total is.
console.log(scan2Total); // >>> 19
```

##### JavaScript (Node.js)

```javascript

let cursor = '0';
let scanResult;
let total = 0;

scanResult = await client.scan(cursor, { MATCH: '*11*' });
total += scanResult.keys.length;
console.log(scanResult.cursor, scanResult.keys);

scanResult = await client.scan(scanResult.cursor, { MATCH: '*11*' });
total += scanResult.keys.length;
console.log(scanResult.cursor, scanResult.keys);

scanResult = await client.scan(scanResult.cursor, { MATCH: '*11*' });
total += scanResult.keys.length;
console.log(scanResult.cursor, scanResult.keys);

scanResult = await client.scan(scanResult.cursor, { MATCH: '*11*' });
total += scanResult.keys.length;
console.log(scanResult.cursor, scanResult.keys);

scanResult = await client.scan(scanResult.cursor, { MATCH: '*11*', COUNT: 1000 });
total += scanResult.keys.length;
console.log(scanResult.cursor, scanResult.keys);

// The per-call split isn't guaranteed, but the cumulative total is.
console.log(total);
// >>> 19
```

##### JavaScript (Node.js)

```javascript

// MATCH filters after the elements are fetched, so most iterations return nothing.
let [scan2Cursor, scan2Keys] = await redis.scan(0, 'MATCH', '*11*');
let scan2Total = scan2Keys.length;
console.log(scan2Keys.length);

for (let i = 0; i < 3; i++) {
  [scan2Cursor, scan2Keys] = await redis.scan(scan2Cursor, 'MATCH', '*11*');
  scan2Total += scan2Keys.length;
  console.log(scan2Keys.length);
}

// A larger COUNT forces more scanning in a single iteration, so the rest of the
// matches arrive together. The scan continues from the cursor reached above.
[scan2Cursor, scan2Keys] = await redis.scan(scan2Cursor, 'MATCH', '*11*', 'COUNT', 1000);
scan2Total += scan2Keys.length;
console.log(scan2Keys.length);

// The per-call split isn't guaranteed, but the cumulative total is.
console.log(scan2Total); // >>> 19
```

##### PHP

```php

        // MATCH is applied after elements are fetched, so with the default COUNT most
        // iterations return few keys or none at all.
        $scan2Cursor = 0;
        $scan2Total = 0;

        for ($i = 0; $i < 4; $i++) {
            [$scan2Cursor, $scan2Keys] = $r->scan($scan2Cursor, ['MATCH' => '*11*']);
            $scan2Total += count($scan2Keys);
            echo count($scan2Keys) . PHP_EOL;
        }

        // A larger COUNT forces more scanning in a single iteration, so the remaining
        // matches arrive together. This continues from the cursor reached above.
        [$scan2Cursor, $scan2Keys] = $r->scan($scan2Cursor, ['MATCH' => '*11*', 'COUNT' => 1000]);
        $scan2Total += count($scan2Keys);
        echo count($scan2Keys) . PHP_EOL;

        // The per-call split isn't guaranteed, but the cumulative total is.
        echo $scan2Total . PHP_EOL;                          // >>> 19
```

##### Python

```python

total = 0

cursor, keys = r.scan(cursor=0, match='*11*')
total += len(keys)
print(cursor, keys)

cursor, keys = r.scan(cursor, match='*11*')
total += len(keys)
print(cursor, keys)

cursor, keys = r.scan(cursor, match='*11*')
total += len(keys)
print(cursor, keys)

cursor, keys = r.scan(cursor, match='*11*')
total += len(keys)
print(cursor, keys)

cursor, keys = r.scan(cursor, match='*11*', count=1000)
total += len(keys)
print(cursor, keys)

# The per-call split isn't guaranteed, but the cumulative total is.
print(total)
# >>> 19

```

##### Rust (Asynchronous)

```rust

        // Note: Rust redis client scan_match returns an iterator, not cursor-based
        // This simulates the Python cursor-based output but uses the available API
        let keys = match r.scan_match("*11*").await {
            Ok(iter) => {
                let keys: Vec<Result<String, _>> = iter.collect().await;
                keys.into_iter().filter_map(|r| r.ok()).collect::<Vec<String>>()
            },
            Err(e) => {
                println!("Error scanning keys: {e}");
                return;
            }
        };

```

##### Rust (Synchronous)

```rust

        // Note: Rust redis client scan_match returns an iterator, not cursor-based
        // This simulates the Python cursor-based output but uses the available API
        match r.scan_match("*11*") {
            Ok(iter) => {
                let keys: Vec<String> = iter.filter_map(|r| r.ok()).collect();
            },
            Err(e) => {
                println!("Error scanning keys: {e}");
                return;
            }
        }
```



As you can see most of the calls returned zero elements, but the last call where a `COUNT` of 1000 was used in order to force the command to do more scanning for that iteration.

When using [Redis Cluster](https://redis.io/docs/latest/operate/oss_and_stack/management/scaling), the search is optimized for patterns that imply a single slot.
If a pattern can only match keys of one slot,
Redis only iterates over keys in that slot, rather than the whole database,
when searching for keys matching the pattern.
For example, with the pattern `{a}h*llo`, Redis would only try to match it with the keys in slot 15495, which hash tag `{a}` implies.
To use pattern with hash tag, see [Hash tags](https://redis.io/docs/latest/operate/oss_and_stack/reference/cluster-spec#hash-tags) in the Cluster specification for more information.

### The TYPE option

You can use the `TYPE` option to ask `SCAN` to only return objects that match a given `type`, allowing you to iterate through the database looking for keys of a specific type. The **TYPE** option is only available on the whole-database `SCAN`, not [`HSCAN`](https://redis.io/docs/latest/commands/hscan) or [`ZSCAN`](https://redis.io/docs/latest/commands/zscan) etc.

The `type` argument is the same string name that the [`TYPE`](https://redis.io/docs/latest/commands/type) command returns. Note a quirk where some Redis types, such as GeoHashes, HyperLogLogs, Bitmaps, and Bitfields, may internally be implemented using other Redis types, such as a string or zset, so can't be distinguished from other keys of that same type by `SCAN`. For example, a ZSET and GEOHASH:

Iterate keyspace by type: Iterate database keys filtered by type using SCAN TYPE (filters keys by data type, useful for type-specific operations)

**Difficulty:** Intermediate

**Commands:** GEOADD, ZADD, TYPE, SCAN

**Complexity:**
- GEOADD: O(log(N)
- ZADD: O(log(N)
- TYPE: O(1)
- SCAN: O(1)

**Available in:** Redis CLI, C, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), JavaScript (Node.js), PHP, Python, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> GEOADD geokey 0 0 value
(integer) 1
> ZADD zkey 1000 value
(integer) 1
> TYPE geokey
zset
> TYPE zkey
zset
> SCAN 0 TYPE zset
1) "0"
2) 1) "geokey"
   2) "zkey"
```

##### C

```c
    reply = redisCommand(c, "GEOADD geokey 0 0 value");
    printf("%lld\n", reply->integer);
    // >>> 1
    freeReplyObject(reply);

    reply = redisCommand(c, "ZADD zkey 1000 value");
    printf("%lld\n", reply->integer);
    // >>> 1
    freeReplyObject(reply);

    reply = redisCommand(c, "TYPE geokey");
    printf("%s\n", reply->str);
    // >>> zset
    freeReplyObject(reply);

    reply = redisCommand(c, "TYPE zkey");
    printf("%s\n", reply->str);
    // >>> zset
    freeReplyObject(reply);

    reply = redisCommand(c, "SCAN 0 TYPE zset");
    printf("%zu\n", reply->element[1]->elements);
    // >>> 2
    freeReplyObject(reply);
```

##### C#

```csharp

```

##### Go

```go
	scan3Result1, err := rdb.GeoAdd(ctx, "geokey", &redis.GeoLocation{
		Longitude: 0, Latitude: 0, Name: "value",
	}).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(scan3Result1) // >>> 1

	scan3Result2, err := rdb.ZAdd(ctx, "zkey", redis.Z{Score: 1000, Member: "value"}).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(scan3Result2) // >>> 1

	scan3Result3, err := rdb.Type(ctx, "geokey").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(scan3Result3) // >>> zset

	scan3Result4, err := rdb.Type(ctx, "zkey").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(scan3Result4) // >>> zset

	// A single call isn't guaranteed to find every match, so loop until the cursor
	// returns to 0, accumulating matches from every call.
	var scan3Cursor uint64
	var scan3Keys []string
	var scan3Batch []string

	for {
		scan3Batch, scan3Cursor, err = rdb.ScanType(ctx, scan3Cursor, "", 0, "zset").Result()

		if err != nil {
			panic(err)
		}
		scan3Keys = append(scan3Keys, scan3Batch...)

		if scan3Cursor == 0 {
			break
		}
	}

	sort.Strings(scan3Keys)
	fmt.Println(scan3Keys) // >>> [geokey zkey]
```

##### Java (Asynchronous - Lettuce)

```java
            long scan3Result1 = asyncCommands.geoadd("geokey", 0, 0, "value")
                    .toCompletableFuture().join();
            System.out.println(scan3Result1);      // >>> 1

            long scan3Result2 = asyncCommands.zadd("zkey", 1000, "value")
                    .toCompletableFuture().join();
            System.out.println(scan3Result2);      // >>> 1

            String scan3Result3 = asyncCommands.type("geokey").toCompletableFuture().join();
            System.out.println(scan3Result3);      // >>> zset

            String scan3Result4 = asyncCommands.type("zkey").toCompletableFuture().join();
            System.out.println(scan3Result4);      // >>> zset

            // A single call isn't guaranteed to find every match, so loop until
            // the cursor is finished, accumulating matches from every call.
            List<String> scan3Keys = new java.util.ArrayList<>();
            KeyScanCursor<String> scan3Cursor = asyncCommands
                    .scan(KeyScanArgs.Builder.type("zset")).toCompletableFuture().join();
            scan3Keys.addAll(scan3Cursor.getKeys());
            while (!scan3Cursor.isFinished()) {
                scan3Cursor = asyncCommands
                        .scan(scan3Cursor, KeyScanArgs.Builder.type("zset"))
                        .toCompletableFuture().join();
                scan3Keys.addAll(scan3Cursor.getKeys());
            }
            Collections.sort(scan3Keys);
            System.out.println(scan3Keys);         // >>> [geokey, zkey]
```

##### Java (Reactive - Lettuce)

```java
            long scan3Result1 = reactiveCommands.geoadd("geokey", 0, 0, "value").block();
            System.out.println(scan3Result1);      // >>> 1

            long scan3Result2 = reactiveCommands.zadd("zkey", 1000, "value").block();
            System.out.println(scan3Result2);      // >>> 1

            String scan3Result3 = reactiveCommands.type("geokey").block();
            System.out.println(scan3Result3);      // >>> zset

            String scan3Result4 = reactiveCommands.type("zkey").block();
            System.out.println(scan3Result4);      // >>> zset

            // A single call isn't guaranteed to find every match, so loop until
            // the cursor is finished, accumulating matches from every call.
            List<String> scan3Keys = new java.util.ArrayList<>();
            KeyScanCursor<String> scan3Cursor = reactiveCommands
                    .scan(KeyScanArgs.Builder.type("zset")).block();
            scan3Keys.addAll(scan3Cursor.getKeys());
            while (!scan3Cursor.isFinished()) {
                scan3Cursor = reactiveCommands
                        .scan(scan3Cursor, KeyScanArgs.Builder.type("zset")).block();
                scan3Keys.addAll(scan3Cursor.getKeys());
            }
            Collections.sort(scan3Keys);
            System.out.println(scan3Keys);         // >>> [geokey, zkey]
```

##### Java (Synchronous - Jedis)

```java
        long scan3Result1 = jedis.geoadd("geokey", 0, 0, "value");
        System.out.println(scan3Result1); // >>> 1

        long scan3Result2 = jedis.zadd("zkey", 1000, "value");
        System.out.println(scan3Result2); // >>> 1

        System.out.println(jedis.type("geokey")); // >>> zset
        System.out.println(jedis.type("zkey")); // >>> zset

        // A single call isn't guaranteed to find every match, so loop until the cursor
        // returns to "0", accumulating matches from every call.
        String scan3Cursor = "0";
        ArrayList<String> scan3Keys = new ArrayList<>();
        do {
            ScanResult<String> scan3Result3 = jedis.scan(scan3Cursor, new ScanParams(), "zset");
            scan3Cursor = scan3Result3.getCursor();
            scan3Keys.addAll(scan3Result3.getResult());
        } while (!scan3Cursor.equals("0"));
        Collections.sort(scan3Keys);
        System.out.println(scan3Keys); // >>> [geokey, zkey]
```

##### JavaScript (Node.js)

```javascript
const scan3Res1 = await client.geoAdd('geokey', { longitude: 0, latitude: 0, member: 'value' });
console.log(scan3Res1); // 1

const scan3Res2 = await client.zAdd('zkey', [{ score: 1000, value: 'value' }]);
console.log(scan3Res2); // 1

const scan3Res3 = await client.type('geokey');
console.log(scan3Res3); // zset

const scan3Res4 = await client.type('zkey');
console.log(scan3Res4); // zset

// A single call isn't guaranteed to find every match, so loop until the cursor
// returns to 0, accumulating matches from every call.
let scan3Cursor = '0';
let scan3Keys = [];
do {
    const scan3Res5 = await client.scan(scan3Cursor, { TYPE: 'zset' });
    scan3Cursor = scan3Res5.cursor;
    scan3Keys = scan3Keys.concat(scan3Res5.keys);
} while (scan3Cursor !== '0');
console.log(scan3Keys.sort()); // ['geokey', 'zkey']
```

##### JavaScript (Node.js)

```javascript
const scan3Res1 = await redis.geoadd('geokey', '0', '0', 'value');
console.log(scan3Res1); // >>> 1

const scan3Res2 = await redis.zadd('zkey', '1000', 'value');
console.log(scan3Res2); // >>> 1

console.log(await redis.type('geokey')); // >>> zset
console.log(await redis.type('zkey')); // >>> zset

// A single call isn't guaranteed to find every match, so loop until the cursor
// returns to 0, accumulating matches from every call.
let scan3Cursor = '0';
let scan3Keys = [];
do {
  let scan3Batch;
  [scan3Cursor, scan3Batch] = await redis.scan(scan3Cursor, 'TYPE', 'zset');
  scan3Keys = scan3Keys.concat(scan3Batch);
} while (scan3Cursor !== '0');
console.log(scan3Keys.sort()); // >>> ['geokey', 'zkey']
```

##### JavaScript (Node.js)

```javascript
const scan3Res1 = await client.geoAdd('geokey', { longitude: 0, latitude: 0, member: 'value' });
console.log(scan3Res1); // 1

const scan3Res2 = await client.zAdd('zkey', [{ score: 1000, value: 'value' }]);
console.log(scan3Res2); // 1

const scan3Res3 = await client.type('geokey');
console.log(scan3Res3); // zset

const scan3Res4 = await client.type('zkey');
console.log(scan3Res4); // zset

// A single call isn't guaranteed to find every match, so loop until the cursor
// returns to 0, accumulating matches from every call.
let scan3Cursor = '0';
let scan3Keys = [];
do {
    const scan3Res5 = await client.scan(scan3Cursor, { TYPE: 'zset' });
    scan3Cursor = scan3Res5.cursor;
    scan3Keys = scan3Keys.concat(scan3Res5.keys);
} while (scan3Cursor !== '0');
console.log(scan3Keys.sort()); // ['geokey', 'zkey']
```

##### JavaScript (Node.js)

```javascript
const scan3Res1 = await redis.geoadd('geokey', '0', '0', 'value');
console.log(scan3Res1); // >>> 1

const scan3Res2 = await redis.zadd('zkey', '1000', 'value');
console.log(scan3Res2); // >>> 1

console.log(await redis.type('geokey')); // >>> zset
console.log(await redis.type('zkey')); // >>> zset

// A single call isn't guaranteed to find every match, so loop until the cursor
// returns to 0, accumulating matches from every call.
let scan3Cursor = '0';
let scan3Keys = [];
do {
  let scan3Batch;
  [scan3Cursor, scan3Batch] = await redis.scan(scan3Cursor, 'TYPE', 'zset');
  scan3Keys = scan3Keys.concat(scan3Batch);
} while (scan3Cursor !== '0');
console.log(scan3Keys.sort()); // >>> ['geokey', 'zkey']
```

##### PHP

```php
<?php
use PHPUnit\Framework\TestCase;
use Predis\Client as PredisClient;

class CmdsGenericTest
{
    public function testCmdsGeneric() {
        $r = new PredisClient([
            'scheme'   => 'tcp',
            'host'     => '127.0.0.1',
            'port'     => 6379,
            'password' => '',
            'database' => 0,
        ]);

        $existsResult1 = $r->set('key1', 'Hello');
        echo $existsResult1 . PHP_EOL; // >>> OK

        $existsResult2 = $r->exists('key1');
        echo $existsResult2 . PHP_EOL; // >>> 1

        $existsResult3 = $r->exists('nosuchkey');
        echo $existsResult3 . PHP_EOL; // >>> 0

        $existsResult4 = $r->set('key2', 'World');
        echo $existsResult4 . PHP_EOL; // >>> OK

        $existsResult5 = $r->exists('key1', 'key2', 'nosuchkey');
        echo $existsResult5 . PHP_EOL; // >>> 2

        $keysResult1 = $r->mset(['firstname' => 'Jack', 'lastname' => 'Stuntman', 'age' => '35']);
        echo $keysResult1 . PHP_EOL; // >>> OK

        $keysResult2 = $r->keys('*name*');
        sort($keysResult2);
        echo implode(', ', $keysResult2) . PHP_EOL; // >>> firstname, lastname

        $keysResult3 = $r->keys('a??');
        echo implode(', ', $keysResult3) . PHP_EOL; // >>> age

        $keysResult4 = $r->keys('*');
        sort($keysResult4);
        echo implode(', ', $keysResult4) . PHP_EOL; // >>> age, firstname, lastname

        $scan1Result1 = $r->sadd('myset', ['1', '2', '3', 'foo', 'foobar', 'feelsgood']);
        echo $scan1Result1 . PHP_EOL;                       // >>> 6

        [$scan1Cursor, $scan1Members] = $r->sscan('myset', 0, ['MATCH' => 'f*']);
        sort($scan1Members);
        echo implode(', ', $scan1Members) . PHP_EOL;         // >>> feelsgood, foo, foobar



        // MATCH is applied after elements are fetched, so with the default COUNT most
        // iterations return few keys or none at all.
        $scan2Cursor = 0;
        $scan2Total = 0;

        for ($i = 0; $i < 4; $i++) {
            [$scan2Cursor, $scan2Keys] = $r->scan($scan2Cursor, ['MATCH' => '*11*']);
            $scan2Total += count($scan2Keys);
            echo count($scan2Keys) . PHP_EOL;
        }

        // A larger COUNT forces more scanning in a single iteration, so the remaining
        // matches arrive together. This continues from the cursor reached above.
        [$scan2Cursor, $scan2Keys] = $r->scan($scan2Cursor, ['MATCH' => '*11*', 'COUNT' => 1000]);
        $scan2Total += count($scan2Keys);
        echo count($scan2Keys) . PHP_EOL;

        // The per-call split isn't guaranteed, but the cumulative total is.
        echo $scan2Total . PHP_EOL;                          // >>> 19


        $scan4Result1 = $r->hset('myhash', 'a', 1, 'b', 2);
        echo $scan4Result1 . PHP_EOL;                        // >>> 2

        [$scan4Cursor, $scan4Pairs] = $r->hscan('myhash', 0);
        echo json_encode($scan4Pairs) . PHP_EOL;             // >>> {"a":"1","b":"2"}

        // Redis does not promise a field order, so sort before comparing.
        [$scan4Cursor, $scan4Fields] = $r->hscan('myhash', 0, ['NOVALUES' => true]);
        sort($scan4Fields);
        echo implode(', ', $scan4Fields) . PHP_EOL;          // >>> a, b


        echo $r->set('key1', 'Hello') . PHP_EOL;             // >>> OK
        echo $r->set('key2', 'World') . PHP_EOL;             // >>> OK

        $delResult = $r->del('key1', 'key2', 'key3');
        echo $delResult . PHP_EOL;                           // >>> 2


        echo $r->set('mykey', 'Hello') . PHP_EOL;            // >>> OK

        echo $r->expire('mykey', 10) . PHP_EOL;              // >>> 1
        echo $r->ttl('mykey') . PHP_EOL;                     // >>> 10

        // Overwriting a key with SET clears its expiry.
        echo $r->set('mykey', 'Hello World') . PHP_EOL;      // >>> OK
        echo $r->ttl('mykey') . PHP_EOL;                     // >>> -1

        // XX only sets the expiry when one already exists, so this is a no-op.
        echo $r->expire('mykey', 10, 'XX') . PHP_EOL;        // >>> 0
        echo $r->ttl('mykey') . PHP_EOL;                     // >>> -1

        // NX only sets the expiry when there is none, so this one applies.
        echo $r->expire('mykey', 10, 'NX') . PHP_EOL;        // >>> 1
        $expireTtl = $r->ttl('mykey');
        echo $expireTtl . PHP_EOL;                           // >>> 10


        echo $r->set('mykey', 'Hello') . PHP_EOL;            // >>> OK
        echo $r->expire('mykey', 10) . PHP_EOL;              // >>> 1

        $ttlResult = $r->ttl('mykey');
        echo $ttlResult . PHP_EOL;                           // >>> 10


    }
}

```

##### Python

```python
res = r.geoadd("geokey", (0, 0, "value"))
print(res)
# >>> 1

res = r.zadd("zkey", {"value": 1000})
print(res)
# >>> 1

res = r.type("geokey")
print(res)
# >>> zset

res = r.type("zkey")
print(res)
# >>> zset

# A single call isn't guaranteed to find every match, so loop until the cursor
# returns to 0, accumulating matches from every call.
cursor = 0
scan3_keys = []
while True:
    cursor, keys = r.scan(cursor=cursor, _type="zset")
    scan3_keys.extend(keys)
    if cursor == 0:
        break
print(sorted(scan3_keys))
# >>> ['geokey', 'zkey']
```

##### Rust (Asynchronous)

```rust
        match r.geo_add("geokey", &[(0.0, 0.0, "value")]).await {
            Ok(res) => {
                let res: i32 = res;
                println!("{res}");    // >>> 1
            },
            Err(e) => {
                println!("Error adding geo location: {e}");
                return;
            }
        }

        match r.zadd("zkey", "value", 1000).await {
            Ok(res) => {
                let res: i32 = res;
                println!("{res}");    // >>> 1
            },
            Err(e) => {
                println!("Error adding to sorted set: {e}");
                return;
            }
        }

        match r.key_type::<&str, redis::ValueType>("geokey").await {
            Ok(res) => {
                println!("{res:?}");    // >>> zset
            },
            Err(e) => {
                println!("Error getting key type: {e}");
                return;
            }
        }

        match r.key_type::<&str, redis::ValueType>("zkey").await {
            Ok(res) => {
                println!("{res:?}");    // >>> zset
            },
            Err(e) => {
                println!("Error getting key type: {e}");
                return;
            }
        }

        // Note: Rust redis client doesn't support scan by type directly
        // We'll manually check the types of our known keys
        let mut zset_keys = Vec::new();
        for key in &["geokey", "zkey"] {
            match r.key_type::<&str, redis::ValueType>(key).await {
                Ok(key_type) => {
                    if format!("{key_type:?}") == "ZSet" {
                        zset_keys.push(key.to_string());
                    }
                },
                Err(_) => {},
            }
        }
        println!("{:?}", zset_keys);    // >>> ["zkey", "geokey"]
```

##### Rust (Synchronous)

```rust
        match r.geo_add("geokey", &[(0.0, 0.0, "value")]) {
            Ok(res) => {
                let res: i32 = res;
                println!("{res}");    // >>> 1
            },
            Err(e) => {
                println!("Error adding geo location: {e}");
                return;
            }
        }

        match r.zadd("zkey", "value", 1000) {
            Ok(res) => {
                let res: i32 = res;
                println!("{res}");    // >>> 1
            },
            Err(e) => {
                println!("Error adding to sorted set: {e}");
                return;
            }
        }

        match r.key_type::<&str, redis::ValueType>("geokey") {
            Ok(res) => {
                println!("{res:?}");    // >>> zset
            },
            Err(e) => {
                println!("Error getting key type: {e}");
                return;
            }
        }

        match r.key_type::<&str, redis::ValueType>("zkey") {
            Ok(res) => {
                println!("{res:?}");    // >>> zset
            },
            Err(e) => {
                println!("Error getting key type: {e}");
                return;
            }
        }

        // Note: Rust redis client doesn't support scan by type directly
        // We'll manually check the types of our known keys
        let mut zset_keys = Vec::new();
        for key in &["geokey", "zkey"] {
            match r.key_type::<&str, redis::ValueType>(key) {
                Ok(key_type) => {
                    if format!("{key_type:?}") == "ZSet" {
                        zset_keys.push(key.to_string());
                    }
                },
                Err(_) => {},
            }
        }
        println!("{:?}", zset_keys);    // >>> ["zkey", "geokey"]
```



It is important to note that the **TYPE** filter is also applied after elements are retrieved from the database, so the option does not reduce the amount of work the server has to do to complete a full iteration, and for rare types you may receive no elements in many iterations.

### The NOVALUES option

When using [`HSCAN`](https://redis.io/docs/latest/commands/hscan), you can use the `NOVALUES` option to make Redis return only the keys in the hash table without their corresponding values.

Hash iteration: Iterate hash fields with optional NOVALUES using HSCAN (returns field-value pairs or fields only)

**Difficulty:** Intermediate

**Commands:** HSET, HSCAN

**Complexity:**
- HSET: O(1)
- HSCAN: O(1)

**Available in:** Redis CLI, C, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), JavaScript (Node.js), PHP, Python, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> HSET myhash a 1 b 2
OK
> HSCAN myhash 0
1) "0"
2) 1) "a"
   2) "1"
   3) "b"
   4) "2"
> HSCAN myhash 0 NOVALUES
1) "0"
2) 1) "a"
   2) "b"
```

##### C

```c
    reply = redisCommand(c, "HSET myhash a 1 b 2");
    printf("%lld\n", reply->integer);
    // >>> 2
    freeReplyObject(reply);

    // Without NOVALUES the results alternate field, value, field, value.
    reply = redisCommand(c, "HSCAN myhash 0");
    for (size_t i = 0; i < reply->element[1]->elements; i += 2) {
        printf("%s=%s\n", reply->element[1]->element[i]->str,
                           reply->element[1]->element[i + 1]->str);
    }
    // >>> a=1
    // >>> b=2
    freeReplyObject(reply);

    reply = redisCommand(c, "HSCAN myhash 0 NOVALUES");
    for (size_t i = 0; i < reply->element[1]->elements; i++) {
        printf("%s\n", reply->element[1]->element[i]->str);
    }
    // >>> a
    // >>> b
    freeReplyObject(reply);
```

##### C#

```csharp

```

##### Go

```go
	scan4Result1, err := rdb.HSet(ctx, "myhash", "a", 1, "b", 2).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(scan4Result1) // >>> 2

	scan4Result2, _, err := rdb.HScan(ctx, "myhash", 0, "", 0).Result()

	if err != nil {
		panic(err)
	}

	// HSCAN returns field and value interleaved. Redis does not promise an order, so
	// collect the pairs into a map: fmt prints map keys sorted, whatever order they arrived in.
	scan4Fields := map[string]string{}

	for i := 0; i < len(scan4Result2); i += 2 {
		scan4Fields[scan4Result2[i]] = scan4Result2[i+1]
	}

	fmt.Println(scan4Fields) // >>> map[a:1 b:2]

	scan4Result3, _, err := rdb.HScanNoValues(ctx, "myhash", 0, "", 0).Result()

	if err != nil {
		panic(err)
	}

	sort.Strings(scan4Result3)
	fmt.Println(scan4Result3) // >>> [a b]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> scan4Example = asyncCommands
                    .hset("myhash", Map.of("a", "1", "b", "2"))
                    .thenCompose(scan4Res1 -> {
                        System.out.println(scan4Res1);      // >>> 2
                        return asyncCommands.hscan("myhash");
                    })
                    .thenCompose(scan4Res2 -> {
                        System.out.println(new java.util.TreeMap<>(scan4Res2.getMap()));
                        // >>> {a=1, b=2}
                        return asyncCommands.hscanNovalues("myhash");
                    })
                    .thenAccept(scan4Res3 -> {
                        List<String> fields = new java.util.ArrayList<>(scan4Res3.getKeys());
                        Collections.sort(fields);
                        System.out.println(fields);         // >>> [a, b]
                    })
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> scan4Example = reactiveCommands
                    .hset("myhash", Map.of("a", "1", "b", "2"))
                    .flatMap(scan4Res1 -> {
                        System.out.println(scan4Res1);      // >>> 2
                        return reactiveCommands.hscan("myhash");
                    })
                    .flatMap(scan4Res2 -> {
                        System.out.println(new java.util.TreeMap<>(scan4Res2.getMap()));
                        // >>> {a=1, b=2}
                        return reactiveCommands.hscanNovalues("myhash");
                    })
                    .doOnNext(scan4Res3 -> {
                        List<String> fields = new java.util.ArrayList<>(scan4Res3.getKeys());
                        Collections.sort(fields);
                        System.out.println(fields);         // >>> [a, b]
                    })
                    .then();
```

##### Java (Synchronous - Jedis)

```java
        long scan4Result1 = jedis.hset("myhash", Map.of("a", "1", "b", "2"));
        System.out.println(scan4Result1); // >>> 2

        ScanResult<Map.Entry<String, String>> scan4Result2 = jedis.hscan(
                "myhash", "0", new ScanParams()
        );
        ArrayList<String> scan4Pairs = new ArrayList<>();
        for (Map.Entry<String, String> entry : scan4Result2.getResult()) {
            scan4Pairs.add(entry.getKey() + "=" + entry.getValue());
        }
        Collections.sort(scan4Pairs);
        System.out.println(scan4Pairs); // >>> [a=1, b=2]

        ScanResult<String> scan4Result3 = jedis.hscanNoValues(
                "myhash", "0", new ScanParams()
        );
        ArrayList<String> scan4Fields = new ArrayList<>(scan4Result3.getResult());
        Collections.sort(scan4Fields);
        System.out.println(scan4Fields); // >>> [a, b]
```

##### JavaScript (Node.js)

```javascript
const scan4Res1 = await client.hSet('myhash', { a: 1, b: 2 });
console.log(scan4Res1); // 2

// HSCAN doesn't promise a field order, so pair entries into an object rather than
// relying on position.
const scan4Res2 = await client.hScan('myhash', '0');
const scan4Pairs = Object.fromEntries(scan4Res2.entries.map((e) => [e.field, e.value]));
console.log(scan4Pairs); // {a: '1', b: '2'}

const scan4Res3 = await client.hScan('myhash', '0', { COUNT: 10 });
const items = scan4Res3.entries.map((item) => item.field).sort()
console.log(items); // ['a', 'b']
```

##### JavaScript (Node.js)

```javascript
const scan4Res1 = await redis.hset('myhash', { a: 1, b: 2 });
console.log(scan4Res1); // >>> 2

// HSCAN returns field and value interleaved. Redis does not promise an order, so pair
// them up into an object rather than relying on the position of each element.
const [, scan4Flat] = await redis.hscan('myhash', 0);
const scan4Pairs = Object.fromEntries(
  scan4Flat.reduce((acc, v, i) => (i % 2 ? acc : [...acc, [v, scan4Flat[i + 1]]]), [])
);
console.log(scan4Pairs); // >>> { a: '1', b: '2' }

const [, scan4Fields] = await redis.hscan('myhash', 0, 'NOVALUES');
console.log(scan4Fields.sort()); // >>> [ 'a', 'b' ]
```

##### JavaScript (Node.js)

```javascript
const scan4Res1 = await client.hSet('myhash', { a: 1, b: 2 });
console.log(scan4Res1); // 2

// HSCAN doesn't promise a field order, so pair entries into an object rather than
// relying on position.
const scan4Res2 = await client.hScan('myhash', '0');
const scan4Pairs = Object.fromEntries(scan4Res2.entries.map((e) => [e.field, e.value]));
console.log(scan4Pairs); // {a: '1', b: '2'}

const scan4Res3 = await client.hScan('myhash', '0', { COUNT: 10 });
const items = scan4Res3.entries.map((item) => item.field).sort()
console.log(items); // ['a', 'b']
```

##### JavaScript (Node.js)

```javascript
const scan4Res1 = await redis.hset('myhash', { a: 1, b: 2 });
console.log(scan4Res1); // >>> 2

// HSCAN returns field and value interleaved. Redis does not promise an order, so pair
// them up into an object rather than relying on the position of each element.
const [, scan4Flat] = await redis.hscan('myhash', 0);
const scan4Pairs = Object.fromEntries(
  scan4Flat.reduce((acc, v, i) => (i % 2 ? acc : [...acc, [v, scan4Flat[i + 1]]]), [])
);
console.log(scan4Pairs); // >>> { a: '1', b: '2' }

const [, scan4Fields] = await redis.hscan('myhash', 0, 'NOVALUES');
console.log(scan4Fields.sort()); // >>> [ 'a', 'b' ]
```

##### PHP

```php
        $scan4Result1 = $r->hset('myhash', 'a', 1, 'b', 2);
        echo $scan4Result1 . PHP_EOL;                        // >>> 2

        [$scan4Cursor, $scan4Pairs] = $r->hscan('myhash', 0);
        echo json_encode($scan4Pairs) . PHP_EOL;             // >>> {"a":"1","b":"2"}

        // Redis does not promise a field order, so sort before comparing.
        [$scan4Cursor, $scan4Fields] = $r->hscan('myhash', 0, ['NOVALUES' => true]);
        sort($scan4Fields);
        echo implode(', ', $scan4Fields) . PHP_EOL;          // >>> a, b
```

##### Python

```python
res = r.hset("myhash", mapping={"a": 1, "b": 2})
print(res)
# >>> 2

cursor, keys = r.hscan("myhash", 0)
print(keys)
# >>> {'a': '1', 'b': '2'}

cursor, keys = r.hscan("myhash", 0, no_values=True)
print(sorted(keys))
# >>> ['a', 'b']

```

##### Rust (Asynchronous)

```rust
        match r.hset("myhash", "a", "1").await {
            Ok(res) => {
                let res: i32 = res;
                println!("{res}");    // >>> 1
            },
            Err(e) => {
                println!("Error setting hash field: {e}");
                return;
            }
        }

        match r.hset("myhash", "b", "2").await {
            Ok(res) => {
                let res: i32 = res;
                println!("{res}");    // >>> 1
            },
            Err(e) => {
                println!("Error setting hash fields: {e}");
                return;
            }
        }

        let fields = match r.hscan("myhash").await {
            Ok(iter) => {
                let items: Vec<Result<(String, String), _>> = iter.collect().await;
                items.into_iter().filter_map(|r| r.ok()).collect::<std::collections::HashMap<String, String>>()
            },
            Err(e) => {
                println!("Error scanning hash: {e}");
                return;
            }
        };

        println!("{fields:?}");    // >>> {"a": "1", "b": "2"}

        // Scan hash keys only (no values)
        match r.hkeys("myhash").await {
            Ok(keys) => {
                let keys: Vec<String> = keys;
                println!("{keys:?}");    // >>> ["a", "b"]
            },
            Err(e) => {
                println!("Error getting hash keys: {e}");
                return;
            }
        }
```

##### Rust (Synchronous)

```rust
        match r.hset("myhash", "a", "1") {
            Ok(res) => {
                let res: i32 = res;
                println!("{res}");    // >>> 1
            },
            Err(e) => {
                println!("Error setting hash field: {e}");
                return;
            }
        }

        match r.hset("myhash", "b", "2") {
            Ok(res) => {
                let res: i32 = res;
                println!("{res}");    // >>> 1
            },
            Err(e) => {
                println!("Error setting hash fields: {e}");
                return;
            }
        }

        match r.hscan("myhash") {
            Ok(iter) => {
                let fields: std::collections::HashMap<String, String> = iter.filter_map(|r| r.ok()).collect();
                println!("{fields:?}");    // >>> {"a": "1", "b": "2"}
            },
            Err(e) => {
                println!("Error scanning hash: {e}");
                return;
            }
        }

        // Scan hash keys only (no values)
        match r.hkeys("myhash") {
            Ok(keys) => {
                let keys: Vec<String> = keys;
                println!("{keys:?}");    // >>> ["a", "b"]
            },
            Err(e) => {
                println!("Error getting hash keys: {e}");
                return;
            }
        }
```



### Multiple parallel iterations

It is possible for an infinite number of clients to iterate the same collection at the same time, as the full state of the iterator is in the cursor, that is obtained and returned to the client at every call. No server side state is taken at all.

### Terminating iterations in the middle

Since there is no state server side, but the full state is captured by the cursor, the caller is free to terminate an iteration half-way without signaling this to the server in any way. An infinite number of iterations can be started and never terminated without any issue.

### Calling SCAN with a corrupted cursor

Calling `SCAN` with a broken, negative, out of range, or otherwise invalid cursor, will result in undefined behavior but never in a crash. What will be undefined is that the guarantees about the returned elements can no longer be ensured by the `SCAN` implementation.

The only valid cursors to use are:

* The cursor value of 0 when starting an iteration.
* The cursor returned by the previous call to SCAN in order to continue the iteration.

### Guarantee of termination

The `SCAN` algorithm is guaranteed to terminate only if the size of the iterated collection remains bounded to a given maximum size, otherwise iterating a collection that always grows may result into `SCAN` to never terminate a full iteration.

This is easy to see intuitively: if the collection grows there is more and more work to do in order to visit all the possible elements, and the ability to terminate the iteration depends on the number of calls to `SCAN` and its COUNT option value compared with the rate at which the collection grows.

### Why SCAN may return all the items of an aggregate data type in a single call?

In the `COUNT` option documentation, we state that sometimes this family of commands may return all the elements of a Set, Hash or Sorted Set at once in a single call, regardless of the `COUNT` option value. The reason why this happens is that the cursor-based iterator can be implemented, and is useful, only when the aggregate data type that we are scanning is represented as a hash table. However Redis uses a [memory optimization](https://redis.io/docs/latest/operate/oss_and_stack/management/optimization/memory-optimization) where small aggregate data types, until they reach a given amount of items or a given max size of single elements, are represented using a compact single-allocation packed encoding. When this is the case, `SCAN` has no meaningful cursor to return, and must iterate the whole data structure at once, so the only sane behavior it has is to return everything in a call.

However once the data structures are bigger and are promoted to use real hash tables, the `SCAN` family of commands will resort to the normal behavior. Note that since this special behavior of returning all the elements is true only for small aggregates, it has no effects on the command complexity or latency. However the exact limits to get converted into real hash tables are [user configurable](https://redis.io/docs/latest/operate/oss_and_stack/management/optimization/memory-optimization), so the maximum number of elements you can see returned in a single call depends on how big an aggregate data type could be and still use the packed representation.

Also note that this behavior is specific of [`SSCAN`](https://redis.io/docs/latest/commands/sscan), [`HSCAN`](https://redis.io/docs/latest/commands/hscan) and [`ZSCAN`](https://redis.io/docs/latest/commands/zscan). `SCAN` itself never shows this behavior because the key space is always represented by hash tables.

### Further reading

For more information about managing keys, please refer to the [The Redis Keyspace](https://redis.io/docs/latest/develop/using-commands/keyspace) tutorial.

### Additional examples

Give the following commands, showing iteration of a hash key, a try in the interactive console:


redis> HMSET hash name Jack age 33
OK
redis> HSCAN hash 0
1) "0"
2) 1) "name"
   2) "Jack"
   3) "age"
   4) "33"


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Array reply](../../develop/reference/protocol-spec#arrays): specifically, an array with two elements.
* The first element is a [Bulk string reply](../../develop/reference/protocol-spec#bulk-strings) that represents an unsigned 64-bit number, the cursor.
* The second element is an [Array reply](../../develop/reference/protocol-spec#arrays) with the names of scanned keys.

**RESP3:**

[Array reply](../../develop/reference/protocol-spec#arrays): specifically, an array with two elements.
* The first element is a [Bulk string reply](../../develop/reference/protocol-spec#bulk-strings) that represents an unsigned 64-bit number, the cursor.
* The second element is an [Array reply](../../develop/reference/protocol-spec#arrays) with the names of scanned keys.



