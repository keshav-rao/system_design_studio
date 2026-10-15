# Handle command results efficiently

```json metadata
{
  "schema_version": 2,
  "title": "Handle command results efficiently",
  "description": "Scan go-redis command results into Go values and use buffers for large string payloads.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"initialize","title":"Initialize"},{"id":"scan-hashes-into-structs","title":"Scan hashes into structs"},{"id":"scan-lists-into-slices","title":"Scan lists into slices"},{"id":"use-byte-buffers","title":"Use byte buffers"},{"id":"more-information","title":"More information"}]}

,
  "codeExamples": [{"codetabsId":"go_scan_buffer-stepimport","description":"Foundational: Import go-redis and supporting packages for scanning and buffer examples","difficulty":"beginner","id":"import","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_go_scan_buffer-stepimport"}]},{"codetabsId":"go_scan_buffer-stepconnect","description":"Foundational: Connect to Redis before running scan and buffer examples","difficulty":"beginner","id":"connect","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_go_scan_buffer-stepconnect"}]},{"codetabsId":"go_scan_buffer-stepscan_hash","description":"Structured results: Scan all hash fields into a Go struct using redis field tags","difficulty":"beginner","id":"scan_hash","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_go_scan_buffer-stepscan_hash"}]},{"buildsUpon":["scan_hash"],"codetabsId":"go_scan_buffer-stepscan_hash_subset","description":"Structured results: Scan selected hash fields and leave missing fields at their zero values","difficulty":"intermediate","id":"scan_hash_subset","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_go_scan_buffer-stepscan_hash_subset"}]},{"codetabsId":"go_scan_buffer-stepscan_list","description":"Structured results: Convert a list command result into a typed Go slice with ScanSlice","difficulty":"beginner","id":"scan_list","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_go_scan_buffer-stepscan_list"}]},{"codetabsId":"go_scan_buffer-stepbuffer_round_trip","description":"Buffer optimization: Write and read Redis string values using caller-owned byte buffers","difficulty":"intermediate","id":"buffer_round_trip","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_go_scan_buffer-stepbuffer_round_trip"}]},{"buildsUpon":["buffer_round_trip"],"codetabsId":"go_scan_buffer-stepbuffer_too_small","description":"Buffer sizing: Detect and handle a buffer that is too small for the Redis value","difficulty":"intermediate","id":"buffer_too_small","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_go_scan_buffer-stepbuffer_too_small"}]}]
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


`go-redis` can convert command results directly into Go values. This is useful
when you want to keep application code close to your domain types instead of
working with strings and maps everywhere. You can scan [hash](https://redis.io/docs/latest/develop/data-types/hashes)
results into structs, scan list-style command results into slices, and use
byte buffers for large [string](https://redis.io/docs/latest/develop/data-types/strings)
values.

## Initialize

Import the packages you need:

Foundational: Import go-redis and supporting packages for scanning and buffer examples

**Difficulty:** Beginner

**Available in:** Go

##### Go

```go
import (
	"context"
	"fmt"
	"strings"

	"github.com/redis/go-redis/v9"
)

```



Connect to Redis:

Foundational: Connect to Redis before running scan and buffer examples

**Difficulty:** Beginner

**Available in:** Go

##### Go

```go
	ctx := context.Background()

	rdb := redis.NewClient(&redis.Options{
		Addr:     "localhost:6379",
		Password: "", // no password
		DB:       0,  // use default DB
		Protocol: 2,
	})
	defer rdb.Close()
```



## Scan hashes into structs

Use struct tags of the form `redis:"field"` to map Redis hash fields to Go
struct fields. The `Scan()` method converts matching fields to the destination
types and returns an error if a conversion fails.

The following example stores a hash with [`HSET`](https://redis.io/docs/latest/commands/hset)
and then scans the result of [`HGETALL`](https://redis.io/docs/latest/commands/hgetall)
into a `Bike` struct:

Structured results: Scan all hash fields into a Go struct using redis field tags

**Difficulty:** Beginner

**Available in:** Go

##### Go

```go
	type Bike struct {
		Model string `redis:"model"`
		Brand string `redis:"brand"`
		Price int    `redis:"price"`
	}

	if err := rdb.HSet(ctx, "scanbuf:bike:1",
		"model", "Deimos",
		"brand", "Ergonom",
		"price", 4972,
	).Err(); err != nil {
		panic(err)
	}

	var bike Bike
	if err := rdb.HGetAll(ctx, "scanbuf:bike:1").Scan(&bike); err != nil {
		panic(err)
	}

	fmt.Printf("Model: %s, brand: %s, price: $%d\n",
		bike.Model, bike.Brand, bike.Price)
	// >>> Model: Deimos, brand: Ergonom, price: $4972
