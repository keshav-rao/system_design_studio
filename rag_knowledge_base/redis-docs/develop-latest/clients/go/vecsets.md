# Vector set embeddings

```json metadata
{
  "schema_version": 2,
  "title": "Vector set embeddings",
  "description": "Index and query embeddings with Redis vector sets",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "topics": ["vector sets","vectors"],
  "relatedPages": ["/develop/clients/go/vecsearch"],
  "scope": "example",
  "tableOfContents": {"sections":[{"id":"initialize","title":"Initialize"},{"id":"create-the-data","title":"Create the data"},{"id":"add-the-data-to-a-vector-set","title":"Add the data to a vector set"},{"id":"query-the-vector-set","title":"Query the vector set"},{"id":"more-information","title":"More information"}]}

,
  "codeExamples": [{"codetabsId":"home_vecsets-stepimport","description":"Foundational: Import required packages for vector set operations and text embeddings","difficulty":"beginner","id":"import","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_home_vecsets-stepimport"}]},{"codetabsId":"home_vecsets-stepmodel","description":"Practical pattern: Initialize a sentence transformer model for generating text embeddings","difficulty":"beginner","id":"model","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_home_vecsets-stepmodel"}]},{"codetabsId":"home_vecsets-stepdata","description":"Foundational: Create sample data with descriptions of famous people for vector set storage","difficulty":"beginner","id":"data","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_home_vecsets-stepdata"}]},{"codetabsId":"home_vecsets-stepadd_data","description":"Foundational: Generate embeddings and add data to a vector set with VAdd including attribute metadata","difficulty":"intermediate","id":"add_data","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_home_vecsets-stepadd_data"}]},{"codetabsId":"home_vecsets-stepbasic_query","description":"Vector similarity search: Find semantically similar items in a vector set using VSIM command","difficulty":"intermediate","id":"basic_query","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_home_vecsets-stepbasic_query"}]},{"codetabsId":"home_vecsets-steplimited_query","description":"Vector similarity search with limits: Restrict results to the top K most similar items using the count parameter","difficulty":"intermediate","id":"limited_query","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_home_vecsets-steplimited_query"}]},{"codetabsId":"home_vecsets-stepentertainer_query","description":"Semantic search: Leverage text embeddings to find semantically similar items even when exact keywords don\u0026amp;#39;t match","difficulty":"intermediate","id":"entertainer_query","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_home_vecsets-stepentertainer_query"}]},{"codetabsId":"home_vecsets-stepfiltered_query","description":"Filtered vector search: Combine vector similarity with attribute filters to narrow results based on metadata conditions","difficulty":"advanced","id":"filtered_query","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_home_vecsets-stepfiltered_query"}]}]
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


A Redis [vector set](https://redis.io/docs/latest/develop/data-types/vector-sets) lets
you store a set of unique keys, each with its own associated vector.
You can then retrieve keys from the set according to the similarity between
their stored vectors and a query vector that you specify.

You can use vector sets to store any type of numeric vector but they are
particularly optimized to work with text embedding vectors (see
[Redis for AI](https://redis.io/docs/latest/develop/ai) to learn more about text
embeddings). The example below shows how to use the
[`Hugot`](https://github.com/knights-analytics/hugot)
library to generate vector embeddings and then
store and retrieve them using a vector set with `go-redis`.

## Initialize

Start by [installing](https://redis.io/docs/latest/develop/clients/go#install) `go-redis` if you haven't already done so. Note that you need `go-redis`
[v9.10.0](https://github.com/redis/go-redis/releases/tag/v9.10.0)
or later to use vector sets.

Also, install `hugot`:

```bash
go get github.com/knights-analytics/hugot
```

In a new Go file, add the required imports:

Foundational: Import required packages for vector set operations and text embeddings

**Difficulty:** Beginner

**Available in:** Go

##### Go

```go
package main

import (
	"context"
	"fmt"
	"strings"

	"github.com/knights-analytics/hugot"
	"github.com/redis/go-redis/v9"
)

