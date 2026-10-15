# Index and query vectors

```json metadata
{
  "schema_version": 2,
  "title": "Index and query vectors",
  "description": "Learn how to index and query vector embeddings with Redis",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "topics": ["Redis Search","JSON","hash","vectors"],
  "relatedPages": ["/develop/clients/jedis/queryjson","/develop/clients/jedis/vecsets","/develop/ai/search-and-query"],
  "scope": "example",
  "tableOfContents": {"sections":[{"id":"initialize","title":"Initialize"},{"id":"import-dependencies","title":"Import dependencies"},{"id":"define-a-helper-method","title":"Define a helper method"},{"id":"create-a-tokenizer-instance","title":"Create a tokenizer instance"},{"id":"create-the-index","title":"Create the index"},{"id":"add-data","title":"Add data"},{"id":"run-a-query","title":"Run a query"},{"id":"differences-with-json-documents","title":"Differences with JSON documents"},{"id":"learn-more","title":"Learn more"}]}

,
  "codeExamples": [{"codetabsId":"HomeQueryVec-stepimport","description":"Foundational: Import required libraries for vector embeddings, Redis operations, and search functionality","difficulty":"beginner","id":"import","languages":[{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_HomeQueryVec-stepimport"}]},{"codetabsId":"HomeQueryVec-stephelper_method","description":"Foundational: Create a helper method to convert float arrays to binary strings for vector storage in hash objects","difficulty":"beginner","id":"helper_method","languages":[{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_HomeQueryVec-stephelper_method"}]},{"codetabsId":"HomeQueryVec-steptokenizer","description":"Practical pattern: Initialize a tokenizer and embedding model for generating vector representations from text","difficulty":"beginner","id":"tokenizer","languages":[{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_HomeQueryVec-steptokenizer"}]},{"codetabsId":"HomeQueryVec-stepconnect","description":"Foundational: Connect to Redis and clean up existing vector indexes","difficulty":"beginner","id":"connect","languages":[{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_HomeQueryVec-stepconnect"}]},{"codetabsId":"HomeQueryVec-stepcreate_index","description":"Foundational: Create a vector search index for hash documents with HNSW algorithm and L2 distance metric","difficulty":"intermediate","id":"create_index","languages":[{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_HomeQueryVec-stepcreate_index"}]},{"codetabsId":"HomeQueryVec-stepadd_data","description":"Foundational: Store hash documents with vector embeddings generated from text content","difficulty":"beginner","id":"add_data","languages":[{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_HomeQueryVec-stepadd_data"}]},{"codetabsId":"HomeQueryVec-stepquery","description":"Vector similarity search: Find semantically similar documents by comparing query embeddings with indexed vectors using L2 distance","difficulty":"intermediate","id":"query","languages":[{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_HomeQueryVec-stepquery"}]},{"codetabsId":"HomeQueryVec-stepjson_schema","description":"Foundational: Create a vector search index for JSON documents with JSON paths and field aliases","difficulty":"intermediate","id":"json_schema","languages":[{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_HomeQueryVec-stepjson_schema"}]},{"codetabsId":"HomeQueryVec-stepjson_data","description":"Foundational: Store JSON documents with vector embeddings as arrays (different from hash binary format)","difficulty":"beginner","id":"json_data","languages":[{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_HomeQueryVec-stepjson_data"}]},{"codetabsId":"HomeQueryVec-stepjson_query","description":"Vector similarity search: Query JSON documents using vector embeddings with field aliases for simplified syntax","difficulty":"intermediate","id":"json_query","languages":[{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_HomeQueryVec-stepjson_query"}]}]
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

The example below uses the [HuggingFace](https://huggingface.co/) model
[`all-MiniLM-L6-v2`](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
to generate the vector embeddings to store and index with Redis Search.
The code is first demonstrated for hash documents with a
separate section to explain the
[differences with JSON documents](#differences-with-json-documents).

> [!NOTE]
> From [v6.0.0](https://github.com/redis/jedis/releases/tag/v6.0.0) onwards,
> `Jedis` uses query dialect 2 by default.
> Redis Search methods such as [`ftSearch()`](https://redis.io/docs/latest/commands/ft.search)
> will explicitly request this dialect, overriding the default set for the server.
> See
> [Query dialects](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/dialects)
> for more information.

## Initialize

If you are using [Maven](https://maven.apache.org/), add the following
dependencies to your `pom.xml` file:

```xml
<dependency>
    <groupId>redis.clients</groupId>
    <artifactId>jedis</artifactId>
    <version>7.2.0</version>
