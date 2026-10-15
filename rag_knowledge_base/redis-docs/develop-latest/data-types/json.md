# JSON

```json metadata
{
  "schema_version": 2,
  "title": "JSON",
  "description": "JSON support for Redis",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"primary-features","title":"Primary features"},{"id":"use-redis-with-json","title":"Use Redis with JSON"},{"id":"format-cli-output","title":"Format CLI output"},{"id":"enable-redis-json","title":"Enable Redis JSON"},{"id":"limitation","title":"Limitation"},{"id":"further-information","title":"Further information"}]}

,
  "codeExamples": [{"codetabsId":"json_tutorial-stepset_get","commands":[{"acl_categories":["@write","@json"],"complexity":"O(M+N)","name":"JSON.SET"},{"acl_categories":["@read","@json"],"complexity":"O(N)","name":"JSON.GET"},{"acl_categories":["@read","@json"],"complexity":"O(1)","name":"JSON.TYPE"}],"description":"Foundational: Set and retrieve JSON values using JSON.SET and JSON.GET to store and access JSON documents","difficulty":"beginner","id":"set_get","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_json_tutorial-stepset_get"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_json_tutorial-stepset_get"},{"id":"Node-js","panelId":"panel_Nodejs_json_tutorial-stepset_get"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_json_tutorial-stepset_get"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_json_tutorial-stepset_get"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_json_tutorial-stepset_get"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_json_tutorial-stepset_get"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_json_tutorial-stepset_get"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_json_tutorial-stepset_get"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_json_tutorial-stepset_get"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_json_tutorial-stepset_get"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_json_tutorial-stepset_get"}]},{"buildsUpon":["set_get"],"codetabsId":"json_tutorial-stepstr","commands":[{"acl_categories":["@read","@json"],"complexity":"O(1)","name":"JSON.STRLEN"},{"acl_categories":["@write","@json"],"complexity":"O(1)","name":"JSON.STRAPPEND"},{"acl_categories":["@read","@json"],"complexity":"O(N)","name":"JSON.GET"}],"description":"String operations: Manipulate JSON strings using JSON.STRLEN to get length and JSON.STRAPPEND to concatenate values","difficulty":"beginner","id":"str","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_json_tutorial-stepstr"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_json_tutorial-stepstr"},{"id":"Node-js","panelId":"panel_Nodejs_json_tutorial-stepstr"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_json_tutorial-stepstr"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_json_tutorial-stepstr"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_json_tutorial-stepstr"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_json_tutorial-stepstr"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_json_tutorial-stepstr"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_json_tutorial-stepstr"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_json_tutorial-stepstr"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_json_tutorial-stepstr"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_json_tutorial-stepstr"}]},{"buildsUpon":["set_get"],"codetabsId":"json_tutorial-stepnum","commands":[{"acl_categories":["@write","@json"],"complexity":"O(M+N)","name":"JSON.SET"},{"acl_categories":["@write","@json"],"complexity":"O(1)","name":"JSON.NUMINCRBY"},{"acl_categories":["@write","@json"],"complexity":"O(1)","name":"JSON.NUMMULTBY"}],"description":"Numeric operations: Perform atomic arithmetic on JSON numbers using JSON.NUMINCRBY to increment and JSON.NUMMULTBY to multiply values","difficulty":"beginner","id":"num","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_json_tutorial-stepnum"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_json_tutorial-stepnum"},{"id":"Node-js","panelId":"panel_Nodejs_json_tutorial-stepnum"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_json_tutorial-stepnum"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_json_tutorial-stepnum"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_json_tutorial-stepnum"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_json_tutorial-stepnum"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_json_tutorial-stepnum"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_json_tutorial-stepnum"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_json_tutorial-stepnum"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_json_tutorial-stepnum"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_json_tutorial-stepnum"}]},{"buildsUpon":["set_get"],"codetabsId":"json_tutorial-steparr","commands":[{"acl_categories":["@write","@json"],"complexity":"O(M+N)","name":"JSON.SET"},{"acl_categories":["@read","@json"],"complexity":"O(N)","name":"JSON.GET"},{"acl_categories":["@write","@json"],"complexity":"O(N)","name":"JSON.DEL"}],"description":"Arrays and objects: Work with complex JSON structures using JSONPath to access nested elements and JSON.DEL to remove values","difficulty":"intermediate","id":"arr","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_json_tutorial-steparr"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_json_tutorial-steparr"},{"id":"Node-js","panelId":"panel_Nodejs_json_tutorial-steparr"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_json_tutorial-steparr"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_json_tutorial-steparr"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_json_tutorial-steparr"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_json_tutorial-steparr"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_json_tutorial-steparr"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_json_tutorial-steparr"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_json_tutorial-steparr"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_json_tutorial-steparr"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_json_tutorial-steparr"}]},{"buildsUpon":["arr"],"codetabsId":"json_tutorial-steparr2","commands":[{"acl_categories":["@write","@json"],"complexity":"O(M+N)","name":"JSON.SET"},{"acl_categories":["@write","@json"],"complexity":"O(1)","name":"JSON.ARRAPPEND"},{"acl_categories":["@read","@json"],"complexity":"O(N)","name":"JSON.GET"},{"acl_categories":["@write","@json"],"complexity":"O(N)","name":"JSON.ARRINSERT"},{"acl_categories":["@write","@json"],"complexity":"O(N)","name":"JSON.ARRTRIM"},{"acl_categories":["@write","@json"],"complexity":"O(N)","name":"JSON.ARRPOP"}],"description":"Array manipulation: Use JSON.ARRAPPEND to add elements, JSON.ARRINSERT to insert at positions, JSON.ARRTRIM to keep ranges, and JSON.ARRPOP to remove elements","difficulty":"intermediate","id":"arr2","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_json_tutorial-steparr2"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_json_tutorial-steparr2"},{"id":"Node-js","panelId":"panel_Nodejs_json_tutorial-steparr2"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_json_tutorial-steparr2"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_json_tutorial-steparr2"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_json_tutorial-steparr2"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_json_tutorial-steparr2"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_json_tutorial-steparr2"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_json_tutorial-steparr2"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_json_tutorial-steparr2"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_json_tutorial-steparr2"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_json_tutorial-steparr2"}]},{"buildsUpon":["arr"],"codetabsId":"json_tutorial-stepobj","commands":[{"acl_categories":["@write","@json"],"complexity":"O(M+N)","name":"JSON.SET"},{"acl_categories":["@read","@json"],"complexity":"O(1)","name":"JSON.OBJLEN"},{"acl_categories":["@read","@json"],"complexity":"O(1)","name":"JSON.OBJKEYS"}],"description":"Object operations: Inspect JSON objects using JSON.OBJLEN to count fields and JSON.OBJKEYS to retrieve all keys","difficulty":"intermediate","id":"obj","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_json_tutorial-stepobj"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_json_tutorial-stepobj"},{"id":"Node-js","panelId":"panel_Nodejs_json_tutorial-stepobj"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_json_tutorial-stepobj"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_json_tutorial-stepobj"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_json_tutorial-stepobj"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_json_tutorial-stepobj"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_json_tutorial-stepobj"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_json_tutorial-stepobj"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_json_tutorial-stepobj"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_json_tutorial-stepobj"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_json_tutorial-stepobj"}]}]
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


### JSON command summary

**25 commands in this group:**

[View all json commands](https://redis.io/commands/?group=json)

| Command | Summary | Complexity | Since |
|---------|---------|------------|-------|
| [JSON.ARRAPPEND](https://redis.io/commands/json.arrappend/) | Append the JSON values into the array at path after the last element in it | O(1) when path is evaluated to a single value, ... | 1.0.0 |
| [JSON.ARRINDEX](https://redis.io/commands/json.arrindex/) | Search for the first occurrence of a JSON value in an array | O(N) when path is evaluated to a single value w... | 1.0.0 |
| [JSON.ARRINSERT](https://redis.io/commands/json.arrinsert/) | Insert the json values into the array at path before the index (shifts to the right) | O(N) when path is evaluated to a single value w... | 1.0.0 |
| [JSON.ARRLEN](https://redis.io/commands/json.arrlen/) | Report the length of the JSON array at path in key | O(1) where path is evaluated to a single value,... | 1.0.0 |
| [JSON.ARRPOP](https://redis.io/commands/json.arrpop/) | Remove and return the element at the specified index in the array at path | O(N) when path is evaluated to a single value w... | 1.0.0 |
| [JSON.ARRTRIM](https://redis.io/commands/json.arrtrim/) | Trim an array so that it contains only the specified inclusive range of elements | O(N) when path is evaluated to a single value w... | 1.0.0 |
| [JSON.CLEAR](https://redis.io/commands/json.clear/) | Clear container values (arrays/objects) and set numeric values to 0 | O(N) when path is evaluated to a single value w... | 2.0.0 |
| [JSON.DEBUG](https://redis.io/commands/json.debug/) | This is a container command for debugging related tasks | N/A | 1.0.0 |
| [JSON.DEL](https://redis.io/commands/json.del/) | Delete a value | O(N) when path is evaluated to a single value w... | 1.0.0 |
| [JSON.FORGET](https://redis.io/commands/json.forget/) | Delete a value | O(N) when path is evaluated to a single value w... | 1.0.0 |

#### JSON command summary (part 2)

| Command | Summary | Complexity | Since |
|---------|---------|------------|-------|
| [JSON.GET](https://redis.io/commands/json.get/) | Get JSON value at path | O(N) where N is the size of the JSON | 1.0.0 |
| [JSON.MERGE](https://redis.io/commands/json.merge/) | Merge a given JSON value into matching paths. Consequently, JSON values at matching paths are updated, deleted, or expanded with new children | O(M+N) when path is evaluated to a single value... | 2.6.0 |
| [JSON.MGET](https://redis.io/commands/json.mget/) | Return the values at path from multiple key arguments | O(M*N) when path is evaluated to a single value... | 1.0.0 |
| [JSON.MSET](https://redis.io/commands/json.mset/) | Set or update one or more JSON values according to the specified key-path-value triplets | O(K*(M+N)) where k is the number of keys in the... | 2.6.0 |
| [JSON.NUMINCRBY](https://redis.io/commands/json.numincrby/) | Increment the number value stored at path by number | O(1) when path is evaluated to a single value, ... | 1.0.0 |
| [JSON.NUMMULTBY](https://redis.io/commands/json.nummultby/) | Multiply the number value stored at path by number | O(1) when path is evaluated to a single value, ... | 1.0.0 |
| [JSON.NUMPOWBY](https://redis.io/commands/json.numpowby/) | Raise the number value stored at path to the power of number | O(1) when path is evaluated to a single value, ... | 1.0.0 |
| [JSON.OBJKEYS](https://redis.io/commands/json.objkeys/) | Return the keys in the object that's referenced by path | O(1) when path is evaluated to a single value, ... | 1.0.0 |
| [JSON.OBJLEN](https://redis.io/commands/json.objlen/) | Report the number of keys in the JSON object at path in key | O(1) when path is evaluated to a single value, ... | 1.0.0 |
| [JSON.RESP](https://redis.io/commands/json.resp/) | Return the JSON in key in Redis serialization protocol specification form | O(N) when path is evaluated to a single value, ... | 1.0.0 |

#### JSON command summary (part 3)

| Command | Summary | Complexity | Since |
|---------|---------|------------|-------|
| [JSON.SET](https://redis.io/commands/json.set/) | Set the JSON value at path in key | O(M+N) where M is the size of the original valu... | 1.0.0 |
| [JSON.STRAPPEND](https://redis.io/commands/json.strappend/) | Append the json-string values to the string at path | O(1) when path is evaluated to a single value, ... | 1.0.0 |
| [JSON.STRLEN](https://redis.io/commands/json.strlen/) | Report the length of the JSON String at path in key | O(1) when path is evaluated to a single value, ... | 1.0.0 |
| [JSON.TOGGLE](https://redis.io/commands/json.toggle/) | Toggle the boolean value stored at path | O(1) when path is evaluated to a single value, ... | 2.0.0 |
| [JSON.TYPE](https://redis.io/commands/json.type/) | Report the type of JSON value at path | O(1) when path is evaluated to a single value, ... | 1.0.0 |



[![Discord](https://img.shields.io/discord/697882427875393627?style=flat-square)](https://discord.gg/QUkjSsk)
[![Github](https://img.shields.io/static/v1?label=&message=repository&color=5961FF&logo=github)](https://github.com/RedisJSON/RedisJSON/)

The JSON capability of Redis Open Source provides JavaScript Object Notation (JSON) support for Redis. It lets you store, update, and retrieve JSON values in a Redis database, similar to any other Redis data type. Redis JSON also works seamlessly with [Redis Search](https://redis.io/docs/latest/develop/ai/search-and-query) to let you [index and query JSON documents](https://redis.io/docs/latest/develop/ai/search-and-query/indexing).

## Primary features

* Full support for the JSON standard
* A [JSONPath](http://goessner.net/articles/JsonPath/) syntax for selecting/updating elements inside documents (see [JSONPath syntax](https://redis.io/docs/latest/develop/data-types/json/path#jsonpath-syntax))
* Documents stored as binary data in a tree structure, allowing fast access to sub-elements
* Typed atomic operations for all JSON value types

## Use Redis with JSON

The first JSON command to try is [`JSON.SET`](https://redis.io/docs/latest/commands/json.set), which sets a Redis key with a JSON value. [`JSON.SET`](https://redis.io/docs/latest/commands/json.set) accepts all JSON value types. This example creates a JSON string:

Foundational: Set and retrieve JSON values using JSON.SET and JSON.GET to store and access JSON documents

**Commands:** JSON.SET, JSON.GET, JSON.TYPE

**Complexity:**
- JSON.SET: O(M+N)
- JSON.GET: O(N)
- JSON.TYPE: O(1)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> JSON.SET bike $ '"Hyperion"'
OK
> JSON.GET bike $
"[\"Hyperion\"]"
> JSON.TYPE bike $
1) "string"
```

