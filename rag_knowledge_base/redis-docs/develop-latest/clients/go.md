# go-redis guide (Go)

```json metadata
{
  "schema_version": 2,
  "title": "go-redis guide (Go)",
  "description": "Connect your Go application to a Redis database",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"install","title":"Install"},{"id":"connect","title":"Connect"},{"id":"more-information","title":"More information"}]}

,
  "codeExamples": [{"codetabsId":"landing-stepimport","description":"Foundational: Import the go-redis package","difficulty":"beginner","id":"import","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_landing-stepimport"}]},{"codetabsId":"landing-stepconnect","description":"Foundational: Connect to a Redis server and establish a client connection","difficulty":"beginner","id":"connect","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_landing-stepconnect"}]},{"codetabsId":"landing-stepset_get_string","description":"Foundational: Set and retrieve string values using SET and GET commands","difficulty":"beginner","id":"set_get_string","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_landing-stepset_get_string"}]},{"codetabsId":"landing-stepset_get_hash","description":"Foundational: Store and retrieve hash data structures using HSET and HGET commands","difficulty":"beginner","id":"set_get_hash","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_landing-stepset_get_hash"}]},{"codetabsId":"landing-stepget_hash_scan","description":"Foundational: Parse hash data structures into struct fields using Scan()","difficulty":"beginner","id":"get_hash_scan","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_landing-stepget_hash_scan"}]},{"codetabsId":"landing-stepclose","description":"Foundational: Close the Redis client connection","difficulty":"beginner","id":"close","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_landing-stepclose"}]}]
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


[`go-redis`](https://github.com/redis/go-redis) is the [Go](https://go.dev/) client for Redis.
The sections below explain how to install `go-redis` and connect your application to a Redis database.

`go-redis` requires a running Redis server. See [here](https://redis.io/docs/latest/operate/oss_and_stack/install) for Redis Open Source installation instructions.

## Install

`go-redis` supports the last two Go versions. You can only use it from within
a Go module, so you must initialize a Go module before you start, or add your code to
an existing module:

```
go mod init github.com/my/repo
```

Use the `go get` command to install `go-redis/v9`:

```
go get github.com/redis/go-redis/v9
```

## Connect

The following example shows the simplest way to connect to a Redis server.
First, import the `go-redis` package:

Foundational: Import the go-redis package

**Difficulty:** Beginner

**Available in:** Go

##### Go

```go
import (
	"context"
	"fmt"

	"github.com/redis/go-redis/v9"
)

```



Then connect to localhost on port 6379 and add a
[context](https://golang.org/pkg/context/) object:

Foundational: Connect to a Redis server and establish a client connection

**Difficulty:** Beginner

**Available in:** Go

##### Go

```go
	rdb := redis.NewClient(&redis.Options{
		Addr:     "localhost:6379",
		Password: "", // no password
		DB:       0,  // use default DB
		Protocol: 2,
	})

	ctx := context.Background()
```



You can also connect using a connection URL:

```go
opt, err := redis.ParseURL("redis://<user>:<pass>@localhost:6379/<db>")
if err != nil {
	panic(err)
}

client := redis.NewClient(opt)
```

> [!NOTE]
> go-redis supports [connection URLs](https://redis.io/docs/latest/develop/clients/connection-urls#go-redis-go) through `redis.ParseURL()`.
> A URL can set the host, port, credentials, database, and whether to use TLS,
> so you can use one instead of passing those options separately.

After connecting, you can test the connection by  storing and retrieving
a simple [string](https://redis.io/docs/latest/develop/data-types/strings):

Foundational: Set and retrieve string values using SET and GET commands

**Difficulty:** Beginner

**Available in:** Go

##### Go

```go
	err := rdb.Set(ctx, "foo", "bar", 0).Err()
	if err != nil {
		panic(err)
	}

	val, err := rdb.Get(ctx, "foo").Result()
	if err != nil {
		panic(err)
	}
	fmt.Println("foo", val) // >>> foo bar
```



You can also easily store and retrieve a [hash](https://redis.io/docs/latest/develop/data-types/hashes):

Foundational: Store and retrieve hash data structures using HSET and HGET commands

**Difficulty:** Beginner

**Available in:** Go

##### Go

```go
	hashFields := []string{
		"model", "Deimos",
		"brand", "Ergonom",
		"type", "Enduro bikes",
		"price", "4972",
	}

	res1, err := rdb.HSet(ctx, "bike:1", hashFields).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // >>> 4

	res2, err := rdb.HGet(ctx, "bike:1", "model").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2) // >>> Deimos

	res3, err := rdb.HGet(ctx, "bike:1", "price").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3) // >>> 4972

	res4, err := rdb.HGetAll(ctx, "bike:1").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4)
	// >>> map[brand:Ergonom model:Deimos price:4972 type:Enduro bikes]
```



 Use
 [struct tags](https://stackoverflow.com/questions/10858787/what-are-the-uses-for-struct-tags-in-go)
 of the form `redis:"<field-name>"` with the `Scan()` method to parse fields from
 a hash directly into corresponding struct fields:

Foundational: Parse hash data structures into struct fields using Scan()

**Difficulty:** Beginner

**Available in:** Go

##### Go

```go
	type BikeInfo struct {
		Model string `redis:"model"`
		Brand string `redis:"brand"`
		Type  string `redis:"type"`
		Price int    `redis:"price"`
	}

	var res4a BikeInfo
	err = rdb.HGetAll(ctx, "bike:1").Scan(&res4a)

	if err != nil {
		panic(err)
	}

	fmt.Printf("Model: %v, Brand: %v, Type: %v, Price: $%v\n",
		res4a.Model, res4a.Brand, res4a.Type, res4a.Price)
	// >>> Model: Deimos, Brand: Ergonom, Type: Enduro bikes, Price: $4972
```



Close the connection when you're done using a `Close()` call:

Foundational: Close the Redis client connection

**Difficulty:** Beginner

**Available in:** Go

##### Go

```go
	rdb.Close()
```



In the common case where you want to close the connection at the end of the
function where you opened it, you may find it convenient to use a `defer`
statement right after connecting:

```go
func main() {    
    rdb := redis.NewClient(&redis.Options{
        ...
    })
    defer rdb.Close()
    ...
}
```

## More information

See the other pages in this section for more information and examples.
Further examples are available at the [`go-redis`](https://redis.uptrace.dev/guide/) website
and the [GitHub repository](https://github.com/redis/go-redis).

