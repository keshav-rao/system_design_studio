# Index and query vectors

```json metadata
{
  "schema_version": 2,
  "title": "Index and query vectors",
  "description": "Learn how to index and query vector embeddings with Redis",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "topics": ["Redis Search","JSON","hash","vectors"],
  "relatedPages": ["/develop/clients/ruby/queryjson","/develop/ai/search-and-query"],
  "scope": "example",
  "tableOfContents": {"sections":[{"id":"initialize","title":"Initialize"},{"id":"import-dependencies","title":"Import dependencies"},{"id":"initialize-the-embedding-model","title":"Initialize the embedding model"},{"id":"define-a-helper-method","title":"Define a helper method"},{"id":"create-the-index","title":"Create the index"},{"id":"add-data","title":"Add data"},{"id":"run-a-query","title":"Run a query"},{"id":"differences-with-json-documents","title":"Differences with JSON documents"},{"id":"learn-more","title":"Learn more"}]}

,
  "codeExamples": [{"codetabsId":"ruby_home_query_vec-stepimport","description":"Foundational: Import required libraries for vector embeddings, Redis operations, and search functionality","difficulty":"beginner","id":"import","languages":[{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_ruby_home_query_vec-stepimport"}]},{"codetabsId":"ruby_home_query_vec-stepmodel","description":"Foundational: Initialize an informers pipeline to generate vector embeddings from text","difficulty":"beginner","id":"model","languages":[{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_ruby_home_query_vec-stepmodel"}]},{"codetabsId":"ruby_home_query_vec-stephelper_method","description":"Foundational: Create a helper method to pack float arrays into binary strings for vector storage in hash objects","difficulty":"beginner","id":"helper_method","languages":[{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_ruby_home_query_vec-stephelper_method"}]},{"codetabsId":"ruby_home_query_vec-stepconnect","description":"Foundational: Connect to a Redis server","difficulty":"beginner","id":"connect","languages":[{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_ruby_home_query_vec-stepconnect"}]},{"codetabsId":"ruby_home_query_vec-stepcreate_index","description":"Foundational: Create a vector search index for hash documents with HNSW algorithm and L2 distance metric","difficulty":"intermediate","id":"create_index","languages":[{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_ruby_home_query_vec-stepcreate_index"}]},{"codetabsId":"ruby_home_query_vec-stepadd_data","description":"Foundational: Store hash documents with vector embeddings generated from text content","difficulty":"beginner","id":"add_data","languages":[{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_ruby_home_query_vec-stepadd_data"}]},{"codetabsId":"ruby_home_query_vec-stepquery","description":"Vector similarity search: Find semantically similar documents by comparing query embeddings with indexed vectors using L2 distance","difficulty":"intermediate","id":"query","languages":[{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_ruby_home_query_vec-stepquery"}]},{"codetabsId":"ruby_home_query_vec-stepjson_index","description":"Foundational: Create a vector search index for JSON documents with JSON paths and field aliases","difficulty":"intermediate","id":"json_index","languages":[{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_ruby_home_query_vec-stepjson_index"}]},{"codetabsId":"ruby_home_query_vec-stepjson_data","description":"Foundational: Store JSON documents with vector embeddings as arrays (different from hash binary format)","difficulty":"beginner","id":"json_data","languages":[{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_ruby_home_query_vec-stepjson_data"}]},{"codetabsId":"ruby_home_query_vec-stepjson_query","description":"Vector similarity search: Query JSON documents using vector embeddings with field aliases for simplified syntax","difficulty":"intermediate","id":"json_query","languages":[{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_ruby_home_query_vec-stepjson_query"}]}]
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
[`informers`](https://github.com/ankane/informers) gem to generate the vector
embeddings to store and index with Redis Search. `informers` is a Ruby port of
Hugging Face transformers that runs the ONNX-exported
[`all-MiniLM-L6-v2`](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
model locally on the CPU, so no external embedding service is required.
The code is first demonstrated for hash documents with a
separate section to explain the
[differences with JSON documents](#differences-with-json-documents).

> [!NOTE]
> The redis-rb Query Engine requires redis-rb v6.0.0 or later.

&nbsp;

> [!NOTE]
> `redis-rb` uses query dialect 2 by default.
> Redis Search methods such as [`search()`](https://redis.io/docs/latest/commands/ft.search)
> will explicitly request this dialect, overriding the default set for the server.
> See
> [Query dialects](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/dialects)
> for more information.

## Initialize

Install [`redis-rb`](https://redis.io/docs/latest/develop/clients/ruby) if you
have not already done so. Also, install `informers` with the
following command:

```bash
gem install informers
```

The `informers` gem pulls in [`onnxruntime`](https://rubygems.org/gems/onnxruntime)
(which ships the ONNX Runtime shared library as a native extension) and
[`tokenizers`](https://rubygems.org/gems/tokenizers) (a Hugging Face fast-tokenizer
binding). Both come as pre-built binary gems for `arm64-darwin`, `x86_64-darwin`,
`aarch64-linux`, and `x86_64-linux`, so there is no system ONNX install step on
those platforms.

## Import dependencies

In a new Ruby source file, start by requiring the libraries and declaring a
short alias for the Query Engine namespace:

Foundational: Import required libraries for vector embeddings, Redis operations, and search functionality

**Difficulty:** Beginner

**Available in:** Ruby

##### Ruby

```ruby
require 'redis'
require 'informers'