##### C#

```csharp
        bool res1 = db.JSON().Set("bike", "$", "\"Hyperion\"");
        Console.WriteLine(res1);    // >>> True

        RedisResult res2 = db.JSON().Get("bike", path: "$");
        Console.WriteLine(res2);    // >>> ["Hyperion"]

        JsonType[] res3 = db.JSON().Type("bike", "$");
        Console.WriteLine(string.Join(", ", res3)); // >>> STRING
```

##### Go

```go
	res1, err := rdb.JSONSet(ctx, "bike", "$",
		"\"Hyperion\"",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // >>> OK

	res2, err := rdb.JSONGet(ctx, "bike", "$").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2) // >>> ["Hyperion"]

	res3, err := rdb.JSONType(ctx, "bike", "$").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3) // >>> [[string]]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> setget = asyncCommands
                    .jsonSet("bike", JsonPath.ROOT_PATH, parser.createJsonValue("\"Hyperion\"")).thenCompose(res1 -> {
                        System.out.println(res1); // OK

                        return asyncCommands.jsonGet("bike", JsonPath.ROOT_PATH);
                    }).thenCompose(res2 -> {
                        System.out.println(res2); // >>> [["Hyperion"]]

                        return asyncCommands.jsonType("bike", JsonPath.ROOT_PATH);
                    })
                    .thenAccept(System.out::println)
                    // >>> [STRING]
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> setget = reactiveCommands.jsonSet("bike", JsonPath.ROOT_PATH, parser.createJsonValue("\"Hyperion\""))
                    .doOnNext(res1 -> {
                        System.out.println(res1); // OK
                    }).flatMap(res1 -> reactiveCommands.jsonGet("bike", JsonPath.ROOT_PATH).collectList()).doOnNext(res2 -> {
                        System.out.println(res2); // >>> [["Hyperion"]]
                    }).flatMap(res2 -> reactiveCommands.jsonType("bike", JsonPath.ROOT_PATH).collectList())
                    .doOnNext(System.out::println) // >>> [STRING]
                    .then();
```

##### Java (Synchronous - Jedis)

```java
        String res1 = jedis.jsonSet("bike", new Path2("$"), "\"Hyperion\"");
        System.out.println(res1);   // >>> OK

        Object res2 = jedis.jsonGet("bike", new Path2("$"));
        System.out.println(res2);   // >>> ["Hyperion"]

        List<Class<?>> res3 = jedis.jsonType("bike", new Path2("$"));
        System.out.println(res3);   // >>> [class java.lang.String]
```

##### JavaScript (Node.js)

```javascript
const res1 = await client.json.set("bike", "$", '"Hyperion"');
console.log(res1); // OK

const res2 = await client.json.get("bike", { path: "$" });
console.log(res2); // ['"Hyperion"']

const res3 = await client.json.type("bike", { path: "$" });
console.log(res3); //  [ 'string' ]
```

##### PHP

```php
        $res1 = $r->jsonset('bike', '$', '"Hyperion"');
        echo $res1 . PHP_EOL;
        // >>> OK

        $res2 = $r->jsonget('bike', '', '', '', '$');
        echo $res2 . PHP_EOL;
        // >>> ["Hyperion"]

        $res3 = $r->jsontype('bike', '$');
        echo json_encode($res3) . PHP_EOL;
        // >>> ["string"]
```

##### Python

```python
res1 = r.json().set("bike", "$", '"Hyperion"')
print(res1)  # >>> True

res2 = r.json().get("bike", "$")
print(res2)  # >>> ['"Hyperion"']

res3 = r.json().type("bike", "$")
print(res3)  # >>> ['string']
```

##### Ruby

```ruby
res1 = r.json_set('bike', '$', 'Hyperion')
puts res1 # >>> OK

res2 = r.json_get('bike', '$')
p res2 # >>> ["Hyperion"]

res3 = r.json_type('bike', '$')
p res3 # >>> ["string"]

# With raw: true, json_set accepts an already-encoded JSON string (skipping
# serialization) and json_get returns the unparsed JSON string rather than a
# Ruby object — useful when you store or forward plain JSON.
res_raw1 = r.json_set('bike', '$', '"Hyperion"', raw: true)
puts res_raw1 # >>> OK

res_raw2 = r.json_get('bike', '$', raw: true)
puts res_raw2 # >>> ["Hyperion"]  (a JSON string, not a Ruby array)
```