</dependency>
<dependency>
    <groupId>ai.djl.huggingface</groupId>
    <artifactId>tokenizers</artifactId>
    <version>0.33.0</version>
</dependency>
<dependency>
    <groupId>ai.djl.pytorch</groupId>
    <artifactId>pytorch-model-zoo</artifactId>
    <version>0.33.0</version>
</dependency>
<dependency>
    <groupId>ai.djl</groupId>
    <artifactId>api</artifactId>
    <version>0.33.0</version>
</dependency>
```

If you are using [Gradle](https://gradle.org/), add the following
dependencies to your `build.gradle` file:

```bash
implementation 'redis.clients:jedis:7.2.0'
implementation 'ai.djl.huggingface:tokenizers:0.33.0'
implementation 'ai.djl.pytorch:pytorch-model-zoo:0.33.0'
implementation 'ai.djl:api:0.33.0'
```

## Import dependencies

Import the following classes in your source file:

Foundational: Import required libraries for vector embeddings, Redis operations, and search functionality

**Difficulty:** Beginner

**Available in:** Java (Synchronous - Jedis)

##### Java (Synchronous - Jedis)

```java
import redis.clients.jedis.RedisClient;
import redis.clients.jedis.search.*;
import redis.clients.jedis.search.schemafields.*;
import redis.clients.jedis.search.schemafields.VectorField.VectorAlgorithm;
import redis.clients.jedis.exceptions.JedisDataException;
import redis.clients.jedis.json.Path2;

import org.json.JSONObject;

import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.util.Map;
import java.util.List;

// DJL classes for model loading and inference.
import ai.djl.huggingface.translator.TextEmbeddingTranslatorFactory;
import ai.djl.inference.Predictor;
import ai.djl.repository.zoo.Criteria;
import ai.djl.training.util.ProgressBar;
```



## Define a helper method

The embedding model represents the vectors as an array of `float` values,
which is the format required by Redis Search.
Also, when you store vectors in a hash object, you must encode the vector
array as a `byte` string. To simplify this situation, you can declare a helper
method `floatsToByteString()` that takes the `float` array that the
embedding model returns and encodes it as a `byte` string:

Foundational: Create a helper method to convert float arrays to binary strings for vector storage in hash objects

**Difficulty:** Beginner

**Available in:** Java (Synchronous - Jedis)

##### Java (Synchronous - Jedis)

```java
    public static byte[] floatsToByteString(float[] floats) {
        byte[] bytes = new byte[Float.BYTES * floats.length];
        ByteBuffer
            .wrap(bytes)
            .order(ByteOrder.LITTLE_ENDIAN)
            .asFloatBuffer()
            .put(floats);
        return bytes;
    }
```



## Create a tokenizer instance

The next step is to generate the embeddings using the
[`all-MiniLM-L6-v2`](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
model. The vectors that represent the
embeddings have 384 components, regardless of the length of the input
text, but note that the input is truncated to 256
tokens (see
[Word piece tokenization](https://huggingface.co/learn/nlp-course/en/chapter6/6)

Practical pattern: Initialize a tokenizer and embedding model for generating vector representations from text

**Difficulty:** Beginner

**Available in:** Java (Synchronous - Jedis)

##### Java (Synchronous - Jedis)

```java
        Predictor<String, float[]> predictor = null;

        try {
            Criteria<String, float[]> criteria = Criteria.builder().setTypes(String.class, float[].class)
                    .optModelUrls("djl://ai.djl.huggingface.pytorch/sentence-transformers/all-MiniLM-L6-v2")
                    .optEngine("PyTorch").optTranslatorFactory(new TextEmbeddingTranslatorFactory())
                    .optProgress(new ProgressBar()).build();

            predictor = criteria.loadModel().newPredictor();
        } catch (Exception e) {
            // ...
        }