```



These include the `Hugot` library to generate an embedding from a section of text.
This example uses an instance of the `SentenceTransformer` model
[`all-MiniLM-L6-v2`](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
for the embeddings. This model generates vectors with 384 dimensions, regardless
of the length of the input text, but note that the input is truncated to 256
tokens (see
[Word piece tokenization](https://huggingface.co/learn/nlp-course/en/chapter6/6)
at the [Hugging Face](https://huggingface.co/) docs to learn more about the way tokens
are related to the original text).

Practical pattern: Initialize a sentence transformer model for generating text embeddings

**Difficulty:** Beginner

**Available in:** Go

##### Go

```go
	// Create a new Hugot session
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

	// Download the model.
	downloadOptions := hugot.NewDownloadOptions()
	downloadOptions.OnnxFilePath = "onnx/model.onnx"
	modelPath, err := hugot.DownloadModel(
		"sentence-transformers/all-MiniLM-L6-v2",
		"./models/",
		downloadOptions,
	)
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



## Create the data

The example data is contained in a map with some brief
descriptions of famous people:

Foundational: Create sample data with descriptions of famous people for vector set storage

**Difficulty:** Beginner

**Available in:** Go

##### Go

```go
type PersonData struct {
	Born        int
	Died        int
	Description string
}

var peopleData = map[string]PersonData{
	"Marie Curie": {
		Born: 1867, Died: 1934,
		Description: `Polish-French chemist and physicist. The only person ever to win
		two Nobel prizes for two different sciences.
		`,
	},
	"Linus Pauling": {
		Born: 1901, Died: 1994,
		Description: `American chemist and peace activist. One of only two people to win two
		Nobel prizes in different fields (chemistry and peace).
		`,
	},
	"Freddie Mercury": {
		Born: 1946, Died: 1991,
		Description: `British musician, best known as the lead singer of the rock band
		Queen.
		`,
	},
	"Marie Fredriksson": {
		Born: 1958, Died: 2019,
		Description: `Swedish multi-instrumentalist, mainly known as the lead singer and
		keyboardist of the band Roxette.
		`,
	},
	"Paul Erdos": {
		Born: 1913, Died: 1996,
		Description: `Hungarian mathematician, known for his eccentric personality almost
		as much as his contributions to many different fields of mathematics.
		`,
	},
	"Maryam Mirzakhani": {
		Born: 1977, Died: 2017,
		Description: `Iranian mathematician. The first woman ever to win the Fields medal
		for her contributions to mathematics.
		`,
	},
	"Masako Natsume": {
		Born: 1957, Died: 1985,
		Description: `Japanese actress. She was very famous in Japan but was primarily
		known elsewhere in the world for her portrayal of Tripitaka in the
		TV series Monkey.
		`,
	},
	"Chaim Topol": {
		Born: 1935, Died: 2023,
		Description: `Israeli actor and singer, usually credited simply as 'Topol'. He was
		best known for his many appearances as Tevye in the musical Fiddler
		on the Roof.
		`,
	},
}

```



## Add the data to a vector set

The next step is to connect to Redis and add the data to a new vector set.

The code below iterates through the `peopleData` map and adds corresponding
elements to a vector set called `famousPeople`.

