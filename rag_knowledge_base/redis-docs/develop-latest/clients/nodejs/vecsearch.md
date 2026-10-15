# Index and query vectors

```json metadata
{
  "schema_version": 2,
  "title": "Index and query vectors",
  "description": "Learn how to index and query vector embeddings with Redis",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "topics": ["Redis Search","JSON","hash","vectors"],
  "relatedPages": ["/develop/clients/nodejs/queryjson","/develop/clients/nodejs/vecsets","/develop/ai/search-and-query"],
  "scope": "example",
  "tableOfContents": {"sections":[{"id":"initialize","title":"Initialize"},{"id":"create-the-index","title":"Create the index"},{"id":"add-data","title":"Add data"},{"id":"run-a-query","title":"Run a query"},{"id":"differences-with-json-documents","title":"Differences with JSON documents"},{"id":"learn-more","title":"Learn more"}]}

,
  "codeExamples": [{"codetabsId":"home_query_vec-stepimport","description":"Foundational: Import Redis client and transformer modules for vector embedding operations","difficulty":"beginner","id":"import","languages":[{"id":"Node-js","panelId":"panel_Nodejs_home_query_vec-stepimport"}]},{"codetabsId":"home_query_vec-steppipeline","description":"Foundational: Configure a transformer pipeline to generate vector embeddings from text","difficulty":"beginner","id":"pipeline","languages":[{"id":"Node-js","panelId":"panel_Nodejs_home_query_vec-steppipeline"}]},{"codetabsId":"home_query_vec-stepconnect","description":"Foundational: Connect to Redis and clean up existing vector indexes","difficulty":"beginner","id":"connect","languages":[{"id":"Node-js","panelId":"panel_Nodejs_home_query_vec-stepconnect"}]},{"codetabsId":"home_query_vec-stepcreate_index","description":"Foundational: Create a vector search index with HNSW algorithm and L2 distance metric for semantic search","difficulty":"intermediate","id":"create_index","languages":[{"id":"Node-js","panelId":"panel_Nodejs_home_query_vec-stepcreate_index"}]},{"codetabsId":"home_query_vec-stepadd_data","description":"Practical pattern: Generate embeddings and store documents with vector fields using pipelined hSet() commands","difficulty":"intermediate","id":"add_data","languages":[{"id":"Node-js","panelId":"panel_Nodejs_home_query_vec-stepadd_data"}]},{"codetabsId":"home_query_vec-stepquery","description":"Vector query: Execute a vector similarity search by generating a query embedding and finding nearest neighbors","difficulty":"intermediate","id":"query","languages":[{"id":"Node-js","panelId":"panel_Nodejs_home_query_vec-stepquery"}]},{"codetabsId":"home_query_vec-stepjson_index","description":"Foundational: Create a vector search index for JSON documents with path aliases and nested field support","difficulty":"intermediate","id":"json_index","languages":[{"id":"Node-js","panelId":"panel_Nodejs_home_query_vec-stepjson_index"}]},{"codetabsId":"home_query_vec-stepjson_data","description":"Practical pattern: Store JSON documents with vector embeddings converted to arrays for nested field support","difficulty":"intermediate","id":"json_data","languages":[{"id":"Node-js","panelId":"panel_Nodejs_home_query_vec-stepjson_data"}]},{"codetabsId":"home_query_vec-stepjson_query","description":"Vector query: Execute vector similarity search on JSON documents with the same query syntax as hash documents","difficulty":"intermediate","id":"json_query","languages":[{"id":"Node-js","panelId":"panel_Nodejs_home_query_vec-stepjson_query"}]}]
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

Vector fields can store *text embeddings*, which are AI-generated vector
representations of text content. The
[vector distance](https://redis.io/docs/latest/develop/ai/search-and-query/vectors#distance-metrics)
between two embeddings measures their semantic similarity. When you compare the
similarity of a query embedding with stored embeddings, Redis can retrieve documents
that closely match the query's meaning.

In the example below, we use the
[`@xenova/transformers`](https://www.npmjs.com/package/@xenova/transformers)
library to generate vector embeddings to store and index with
Redis Search. The code is first demonstrated for hash documents with a
separate section to explain the
[differences with JSON documents](#differences-with-json-documents).

> [!NOTE]
> From [v5.0.0](https://github.com/redis/node-redis/releases/tag/redis%405.0.0)
> onwards, `node-redis` uses query dialect 2 by default.
> Redis Search methods such as [`ft.search()`](https://redis.io/docs/latest/commands/ft.search)
> will explicitly request this dialect, overriding the default set for the server.
> See
> [Query dialects](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/dialects)
> for more information.

## Initialize

Install the required dependencies:

1. Install [`node-redis`](https://redis.io/docs/latest/develop/clients/nodejs) if you haven't already.
2. Install `@xenova/transformers`:

```bash
npm install @xenova/transformers
```

In your JavaScript source file, import the required classes:

Foundational: Import Redis client and transformer modules for vector embedding operations

**Difficulty:** Beginner

**Available in:** JavaScript (Node.js)

##### JavaScript (Node.js)

```javascript
import * as transformers from '@xenova/transformers';
import {
    VectorAlgorithms,
    createClient,
    SchemaFieldTypes,
} from 'redis';
```



The `@xenova/transformers` module handles embedding models. This example uses the
[`all-distilroberta-v1`](https://huggingface.co/sentence-transformers/all-distilroberta-v1)
model, which:
- Generates 768-dimensional vectors
- Truncates input to 128 tokens
- Uses word piece tokenization (see [Word piece tokenization](https://huggingface.co/learn/nlp-course/en/chapter6/6)
  at the [Hugging Face](https://huggingface.co/) docs for details)

The `pipe` function generates embeddings. The `pipeOptions` object specifies how to generate sentence embeddings from token embeddings (see the
[`all-distilroberta-v1`](https://huggingface.co/sentence-transformers/all-distilroberta-v1)
documentation for details):

Foundational: Configure a transformer pipeline to generate vector embeddings from text

**Difficulty:** Beginner

**Available in:** JavaScript (Node.js)

##### JavaScript (Node.js)

```javascript
let pipe = await transformers.pipeline(
    'feature-extraction', 'Xenova/all-distilroberta-v1'
);

