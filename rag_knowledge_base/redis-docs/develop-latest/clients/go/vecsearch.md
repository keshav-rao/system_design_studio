# Index and query vectors

```json metadata
{
  "schema_version": 2,
  "title": "Index and query vectors",
  "description": "Learn how to index and query vector embeddings with Redis",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "topics": ["Redis Search","JSON","hash","vectors"],
  "relatedPages": ["/develop/clients/go/queryjson","/develop/clients/go/vecsets","/develop/ai/search-and-query"],
  "scope": "example",
  "tableOfContents": {"sections":[{"id":"initialize","title":"Initialize"},{"id":"add-a-helper-function","title":"Add a helper function"},{"id":"create-the-index","title":"Create the index"},{"id":"create-an-embedder-instance","title":"Create an embedder instance"},{"id":"add-data","title":"Add data"},{"id":"run-a-query","title":"Run a query"},{"id":"differences-with-json-documents","title":"Differences with JSON documents"},{"id":"learn-more","title":"Learn more"}]}

,
  "codeExamples": [{"codetabsId":"home_query_vec-stepimport","description":"Foundational: Import required packages for vector search and embedding operations","difficulty":"beginner","id":"import","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_home_query_vec-stepimport"}]},{"codetabsId":"home_query_vec-stephelper","description":"Foundational: Create a helper function to convert float32 embeddings to binary format for hash storage","difficulty":"beginner","id":"helper","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_home_query_vec-stephelper"}]},{"codetabsId":"home_query_vec-stepconnect","description":"Foundational: Connect to Redis and clean up existing vector indexes","difficulty":"beginner","id":"connect","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_home_query_vec-stepconnect"}]},{"codetabsId":"home_query_vec-stepcreate_index","description":"Foundational: Create a vector search index with HNSW algorithm and L2 distance metric for hash documents","difficulty":"intermediate","id":"create_index","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_home_query_vec-stepcreate_index"}]},{"codetabsId":"home_query_vec-stepembedder","description":"Practical pattern: Initialize a feature extraction pipeline for generating text embeddings","difficulty":"beginner","id":"embedder","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_home_query_vec-stepembedder"}]},{"codetabsId":"home_query_vec-stepadd_data","description":"Foundational: Generate embeddings and store hash documents with vector fields using HSet","difficulty":"intermediate","id":"add_data","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_home_query_vec-stepadd_data"}]},{"codetabsId":"home_query_vec-stepquery","description":"Vector similarity search: Find semantically similar documents by comparing query embeddings with indexed vectors using L2 distance","difficulty":"intermediate","id":"query","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_home_query_vec-stepquery"}]},{"codetabsId":"home_query_vec-stepjson_index","description":"Foundational: Create a vector search index for JSON documents with OnJSON option and JSON path specifications","difficulty":"intermediate","id":"json_index","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_home_query_vec-stepjson_index"}]},{"codetabsId":"home_query_vec-stepjson_data","description":"Foundational: Store JSON documents with vector embeddings as arrays using JSONSet","difficulty":"intermediate","id":"json_data","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_home_query_vec-stepjson_data"}]},{"codetabsId":"home_query_vec-stepjson_query","description":"Vector query: Execute vector similarity search on JSON documents using path aliases for cleaner queries","difficulty":"intermediate","id":"json_query","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_home_query_vec-stepjson_query"}]}]
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


[Redis Search](https://redis.io/docs/latest/develop/ai/search-and-query)
lets you index vector fields in [hash](https://redis.io/docs/latest/develop/data-types/hashes)
or [JSON](https://redis.io/docs/latest/develop/data-types/json) objects (see the
[Vectors](https://redis.io/docs/latest/develop/ai/search-and-query/vectors) 
reference page for more information).
Among other things, vector fields can store *text embeddings*, which are AI-generated vector
representations of the semantic information in pieces of text. The
[vector distance](https://redis.io/docs/latest/develop/ai/search-and-query/vectors#distance-metrics)
between two embeddings indicates how similar they are semantically. By comparing the
similarity of an embedding generated from some query text with embeddings stored in hash
or JSON fields, Redis can retrieve documents that closely match the query in terms
of their meaning.

In the example below, we use the
[`Hugot`](https://pkg.go.dev/github.com/knights-analytics/hugot)
library to generate vector embeddings to store and index with
Redis Search.  The code is first demonstrated for hash documents with a
separate section to explain the
[differences with JSON documents](#differences-with-json-documents).

> [!NOTE]
> From [v9.8.0](https://github.com/redis/go-redis/releases/tag/v9.8.0) onwards,
> `go-redis` uses query dialect 2 by default.
> Redis Search methods such as [`FTSearch()`](https://redis.io/docs/latest/commands/ft.search)
> will explicitly request this dialect, overriding the default set for the server.
> See
> [Query dialects](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/dialects)
> for more information.

## Initialize

First, install [`go-redis`](https://redis.io/docs/latest/develop/clients/go)
if you haven't already done so. Then, install
[`Hugot`](https://pkg.go.dev/github.com/knights-analytics/hugot)
using the following command:

```bash
go get github.com/knights-analytics/hugot
```

Add the following imports to your module's main program file:

Foundational: Import required packages for vector search and embedding operations

**Difficulty:** Beginner

**Available in:** Go

##### Go

```go
package main

