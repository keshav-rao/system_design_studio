# KEYS

```json metadata
{
  "schema_version": 2,
  "title": "KEYS",
  "description": "Returns all key names that match a pattern.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"pattern","name":"pattern","type":"pattern"}],
  "syntax_fmt": "KEYS pattern",
  "complexity": "O(N) with N being the number of keys in the database, under the assumption that the key names in the database and the given pattern have limited length.",
  "group": "generic",
  "command_flags": ["readonly"],
  "acl_categories": ["@keyspace","@read","@slow","@dangerous"],
  "since": "1.0.0",
  "arity": 2,
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"details","title":"Details"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": [{"codetabsId":"cmds_generic-stepkeys","commands":[{"acl_categories":["@write","@string","@slow"],"complexity":"O(N)","name":"MSET"},{"acl_categories":["@keyspace","@read","@slow","@dangerous"],"complexity":"O(N)","name":"KEYS"}],"description":"Returns all key names that match a pattern","difficulty":"beginner","id":"keys","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_cmds_generic-stepkeys"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_cmds_generic-stepkeys"},{"id":"Node-js","panelId":"panel_Nodejs_cmds_generic-stepkeys"},{"clientId":"ioredis","clientName":"ioredis","id":"ioredis","langId":"javascript","panelId":"panel_ioredis_cmds_generic-stepkeys"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_cmds_generic-stepkeys"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_cmds_generic-stepkeys"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_cmds_generic-stepkeys"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_cmds_generic-stepkeys"},{"clientId":"hiredis","clientName":"hiredis","id":"C","langId":"c","panelId":"panel_C_cmds_generic-stepkeys"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_cmds_generic-stepkeys"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_cmds_generic-stepkeys"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_cmds_generic-stepkeys"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_cmds_generic-stepkeys"}]}]
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


Returns all keys matching `pattern`.



## Required arguments

<details open><summary><code>pattern</code></summary>

The glob-style pattern to match key names against.

</details>

## Details

While the time complexity for this operation is O(N), the constant times are
fairly low.
For example, Redis running on an entry level laptop can scan a 1 million key
database in 40 milliseconds.

> [!WARNING]
> Use extreme care when using this command in production environments.
> It may ruin performance when it is executed against large databases.
> This command is intended for debugging and special operations, such as changing
> your keyspace layout.
> Don't use `KEYS` in your regular application code.
> If you're looking for a way to find keys in a subset of your keyspace, consider
> using [`SCAN`](https://redis.io/docs/latest/commands/scan) or [sets](https://redis.io/docs/latest/develop/data-types/sets).

Supported glob-style patterns:

* `h?llo` matches `hello`, `hallo` and `hxllo`
* `h*llo` matches `hllo` and `heeeello`
* `h[ae]llo` matches `hello` and `hallo,` but not `hillo`
* `h[^e]llo` matches `hallo`, `hbllo`, ... but not `hello`
* `h[a-b]llo` matches `hallo` and `hbllo`

Use `\` to escape special characters if you want to match them verbatim.

When using [Redis Cluster](https://redis.io/docs/latest/operate/oss_and_stack/management/scaling), the search is optimized for patterns that imply a single slot.
If a pattern can only match keys of one slot,
Redis only iterates over keys in that slot, rather than the whole database,
when searching for keys matching the pattern.
For example, with the pattern `{a}h*llo`, Redis would only try to match it with the keys in slot 15495, which hash tag `{a}` implies.
To use pattern with a hash tag, see [Hash tags](https://redis.io/docs/latest/operate/oss_and_stack/reference/cluster-spec#hash-tags) in the Cluster specification for more information.

## Examples

Returns all key names that match a pattern

**Difficulty:** Beginner

**Commands:** MSET, KEYS

**Complexity:**
- MSET: O(N)
- KEYS: O(N)

**Available in:** Redis CLI, C, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), JavaScript (Node.js), PHP, Python, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> MSET firstname Jack lastname Stuntman age 35
OK
> KEYS *name*
1) "lastname"
2) "firstname"
> KEYS a??
1) "age"
> KEYS *
1) "age"
2) "lastname"
3) "firstname"
```

##### C

```c
    redisReply *reply;

    // Set up keys
    reply = redisCommand(c, "MSET %s %s %s %s %s %s",
        "firstname", "Jack", "lastname", "Stuntman", "age", "35");
    printf("MSET firstname Jack lastname Stuntman age 35: %s\n", reply->str);
    // >>> OK
    freeReplyObject(reply);

    // Keys matching *name*
    reply = redisCommand(c, "KEYS %s", "*name*");
    printf("KEYS *name*:\n");
    for (size_t i = 0; i < reply->elements; i++) {
        printf("  %s\n", reply->element[i]->str);
    }
    // >>> firstname
    // >>> lastname
    freeReplyObject(reply);

    // Keys matching a??
    reply = redisCommand(c, "KEYS %s", "a??");
    printf("KEYS a??:\n");
    for (size_t i = 0; i < reply->elements; i++) {
        printf("  %s\n", reply->element[i]->str);
    }
    // >>> age
    freeReplyObject(reply);

    // All keys
    reply = redisCommand(c, "KEYS %s", "*");
    printf("KEYS *:\n");
    for (size_t i = 0; i < reply->elements; i++) {
        printf("  %s\n", reply->element[i]->str);
    }
    // >>> age
    // >>> firstname
    // >>> lastname
    freeReplyObject(reply);
```