```



## Create the index

Connect to Redis and delete any index previously created with the
name `vector_idx`. (The `ftDropIndex()` call throws an exception if
the index doesn't already exist, which is why you need the
`try...catch` block.)

Foundational: Connect to Redis and clean up existing vector indexes

**Difficulty:** Beginner

**Available in:** Java (Synchronous - Jedis)

##### Java (Synchronous - Jedis)

```java
        RedisClient jedis = new RedisClient("redis://localhost:6379");
        
        try {jedis.ftDropIndex("vector_idx");} catch (JedisDataException j){}
```



Next, create the index.
The schema in the example below includes three fields: the text content to index, a
[tag](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/tags)
field to represent the "genre" of the text, and the embedding vector generated from
the original text content. The `embedding` field specifies
[HNSW](https://redis.io/docs/latest/develop/ai/search-and-query/vectors#hnsw-index)
indexing, the
[L2](https://redis.io/docs/latest/develop/ai/search-and-query/vectors#distance-metrics)
vector distance metric, `Float32` values to represent the vector's components,
and 384 dimensions, as required by the `all-MiniLM-L6-v2` embedding model.

The `FTCreateParams` object specifies hash objects for storage and a
prefix `doc:` that identifies the hash objects to index.

Foundational: Create a vector search index for hash documents with HNSW algorithm and L2 distance metric

**Difficulty:** Intermediate

**Available in:** Java (Synchronous - Jedis)

##### Java (Synchronous - Jedis)

```java
        SchemaField[] schema = {
            TextField.of("content"),
            TagField.of("genre"),
            VectorField.builder()
                .fieldName("embedding")
                .algorithm(VectorAlgorithm.HNSW)
                .attributes(
                    Map.of(
                        "TYPE", "FLOAT32",
                        "DIM", 384,
                        "DISTANCE_METRIC", "L2"
                    )
                )
                .build()
        };
        
        jedis.ftCreate("vector_idx",
            FTCreateParams.createParams()
                .addPrefix("doc:")
                .on(IndexDataType.HASH),
                schema
        );
        
```



## Add data

You can now supply the data objects, which will be indexed automatically
when you add them with [`hset()`](https://redis.io/docs/latest/commands/hset), as long as
you use the `doc:` prefix specified in the index definition.

Use the `predict()` method of the `Predictor` object
as shown below to create the embedding that represents the `content` field.
The `predict()` method returns a `float[]` array which is then converted to a `byte`
string using the helper method. Use the `byte` string representation when you are
indexing hash objects (as in this example), but use the array of `float` directly for
JSON objects (see [Differences with JSON objects](#differences-with-json-documents)
below). Note that when you set the `embedding` field, you must use an overload
of `hset()` that requires `byte` arrays for each of the key, the field name, and
the value, which is why you must include the `getBytes()` calls on the strings.

Foundational: Store hash documents with vector embeddings generated from text content

**Difficulty:** Beginner

**Available in:** Java (Synchronous - Jedis)

##### Java (Synchronous - Jedis)

```java
        String sentence1 = "That is a very happy person";
        byte[] embedding1;

        try {
            embedding1 = floatsToByteString(predictor.predict(sentence1));
        } catch (Exception e) {
            // This just allows the code to compile without errors.
            // In a real-world scenario, you would handle the exception properly.
            embedding1 = new byte[384 * Float.BYTES];
        }

        jedis.hset("doc:1", Map.of(  "content", sentence1, "genre", "persons"));
        jedis.hset("doc:1".getBytes(), "embedding".getBytes(), embedding1);
        
        String sentence2 = "That is a happy dog";
        byte[] embedding2;

        try {
            embedding2 = floatsToByteString(predictor.predict(sentence2));
        } catch (Exception e) {
            embedding2 = new byte[384 * Float.BYTES];
        }
        
        jedis.hset("doc:2", Map.of(  "content", sentence2, "genre", "pets"));
        jedis.hset("doc:2".getBytes(), "embedding".getBytes(), embedding2);

        String sentence3 = "Today is a sunny day";
        byte[] embedding3;

        try {
            embedding3 = floatsToByteString(predictor.predict(sentence3));
        } catch (Exception e) {
            embedding3 = new byte[384 * Float.BYTES];
        }

        Map<String, String> doc3 = Map.of(  "content", sentence3, "genre", "weather");
        jedis.hset("doc:3", doc3);
        jedis.hset("doc:3".getBytes(), "embedding".getBytes(), embedding3);