##### Rust (Asynchronous)

```rust
        let res1: bool = r
            .json_set("bike", "$", &json!("Hyperion"))
            .await
            .expect("Failed to run JSON.SET");
        print_set_result(res1); // >>> OK

        let res2: String = r
            .json_get("bike", "$")
            .await
            .expect("Failed to run JSON.GET");
        println!("{res2}"); // >>> ["Hyperion"]

        let res3: Value = r
            .json_type("bike", "$")
            .await
            .expect("Failed to run JSON.TYPE");
        print_redis_value(&res3); // >>> ["string"]
```

##### Rust (Synchronous)

```rust
        let res1: bool = r
            .json_set("bike", "$", &json!("Hyperion"))
            .expect("Failed to run JSON.SET");
        print_set_result(res1); // >>> OK

        let res2: String = r.json_get("bike", "$").expect("Failed to run JSON.GET");
        println!("{res2}"); // >>> ["Hyperion"]

        let res3: Value = r.json_type("bike", "$").expect("Failed to run JSON.TYPE");
        print_redis_value(&res3); // >>> ["string"]
```



Note how the commands include the dollar sign character `$`. This is the [path](https://redis.io/docs/latest/develop/data-types/json/path) to the value in the JSON document (in this case it just means the root).

Here are a few more string operations. [`JSON.STRLEN`](https://redis.io/docs/latest/commands/json.strlen) tells you the length of the string, and you can append another string to it with [`JSON.STRAPPEND`](https://redis.io/docs/latest/commands/json.strappend).

String operations: Manipulate JSON strings using JSON.STRLEN to get length and JSON.STRAPPEND to concatenate values

**Builds upon:** set_get

**Commands:** JSON.STRLEN, JSON.STRAPPEND, JSON.GET

**Complexity:**
- JSON.STRLEN: O(1)
- JSON.STRAPPEND: O(1)
- JSON.GET: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> JSON.STRLEN bike $
1) (integer) 8
> JSON.STRAPPEND bike $ '" (Enduro bikes)"'
1) (integer) 23
> JSON.GET bike $
"[\"Hyperion (Enduro bikes)\"]"
```

##### C#

```csharp
        long?[] res4 = db.JSON().StrLen("bike", "$");
        Console.Write(string.Join(", ", res4)); // >>> 8

        long?[] res5 = db.JSON().StrAppend("bike", " (Enduro bikes)");
        Console.WriteLine(string.Join(", ", res5)); // >>> 23

        RedisResult res6 = db.JSON().Get("bike", path: "$");
        Console.WriteLine(res6);    // >>> ["Hyperion (Enduro bikes)"]
```

##### Go

```go
	res4, err := rdb.JSONStrLen(ctx, "bike", "$").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(*res4[0]) // >>> 8

	res5, err := rdb.JSONStrAppend(ctx, "bike", "$", "\" (Enduro bikes)\"").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(*res5[0]) // >>> 23

	res6, err := rdb.JSONGet(ctx, "bike", "$").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res6) // >>> ["Hyperion (Enduro bikes)"]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> str = asyncCommands.jsonStrlen("bike", JsonPath.ROOT_PATH).thenCompose(res3 -> {
                System.out.println(res3); // >>> [8]

                return asyncCommands.jsonStrappend("bike", JsonPath.ROOT_PATH, parser.createJsonValue("\" (Enduro bikes)\""));
            }).thenCompose(res4 -> {
                System.out.println(res4); // >>> [23]

                return asyncCommands.jsonGet("bike", JsonPath.ROOT_PATH);
            })
                    .thenAccept(System.out::println)
                    // >>> [["Hyperion (Enduro bikes)"]]
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> str = reactiveCommands.jsonStrlen("bike", JsonPath.ROOT_PATH).collectList().doOnNext(res3 -> {
                System.out.println(res3); // >>> [8]
            }).flatMap(res3 -> reactiveCommands
                    .jsonStrappend("bike", JsonPath.ROOT_PATH, parser.createJsonValue("\" (Enduro bikes)\"")).collectList())
                    .doOnNext(res4 -> {
                        System.out.println(res4); // >>> [23]
                    }).flatMap(res4 -> reactiveCommands.jsonGet("bike", JsonPath.ROOT_PATH).collectList())
                    .doOnNext(System.out::println) // >>> [["Hyperion (Enduro bikes)"]]
                    .then();
```

##### Java (Synchronous - Jedis)

```java
        List<Long> res4 = jedis.jsonStrLen("bike", new Path2("$"));
        System.out.println(res4);   // >>> [8]

        List<Long> res5 = jedis.jsonStrAppend("bike", new Path2("$"), " (Enduro bikes)");
        System.out.println(res5);   // >>> [23]

        Object res6 = jedis.jsonGet("bike", new Path2("$"));
        System.out.println(res6);   // >>> ["Hyperion (Enduro bikes)"]
```

##### JavaScript (Node.js)

```javascript
const res4 = await client.json.strLen("bike", { path: "$" });
console.log(res4) //  [10]

const res5 = await client.json.strAppend("bike", '" (Enduro bikes)"');
console.log(res5) //  27

const res6 = await client.json.get("bike", { path: "$" });
console.log(res6) //  ['"Hyperion"" (Enduro bikes)"']
```

##### PHP

```php
        $res4 = $r->jsonstrlen('bike', '$');
        echo json_encode($res4) . PHP_EOL;
        // >>> [8]

        $res5 = $r->jsonstrappend('bike', '$', '" (Enduro bikes)"');
        echo json_encode($res5) . PHP_EOL;
        // >>> [23]

        $res6 = $r->jsonget('bike', '', '', '', '$');
        echo $res6 . PHP_EOL;
        // >>> "Hyperion (Enduro bikes)"
```

##### Python

```python
res4 = r.json().strlen("bike", "$")
print(res4)  # >>> [10]

res5 = r.json().strappend("bike", '" (Enduro bikes)"')
print(res5)  # >>> 27

res6 = r.json().get("bike", "$")
print(res6)  # >>> ['"Hyperion"" (Enduro bikes)"']
```

##### Ruby

```ruby
res4 = r.json_strlen('bike', '$')
p res4 # >>> [8]

res5 = r.json_strappend('bike', '$', ' (Enduro bikes)')
p res5 # >>> [23]

res6 = r.json_get('bike', '$')
p res6 # >>> ["Hyperion (Enduro bikes)"]
```

##### Rust (Asynchronous)

```rust
        let res4: Value = r
            .json_str_len("bike", "$")
            .await
            .expect("Failed to run JSON.STRLEN");
        print_redis_value(&res4); // >>> [8]

        let res5: Value = r
            .json_str_append("bike", "$", "\" (Enduro bikes)\"")
            .await
            .expect("Failed to run JSON.STRAPPEND");
        print_redis_value(&res5); // >>> [23]

        let res6: String = r
            .json_get("bike", "$")
            .await
            .expect("Failed to run JSON.GET");
        println!("{res6}"); // >>> ["Hyperion (Enduro bikes)"]
```

##### Rust (Synchronous)

```rust
        let res4: Value = r
            .json_str_len("bike", "$")
            .expect("Failed to run JSON.STRLEN");
        print_redis_value(&res4); // >>> [8]

        let res5: Value = r
            .json_str_append("bike", "$", "\" (Enduro bikes)\"")
            .expect("Failed to run JSON.STRAPPEND");
        print_redis_value(&res5); // >>> [23]

        let res6: String = r.json_get("bike", "$").expect("Failed to run JSON.GET");
        println!("{res6}"); // >>> ["Hyperion (Enduro bikes)"]
```



Numbers can be [incremented](https://redis.io/docs/latest/commands/json.numincrby) and [multiplied](https://redis.io/docs/latest/commands/json.nummultby):

Numeric operations: Perform atomic arithmetic on JSON numbers using JSON.NUMINCRBY to increment and JSON.NUMMULTBY to multiply values

**Builds upon:** set_get

**Commands:** JSON.SET, JSON.NUMINCRBY, JSON.NUMMULTBY

**Complexity:**
- JSON.SET: O(M+N)
- JSON.NUMINCRBY: O(1)
- JSON.NUMMULTBY: O(1)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> JSON.SET crashes $ 0
OK
> JSON.NUMINCRBY crashes $ 1
"[1]"
> JSON.NUMINCRBY crashes $ 1.5
"[2.5]"
> JSON.NUMINCRBY crashes $ -0.75
"[1.75]"
> JSON.NUMMULTBY crashes $ 24
"[42.0]"
```

##### C#

```csharp
        bool res7 = db.JSON().Set("crashes", "$", 0);
        Console.WriteLine(res7);    // >>> True

        double?[] res8 = db.JSON().NumIncrby("crashes", "$", 1);
        Console.WriteLine(string.Join(", ", res8));    // >>> 1

        double?[] res9 = db.JSON().NumIncrby("crashes", "$", 1.5);
        Console.WriteLine(string.Join(", ", res9));    // >>> 2.5

        double?[] res10 = db.JSON().NumIncrby("crashes", "$", -0.75);
        Console.WriteLine(string.Join(", ", res10));    // >>> 1.75
```

