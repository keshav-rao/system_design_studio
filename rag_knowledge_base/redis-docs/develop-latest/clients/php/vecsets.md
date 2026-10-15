# Vector set embeddings

```json metadata
{
  "schema_version": 2,
  "title": "Vector set embeddings",
  "description": "Index and query embeddings with Redis vector sets",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "topics": ["vector sets","vectors"],
  "relatedPages": ["/develop/clients/php/vecsearch"],
  "scope": "example",
  "tableOfContents": {"sections":[{"id":"initialize","title":"Initialize"},{"id":"create-the-data","title":"Create the data"},{"id":"add-the-data-to-a-vector-set","title":"Add the data to a vector set"},{"id":"query-the-vector-set","title":"Query the vector set"},{"id":"more-information","title":"More information"}]}

,
  "codeExamples": [{"codetabsId":"home_vecsets-stepimport","description":"Foundational: Import required libraries for vector sets, embeddings, and Redis operations","difficulty":"beginner","id":"import","languages":[{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_home_vecsets-stepimport"}]},{"codetabsId":"home_vecsets-stepmodel","description":"Foundational: Initialize a TransformersPHP embedding pipeline to generate vectors from text","difficulty":"beginner","id":"model","languages":[{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_home_vecsets-stepmodel"}]},{"codetabsId":"home_vecsets-stepdata","description":"Foundational: Define sample data with text descriptions and metadata for vector embedding and storage","difficulty":"beginner","id":"data","languages":[{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_home_vecsets-stepdata"}]},{"codetabsId":"home_vecsets-stepadd_data","description":"Foundational: Add embedding vectors to a vector set and attach metadata attributes for later filtering","difficulty":"beginner","id":"add_data","languages":[{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_home_vecsets-stepadd_data"}]},{"codetabsId":"home_vecsets-stepbasic_query","description":"Vector similarity search: Find semantically similar items in a vector set using VSIM","difficulty":"intermediate","id":"basic_query","languages":[{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_home_vecsets-stepbasic_query"}]},{"codetabsId":"home_vecsets-steplimited_query","description":"Vector similarity search with limits: Restrict results to the top K most similar items using the count parameter","difficulty":"intermediate","id":"limited_query","languages":[{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_home_vecsets-steplimited_query"}]},{"codetabsId":"home_vecsets-stepentertainer_query","description":"Semantic search: Use text embeddings to find related concepts even when exact keywords do not appear in the source text","difficulty":"intermediate","id":"entertainer_query","languages":[{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_home_vecsets-stepentertainer_query"}]},{"codetabsId":"home_vecsets-stepfiltered_query","description":"Filtered vector search: Combine vector similarity with attribute filters to narrow results based on metadata conditions","difficulty":"advanced","id":"filtered_query","languages":[{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_home_vecsets-stepfiltered_query"}]}]
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
[TransformersPHP](https://transformers.codewithkyrian.com/) library to
generate text embeddings and then store and retrieve them using a vector set
with [`Predis`](https://redis.io/docs/latest/develop/clients/php).

## Initialize

Install `Predis` and `TransformersPHP` with Composer:

```bash
composer require predis/predis codewithkyrian/transformers
```

In a new PHP file, import the required classes and function:

Foundational: Import required libraries for vector sets, embeddings, and Redis operations

**Difficulty:** Beginner

**Available in:** PHP

##### PHP

```php
<?php

require 'vendor/autoload.php';

use function Codewithkyrian\Transformers\Pipelines\pipeline;

use Predis\Client as PredisClient;
```



The `pipeline()` function below creates an embedding generator for the
[`all-MiniLM-L6-v2`](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
model. This model generates vectors with 384 dimensions, regardless of the
length of the input text:

Foundational: Initialize a TransformersPHP embedding pipeline to generate vectors from text

**Difficulty:** Beginner

**Available in:** PHP

##### PHP

```php
$extractor = pipeline('embeddings', 'Xenova/all-MiniLM-L6-v2');
```



## Create the data

The example data is an array containing brief descriptions of famous people:

Foundational: Define sample data with text descriptions and metadata for vector embedding and storage

**Difficulty:** Beginner

**Available in:** PHP

##### PHP

```php
$peopleData = [
    'Marie Curie' => [
        'born' => 1867,
        'died' => 1934,
        'description' => 'Polish-French chemist and physicist. The only person ever to win two Nobel prizes for two different sciences.',
    ],
    'Linus Pauling' => [
        'born' => 1901,
        'died' => 1994,
        'description' => 'American chemist and peace activist. One of only two people to win two Nobel prizes in different fields (chemistry and peace).',
    ],
    'Freddie Mercury' => [
        'born' => 1946,
        'died' => 1991,
        'description' => 'British musician, best known as the lead singer of the rock band Queen.',
    ],
    'Marie Fredriksson' => [
        'born' => 1958,
        'died' => 2019,
        'description' => 'Swedish multi-instrumentalist, mainly known as the lead singer and keyboardist of the band Roxette.',
    ],
    'Paul Erdos' => [
        'born' => 1913,
        'died' => 1996,
        'description' => 'Hungarian mathematician, known for his eccentric personality almost as much as his contributions to many different fields of mathematics.',
    ],
    'Maryam Mirzakhani' => [
        'born' => 1977,
        'died' => 2017,
        'description' => 'Iranian mathematician. The first woman ever to win the Fields medal for her contributions to mathematics.',
    ],
    'Masako Natsume' => [
        'born' => 1957,
        'died' => 1985,
        'description' => 'Japanese actress. She was very famous in Japan but was primarily known elsewhere in the world for her portrayal of Tripitaka in the TV series Monkey.',
    ],
    'Chaim Topol' => [
        'born' => 1935,
        'died' => 2023,
        'description' => "Israeli actor and singer, usually credited simply as 'Topol'. He was best known for his many appearances as Tevye in the musical Fiddler on the Roof.",
    ],
];
```



## Add the data to a vector set

The next step is to connect to Redis and add the data to a new vector set.

The code below iterates through the array, uses the embedding pipeline to
generate a `float` vector from each description, and then adds the result to a
vector set called `famousPeople` with [`vadd()`](https://redis.io/docs/latest/commands/vadd).
It then stores the `born` and `died` values as element attributes using
[`vsetattr()`](https://redis.io/docs/latest/commands/vsetattr), so you can use the metadata
later during queries.

Foundational: Add embedding vectors to a vector set and attach metadata attributes for later filtering

**Difficulty:** Beginner

**Available in:** PHP

##### PHP

```php
$r->del('famousPeople');

