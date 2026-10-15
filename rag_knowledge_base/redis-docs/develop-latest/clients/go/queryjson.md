# Index and query documents

```json metadata
{
  "schema_version": 2,
  "title": "Index and query documents",
  "description": "Learn how to use Redis Search with JSON and hash documents.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "topics": ["Redis Search","JSON","hash"],
  "relatedPages": ["/develop/clients/go/vecsearch","/develop/ai/search-and-query"],
  "scope": "example",
  "tableOfContents": {"sections":[{"id":"initialize","title":"Initialize"},{"id":"create-data","title":"Create data"},{"id":"add-the-index","title":"Add the index"},{"id":"add-the-data","title":"Add the data"},{"id":"query-the-data","title":"Query the data"},{"id":"differences-with-hash-documents","title":"Differences with hash documents"},{"id":"more-information","title":"More information"}]}

,
  "codeExamples": [{"codetabsId":"go_home_json-stepimport","description":"Foundational: Import go-redis package, which includes support for Redis Search operations","difficulty":"beginner","id":"import","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_go_home_json-stepimport"}]},{"codetabsId":"go_home_json-stepcreate_data","description":"Foundational: Create sample user data structures for indexing and querying","difficulty":"beginner","id":"create_data","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_go_home_json-stepcreate_data"}]},{"codetabsId":"go_home_json-stepconnect","description":"Foundational: Establish a connection to Redis with RESP2 protocol for Redis Search operations","difficulty":"beginner","id":"connect","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_go_home_json-stepconnect"}]},{"codetabsId":"go_home_json-stepmake_index","description":"Foundational: Create a search index for JSON documents with field definitions and key prefix filtering","difficulty":"beginner","id":"make_index","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_go_home_json-stepmake_index"}]},{"codetabsId":"go_home_json-stepadd_data","description":"Foundational: Store JSON documents with automatic indexing using JSONSet with matching key prefix","difficulty":"beginner","id":"add_data","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_go_home_json-stepadd_data"}]},{"codetabsId":"go_home_json-stepquery1","description":"Query data: Execute a full-text search with numeric range filtering using FTSearchWithArgs","difficulty":"intermediate","id":"query1","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_go_home_json-stepquery1"}]},{"codetabsId":"go_home_json-stepquery2","description":"Restrict query results: Limit query results to specific fields using FTSearchOptions to reduce data transfer","difficulty":"intermediate","id":"query2","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_go_home_json-stepquery2"}]},{"codetabsId":"go_home_json-stepquery2count_only","description":"Performance optimization: Get document count without retrieving results using CountOnly option for better performance","difficulty":"intermediate","id":"query2count_only","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_go_home_json-stepquery2count_only"}]},{"codetabsId":"go_home_json-stepquery3","description":"Aggregation: Perform aggregation queries to group and count documents by field values using FTAggregateWithArgs","difficulty":"intermediate","id":"query3","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_go_home_json-stepquery3"}]},{"codetabsId":"go_home_json-stepmake_hash_index","description":"Foundational: Create a search index for hash documents with OnHash option and simplified field schema","difficulty":"intermediate","id":"make_hash_index","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_go_home_json-stepmake_hash_index"}]},{"codetabsId":"go_home_json-stepadd_hash_data","description":"Foundational: Store hash documents with automatic indexing using HSet with matching key prefix","difficulty":"beginner","id":"add_hash_data","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_go_home_json-stepadd_hash_data"}]},{"codetabsId":"go_home_json-stepquery1_hash","description":"Query data: Execute search queries on hash documents with slightly different result structure compared to JSON","difficulty":"intermediate","id":"query1_hash","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_go_home_json-stepquery1_hash"}]}]
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


This example shows how to create a
[search index](https://redis.io/docs/latest/develop/ai/search-and-query/indexing)
for [JSON](https://redis.io/docs/latest/develop/data-types/json) documents and
run queries against the index. It then goes on to show the slight differences
in the equivalent code for [hash](https://redis.io/docs/latest/develop/data-types/hashes)
documents.

> [!NOTE]
> From [v9.8.0](https://github.com/redis/go-redis/releases/tag/v9.8.0) onwards,
> `go-redis` uses query dialect 2 by default.
> Redis Search methods such as [`FTSearch()`](https://redis.io/docs/latest/commands/ft.search)
> will explicitly request this dialect, overriding the default set for the server.
> See
> [Query dialects](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/dialects)
> for more information.

## Initialize

Make sure that you have [Redis Open Source](https://redis.io/docs/latest/operate/oss_and_stack)
or another Redis server available. Also install the
[`go-redis`](https://redis.io/docs/latest/develop/clients/go) client library if you
haven't already done so.

Add the following dependencies:

Foundational: Import go-redis package, which includes support for Redis Search operations

**Difficulty:** Beginner

**Available in:** Go

##### Go

```go
import (
	"context"
	"fmt"
	"sort"

	"github.com/redis/go-redis/v9"
)

