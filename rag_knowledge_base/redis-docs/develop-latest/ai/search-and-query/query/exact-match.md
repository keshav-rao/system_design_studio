# Exact match queries

```json metadata
{
  "schema_version": 2,
  "title": "Exact match queries",
  "description": "Perform simple exact match queries",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"numeric-field","title":"Numeric field"},{"id":"tag-field","title":"Tag field"},{"id":"full-text-field","title":"Full-text field"}]}

,
  "codeExamples": [{"codetabsId":"query_em-stepem1","commands":[{"acl_categories":["@read","@search"],"complexity":"O(N)","name":"FT.SEARCH"}],"description":"Foundational: Query numeric fields for exact matches using range syntax or equality operators when you need to find documents with specific numeric values","difficulty":"beginner","id":"em1","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_query_em-stepem1"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_query_em-stepem1"},{"id":"Node-js","panelId":"panel_Nodejs_query_em-stepem1"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_query_em-stepem1"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_query_em-stepem1"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_query_em-stepem1"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_query_em-stepem1"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_query_em-stepem1"}]},{"codetabsId":"query_em-stepem2","commands":[{"acl_categories":["@read","@search"],"complexity":"O(N)","name":"FT.SEARCH"}],"description":"Foundational: Query tag fields for exact matches using curly bracket syntax when you need to find documents with specific categorical values","difficulty":"beginner","id":"em2","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_query_em-stepem2"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_query_em-stepem2"},{"id":"Node-js","panelId":"panel_Nodejs_query_em-stepem2"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_query_em-stepem2"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_query_em-stepem2"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_query_em-stepem2"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_query_em-stepem2"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_query_em-stepem2"}]},{"codetabsId":"query_em-stepem3","commands":[{"acl_categories":["@search"],"complexity":"O(K)","name":"FT.CREATE"},{"acl_categories":["@write","@json"],"complexity":"O(M+N)","name":"JSON.SET"},{"acl_categories":["@read","@search"],"complexity":"O(N)","name":"FT.SEARCH"}],"description":"Tag fields: Query tag fields with special characters using double-quoted syntax and DIALECT 2 when you need to match tags containing symbols or spaces","difficulty":"advanced","id":"em3","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_query_em-stepem3"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_query_em-stepem3"},{"id":"Node-js","panelId":"panel_Nodejs_query_em-stepem3"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_query_em-stepem3"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_query_em-stepem3"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_query_em-stepem3"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_query_em-stepem3"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_query_em-stepem3"}]},{"codetabsId":"query_em-stepem4","commands":[{"acl_categories":["@read","@search"],"complexity":"O(N)","name":"FT.SEARCH"}],"description":"Text fields: Query text fields for exact phrase matches using escaped double quotes when you need to find documents containing specific multi-word phrases","difficulty":"intermediate","id":"em4","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_query_em-stepem4"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_query_em-stepem4"},{"id":"Node-js","panelId":"panel_Nodejs_query_em-stepem4"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_query_em-stepem4"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_query_em-stepem4"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_query_em-stepem4"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_query_em-stepem4"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_query_em-stepem4"}]}]
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


An exact match query allows you to select all documents where a field matches a specific value. 

You can use exact match queries on several field types. The query syntax varies depending on the type. 

The examples in this article use a schema with the following fields:

| Field name | Field type |
| ---------- | ---------- |
| `description`| `TEXT` |
| `condition` | `TAG` |
| `price` | `NUMERIC` |

You can find more details about creating the index and loading the demo data in the [quick start guide](https://redis.io/docs/latest/develop/get-started/search-tutorial).

## Numeric field

To perform an exact match query on a numeric field, you need to construct a range query with the same start and end value:

```
FT.SEARCH index "@field:[value value]"

or

FT.SEARCH index "@field:[value]" DIALECT 2 # requires v2.10

or