# A short alias for the Query Engine namespace to keep the code below readable.
Search = Redis::Commands::Search
```



## Initialize the embedding model

The [`Informers.pipeline`](https://github.com/ankane/informers#usage) method
returns a callable that generates an embedding from a section of text.
Here, we create a pipeline that uses the
[`all-MiniLM-L6-v2`](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
model. This model generates vectors with 384 dimensions, regardless
of the length of the input text, but note that the input is truncated to 256
tokens (see
[Word piece tokenization](https://huggingface.co/learn/nlp-course/en/chapter6/6)
at the [Hugging Face](https://huggingface.co/) docs to learn more about the way tokens
are related to the original text).

Foundational: Initialize an informers pipeline to generate vector embeddings from text

**Difficulty:** Beginner

**Available in:** Ruby

##### Ruby

```ruby
# `informers` is a Ruby port of Hugging Face transformers that runs the
# ONNX-exported `all-MiniLM-L6-v2` encoder locally through `onnxruntime`.
# `Informers.pipeline("embedding", ...)` returns a callable that maps a
# string to a 384-element `Array<Float>`. The model data is downloaded
# into the local Hugging Face cache on the first call.
model = Informers.pipeline('embedding', 'sentence-transformers/all-MiniLM-L6-v2')
```



## Define a helper method

The embedding pipeline returns the vector as an `Array` of `Float` values.
When you store a vector in a hash object, you must encode this array as a
binary string of raw little-endian `float32` values, which is the format
Redis Search expects. Declare a helper method `to_bytes` that packs the
array using Ruby's [`Array#pack`](https://docs.ruby-lang.org/en/master/Array.html#method-i-pack)
directive `'e*'`:

Foundational: Create a helper method to pack float arrays into binary strings for vector storage in hash objects

**Difficulty:** Beginner

**Available in:** Ruby

##### Ruby

```ruby
# Redis Search stores a `FLOAT32` vector as raw little-endian bytes, with
# no header. Ruby's `Array#pack` directive `'e'` is a little-endian
# single-precision float, so `'e*'` packs every element of the vector.
# The result is an ASCII-8BIT (binary) string that `redis-rb` sends
# through unchanged.
def to_bytes(vector)
  vector.pack('e*')
end
```



## Create the index

Connect to Redis:

Foundational: Connect to a Redis server

**Difficulty:** Beginner

**Available in:** Ruby

##### Ruby

```ruby
r = Redis.new
```



Next, delete any index previously created with the name `vector_idx`
(the `ft_dropindex` call raises an exception if the index doesn't already exist,
which is why you need the `begin`/`rescue` block) and create the index.
The schema in the example below specifies hash objects for storage and includes
three fields: the text content to index, a
[tag](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/tags)
field to represent the "genre" of the text, and the embedding vector generated from
the original text content. The `embedding` field specifies
[HNSW](https://redis.io/docs/latest/develop/ai/search-and-query/vectors#hnsw-index)
indexing, the
[L2](https://redis.io/docs/latest/develop/ai/search-and-query/vectors#distance-metrics)
vector distance metric, `FLOAT32` values to represent the vector's components,
and 384 dimensions, as required by the `all-MiniLM-L6-v2` embedding model.

Foundational: Create a vector search index for hash documents with HNSW algorithm and L2 distance metric

**Difficulty:** Intermediate

**Available in:** Ruby

##### Ruby

```ruby
begin
  r.ft_dropindex('vector_idx', delete_documents: true)