import (
	"context"
	"encoding/binary"
	"fmt"
	"math"

	"github.com/knights-analytics/hugot"
	"github.com/redis/go-redis/v9"
)

```



## Add a helper function

The `Hugot` model outputs the embeddings as a
`[]float32` array. If you are storing your documents as
[hash](https://redis.io/docs/latest/develop/data-types/hashes) objects, then you
must convert this array to a `byte` string before adding it as a hash field.
The function shown below uses Go's [`binary`](https://pkg.go.dev/encoding/binary)
package to produce the `byte` string:

Foundational: Create a helper function to convert float32 embeddings to binary format for hash storage

**Difficulty:** Beginner

**Available in:** Go

##### Go

```go
func floatsToBytes(fs []float32) []byte {
	buf := make([]byte, len(fs)*4)

	for i, f := range fs {
		u := math.Float32bits(f)
		binary.NativeEndian.PutUint32(buf[i*4:], u)
	}

	return buf
}

```



Note that if you are using [JSON](https://redis.io/docs/latest/develop/data-types/json)
objects to store your documents instead of hashes, then you should store
the `[]float32` array directly without first converting it to a `byte`
string (see [Differences with JSON documents](#differences-with-json-documents)
below).

## Create the index

In the `main()` function, connect to Redis and delete any index previously
created with the name `vector_idx`:

Foundational: Connect to Redis and clean up existing vector indexes

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

	rdb.FTDropIndexWithArgs(ctx,
		"vector_idx",
		&redis.FTDropIndexOptions{
			DeleteDocs: true,
		},
	)
```