##### Go

```go
	res7, err := rdb.JSONSet(ctx, "crashes", "$", 0).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res7) // >>> OK

	res8, err := rdb.JSONNumIncrBy(ctx, "crashes", "$", 1).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res8) // >>> [1]

	res9, err := rdb.JSONNumIncrBy(ctx, "crashes", "$", 1.5).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res9) // >>> [2.5]

	res10, err := rdb.JSONNumIncrBy(ctx, "crashes", "$", -0.75).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res10) // >>> [1.75]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> num = asyncCommands.jsonSet("crashes", JsonPath.ROOT_PATH, parser.createJsonValue("0"))
                    .thenCompose(res5 -> {
                        System.out.println(res5); // >>> OK

                        return asyncCommands.jsonNumincrby("crashes", JsonPath.ROOT_PATH, 1);
                    }).thenCompose(res6 -> {
                        System.out.println(res6); // >>> [1]

                        return asyncCommands.jsonNumincrby("crashes", JsonPath.ROOT_PATH, 1.5);
                    }).thenCompose(res7 -> {
                        System.out.println(res7); // >>> [2.5]

                        return asyncCommands.jsonNumincrby("crashes", JsonPath.ROOT_PATH, -0.75);
                    })
                    .thenAccept(System.out::println) // >>> [1.75]
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> num = reactiveCommands.jsonSet("crashes", JsonPath.ROOT_PATH, parser.createJsonValue("0"))
                    .doOnNext(res5 -> {
                        System.out.println(res5); // >>> OK
                    }).flatMap(res5 -> reactiveCommands.jsonNumincrby("crashes", JsonPath.ROOT_PATH, 1).collectList())
                    .doOnNext(res6 -> {
                        System.out.println(res6); // >>> [1]
                    }).flatMap(res6 -> reactiveCommands.jsonNumincrby("crashes", JsonPath.ROOT_PATH, 1.5).collectList())
                    .doOnNext(res7 -> {
                        System.out.println(res7); // >>> [2.5]
                    }).flatMap(res7 -> reactiveCommands.jsonNumincrby("crashes", JsonPath.ROOT_PATH, -0.75).collectList())
                    .doOnNext(System.out::println) // >>> [1.75]
                    .then();
```

##### Java (Synchronous - Jedis)

```java
        String res7 = jedis.jsonSet("crashes", new Path2("$"), 0);
        System.out.println(res7);   // >>> OK

        Object res8 = jedis.jsonNumIncrBy("crashes", new Path2("$"), 1);
        System.out.println(res8);   // >>> [1]

        Object res9 = jedis.jsonNumIncrBy("crashes", new Path2("$"), 1.5);
        System.out.println(res9);   // >>> [2.5]

        Object res10 = jedis.jsonNumIncrBy("crashes", new Path2("$"), -0.75);
        System.out.println(res10);   // >>> [1.75]
```

##### JavaScript (Node.js)

```javascript
const res7 = await client.json.set("crashes", "$", 0);
console.log(res7) //  OK

const res8 = await client.json.numIncrBy("crashes", "$", 1);
console.log(res8) //  [1]

const res9 = await client.json.numIncrBy("crashes", "$", 1.5);
console.log(res9) //  [2.5]

const res10 = await client.json.numIncrBy("crashes", "$", -0.75);
console.log(res10) //  [1.75]
```

##### PHP

```php
        $res7 = $r->jsonset('crashes', '$', '0');
        echo $res7 . PHP_EOL;
        // >>> OK

        $res8 = $r->jsonnumincrby('crashes', '$', 1);
        echo $res8 . PHP_EOL;
        // >>> [1]

        $res9 = $r->jsonnumincrby('crashes', '$', 1.5);
        echo $res9 . PHP_EOL;
        // >>> [2.5]

        $res10 = $r->jsonnumincrby('crashes', '$', -0.75);
        echo $res10 . PHP_EOL;
        // >>> [1.75]
```

##### Python

```python
res7 = r.json().set("crashes", "$", 0)
print(res7)  # >>> True

res8 = r.json().numincrby("crashes", "$", 1)
print(res8)  # >>> [1]

res9 = r.json().numincrby("crashes", "$", 1.5)
print(res9)  # >>> [2.5]

res10 = r.json().numincrby("crashes", "$", -0.75)
print(res10)  # >>> [1.75]
```

##### Ruby

```ruby
res7 = r.json_set('crashes', '$', 0)
puts res7 # >>> OK

res8 = r.json_numincrby('crashes', '$', 1)
p res8 # >>> [1]

res9 = r.json_numincrby('crashes', '$', 1.5)
p res9 # >>> [2.5]

res10 = r.json_numincrby('crashes', '$', -0.75)
p res10 # >>> [1.75]
```

##### Rust (Asynchronous)

```rust
        let res7: bool = r
            .json_set("crashes", "$", &json!(0))
            .await
            .expect("Failed to run JSON.SET");
        print_set_result(res7); // >>> OK

        let res8: String = cmd("JSON.NUMINCRBY")
            .arg("crashes")
            .arg("$")
            .arg(1)
            .query_async(&mut r)
            .await
            .expect("Failed to run JSON.NUMINCRBY");
        println!("{res8}"); // >>> [1]

        let res9: String = cmd("JSON.NUMINCRBY")
            .arg("crashes")
            .arg("$")
            .arg(1.5)
            .query_async(&mut r)
            .await
            .expect("Failed to run JSON.NUMINCRBY");
        println!("{res9}"); // >>> [2.5]

        let res10: String = cmd("JSON.NUMINCRBY")
            .arg("crashes")
            .arg("$")
            .arg(-0.75)
            .query_async(&mut r)
            .await
            .expect("Failed to run JSON.NUMINCRBY");
        println!("{res10}"); // >>> [1.75]

        let res11: String = cmd("JSON.NUMMULTBY")
            .arg("crashes")
            .arg("$")
            .arg(24)
            .query_async(&mut r)
            .await
            .expect("Failed to run JSON.NUMMULTBY");
        println!("{res11}"); // >>> [42.0]
```

##### Rust (Synchronous)

```rust
        let res7: bool = r
            .json_set("crashes", "$", &json!(0))
            .expect("Failed to run JSON.SET");
        print_set_result(res7); // >>> OK

        let res8: String = cmd("JSON.NUMINCRBY")
            .arg("crashes")
            .arg("$")
            .arg(1)
            .query(&mut r)
            .expect("Failed to run JSON.NUMINCRBY");
        println!("{res8}"); // >>> [1]

        let res9: String = cmd("JSON.NUMINCRBY")
            .arg("crashes")
            .arg("$")
            .arg(1.5)
            .query(&mut r)
            .expect("Failed to run JSON.NUMINCRBY");
        println!("{res9}"); // >>> [2.5]

        let res10: String = cmd("JSON.NUMINCRBY")
            .arg("crashes")
            .arg("$")
            .arg(-0.75)
            .query(&mut r)
            .expect("Failed to run JSON.NUMINCRBY");
        println!("{res10}"); // >>> [1.75]

        let res11: String = cmd("JSON.NUMMULTBY")
            .arg("crashes")
            .arg("$")
            .arg(24)
            .query(&mut r)
            .expect("Failed to run JSON.NUMMULTBY");
        println!("{res11}"); // >>> [42.0]
```



Here's a more interesting example that includes JSON arrays and objects:

Arrays and objects: Work with complex JSON structures using JSONPath to access nested elements and JSON.DEL to remove values

**Difficulty:** Intermediate

**Builds upon:** set_get

**Commands:** JSON.SET, JSON.GET, JSON.DEL

**Complexity:**
- JSON.SET: O(M+N)
- JSON.GET: O(N)
- JSON.DEL: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> JSON.SET newbike $ '["Deimos", {"crashes": 0}, null]'
OK
> JSON.GET newbike $
"[[\"Deimos\",{\"crashes\":0},null]]"
> JSON.GET newbike $[1].crashes
"[0]"
> JSON.DEL newbike $[-1]
(integer) 1
> JSON.GET newbike $
"[[\"Deimos\",{\"crashes\":0}]]"
```

##### C#

```csharp
        bool res11 = db.JSON().Set("newbike", "$", new object?[] { "Deimos", new { crashes = 0 }, null });
        Console.WriteLine(res11);   // >>> True

        RedisResult res12 = db.JSON().Get("newbike", path: "$");
        Console.WriteLine(res12);   //  >>> [["Deimos",{"crashes":0},null]]

        RedisResult res13 = db.JSON().Get("newbike", path: "$[1].crashes");
        Console.WriteLine(res13);   // >>> [0]

        long res14 = db.JSON().Del("newbike", "$.[-1]");
        Console.WriteLine(res14);   // >>> 1

        RedisResult res15 = db.JSON().Get("newbike", path: "$");
        Console.WriteLine(res15);   // >>> [["Deimos",{"crashes":0}]]
