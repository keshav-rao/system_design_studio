# Index and query vectors

```json metadata
{
  "schema_version": 2,
  "title": "Index and query vectors",
  "description": "Learn how to index and query vector embeddings with Redis",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "topics": ["Redis Search","JSON","hash","vectors"],
  "relatedPages": ["/develop/clients/redis-py/queryjson","/develop/clients/redis-py/vecsets","/develop/ai/search-and-query"],
  "scope": "example",
  "tableOfContents": {"sections":[{"id":"initialize","title":"Initialize"},{"id":"create-the-index","title":"Create the index"},{"id":"add-data","title":"Add data"},{"id":"run-a-query","title":"Run a query"},{"id":"differences-with-json-documents","title":"Differences with JSON documents"},{"id":"learn-more","title":"Learn more"}]}

,
  "codeExamples": [{"codetabsId":"home_query_vec-stepimport","description":"Foundational: Import required libraries for vector embeddings, Redis operations, and search functionality","difficulty":"beginner","id":"import","languages":[{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_home_query_vec-stepimport"}]},{"codetabsId":"home_query_vec-stepmodel","description":"Foundational: Initialize a SentenceTransformer model to generate vector embeddings from text","difficulty":"beginner","id":"model","languages":[{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_home_query_vec-stepmodel"}]},{"codetabsId":"home_query_vec-stepconnect","description":"Foundational: Connect to a Redis server and clean up existing vector indexes","difficulty":"beginner","id":"connect","languages":[{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_home_query_vec-stepconnect"}]},{"codetabsId":"home_query_vec-stepcreate_index","description":"Foundational: Create a vector search index for hash documents with HNSW algorithm and L2 distance metric","difficulty":"intermediate","id":"create_index","languages":[{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_home_query_vec-stepcreate_index"}]},{"codetabsId":"home_query_vec-stepadd_data","description":"Foundational: Store hash documents with vector embeddings generated from text content","difficulty":"beginner","id":"add_data","languages":[{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_home_query_vec-stepadd_data"}]},{"codetabsId":"home_query_vec-stepquery","description":"Vector similarity search: Find semantically similar documents by comparing query embeddings with indexed vectors using L2 distance","difficulty":"intermediate","id":"query","languages":[{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_home_query_vec-stepquery"}]},{"codetabsId":"home_query_vec-stepjson_index","description":"Foundational: Create a vector search index for JSON documents with JSON paths and field aliases","difficulty":"intermediate","id":"json_index","languages":[{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_home_query_vec-stepjson_index"}]},{"codetabsId":"home_query_vec-stepjson_data","description":"Foundational: Store JSON documents with vector embeddings as lists (different from hash binary format)","difficulty":"beginner","id":"json_data","languages":[{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_home_query_vec-stepjson_data"}]},{"codetabsId":"home_query_vec-stepjson_query","description":"Vector similarity search: Query JSON documents using vector embeddings with field aliases for simplified syntax","difficulty":"intermediate","id":"json_query","languages":[{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_home_query_vec-stepjson_query"}]}]
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

The example below uses the
[`sentence-transformers`](https://pypi.org/project/sentence-transformers/)
library to generate vector embeddings to store and index with
Redis Search. The code is first demonstrated for hash documents with a
separate section to explain the
[differences with JSON documents](#differences-with-json-documents).

> [!NOTE]
> From [v6.0.0](https://github.com/redis/redis-py/releases/tag/v6.0.0) onwards,
> `redis-py` uses query dialect 2 by default.
> Redis Search methods such as [`ft().search()`](https://redis.io/docs/latest/commands/ft.search)
> will explicitly request this dialect, overriding the default set for the server.
> See
> [Query dialects](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/dialects)
> for more information.

## Initialize

Install [`redis-py`](https://redis.io/docs/latest/develop/clients/redis-py) if you
have not already done so. Also, install `sentence-transformers` with the
following command:

```bash
pip install sentence-transformers
```

In a new Python source file, start by importing the required classes:

Foundational: Import required libraries for vector embeddings, Redis operations, and search functionality

**Difficulty:** Beginner

**Available in:** Python

##### Python

```python
from sentence_transformers import SentenceTransformer
from redis.commands.search.query import Query
from redis.commands.search.field import TextField, TagField, VectorField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
from redis.commands.json.path import Path