```



## Run a query

After you have created the index and added the data, you are ready to run a query.
To do this, you must create another embedding vector from your chosen query
text. Redis calculates the vector distance between the query vector and each
embedding vector in the index as it runs the query. You can request the results to be
sorted to rank them in order of ascending distance.

The code below creates the query embedding using the `predict()` method, as with
the indexing, and passes it as a parameter when the query executes (see
[Vector search](https://redis.io/docs/latest/develop/ai/search-and-query/query/vector-search)
for more information about using query parameters with embeddings).
The query is a
[K nearest neighbors (KNN)](https://redis.io/docs/latest/develop/ai/search-and-query/vectors#knn-vector-search)
search that sorts the results in order of vector distance from the query vector.

Vector similarity search: Find semantically similar documents by comparing query embeddings with indexed vectors using L2 distance

**Difficulty:** Intermediate

**Available in:** Java (Synchronous - Jedis)

##### Java (Synchronous - Jedis)

```java
        String sentence = "That is a happy person";
        byte[] embedding;

        try {
            embedding = floatsToByteString(predictor.predict(sentence));
        } catch (Exception e) {
            embedding = new byte[384 * Float.BYTES];
        }
        
        int K = 3;
        Query q = new Query("*=>[KNN $K @embedding $BLOB AS distance]").
                            returnFields("content", "distance").
                            addParam("K", K).
                            addParam("BLOB", embedding)
                            .setSortBy("distance", true)
                            .dialect(2);

        // Execute the query
        List<Document> docs = jedis.ftSearch("vector_idx", q).getDocuments();
        System.out.println("Results:");
        
        for (Document doc: docs) {
            System.out.println(
                String.format(
                    "ID: %s, Distance: %s, Content: %s",
                    doc.getId(),
                    doc.get("distance"),
                    doc.get("content")
                )
            );
        }
```



Assuming you have added the code from the steps above to your source file,
it is now ready to run, but note that it may take a while to complete when
you run it for the first time (which happens because the tokenizer must download the
`all-MiniLM-L6-v2` model data before it can
generate the embeddings). When you run the code, it outputs the following result text:

```
Results:
ID: doc:1, Distance: 0.114169836044, Content: That is a very happy person
ID: doc:2, Distance: 0.610845506191, Content: That is a happy dog
ID: doc:3, Distance: 1.48624765873, Content: Today is a sunny day
```

Note that the results are ordered according to the value of the `distance`
field, with the lowest distance indicating the greatest similarity to the query.
As expected, the text *"That is a very happy person"*
is the result judged to be most similar in meaning to the query text
*"That is a happy person"*.

## Differences with JSON documents

Indexing JSON documents is similar to hash indexing, but there are some
important differences. JSON allows much richer data modeling with nested fields, so
you must supply a [path](https://redis.io/docs/latest/develop/data-types/json/path) in the schema
to identify each field you want to index. However, you can declare a short alias for each
of these paths (using the `as()` option) to avoid typing it in full for
every query. Also, you must specify `IndexDataType.JSON` when you create the index.

The code below shows these differences, but the index is otherwise very similar to
the one created previously for hashes:

Foundational: Create a vector search index for JSON documents with JSON paths and field aliases

**Difficulty:** Intermediate

**Available in:** Java (Synchronous - Jedis)

##### Java (Synchronous - Jedis)

```java
        SchemaField[] jsonSchema = {
            TextField.of("$.content").as("content"),
            TagField.of("$.genre").as("genre"),
            VectorField.builder()
                .fieldName("$.embedding").as("embedding")
                .algorithm(VectorAlgorithm.HNSW)
                .attributes(
                    Map.of(
                        "TYPE", "FLOAT32",
                        "DIM", 384,
                        "DISTANCE_METRIC", "L2"
                    )
                )
                .build()
        };
        
        jedis.ftCreate("vector_json_idx",
            FTCreateParams.createParams()
                .addPrefix("jdoc:")
                .on(IndexDataType.JSON),
                jsonSchema
        );