```

##### Go

```go
	res11, err := rdb.JSONSet(ctx, "newbike", "$",
		[]interface{}{
			"Deimos",
			map[string]interface{}{"crashes": 0},
			nil,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res11) // >>> OK

	res12, err := rdb.JSONGet(ctx, "newbike", "$").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res12) // >>> [["Deimos",{"crashes":0},null]]

	res13, err := rdb.JSONGet(ctx, "newbike", "$[1].crashes").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res13) // >>> [0]

	res14, err := rdb.JSONDel(ctx, "newbike", "$.[-1]").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res14) // >>> 1

	res15, err := rdb.JSONGet(ctx, "newbike", "$").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res15) // >>> [["Deimos",{"crashes":0}]]
```

##### Java (Asynchronous - Lettuce)

```java
            JsonObject crashDetails = parser.createJsonObject();
            crashDetails.put("crashes", parser.createJsonValue("0"));

            JsonArray bikeDetails = parser.createJsonArray();
            bikeDetails.add(parser.createJsonValue("\"Deimos\""));
            bikeDetails.add(crashDetails);
            bikeDetails.add(null);

            CompletableFuture<Void> arr = asyncCommands.jsonSet("newbike", JsonPath.ROOT_PATH, bikeDetails).thenCompose(r -> {
                System.out.println(r); // >>> OK

                return asyncCommands.jsonGet("newbike", JsonPath.ROOT_PATH);
            }).thenCompose(res8 -> {
                System.out.println(res8);
                // >>> [["Deimos",{"crashes":0},null]]

                return asyncCommands.jsonGet("newbike", JsonPath.of("$[1].crashes"));
            }).thenCompose(res9 -> {
                System.out.println(res9); // >>> [[0]]

                return asyncCommands.jsonDel("newbike", JsonPath.of("$.[-1]"));
            }).thenCompose(res10 -> {
                System.out.println(res10); // >>> 1

                return asyncCommands.jsonGet("newbike", JsonPath.ROOT_PATH);
            })
                    .thenAccept(System.out::println)
                    // >>> [[[\"Deimos\",{\"crashes\":0}]]]
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            JsonObject crashDetails = parser.createJsonObject();
            crashDetails.put("crashes", parser.createJsonValue("0"));

            JsonArray bikeDetails = parser.createJsonArray();
            bikeDetails.add(parser.createJsonValue("\"Deimos\""));
            bikeDetails.add(crashDetails);
            bikeDetails.add(null);

            Mono<Void> arr = reactiveCommands.jsonSet("newbike", JsonPath.ROOT_PATH, bikeDetails).doOnNext(r -> {
                System.out.println(r); // >>> OK
            }).flatMap(r -> reactiveCommands.jsonGet("newbike", JsonPath.ROOT_PATH).collectList()).doOnNext(res8 -> {
                System.out.println(res8);
                // >>> [["Deimos",{"crashes":0},null]]
            }).flatMap(res8 -> reactiveCommands.jsonGet("newbike", JsonPath.of("$[1].crashes")).collectList())
                    .doOnNext(res9 -> {
                        System.out.println(res9); // >>> [[0]]
                    }).flatMap(res9 -> reactiveCommands.jsonDel("newbike", JsonPath.of("$.[-1]"))).doOnNext(res10 -> {
                        System.out.println(res10); // >>> 1
                    }).flatMap(res10 -> reactiveCommands.jsonGet("newbike", JsonPath.ROOT_PATH).collectList())
                    .doOnNext(System.out::println) // >>> [[[\"Deimos\",{\"crashes\":0}]]]
                    .then();
```

##### Java (Synchronous - Jedis)

```java
        String res11 = jedis.jsonSet("newbike", new Path2("$"),
            new JSONArray()
                .put("Deimos")
                .put(new JSONObject().put("crashes", 0))
                .put((Object) null)
        );
        System.out.println(res11);  // >>> OK
        
        Object res12 = jedis.jsonGet("newbike", new Path2("$"));
        System.out.println(res12);  // >>> [["Deimos",{"crashes":0},null]]

        Object res13 = jedis.jsonGet("newbike", new Path2("$[1].crashes"));
        System.out.println(res13);  // >>> [0]

        long res14 = jedis.jsonDel("newbike", new Path2("$.[-1]"));
        System.out.println(res14);  // >>> 1

        Object res15 = jedis.jsonGet("newbike", new Path2("$"));
        System.out.println(res15);  // >>> [["Deimos",{"crashes":0}]]
```

##### JavaScript (Node.js)

```javascript
const res11 = await client.json.set("newbike", "$", ["Deimos", {"crashes": 0 }, null]);
console.log(res11); //  OK

const res12 = await client.json.get("newbike", { path: "$" });
console.log(res12); //  [[ 'Deimos', { crashes: 0 }, null ]]

const res13 = await client.json.get("newbike", { path: "$[1].crashes" });
console.log(res13); //  [0]

const res14 = await client.json.del("newbike", { path: "$.[-1]"} );
console.log(res14); //  1

const res15 = await client.json.get("newbike", { path: "$" });
console.log(res15); //  [[ 'Deimos', { crashes: 0 } ]]
```

##### PHP

```php
        $newbike = json_encode(["Deimos", ["crashes" => 0], null], JSON_THROW_ON_ERROR);
        $res11 = $r->jsonset('newbike', '$', $newbike);
        echo $res11 . PHP_EOL;
        // >>> OK

        $res12 = $r->jsonget('newbike', '', '', '', '$');
        echo $res12 . PHP_EOL;
        // >>> [["Deimos",{"crashes":0},null]]

        $res13 = $r->jsonget('newbike', '', '', '', '$[1].crashes');
        echo $res13 . PHP_EOL;
        // >>> 0

        $res14 = $r->jsondel('newbike', '$.[-1]');
        echo $res14 . PHP_EOL;
        // >>> 1

        $res15 = $r->jsonget('newbike', '', '', '', '$');
        echo $res15 . PHP_EOL;
        // >>> ["Deimos",{"crashes":0}]
```

##### Python

```python
res11 = r.json().set("newbike", "$", ["Deimos", {"crashes": 0}, None])
print(res11)  # >>> True

res12 = r.json().get("newbike", "$")
print(res12)  # >>> ['["Deimos", { "crashes": 0 }, null]']

res13 = r.json().get("newbike", "$[1].crashes")
print(res13)  # >>> [0]

res14 = r.json().delete("newbike", "$.[-1]")
print(res14)  # >>> [1]

res15 = r.json().get("newbike", "$")
print(res15)  # >>> [['Deimos', {'crashes': 0}]]
```

##### Ruby

```ruby
res11 = r.json_set('newbike', '$', ['Deimos', { 'crashes' => 0 }, nil])
puts res11 # >>> OK

res12 = r.json_get('newbike', '$')
p res12 # >>> [["Deimos", {"crashes"=>0}, nil]]

res13 = r.json_get('newbike', '$[1].crashes')
p res13 # >>> [0]

res14 = r.json_del('newbike', '$.[-1]')
p res14 # >>> 1

res15 = r.json_get('newbike', '$')
p res15 # >>> [["Deimos", {"crashes"=>0}]]

# The same raw: true option returns the array as unparsed JSON text.
res_raw3 = r.json_get('newbike', '$', raw: true)
puts res_raw3 # >>> [["Deimos",{"crashes":0}]]  (a JSON string)
```

##### Rust (Asynchronous)

```rust
        let res12: bool = r
            .json_set("newbike", "$", &json!(["Deimos", {"crashes": 0}, null]))
            .await
            .expect("Failed to run JSON.SET");
        print_set_result(res12); // >>> OK

        let res13: String = r
            .json_get("newbike", "$")
            .await
            .expect("Failed to run JSON.GET");
        println!("{res13}"); // >>> [["Deimos",{"crashes":0},null]]

        let res14: String = r
            .json_get("newbike", "$[1].crashes")
            .await
            .expect("Failed to run JSON.GET");
        println!("{res14}"); // >>> [0]

        let res15: i64 = r
            .json_del("newbike", "$[-1]")
            .await
            .expect("Failed to run JSON.DEL");
        println!("{res15}"); // >>> 1

        let res16: String = r
            .json_get("newbike", "$")
            .await
            .expect("Failed to run JSON.GET");
        println!("{res16}"); // >>> [["Deimos",{"crashes":0}]]
```

##### Rust (Synchronous)

```rust
        let res12: bool = r
            .json_set("newbike", "$", &json!(["Deimos", {"crashes": 0}, null]))
            .expect("Failed to run JSON.SET");
        print_set_result(res12); // >>> OK

        let res13: String = r.json_get("newbike", "$").expect("Failed to run JSON.GET");
        println!("{res13}"); // >>> [["Deimos",{"crashes":0},null]]

        let res14: String = r
            .json_get("newbike", "$[1].crashes")
            .expect("Failed to run JSON.GET");
        println!("{res14}"); // >>> [0]

        let res15: i64 = r
            .json_del("newbike", "$[-1]")
            .expect("Failed to run JSON.DEL");
        println!("{res15}"); // >>> 1

        let res16: String = r.json_get("newbike", "$").expect("Failed to run JSON.GET");
        println!("{res16}"); // >>> [["Deimos",{"crashes":0}]]
