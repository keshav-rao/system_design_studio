# Vector set embeddings

```json metadata
{
  "schema_version": 2,
  "title": "Vector set embeddings",
  "description": "Index and query embeddings with Redis vector sets",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "topics": ["vector sets","vectors"],
  "relatedPages": ["/develop/clients/nodejs/vecsearch"],
  "scope": "example",
  "tableOfContents": {"sections":[{"id":"initialize","title":"Initialize"},{"id":"create-the-data","title":"Create the data"},{"id":"add-the-data-to-a-vector-set","title":"Add the data to a vector set"},{"id":"query-the-vector-set","title":"Query the vector set"},{"id":"more-information","title":"More information"}]}

,
  "codeExamples": [{"codetabsId":"home_vecsets-stepimport","description":"Foundational: Import Redis client and transformer modules for vector set operations","difficulty":"beginner","id":"import","languages":[{"id":"Node-js","panelId":"panel_Nodejs_home_vecsets-stepimport"}]},{"codetabsId":"home_vecsets-stepmodel","description":"Foundational: Configure a transformer pipeline to generate text embeddings for vector set operations","difficulty":"beginner","id":"model","languages":[{"id":"Node-js","panelId":"panel_Nodejs_home_vecsets-stepmodel"}]},{"codetabsId":"home_vecsets-stepdata","description":"Foundational: Define sample data structures with descriptions for vector set examples","difficulty":"beginner","id":"data","languages":[{"id":"Node-js","panelId":"panel_Nodejs_home_vecsets-stepdata"}]},{"codetabsId":"home_vecsets-stepadd_data","description":"Practical pattern: Generate embeddings and add elements to a vector set with vAdd() and attribute metadata","difficulty":"intermediate","id":"add_data","languages":[{"id":"Node-js","panelId":"panel_Nodejs_home_vecsets-stepadd_data"}]},{"codetabsId":"home_vecsets-stepbasic_query","description":"Vector set query: Execute a basic vector similarity search using vSim() to find semantically similar elements","difficulty":"intermediate","id":"basic_query","languages":[{"id":"Node-js","panelId":"panel_Nodejs_home_vecsets-stepbasic_query"}]},{"codetabsId":"home_vecsets-steplimited_query","description":"Restrict results: Limit vector search results using the COUNT parameter to return only the most relevant matches","difficulty":"intermediate","id":"limited_query","languages":[{"id":"Node-js","panelId":"panel_Nodejs_home_vecsets-steplimited_query"}]},{"codetabsId":"home_vecsets-stepentertainer_query","description":"Semantic search: Find elements with similar meaning despite different text","difficulty":"intermediate","id":"entertainer_query","languages":[{"id":"Node-js","panelId":"panel_Nodejs_home_vecsets-stepentertainer_query"}]},{"codetabsId":"home_vecsets-stepfiltered_query","description":"Pre-filtering: Combine vector similarity search with filter expressions to restrict results based on attribute metadata","difficulty":"advanced","id":"filtered_query","languages":[{"id":"Node-js","panelId":"panel_Nodejs_home_vecsets-stepfiltered_query"}]}]
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
[`@xenova/transformers`](https://www.npmjs.com/package/@xenova/transformers)
library to generate vector embeddings and then
store and retrieve them using a vector set with `node-redis`.

## Initialize

Start by [installing](https://redis.io/docs/latest/develop/clients/nodejs#install) `node-redis`
if you haven't already done so. Also, install `@xenova/transformers`:

```bash
npm install @xenova/transformers
```

In your JavaScript source file, import the required classes:

Foundational: Import Redis client and transformer modules for vector set operations

**Difficulty:** Beginner

**Available in:** JavaScript (Node.js)

##### JavaScript (Node.js)

```javascript
import * as transformers from '@xenova/transformers';
import { createClient } from 'redis';
```



The first of these imports is the
`@xenova/transformers` class, which generates an embedding from a section of text.
This example uses `transformers.pipeline` with the
[`all-MiniLM-L6-v2`](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
model for the embeddings. This model generates vectors with 384 dimensions, regardless
of the length of the input text, but note that the input is truncated to 256
tokens (see
[Word piece tokenization](https://huggingface.co/learn/nlp-course/en/chapter6/6)
at the [Hugging Face](https://huggingface.co/) docs to learn more about the way tokens
are related to the original text).

The output from `transformers.pipeline` is a function (called `pipe` in the examples)
that you can call to generate embeddings. The `pipeOptions` object is a parameter for
`pipe` that specifies how to generate sentence embeddings from token embeddings (see the
[`all-MiniLM-L6-v2`](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
documentation for details).

Foundational: Configure a transformer pipeline to generate text embeddings for vector set operations

**Difficulty:** Beginner

**Available in:** JavaScript (Node.js)

##### JavaScript (Node.js)

```javascript
const pipe = await transformers.pipeline(
    'feature-extraction', 'Xenova/all-MiniLM-L6-v2'
);

