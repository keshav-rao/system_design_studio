# Full-text search

```json metadata
{
  "schema_version": 2,
  "title": "Full-text search",
  "description": "Perform a full-text search",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"single-word","title":"Single word"},{"id":"phrase","title":"Phrase"},{"id":"word-prefix","title":"Word prefix"},{"id":"word-suffix","title":"Word suffix"},{"children":[{"id":"fuzzy-search-on-a-specific-attribute","title":"Fuzzy search on a specific attribute"}],"id":"fuzzy-search","title":"Fuzzy search"},{"id":"unicode-considerations","title":"Unicode considerations"}]}

,
  "codeExamples": [{"codetabsId":"query_ft-stepft1","description":"Foundational: Search for single words across text fields using simple word queries when you need to find documents containing specific terms","difficulty":"beginner","id":"ft1","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_query_ft-stepft1"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_query_ft-stepft1"},{"id":"Node-js","panelId":"panel_Nodejs_query_ft-stepft1"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_query_ft-stepft1"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_query_ft-stepft1"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_query_ft-stepft1"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_query_ft-stepft1"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_query_ft-stepft1"}]},{"codetabsId":"query_ft-stepft2","description":"Prefix matching: Search for words with a specific prefix using wildcard syntax when you need to find documents with words starting with certain characters","difficulty":"intermediate","id":"ft2","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_query_ft-stepft2"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_query_ft-stepft2"},{"id":"Node-js","panelId":"panel_Nodejs_query_ft-stepft2"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_query_ft-stepft2"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_query_ft-stepft2"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_query_ft-stepft2"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_query_ft-stepft2"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_query_ft-stepft2"}]},{"codetabsId":"query_ft-stepft3","description":"Suffix/infix matching: Search for words with a specific suffix or infix using wildcard syntax when you need to find documents with words ending or containing certain characters","difficulty":"intermediate","id":"ft3","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_query_ft-stepft3"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_query_ft-stepft3"},{"id":"Node-js","panelId":"panel_Nodejs_query_ft-stepft3"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_query_ft-stepft3"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_query_ft-stepft3"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_query_ft-stepft3"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_query_ft-stepft3"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_query_ft-stepft3"}]},{"codetabsId":"query_ft-stepft4","description":"Fuzzy search: Search for words with approximate matches using fuzzy search with single % delimiters when you need to find documents despite spelling variations or typos","difficulty":"intermediate","id":"ft4","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_query_ft-stepft4"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_query_ft-stepft4"},{"id":"Node-js","panelId":"panel_Nodejs_query_ft-stepft4"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_query_ft-stepft4"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_query_ft-stepft4"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_query_ft-stepft4"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_query_ft-stepft4"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_query_ft-stepft4"}]},{"codetabsId":"query_ft-stepft5","description":"Fuzzy search: Search for words with larger approximate matches using fuzzy search with double %% delimiters when you need to tolerate greater spelling variations","difficulty":"intermediate","id":"ft5","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_query_ft-stepft5"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_query_ft-stepft5"},{"id":"Node-js","panelId":"panel_Nodejs_query_ft-stepft5"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_query_ft-stepft5"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_query_ft-stepft5"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_query_ft-stepft5"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_query_ft-stepft5"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_query_ft-stepft5"}]}]
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


A full-text search finds words or phrases within larger texts. You can search within a specific text field or across all text fields. 

This article provides a good overview of the most relevant full-text search capabilities. Please find further details about all the full-text search features in the [reference documentation](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts).

The examples in this article use a schema with the following fields:

| Field name | Field type |
| ---------- | ---------- |
| `brand`      | `TEXT`       |
| `model`      | `TEXT`       |
| `description`| `TEXT`       |


## Single word

To search for a word (or word stem) across all text fields, you can construct the following simple query:

```
FT.SEARCH index "word"
```

Instead of searching across all text fields, you might want to limit the search to a specific text field.

```
FT.SEARCH index "@field: word"
```

Words that occur very often in natural language, such as `the` or `a` for the English language, aren't indexed and will not return a search result. You can find further details in the [stop words article](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/stopwords).

The following example searches for all bicycles that have the word 'kids' in the description:

Foundational: Search for single words across text fields using simple word queries when you need to find documents containing specific terms

**Difficulty:** Beginner

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), Python

##### Redis CLI

```
FT.SEARCH idx:bicycle "@description: kids"
```

##### C#

```csharp
        SearchResult res1 = db.FT().Search(
           "idx:bicycle",
           new("@description: kids")
       );
        Console.WriteLine(res1);    // >>> 2