const pipeOptions = {
    pooling: 'mean',
    normalize: true,
};
```



## Create the index

First, connect to Redis and remove any existing index named `vector_idx`:

Foundational: Connect to Redis and clean up existing vector indexes

**Difficulty:** Beginner

**Available in:** JavaScript (Node.js)

##### JavaScript (Node.js)

```javascript
const client = createClient({url: 'redis://localhost:6379'});
await client.connect();

try { 
    await client.ft.dropIndex('vector_idx'); 
} catch (e) {
    // Index doesn't exist, which is fine
}
```



Next, create the index with the following schema:
-   `content`: Text field for the content to index
-   `genre`: [Tag](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/tags)
    field representing the text's genre
-   `embedding`: [Vector](https://redis.io/docs/latest/develop/ai/search-and-query/vectors)
    field with:
    -   [HNSW](https://redis.io/docs/latest/develop/ai/search-and-query/vectors#hnsw-index)
        indexing
    -   [L2](https://redis.io/docs/latest/develop/ai/search-and-query/vectors#distance-metrics)
        distance metric
    -   Float32 values
    -   768 dimensions (matching the embedding model)

Foundational: Create a vector search index with HNSW algorithm and L2 distance metric for semantic search

**Difficulty:** Intermediate

**Available in:** JavaScript (Node.js)

##### JavaScript (Node.js)

```javascript
await client.ft.create('vector_idx', {
    'content': {
        type: SchemaFieldTypes.TEXT,
    },
    'genre': {
        type: SchemaFieldTypes.TAG,
    },
    'embedding': {
        type: SchemaFieldTypes.VECTOR,
        TYPE: 'FLOAT32',
        ALGORITHM: VectorAlgorithms.HNSW,
        DISTANCE_METRIC: 'L2',
        DIM: 768,
    }
}, {
    ON: 'HASH',
    PREFIX: 'doc:'
});
```



## Add data

Add data objects to the index using `hSet()`. The index automatically processes objects with the `doc:` prefix.

For each document:
1. Generate an embedding using the `pipe()` function and `pipeOptions`
2. Convert the embedding to a binary string using `Buffer.from()`
3. Store the document with `hSet()`

Use `Promise.all()` to batch the commands and reduce network round trips:

Practical pattern: Generate embeddings and store documents with vector fields using pipelined hSet() commands

**Difficulty:** Intermediate

**Available in:** JavaScript (Node.js)

##### JavaScript (Node.js)

```javascript
const sentence1 = 'That is a very happy person';
const doc1 = {
    'content': sentence1, 
    'genre': 'persons', 
    'embedding': Buffer.from(
        (await pipe(sentence1, pipeOptions)).data.buffer
    ),
};

const sentence2 = 'That is a happy dog';
const doc2 = {
    'content': sentence2, 
    'genre': 'pets', 
    'embedding': Buffer.from(
        (await pipe(sentence2, pipeOptions)).data.buffer
    )
};

const sentence3 = 'Today is a sunny day';
const doc3 = {
    'content': sentence3, 
    'genre': 'weather', 
    'embedding': Buffer.from(
        (await pipe(sentence3, pipeOptions)).data.buffer
    )
};