```



Beginning with Redis 8.8, the JSON data type supports the ability to force a particular type when storing floating point homogeneous arrays (FPHAs)using the `FPHA BF16|FP16|FP32|FP64` option to the [`JSON.SET`](https://redis.io/docs/latest/commands/json.set) command. Here's an example:

```
> JSON.SET fp_array $ '[[1,2,3,4e3],[5,6.0,7,8]]' FPHA FP16
OK
> JSON.GET fp_array $
"[[[1.0,2.0,3.0,4000.0],[5.0,6.0,7.0,8.0]]]"
```

The [`JSON.DEL`](https://redis.io/docs/latest/commands/json.del) command deletes any JSON value you specify with the `path` parameter.

You can manipulate arrays with a dedicated subset of JSON commands:

Array manipulation: Use JSON.ARRAPPEND to add elements, JSON.ARRINSERT to insert at positions, JSON.ARRTRIM to keep ranges, and JSON.ARRPOP to remove elements

**Difficulty:** Intermediate

**Builds upon:** arr

**Commands:** JSON.SET, JSON.ARRAPPEND, JSON.GET, JSON.ARRINSERT, JSON.ARRTRIM, JSON.ARRPOP

**Complexity:**
- JSON.SET: O(M+N)
- JSON.ARRAPPEND: O(1)
- JSON.GET: O(N)
- JSON.ARRINSERT: O(N)
- JSON.ARRTRIM: O(N)
- JSON.ARRPOP: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> JSON.SET riders $ []
OK
> JSON.ARRAPPEND riders $ '"Norem"'
1) (integer) 1
> JSON.GET riders $
"[[\"Norem\"]]"
> JSON.ARRINSERT riders $ 1 '"Prickett"' '"Royce"' '"Castilla"'
1) (integer) 4
> JSON.GET riders $
"[[\"Norem\",\"Prickett\",\"Royce\",\"Castilla\"]]"
> JSON.ARRTRIM riders $ 1 1
1) (integer) 1
> JSON.GET riders $
"[[\"Prickett\"]]"
> JSON.ARRPOP riders $
1) "\"Prickett\""
> JSON.ARRPOP riders $
1) (nil)
```

##### C#

```csharp
        bool res16 = db.JSON().Set("riders", "$", new object[] { });
        Console.WriteLine(res16);   // >>> True

        long?[] res17 = db.JSON().ArrAppend("riders", "$", "Norem");
        Console.WriteLine(string.Join(", ", res17));    // >>> 1

        RedisResult res18 = db.JSON().Get("riders", path: "$");
        Console.WriteLine(res18);   // >>> [["Norem"]]

        long?[] res19 = db.JSON().ArrInsert("riders", "$", 1, "Prickett", "Royce", "Castilla");
        Console.WriteLine(string.Join(", ", res19));    // >>> 4

        RedisResult res20 = db.JSON().Get("riders", path: "$");
        Console.WriteLine(res20);   // >>> [["Norem","Prickett","Royce","Castilla"]]

        long?[] res21 = db.JSON().ArrTrim("riders", "$", 1, 1);
        Console.WriteLine(string.Join(", ", res21));    // 1

        RedisResult res22 = db.JSON().Get("riders", path: "$");
        Console.WriteLine(res22);   // >>> [["Prickett"]]

        RedisResult[] res23 = db.JSON().ArrPop("riders", "$");
        Console.WriteLine(string.Join(", ", (object[])res23)); // >>> "Prickett"

        RedisResult[] res24 = db.JSON().ArrPop("riders", "$");
        Console.WriteLine(string.Join(", ", (object[])res24)); // >>> <Empty string>
```

##### Go

```go
	res16, err := rdb.JSONSet(ctx, "riders", "$", []interface{}{}).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res16) // >>> OK

	res17, err := rdb.JSONArrAppend(ctx, "riders", "$", "\"Norem\"").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res17) // >>> [1]

	res18, err := rdb.JSONGet(ctx, "riders", "$").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res18) // >>> [["Norem"]]

	res19, err := rdb.JSONArrInsert(ctx, "riders", "$", 1,
		"\"Prickett\"", "\"Royce\"", "\"Castilla\"",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res19) // [3]

	res20, err := rdb.JSONGet(ctx, "riders", "$").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res20) // >>> [["Norem", "Prickett", "Royce", "Castilla"]]

	rangeStop := 1

	res21, err := rdb.JSONArrTrimWithArgs(ctx, "riders", "$",
		&redis.JSONArrTrimArgs{Start: 1, Stop: &rangeStop},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res21) // >>> [1]

	res22, err := rdb.JSONGet(ctx, "riders", "$").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res22) // >>> [["Prickett"]]

	res23, err := rdb.JSONArrPop(ctx, "riders", "$", -1).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res23) // >>> [["Prickett"]]

	res24, err := rdb.JSONArrPop(ctx, "riders", "$", -1).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res24) // []
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> arr2 = asyncCommands.jsonSet("riders", JsonPath.ROOT_PATH, parser.createJsonArray())
                    .thenCompose(r -> {
                        System.out.println(r); // >>> OK

                        return asyncCommands.jsonArrinsert("riders", JsonPath.ROOT_PATH, 0,
                                parser.createJsonValue("\"Norem\""));
                    }).thenCompose(res11 -> {
                        System.out.println(res11); // >>> [1]

                        return asyncCommands.jsonGet("riders", JsonPath.ROOT_PATH);
                    })

                    .thenCompose(res12 -> {
                        System.out.println(res12); // >>> ["Norem"]

                        return asyncCommands.jsonArrinsert("riders", JsonPath.ROOT_PATH, 1,
                                parser.createJsonValue("\"Prickett\""), parser.createJsonValue("\"Royce\""),
                                parser.createJsonValue("\"Castilla\""));
                    }).thenCompose(res13 -> {
                        System.out.println(res13); // >>> [4]

                        return asyncCommands.jsonGet("riders", JsonPath.ROOT_PATH);
                    }).thenCompose(res14 -> {
                        System.out.println(res14); // >>> ["Norem","Prickett","Royce","Castilla"]
                        //
                        return asyncCommands.jsonArrtrim("riders", JsonPath.ROOT_PATH, new JsonRangeArgs().start(1).stop(1));
                    }).thenCompose(res15 -> {
                        System.out.println(res15); // >>> [1]

                        return asyncCommands.jsonGet("riders", JsonPath.ROOT_PATH);
                    }).thenCompose(res16 -> {
                        System.out.println(res16); // >>> [[["Prickett"]]]
                        return asyncCommands.jsonArrpop("riders", JsonPath.ROOT_PATH, 0);
                    }).thenCompose(res17 -> {
                        System.out.println(res17); // >>> ["Prickett"]
                        return asyncCommands.jsonArrpop("riders", JsonPath.ROOT_PATH);
                    })
                    .thenAccept(System.out::println)
                    // >>> null
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> arr2 = reactiveCommands.jsonSet("riders", JsonPath.ROOT_PATH, parser.createJsonArray()).doOnNext(r -> {
                System.out.println(r); // >>> OK
            }).flatMap(r -> reactiveCommands.jsonArrinsert("riders", JsonPath.ROOT_PATH, 0, parser.createJsonValue("\"Norem\""))
                    .collectList()).doOnNext(res11 -> {
                        System.out.println(res11); // >>> [1]
                    }).flatMap(res11 -> reactiveCommands.jsonGet("riders", JsonPath.ROOT_PATH).collectList())
                    .doOnNext(res12 -> {
                        System.out.println(res12); // >>> ["Norem"]
                    })
                    .flatMap(
                            res12 -> reactiveCommands
                                    .jsonArrinsert("riders", JsonPath.ROOT_PATH, 1, parser.createJsonValue("\"Prickett\""),
                                            parser.createJsonValue("\"Royce\""), parser.createJsonValue("\"Castilla\""))
                                    .collectList())
                    .doOnNext(res13 -> {
                        System.out.println(res13); // >>> [4]
                    }).flatMap(res13 -> reactiveCommands.jsonGet("riders", JsonPath.ROOT_PATH).collectList())
                    .doOnNext(System.out::println) // >>> [["Norem","Prickett","Royce","Castilla"]]
                    .flatMap(res14 -> reactiveCommands
                            .jsonArrtrim("riders", JsonPath.ROOT_PATH, new JsonRangeArgs().start(1).stop(1)).collectList())
                    .doOnNext(res15 -> {
                        System.out.println(res15); // >>> [1]
                    }).flatMap(res15 -> reactiveCommands.jsonGet("riders", JsonPath.ROOT_PATH).collectList())
                    .doOnNext(res16 -> {
                        System.out.println(res16); // >>> [[["Prickett"]]]
                    }).flatMap(res16 -> reactiveCommands.jsonArrpop("riders", JsonPath.ROOT_PATH, 0).collectList())
                    .doOnNext(res17 -> {
                        System.out.println(res17); // >>> ["Prickett"]
                    }).flatMap(res17 -> reactiveCommands.jsonArrpop("riders", JsonPath.ROOT_PATH).collectList())
                    .doOnNext(System.out::println) // >>> null
                    .then();
```

##### Java (Synchronous - Jedis)