```

##### Go

```go
	res1, err := rdb.FTSearch(ctx,
		"idx:bicycle", "@description: kids",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1.Total) // >>> 2

	sort.Slice(res1.Docs, func(i, j int) bool {
		return res1.Docs[i].ID < res1.Docs[j].ID
	})

	for _, doc := range res1.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:1
	// >>> bicycle:2
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<SearchReply<String, String>> descriptionResults = asyncCommands
                    .ftSearch("idx:bicycle", "@description: kids").thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:1
                        // >>> ID: bicycle:2
                        return res;
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<SearchReply<String, String>> descriptionResults = reactiveCommands
                    .ftSearch("idx:bicycle", "@description: kids").doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                            // >>> ID: bicycle:1
                            // >>> ID: bicycle:2
                        });
                    });
```

##### Java (Synchronous - Jedis)

```java
        SearchResult res1 = jedis.ftSearch("idx:bicycle", "@description: kids");
        System.out.println(res1.getTotalResults()); // >>> 2

        List<Document> docs1 = res1.getDocuments();

        for (int i = 0; i < docs1.size(); i++) {
            System.out.println(docs1.get(i).getId());
        }
        // >>> bicycle:2
        // >>> bicycle:1
```

##### JavaScript (Node.js)

```javascript
const res1 = await client.ft.search('idx:bicycle', '@description: kids');
console.log(res1.total); // >>> 2
```

##### Python

```python
res = index.search(Query("@description: kids"))
print(res.total)
# >>> 2
```



## Phrase

A phrase is a sentence, sentence fragment, or small group of words. You can find further details about how to find exact phrases in the [exact match article](https://redis.io/docs/latest/develop/ai/search-and-query/query/exact-match).


## Word prefix

You can also search for words that match a given prefix.

```
FT.SEARCH index "prefix*"
```

```
FT.SEARCH index "@field: prefix*"
```

> [!NOTE] Important
> The prefix needs to be at least two characters long.

Here is an example that shows you how to search for bicycles with a brand that starts with 'ka':

Prefix matching: Search for words with a specific prefix using wildcard syntax when you need to find documents with words starting with certain characters

**Difficulty:** Intermediate

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), Python

##### Redis CLI

```
FT.SEARCH idx:bicycle "@model: ka*"
```

##### C#

```csharp
        SearchResult res2 = db.FT().Search(
            "idx:bicycle",
            new("@model: ka*")
        );
        Console.WriteLine(res2.TotalResults);   // >>> 1
```

##### Go

```go
	res2, err := rdb.FTSearch(ctx,
		"idx:bicycle", "@model: ka*",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2.Total) // >>> 1

	for _, doc := range res2.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:4
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<SearchReply<String, String>> startsWithResults = asyncCommands
                    .ftSearch("idx:bicycle", "@model: ka*").thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:4
                        return res;
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<SearchReply<String, String>> startsWithResults = reactiveCommands.ftSearch("idx:bicycle", "@model: ka*")
                    .doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                            // >>> ID: bicycle:4
                        });
                    });
```

##### Java (Synchronous - Jedis)

```java
        SearchResult res2 = jedis.ftSearch("idx:bicycle", "@model: ka*");
        System.out.println(res2.getTotalResults()); // >>> 1

        List<Document> docs2 = res2.getDocuments();

        for (int i = 0; i < docs2.size(); i++) {
            System.out.println(docs2.get(i).getId());
        }
        // >>> bicycle:4
```

##### JavaScript (Node.js)

```javascript
const res2 = await client.ft.search('idx:bicycle', '@model: ka*');
console.log(res2.total); // >>> 1
```

##### Python

```python
res = index.search(Query("@model: ka*"))
print(res.total)
# >>> 1
```



## Word suffix

Similar to the prefix, it is also possible to search for words that share the same suffix.

```
FT.SEARCH index "*suffix"
```

You can also combine prefix- and suffix-based searches within a query expression.

```
FT.SEARCH index "*infix*"
```

Here is an example that finds all brands that end with 'bikes':

Suffix/infix matching: Search for words with a specific suffix or infix using wildcard syntax when you need to find documents with words ending or containing certain characters

**Difficulty:** Intermediate

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), Python

##### Redis CLI

```
FT.SEARCH idx:bicycle "@brand:*bikes"
```

##### C#

```csharp
        SearchResult res3 = db.FT().Search(
            "idx:bicycle",
            new("@brand: *bikes")
        );
        Console.WriteLine(res3.TotalResults);   // >>> 2