```



You can also scan a subset of fields with [`HMGET`](https://redis.io/docs/latest/commands/hmget).
Fields that are not returned keep their Go zero values:

Structured results: Scan selected hash fields and leave missing fields at their zero values

**Difficulty:** Intermediate

**Builds upon:** scan_hash

**Available in:** Go

##### Go

```go
	type BikeStock struct {
		Model string `redis:"model"`
		Stock int    `redis:"stock"`
		Price int    `redis:"price"`
	}

	var partial BikeStock
	if err := rdb.HMGet(ctx, "scanbuf:bike:1", "model", "stock").Scan(&partial); err != nil {
		panic(err)
	}

	fmt.Printf("Model: %s, stock: %d, price: $%d\n",
		partial.Model, partial.Stock, partial.Price)
	// >>> Model: Deimos, stock: 0, price: $0
```



## Scan lists into slices

Commands that return a list of strings, such as [`LRANGE`](https://redis.io/docs/latest/commands/lrange),
can use `ScanSlice()` to convert the result into a typed Go slice:

Structured results: Convert a list command result into a typed Go slice with ScanSlice

**Difficulty:** Beginner

**Available in:** Go

##### Go

```go
	if err := rdb.RPush(ctx, "scanbuf:stock", 3, 4, 5).Err(); err != nil {
		panic(err)
	}

	var stockCounts []int
	if err := rdb.LRange(ctx, "scanbuf:stock", 0, -1).ScanSlice(&stockCounts); err != nil {
		panic(err)
	}

	fmt.Println("Stock counts:", stockCounts)
	// >>> Stock counts: [3 4 5]
```



## Use byte buffers

For large string payloads, you can avoid creating a new string for every read by
providing a caller-owned byte buffer. Use `SetFromBuffer()` to write a `[]byte`
value and `GetToBuffer()` to read the value into an existing buffer.

> [!NOTE]
> The buffer APIs require `github.com/redis/go-redis/v9` v9.21.0
> or later.
&nbsp;

Buffer optimization: Write and read Redis string values using caller-owned byte buffers

**Difficulty:** Intermediate

**Available in:** Go

##### Go

```go
	payload := []byte("compact bike data")

	if err := rdb.SetFromBuffer(ctx, "scanbuf:payload", payload).Err(); err != nil {
		panic(err)
	}
	fmt.Println("OK") // >>> OK

	buf := make([]byte, len(payload))
	cmd := rdb.GetToBuffer(ctx, "scanbuf:payload", buf)
	n, err := cmd.Result()
	if err != nil {
		panic(err)
	}

	fmt.Printf("Read %d bytes: %s\n", n, string(cmd.Bytes()))
	// >>> Read 17 bytes: compact bike data
```



`GetToBuffer()` returns a `*redis.ZeroCopyStringCmd`. Use `Val()` or `Result()`
to get the number of bytes read, `Bytes()` to access the populated slice
(`buf[:n]`), and `Err()` to check for errors such as `redis.Nil` when the key
does not exist.

> [!NOTE]
> `GetToBuffer()` requires a buffer large enough to hold the whole value. It also
> opts out of automatic retries because a failed read might already have written
> partial data into your buffer. If a buffer is too small, `Err()` reports a
> `buffer too small` error.

The following example shows how to detect a buffer that is too small:

Buffer sizing: Detect and handle a buffer that is too small for the Redis value

**Difficulty:** Intermediate

**Builds upon:** buffer_round_trip

**Available in:** Go

##### Go

```go
	smallBuf := make([]byte, 4)
	smallCmd := rdb.GetToBuffer(ctx, "scanbuf:payload", smallBuf)

	if err := smallCmd.Err(); err != nil {
		if strings.Contains(err.Error(), "buffer too small") {
			fmt.Println("Buffer too small")
		} else {
			panic(err)
		}
	}
	// >>> Buffer too small
```



`SetFromBuffer()` does not set an expiration. If you need a TTL, call
[`EXPIRE`](https://redis.io/docs/latest/commands/expire) separately with `Expire()`, or use
`Set()` with an expiration when the extra allocation is acceptable.

## More information

See the [`go-redis`](https://github.com/redis/go-redis) repository for more
examples and API details.

