# Vector set embeddings

```json metadata
{
  "schema_version": 2,
  "title": "Vector set embeddings",
  "description": "Index and query embeddings with Redis vector sets",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "topics": ["vector sets","vectors"],
  "relatedPages": ["/develop/clients/jedis/vecsearch"],
  "scope": "example",
  "tableOfContents": {"sections":[{"id":"initialize","title":"Initialize"},{"id":"create-the-data","title":"Create the data"},{"id":"add-the-data-to-a-vector-set","title":"Add the data to a vector set"},{"id":"query-the-vector-set","title":"Query the vector set"},{"id":"more-information","title":"More information"}]}

,
  "codeExamples": [{"codetabsId":"home_vecsets-stepimport","description":"Foundational: Import required libraries for vector sets, embeddings, and Redis operations","difficulty":"beginner","id":"import","languages":[{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_home_vecsets-stepimport"}]},{"codetabsId":"home_vecsets-stepmodel","description":"Foundational: Initialize a tokenizer and embedding model to generate vector representations from text","difficulty":"beginner","id":"model","languages":[{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_home_vecsets-stepmodel"}]},{"codetabsId":"home_vecsets-stepdata","description":"Foundational: Define sample data with text descriptions for vector embedding and storage","difficulty":"beginner","id":"data","languages":[{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_home_vecsets-stepdata"}]},{"codetabsId":"home_vecsets-stepadd_data","description":"Foundational: Add vector embeddings and attributes to a vector set using VADD command","difficulty":"beginner","id":"add_data","languages":[{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_home_vecsets-stepadd_data"}]},{"codetabsId":"home_vecsets-stepbasic_query","description":"Vector similarity search: Find semantically similar items in a vector set using VSIM command","difficulty":"intermediate","id":"basic_query","languages":[{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_home_vecsets-stepbasic_query"}]},{"codetabsId":"home_vecsets-steplimited_query","description":"Vector similarity search with limits: Restrict results to the top K most similar items using the count parameter","difficulty":"intermediate","id":"limited_query","languages":[{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_home_vecsets-steplimited_query"}]},{"codetabsId":"home_vecsets-stepentertainer_query","description":"Semantic search: Leverage text embeddings to find semantically similar items even when exact keywords don\u0026amp;#39;t match","difficulty":"intermediate","id":"entertainer_query","languages":[{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_home_vecsets-stepentertainer_query"}]},{"codetabsId":"home_vecsets-stepfiltered_query","description":"Filtered vector search: Combine vector similarity with attribute filters to narrow results based on metadata conditions","difficulty":"advanced","id":"filtered_query","languages":[{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_home_vecsets-stepfiltered_query"}]}]
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
embeddings). The example below shows how to generate vector embeddings and then
store and retrieve them using a vector set with `Jedis`.

## Initialize

If you are using [Maven](https://maven.apache.org/), add the following
dependencies to your `pom.xml` file
(note that you need `Jedis` v6.2.0 or later to use vector sets):

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
compileOnly 'redis.clients:jedis:7.2.0'
compileOnly 'ai.djl.huggingface:tokenizers:0.33.0'
compileOnly 'ai.djl.pytorch:pytorch-model-zoo:0.33.0'
compileOnly 'ai.djl:api:0.33.0'
```

In a new Java file, import the required classes:

Foundational: Import required libraries for vector sets, embeddings, and Redis operations

**Difficulty:** Beginner

**Available in:** Java (Synchronous - Jedis)

##### Java (Synchronous - Jedis)

```java
import redis.clients.jedis.RedisClient;
import redis.clients.jedis.params.VAddParams;
import redis.clients.jedis.params.VSimParams;

import java.util.*;

// DJL classes for model loading and inference.
import ai.djl.huggingface.translator.TextEmbeddingTranslatorFactory;
import ai.djl.inference.Predictor;
import ai.djl.repository.zoo.Criteria;
import ai.djl.training.util.ProgressBar;
```