```

##### Go

```go
	res3, err := rdb.FTSearch(ctx,
		"idx:bicycle", "@brand: *bikes",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3.Total) // >>> 2

	sort.Slice(res3.Docs, func(i, j int) bool {
		return res3.Docs[i].ID < res3.Docs[j].ID
	})
	for _, doc := range res3.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:4
	// >>> bicycle:6
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<SearchReply<String, String>> endsWithResults = asyncCommands
                    .ftSearch("idx:bicycle", "@brand: *bikes").thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:4
                        // >>> ID: bicycle:6
                        return res;
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<SearchReply<String, String>> endsWithResults = reactiveCommands.ftSearch("idx:bicycle", "@brand: *bikes")
                    .doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                            // >>> ID: bicycle:4
                            // >>> ID: bicycle:6
                        });
                    });
```

##### Java (Synchronous - Jedis)

```java
        SearchResult res3 = jedis.ftSearch("idx:bicycle", "@brand: *bikes");
        System.out.println(res3.getTotalResults()); // >>> 2

        List<Document> docs3 = res3.getDocuments();

        for (int i = 0; i < docs3.size(); i++) {
            System.out.println(docs3.get(i).getId());
        }
        // >>> bicycle:6
        // >>> bicycle:4
```

##### JavaScript (Node.js)

```javascript
const res3 = await client.ft.search('idx:bicycle', '@brand: *bikes');
console.log(res3.total); // >>> 2
```

##### Python

```python
res = index.search(Query("@brand: *bikes"))
print(res.total)
# >>> 2
```



## Fuzzy search

A fuzzy search allows you to find documents with words that approximately match your search term. To perform a fuzzy search, you wrap search terms with pairs of `%` characters. A single pair represents a (Levenshtein) distance of one, two pairs represent a distance of two, and three pairs, the maximum distance, represents a distance of three.

Here is the command that searches across all text fields with a distance of one:

```
FT.SEARCH index "%word%"
```

The following example finds all documents that contain a word that has a distance of one to the incorrectly spelled word 'optamized'. You can see that this matches the word 'optimized'.

Fuzzy search: Search for words with approximate matches using fuzzy search with single % delimiters when you need to find documents despite spelling variations or typos

**Difficulty:** Intermediate

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), Python

##### Redis CLI

```
FT.SEARCH idx:bicycle "%optamized%"
```

##### C#

```csharp
        SearchResult res4 = db.FT().Search(
            "idx:bicycle",
            new("%optamized%")
        );
        Console.WriteLine(res4.TotalResults);   // >>> 1
```

##### Go

```go
	res4, err := rdb.FTSearch(ctx,
		"idx:bicycle", "%optamized%",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4.Total) // >>> 1

	for _, doc := range res4.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:3
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<SearchReply<String, String>> fuzzyResults = asyncCommands.ftSearch("idx:bicycle", "%optamized%")
                    .thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:3
                        return res;
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<SearchReply<String, String>> fuzzyResults = reactiveCommands.ftSearch("idx:bicycle", "%optamized%")
                    .doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                            // >>> ID: bicycle:3
                        });
                    });
```

##### Java (Synchronous - Jedis)

```java
        SearchResult res4 = jedis.ftSearch("idx:bicycle", "%optamized%");
        System.out.println(res4.getTotalResults()); // >>> 1

        List<Document> docs4 = res4.getDocuments();

        for (int i = 0; i < docs4.size(); i++) {
            System.out.println(docs4.get(i).getId());
        }
        // >>> bicycle:3
```

##### JavaScript (Node.js)

```javascript
const res4 = await client.ft.search('idx:bicycle', '%optamized%');
console.log(res4); // >>> { total: 1, documents: [ { id: 'bicycle:3', value: [Object: null prototype] } ]}
```

##### Python

```python
res = index.search(Query("%optamized%"))
print(res)
# >>> Result{1 total, docs: [Document {'id': 'bicycle:3', 'payload': None, 'json': '{"pickup_zone":"POLYGON((-80.2433 25.8067, -80.1333 25.8067, -80.1333 25.6967, -80.2433 25.6967, -80.2433 25.8067))","store_location":"-80.1918,25.7617","brand":"Eva","model":"Eva 291","price":3400,"description":"The sister company to Nord, Eva launched in 2005 as the first and only women-dedicated bicycle brand. Designed by women for women, allEva bikes are optimized for the feminine physique using analytics from a body metrics database. If you like 29ers, try the Eva 291. It’s a brand new bike for 2022.. This full-suspension, cross-country ride has been designed for velocity. The 291 has 100mm of front and rear travel, a superlight aluminum frame and fast-rolling 29-inch wheels. Yippee!","condition":"used"}'}]}
```



If you want to increase the maximum word distance to two, you can use the following query:

Fuzzy search: Search for words with larger approximate matches using fuzzy search with double %% delimiters when you need to tolerate greater spelling variations

**Difficulty:** Intermediate

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), Python

##### Redis CLI

```
FT.SEARCH idx:bicycle "%%optamised%%"
```

##### C#

```csharp
        SearchResult res5 = db.FT().Search(
            "idx:bicycle",
            new("%%optamised%%")
        );
        Console.WriteLine(res5.TotalResults);   // >>> 1
