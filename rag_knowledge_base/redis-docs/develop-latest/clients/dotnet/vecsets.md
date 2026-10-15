# Vector set embeddings

```json metadata
{
  "schema_version": 2,
  "title": "Vector set embeddings",
  "description": "Index and query embeddings with Redis vector sets",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "topics": ["vector sets","vectors"],
  "relatedPages": ["/develop/clients/dotnet/vecsearch"],
  "scope": "example",
  "tableOfContents": {"sections":[{"id":"initialize","title":"Initialize"},{"id":"access-the-model","title":"Access the model"},{"id":"create-the-data","title":"Create the data"},{"id":"add-the-data-to-a-vector-set","title":"Add the data to a vector set"},{"id":"query-the-vector-set","title":"Query the vector set"},{"id":"more-information","title":"More information"}]}

,
  "codeExamples": [{"codetabsId":"home_vecsets-stepimport","description":"Foundational: Import required libraries for vector sets, embeddings, and Redis operations","difficulty":"beginner","id":"import","languages":[{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_home_vecsets-stepimport"}]},{"codetabsId":"home_vecsets-stepmodel","description":"Practical pattern: Initialize a SentenceTransformer model to generate vector embeddings from text","difficulty":"beginner","id":"model","languages":[{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_home_vecsets-stepmodel"}]},{"codetabsId":"home_vecsets-stepdata_classes","description":"Foundational: Define data classes for the embedding model\u0026amp;#39;s input and output structures","difficulty":"beginner","id":"data_classes","languages":[{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_home_vecsets-stepdata_classes"}]},{"codetabsId":"home_vecsets-stepget_embedding","description":"Foundational: Create a function to generate vector embeddings from text using the prediction engine","difficulty":"beginner","id":"get_embedding","languages":[{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_home_vecsets-stepget_embedding"}]},{"codetabsId":"home_vecsets-stepdata","description":"Foundational: Define sample data with text descriptions for vector embedding and storage","difficulty":"beginner","id":"data","languages":[{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_home_vecsets-stepdata"}]},{"codetabsId":"home_vecsets-stepadd_data","description":"Foundational: Add vector embeddings and attributes to a vector set using VADD command","difficulty":"beginner","id":"add_data","languages":[{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_home_vecsets-stepadd_data"}]},{"codetabsId":"home_vecsets-stepbasic_query","description":"Vector similarity search: Find semantically similar items in a vector set using VSIM command","difficulty":"intermediate","id":"basic_query","languages":[{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_home_vecsets-stepbasic_query"}]},{"codetabsId":"home_vecsets-steplimited_query","description":"Vector similarity search with limits: Restrict results to the top K most similar items using the count parameter","difficulty":"intermediate","id":"limited_query","languages":[{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_home_vecsets-steplimited_query"}]},{"codetabsId":"home_vecsets-stepentertainer_query","description":"Semantic search: Leverage text embeddings to find semantically similar items even when exact keywords don\u0026amp;#39;t match","difficulty":"intermediate","id":"entertainer_query","languages":[{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_home_vecsets-stepentertainer_query"}]},{"codetabsId":"home_vecsets-stepfiltered_query","description":"Filtered vector search: Combine vector similarity with attribute filters to narrow results based on metadata conditions","difficulty":"advanced","id":"filtered_query","languages":[{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_home_vecsets-stepfiltered_query"}]}]
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
[`Microsoft.ML`](https://dotnet.microsoft.com/en-us/apps/ai/ml-dotnet)
library to generate vector embeddings and then
store and retrieve them using a vector set with `StackExchange.Redis`.

## Initialize

Start by installing `StackExchange.Redis` with the following
command (version 2.9.17 or later is required for vector sets):

```bash
dotnet add package StackExchange.Redis --version 2.9.17
```

Also, install `Microsoft.ML`:

```bash
dotnet add package Microsoft.ML
```

In a new C# file, import the required classes:

Foundational: Import required libraries for vector sets, embeddings, and Redis operations

**Difficulty:** Beginner

**Available in:** C#

##### C#

```csharp
using StackExchange.Redis;

