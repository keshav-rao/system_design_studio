# Redis bitfields

```json metadata
{
  "schema_version": 2,
  "title": "Redis bitfields",
  "description": "Introduction to Redis bitfields",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"example","title":"Example"},{"id":"performance","title":"Performance"}]}

,
  "codeExamples": [{"codetabsId":"bitfield_tutorial-stepbf","commands":[{"acl_categories":["@write","@bitmap","@slow"],"complexity":"O(1)","name":"BITFIELD"}],"description":"Bitfield operations: Use BITFIELD to atomically set, increment, and get integer values of arbitrary bit length when you need to manage multiple counters efficiently","difficulty":"intermediate","id":"bf","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_bitfield_tutorial-stepbf"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_bitfield_tutorial-stepbf"},{"id":"Node-js","panelId":"panel_Nodejs_bitfield_tutorial-stepbf"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_bitfield_tutorial-stepbf"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_bitfield_tutorial-stepbf"}]}]
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


### Bitmap/bitfield command summary

**7 commands in this group:**

[View all bitmap commands](https://redis.io/commands/?group=bitmap)

| Command | Summary | Complexity | Since |
|---------|---------|------------|-------|
| [BITCOUNT](https://redis.io/commands/bitcount/) | Counts the number of set bits (population counting) in a string. | O(N) | 2.6.0 |
| [BITFIELD](https://redis.io/commands/bitfield/) | Performs arbitrary bitfield integer operations on strings. | O(1) for each subcommand specified | 3.2.0 |
| [BITFIELD_RO](https://redis.io/commands/bitfield_ro/) | Performs arbitrary read-only bitfield integer operations on strings. | O(1) for each subcommand specified | 6.0.0 |
| [BITOP](https://redis.io/commands/bitop/) | Performs bitwise operations on multiple strings, and stores the result. | O(N) | 2.6.0 |
| [BITPOS](https://redis.io/commands/bitpos/) | Finds the first set (1) or clear (0) bit in a string. | O(N) | 2.8.7 |
| [GETBIT](https://redis.io/commands/getbit/) | Returns a bit value by offset. | O(1) | 2.2.0 |
| [SETBIT](https://redis.io/commands/setbit/) | Sets or clears the bit at offset of the string value. Creates the key if it doesn't exist. | O(1) | 2.2.0 |



Redis bitfields let you set, increment, and get integer values of arbitrary bit length.
For example, you can operate on anything from unsigned 1-bit integers to signed 63-bit integers.

These values are stored using binary-encoded Redis strings.
Bitfields support atomic read, write and increment operations, making them a good choice for managing counters and similar numerical values.

## Example

Suppose you want to maintain two metrics for various bicycles: the current price and the number of owners over time. You can represent these counters with a 32-bit wide bitfield for each bike.

* Bike 1 initially costs 1,000 (counter in offset 0) and has never had an owner. After being sold, it's now considered used and the price instantly drops to reflect its new condition, and it now has an owner (offset 1). After quite some time, the bike becomes a classic. The original owner sells it for a profit, so the price goes up and the number of owners does as well.Finally, you can look at the bike's current price and number of owners.

Bitfield operations: Use BITFIELD to atomically set, increment, and get integer values of arbitrary bit length when you need to manage multiple counters efficiently

**Difficulty:** Intermediate

**Commands:** BITFIELD

**Complexity:**
- BITFIELD: O(1)

**Available in:** Redis CLI, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python

##### Redis CLI

```
> BITFIELD bike:1:stats SET u32 #0 1000
1) (integer) 0
> BITFIELD bike:1:stats INCRBY u32 #0 -50 INCRBY u32 #1 1
1) (integer) 950
2) (integer) 1
> BITFIELD bike:1:stats INCRBY u32 #0 500 INCRBY u32 #1 1
1) (integer) 1450
2) (integer) 2
> BITFIELD bike:1:stats GET u32 #0 GET u32 #1
1) (integer) 1450
2) (integer) 2
```

##### Go

```go
	res1, err := rdb.BitField(ctx, "bike:1:stats",
		"set", "u32", "#0", "1000",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // >>> [0]

	res2, err := rdb.BitField(ctx,
		"bike:1:stats",
		"incrby", "u32", "#0", "-50",
		"incrby", "u32", "#1", "1",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2) // >>> [950 1]

	res3, err := rdb.BitField(ctx,
		"bike:1:stats",
		"incrby", "u32", "#0", "500",
		"incrby", "u32", "#1", "1",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3) // >>> [1450 2]

	res4, err := rdb.BitField(ctx, "bike:1:stats",
		"get", "u32", "#0",
		"get", "u32", "#1",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4) // >>> [1450 2]
```

##### Java (Synchronous - Jedis)

```java
        List<Long> res1 = jedis.bitfield("bike:1:stats", "SET", "u32", "#0", "1000");
        System.out.println(res1);   // >>> [0]

        List<Long> res2 = jedis.bitfield("bike:1:stats", "INCRBY", "u32", "#0", "-50", "INCRBY", "u32", "#1", "1");
        System.out.println(res2);   // >>> [950, 1]

        List<Long> res3 = jedis.bitfield("bike:1:stats", "INCRBY", "u32", "#0", "500", "INCRBY", "u32", "#1", "1");
        System.out.println(res3);   // >>> [1450, 2]

        List<Long> res4 = jedis.bitfield("bike:1:stats", "GET", "u32", "#0", "GET", "u32", "#1");
        System.out.println(res4);   // >>> [1450, 2]
```

##### JavaScript (Node.js)

```javascript
let res1 = await client.bitField("bike:1:stats", [{
  operation: 'SET',
  encoding: 'u32',
  offset: '#0',
  value: 1000
}]);
console.log(res1);  // >>> [0]

let res2 = await client.bitField('bike:1:stats', [
  {
    operation: 'INCRBY',
    encoding: 'u32',
    offset: '#0',
    increment: -50
  },
  {
    operation: 'INCRBY',
    encoding: 'u32',
    offset: '#1',
    increment: 1
  }
]);
console.log(res2);  // >>> [950, 1]

let res3 = await client.bitField('bike:1:stats', [
  {
    operation: 'INCRBY',
    encoding: 'u32',
    offset: '#0',
    increment: 500
  },
  {
    operation: 'INCRBY',
    encoding: 'u32',
    offset: '#1',
    increment: 1
  }
]);
console.log(res3);  // >>> [1450, 2]

let res4 = await client.bitField('bike:1:stats', [
  {
    operation: 'GET',
    encoding: 'u32',
    offset: '#0'
  },
  {
    operation: 'GET',
    encoding: 'u32',
    offset: '#1'
  }
]);
console.log(res4);  // >>> [1450, 2]
```

##### Python

```python
bf = r.bitfield("bike:1:stats")
res1 = bf.set("u32", "#0", 1000).execute()
print(res1)  # >>> [0]

res2 = bf.incrby("u32", "#0", -50).incrby("u32", "#1", 1).execute()
print(res2)  # >>> [950, 1]

res3 = bf.incrby("u32", "#0", 500).incrby("u32", "#1", 1).execute()
print(res3)  # >>> [1450, 2]

res4 = bf.get("u32", "#0").get("u32", "#1").execute()
print(res4)  # >>> [1450, 2]
```




## Performance

[`BITFIELD`](https://redis.io/docs/latest/commands/bitfield) is O(n), where _n_ is the number of counters accessed.