const pipeOptions = {
    pooling: 'mean',
    normalize: true,
};
```



## Create the data

The example data is contained in an object with some brief
descriptions of famous people:

Foundational: Define sample data structures with descriptions for vector set examples

**Difficulty:** Beginner

**Available in:** JavaScript (Node.js)

##### JavaScript (Node.js)

```javascript
const peopleData = {
    "Marie Curie": {
        "born": 1867, "died": 1934,
        "description": `
        Polish-French chemist and physicist. The only person ever to win
        two Nobel prizes for two different sciences.
        `
    },
    "Linus Pauling": {
        "born": 1901, "died": 1994,
        "description": `
        American chemist and peace activist. One of only two people to win two
        Nobel prizes in different fields (chemistry and peace).
        `
    },
    "Freddie Mercury": {
        "born": 1946, "died": 1991,
        "description": `
        British musician, best known as the lead singer of the rock band
        Queen.
        `
    },
    "Marie Fredriksson": {
        "born": 1958, "died": 2019,
        "description": `
        Swedish multi-instrumentalist, mainly known as the lead singer and
        keyboardist of the band Roxette.
        `
    },
    "Paul Erdos": {
        "born": 1913, "died": 1996,
        "description": `
        Hungarian mathematician, known for his eccentric personality almost
        as much as his contributions to many different fields of mathematics.
        `
    },
    "Maryam Mirzakhani": {
        "born": 1977, "died": 2017,
        "description": `
        Iranian mathematician. The first woman ever to win the Fields medal
        for her contributions to mathematics.
        `
    },
    "Masako Natsume": {
        "born": 1957, "died": 1985,
        "description": `
        Japanese actress. She was very famous in Japan but was primarily
        known elsewhere in the world for her portrayal of Tripitaka in the
        TV series Monkey.
        `
    },
    "Chaim Topol": {
        "born": 1935, "died": 2023,
        "description": `
        Israeli actor and singer, usually credited simply as 'Topol'. He was
        best known for his many appearances as Tevye in the musical Fiddler
        on the Roof.
        `
    }
};
```



## Add the data to a vector set

The next step is to connect to Redis and add the data to a new vector set.

The code below iterates through all the key-value pairs in the `peopleData` object
and adds corresponding elements to a vector set called `famousPeople`.

Use the `pipe()` function created above to generate the
embedding and then use `Array.from()` to convert the embedding to an array
of `float32` values that you can pass to the
[`vAdd()`](https://redis.io/docs/latest/commands/vadd) command to set the embedding.

The call to `vAdd()` also adds the `born` and `died` values from the
`peopleData` object as attribute data. You can access this during a query
or by using the [`vGetAttr()`](https://redis.io/docs/latest/commands/vgetattr) method.

Practical pattern: Generate embeddings and add elements to a vector set with vAdd() and attribute metadata

**Difficulty:** Intermediate

**Available in:** JavaScript (Node.js)

##### JavaScript (Node.js)

```javascript
const client = createClient({ url: 'redis://localhost:6379' });

client.on('error', err => console.log('Redis Client Error', err));
await client.connect();

for (const [name, details] of Object.entries(peopleData)) {
    const embedding = await pipe(details.description, pipeOptions);
    const embeddingArray = Array.from(embedding.data);

    await client.vAdd('famousPeople', embeddingArray, name);
    await client.vSetAttr('famousPeople', name, JSON.stringify({
        born: details.born,
        died: details.died
    }));
}
```



## Query the vector set

You can now query the data in the set. The basic approach is to use the
`pipe()` function to generate another embedding vector for the query text.
(This is the same method used to add the elements to the set.) Then, pass
the query vector to [`vSim()`](https://redis.io/docs/latest/commands/vsim) to return elements
of the set, ranked in order of similarity to the query.

Start with a simple query for "actors":

Vector set query: Execute a basic vector similarity search using vSim() to find semantically similar elements

**Difficulty:** Intermediate

**Available in:** JavaScript (Node.js)

##### JavaScript (Node.js)

```javascript
const queryValue = "actors";

