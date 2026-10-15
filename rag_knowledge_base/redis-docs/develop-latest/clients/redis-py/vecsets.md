# Vector set embeddings

```json metadata
{
  "schema_version": 2,
  "title": "Vector set embeddings",
  "description": "Index and query embeddings with Redis vector sets",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "topics": ["vector sets","vectors"],
  "relatedPages": ["/develop/clients/redis-py/vecsearch"],
  "scope": "example",
  "tableOfContents": {"sections":[{"id":"initialize","title":"Initialize"},{"id":"create-the-data","title":"Create the data"},{"id":"add-the-data-to-a-vector-set","title":"Add the data to a vector set"},{"id":"query-the-vector-set","title":"Query the vector set"},{"id":"more-information","title":"More information"}]}

,
  "codeExamples": [{"codetabsId":"home_vecsets-stepimport","description":"Foundational: Import required libraries for vector sets, embeddings, and Redis operations","difficulty":"beginner","id":"import","languages":[{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_home_vecsets-stepimport"}]},{"codetabsId":"home_vecsets-stepmodel","description":"Foundational: Initialize a SentenceTransformer model to generate vector embeddings from text","difficulty":"beginner","id":"model","languages":[{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_home_vecsets-stepmodel"}]},{"codetabsId":"home_vecsets-stepdata","description":"Foundational: Define sample data with text descriptions for vector embedding and storage","difficulty":"beginner","id":"data","languages":[{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_home_vecsets-stepdata"}]},{"codetabsId":"home_vecsets-stepadd_data","description":"Foundational: Add vector embeddings and attributes to a vector set using VADD command","difficulty":"beginner","id":"add_data","languages":[{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_home_vecsets-stepadd_data"}]},{"codetabsId":"home_vecsets-stepbasic_query","description":"Vector similarity search: Find semantically similar items in a vector set using VSIM command","difficulty":"intermediate","id":"basic_query","languages":[{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_home_vecsets-stepbasic_query"}]},{"codetabsId":"home_vecsets-steplimited_query","description":"Vector similarity search with limits: Restrict results to the top K most similar items using the count parameter","difficulty":"intermediate","id":"limited_query","languages":[{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_home_vecsets-steplimited_query"}]},{"codetabsId":"home_vecsets-stepentertainer_query","description":"Semantic search: Leverage text embeddings to find semantically similar items even when exact keywords don\u0026amp;#39;t match","difficulty":"intermediate","id":"entertainer_query","languages":[{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_home_vecsets-stepentertainer_query"}]},{"codetabsId":"home_vecsets-stepfiltered_query","description":"Filtered vector search: Combine vector similarity with attribute filters to narrow results based on metadata conditions","difficulty":"advanced","id":"filtered_query","languages":[{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_home_vecsets-stepfiltered_query"}]}]
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
[`sentence-transformers`](https://pypi.org/project/sentence-transformers/)
library to generate vector embeddings and then
store and retrieve them using a vector set with `redis-py`.

## Initialize

Start by installing the preview version of `redis-py` with the following
command:

```bash
pip install redis==6.0.0b2
```

Also, install `sentence-transformers`:

```bash
pip install sentence-transformers
```

In a new Python file, import the required classes:

Foundational: Import required libraries for vector sets, embeddings, and Redis operations

**Difficulty:** Beginner

**Available in:** Python

##### Python

```python
from sentence_transformers import SentenceTransformer

import redis
import numpy as np
```



The first of these imports is the
`SentenceTransformer` class, which generates an embedding from a section of text.
This example uses an instance of `SentenceTransformer` with the
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



## Create the data

The example data is contained a dictionary with some brief
descriptions of famous people:

Foundational: Define sample data with text descriptions for vector embedding and storage

**Difficulty:** Beginner

**Available in:** Python

##### Python

```python
peopleData = {
    "Marie Curie": {
        "born": 1867, "died": 1934,
        "description": """
        Polish-French chemist and physicist. The only person ever to win
        two Nobel prizes for two different sciences.
        """
    },
    "Linus Pauling": {
        "born": 1901, "died": 1994,
        "description": """
        American chemist and peace activist. One of only two people to win two
        Nobel prizes in different fields (chemistry and peace).
        """
    },
    "Freddie Mercury": {
        "born": 1946, "died": 1991,
        "description": """
        British musician, best known as the lead singer of the rock band
        Queen.
        """
    },
    "Marie Fredriksson": {
        "born": 1958, "died": 2019,
        "description": """
        Swedish multi-instrumentalist, mainly known as the lead singer and
        keyboardist of the band Roxette.
        """
    },
    "Paul Erdos": {
        "born": 1913, "died": 1996,
        "description": """
        Hungarian mathematician, known for his eccentric personality almost
        as much as his contributions to many different fields of mathematics.
        """
    },
    "Maryam Mirzakhani": {
        "born": 1977, "died": 2017,
        "description": """
        Iranian mathematician. The first woman ever to win the Fields medal
        for her contributions to mathematics.
        """
    },
    "Masako Natsume": {
        "born": 1957, "died": 1985,
        "description": """
        Japanese actress. She was very famous in Japan but was primarily
        known elsewhere in the world for her portrayal of Tripitaka in the
        TV series Monkey.
        """
    },
    "Chaim Topol": {
        "born": 1935, "died": 2023,
        "description": """
        Israeli actor and singer, usually credited simply as 'Topol'. He was
        best known for his many appearances as Tevye in the musical Fiddler
        on the Roof.
        """
    }
}
```



## Add the data to a vector set

The next step is to connect to Redis and add the data to a new vector set.

The code below uses the dictionary's
[`items()`](https://docs.python.org/3/library/stdtypes.html#dict.items)
view to iterate through all the key-value pairs and add corresponding
elements to a vector set called `famousPeople`.

Use the
[`encode()`](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode)
method of `SentenceTransformer` to generate the
embedding as an array of `float32` values. The `tobytes()` method converts
the array to a byte string that you can pass to the
[`vadd()`](https://redis.io/docs/latest/commands/vadd) command to set the embedding.
Note that `vadd()` can also accept a list of `float` values to set the
vector, but the byte string format is more compact and saves a little
transmission time. If you later use
[`vemb()`](https://redis.io/docs/latest/commands/vemb) to retrieve the embedding,
it will return the vector as an array rather than the original byte
string (note that this is different from the behavior of byte strings in
[hash vector indexing](https://redis.io/docs/latest/develop/ai/search-and-query/vectors)).

The call to `vadd()` also adds the `born` and `died` values from the
original dictionary as attribute data. You can access this during a query
or by using the [`vgetattr()`](https://redis.io/docs/latest/commands/vgetattr) method.

Foundational: Add vector embeddings and attributes to a vector set using VADD command

**Difficulty:** Beginner

**Available in:** Python

##### Python

```python
r = redis.Redis(decode_responses=True)