```



An important difference with JSON indexing is that the vectors are
specified using arrays of `float` instead of binary strings, so you don't need
a helper method to convert the array to a binary string.

Use [`jsonSet()`](https://redis.io/docs/latest/commands/json.set) to add the data
instead of [`hset()`](https://redis.io/docs/latest/commands/hset). Use instances
of `JSONObject` to supply the data instead of `Map`, as you would for
hash objects.

Foundational: Store JSON documents with vector embeddings as arrays (different from hash binary format)

**Difficulty:** Beginner

**Available in:** Java (Synchronous - Jedis)

##### Java (Synchronous - Jedis)

```java
        String jSentence1 = "That is a very happy person";

        float[] jEmbedding1;

        try {
            jEmbedding1 = predictor.predict(jSentence1);
        } catch (Exception e) {
            // This just allows the code to compile without errors.
            // In a real-world scenario, you would handle the exception properly.
            jEmbedding1 = new float[384];
        }

        JSONObject jdoc1 = new JSONObject()
                .put("content", jSentence1)
                .put("genre", "persons")
                .put(
                    "embedding",
                    jEmbedding1
                );

        jedis.jsonSet("jdoc:1", Path2.ROOT_PATH, jdoc1);

        String jSentence2 = "That is a happy dog";

        float[] jEmbedding2;

        try {
            jEmbedding2 = predictor.predict(jSentence2);
        } catch (Exception e) {
            jEmbedding2 = new float[384];
        }

        JSONObject jdoc2 = new JSONObject()
                .put("content", jSentence2)
                .put("genre", "pets")
                .put(
                    "embedding",
                    jEmbedding2
                );
        
        jedis.jsonSet("jdoc:2", Path2.ROOT_PATH, jdoc2);

        String jSentence3 = "Today is a sunny day";

        float[] jEmbedding3;

        try {
            jEmbedding3 = predictor.predict(jSentence3);
        } catch (Exception e) {
            jEmbedding3 = new float[384];
        }

        JSONObject jdoc3 = new JSONObject()
                .put("content", jSentence3)
                .put("genre", "weather")
                .put(
                    "embedding",
                    jEmbedding3
                );

        jedis.jsonSet("jdoc:3", Path2.ROOT_PATH, jdoc3);
```



The query is almost identical to the one for the hash documents. This
demonstrates how the right choice of aliases for the JSON paths can
save you having to write complex queries. An important thing to notice
is that the vector parameter for the query is still specified as a
binary string (created using the `floatsToByteString()` method), even though
the data for the `embedding` field of the JSON was specified as an array.

Vector similarity search: Query JSON documents using vector embeddings with field aliases for simplified syntax

**Difficulty:** Intermediate

**Available in:** Java (Synchronous - Jedis)

##### Java (Synchronous - Jedis)

```java
        String jSentence = "That is a happy person";
        byte[] jEmbedding;

        try {
            jEmbedding = floatsToByteString(predictor.predict(jSentence));
        } catch (Exception e) {
            jEmbedding = new byte[384 * Float.BYTES];
        }

        int jK = 3;
        Query jq = new Query("*=>[KNN $K @embedding $BLOB AS distance]").
                            returnFields("content", "distance").
                            addParam("K", jK).
                            addParam(
                                "BLOB",
                                jEmbedding
                            )
                            .setSortBy("distance", true)
                            .dialect(2);

        // Execute the query
        List<Document> jDocs = jedis
                .ftSearch("vector_json_idx", jq)
                .getDocuments();

        System.out.println("Results:");
        
        for (Document doc: jDocs) {
            System.out.println(
                String.format(
                    "ID: %s, Distance: %s, Content: %s",
                    doc.getId(),
                    doc.get("distance"),
                    doc.get("content")
                )
            );
        }
```



Apart from the `jdoc:` prefixes for the keys, the result from the JSON
query is the same as for hash:

```
Results:
ID: jdoc:1, Distance: 0.114169836044, Content: That is a very happy person
ID: jdoc:2, Distance: 0.610845506191, Content: That is a happy dog
ID: jdoc:3, Distance: 1.48624765873, Content: Today is a sunny day
```

## Learn more

See
[Vector search](https://redis.io/docs/latest/develop/ai/search-and-query/query/vector-search)
for more information about the indexing options, distance metrics, and query format
for vectors.