rescue Redis::CommandError
  # Index doesn't exist, so there is nothing to drop.
end

schema = Search::Schema.build do
  text_field 'content'
  tag_field 'genre'
  vector_field 'embedding', 'HNSW',
               type: 'FLOAT32', dim: 384, distance_metric: 'L2'
end

definition = Search::IndexDefinition.new(
  prefix: ['doc:'],
  index_type: Search::IndexType::HASH
)

index = r.create_index('vector_idx', schema, definition: definition)
puts index.name # >>> vector_idx
```



## Add data

You can now supply the data objects, which will be indexed automatically
when you add them with [`hset()`](https://redis.io/docs/latest/commands/hset), as long as
you use the `doc:` prefix specified in the index definition.

Call the pipeline with `pooling: 'mean'` and `normalize: true` to create the
embedding that represents the `content` field, then pass the result through the
`to_bytes` helper to get the binary string that Redis Search indexes.

Foundational: Store hash documents with vector embeddings generated from text content

**Difficulty:** Beginner

**Available in:** Ruby

##### Ruby

```ruby
# Pass `normalize: true` so `informers` L2-normalises each embedding in
# the ONNX graph; the L2 distances Redis reports are then directly
# comparable across documents.
sentence1 = 'That is a very happy person'
r.hset('doc:0', {
  'content' => sentence1,
  'genre' => 'persons',
  'embedding' => to_bytes(model.(sentence1, pooling: 'mean', normalize: true))
})

sentence2 = 'That is a happy dog'
r.hset('doc:1', {
  'content' => sentence2,
  'genre' => 'pets',
  'embedding' => to_bytes(model.(sentence2, pooling: 'mean', normalize: true))
})

sentence3 = 'Today is a sunny day'
r.hset('doc:2', {
  'content' => sentence3,
  'genre' => 'weather',
  'embedding' => to_bytes(model.(sentence3, pooling: 'mean', normalize: true))
})
```



## Run a query

After you have created the index and added the data, you are ready to run a query.
To do this, you must create another embedding vector from your chosen query
text. Redis calculates the similarity between the query vector and each
embedding vector in the index as it runs the query. It then ranks the
results in order of this numeric similarity value.

The code below creates the query embedding, packs it with the `to_bytes` helper,
and passes it as a query parameter (see
[Vector search](https://redis.io/docs/latest/develop/ai/search-and-query/query/vector-search)
for more information about using query parameters with embeddings).

Vector similarity search: Find semantically similar documents by comparing query embeddings with indexed vectors using L2 distance

**Difficulty:** Intermediate

**Available in:** Ruby

##### Ruby

```ruby
query_text = 'That is a happy person'
query_vec = to_bytes(model.(query_text, pooling: 'mean', normalize: true))

res = index.search(
  '*=>[KNN 3 @embedding $vec AS vector_distance]',
  sort_by: 'vector_distance',
  return_fields: ['content', 'vector_distance'],
  params: { 'vec' => query_vec }
)

puts res.total # >>> 3
# The index has the key prefix `doc:`, so `redis-rb` returns the logical
# document id with that prefix removed (`0`, not `doc:0`).
res.each do |doc|
  puts "#{doc.id}: #{doc['content']} (distance #{doc['vector_distance']})"