FT.SEARCH index "@field==value" DIALECT 2 # requires v2.10
```

As described in the [article about range queries](https://redis.io/docs/latest/develop/ai/search-and-query/query/range), you can also use the `FILTER` argument:

```
FT.SEARCH index "*" FILTER field start end
```

The following examples show you how to query for bicycles with a price of exactly 270 USD:

Foundational: Query numeric fields for exact matches using range syntax or equality operators when you need to find documents with specific numeric values

**Difficulty:** Beginner

**Commands:** FT.SEARCH

**Complexity:**
- FT.SEARCH: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), Python

##### Redis CLI

```
> FT.SEARCH idx:bicycle "@price:[270 270]"
1) (integer) 1
2) "bicycle:0"
3) 1) "$"
   2) "{\"pickup_zone\":\"POLYGON((-74.0610 40.7578, ...

> FT.SEARCH idx:bicycle "@price:[270]" # requires v2.10
1) (integer) 1
2) "bicycle:0"
3) 1) "$"
   2) "{\"pickup_zone\":\"POLYGON((-74.0610 40.7578, ...

> FT.SEARCH idx:bicycle "@price==270" # requires v2.10
1) (integer) 1
2) "bicycle:0"
3) 1) "$"
   2) "{\"pickup_zone\":\"POLYGON((-74.0610 40.7578, ...

> FT.SEARCH idx:bicycle "*" FILTER price 270 270
1) (integer) 1
2) "bicycle:0"
3) 1) "$"
   2) "{\"pickup_zone\":\"POLYGON((-74.0610 40.7578, ...
```

##### C#

```csharp
        SearchResult res1 = db.FT().Search(
            "idx:bicycle",
            new("@price:[270 270]")
        );
        Console.WriteLine(res1.TotalResults); //    >>> 1

        SearchResult res2 = db.FT().Search(
            "idx:bicycle",
            new Query().AddFilter(
                new Query.NumericFilter("price", 270, 270)
            )
        );
        Console.WriteLine(res2.TotalResults); //    >>> 1