import numpy as np
import redis
```



The first of these imports is the
`SentenceTransformer` class, which generates an embedding from a section of text.
Here, we create an instance of `SentenceTransformer` that uses the
[`all-MiniLM-L6-v2`](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
model for the embeddings. This model generates vectors with 384 dimensions, regardless
of the length of the input text, but note that the input is truncated to 256
tokens (see
[Word piece tokenization](https://huggingface.co/learn/nlp-course/en/chapter6/6)
at the [Hugging Face](https://huggingface.co/) docs to learn more about the way tokens
are related to the original text).

Foundational: Initialize a SentenceTransformer model to generate vector embeddings from text

**Difficulty:** Beginner

**Available in:** Python

##### Python

```python
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
```



## Create the index

Connect to Redis and delete any index previously created with the
name `vector_idx`. (The `dropindex()` call throws an exception if
the index doesn't already exist, which is why you need the
`try: except:` block.)

Foundational: Connect to a Redis server and clean up existing vector indexes

**Difficulty:** Beginner

**Available in:** Python

##### Python

```python
r = redis.Redis(decode_responses=True)

try:
    r.ft("vector_idx").dropindex(True)
except redis.exceptions.ResponseError:
    pass
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

Foundational: Create a vector search index for hash documents with HNSW algorithm and L2 distance metric

**Difficulty:** Intermediate

**Available in:** Python

##### Python

```python
schema = (
    TextField("content"),
    TagField("genre"),
    VectorField("embedding", "HNSW", {
        "TYPE": "FLOAT32",
        "DIM": 384,
        "DISTANCE_METRIC":"L2"
    })
)

r.ft("vector_idx").create_index(
    schema,
    definition=IndexDefinition(
        prefix=["doc:"], index_type=IndexType.HASH
    )
)
```



## Add data