const queryEmbedding = await pipe(queryValue, pipeOptions);
const queryArray = Array.from(queryEmbedding.data);

const actorsResults = await client.vSim('famousPeople', queryArray);

console.log(`'actors': ${JSON.stringify(actorsResults)}`);
// >>> 'actors': ["Masako Natsume","Chaim Topol","Linus Pauling",
// "Marie Fredriksson","Maryam Mirzakhani","Freddie Mercury",
// "Marie Curie","Paul Erdos"]
```



This returns the following list of elements (formatted slightly for clarity):

```
'actors': ["Masako Natsume","Chaim Topol","Linus Pauling",
    "Marie Fredriksson","Maryam Mirzakhani","Freddie Mercury",
    "Marie Curie","Paul Erdos"]
```

The first two people in the list are the two actors, as expected, but none of the
people from Linus Pauling onward was especially well-known for acting (and there certainly
isn't any information about that in the short description text).
As it stands, the search attempts to rank all the elements in the set, based
on the information contained in the embedding model.
You can use the `COUNT` parameter of `vSim()` to limit the list of elements
to just the most relevant few items:

Restrict results: Limit vector search results using the COUNT parameter to return only the most relevant matches

**Difficulty:** Intermediate

**Available in:** JavaScript (Node.js)

##### JavaScript (Node.js)

```javascript
const queryValue2 = "actors";

const queryEmbedding2 = await pipe(queryValue2, pipeOptions);
const queryArray2 = Array.from(queryEmbedding2.data);

const twoActorsResults = await client.vSim('famousPeople', queryArray2, {
    COUNT: 2
});

console.log(`'actors (2)': ${JSON.stringify(twoActorsResults)}`);
// >>> 'actors (2)': ["Masako Natsume","Chaim Topol"]
```



The reason for using text embeddings rather than simple text search
is that the embeddings represent semantic information. This allows a query
to find elements with a similar meaning even if the text is
different. For example, the word "entertainer" doesn't appear in any of the
descriptions but if you use it as a query, the actors and musicians are ranked
highest in the results list:

Semantic search: Find elements with similar meaning despite different text

**Difficulty:** Intermediate

**Available in:** JavaScript (Node.js)

##### JavaScript (Node.js)

```javascript
const queryValue3 = "entertainer";

const queryEmbedding3 = await pipe(queryValue3, pipeOptions);
const queryArray3 = Array.from(queryEmbedding3.data);

const entertainerResults = await client.vSim('famousPeople', queryArray3);

console.log(`'entertainer': ${JSON.stringify(entertainerResults)}`);
// >>> 'actors': ["Masako Natsume","Chaim Topol","Linus Pauling",
// "Marie Fredriksson","Maryam Mirzakhani","Freddie Mercury",
// "Marie Curie","Paul Erdos"]
```



Similarly, if you use "science" as a query, you get the following results:

```
'science': ["Linus Pauling","Marie Curie","Maryam Mirzakhani","Paul Erdos",
"Marie Fredriksson","Masako Natsume","Freddie Mercury","Chaim Topol"]
```

The scientists are ranked highest but they are then followed by the
mathematicians. This seems reasonable given the connection between mathematics
and science.

You can also use
[filter expressions](https://redis.io/docs/latest/develop/data-types/vector-sets/filtered-search)
with `vSim()` to restrict the search further. For example,
repeat the "science" query, but this time limit the results to people
who died before the year 2000:

Pre-filtering: Combine vector similarity search with filter expressions to restrict results based on attribute metadata

**Difficulty:** Advanced

**Available in:** JavaScript (Node.js)

##### JavaScript (Node.js)

```javascript
const queryValue5 = "science";

const queryEmbedding5 = await pipe(queryValue5, pipeOptions);
const queryArray5 = Array.from(queryEmbedding5.data);

const science2000Results = await client.vSim('famousPeople', queryArray5, {
    FILTER: '.died < 2000'
});

console.log(`'science2000': ${JSON.stringify(science2000Results)}`);
// >>> 'science2000': ["Linus Pauling","Marie Curie","Paul Erdos",
// "Masako Natsume","Freddie Mercury"]
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
[vector search](https://redis.io/docs/latest/develop/clients/nodejs/vecsearch).
This is a feature of
[Redis Search](https://redis.io/docs/latest/develop/ai/search-and-query)
that lets you retrieve
[JSON](https://redis.io/docs/latest/develop/data-types/json) and
[hash](https://redis.io/docs/latest/develop/data-types/hashes) documents based on
vector data stored in their fields.