```

##### Go

```go
	res1, err := rdb.FTSearch(ctx,
		"idx:bicycle", "@price:[270 270]",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1.Total) // >>> 1

	for _, doc := range res1.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:0

	res2, err := rdb.FTSearchWithArgs(ctx,
		"idx:bicycle",
		"*",
		&redis.FTSearchOptions{
			Filters: []redis.FTSearchFilter{
				{
					FieldName: "price",
					Min:       270,
					Max:       270,
				},
			},
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2.Total) // >>> 1

	for _, doc := range res2.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:0
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<SearchReply<String, String>> priceResults = asyncCommands.ftSearch("idx:bicycle", "@price:[270]")

                    .thenApply(res -> {

                        res.getResults().forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:0

                        return res;
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<SearchReply<String, String>> priceResults = reactiveCommands.ftSearch("idx:bicycle", "@price:[270]")
                    .doOnNext(res -> {
                        res.getResults().forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:0
                    });
```

##### Java (Synchronous - Jedis)

```java
        SearchResult res1 = jedis.ftSearch("idx:bicycle", "@price:[270 270]");
        System.out.println(res1.getTotalResults()); // >>> 1

        List<Document> docs1 = res1.getDocuments();

        for (int i = 0; i < docs1.size(); i++) {
            System.out.println(docs1.get(i).getId());
        }
        // >>> bicycle:0

        SearchResult res2 = jedis.ftSearch("idx:bicycle",
            "*",
            FTSearchParams.searchParams()
                    .filter("price", 270, 270)
        );
        System.out.println(res2.getTotalResults()); // >>> 1

        List<Document> docs2 = res2.getDocuments();

        for (int i = 0; i < docs2.size(); i++) {
            System.out.println(docs2.get(i).getId());
        }
        // >>> bicycle:0
```

##### JavaScript (Node.js)

```javascript
const res1 = await client.ft.search('idx:bicycle', '@price:[270 270]');
console.log(res1.total); // >>> 1

try {
    const res2 = await client.ft.search('idx:bicycle', '@price:[270]');
    console.log(res2.total); // >>> 1
    assert.strictEqual(res2.total, 1);
} catch (err) {
    console.log("'@price:[270]' syntax not yet supported.");
}

try {
    const res3 = await client.ft.search('idx:bicycle', '@price==270');
    console.log(res3.total); // >>> 1
    assert.strictEqual(res3.total, 1);
} catch (err) {
    console.log("'@price==270' syntax not yet supported.");
}

// FILTER is not supported
// const res4 = await client.ft.search('idx:bicycle', '*', {
//   FILTER: {
//       field: 'price',
//       min: 270,
//       max: 270,
//   }
// });
// console.log(res4.total); // >>> 1
```

##### Python

```python
res = index.search(Query("@price:[270 270]"))
print(res.total)
# >>> 1

try:
    res = index.search(Query("@price:[270]")) # not yet supported in redis-py
    print(res.total)
    # >>> 1
    assert res.total == 1
except Exception:
    print("'@price:[270]' syntax not yet supported.")

try:
    res = index.search(Query("@price==270")) # not yet supported in redis-py
    print(res.total)
    # >>> 1
    assert res.total == 1
except Exception:
    print("'@price==270' syntax not yet supported.")

query = Query("*").add_filter(NumericFilter("price", 270, 270))
res = index.search(query)
print(res.total)
# >>> 1
```




## Tag field

A tag is a short sequence of text, for example, "new" or "Los Angeles". 

> [!NOTE] Important
> If you need to query for short texts, use a tag query instead of a full-text query. Tag fields are more space-efficient for storing index entries and often lead to lower query complexity for exact match queries.

You can construct a tag query for a single tag in the following way:

```
FT.SEARCH index "@field:{tag}"
```

> [!NOTE]
> The curly brackets are mandatory for tag queries.

This short example shows you how to query for new bicycles:

Foundational: Query tag fields for exact matches using curly bracket syntax when you need to find documents with specific categorical values

**Difficulty:** Beginner

**Commands:** FT.SEARCH

**Complexity:**
- FT.SEARCH: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), Python

##### Redis CLI

```
> FT.SEARCH idx:bicycle "@condition:{new}"
 1) (integer) 5
 2) "bicycle:0"
 3) 1) "$"
    2) "{\"pickup_zone\":\"POLYGON((-74.0610 40.7578, -73.9510 40.7578, -73.9510 40.6678, -74.0610 40.6678, -74.0610 40.7578))\",\"store_location\":\"-74.0060,40.7128\",\"brand\":\"Velorim\",\"model\":\"Jigger\",\"price\":270,\"description\":\"Small and powerful, the Jigger is the best ride for the smallest of tikes! This is the tiniest kids\xe2\x80\x99 pedal bike on the market available without a coaster brake, the Jigger is the vehicle of choice for the rare tenacious little rider raring to go.\",\"condition\":\"new\"}"
 4) "bicycle:5"
... output truncated for AI-facing Markdown ...
    2) "{\"pickup_zone\":\"POLYGON((1.9450 41.4301, 2.4018 41.4301, 2.4018 41.1987, 1.9450 41.1987, 1.9450 41.4301))\",\"store_location\":\"2.1734, 41.3851\",\"brand\":\"nHill\",\"model\":\"Summit\",\"price\":1200,\"description\":\"This budget mountain bike from nHill performs well both on bike paths and on the trail. The fork with 100mm of travel absorbs rough terrain. Fat Kenda Booster tires give you grip in corners and on wet trails. The Shimano Tourney drivetrain offered enough gears for finding a comfortable pace to ride uphill, and the Tektro hydraulic disc brakes break smoothly. Whether you want an affordable bike that you can take to work, but also take trail in mountains on the weekends or you\xe2\x80\x99re just after a stable, comfortable ride for the bike path, the Summit gives a good value for money.\",\"condition\":\"new\"}"
```

##### C#

```csharp
        SearchResult res3 = db.FT().Search(
            "idx:bicycle",
            new("@condition:{new}")
        );
        Console.WriteLine(res3.TotalResults);   // >>> 4