```



## Create data

Create some test data to add to your database. The example data shown
below is compatible with both JSON and hash objects.

Foundational: Create sample user data structures for indexing and querying

**Difficulty:** Beginner

**Available in:** Go

##### Go

```go
	user1 := map[string]interface{}{
		"name":  "Paul John",
		"email": "paul.john@example.com",
		"age":   42,
		"city":  "London",
	}

	user2 := map[string]interface{}{
		"name":  "Eden Zamir",
		"email": "eden.zamir@example.com",
		"age":   29,
		"city":  "Tel Aviv",
	}

	user3 := map[string]interface{}{
		"name":  "Paul Zamir",
		"email": "paul.zamir@example.com",
		"age":   35,
		"city":  "Tel Aviv",
	}
```



## Add the index

Connect to your Redis database. The code below shows the most
basic connection but see
[Connect to the server](https://redis.io/docs/latest/develop/clients/go/connect)
to learn more about the available connection options.

Foundational: Establish a connection to Redis with RESP2 protocol for Redis Search operations

**Difficulty:** Beginner

**Available in:** Go

##### Go

```go
	ctx := context.Background()

	rdb := redis.NewClient(&redis.Options{
		Addr:     "localhost:6379",
		Password: "", // no password docs
		DB:       0,  // use default DB
		Protocol: 2,
	})
```


&nbsp;

> [!NOTE]
> The connection options in the example specify
> [RESP2](https://redis.io/docs/latest/develop/reference/protocol-spec) in the `Protocol`
> field. We recommend that you use RESP2 for Redis Search operations in `go-redis`
> because some of the response structures for the default RESP3 are currently
> incomplete and so you must handle the "raw" responses in your own code.
>
> If you do want to use RESP3, you should set the `UnstableResp3` option when
> you connect:
>
> ```go
> rdb := redis.NewClient(&redis.Options{
>     UnstableResp3: true,
>     // Other options...
> })
> ```
>
> You must also access command results using the `RawResult()` and `RawVal()` methods
> rather than the usual `Result()` and `Val()`:
>
> ```go
> res1, err := client.FTSearchWithArgs(
>     ctx, "txt", "foo bar", &redis.FTSearchOptions{},
> ).RawResult()
> val1 := client.FTSearchWithArgs(
>     ctx, "txt", "foo bar", &redis.FTSearchOptions{},
> ).RawVal()
> ```

Use the code below to create a search index. The `FTCreateOptions` parameter enables
indexing only for JSON objects where the key has a `user:` prefix.
The
[schema](https://redis.io/docs/latest/develop/ai/search-and-query/indexing)
for the index has three fields for the user's name, age, and city.
The `FieldName` field of the `FieldSchema` struct specifies a
[JSON path](https://redis.io/docs/latest/develop/data-types/json/path)
that identifies which data field to index. Use the `As` struct field
to provide an alias for the JSON path expression. You can use
the alias in queries as a short and intuitive way to refer to the
expression, instead of typing it in full:

Foundational: Create a search index for JSON documents with field definitions and key prefix filtering

**Difficulty:** Beginner

**Available in:** Go

##### Go

```go
	_, err := rdb.FTCreate(
		ctx,
		"idx:users",
		// Options:
		&redis.FTCreateOptions{
			OnJSON: true,
			Prefix: []interface{}{"user:"},
		},
		// Index schema fields:
		&redis.FieldSchema{
			FieldName: "$.name",
			As:        "name",
			FieldType: redis.SearchFieldTypeText,
		},
		&redis.FieldSchema{
			FieldName: "$.city",
			As:        "city",
			FieldType: redis.SearchFieldTypeTag,
		},
		&redis.FieldSchema{
			FieldName: "$.age",
			As:        "age",
			FieldType: redis.SearchFieldTypeNumeric,
		},
	).Result()

	if err != nil {
		panic(err)
	}