```java
        String res16 = jedis.jsonSet("riders", new Path2("$"), new JSONArray());
        System.out.println(res16);  // >>> OK

        List<Long> res17 = jedis.jsonArrAppendWithEscape("riders", new Path2("$"), "Norem");
        System.out.println(res17);  // >>> [1]

        Object res18 = jedis.jsonGet("riders", new Path2("$"));
        System.out.println(res18);  // >>> [["Norem"]]

        List<Long> res19 = jedis.jsonArrInsertWithEscape(
            "riders", new Path2("$"), 1, "Prickett", "Royce", "Castilla"
        );
        System.out.println(res19);  // >>> [4]

        Object res20 = jedis.jsonGet("riders", new Path2("$"));
        System.out.println(res20);
        // >>> [["Norem","Prickett","Royce","Castilla"]]
        
        List<Long> res21 = jedis.jsonArrTrim("riders", new Path2("$"), 1, 1);
        System.out.println(res21);  // >>> [1]

        Object res22 = jedis.jsonGet("riders", new Path2("$"));
        System.out.println(res22);  // >>> [["Prickett"]]

        Object res23 = jedis.jsonArrPop("riders", new Path2("$"));
        System.out.println(res23);  // >>> [Prickett]

        Object res24 = jedis.jsonArrPop("riders", new Path2("$"));
        System.out.println(res24);  // >>> [null]
```

##### JavaScript (Node.js)

```javascript
const res16 = await client.json.set("riders", "$", []);
console.log(res16); //  OK

const res17 = await client.json.arrAppend("riders", "$", "Norem");
console.log(res17); //  [1]

const res18 = await client.json.get("riders", { path: "$" });
console.log(res18); //  [[ 'Norem' ]]

const res19 = await client.json.arrInsert("riders", "$", 1, "Prickett", "Royse", "Castilla");
console.log(res19); //  [4]

const res20 = await client.json.get("riders", { path: "$" });
console.log(res20); //  [[ 'Norem', 'Prickett', 'Royse', 'Castilla' ]]

const res21 = await client.json.arrTrim("riders", "$", 1, 1);
console.log(res21); //  [1]

const res22 = await client.json.get("riders", { path: "$" });
console.log(res22); //  [[ 'Prickett' ]]

const res23 = await client.json.arrPop("riders", { path: "$" });
console.log(res23); //  [ 'Prickett' ]

const res24 = await client.json.arrPop("riders", { path: "$" });
console.log(res24); //  [null]
```

##### PHP

```php
        $res16 = $r->jsonset('riders', '$', '[]');
        echo $res16 . PHP_EOL;
        // >>> OK

        $res17 = $r->jsonarrappend('riders', '$', '"Norem"');
        echo json_encode($res17) . PHP_EOL;
        // >>> [1]

        $res18 = $r->jsonget('riders', '', '', '', '$');
        echo $res18 . PHP_EOL;
        // >>> ["Norem"]

        $res19 = $r->jsonarrinsert('riders', '$', 1, '"Prickett"', '"Royce"', '"Castilla"');
        echo json_encode($res19) . PHP_EOL;
        // >>> [4]

        $res20 = $r->jsonget('riders', '', '', '', '$');
        echo $res20 . PHP_EOL;
        // >>> ["Norem","Prickett","Royce","Castilla"]

        $res21 = $r->jsonarrtrim('riders', '$', 1, 1);
        echo json_encode($res21) . PHP_EOL;
        // >>> [1]

        $res22 = $r->jsonget('riders', '', '', '', '$');
        echo $res22 . PHP_EOL;
        // >>> ["Prickett"]

        $res23 = $r->jsonarrpop('riders', '$');
        echo json_encode($res23) . PHP_EOL;
        // >>> ["\"Prickett\""]

        $res24 = $r->jsonarrpop('riders', '$');
        echo json_encode($res24) . PHP_EOL;
        // >>> [null]
```

##### Python

```python
res16 = r.json().set("riders", "$", [])
print(res16)  # >>> True

res17 = r.json().arrappend("riders", "$", "Norem")
print(res17)  # >>> [1]

res18 = r.json().get("riders", "$")
print(res18)  # >>> [['Norem']]

res19 = r.json().arrinsert("riders", "$", 1, "Prickett", "Royce", "Castilla")
print(res19)  # >>> [4]

res20 = r.json().get("riders", "$")
print(res20)  # >>> [['Norem', 'Prickett', 'Royce', 'Castilla']]

res21 = r.json().arrtrim("riders", "$", 1, 1)
print(res21)  # >>> [1]

res22 = r.json().get("riders", "$")
print(res22)  # >>> [['Prickett']]

res23 = r.json().arrpop("riders", "$")
print(res23)  # >>> ['"Prickett"']

res24 = r.json().arrpop("riders", "$")
print(res24)  # >>> [None]
```

##### Ruby

```ruby
res16 = r.json_set('riders', '$', [])
puts res16 # >>> OK

res17 = r.json_arrappend('riders', '$', 'Norem')
p res17 # >>> [1]

res18 = r.json_get('riders', '$')
p res18 # >>> [["Norem"]]

res19 = r.json_arrinsert('riders', '$', 1, 'Prickett', 'Royce', 'Castilla')
p res19 # >>> [4]

res20 = r.json_get('riders', '$')
p res20 # >>> [["Norem", "Prickett", "Royce", "Castilla"]]

res21 = r.json_arrtrim('riders', '$', 1, 1)
p res21 # >>> [1]

res22 = r.json_get('riders', '$')
p res22 # >>> [["Prickett"]]

res23 = r.json_arrpop('riders', '$')
p res23 # >>> ["Prickett"]

res24 = r.json_arrpop('riders', '$')
p res24 # >>> [nil]

# json_arrappend also takes a pre-encoded JSON value with raw: true.
res_raw4 = r.json_arrappend('riders', '$', '"Castilla"', raw: true)
p res_raw4 # >>> [1]
```

##### Rust (Asynchronous)

```rust
        let res17: bool = r
            .json_set("riders", "$", &json!([]))
            .await
            .expect("Failed to run JSON.SET");
        print_set_result(res17); // >>> OK

        let res18: Value = r
            .json_arr_append("riders", "$", &json!("Norem"))
            .await
            .expect("Failed to run JSON.ARRAPPEND");
        print_redis_value(&res18); // >>> [1]

        let res19: String = r
            .json_get("riders", "$")
            .await
            .expect("Failed to run JSON.GET");
        println!("{res19}"); // >>> [["Norem"]]

        let res20: Value = cmd("JSON.ARRINSERT")
            .arg("riders")
            .arg("$")
            .arg(1)
            .arg("\"Prickett\"")
            .arg("\"Royce\"")
            .arg("\"Castilla\"")
            .query_async(&mut r)
            .await
            .expect("Failed to run JSON.ARRINSERT");
        print_redis_value(&res20); // >>> [4]

        let res21: String = r
            .json_get("riders", "$")
            .await
            .expect("Failed to run JSON.GET");
        println!("{res21}"); // >>> [["Norem","Prickett","Royce","Castilla"]]

        let res22: Value = r
            .json_arr_trim("riders", "$", 1, 1)
            .await
            .expect("Failed to run JSON.ARRTRIM");
        print_redis_value(&res22); // >>> [1]

        let res23: String = r
            .json_get("riders", "$")
            .await
            .expect("Failed to run JSON.GET");
        println!("{res23}"); // >>> [["Prickett"]]

        let res24: Value = r
            .json_arr_pop("riders", "$", -1)
            .await
            .expect("Failed to run JSON.ARRPOP");
        print_redis_value(&res24); // >>> ["Prickett"]

        let res25: Value = r
            .json_arr_pop("riders", "$", -1)
            .await
            .expect("Failed to run JSON.ARRPOP");
        print_redis_value(&res25); // >>> [null]
```

##### Rust (Synchronous)

```rust
        let res17: bool = r
            .json_set("riders", "$", &json!([]))
            .expect("Failed to run JSON.SET");
        print_set_result(res17); // >>> OK

        let res18: Value = r
            .json_arr_append("riders", "$", &json!("Norem"))
            .expect("Failed to run JSON.ARRAPPEND");
        print_redis_value(&res18); // >>> [1]

        let res19: String = r.json_get("riders", "$").expect("Failed to run JSON.GET");
        println!("{res19}"); // >>> [["Norem"]]

        let res20: Value = cmd("JSON.ARRINSERT")
            .arg("riders")
            .arg("$")
            .arg(1)
            .arg("\"Prickett\"")
            .arg("\"Royce\"")
            .arg("\"Castilla\"")
            .query(&mut r)
            .expect("Failed to run JSON.ARRINSERT");
        print_redis_value(&res20); // >>> [4]

        let res21: String = r.json_get("riders", "$").expect("Failed to run JSON.GET");
        println!("{res21}"); // >>> [["Norem","Prickett","Royce","Castilla"]]

        let res22: Value = r
            .json_arr_trim("riders", "$", 1, 1)
            .expect("Failed to run JSON.ARRTRIM");
        print_redis_value(&res22); // >>> [1]

        let res23: String = r.json_get("riders", "$").expect("Failed to run JSON.GET");
        println!("{res23}"); // >>> [["Prickett"]]

        let res24: Value = r
            .json_arr_pop("riders", "$", -1)
            .expect("Failed to run JSON.ARRPOP");
        print_redis_value(&res24); // >>> ["Prickett"]

        let res25: Value = r
            .json_arr_pop("riders", "$", -1)
            .expect("Failed to run JSON.ARRPOP");
        print_redis_value(&res25); // >>> [null]
```