Next, create the index.
The schema in the example below specifies hash objects for storage and includes
three fields: the text content to index, a
[tag](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/tags)
field to represent the "genre" of the text, and the embedding vector generated from
the original text content. The `embedding` field specifies
[HNSW](https://redis.io/docs/latest/develop/ai/search-and-query/vectors#hnsw-index)
indexing, the
[L2](https://redis.io/docs/latest/develop/ai/search-and-query/vectors#distance-metrics)
vector distance metric, `Float32` values to represent the vector's components,
and 384 dimensions, as required by the `all-MiniLM-L6-v2` embedding model.

Foundational: Create a vector search index with HNSW algorithm and L2 distance metric for hash documents

**Difficulty:** Intermediate

**Available in:** Go

##### Go

```go
	_, err := rdb.FTCreate(ctx,
		"vector_idx",
		&redis.FTCreateOptions{
			OnHash: true,
			Prefix: []any{"doc:"},
		},
		&redis.FieldSchema{
			FieldName: "content",
			FieldType: redis.SearchFieldTypeText,
		},
		&redis.FieldSchema{
			FieldName: "genre",
			FieldType: redis.SearchFieldTypeTag,
		},
		&redis.FieldSchema{
			FieldName: "embedding",
			FieldType: redis.SearchFieldTypeVector,
			VectorArgs: &redis.FTVectorArgs{
				HNSWOptions: &redis.FTHNSWOptions{
					Dim:            384,
					DistanceMetric: "L2",
					Type:           "FLOAT32",
				},
			},
		},
	).Result()
	if err != nil {
		panic(err)
	}
```



## Create an embedder instance

You need an instance of the `FeatureExtractionPipeline` class to
generate the embeddings. Use the code below to create an
instance that uses the `sentence-transformers/all-MiniLM-L6-v2`
model:

Practical pattern: Initialize a feature extraction pipeline for generating text embeddings

**Difficulty:** Beginner

**Available in:** Go

##### Go

```go
	// Create a Hugot session
	session, err := hugot.NewGoSession()
	if err != nil {
		panic(err)
	}
	defer func() {
		err := session.Destroy()
		if err != nil {
			panic(err)
		}
	}()

	// Download the model
	downloadOptions := hugot.NewDownloadOptions()
	downloadOptions.OnnxFilePath = "onnx/model.onnx" // Specify which ONNX file to use
	modelPath, err := hugot.DownloadModel("sentence-transformers/all-MiniLM-L6-v2", "./models/", downloadOptions)
	if err != nil {
		panic(err)
	}

	// Create feature extraction pipeline configuration
	config := hugot.FeatureExtractionConfig{
		ModelPath: modelPath,
		Name:      "embeddingPipeline",
	}

	// Create the feature extraction pipeline
	embeddingPipeline, err := hugot.NewPipeline(session, config)
	if err != nil {
		panic(err)
	}
```



## Add data

You can now supply the data objects, which will be indexed automatically
when you add them with [`HSet()`](https://redis.io/docs/latest/commands/hset), as long as
you use the `doc:` prefix specified in the index definition.

Use the `RunPipeline()` method of `FeatureExtractionPipeline`
as shown below to create the embeddings that represent the `content` fields.
This method takes an array of strings and outputs a corresponding
array of `FeatureExtractionOutput` objects.
The `Embeddings` field of `FeatureExtractionOutput` contains the array of float
values that you need for the index. Use the `floatsToBytes()` function defined
above to convert this array to a `byte` string.

Foundational: Generate embeddings and store hash documents with vector fields using HSet

**Difficulty:** Intermediate

**Available in:** Go

##### Go

```go
	sentences := []string{
		"That is a very happy person",
		"That is a happy dog",
		"Today is a sunny day",
	}

	tags := []string{
		"persons", "pets", "weather",
	}

	// Generate embeddings using Hugot
	embeddingResult, err := embeddingPipeline.RunPipeline(sentences)
	if err != nil {
		panic(err)
	}

	// Extract the embeddings from the result
	embeddings := embeddingResult.Embeddings

	for i, emb := range embeddings {
		buffer := floatsToBytes(emb)

		_, err = rdb.HSet(ctx,
			fmt.Sprintf("doc:%v", i),
			map[string]any{
				"content":   sentences[i],
				"genre":     tags[i],
				"embedding": buffer,
			},
		).Result()

		if err != nil {
			panic(err)
		}
	}
```



## Run a query

After you have created the index and added the data, you are ready to run a query.
To do this, you must create another embedding vector from your chosen query
text. Redis calculates the similarity between the query vector and each
embedding vector in the index as it runs the query. It then ranks the
results in order of this numeric similarity value.

The code below creates the query embedding using `RunPipeline()`, as with
the indexing, and passes it as a parameter when the query executes
(see
[Vector search](https://redis.io/docs/latest/develop/ai/search-and-query/query/vector-search)
for more information about using query parameters with embeddings).

Vector similarity search: Find semantically similar documents by comparing query embeddings with indexed vectors using L2 distance

**Difficulty:** Intermediate

**Available in:** Go

##### Go

```go
	// Generate query embedding using Hugot
	queryResult, err := embeddingPipeline.RunPipeline([]string{
		"That is a happy person",
	})

	if err != nil {
		panic(err)
	}

	buffer := floatsToBytes(queryResult.Embeddings[0])

	results, err := rdb.FTSearchWithArgs(ctx,
		"vector_idx",
		"*=>[KNN 3 @embedding $vec AS vector_distance]",
		&redis.FTSearchOptions{
			Return: []redis.FTSearchReturn{
				{FieldName: "vector_distance"},
				{FieldName: "content"},
			},
			DialectVersion: 2,
			Params: map[string]any{
				"vec": buffer,
			},
		},
	).Result()

	if err != nil {
		panic(err)
	}

	for _, doc := range results.Docs {
		fmt.Printf(
			"ID: %v, Distance:%v, Content:'%v'\n",
			doc.ID, doc.Fields["vector_distance"], doc.Fields["content"],
		)
	}
```



The code is now ready to run, but note that it may take a while to complete when
you run it for the first time (which happens because `Hugot`
must download the `all-MiniLM-L6-v2` model data before it can
generate the embeddings). When you run the code, it outputs the following text:

```
ID: doc:0, Distance:2.96992516518, Content:'That is a very happy person'
ID: doc:1, Distance:17.3678302765, Content:'That is a happy dog'
ID: doc:2, Distance:43.7771987915, Content:'Today is a sunny day'
```

The results are ordered according to the value of the `vector_distance`
field, with the lowest distance indicating the greatest similarity to the query.
As you would expect, the result for `doc:0` with the content text *"That is a very happy person"*
is the result that is most similar in meaning to the query text
*"That is a happy person"*.

## Differences with JSON documents

Indexing JSON documents is similar to hash indexing, but there are some
important differences. JSON allows much richer data modelling with nested fields, so
you must supply a [path](https://redis.io/docs/latest/develop/data-types/json/path) in the schema
to identify each field you want to index. However, you can declare a short alias for each
of these paths (using the `As` option) to avoid typing it in full for
every query. Also, you must set `OnJSON` to `true` when you create the index.

The code below shows these differences, but the index is otherwise very similar to
the one created previously for hashes:

Foundational: Create a vector search index for JSON documents with OnJSON option and JSON path specifications

**Difficulty:** Intermediate

**Available in:** Go

##### Go

```go
	rdb.FTDropIndexWithArgs(ctx,
		"vector_json_idx",
		&redis.FTDropIndexOptions{
			DeleteDocs: true,
		},
	)

	_, err = rdb.FTCreate(ctx,
		"vector_json_idx",
		&redis.FTCreateOptions{
			OnJSON: true,
			Prefix: []any{"jdoc:"},
		},
		&redis.FieldSchema{
			FieldName: "$.content",
			As:        "content",
			FieldType: redis.SearchFieldTypeText,
		},
		&redis.FieldSchema{
			FieldName: "$.genre",
			As:        "genre",
			FieldType: redis.SearchFieldTypeTag,
		},
		&redis.FieldSchema{
			FieldName: "$.embedding",
			As:        "embedding",
			FieldType: redis.SearchFieldTypeVector,
			VectorArgs: &redis.FTVectorArgs{
				HNSWOptions: &redis.FTHNSWOptions{
					Dim:            384,
					DistanceMetric: "L2",
					Type:           "FLOAT32",
				},
			},
		},
	).Result()
	if err != nil {
		panic(err)
	}
```



Use [`JSONSet()`](https://redis.io/docs/latest/commands/json.set) to add the data
instead of [`HSet()`](https://redis.io/docs/latest/commands/hset). The maps
that specify the fields have the same structure as the ones used for `HSet()`.

An important difference with JSON indexing is that the vectors are
specified using lists instead of binary strings. The loop below is similar
to the one used previously to add the hash data, but it doesn't use the
`floatsToBytes()` function to encode the `float32` array.

Foundational: Store JSON documents with vector embeddings as arrays using JSONSet

**Difficulty:** Intermediate

**Available in:** Go

##### Go

```go
	for i, emb := range embeddings {
		_, err = rdb.JSONSet(ctx,
			fmt.Sprintf("jdoc:%v", i),
			"$",
			map[string]any{
				"content":   sentences[i],
				"genre":     tags[i],
				"embedding": emb,
			},
		).Result()

		if err != nil {
			panic(err)
		}
	}
```



The query is almost identical to the one for the hash documents. This
demonstrates how the right choice of aliases for the JSON paths can
save you having to write complex queries. An important thing to notice
is that the vector parameter for the query is still specified as a
binary string (using the `floatsToBytes()` method), even though the data for
the `embedding` field of the JSON was specified as an array.

Vector query: Execute vector similarity search on JSON documents using path aliases for cleaner queries

**Difficulty:** Intermediate

**Available in:** Go

##### Go

```go
	// Generate query embedding for JSON search using Hugot
	jsonQueryResult, err := embeddingPipeline.RunPipeline([]string{
		"That is a happy person",
	})

	if err != nil {
		panic(err)
	}

	jsonBuffer := floatsToBytes(jsonQueryResult.Embeddings[0])

	jsonResults, err := rdb.FTSearchWithArgs(ctx,
		"vector_json_idx",
		"*=>[KNN 3 @embedding $vec AS vector_distance]",
		&redis.FTSearchOptions{
			Return: []redis.FTSearchReturn{
				{FieldName: "vector_distance"},
				{FieldName: "content"},
			},
			DialectVersion: 2,
			Params: map[string]any{
				"vec": jsonBuffer,
			},
		},
	).Result()

	if err != nil {
		panic(err)
	}

	for _, doc := range jsonResults.Docs {
		fmt.Printf(
			"ID: %v, Distance:%v, Content:'%v'\n",
			doc.ID, doc.Fields["vector_distance"], doc.Fields["content"],
		)
	}
```



Apart from the `jdoc:` prefixes for the keys, the result from the JSON
query is the same as for hash:

```
ID: jdoc:0, Distance:2.96992516518, Content:'That is a very happy person'
ID: jdoc:1, Distance:17.3678302765, Content:'That is a happy dog'
ID: jdoc:2, Distance:43.7771987915, Content:'Today is a sunny day'
```

## Learn more

See
[Vector search](https://redis.io/docs/latest/develop/ai/search-and-query/query/vector-search)
for more information about the indexing options, distance metrics, and query format
for vectors.