```

##### Go

```go
	res3, err := rdb.FTSearch(ctx,
		"idx:bicycle", "@condition:{new}",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3.Total) // >>> 5

	docs := res3.Docs
	slices.SortFunc(docs, func(a, b redis.Document) int {
		return strings.Compare(a.ID, b.ID)
	})

	for _, doc := range docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:0
	// >>> bicycle:5
	// >>> bicycle:6
	// >>> bicycle:7
	// >>> bicycle:8
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<SearchReply<String, String>> conditionResults = asyncCommands
                    .ftSearch("idx:bicycle", "@condition:{new}").thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:0
                        // >>> ID: bicycle:5
                        // >>> ID: bicycle:6
                        // >>> ID: bicycle:7
                        // >>> ID: bicycle:8

                        return res;
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<SearchReply<String, String>> conditionResults = reactiveCommands.ftSearch("idx:bicycle", "@condition:{new}")
                    .doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:0
                        // >>> ID: bicycle:5
                        // >>> ID: bicycle:6
                        // >>> ID: bicycle:7
                        // >>> ID: bicycle:8
                    });
```

##### Java (Synchronous - Jedis)

```java
        SearchResult res3 = jedis.ftSearch("idx:bicycle", "@condition:{new}");
        System.out.println(res3.getTotalResults()); // >>> 5

        List<Document> docs3 = res3.getDocuments();

        for (int i = 0; i < docs3.size(); i++) {
            System.out.println(docs3.get(i).getId());
        }
        // >>> bicycle:5
        // >>> bicycle:0
        // >>> bicycle:6
        // >>> bicycle:7
        // >>> bicycle:8
```

##### JavaScript (Node.js)

```javascript
const res5 = await client.ft.search('idx:bicycle', '@condition:{new}');
console.log(res5.total); // >>> 5
```

##### Python

```python
res = index.search(Query("@condition:{new}"))
print(res.total)
# >>> 5
```



Use double quotes and [DIALECT 2](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/dialects#dialect-2) for exact match queries involving tags that contain special characters. As of v2.10, the only character that needs escaping in queries involving double-quoted tags is the double-quote character. Here's an example of using double-quoted tags that contain special characters:

Tag fields: Query tag fields with special characters using double-quoted syntax and DIALECT 2 when you need to match tags containing symbols or spaces

**Difficulty:** Advanced

**Commands:** FT.CREATE, JSON.SET, FT.SEARCH

**Complexity:**
- FT.CREATE: O(K)
- JSON.SET: O(M+N)
- FT.SEARCH: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), Python

##### Redis CLI

```
> FT.CREATE idx:email ON JSON PREFIX 1 key: SCHEMA $.email AS email TAG
OK
> JSON.SET key:1 $ '{"email": "test@redis.com"}'
OK
> FT.SEARCH idx:email '@email:{"test@redis.com"}' DIALECT 2
1) (integer) 1
2) "key:1"
3) 1) "$"
   2) "{\"email\":\"test@redis.com\"}"
```

##### C#

```csharp
        Schema emailSchema = new Schema()
            .AddTagField(new FieldName("$.email", "email"));

        FTCreateParams emailParams = new FTCreateParams()
            .AddPrefix("key:")
            .On(IndexDataType.JSON);

        db.FT().Create("idx:email", emailParams, emailSchema);

        db.JSON().Set("key:1", "$", "{\"email\": \"test@redis.com\"}");



        SearchResult res4 = db.FT().Search(
            "idx:email",
            new Query("@email:{test\\@redis\\.com}").Dialect(2)
        );
        Console.WriteLine(res4.TotalResults);   // >>> 1