JSON objects also have their own commands:

Object operations: Inspect JSON objects using JSON.OBJLEN to count fields and JSON.OBJKEYS to retrieve all keys

**Difficulty:** Intermediate

**Builds upon:** arr

**Commands:** JSON.SET, JSON.OBJLEN, JSON.OBJKEYS

**Complexity:**
- JSON.SET: O(M+N)
- JSON.OBJLEN: O(1)
- JSON.OBJKEYS: O(1)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> JSON.SET bike:1 $ '{"model": "Deimos", "brand": "Ergonom", "price": 4972}'
OK
> JSON.OBJLEN bike:1 $
1) (integer) 3
> JSON.OBJKEYS bike:1 $
1) 1) "model"
   2) "brand"
   3) "price"
```

##### C#

```csharp
        bool res25 = db.JSON().Set("bike:1", "$",
            new { model = "Deimos", brand = "Ergonom", price = 4972 }
        );
        Console.WriteLine(res25);   // >>> True

        long?[] res26 = db.JSON().ObjLen("bike:1", "$");
        Console.WriteLine(string.Join(", ", res26));    // >>> 3

        IEnumerable<HashSet<string>> res27 = db.JSON().ObjKeys("bike:1", "$");
        Console.WriteLine(
            string.Join(", ", res27.Select(b => $"{string.Join(", ", b.Select(c => $"{c}"))}"))
        ); // >>> model, brand, price
```

##### Go

```go
	res25, err := rdb.JSONSet(ctx, "bike:1", "$",
		map[string]interface{}{
			"model": "Deimos",
			"brand": "Ergonom",
			"price": 4972,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res25) // >>> OK

	res26, err := rdb.JSONObjLen(ctx, "bike:1", "$").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(*res26[0]) // >>> 3

	res27, err := rdb.JSONObjKeys(ctx, "bike:1", "$").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res27) // >>> [brand model price]
```

##### Java (Asynchronous - Lettuce)

```java
            JsonObject bikeObj = parser.createJsonObject().put("model", parser.createJsonValue("\"Deimos\""))
                    .put("brand", parser.createJsonValue("\"Ergonom\"")).put("price", parser.createJsonValue("\"4972\""));

            CompletableFuture<Void> obj = asyncCommands.jsonSet("bike:1", JsonPath.ROOT_PATH, bikeObj).thenCompose(r -> {
                System.out.println(r); // >>> OK

                return asyncCommands.jsonObjlen("bike:1", JsonPath.ROOT_PATH);
            }).thenCompose(res18 -> {
                System.out.println(res18); // >>> [3]

                return asyncCommands.jsonObjkeys("bike:1", JsonPath.ROOT_PATH);
            })
                    .thenAccept(System.out::println)
                    // >>> [model, brand, price]
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            JsonObject bikeObj = parser.createJsonObject().put("model", parser.createJsonValue("\"Deimos\""))
                    .put("brand", parser.createJsonValue("\"Ergonom\"")).put("price", parser.createJsonValue("\"4972\""));

            Mono<Void> obj = reactiveCommands.jsonSet("bike:1", JsonPath.ROOT_PATH, bikeObj).doOnNext(r -> {
                System.out.println(r); // >>> OK
            }).flatMap(r -> reactiveCommands.jsonObjlen("bike:1", JsonPath.ROOT_PATH).collectList()).doOnNext(res18 -> {
                System.out.println(res18); // >>> [3]
            }).flatMap(res18 -> reactiveCommands.jsonObjkeys("bike:1", JsonPath.ROOT_PATH).collectList())
                    .doOnNext(System.out::println) // >>> [model, brand, price]
                    .then();
```

##### Java (Synchronous - Jedis)

```java
        String res25 = jedis.jsonSet("bike:1", new Path2("$"),
            new JSONObject()
                .put("model", "Deimos")
                .put("brand", "Ergonom")
                .put("price", 4972)
        );
        System.out.println(res25);  // >>> OK

        List<Long> res26 = jedis.jsonObjLen("bike:1", new Path2("$"));
        System.out.println(res26);  // >>> [3]

        List<List<String>> res27 = jedis.jsonObjKeys("bike:1", new Path2("$"));
        System.out.println(res27);  // >>> [[price, model, brand]]
```

##### JavaScript (Node.js)

```javascript
const res25 = await client.json.set(
  "bike:1", "$", {
    "model": "Deimos",
    "brand": "Ergonom",
    "price": 4972
  }
);
console.log(res25); //  OK

const res26 = await client.json.objLen("bike:1", { path: "$" });
console.log(res26); //  [3]

const res27 = await client.json.objKeys("bike:1", { path: "$" });
console.log(res27); //  [['model', 'brand', 'price']]
```

##### PHP

```php
        $bike1 = json_encode([
            'model' => 'Deimos',
            'brand' => 'Ergonom',
            'price' => 4972,
        ], JSON_THROW_ON_ERROR);
        $res25 = $r->jsonset('bike:1', '$', $bike1);
        echo $res25 . PHP_EOL;
        // >>> OK

        $res26 = $r->jsonobjlen('bike:1', '$');
        echo json_encode($res26) . PHP_EOL;
        // >>> [3]

        $res27 = $r->jsonobjkeys('bike:1', '$');
        echo json_encode($res27) . PHP_EOL;
        // >>> [["model","brand","price"]]
```

##### Python

```python
res25 = r.json().set(
    "bike:1", "$", {"model": "Deimos", "brand": "Ergonom", "price": 4972}
)
print(res25)  # >>> True

res26 = r.json().objlen("bike:1", "$")
print(res26)  # >>> [3]

res27 = r.json().objkeys("bike:1", "$")
print(res27)  # >>> [['model', 'brand', 'price']]
```

##### Ruby

```ruby
res25 = r.json_set('bike:1', '$', { 'model' => 'Deimos', 'brand' => 'Ergonom', 'price' => 4972 })
puts res25 # >>> OK

res26 = r.json_objlen('bike:1', '$')
p res26 # >>> [3]

res27 = r.json_objkeys('bike:1', '$')
p res27 # >>> [["model", "brand", "price"]]

# raw: true returns the object as unparsed JSON text.
res_raw5 = r.json_get('bike:1', '$', raw: true)
puts res_raw5 # >>> [{"model":"Deimos","brand":"Ergonom","price":4972}]  (a JSON string)
```

##### Rust (Asynchronous)

```rust
        let res26: bool = r
            .json_set(
                "bike:1",
                "$",
                &json!({"model": "Deimos", "brand": "Ergonom", "price": 4972}),
            )
            .await
            .expect("Failed to run JSON.SET");
        print_set_result(res26); // >>> OK

        let res27: Value = r
            .json_obj_len("bike:1", "$")
            .await
            .expect("Failed to run JSON.OBJLEN");
        print_redis_value(&res27); // >>> [3]

        let res28: Value = r
            .json_obj_keys("bike:1", "$")
            .await
            .expect("Failed to run JSON.OBJKEYS");
        print_redis_value(&res28); // >>> [["brand","model","price"]]
```

##### Rust (Synchronous)

```rust
        let res26: bool = r
            .json_set(
                "bike:1",
                "$",
                &json!({"model": "Deimos", "brand": "Ergonom", "price": 4972}),
            )
            .expect("Failed to run JSON.SET");
        print_set_result(res26); // >>> OK

        let res27: Value = r
            .json_obj_len("bike:1", "$")
            .expect("Failed to run JSON.OBJLEN");
        print_redis_value(&res27); // >>> [3]

        let res28: Value = r
            .json_obj_keys("bike:1", "$")
            .expect("Failed to run JSON.OBJKEYS");
        print_redis_value(&res28); // >>> [["brand","model","price"]]
```



## Format CLI output

The CLI has a raw output mode that lets you add formatting to the output from
[`JSON.GET`](https://redis.io/docs/latest/commands/json.get) to make
it more readable. To use this, run `redis-cli` with the `--raw` option
and include formatting keywords such as `INDENT`, `NEWLINE`, and `SPACE`
with [`JSON.GET`](https://redis.io/docs/latest/commands/json.get):

```bash
$ redis-cli --raw
> JSON.GET obj INDENT "\t" NEWLINE "\n" SPACE " " $
[
	{
		"name": "Leonard Cohen",
		"lastSeen": 1478476800,
		"loggedOut": true
	}
]
```

## Enable Redis JSON

The Redis JSON data type is part of Redis Open Source and it is also available in Redis Software and Redis Cloud.
See
[Install Redis Open Source](https://redis.io/docs/latest/operate/oss_and_stack/install/install-stack) or
[Install Redis Software](https://redis.io/docs/latest/operate/rs/installing-upgrading/install)
for full installation instructions.

## Limitation

A JSON value passed to a command can have a depth of up to 128. If you pass to a command a JSON value that contains an object or an array with a nesting level of more than 128, the command returns an error.

## Further information

Read the other pages in this section to learn more about Redis JSON