foreach ($peopleData as $name => $details) {
    $embedding = $extractor($details['description'], normalize: true, pooling: 'mean');

    $r->vadd('famousPeople', $embedding[0], $name);
    $r->vsetattr('famousPeople', $name, [
        'born' => $details['born'],
        'died' => $details['died'],
    ]);
}
```



## Query the vector set

You can now query the data in the set. The basic approach is to generate
another embedding vector from the query text and pass it to
[`vsim()`](https://redis.io/docs/latest/commands/vsim), which returns elements ranked in
order of similarity to that query vector.

Start with a simple query for "actors":

Vector similarity search: Find semantically similar items in a vector set using VSIM

**Difficulty:** Intermediate

**Available in:** PHP

##### PHP

```php
$actorsEmbedding = $extractor('actors', normalize: true, pooling: 'mean');
$actorsResults = $r->vsim('famousPeople', $actorsEmbedding[0]);

echo "'actors': " . json_encode($actorsResults), PHP_EOL;
// >>> 'actors': ["Masako Natsume","Chaim Topol","Linus Pauling","Marie Fredriksson","Maryam Mirzakhani","Freddie Mercury","Marie Curie","Paul Erdos"]
```



This returns the following list of elements:

```
'actors': ["Masako Natsume","Chaim Topol","Linus Pauling",
"Marie Fredriksson","Maryam Mirzakhani","Freddie Mercury",
"Marie Curie","Paul Erdos"]
```

The first two people in the list are the two actors, as expected, but the
remaining results are less directly related. By default, the search attempts
to rank all the elements in the set. You can use the `count` parameter of
`vsim()` to limit the list to the most relevant few results:

Vector similarity search with limits: Restrict results to the top K most similar items using the count parameter

**Difficulty:** Intermediate

**Available in:** PHP

##### PHP

```php
$twoActorsResults = $r->vsim('famousPeople', $actorsEmbedding[0], false, false, 2);

echo "'actors (2)': " . json_encode($twoActorsResults), PHP_EOL;
// >>> 'actors (2)': ["Masako Natsume","Chaim Topol"]
```



The reason for using text embeddings rather than simple text search is that
the embeddings capture semantic information. This allows a query to find
elements with a similar meaning even if the text is different. For example, the
word "entertainer" doesn't appear in any of the descriptions but if you use it
as a query, the actors and musicians rank highly in the results:

Semantic search: Use text embeddings to find related concepts even when exact keywords do not appear in the source text

**Difficulty:** Intermediate

**Available in:** PHP

##### PHP

```php
$entertainerEmbedding = $extractor('entertainer', normalize: true, pooling: 'mean');
$entertainerResults = $r->vsim('famousPeople', $entertainerEmbedding[0]);

echo "'entertainer': " . json_encode($entertainerResults), PHP_EOL;
// >>> 'entertainer': ["Chaim Topol","Freddie Mercury","Linus Pauling","Marie Fredriksson","Masako Natsume","Paul Erdos","Maryam Mirzakhani","Marie Curie"]
```



Similarly, if you use "science" as a query, you get the scientists first,
followed by the mathematicians:

```text
'science': ["Linus Pauling","Marie Curie","Maryam Mirzakhani",
"Paul Erdos","Marie Fredriksson","Masako Natsume",
"Freddie Mercury","Chaim Topol"]
```

You can also use
[filter expressions](https://redis.io/docs/latest/develop/data-types/vector-sets/filtered-search)
with `vsim()` to restrict the search further. For example, repeat the
"science" query, but this time limit the results to people who died before the
year 2000:

Filtered vector search: Combine vector similarity with attribute filters to narrow results based on metadata conditions

**Difficulty:** Advanced

**Available in:** PHP

##### PHP

```php
$science2000Results = $r->vsim('famousPeople', $scienceEmbedding[0], false, false, null, null, null, '.died < 2000');

echo "'science2000': " . json_encode($science2000Results), PHP_EOL;
// >>> 'science2000': ["Linus Pauling","Marie Curie","Paul Erdos","Masako Natsume","Freddie Mercury"]
```



## More information

See the [vector sets](https://redis.io/docs/latest/develop/data-types/vector-sets)
docs for more information and code examples. See the
[Redis for AI](https://redis.io/docs/latest/develop/ai) section for more details
about text embeddings and other AI techniques you can use with Redis.

You may also be interested in
[vector search](https://redis.io/docs/latest/develop/clients/php/vecsearch).
This is a feature of
[Redis Search](https://redis.io/docs/latest/develop/ai/search-and-query)
that lets you retrieve
[JSON](https://redis.io/docs/latest/develop/data-types/json) and
[hash](https://redis.io/docs/latest/develop/data-types/hashes) documents based on
vector data stored in their fields.

