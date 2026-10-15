# RPOP

```json metadata
{
  "schema_version": 2,
  "title": "RPOP",
  "description": "Returns and removes the last elements of a list. Deletes the list if the last element was popped.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"},{"display_text":"count","name":"count","optional":true,"since":"6.2.0","type":"integer"}],
  "syntax_fmt": "RPOP key [count]",
  "complexity": "O(N) where N is the number of elements returned",
  "group": "list",
  "command_flags": ["write","fast"],
  "acl_categories": ["@write","@list","@fast"],
  "since": "1.0.0",
  "arity": -2,
  "key_specs": [{"RW":true,"access":true,"begin_search":{"spec":{"index":1},"type":"index"},"delete":true,"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": [{"codetabsId":"cmds_list-steprpop","commands":[{"acl_categories":["@write","@list","@fast"],"complexity":"O(1)","name":"RPUSH"},{"acl_categories":["@write","@list","@fast"],"complexity":"O(N)","name":"RPOP"},{"acl_categories":["@read","@list","@slow"],"complexity":"O(S+N)","name":"LRANGE"}],"description":"Foundational: Remove and return the last element(s) from a list using RPOP (supports optional count parameter to pop multiple elements from tail)","difficulty":"beginner","id":"rpop","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_cmds_list-steprpop"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_cmds_list-steprpop"},{"id":"Node-js","panelId":"panel_Nodejs_cmds_list-steprpop"},{"clientId":"ioredis","clientName":"ioredis","id":"ioredis","langId":"javascript","panelId":"panel_ioredis_cmds_list-steprpop"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_cmds_list-steprpop"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_cmds_list-steprpop"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_cmds_list-steprpop"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_cmds_list-steprpop"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_cmds_list-steprpop"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_cmds_list-steprpop"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_cmds_list-steprpop"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_cmds_list-steprpop"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_cmds_list-steprpop"}]}]
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

Removes and returns the last elements of the list stored at `key`.

By default, the command pops a single element from the end of the list.
When provided with the optional `count` argument, the reply will consist of up
to `count` elements, depending on the list's length.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key that holds the list.

</details>

## Optional arguments

<details open><summary><code>count</code></summary>

The number of elements to pop. Without it, a single element is popped.

</details>

## Examples

Foundational: Remove and return the last element(s) from a list using RPOP (supports optional count parameter to pop multiple elements from tail)

**Difficulty:** Beginner

**Commands:** RPUSH, RPOP, LRANGE

**Complexity:**
- RPUSH: O(1)
- RPOP: O(N)
- LRANGE: O(S+N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
redis> RPUSH mylist "one" "two" "three" "four" "five"
(integer) 5
redis> RPOP mylist
"five"
redis> RPOP mylist 2
1) "four"
2) "three"
redis> LRANGE mylist 0 -1
1) "one"
2) "two"
```

##### C#

```csharp
        long rPopResult1 = db.ListRightPush("mylist", ["one", "two", "three", "four", "five"]);
        Console.WriteLine(rPopResult1); // >>> 5

        RedisValue rPopResult2 = db.ListRightPop("mylist");
        Console.WriteLine(rPopResult2); // >>> five

        RedisValue[] rPopResult3 = db.ListRightPop("mylist", 2);
        Console.WriteLine($"[{string.Join(", ", rPopResult3)}]");
        // >>> [four, three]

        RedisValue[] rPopResult4 = db.ListRange("mylist", 0, -1);
        Console.WriteLine($"[{string.Join(", ", rPopResult4)}]");
        // >>> [one, two]
```

##### Go

```go
	rPushResult, err := rdb.RPush(ctx, "mylist",
		"one", "two", "three", "four", "five",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(rPushResult) // >>> 5

	rPopResult, err := rdb.RPop(ctx, "mylist").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(rPopResult) // >>> five

	rPopCountResult, err := rdb.RPopCount(ctx, "mylist", 2).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(rPopCountResult) // >>> [four three]

	lRangeResult, err := rdb.LRange(ctx, "mylist", 0, -1).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(lRangeResult) // >>> [one two]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> rpop = asyncCommands.rpush("mylist", "one", "two", "three", "four", "five")
                    .thenCompose(res18 -> {
                        System.out.println(res18); // >>> 5

                        return asyncCommands.rpop("mylist");
                    }).thenCompose(res19 -> {
                        System.out.println(res19); // >>> five

                        return asyncCommands.rpop("mylist", 2);
                    }).thenCompose(res20 -> {
                        System.out.println(res20); // >>> [four, three]

                        return asyncCommands.lrange("mylist", 0, -1);
                    })
                    .thenAccept(res21 -> System.out.println(res21)) // >>> [one, two]
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> rpop = reactiveCommands.rpush("mylist", "one", "two", "three", "four", "five").doOnNext(res18 -> {
                System.out.println(res18); // >>> 5
            }).flatMap(res18 -> reactiveCommands.rpop("mylist")).doOnNext(res19 -> {
                System.out.println(res19); // >>> five
            }).flatMap(res19 -> reactiveCommands.rpop("mylist", 2).collectList()).doOnNext(res20 -> {
                System.out.println(res20); // >>> [four, three]
            }).flatMap(res20 -> reactiveCommands.lrange("mylist", 0, -1).collectList()).doOnNext(res21 -> {
                System.out.println(res21); // >>> [one, two]
            }).then();
```

##### Java (Synchronous - Jedis)