##### C#

```csharp
        bool keysResult1 = db.StringSet(
            new KeyValuePair<RedisKey, RedisValue>[] {
                new("firstname", "Jack"),
                new("lastname", "Stuntman"),
                new("age", "35")
            }
        );
        Console.WriteLine(keysResult1);  // >>> True

        IServer server = muxer.GetServer("localhost:6379");

        RedisKey[] keysResult2 = server.Keys(pattern: "*name*").ToArray();
        Array.Sort(keysResult2, (a, b) => a.ToString().CompareTo(b.ToString()));
        Console.WriteLine(string.Join(", ", keysResult2.Select(k => k.ToString())));  // >>> firstname, lastname

        RedisKey[] keysResult3 = server.Keys(pattern: "a??").ToArray();
        Console.WriteLine(string.Join(", ", keysResult3.Select(k => k.ToString())));  // >>> age

        RedisKey[] keysResult4 = server.Keys(pattern: "*").ToArray();
        Array.Sort(keysResult4, (a, b) => a.ToString().CompareTo(b.ToString()));
        Console.WriteLine(string.Join(", ", keysResult4.Select(k => k.ToString())));  // >>> age, firstname, lastname
```

##### Go

```go
	keysResult1, err := rdb.MSet(ctx, "firstname", "Jack", "lastname", "Stuntman", "age", "35").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(keysResult1) // >>> OK

	keysResult2, err := rdb.Keys(ctx, "*name*").Result()

	if err != nil {
		panic(err)
	}

	sort.Strings(keysResult2)
	fmt.Println(keysResult2) // >>> [firstname lastname]

	keysResult3, err := rdb.Keys(ctx, "a??").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(keysResult3) // >>> [age]

	keysResult4, err := rdb.Keys(ctx, "*").Result()

	if err != nil {
		panic(err)
	}

	sort.Strings(keysResult4)
	fmt.Println(keysResult4) // >>> [age firstname lastname]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> keysExample = asyncCommands.mset(Map.of(
                    "firstname", "Jack",
                    "lastname", "Stuntman",
                    "age", "35"
            )).thenCompose(res1 -> {
                System.out.println(res1); // >>> OK

                return asyncCommands.keys("*name*");
            }).thenCompose(res2 -> {
                Collections.sort(res2);
                System.out.println(res2); // >>> [firstname, lastname]

                return asyncCommands.keys("a??");
            }).thenCompose(res3 -> {
                System.out.println(res3); // >>> [age]

                return asyncCommands.keys("*");
            }).thenAccept(res4 -> {
                Collections.sort(res4);
                System.out.println(res4); // >>> [age, firstname, lastname]
            }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> keysExample = reactiveCommands.mset(Map.of(
                    "firstname", "Jack",
                    "lastname", "Stuntman",
                    "age", "35"
            )).doOnNext(res1 -> {
                System.out.println(res1); // >>> OK
            }).then(reactiveCommands.keys("*name*").collectList()).doOnNext(res2 -> {
                Collections.sort(res2);
                System.out.println(res2); // >>> [firstname, lastname]
            }).then(reactiveCommands.keys("a??").collectList()).doOnNext(res3 -> {
                System.out.println(res3); // >>> [age]
            }).then(reactiveCommands.keys("*").collectList()).doOnNext(res4 -> {
                Collections.sort(res4);
                System.out.println(res4); // >>> [age, firstname, lastname]
            }).then();
```

##### Java (Synchronous - Jedis)

```java
        String keysResult1 = jedis.mset("firstname", "Jack", "lastname", "Stuntman", "age", "35");
        System.out.println(keysResult1); // >>> OK

        Set<String> keysResult2 = jedis.keys("*name*");
        ArrayList<String> keysResult2List = new ArrayList<>(keysResult2);
        Collections.sort(keysResult2List);
        System.out.println(keysResult2List); // >>> [firstname, lastname]

        Set<String> keysResult3 = jedis.keys("a??");
        System.out.println(keysResult3); // >>> [age]

        Set<String> keysResult4 = jedis.keys("*");
        ArrayList<String> keysResult4List = new ArrayList<>(keysResult4);
        Collections.sort(keysResult4List);
        System.out.println(keysResult4List); // >>> [age, firstname, lastname]
```

##### JavaScript (Node.js)

```javascript
const keysRes1 = await client.mSet({ firstname: 'Jack', lastname: 'Stuntman', age: '35' });
console.log(keysRes1); // OK

const keysRes2 = await client.keys('*name*');
console.log(keysRes2.sort()); // ['firstname', 'lastname']

const keysRes3 = await client.keys('a??');
console.log(keysRes3); // ['age']

const keysRes4 = await client.keys('*');
console.log(keysRes4.sort()); // ['age', 'firstname', 'lastname']
```