await Promise.all([
    client.hSet('doc:1', doc1),
    client.hSet('doc:2', doc2),
    client.hSet('doc:3', doc3)
]);
```



## Run a query

To query the index:
1. Generate an embedding for your query text
2. Pass the embedding as a parameter to the search
3. Redis calculates vector distances and ranks results

The query returns an array of document objects. Each object contains:
- `id`: The document's key
- `value`: An object with fields specified in the `RETURN` option

Vector query: Execute a vector similarity search by generating a query embedding and finding nearest neighbors

**Difficulty:** Intermediate

**Available in:** JavaScript (Node.js)

##### JavaScript (Node.js)

```javascript
const similar = await client.ft.search(
    'vector_idx',
    '*=>[KNN 3 @embedding $B AS score]',
    {
        'PARAMS': {
            B: Buffer.from(
                (await pipe('That is a happy person', pipeOptions)).data.buffer
            ),
        },
        'RETURN': ['score', 'content'],
        'DIALECT': '2'
    },
);

for (const doc of similar.documents) {
    console.log(`${doc.id}: '${doc.value.content}', Score: ${doc.value.score}`);
}
```



The first run may take longer as it downloads the model data. The output shows results ordered by score (vector distance), with lower scores indicating greater similarity:

```
doc:1: 'That is a very happy person', Score: 0.127055495977
doc:2: 'That is a happy dog', Score: 0.836842417717
doc:3: 'Today is a sunny day', Score: 1.50889515877
```

## Differences with JSON documents

JSON documents support richer data modeling with nested fields. Key differences from hash documents:

1. Use paths in the schema to identify fields
2. Declare aliases for paths using the `AS` option
3. Set `ON` to `JSON` when creating the index
4. Use arrays instead of binary strings for vectors
5. Use `json.set()` instead of `hSet()`

Create the index with path aliases:

Foundational: Create a vector search index for JSON documents with path aliases and nested field support

**Difficulty:** Intermediate

**Available in:** JavaScript (Node.js)

##### JavaScript (Node.js)

```javascript
await client.ft.create('vector_json_idx', {
    '$.content': {
        type: SchemaFieldTypes.TEXT,
        AS: 'content',
    },
    '$.genre': {
        type: SchemaFieldTypes.TAG,
        AS: 'genre',
    },
    '$.embedding': {
        type: SchemaFieldTypes.VECTOR,
        TYPE: 'FLOAT32',
        ALGORITHM: VectorAlgorithms.HNSW,
        DISTANCE_METRIC: 'L2',
        DIM: 768,
        AS: 'embedding',
    }
}, {
    ON: 'JSON',
    PREFIX: 'jdoc:'
});
```



Add data using `json.set()`. Convert the `Float32Array` to a standard JavaScript array using the spread operator:

Practical pattern: Store JSON documents with vector embeddings converted to arrays for nested field support

**Difficulty:** Intermediate

**Available in:** JavaScript (Node.js)

##### JavaScript (Node.js)

```javascript
const jSentence1 = 'That is a very happy person';
const jdoc1 = {
    'content': jSentence1,
    'genre': 'persons',
    'embedding': [...(await pipe(jSentence1, pipeOptions)).data],
};

const jSentence2 = 'That is a happy dog';
const jdoc2 = {
    'content': jSentence2,
    'genre': 'pets',
    'embedding': [...(await pipe(jSentence2, pipeOptions)).data],
};

const jSentence3 = 'Today is a sunny day';
const jdoc3 = {
    'content': jSentence3,
    'genre': 'weather',
    'embedding': [...(await pipe(jSentence3, pipeOptions)).data],
};

await Promise.all([
    client.json.set('jdoc:1', '$', jdoc1),
    client.json.set('jdoc:2', '$', jdoc2),
    client.json.set('jdoc:3', '$', jdoc3)
]);
```



Query JSON documents using the same syntax, but note that the vector parameter must still be a binary string:

Vector query: Execute vector similarity search on JSON documents with the same query syntax as hash documents

**Difficulty:** Intermediate

**Available in:** JavaScript (Node.js)

##### JavaScript (Node.js)

```javascript
const jsons = await client.ft.search(
    'vector_json_idx',
    '*=>[KNN 3 @embedding $B AS score]',
    {
        "PARAMS": {
            B: Buffer.from(
                (await pipe('That is a happy person', pipeOptions)).data.buffer
            ),
        },
        'RETURN': ['score', 'content'],
        'DIALECT': '2'
    },
);
```



The results are identical to the hash document query, except for the `jdoc:` prefix:

```
jdoc:1: 'That is a very happy person', Score: 0.127055495977
jdoc:2: 'That is a happy dog', Score: 0.836842417717
jdoc:3: 'Today is a sunny day', Score: 1.50889515877
```

## Learn more

See
[Vector search](https://redis.io/docs/latest/develop/ai/search-and-query/query/vector-search)
for more information about indexing options, distance metrics, and query format.