```



## Add the data

Add the three sets of user data to the database as
[JSON](https://redis.io/docs/latest/develop/data-types/json) objects.
If you use keys with the `user:` prefix then Redis will index the
objects automatically as you add them:

Foundational: Store JSON documents with automatic indexing using JSONSet with matching key prefix

**Difficulty:** Beginner

**Available in:** Go

##### Go

```go
	_, err = rdb.JSONSet(ctx, "user:1", "$", user1).Result()

	if err != nil {
		panic(err)
	}

	_, err = rdb.JSONSet(ctx, "user:2", "$", user2).Result()

	if err != nil {
		panic(err)
	}

	_, err = rdb.JSONSet(ctx, "user:3", "$", user3).Result()

	if err != nil {
		panic(err)
	}
```



## Query the data

You can now use the index to search the JSON objects. The
[query](https://redis.io/docs/latest/develop/ai/search-and-query/query)
below searches for objects that have the text "Paul" in any field
and have an `age` value in the range 30 to 40:

Query data: Execute a full-text search with numeric range filtering using FTSearchWithArgs

**Difficulty:** Intermediate

**Available in:** Go

##### Go

```go
	findPaulResult, err := rdb.FTSearch(
		ctx,
		"idx:users",
		"Paul @age:[30 40]",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(findPaulResult)
	// >>> {1 [{user:3 <nil> <nil> <nil> map[$:{"age":35,"city":"Tel Aviv"...
```



Specify query options to return only the `city` field:

Restrict query results: Limit query results to specific fields using FTSearchOptions to reduce data transfer

**Difficulty:** Intermediate

**Available in:** Go

##### Go

```go
	citiesResult, err := rdb.FTSearchWithArgs(
		ctx,
		"idx:users",
		"Paul",
		&redis.FTSearchOptions{
			Return: []redis.FTSearchReturn{
				{
					FieldName: "$.city",
					As:        "city",
				},
			},
		},
	).Result()

	if err != nil {
		panic(err)
	}

	sort.Slice(citiesResult.Docs, func(i, j int) bool {
		return citiesResult.Docs[i].Fields["city"] < citiesResult.Docs[j].Fields["city"]
	})

	for _, result := range citiesResult.Docs {
		fmt.Println(result.Fields["city"])
	}
	// >>> London
	// >>> Tel Aviv
```



You can also use the same query with the `CountOnly` option
enabled to get the number of documents found without
returning the documents themselves.

Performance optimization: Get document count without retrieving results using CountOnly option for better performance

**Difficulty:** Intermediate

**Available in:** Go

##### Go

```go
	citiesResult2, err := rdb.FTSearchWithArgs(
		ctx,
		"idx:users",
		"Paul",
		&redis.FTSearchOptions{
			Return: []redis.FTSearchReturn{
				{
					FieldName: "$.city",
					As:        "city",
				},
			},
			CountOnly: true,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	// The `Total` field has the correct number of docs found
	// by the query but the `Docs` slice is empty.
	fmt.Println(len(citiesResult2.Docs)) // >>> 0
	fmt.Println(citiesResult2.Total)     // >>> 2
```



Use an
[aggregation query](https://redis.io/docs/latest/develop/ai/search-and-query/query/aggregation)
to count all users in each city.

Aggregation: Perform aggregation queries to group and count documents by field values using FTAggregateWithArgs

**Difficulty:** Intermediate

**Available in:** Go

##### Go

```go
	aggOptions := redis.FTAggregateOptions{
		GroupBy: []redis.FTAggregateGroupBy{
			{
				Fields: []interface{}{"@city"},
				Reduce: []redis.FTAggregateReducer{
					{
						Reducer: redis.SearchCount,
						As:      "count",
					},
				},
			},
		},
	}

	aggResult, err := rdb.FTAggregateWithArgs(
		ctx,
		"idx:users",
		"*",
		&aggOptions,
	).Result()

	if err != nil {
		panic(err)
	}

	sort.Slice(aggResult.Rows, func(i, j int) bool {
		return aggResult.Rows[i].Fields["city"].(string) <
			aggResult.Rows[j].Fields["city"].(string)
	})

	for _, row := range aggResult.Rows {
		fmt.Printf("%v - %v\n",
			row.Fields["city"], row.Fields["count"],
		)
	}
	// >>> City: London - 1
	// >>> City: Tel Aviv - 2
```



## Differences with hash documents

Indexing for hash documents is very similar to JSON indexing but you
need to specify some slightly different options.

When you create the schema for a hash index, you don't need to
add aliases for the fields, since you use the basic names to access
the fields anyway. Also, you must set `OnHash` to `true` in the `FTCreateOptions`
object when you create the index. The code below shows these changes with
a new index called `hash-idx:users`, which is otherwise the same as
the `idx:users` index used for JSON documents in the previous examples.

Foundational: Create a search index for hash documents with OnHash option and simplified field schema

**Difficulty:** Intermediate

**Available in:** Go

##### Go

```go
	_, err := rdb.FTCreate(
		ctx,
		"hash-idx:users",
		// Options:
		&redis.FTCreateOptions{
			OnHash: true,
			Prefix: []interface{}{"huser:"},
		},
		// Index schema fields:
		&redis.FieldSchema{
			FieldName: "name",
			FieldType: redis.SearchFieldTypeText,
		},
		&redis.FieldSchema{
			FieldName: "city",
			FieldType: redis.SearchFieldTypeTag,
		},
		&redis.FieldSchema{
			FieldName: "age",
			FieldType: redis.SearchFieldTypeNumeric,
		},
	).Result()

	if err != nil {
		panic(err)
	}
```



You use [`HSet()`](https://redis.io/docs/latest/commands/hset) to add the hash
documents instead of [`JSONSet()`](https://redis.io/docs/latest/commands/json.set),
but the same flat `userX` maps work equally well with either
hash or JSON:

Foundational: Store hash documents with automatic indexing using HSet with matching key prefix

**Difficulty:** Beginner

**Available in:** Go

##### Go

```go
	_, err = rdb.HSet(ctx, "huser:1", user1).Result()

	if err != nil {
		panic(err)
	}

	_, err = rdb.HSet(ctx, "huser:2", user2).Result()

	if err != nil {
		panic(err)
	}

	_, err = rdb.HSet(ctx, "huser:3", user3).Result()

	if err != nil {
		panic(err)
	}
```



The query commands work the same here for hash as they do for JSON (but
the name of the hash index is different). The format of the result is
almost the same except that the fields are returned directly in the
`Document` object map of the result (for JSON, the fields are all enclosed
in a string under the key "$"):

Query data: Execute search queries on hash documents with slightly different result structure compared to JSON

**Difficulty:** Intermediate

**Available in:** Go

##### Go

```go
	findPaulHashResult, err := rdb.FTSearch(
		ctx,
		"hash-idx:users",
		"Paul @age:[30 40]",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(findPaulHashResult)
	// >>> {1 [{huser:3 <nil> <nil> <nil> map[age:35 city:Tel Aviv...
```



## More information

See the [Redis Search](https://redis.io/docs/latest/develop/ai/search-and-query) docs
for a full description of all query features with examples.