The imports include the classes required to generate embeddings from text.
This example uses an instance of the `Predictor` class with the
[`all-MiniLM-L6-v2`](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
model for the embeddings. This model generates vectors with 384 dimensions, regardless
of the length of the input text, but note that the input is truncated to 256
tokens (see
[Word piece tokenization](https://huggingface.co/learn/nlp-course/en/chapter6/6)
at the [Hugging Face](https://huggingface.co/) docs to learn more about the way tokens
are related to the original text).

Foundational: Initialize a tokenizer and embedding model to generate vector representations from text

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



## Create the data

The example data is contained in a `List<Person>` object with some brief
descriptions of famous people.

Foundational: Define sample data with text descriptions for vector embedding and storage

**Difficulty:** Beginner

**Available in:** Java (Synchronous - Jedis)

##### Java (Synchronous - Jedis)

```java
        final class Person {
            final String name;
            final int born;
            final int died;
            final String description;
            Person(String name, int born, int died, String description) {
                this.name = name; this.born = born; this.died = died; this.description = description;
            }
        }

        List<Person> people = Arrays.asList(
            new Person(
                "Marie Curie",
                1867, 1934,
                "Polish-French chemist and physicist. The only person ever to win" +
                " two Nobel prizes for two different sciences."
            ),
            new Person(
                "Linus Pauling",
                1901, 1994,
                "American chemist and peace activist. One of only two people to" +
                " win two Nobel prizes in different fields (chemistry and peace)."
            ),
            new Person(
                "Freddie Mercury",
                1946, 1991,
                "British musician, best known as the lead singer of the rock band Queen."
            ),
            new Person(
                "Marie Fredriksson",
                1958, 2019,
                "Swedish multi-instrumentalist, mainly known as the lead singer and" +
                " keyboardist of the band Roxette."
            ),
            new Person(
                "Paul Erdos",
                1913, 1996,
                "Hungarian mathematician, known for his eccentric personality almost" +
                " as much as his contributions to many different fields of mathematics."
            ),
            new Person(
                "Maryam Mirzakhani",
                1977, 2017,
                "Iranian mathematician. The first woman ever to win the Fields medal" +
                " for her contributions to mathematics."
            ),
            new Person(
                "Masako Natsume",
                1957, 1985,
                "Japanese actress. She was very famous in Japan but was primarily" +
                " known elsewhere in the world for her portrayal of Tripitaka in the" +
                " TV series Monkey."
            ),
            new Person(
                "Chaim Topol",
                1935, 2023,
                "Israeli actor and singer, usually credited simply as 'Topol'. He was" +
                " best known for his many appearances as Tevye in the musical Fiddler" +
                " on the Roof."
            )
        );
```



## Add the data to a vector set

The code below connects to Redis, then iterates through all the items in the `people` list,
generates embeddings for each person's description, and then
adds the appropriate elements to a vector set called `famousPeople`.
Note that the `predict()` call is in a `try`/`catch` block because it can throw
exceptions if it can't download the embedding model (you should add code to handle
the exceptions for production).

The call to `vadd()` also adds the `born` and `died` values from the
original `people` list as attribute data. You can access this during a query
or by using the [`vgetattr()`](https://redis.io/docs/latest/commands/vgetattr) method.

Foundational: Add vector embeddings and attributes to a vector set using VADD command

**Difficulty:** Beginner

**Available in:** Java (Synchronous - Jedis)

##### Java (Synchronous - Jedis)

```java
        RedisClient jedis = new RedisClient("redis://localhost:6379");

        for (Person person : people) {
            float[] embedding;
            try {
                embedding = predictor.predict(person.description);
            } catch (Exception e) {
                // This just allows the code to compile without errors.
                // In a real-world scenario, you would handle the exception properly.
                embedding = new float[384];
            }

            // Add element with attributes using VAddParams
            String attrs = String.format("{\"born\": %d, \"died\": %d}", person.born, person.died);
            boolean added = jedis.vadd("famousPeople", embedding, person.name, new VAddParams().setAttr(attrs));
            System.out.println(added); // >>> true
        }
```



## Query the vector set

You can now query the data in the set. The basic approach is to use the
`predict()` method to generate another embedding vector for the query text.
(This is the same method used to add the elements to the set.) Then, pass
the query vector to [`vsim()`](https://redis.io/docs/latest/commands/vsim) to return elements
of the set, ranked in order of similarity to the query.

Start with a simple query for "actors":

Vector similarity search: Find semantically similar items in a vector set using VSIM command

**Difficulty:** Intermediate

**Available in:** Java (Synchronous - Jedis)

##### Java (Synchronous - Jedis)

```java
        float[] actorsEmbedding;
        try {
            actorsEmbedding = predictor.predict("actors");
        } catch (Exception e) {
            actorsEmbedding = new float[384];
        }

        List<String> basicResults = jedis.vsim("famousPeople", actorsEmbedding);
        System.out.println(basicResults);
        // >>> [Masako Natsume, Chaim Topol, Linus Pauling, Marie Fredriksson,
        // >>> Maryam Mirzakhani, Marie Curie, Freddie Mercury, Paul Erdos]
```



This returns the following list of elements (formatted slightly for clarity):

```
['Masako Natsume', 'Chaim Topol', 'Linus Pauling',
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

**Available in:** Java (Synchronous - Jedis)

##### Java (Synchronous - Jedis)

```java
        VSimParams limitParams = new VSimParams().count(2);
        List<String> limitedResults = jedis.vsim("famousPeople", actorsEmbedding, limitParams);
        System.out.println(limitedResults);
        // >>> [Masako Natsume, Chaim Topol]
```



The reason for using text embeddings rather than simple text search
is that the embeddings represent semantic information. This allows a query
to find elements with a similar meaning even if the text is
different. For example, the word "entertainer" doesn't appear in any of the
descriptions, but if you use it as a query, the actors and musicians are ranked
highest in the results list:

Semantic search: Leverage text embeddings to find semantically similar items even when exact keywords don't match

**Difficulty:** Intermediate

**Available in:** Java (Synchronous - Jedis)

##### Java (Synchronous - Jedis)

```java
        float[] entertainerEmbedding;
        try {
            entertainerEmbedding = predictor.predict("entertainers");
        } catch (Exception e) {
            entertainerEmbedding = new float[384];
        }

        List<String> entertainerResults = jedis.vsim("famousPeople", entertainerEmbedding);
        System.out.println(entertainerResults);
        // >>> [Freddie Mercury, Chaim Topol, Linus Pauling, Marie Fredriksson,
        // >>> Masako Natsume, Paul Erdos, Maryam Mirzakhani, Marie Curie]
```



Similarly, if you use "science" as a query, you get the following results:

```
['Marie Curie', 'Linus Pauling', 'Maryam Mirzakhani',
'Paul Erdos', 'Marie Fredriksson', 'Freddie Mercury', 'Masako Natsume',
'Chaim Topol']
```

The scientists are ranked highest, followed by the
mathematicians. This ranking seems reasonable given the connection between mathematics and science.

You can also use
[filter expressions](https://redis.io/docs/latest/develop/data-types/vector-sets/filtered-search)
with `vsim()` to restrict the search further. For example,
repeat the "science" query, but this time limit the results to people
who died before the year 2000:

Filtered vector search: Combine vector similarity with attribute filters to narrow results based on metadata conditions

**Difficulty:** Advanced

**Available in:** Java (Synchronous - Jedis)

##### Java (Synchronous - Jedis)

```java
        float[] science2000Embedding;
        try {
            science2000Embedding = predictor.predict("science");
        } catch (Exception e) {
            science2000Embedding = new float[384];
        }

        VSimParams filterParams = new VSimParams().filter(".died < 2000");
        List<String> filteredResults = jedis.vsim("famousPeople", science2000Embedding, filterParams);
        System.out.println(filteredResults);
        // >>> [Marie Curie, Linus Pauling, Paul Erdos, Freddie Mercury, Masako Natsume]
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
[vector search](https://redis.io/docs/latest/develop/clients/jedis/vecsearch).
This is a feature of
[Redis Search](https://redis.io/docs/latest/develop/ai/search-and-query)
that lets you retrieve
[JSON](https://redis.io/docs/latest/develop/data-types/json) and
[hash](https://redis.io/docs/latest/develop/data-types/hashes) documents based on
vector data stored in their fields.