Use the
`RunPipeline()` method of `embeddingPipeline` to generate the
embedding as an array of `float32` values, then use a loop like the one
shown below to convert the `float32` array to a `float64` array.
You can then pass this array to the
[`VAdd()`](https://redis.io/docs/latest/commands/vadd) command to set the embedding.

The call to `VAdd()` also adds the `born` and `died` values from the
original map as attribute data. You can access this during a query
or by using the [`VGetAttr()`](https://redis.io/docs/latest/commands/vgetattr) method.

Foundational: Generate embeddings and add data to a vector set with VAdd including attribute metadata

**Difficulty:** Intermediate

**Available in:** Go

##### Go

```go
	for name, details := range peopleData {
		// Generate embeddings using Hugot
		result, err := embeddingPipeline.RunPipeline([]string{details.Description})
		if err != nil {
			panic(err)
		}

		// Convert embedding to float64 slice
		embFloat32 := result.Embeddings[0]
		embFloat64 := make([]float64, len(embFloat32))
		for i, v := range embFloat32 {
			embFloat64[i] = float64(v)
		}

		// Add vector to vector set
		_, err = rdb.VAdd(ctx, "famousPeople", name, &redis.VectorValues{Val: embFloat64}).Result()
		if err != nil {
			panic(err)
		}

		// Set attributes for the element
		_, err = rdb.VSetAttr(ctx, "famousPeople", name, map[string]interface{}{
			"born": details.Born,
			"died": details.Died,
		}).Result()
		if err != nil {
			panic(err)
		}
	}
```



## Query the vector set

You can now query the data in the set. The basic approach is to use the
`RunPipeline()` method to generate another embedding vector for the query text.
(This is the same method used to add the elements to the set.) Then, pass
the query vector to [`VSim()`](https://redis.io/docs/latest/commands/vsim) to return elements
of the set, ranked in order of similarity to the query.

Start with a simple query for "actors":

Vector similarity search: Find semantically similar items in a vector set using VSIM command

**Difficulty:** Intermediate

**Available in:** Go

##### Go

```go
	queryValue := "actors"

	queryResult, err := embeddingPipeline.RunPipeline([]string{queryValue})
	if err != nil {
		panic(err)
	}

	// Convert embedding to float64 slice
	queryFloat32 := queryResult.Embeddings[0]
	queryFloat64 := make([]float64, len(queryFloat32))
	for i, v := range queryFloat32 {
		queryFloat64[i] = float64(v)
	}

	actorsResults, err := rdb.VSim(ctx, "famousPeople", &redis.VectorValues{Val: queryFloat64}).Result()
	if err != nil {
		panic(err)
	}

	fmt.Printf("'actors': %v\n", strings.Join(actorsResults, ", "))
	// >>> 'actors': Masako Natsume, Chaim Topol, Linus Pauling,
	// Marie Fredriksson, Maryam Mirzakhani, Marie Curie, Freddie Mercury,
	// Paul Erdos
```



This returns the following list of elements (formatted slightly for clarity):

```
'actors': Masako Natsume, Chaim Topol, Linus Pauling, Marie Fredriksson,
    Maryam Mirzakhani, Marie Curie, Freddie Mercury, Paul Erdos
```

The first two people in the list are the two actors, as expected, but none of the
people from Linus Pauling onward was especially well-known for acting (and there certainly
isn't any information about that in the short description text).
As it stands, the search attempts to rank all the elements in the set, based
on the information contained in the embedding model.
You can use the `Count` parameter of `VSimWithArgs()` to limit the list of elements
to just the most relevant few items:

Vector similarity search with limits: Restrict results to the top K most similar items using the count parameter

**Difficulty:** Intermediate

**Available in:** Go

##### Go

```go
	queryValue = "actors"

	queryResult, err = embeddingPipeline.RunPipeline([]string{queryValue})
	if err != nil {
		panic(err)
	}

	// Convert embedding to float64 slice
	queryFloat32 = queryResult.Embeddings[0]
	queryFloat64 = make([]float64, len(queryFloat32))
	for i, v := range queryFloat32 {
		queryFloat64[i] = float64(v)
	}

	twoActorsResults, err := rdb.VSimWithArgs(ctx, "famousPeople",
		&redis.VectorValues{Val: queryFloat64},
		&redis.VSimArgs{Count: 2}).Result()
	if err != nil {
		panic(err)
	}

	fmt.Printf("'actors (2)': %v\n", strings.Join(twoActorsResults, ", "))
	// >>> 'actors (2)': Masako Natsume, Chaim Topol
```



The reason for using text embeddings rather than simple text search
is that the embeddings represent semantic information. This allows a query
to find elements with a similar meaning even if the text is
different. For example, the word "entertainer" doesn't appear in any of the
descriptions but if you use it as a query, the actors and musicians are ranked
highest in the results list:

Semantic search: Leverage text embeddings to find semantically similar items even when exact keywords don't match

**Difficulty:** Intermediate

**Available in:** Go

##### Go

```go
	queryValue = "entertainer"

	queryResult, err = embeddingPipeline.RunPipeline([]string{queryValue})
	if err != nil {
		panic(err)
	}

	// Convert embedding to float64 slice
	queryFloat32 = queryResult.Embeddings[0]
	queryFloat64 = make([]float64, len(queryFloat32))
	for i, v := range queryFloat32 {
		queryFloat64[i] = float64(v)
	}

	entertainerResults, err := rdb.VSim(ctx, "famousPeople", &redis.VectorValues{Val: queryFloat64}).Result()
	if err != nil {
		panic(err)
	}

	fmt.Printf("'entertainer': %v\n", strings.Join(entertainerResults, ", "))
	// >>> 'entertainer': Chaim Topol, Freddie Mercury, Marie Fredriksson,
	// Linus Pauling, Masako Natsume, Paul Erdos,
	// Maryam Mirzakhani, Marie Curie
```



Similarly, if you use "science" as a query, you get the following results:

```
'science': Marie Curie, Linus Pauling, Maryam Mirzakhani, Paul Erdos,
Marie Fredriksson, Freddie Mercury, Masako Natsume, Chaim Topol
```

The scientists are ranked highest but they are then followed by the
mathematicians. This seems reasonable given the connection between mathematics
and science.

You can also use
[filter expressions](https://redis.io/docs/latest/develop/data-types/vector-sets/filtered-search)
with `VSimWithArgs()` to restrict the search further. For example,
repeat the "science" query, but this time limit the results to people
who died before the year 2000:

Filtered vector search: Combine vector similarity with attribute filters to narrow results based on metadata conditions

**Difficulty:** Advanced

**Available in:** Go

##### Go

```go
	queryValue = "science"

	queryResult, err = embeddingPipeline.RunPipeline([]string{queryValue})
	if err != nil {
		panic(err)
	}

	// Convert embedding to float64 slice
	queryFloat32 = queryResult.Embeddings[0]
	queryFloat64 = make([]float64, len(queryFloat32))
	for i, v := range queryFloat32 {
		queryFloat64[i] = float64(v)
	}

	science2000Results, err := rdb.VSimWithArgs(ctx, "famousPeople",
		&redis.VectorValues{Val: queryFloat64},
		&redis.VSimArgs{Filter: ".died < 2000"}).Result()
	if err != nil {
		panic(err)
	}

	fmt.Printf("'science2000': %v\n", strings.Join(science2000Results, ", "))
	// >>> 'science2000': Marie Curie, Linus Pauling, Paul Erdos, Freddie Mercury,
	// Masako Natsume
```



Note that the boolean filter expression is applied to items in the list
before the vector distance calculation is performed. Items that don't
pass the filter test are removed from the results completely, rather
than just reduced in rank. This can help to improve the performance of the
search because there is no need to calculate the vector distance for
elements that have already been filtered out of the search.

## More information

See the [vector sets](https://redis.io/docs/latest/develop/data-types/vector-sets)
docs for more information and code examples. See the
[Redis for AI](https://redis.io/docs/latest/develop/ai) section for more details
about text embeddings and other AI techniques you can use with Redis.

You may also be interested in
[vector search](https://redis.io/docs/latest/develop/clients/go/vecsearch).
This is a feature of
[Redis Search](https://redis.io/docs/latest/develop/ai/search-and-query)
that lets you retrieve
[JSON](https://redis.io/docs/latest/develop/data-types/json) and
[hash](https://redis.io/docs/latest/develop/data-types/hashes) documents based on
vector data stored in their fields.