end
```



The code is now ready to run, but note that it may take a while to complete when
you run it for the first time (which happens because `informers` must download the
`all-MiniLM-L6-v2` model data before it can generate the embeddings). When you run
the code, it outputs the following result (the exact distances may differ slightly
on your system):

```
3
0: That is a very happy person (distance 0.114169895649)
1: That is a happy dog (distance 0.610845208168)
2: Today is a sunny day (distance 1.48624789715)
```

Note that the results are ordered according to the value of the `vector_distance`
field, with the lowest distance indicating the greatest similarity to the query.
As you would expect, the result for `doc:0` with the content text *"That is a very happy person"*
is the result that is most similar in meaning to the query text
*"That is a happy person"*.

Note also that `redis-rb` strips the key prefix (`doc:`) that the index
definition specifies, so the document id returned in the result is `0` rather
than `doc:0`.

## Differences with JSON documents

Indexing JSON documents is similar to hash indexing, but there are some
important differences. JSON allows much richer data modelling with nested fields, so
you must supply a [path](https://redis.io/docs/latest/develop/data-types/json/path) in the schema
to identify each field you want to index. However, you can declare a short alias for each
of these paths (using the `as:` keyword argument) to avoid typing it in full for
every query. Also, you must specify `Search::IndexType::JSON` when you create the index.

The code below shows these differences, but the index is otherwise very similar to
the one created previously for hashes:

Foundational: Create a vector search index for JSON documents with JSON paths and field aliases

**Difficulty:** Intermediate

**Available in:** Ruby

##### Ruby

```ruby
begin
  r.ft_dropindex('vector_json_idx', delete_documents: true)
rescue Redis::CommandError
  # Index doesn't exist, so there is nothing to drop.
end

json_schema = Search::Schema.build do
  text_field '$.content', as: 'content'
  tag_field '$.genre', as: 'genre'
  vector_field '$.embedding', 'HNSW', as: 'embedding',
               type: 'FLOAT32', dim: 384, distance_metric: 'L2'
end

json_definition = Search::IndexDefinition.new(
  prefix: ['jdoc:'],
  index_type: Search::IndexType::JSON
)

json_index = r.create_index('vector_json_idx', json_schema, definition: json_definition)
puts json_index.name # >>> vector_json_idx
```



Use [`json_set()`](https://redis.io/docs/latest/commands/json.set) to add the data
instead of [`hset()`](https://redis.io/docs/latest/commands/hset).

An important difference with JSON indexing is that the vectors are
specified using arrays instead of binary strings. Pass the `Array<Float>`
returned by the embedding pipeline directly, without the `to_bytes` step
you use for a hash.

Foundational: Store JSON documents with vector embeddings as arrays (different from hash binary format)

**Difficulty:** Beginner

**Available in:** Ruby

##### Ruby

```ruby
# For a JSON document, store the embedding as a plain `Array<Float>`
# (a JSON array), not the packed binary string used for hashes.
r.json_set('jdoc:0', '$', {
  'content' => sentence1,
  'genre' => 'persons',
  'embedding' => model.(sentence1, pooling: 'mean', normalize: true)
})

r.json_set('jdoc:1', '$', {
  'content' => sentence2,
  'genre' => 'pets',
  'embedding' => model.(sentence2, pooling: 'mean', normalize: true)
})

r.json_set('jdoc:2', '$', {
  'content' => sentence3,
  'genre' => 'weather',
  'embedding' => model.(sentence3, pooling: 'mean', normalize: true)
})
```



The query is almost identical to the one for the hash documents. This
demonstrates how the right choice of aliases for the JSON paths can
save you having to write complex queries. An important thing to notice
is that the vector parameter for the query is still specified as a
binary string (using the `to_bytes` helper), even though the data for
the `embedding` field of the JSON was specified as an array.

Vector similarity search: Query JSON documents using vector embeddings with field aliases for simplified syntax

**Difficulty:** Intermediate

**Available in:** Ruby

##### Ruby

```ruby
# The query vector is still passed as a packed binary string, even though
# the stored `embedding` field is a JSON array.
json_res = json_index.search(
  '*=>[KNN 3 @embedding $vec AS vector_distance]',
  sort_by: 'vector_distance',
  return_fields: ['content', 'vector_distance'],
  params: { 'vec' => query_vec }
)

puts json_res.total # >>> 3
json_res.each do |doc|
  puts "#{doc.id}: #{doc['content']} (distance #{doc['vector_distance']})"
end
```



Apart from the `jdoc:` prefixes for the keys, the result from the JSON
query is the same as for hash:

```
3
0: That is a very happy person (distance 0.114169895649)
1: That is a happy dog (distance 0.610845208168)
2: Today is a sunny day (distance 1.48624789715)
```

## Learn more

See
[Vector search](https://redis.io/docs/latest/develop/ai/search-and-query/query/vector-search)
for more information about the indexing options, distance metrics, and query format
for vectors.