```java
        long rPopResult1 = jedis.rpush(
            "mylist", "one", "two", "three", "four", "five"
        );
        System.out.println(rPopResult1); // >>> 5

        String rPopResult2 = jedis.rpop("mylist");
        System.out.println(rPopResult2); // >>> five

        List<String> rPopResult3 = jedis.rpop("mylist", 2);
        System.out.println(rPopResult3); // >>> [four, three]

        List<String> rPopResult4 = jedis.lrange("mylist", 0, -1);
        System.out.println(rPopResult4); // >>> [one, two]
```

##### JavaScript (Node.js)

```javascript
const res21 = await client.rPush('mylist', ["one", "two", "three", "four", "five"]);
console.log(res21); // 5

const res22 = await client.rPop('mylist');
console.log(res22); // 'five'

const res23 = await client.rPopCount('mylist', 2);
console.log(res23); // [ 'four', 'three' ]

const res24 = await client.lRange('mylist', 0, -1);
console.log(res24); // [ 'one', 'two' ]

```

##### JavaScript (Node.js)

```javascript
const res21 = await redis.rpush('mylist', 'one', 'two', 'three', 'four', 'five');
console.log(res21); // >>> 5

const res22 = await redis.rpop('mylist');
console.log(res22); // >>> five

const res23 = await redis.rpop('mylist', 2);
console.log(res23); // >>> ['four', 'three']

const res24 = await redis.lrange('mylist', 0, -1);
console.log(res24); // >>> ['one', 'two']
```

##### JavaScript (Node.js)

```javascript
const res21 = await client.rPush('mylist', ["one", "two", "three", "four", "five"]);
console.log(res21); // 5

const res22 = await client.rPop('mylist');
console.log(res22); // 'five'

const res23 = await client.rPopCount('mylist', 2);
console.log(res23); // [ 'four', 'three' ]

const res24 = await client.lRange('mylist', 0, -1);
console.log(res24); // [ 'one', 'two' ]

```

##### JavaScript (Node.js)

```javascript
const res21 = await redis.rpush('mylist', 'one', 'two', 'three', 'four', 'five');
console.log(res21); // >>> 5

const res22 = await redis.rpop('mylist');
console.log(res22); // >>> five

const res23 = await redis.rpop('mylist', 2);
console.log(res23); // >>> ['four', 'three']

const res24 = await redis.lrange('mylist', 0, -1);
console.log(res24); // >>> ['one', 'two']
```

##### PHP

```php
        $res21 = $r->rpush('mylist', 'one', 'two', 'three', 'four', 'five');
        echo $res21 . PHP_EOL;
        // >>> 5

        $res22 = $r->rpop('mylist');
        echo $res22 . PHP_EOL;
        // >>> five

        $res23 = $r->rpop('mylist', 2);
        echo json_encode($res23) . PHP_EOL;
        // >>> ["four","three"]

        $res24 = $r->lrange('mylist', 0, -1);
        echo json_encode($res24) . PHP_EOL;
        // >>> ["one","two"]
```

##### Python

```python
res18 = r.rpush("mylist", *["one", "two", "three", "four", "five"])
print(res18) # >>> 5

res19 = r.rpop("mylist")
print(res19) # >>> "five"

res20 = r.rpop("mylist", 2)
print(res20) # >>> ['four', 'three']

res21 = r.lrange("mylist", 0, -1)
print(res21)  # >>> [ "one", "two" ]

```

##### Ruby

```ruby
res21 = r.rpush('mylist', ['one', 'two', 'three', 'four', 'five'])
puts res21 # >>> 5

res22 = r.rpop('mylist')
puts res22 # >>> five

res23 = r.rpop('mylist', 2)
puts res23.inspect # >>> ["four", "three"]

res24 = r.lrange('mylist', 0, -1)
puts res24.inspect # >>> ["one", "two"]
```

##### Rust (Asynchronous)

```rust
        if let Ok(res21) = r.rpush("mylist", &["one", "two", "three", "four", "five"]).await {
            let res21: i32 = res21;
            println!("{res21}"); // >>> 5
        }

        if let Ok(res22) = r.rpop("mylist", None).await {
            let res22: String = res22;
            println!("{res22}"); // >>> five
        }

        if let Ok(res23) = r.rpop("mylist", NonZeroUsize::new(2)).await {
            let res23: Vec<String> = res23;
            println!("{res23:?}"); // >>> ["four", "three"]
        }

        if let Ok(res24) = r.lrange("mylist", 0, -1).await {
            let res24: Vec<String> = res24;
            println!("{res24:?}"); // >>> ["one", "two"]
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res21) = r.rpush("mylist", &["one", "two", "three", "four", "five"]) {
            let res21: i32 = res21;
            println!("{res21}"); // >>> 5
        }

        if let Ok(res22) = r.rpop("mylist", None) {
            let res22: String = res22;
            println!("{res22}"); // >>> five
        }

        if let Ok(res23) = r.rpop("mylist", NonZeroUsize::new(2)) {
            let res23: Vec<String> = res23;
            println!("{res23:?}"); // >>> ["four", "three"]
        }

        if let Ok(res24) = r.lrange("mylist", 0, -1) {
            let res24: Vec<String> = res24;
            println!("{res24:?}"); // >>> ["one", "two"]
        }
```



## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Nil reply](../../develop/reference/protocol-spec#bulk-strings): if the key does not exist.
* [Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): when called without the _count_ argument, the value of the last element.
* [Array reply](../../develop/reference/protocol-spec#arrays): when called with the _count_ argument, a list of popped elements.

**RESP3:**

One of the following:
* [Null reply](../../develop/reference/protocol-spec#nulls): if the key does not exist.
* [Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): when called without the _count_ argument, the value of the last element.
* [Array reply](../../develop/reference/protocol-spec#arrays): when called with the _count_ argument, a list of popped elements.