for name, details in peopleData.items():
    emb = model.encode(details["description"]).astype(np.float32).tobytes()

    r.vset().vadd(
        "famousPeople",
        emb,
        name,
        attributes={
            "born": details["born"],
            "died": details["died"]
        }
    )
```



## Query the vector set

You can now query the data in the set. The basic approach is to use the
`encode()` method to generate another embedding vector for the query text.
(This is the same method used to add the elements to the set.) Then, pass
the query vector to [`vsim()`](https://redis.io/docs/latest/commands/vsim) to return elements
of the set, ranked in order of similarity to the query.

Start with a simple query for "actors":

Vector similarity search: Find semantically similar items in a vector set using VSIM command

**Difficulty:** Intermediate

**Available in:** Python

##### Python

```python
query_value = "actors"

actors_results = r.vset().vsim(
    "famousPeople",
    model.encode(query_value).astype(np.float32).tobytes(),
)

print(f"'actors': {actors_results}")
```



This returns the following list of elements (formatted slightly for clarity):

```
'actors': ['Masako Natsume', 'Chaim Topol', 'Linus Pauling',
'Marie Fredriksson', 'Maryam Mirzakhani', 'Marie Curie',
'Freddie Mercury', 'Paul Erdos']
```

The first two people in the list are the two actors, as expected, but none of the
people from Linus Pauling onward was especially well-known for acting (and there certainly
isn't any information about that in the short description text).
As it stands, the search attempts to rank all the elements in the set, based
on the information contained in the embedding model.
You can use the `count` parameter of `vsim()` to limit the list of elements
to just the most relevant few items:

Vector similarity search with limits: Restrict results to the top K most similar items using the count parameter

**Difficulty:** Intermediate

**Available in:** Python

##### Python

```python
query_value = "actors"

two_actors_results = r.vset().vsim(
    "famousPeople",
    model.encode(query_value).astype(np.float32).tobytes(),
    count=2
)

print(f"'actors (2)': {two_actors_results}")
# >>> 'actors (2)': ['Masako Natsume', 'Chaim Topol']
```



The reason for using text embeddings rather than simple text search
is that the embeddings represent semantic information. This allows a query
to find elements with a similar meaning even if the text is
different. For example, the word "entertainer" doesn't appear in any of the
descriptions but if you use it as a query, the actors and musicians are ranked
highest in the results list:

Semantic search: Leverage text embeddings to find semantically similar items even when exact keywords don't match

**Difficulty:** Intermediate

**Available in:** Python

##### Python

```python
query_value = "entertainer"

entertainer_results = r.vset().vsim(
    "famousPeople",
    model.encode(query_value).astype(np.float32).tobytes()
)

print(f"'entertainer': {entertainer_results}")
# >>> 'entertainer': ['Chaim Topol', 'Freddie Mercury',
# 'Marie Fredriksson', 'Masako Natsume', 'Linus Pauling',
# 'Paul Erdos', 'Maryam Mirzakhani', 'Marie Curie']
```



Similarly, if you use "science" as a query, you get the following results:

```
'science': ['Marie Curie', 'Linus Pauling', 'Maryam Mirzakhani',
'Paul Erdos', 'Marie Fredriksson', 'Freddie Mercury', 'Masako Natsume',
'Chaim Topol']
```

The scientists are ranked highest but they are then followed by the
mathematicians. This seems reasonable given the connection between mathematics
and science.

You can also use
[filter expressions](https://redis.io/docs/latest/develop/data-types/vector-sets/filtered-search)
with `vsim()` to restrict the search further. For example,
repeat the "science" query, but this time limit the results to people
who died before the year 2000:

Filtered vector search: Combine vector similarity with attribute filters to narrow results based on metadata conditions

**Difficulty:** Advanced

**Available in:** Python

##### Python

```python
query_value = "science"

science2000_results = r.vset().vsim(
    "famousPeople",
    model.encode(query_value).astype(np.float32).tobytes(),
    filter=".died < 2000"
)

print(f"'science2000': {science2000_results}")
# >>> 'science2000': ['Marie Curie', 'Linus Pauling',
# 'Paul Erdos', 'Freddie Mercury', 'Masako Natsume']
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
[vector search](https://redis.io/docs/latest/develop/clients/redis-py/vecsearch).
This is a feature of
[Redis Search](https://redis.io/docs/latest/develop/ai/search-and-query)
that lets you retrieve
[JSON](https://redis.io/docs/latest/develop/data-types/json) and
[hash](https://redis.io/docs/latest/develop/data-types/hashes) documents based on
vector data stored in their fields.