```

##### Go

```go
	res4, err := rdb.FTCreate(ctx,
		"idx:email",
		&redis.FTCreateOptions{
			OnJSON: true,
			Prefix: []interface{}{"key:"},
		},
		&redis.FieldSchema{
			FieldName: "$.email",
			As:        "email",
			FieldType: redis.SearchFieldTypeTag,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4) // >>> OK

	res5, err := rdb.JSONSet(ctx, "key:1", "$",
		map[string]interface{}{
			"email": "test@redis.com",
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res5) // >>> OK


	res6, err := rdb.FTSearch(ctx, "idx:email",
		"@email:{test\\@redis\\.com}",
	).Result()
	if err != nil {
		panic(err)
	}
	fmt.Println(res6.Total) // >>> 1
```

##### Java (Asynchronous - Lettuce)

```java
            List<FieldArgs<String>> emailSchema = Arrays
                    .asList(TagFieldArgs.<String> builder().name("$.email").as("email").build());
            CreateArgs<String, String> emailCreateArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.JSON)
                    .withPrefix("key:").build();

            CompletableFuture<SearchReply<String, String>> emailResults = asyncCommands
                    .ftCreate("idx:email", emailCreateArgs, emailSchema).thenCompose(res -> {
                        System.out.println(res); // >>> OK
                        return asyncCommands.jsonSet("key:1", JsonPath.ROOT_PATH,
                                parser.createJsonObject().put("email", parser.createJsonValue("\"test@redis.com\"")));
                    }).thenCompose(res2 -> {
                        System.out.println(res2); // >>> OK
                        return asyncCommands.ftSearch("idx:email", "@email:{test\\@redis\\.com}");
                    }).thenApply(res3 -> {
                        System.out.println(res3.getResults().size()); // >>> 1
                        System.out.println(res3.getResults().get(0).getId());
                        // >>> key:1
                        return res3;
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            List<FieldArgs<String>> emailSchema = Arrays
                    .asList(TagFieldArgs.<String> builder().name("$.email").as("email").build());

            CreateArgs<String, String> emailCreateArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.JSON)
                    .withPrefix("key:").build();

            Mono<Void> emailResults = reactiveCommands.ftCreate("idx:email", emailCreateArgs, emailSchema).doOnNext(res -> {
                System.out.println(res); // >>> OK
            }).flatMap(res -> reactiveCommands.jsonSet("key:1", JsonPath.ROOT_PATH,
                    parser.createJsonObject().put("email", parser.createJsonValue("\"test@redis.com\"")))).doOnNext(res -> {
                        System.out.println(res); // >>> OK
                    }).flatMap(res -> reactiveCommands.ftSearch("idx:email", "@email:{test\\@redis\\.com}")).doOnNext(res -> {
                        System.out.println(res.getResults().size()); // >>> 1
                        System.out.println(res.getResults().get(0).getId());
                        // >>> key:1
                    }).then();
```

##### Java (Synchronous - Jedis)

```java
        SchemaField[] emailSchema = {
            TextField.of("$.email").as("email")
        };

        jedis.ftCreate("idx:email", 
            new FTCreateParams()
                    .addPrefix("key:")
                    .on(IndexDataType.JSON),
            emailSchema
        );

        jedis.jsonSet("key:1", Path2.ROOT_PATH, "{\"email\": \"test@redis.com\"}");
        
        SearchResult res4 = jedis.ftSearch("idx:email",
            RediSearchUtil.escapeQuery("@email{test@redis.com}"),
            new FTSearchParams().dialect(2)
        );
        System.out.println(res4.getTotalResults());
```

##### JavaScript (Node.js)

```javascript
await client.ft.create('idx:email', {
  '$.email': {
    type: SCHEMA_FIELD_TYPE.TAG,
    AS: 'email'
  }
}, {
  ON: 'JSON',
  PREFIX: 'key:'
})

await client.json.set('key:1', '$', { email: 'test@redis.com' });

try {
    const res6 = await client.ft.search('idx:email', 'test@redis.com', { DIALECT: 2 });
    console.log(res6);
} catch (err) {
    console.log("'test@redis.com' syntax not yet supported.");
}
```

##### Python

```python
schema = (
    TagField("$.email", as_name="email")
)

idx_email = r.ft("idx:email")
idx_email.create_index(
    schema,
    definition=IndexDefinition(prefix=["key:"], index_type=IndexType.JSON),
)
r.json().set('key:1', Path.root_path(), '{"email": "test@redis.com"}')

try:
    res = idx_email.search(Query("test@redis.com").dialect(2))
    print(res)
except Exception:
    print("'test@redis.com' syntax not yet supported.")
```



## Full-text field

A detailed explanation of full-text queries is available in the [full-text queries documentation](https://redis.io/docs/latest/develop/ai/search-and-query/query/full-text). You can also query for an exact match of a phrase within a text field:

```
FT.SEARCH index "@field:\"phrase\""
```

> [!NOTE] Important
> The phrase must be wrapped by escaped double quotes for an exact match query.
>
> You can't use a phrase that starts with a [stop word](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/stopwords).

Here is an example for finding all bicycles that have a description containing the exact text 'rough terrain':

Text fields: Query text fields for exact phrase matches using escaped double quotes when you need to find documents containing specific multi-word phrases

**Difficulty:** Intermediate

**Commands:** FT.SEARCH

**Complexity:**
- FT.SEARCH: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), Python

##### Redis CLI

```
> FT.SEARCH idx:bicycle "@description:\"rough terrain\""
1) (integer) 1
2) "bicycle:8"
3) 1) "$"
   2) "{\"pickup_zone\":\"POLYGON((1.9450 41.4301, 2.4018 41.4301, 2.4018 41.1987, 1.9450 41.1987, 1.9450 41.4301))\",\"store_location\":\"2.1734, 41.3851\",\"brand\":\"nHill\",\"model\":\"Summit\",\"price\":1200,\"description\":\"This budget mountain bike from nHill performs well both on bike paths and on the trail. The fork with 100mm of travel absorbs rough terrain. Fat Kenda Booster tires give you grip in corners and on wet trails. The Shimano Tourney drivetrain offered enough gears for finding a comfortable pace to ride uphill, and the Tektro hydraulic disc brakes break smoothly. Whether you want an affordable bike that you can take to work, but also take trail in mountains on the weekends or you\xe2\x80\x99re just after a stable, comfortable ride for the bike path, the Summit gives a good value for money.\",\"condition\":\"new\"}"