using Microsoft.ML;
using Microsoft.ML.Transforms.Text;
```



## Access the model

Use the `GetPredictionEngine()` helper function declared in the example below to load the model that creates the embeddings:

Practical pattern: Initialize a SentenceTransformer model to generate vector embeddings from text

**Difficulty:** Beginner

**Available in:** C#

##### C#

```csharp
static PredictionEngine<TextData, TransformedTextData> GetPredictionEngine()
{
    // Create a new ML context, for ML.NET operations. It can be used for
    // exception tracking and logging, as well as the source of randomness.
    var mlContext = new MLContext();

    // Create an empty list as the dataset
    var emptySamples = new List<TextData>();

    // Convert sample list to an empty IDataView.
    var emptyDataView = mlContext.Data.LoadFromEnumerable(emptySamples);

    // A pipeline for converting text into a 150-dimension embedding vector
    var textPipeline = mlContext.Transforms.Text.NormalizeText("Text")
        .Append(mlContext.Transforms.Text.TokenizeIntoWords("Tokens",
            "Text"))
        .Append(mlContext.Transforms.Text.ApplyWordEmbedding("Features",
            "Tokens", WordEmbeddingEstimator.PretrainedModelKind
            .SentimentSpecificWordEmbedding));

    // Fit to data.
    var textTransformer = textPipeline.Fit(emptyDataView);

    // Create the prediction engine to get the embedding vector from the input text/string.
    var predictionEngine = mlContext.Model.CreatePredictionEngine<TextData,
        TransformedTextData>(textTransformer);

    return predictionEngine;
}
```



The `GetPredictionEngine()` function uses two classes, `TextData` and `TransformedTextData`,
to specify the `PredictionEngine` model. These have a very simple definition
and are required because the model expects the input and output to be
passed in named object fields:

Foundational: Define data classes for the embedding model's input and output structures

**Difficulty:** Beginner

**Available in:** C#

##### C#

```csharp
class TextData
{
    public string Text { get; set; } = string.Empty;
}