##### JavaScript (Node.js)

```javascript
const keysRes1 = await redis.mset({ firstname: 'Jack', lastname: 'Stuntman', age: '35' });
console.log(keysRes1); // >>> OK

const keysRes2 = await redis.keys('*name*');
console.log(keysRes2.sort()); // >>> ['firstname', 'lastname']

const keysRes3 = await redis.keys('a??');
console.log(keysRes3); // >>> ['age']

const keysRes4 = await redis.keys('*');
console.log(keysRes4.sort()); // >>> ['age', 'firstname', 'lastname']
```

##### JavaScript (Node.js)

```javascript
const keysRes1 = await client.mSet({ firstname: 'Jack', lastname: 'Stuntman', age: '35' });
console.log(keysRes1); // OK

const keysRes2 = await client.keys('*name*');
console.log(keysRes2.sort()); // ['firstname', 'lastname']

const keysRes3 = await client.keys('a??');
console.log(keysRes3); // ['age']

const keysRes4 = await client.keys('*');
console.log(keysRes4.sort()); // ['age', 'firstname', 'lastname']
```

##### JavaScript (Node.js)

```javascript
const keysRes1 = await redis.mset({ firstname: 'Jack', lastname: 'Stuntman', age: '35' });
console.log(keysRes1); // >>> OK

const keysRes2 = await redis.keys('*name*');
console.log(keysRes2.sort()); // >>> ['firstname', 'lastname']

const keysRes3 = await redis.keys('a??');
console.log(keysRes3); // >>> ['age']

const keysRes4 = await redis.keys('*');
console.log(keysRes4.sort()); // >>> ['age', 'firstname', 'lastname']
```

##### PHP

```php
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
```

##### Python

```python
res = r.mset({"firstname": "Jack", "lastname": "Stuntman", "age": "35"})
print(res)
# >>> True

res = r.keys("*name*")
print(sorted(res))
# >>> ['firstname', 'lastname']

res = r.keys("a??")
print(res)
# >>> ['age']

res = r.keys("*")
print(sorted(res))
# >>> ['age', 'firstname', 'lastname']
```

##### Rust (Asynchronous)

```rust
        match r.mset(&[("firstname", "Jack"), ("lastname", "Stuntman"), ("age", "35")]).await {
            Ok(res) => {
                let res: String = res;
                println!("{res}");    // >>> OK
            },
            Err(e) => {
                println!("Error setting keys: {e}");
                return;
            }
        }

        match r.keys::<&str, Vec<String>>("*name*").await {
            Ok(res) => {
                let mut sorted_res = res.clone();
                sorted_res.sort();
                println!("{sorted_res:?}");    // >>> ["firstname", "lastname"]
            },
            Err(e) => {
                println!("Error getting keys: {e}");
                return;
            }
        }

        match r.keys::<&str, Vec<String>>("a??").await {
            Ok(res) => {
                println!("{res:?}");    // >>> ["age"]
            },
            Err(e) => {
                println!("Error getting keys: {e}");
                return;
            }
        }

        match r.keys::<&str, Vec<String>>("*").await {
            Ok(res) => {
                let mut sorted_res = res.clone();
                sorted_res.sort();
                println!("{sorted_res:?}");    // >>> ["age", "firstname", "lastname"]
            },
            Err(e) => {
                println!("Error getting keys: {e}");
                return;
            }
        }
```

##### Rust (Synchronous)

```rust
        match r.mset(&[("firstname", "Jack"), ("lastname", "Stuntman"), ("age", "35")]) {
            Ok(res) => {
                let res: String = res;
                println!("{res}");    // >>> OK
            },
            Err(e) => {
                println!("Error setting keys: {e}");
                return;
            }
        }

        match r.keys::<&str, Vec<String>>("*name*") {
            Ok(res) => {
                let mut sorted_res = res.clone();
                sorted_res.sort();
                println!("{sorted_res:?}");    // >>> ["firstname", "lastname"]
            },
            Err(e) => {
                println!("Error getting keys: {e}");
                return;
            }
        }

        match r.keys::<&str, Vec<String>>("a??") {
            Ok(res) => {
                println!("{res:?}");    // >>> ["age"]
            },
            Err(e) => {
                println!("Error getting keys: {e}");
                return;
            }
        }

        match r.keys::<&str, Vec<String>>("*") {
            Ok(res) => {
                let mut sorted_res = res.clone();
                sorted_res.sort();
                println!("{sorted_res:?}");    // >>> ["age", "firstname", "lastname"]
            },
            Err(e) => {
                println!("Error getting keys: {e}");
                return;
            }
        }
```



## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Array reply](../../develop/reference/protocol-spec#arrays): a list of keys matching _pattern_.

**RESP3:**

[Array reply](../../develop/reference/protocol-spec#arrays): a list of keys matching _pattern_.