```

##### C#

```csharp
        SearchResult res5 = db.FT().Search(
            "idx:bicycle",
            new("@description:\"rough terrain\"")
        );
        Console.WriteLine(res5.TotalResults);   // >>> 1
```

##### Go

```go
	res7, err := rdb.FTSearch(ctx,
		"idx:bicycle", "@description:\"rough terrain\"",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res7.Total) // >>> 1

	for _, doc := range res7.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:8
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<SearchReply<String, String>> textMatchResults = asyncCommands
                    .ftSearch("idx:bicycle", "@description:\"rough terrain\"").thenApply(res -> {
                        res.getResults().forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:8

                        return res;
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<SearchReply<String, String>> textMatchResults = reactiveCommands
                    .ftSearch("idx:bicycle", "@description:\"rough terrain\"").doOnNext(res -> {
                        res.getResults().forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:8
                    });
```

##### Java (Synchronous - Jedis)

```java
        SearchResult res5 = jedis.ftSearch("idx:bicycle",
            "@description:\"rough terrain\""
        );
        System.out.println(res5.getTotalResults()); // >>> 1

        List<Document> docs5 = res5.getDocuments();

        for (int i = 0; i < docs5.size(); i++) {
            System.out.println(docs5.get(i).getId());
        }
        // >>> bicycle:8
```

##### JavaScript (Node.js)

```javascript
const res7 = await client.ft.search('idx:bicycle', '@description:"rough terrain"');
console.log(res7.total); // >>> 1 (Result{1 total, docs: [Document {'id': 'bicycle:8'...)
```

##### Python

```python
res = index.search(Query("@description:\"rough terrain\""))
print(res.total)
# >>> 1 (Result{1 total, docs: [Document {'id': 'bicycle:8'...)
```