```

##### Go

```go
	res5, err := rdb.FTSearch(ctx,
		"idx:bicycle", "%%optamised%%",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res5.Total) // >>> 1

	for _, doc := range res5.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:3
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<SearchReply<String, String>> fuzzierResults = asyncCommands
                    .ftSearch("idx:bicycle", "%%optamised%%").thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:3
                        return res;
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<SearchReply<String, String>> fuzzierResults = reactiveCommands.ftSearch("idx:bicycle", "%%optamised%%")
                    .doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                            // >>> ID: bicycle:3
                        });
                    });
```

##### Java (Synchronous - Jedis)

```java
        SearchResult res5 = jedis.ftSearch("idx:bicycle", "%%optamised%%");
        System.out.println(res5.getTotalResults()); // >>> 1

        List<Document> docs5 = res5.getDocuments();

        for (int i = 0; i < docs5.size(); i++) {
            System.out.println(docs5.get(i).getId());
        }
        // >>> bicycle:3
```

##### JavaScript (Node.js)

```javascript
const res5 = await client.ft.search('idx:bicycle', '%%optamised%%');
console.log(res5); // >>> { total: 1, documents: [ { id: 'bicycle:3', value: [Object: null prototype] } ]}
```

##### Python

```python
res = index.search(Query("%%optamised%%"))
print(res)
# >>> Result{1 total, docs: [Document {'id': 'bicycle:3', 'payload': None, 'json': '{"pickup_zone":"POLYGON((-80.2433 25.8067, -80.1333 25.8067, -80.1333 25.6967, -80.2433 25.6967, -80.2433 25.8067))","store_location":"-80.1918,25.7617","brand":"Eva","model":"Eva 291","price":3400,"description":"The sister company to Nord, Eva launched in 2005 as the first and only women-dedicated bicycle brand. Designed by women for women, allEva bikes are optimized for the feminine physique using analytics from a body metrics database. If you like 29ers, try the Eva 291. It’s a brand new bike for 2022.. This full-suspension, cross-country ride has been designed for velocity. The 291 has 100mm of front and rear travel, a superlight aluminum frame and fast-rolling 29-inch wheels. Yippee!","condition":"used"}'}]}
```



### Fuzzy search on a specific attribute

To perform a fuzzy search on a specific text field, use the `@field:(...)` syntax with the fuzzy term inside parentheses.

```
FT.SEARCH index "@field:(%word%)"
```

> [!NOTE] Important
> Do not use quotes around the fuzzy term when targeting a specific field. Wrapping the term in quotes (for example, `@field:("%word%")`) converts the query into an exact match search, and the `%` characters are treated as literal characters rather than fuzzy operators.

The following example shows the correct way to perform a fuzzy search with distance one on the `description` field:

```
FT.SEARCH idx:bicycle "@description:(%optamized%)"
```

For a fuzzy search with distance two on a specific field:

```
FT.SEARCH idx:bicycle "@description:(%%optamised%%)"
```

You can also combine fuzzy searches on multiple fields using boolean operators:

```
FT.SEARCH idx:bicycle "@description:(%optamized%) | @model:(%jigar%)"
```

## Unicode considerations

Redis Search only supports Unicode characters in the [basic multilingual plane](https://en.wikipedia.org/wiki/Plane_(Unicode)#Basic_Multilingual_Plane); U+0000 to U+FFFF. Unicode characters beyond U+FFFF, such as Emojis, are not supported and would not be retrieved by queries including such characters in the following use cases:

* Querying TEXT fields with Prefix/Suffix/Infix
* Querying TEXT fields with fuzzy

Examples:

```
redis> FT.CREATE idx SCHEMA tag TAG text TEXT
OK
redis> HSET doc:1 tag '😀😁🙂' text '😀😁🙂'
(integer) 2
redis> HSET doc:2 tag '😀😁🙂abc' text '😀😁🙂abc'
(integer) 2
redis> FT.SEARCH idx '@text:(*😀😁🙂)' NOCONTENT
1) (integer) 0
redis> FT.SEARCH idx '@text:(*😀😁🙂*)' NOCONTENT
1) (integer) 0
redis> FT.SEARCH idx '@text:(😀😁🙂*)' NOCONTENT
1) (integer) 0

redis> FT.SEARCH idx '@text:(%😀😁🙃%)' NOCONTENT
1) (integer) 0
```