class TransformedTextData : TextData
{
    public float[] Features { get; set; } = Array.Empty<float>();
}
```



Note that you must declare these classes at the end of the source file
if you are using a console app without a main class.

The `GetEmbedding()` function declared below can then use this model to
generate an embedding from a section of text and return it as a `float[]` array,
which is the format required by the vector set API:

Foundational: Create a function to generate vector embeddings from text using the prediction engine

**Difficulty:** Beginner

**Available in:** C#

##### C#

```csharp
static float[] GetEmbedding(
    PredictionEngine<TextData, TransformedTextData> model, string sentence
)
{
    // Call the prediction API to convert the text into embedding vector.
    var data = new TextData()
    {
        Text = sentence
    };

    var prediction = model.Predict(data);

    float[] floatArray = Array.ConvertAll(prediction.Features, x => (float)x);

    return floatArray;
}
```



## Create the data

The example data is contained a `Dictionary` object with some brief
descriptions of famous people:

Foundational: Define sample data with text descriptions for vector embedding and storage

**Difficulty:** Beginner

**Available in:** C#

##### C#

```csharp
Dictionary<string, dynamic> peopleData = new Dictionary<string, dynamic>
{
    ["Marie Curie"] = new
    {
        born = 1867,
        died = 1934,
        description = @"
        Polish-French chemist and physicist. The only person ever to win
        two Nobel prizes for two different sciences.
        "
    },
    ["Linus Pauling"] = new
    {
        born = 1901,
        died = 1994,
        description = @"
        American chemist and peace activist. One of only two people to win two
        Nobel prizes in different fields (chemistry and peace).
        "
    },
    ["Freddie Mercury"] = new
    {
        born = 1946,
        died = 1991,
        description = @"
        British musician, best known as the lead singer of the rock band
        Queen.
        "
    },
    ["Marie Fredriksson"] = new
    {
        born = 1958,
        died = 2019,
        description = @"
        Swedish multi-instrumentalist, mainly known as the lead singer and
        keyboardist of the band Roxette.
        "
    },
    ["Paul Erdos"] = new
    {
        born = 1913,
        died = 1996,
        description = @"
        Hungarian mathematician, known for his eccentric personality almost
        as much as his contributions to many different fields of mathematics.
        "
    },
    ["Maryam Mirzakhani"] = new
    {
        born = 1977,
        died = 2017,
        description = @"
        Iranian mathematician. The first woman ever to win the Fields medal
        for her contributions to mathematics.
        "
    },
    ["Masako Natsume"] = new
    {
        born = 1957,
        died = 1985,
        description = @"
        Japanese actress. She was very famous in Japan but was primarily
        known elsewhere in the world for her portrayal of Tripitaka in the
        TV series Monkey.
        "
    },
    ["Chaim Topol"] = new
    {
        born = 1935,
        died = 2023,
        description = @"
        Israeli actor and singer, usually credited simply as 'Topol'. He was
        best known for his many appearances as Tevye in the musical Fiddler
        on the Roof.
        "
    }
};
```



## Add the data to a vector set

The next step is to connect to Redis and add the data to a new vector set.

The code below iterates through `peopleData` and adds corresponding
elements to a vector set called `famousPeople`.

Use the `GetEmbedding()` function declared above to generate the
embedding as a `byte` array that you can pass to the
[`VectorSetAdd()`](https://redis.io/docs/latest/commands/vadd) command to set the embedding.

The call to `VectorSetAdd()` also adds the `born` and `died` values from the
original dictionary as attribute data. You can access this during a query
or by using the [`VectorSetGetAttributesJson()`](https://redis.io/docs/latest/commands/vgetattr) method.

Foundational: Add vector embeddings and attributes to a vector set using VADD command

**Difficulty:** Beginner

**Available in:** C#

##### C#

```csharp
ConnectionMultiplexer muxer = ConnectionMultiplexer.Connect("localhost:6379");
IDatabase db = muxer.GetDatabase();

PredictionEngine<TextData, TransformedTextData> model = GetPredictionEngine();

foreach (KeyValuePair<string, dynamic> person in peopleData)
{
    string name = person.Key;
    dynamic details = person.Value;
    float[] embedding = GetEmbedding(model, details.description);

    VectorSetAddRequest addRequest = VectorSetAddRequest.Member(name, embedding, null);
    db.VectorSetAdd("famousPeople", addRequest);

    // Set attributes separately
    string attributesJson = $"{{\"born\": {details.born}, \"died\": {details.died}}}";
    db.VectorSetSetAttributesJson("famousPeople", name, attributesJson);
}
```



## Query the vector set

You can now query the data in the set. The basic approach is to use the
`GetEmbedding()` function to generate another embedding vector for the query text.
(This is the same method used to add the elements to the set.) Then, pass
the query vector to [`VectorSetSimilaritySearch()`](https://redis.io/docs/latest/commands/vsim) to 
return elements of the set, ranked in order of similarity to the query.

Start with a simple query for "actors":

Vector similarity search: Find semantically similar items in a vector set using VSIM command

**Difficulty:** Intermediate

**Available in:** C#

##### C#

```csharp
string queryValue = "actors";

float[] queryEmbedding = GetEmbedding(model, queryValue);

VectorSetSimilaritySearchRequest basicQuery = VectorSetSimilaritySearchRequest.ByVector(queryEmbedding);
using (Lease<VectorSetSimilaritySearchResult>? actorsResults = db.VectorSetSimilaritySearch("famousPeople", basicQuery))
{
    IEnumerable<string> resultIds = actorsResults!.Span.ToArray()
        .Select(r => (string?)r.Member)
        .Where(id => id != null)
        .Select(id => $"'{id!}'");
    Console.WriteLine($"'actors': [{string.Join(", ", resultIds)}]");
}
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
You can use the `Count` property of `VectorSetSimilaritySearchRequest` to limit the
list of elements to just the most relevant few items:

Vector similarity search with limits: Restrict results to the top K most similar items using the count parameter

**Difficulty:** Intermediate

**Available in:** C#

##### C#

```csharp
queryValue = "actors";

queryEmbedding = GetEmbedding(model, queryValue);

VectorSetSimilaritySearchRequest limitedQuery = VectorSetSimilaritySearchRequest.ByVector(queryEmbedding);
limitedQuery.Count = 2;
using (Lease<VectorSetSimilaritySearchResult>? twoActorsResults = db.VectorSetSimilaritySearch("famousPeople", limitedQuery))
{
    IEnumerable<string> resultIds = twoActorsResults!.Span.ToArray()
        .Select(r => (string?)r.Member)
        .Where(id => id != null)
        .Select(id => $"'{id!}'");
    Console.WriteLine($"'actors (2)': [{string.Join(", ", resultIds)}]");
    // >>> 'actors (2)': ['Masako Natsume', 'Chaim Topol']
}
```



The reason for using text embeddings rather than simple text search
is that the embeddings represent semantic information. This allows a query
to find elements with a similar meaning even if the text is
different. For example, the word "entertainer" doesn't appear in any of the
descriptions but if you use it as a query, the actors and musicians are ranked
highest in the results list:

Semantic search: Leverage text embeddings to find semantically similar items even when exact keywords don't match

**Difficulty:** Intermediate

**Available in:** C#

##### C#

```csharp
queryValue = "entertainer";

queryEmbedding = GetEmbedding(model, queryValue);

VectorSetSimilaritySearchRequest entertainerQuery = VectorSetSimilaritySearchRequest.ByVector(queryEmbedding);
using (Lease<VectorSetSimilaritySearchResult>? entertainerResults = db.VectorSetSimilaritySearch("famousPeople", entertainerQuery))
{
    IEnumerable<string> resultIds = entertainerResults!.Span.ToArray()
        .Select(r => (string?)r.Member)
        .Where(id => id != null)
        .Select(id => $"'{id!}'");
    Console.WriteLine($"'entertainer': [{string.Join(", ", resultIds)}]");
    // >>> 'entertainer': ['Chaim Topol', 'Freddie Mercury',
    // 'Marie Fredriksson', 'Masako Natsume', 'Linus Pauling',
    // 'Paul Erdos', 'Maryam Mirzakhani', 'Marie Curie']
}
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
with `VectorSetSimilaritySearch()` to restrict the search further. For example,
repeat the "science" query, but this time limit the results to people
who died before the year 2000:

Filtered vector search: Combine vector similarity with attribute filters to narrow results based on metadata conditions

**Difficulty:** Advanced

**Available in:** C#

##### C#

```csharp
queryValue = "science";

queryEmbedding = GetEmbedding(model, queryValue);

VectorSetSimilaritySearchRequest filteredQuery = VectorSetSimilaritySearchRequest.ByVector(queryEmbedding);
filteredQuery.FilterExpression = ".died < 2000";
using (Lease<VectorSetSimilaritySearchResult>? science2000Results = db.VectorSetSimilaritySearch("famousPeople", filteredQuery))
{
    IEnumerable<string> resultIds = science2000Results!.Span.ToArray()
        .Select(r => (string?)r.Member)
        .Where(id => id != null)
        .Select(id => $"'{id!}'");
    Console.WriteLine($"'science2000': [{string.Join(", ", resultIds)}]");
    // >>> 'science2000': ['Marie Curie', 'Linus Pauling',
    // 'Paul Erdos', 'Freddie Mercury', 'Masako Natsume']
}
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
[vector search](https://redis.io/docs/latest/develop/clients/dotnet/nredisstack/vecsearch).
This is a feature of 
[Redis Search](https://redis.io/docs/latest/develop/ai/search-and-query)
that lets you retrieve
[JSON](https://redis.io/docs/latest/develop/data-types/json) and
[hash](https://redis.io/docs/latest/develop/data-types/hashes) documents based on
vector data stored in their fields.