You can now supply the data objects, which will be indexed automatically
when you add them with [`hset()`](https://redis.io/docs/latest/commands/hset), as long as
you use the `doc:` prefix specified in the index definition.

Use the `model.encode()` method of `SentenceTransformer`
as shown below to create the embedding that represents the `content` field.
The `astype()` option that follows the `model.encode()` call specifies that
we want a vector of `float32` values. The `tobytes()` option encodes the
vector components together as a single binary string.
Use the binary string representation when you are indexing hashes
or running a query (but use a list of `float` for
[JSON documents](#differences-with-json-documents)).

Foundational: Store hash documents with vector embeddings generated from text content

**Difficulty:** Beginner

**Available in:** Python

##### Python

```python
content = "That is a very happy person"

r.hset("doc:0", mapping={
    "content": content,
    "genre": "persons",
    "embedding": model.encode(content).astype(np.float32).tobytes(),
})

content = "That is a happy dog"

r.hset("doc:1", mapping={
    "content": content,
    "genre": "pets",
    "embedding": model.encode(content).astype(np.float32).tobytes(),
})

content = "Today is a sunny day"

r.hset("doc:2", mapping={
    "content": content,
    "genre": "weather",
    "embedding": model.encode(content).astype(np.float32).tobytes(),
})
```



## Run a query

After you have created the index and added the data, you are ready to run a query.
To do this, you must create another embedding vector from your chosen query
text. Redis calculates the similarity between the query vector and each
embedding vector in the index as it runs the query. It then ranks the
results in order of this numeric similarity value.

The code below creates the query embedding using `model.encode()`, as with
the indexing, and passes it as a parameter when the query executes
(see
[Vector search](https://redis.io/docs/latest/develop/ai/search-and-query/query/vector-search)
for more information about using query parameters with embeddings).

Vector similarity search: Find semantically similar documents by comparing query embeddings with indexed vectors using L2 distance

**Difficulty:** Intermediate

**Available in:** Python

##### Python

```python
q = Query(
    "*=>[KNN 3 @embedding $vec AS vector_distance]"
).return_field("vector_distance").return_field("content").dialect(2)

query_text = "That is a happy person"

res = r.ft("vector_idx").search(
    q, query_params={
        "vec": model.encode(query_text).astype(np.float32).tobytes()
    }
)

print(res)
```



The code is now ready to run, but note that it may take a while to complete when
you run it for the first time (which happens because RedisVL must download the
`all-MiniLM-L6-v2` model data before it can
generate the embeddings). When you run the code, it outputs the following result
object (slightly formatted here for clarity):

```
Result{
    3 total,
    docs: [
        Document {
            'id': 'doc:0',
            'payload': None,
            'vector_distance': '0.114169985056',
            'content': 'That is a very happy person'
        },
        Document {
            'id': 'doc:1',
            'payload': None,
            'vector_distance': '0.610845386982',
            'content': 'That is a happy dog'
        },
        Document {
            'id': 'doc:2',
            'payload': None,
            'vector_distance': '1.48624813557',
            'content': 'Today is a sunny day'
        }
    ]
}
```

Note that the results are ordered according to the value of the `vector_distance`
field, with the lowest distance indicating the greatest similarity to the query.
As you would expect, the result for `doc:0` with the content text *"That is a very happy person"*
is the result that is most similar in meaning to the query text
*"That is a happy person"*.

## Differences with JSON documents

Indexing JSON documents is similar to hash indexing, but there are some
important differences. JSON allows much richer data modelling with nested fields, so
you must supply a [path](https://redis.io/docs/latest/develop/data-types/json/path) in the schema
to identify each field you want to index. However, you can declare a short alias for each
of these paths (using the `as_name` keyword argument) to avoid typing it in full for
every query. Also, you must specify `IndexType.JSON` when you create the index.

The code below shows these differences, but the index is otherwise very similar to
the one created previously for hashes:

Foundational: Create a vector search index for JSON documents with JSON paths and field aliases

**Difficulty:** Intermediate

**Available in:** Python

##### Python

```python
schema = (
    TextField("$.content", as_name="content"),
    TagField("$.genre", as_name="genre"),
    VectorField(
        "$.embedding", "HNSW", {
            "TYPE": "FLOAT32",
            "DIM": 384,
            "DISTANCE_METRIC": "L2"
        },
        as_name="embedding"
    )
)

r.ft("vector_json_idx").create_index(
    schema,
    definition=IndexDefinition(
        prefix=["jdoc:"], index_type=IndexType.JSON
    )
)
```



Use [`json().set()`](https://redis.io/docs/latest/commands/json.set) to add the data
instead of [`hset()`](https://redis.io/docs/latest/commands/hset). The dictionaries
that specify the fields have the same structure as the ones used for `hset()`
but `json().set()` receives them in a positional argument instead of
the `mapping` keyword argument.

An important difference with JSON indexing is that the vectors are
specified using lists instead of binary strings. Generate the list
using the `tolist()` method instead of `tobytes()` as you would with a
hash.

Foundational: Store JSON documents with vector embeddings as lists (different from hash binary format)

**Difficulty:** Beginner

**Available in:** Python

##### Python

```python
content = "That is a very happy person"

r.json().set("jdoc:0", Path.root_path(), {
    "content": content,
    "genre": "persons",
    "embedding": model.encode(content).astype(np.float32).tolist(),
})

content = "That is a happy dog"

r.json().set("jdoc:1", Path.root_path(), {
    "content": content,
    "genre": "pets",
    "embedding": model.encode(content).astype(np.float32).tolist(),
})

content = "Today is a sunny day"

r.json().set("jdoc:2", Path.root_path(), {
    "content": content,
    "genre": "weather",
    "embedding": model.encode(content).astype(np.float32).tolist(),
})
```



The query is almost identical to the one for the hash documents. This
demonstrates how the right choice of aliases for the JSON paths can
save you having to write complex queries. An important thing to notice
is that the vector parameter for the query is still specified as a
binary string (using the `tobytes()` method), even though the data for
the `embedding` field of the JSON was specified as a list.

Vector similarity search: Query JSON documents using vector embeddings with field aliases for simplified syntax

**Difficulty:** Intermediate

**Available in:** Python

##### Python

```python
q = Query(
    "*=>[KNN 3 @embedding $vec AS vector_distance]"
).return_field("vector_distance").return_field("content").dialect(2)

query_text = "That is a happy person"

res = r.ft("vector_json_idx").search(
    q, query_params={
        "vec": model.encode(query_text).astype(np.float32).tobytes()
    }
)

print(repr(res))
```



Apart from the `jdoc:` prefixes for the keys, the result from the JSON
query is the same as for hash:

```
Result{
    3 total,
    docs: [
        Document {
            'id': 'jdoc:0',
            'payload': None,
            'vector_distance': '0.114169985056',
            'content': 'That is a very happy person'
        },
            .
            .
            .
```

## Learn more

See
[Vector search](https://redis.io/docs/latest/develop/ai/search-and-query/query/vector-search)
for more information about the indexing options, distance metrics, and query format
for vectors.

