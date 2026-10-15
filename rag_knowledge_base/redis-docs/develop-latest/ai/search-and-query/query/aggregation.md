# Aggregation queries

```json metadata
{
  "schema_version": 2,
  "title": "Aggregation queries",
  "description": "Group and aggregate query results",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"simple-mapping","title":"Simple mapping"},{"id":"grouping-with-aggregation","title":"Grouping with aggregation"},{"id":"aggregating-without-grouping","title":"Aggregating without grouping"},{"id":"grouping-without-aggregation","title":"Grouping without aggregation"}]}

,
  "codeExamples": [{"codetabsId":"query_agg-stepagg1","description":"Foundational: Apply mapping functions to transform field values using APPLY when you need to calculate derived values","difficulty":"beginner","id":"agg1","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_query_agg-stepagg1"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_query_agg-stepagg1"},{"id":"Node-js","panelId":"panel_Nodejs_query_agg-stepagg1"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_query_agg-stepagg1"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_query_agg-stepagg1"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_query_agg-stepagg1"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_query_agg-stepagg1"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_query_agg-stepagg1"}]},{"codetabsId":"query_agg-stepagg2","description":"Grouping with aggregation: Use GROUPBY with REDUCE to group results by field values and apply aggregation functions when you need to summarize data across groups","difficulty":"intermediate","id":"agg2","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_query_agg-stepagg2"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_query_agg-stepagg2"},{"id":"Node-js","panelId":"panel_Nodejs_query_agg-stepagg2"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_query_agg-stepagg2"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_query_agg-stepagg2"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_query_agg-stepagg2"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_query_agg-stepagg2"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_query_agg-stepagg2"}]},{"codetabsId":"query_agg-stepagg3","description":"Aggregating without grouping: Create a dummy grouping field with APPLY to aggregate across all documents when you need a single aggregate result","difficulty":"intermediate","id":"agg3","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_query_agg-stepagg3"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_query_agg-stepagg3"},{"id":"Node-js","panelId":"panel_Nodejs_query_agg-stepagg3"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_query_agg-stepagg3"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_query_agg-stepagg3"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_query_agg-stepagg3"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_query_agg-stepagg3"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_query_agg-stepagg3"}]},{"codetabsId":"query_agg-stepagg4","description":"Grouping without aggregation: Use TOLIST to collect grouped values without applying mathematical functions when you need to organize results by category","difficulty":"intermediate","id":"agg4","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_query_agg-stepagg4"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_query_agg-stepagg4"},{"id":"Node-js","panelId":"panel_Nodejs_query_agg-stepagg4"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_query_agg-stepagg4"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_query_agg-stepagg4"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_query_agg-stepagg4"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_query_agg-stepagg4"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_query_agg-stepagg4"}]}]
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


An aggregation query allows you to perform the following actions:

- Apply simple mapping functions.
- Group data based on field values.
- Apply aggregation functions on the grouped data.

This article explains the basic usage of the [FT.AGGREGATE](https://redis.io/docs/latest/commands/ft.aggregate) command. For further details, see the [command specification](https://redis.io/docs/latest/commands/ft.aggregate) and the [aggregations reference documentation](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/aggregations).

The examples in this article use a schema with the following fields:

| Field name | Field type |
| ---------- | ---------- |
| `condition` | `TAG` |
| `price` | `NUMERIC` |

## Simple mapping

The `APPLY` clause allows you to apply a simple mapping function to a result set that is returned based on the query expression.

```
FT.AGGREGATE index "query_expr" LOAD n "field_1" .. "field_n" APPLY "function_expr" AS "result_field"
```

Here is a more detailed explanation of the query syntax:

1. **Query expression**: you can use the same query expressions as you would use with the [`FT.SEARCH`](https://redis.io/docs/latest/commands/ft.search) command. You can substitute `query_expr` with any of the expressions explained in the articles of this [query topic](https://redis.io/docs/latest/develop/ai/search-and-query/query). Vector search queries are an exception. You can't combine a vector search with an aggregation query.
2. **Loaded fields**: if field values weren't already loaded into the aggregation pipeline, you can force their presence via the `LOAD` clause. This clause takes the number of fields (`n`), followed by the field names (`"field_1" .. "field_n"`).
3. **Mapping function**: this mapping function operates on the field values. A specific field is referenced as `@field_name` within the function expression. The result is returned as `result_field`.

The following example shows you how to calculate a discounted price for new bicycles:

Foundational: Apply mapping functions to transform field values using APPLY when you need to calculate derived values

**Difficulty:** Beginner

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), Python

##### Redis CLI

```
FT.AGGREGATE idx:bicycle "@condition:{new}" LOAD 2 "__key" "price" APPLY "@price - (@price * 0.1)" AS "discounted"
```

##### C#

```csharp
        AggregationResult res1 = db.FT().Aggregate(
            "idx:bicycle",
            new AggregationRequest("@condition:{new}")
                .Load(new FieldName("__key"), new FieldName("price"))
                .Apply("@price - (@price * 0.1)", "discounted")
        );
        Console.WriteLine(res1.TotalResults);   // >>> 5

        for (int i = 0; i < res1.TotalResults; i++)
        {
            Row res1Row = res1.GetRow(i);

            Console.WriteLine(
                $"Key: {res1Row["__key"]}, Price: {res1Row["price"]}, Discounted: {res1Row["discounted"]}"
            );
        }
        // >>> Key: bicycle:0, Price: 270, Discounted: 243
        // >>> Key: bicycle:5, Price: 810, Discounted: 729
        // >>> Key: bicycle:6, Price: 2300, Discounted: 2070
        // >>> Key: bicycle:7, Price: 430, Discounted: 387
        // >>> Key: bicycle:8, Price: 1200, Discounted: 1080
```

##### Go

```go
	res1, err := rdb.FTAggregateWithArgs(ctx,
		"idx:bicycle",
		"@condition:{new}",
		&redis.FTAggregateOptions{
			Steps: []redis.FTAggregateStep{
				{Load: &redis.FTAggregateLoad{Field: "__key"}},
				{Load: &redis.FTAggregateLoad{Field: "price"}},
				{Apply: &redis.FTAggregateApply{
					Field: "@price - (@price * 0.1)",
					As:    "discounted",
				}},
			},
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(len(res1.Rows)) // >>> 5

	sort.Slice(res1.Rows, func(i, j int) bool {
		return res1.Rows[i].Fields["__key"].(string) <
			res1.Rows[j].Fields["__key"].(string)
	})

	for _, row := range res1.Rows {
		fmt.Printf(
			"__key=%v, discounted=%v, price=%v\n",
			row.Fields["__key"],
			row.Fields["discounted"],
			row.Fields["price"],
		)
	}
	// >>> __key=bicycle:0, discounted=243, price=270
	// >>> __key=bicycle:5, discounted=729, price=810
	// >>> __key=bicycle:6, discounted=2070, price=2300
	// >>> __key=bicycle:7, discounted=387, price=430
	// >>> __key=bicycle:8, discounted=1080, price=1200
```

##### Java (Asynchronous - Lettuce)

```java
            AggregateArgs<String, String> agg1Args = AggregateArgs.<String, String> builder().load("__key").load("price")
                    .apply("@price - (@price * 0.1)", "discounted").build();

            CompletableFuture<AggregationReply<String, String>> agg1 = asyncCommands
                    .ftAggregate("idx:bicycle", "@condition:{new}", agg1Args).thenApply(result -> {
                        result.getReplies().get(0).getResults().stream()
                                .sorted((doc1, doc2) -> doc1.getFields().get("__key").compareTo(doc2.getFields().get("__key")))
                                .forEach(doc -> {
                                    System.out.printf("Key: %s, Price: %s, Discounted: %s\n", doc.getFields().get("__key"),
                                            doc.getFields().get("price"), doc.getFields().get("discounted"));
                                });
                        // >>> Key: bicycle:0, Price: 270, Discounted: 243
                        // >>> Key: bicycle:5, Price: 810, Discounted: 729
                        // >>> Key: bicycle:6, Price: 2300, Discounted: 2070
                        // >>> Key: bicycle:7, Price: 430, Discounted: 387
                        // >>> Key: bicycle:8, Price: 1200, Discounted: 1080
                        return result;
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            AggregateArgs<String, String> agg1Args = AggregateArgs.<String, String> builder().load("__key").load("price")
                    .apply("@price - (@price * 0.1)", "discounted").build();

            Mono<AggregationReply<String, String>> agg1 = reactiveCommands
                    .ftAggregate("idx:bicycle", "@condition:{new}", agg1Args).doOnNext(result -> {
                        result.getReplies().get(0).getResults().stream()
                                .sorted((doc1, doc2) -> doc1.getFields().get("__key").compareTo(doc2.getFields().get("__key")))
                                .forEach(doc -> {
                                    System.out.printf("Key: %s, Price: %s, Discounted: %s\n", doc.getFields().get("__key"),
                                            doc.getFields().get("price"), doc.getFields().get("discounted"));
                                });
                        // >>> Key: bicycle:0, Price: 270, Discounted: 243
                        // >>> Key: bicycle:5, Price: 810, Discounted: 729
                        // >>> Key: bicycle:6, Price: 2300, Discounted: 2070
                        // >>> Key: bicycle:7, Price: 430, Discounted: 387
                        // >>> Key: bicycle:8, Price: 1200, Discounted: 1080
                    });
```

##### Java (Synchronous - Jedis)

```java
        AggregationResult res1 = jedis.ftAggregate("idx:bicycle",
            new AggregationBuilder("@condition:{new}")
                    .load("__key", "price")
                    .apply("@price - (@price * 0.1)", "discounted")
        );
        
        List<Row> rows1 = res1.getRows();
        System.out.println(rows1.size());   // >>> 5

        for (int i = 0; i < rows1.size(); i++) {
            System.out.println(rows1.get(i));
        }
        // >>> {__key=bicycle:0, discounted=243, price=270}
        // >>> {__key=bicycle:5, discounted=729, price=810}
        // >>> {__key=bicycle:6, discounted=2070, price=2300}
        // >>> {__key=bicycle:7, discounted=387, price=430}
        // >>> {__key=bicycle:8, discounted=1080, price=1200}
```

##### JavaScript (Node.js)

```javascript
const res1 = await client.ft.aggregate('idx:bicycle', '@condition:{new}', {
  LOAD: ['__key', 'price'],
  APPLY: {
    expression: '@price - (@price * 0.1)',
    AS: 'discounted'
  }
});

console.log(res1.results.length); // >>> 5
console.log(res1.results); // >>>
//[
//  [Object: null prototype] { __key: 'bicycle:0', price: '270' },
//  [Object: null prototype] { __key: 'bicycle:5', price: '810' },
//  [Object: null prototype] { __key: 'bicycle:6', price: '2300' },
//  [Object: null prototype] { __key: 'bicycle:7', price: '430' },
//  [Object: null prototype] { __key: 'bicycle:8', price: '1200' }
//]
```

##### Python

```python
search = Search(r, index_name="idx:bicycle")
aggregate_request = AggregateRequest(query='@condition:{new}') \
    .load('__key', 'price') \
    .apply(discounted='@price - (@price * 0.1)')
res = search.aggregate(aggregate_request)
print(len(res.rows)) # >>> 5
print(res.rows) # >>> [['__key', 'bicycle:0', ...
#[['__key', 'bicycle:0', 'price', '270', 'discounted', '243'],
# ['__key', 'bicycle:5', 'price', '810', 'discounted', '729'],
# ['__key', 'bicycle:6', 'price', '2300', 'discounted', '2070'],
# ['__key', 'bicycle:7', 'price', '430', 'discounted', '387'],
# ['__key', 'bicycle:8', 'price', '1200', 'discounted', '1080']]
```



The field `__key` is a built-in field. 

The output of this query is:

```
1) "1"
2) 1) "__key"
   1) "bicycle:0"
   2) "price"
   3) "270"
   4) "discounted"
   5) "243"
3) 1) "__key"
   1) "bicycle:5"
   2) "price"
   3) "810"
   4) "discounted"
   5) "729"
4) 1) "__key"
   1) "bicycle:6"
   2) "price"
   3) "2300"
   4) "discounted"
   5) "2070"
...
```

## Grouping with aggregation

The previous example did not group the data. You can group and aggregate data based on one or many criteria in the following way:

```
FT.AGGREGATE index "query_expr" ...  GROUPBY n "field_1" .. "field_n" REDUCE AGG_FUNC m "@field_param_1" .. "@field_param_m" AS "aggregated_result_field"
```

Here is an explanation of the additional constructs:

1. **Grouping**: you can group by one or many fields. Each ordered sequence of field values then defines one group. It's also possible to group by values that resulted from a previous `APPLY ... AS`.
2. **Aggregation**: you must replace `AGG_FUNC` with one of the supported aggregation functions (e.g., `SUM` or `COUNT`). A complete list of functions is available in the [aggregations reference documentation](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/aggregations). Replace `aggregated_result_field` with a value of your choice.

The following query shows you how to group by the field `condition` and apply a reduction based on the previously derived `price_category`. The expression `@price<1000` causes a bicycle to have the price category `1` if its price is lower than 1000 USD. Otherwise, it has the price category `0`. The output is the number of affordable bicycles grouped by price category.

Grouping with aggregation: Use GROUPBY with REDUCE to group results by field values and apply aggregation functions when you need to summarize data across groups

**Difficulty:** Intermediate

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), Python

##### Redis CLI

```
FT.AGGREGATE idx:bicycle "*" LOAD 1 price APPLY "@price<1000" AS price_category GROUPBY 1 @condition REDUCE SUM 1 "@price_category" AS "num_affordable"
```

##### C#

```csharp
        AggregationResult res2 = db.FT().Aggregate(
            "idx:bicycle",
            new AggregationRequest("*")
                .Load(new FieldName("price"))
                .Apply("@price<1000", "price_category")
                .GroupBy(
                    "@condition",
                    Reducers.Sum("@price_category").As("num_affordable")
                )
        );
        Console.WriteLine(res2.TotalResults);   // >>> 3

        for (int i = 0; i < res2.TotalResults; i++)
        {
            Row res2Row = res2.GetRow(i);

            Console.WriteLine(
                $"Condition: {res2Row["condition"]}, Num affordable: {res2Row["num_affordable"]}"
            );
        }
        // >>> Condition: refurbished, Num affordable: 1
        // >>> Condition: used, Num affordable: 1
        // >>> Condition: new, Num affordable: 3
```

##### Go

```go
	res2, err := rdb.FTAggregateWithArgs(ctx,
		"idx:bicycle", "*",
		&redis.FTAggregateOptions{
			Steps: []redis.FTAggregateStep{
				{Load: &redis.FTAggregateLoad{Field: "price"}},
				{Apply: &redis.FTAggregateApply{
					Field: "@price<1000",
					As:    "price_category",
				}},
				{GroupBy: &redis.FTAggregateGroupBy{
					Fields: []interface{}{"@condition"},
					Reduce: []redis.FTAggregateReducer{
						{
							Reducer: redis.SearchSum,
							Args:    []interface{}{"@price_category"},
							As:      "num_affordable",
						},
					},
				}},
			},
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(len(res2.Rows)) // >>> 3

	sort.Slice(res2.Rows, func(i, j int) bool {
		return res2.Rows[i].Fields["condition"].(string) <
			res2.Rows[j].Fields["condition"].(string)
	})

	for _, row := range res2.Rows {
		fmt.Printf(
			"condition=%v, num_affordable=%v\n",
			row.Fields["condition"],
			row.Fields["num_affordable"],
		)
	}
	// >>> condition=new, num_affordable=3
	// >>> condition=refurbished, num_affordable=1
	// >>> condition=used, num_affordable=1
```

##### Java (Asynchronous - Lettuce)

```java
            AggregateArgs<String, String> agg2Args = AggregateArgs.<String, String> builder().load("price")
                    .apply("@price<1000", "price_category").groupBy(GroupBy.<String, String> of("condition")
                            .reduce(Reducer.<String, String> sum("@price_category").as("num_affordable")))
                    .build();

            CompletableFuture<AggregationReply<String, String>> agg2 = asyncCommands.ftAggregate("idx:bicycle", "*", agg2Args)
                    .thenApply(result -> {
                        result.getReplies().get(0).getResults().stream().sorted(
                                (doc1, doc2) -> doc1.getFields().get("condition").compareTo(doc2.getFields().get("condition")))
                                .forEach(doc -> {
                                    System.out.printf("Condition: %s, Num Affordable: %s\n", doc.getFields().get("condition"),
                                            doc.getFields().get("num_affordable"));
                                });
                        // >>> Condition: new, Num Affordable: 3
                        // >>> Condition: refurbished, Num Affordable: 1
                        // >>> Condition: used, Num Affordable: 1
                        return result;
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            AggregateArgs<String, String> agg2Args = AggregateArgs.<String, String> builder().load("price")
                    .apply("@price<1000", "price_category").groupBy(GroupBy.<String, String> of("condition")
                            .reduce(Reducer.<String, String> sum("@price_category").as("num_affordable")))
                    .build();

            Mono<AggregationReply<String, String>> agg2 = reactiveCommands.ftAggregate("idx:bicycle", "*", agg2Args)
                    .doOnNext(result -> {
                        result.getReplies().get(0).getResults().stream().sorted(
                                (doc1, doc2) -> doc1.getFields().get("condition").compareTo(doc2.getFields().get("condition")))
                                .forEach(doc -> {
                                    System.out.printf("Condition: %s, Num Affordable: %s\n", doc.getFields().get("condition"),
                                            doc.getFields().get("num_affordable"));
                                });
                        // >>> Condition: new, Num Affordable: 3
                        // >>> Condition: refurbished, Num Affordable: 1
                        // >>> Condition: used, Num Affordable: 1
                    });
```

##### Java (Synchronous - Jedis)

```java
        AggregationResult res2 = jedis.ftAggregate("idx:bicycle",
            new AggregationBuilder("*")
                    .load("price")
                    .apply("@price<1000", "price_category")
                    .groupBy("@condition",
                        Reducers.sum("@price_category").as("num_affordable"))
        );

        List<Row> rows2 = res2.getRows();
        System.out.println(rows2.size());   // >>> 3

        for (int i = 0; i < rows2.size(); i++) {
            System.out.println(rows2.get(i));
        }
        // >>> {condition=refurbished, num_affordable=1}
        // >>> {condition=used, num_affordable=1}
        // >>> {condition=new, num_affordable=3}
```

##### JavaScript (Node.js)

```javascript
const res2 = await client.ft.aggregate('idx:bicycle', '*', {
  LOAD: ['@price'],
  STEPS: [{
      type: FT_AGGREGATE_STEPS.APPLY,
      expression: '@price<1000',
      AS: 'price_category'
    },{
      type: FT_AGGREGATE_STEPS.GROUPBY,
      properties: '@condition',
      REDUCE:[{
        type: FT_AGGREGATE_GROUP_BY_REDUCERS.SUM,
        property: '@price_category',
        AS: 'num_affordable'
      }]
    }]
});
console.log(res2.results.length); // >>> 3
console.log(res2.results); // >>>
//[[Object: null prototype] { condition: 'refurbished', num_affordable: '1' },
//  [Object: null prototype] { condition: 'used', num_affordable: '1' },
//  [Object: null prototype] { condition: 'new', num_affordable: '3' }
//]
```

##### Python

```python
search = Search(r, index_name="idx:bicycle")
aggregate_request = AggregateRequest(query='*') \
    .load('price') \
    .apply(price_category='@price<1000') \
    .group_by('@condition', reducers.sum('@price_category').alias('num_affordable'))
res = search.aggregate(aggregate_request)
print(len(res.rows)) # >>> 3
print(res.rows) # >>>
#[['condition', 'refurbished', 'num_affordable', '1'],
# ['condition', 'used', 'num_affordable', '1'],
# ['condition', 'new', 'num_affordable', '3']]
```



```
1) "3"
2) 1) "condition"
   1) "refurbished"
   2) "num_affordable"
   3) "1"
3) 1) "condition"
   1) "used"
   2) "num_affordable"
   3) "1"
4) 1) "condition"
   1) "new"
   2) "num_affordable"
   3) "3"
```

> [!NOTE]
> You can also create more complex aggregation pipelines with [FT.AGGREGATE](https://redis.io/docs/latest/commands/ft.aggregate). Applying multiple reduction functions under one `GROUPBY` clause is possible. In addition, you can also chain groupings and mix in additional mapping steps (e.g., `GROUPBY ... REDUCE ... APPLY ... GROUPBY ... REDUCE`)


## Aggregating without grouping

You can't use an aggregation function outside of a `GROUPBY` clause, but you can construct your pipeline in a way that the aggregation happens on a single group that spans all documents. If your documents don't share a common attribute, you can add it via an extra `APPLY` step.

Here is an example that adds a type attribute `bicycle` to each document before counting all documents with that type:

Aggregating without grouping: Create a dummy grouping field with APPLY to aggregate across all documents when you need a single aggregate result

**Difficulty:** Intermediate

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), Python

##### Redis CLI

```
FT.AGGREGATE idx:bicycle "*" APPLY "'bicycle'" AS type GROUPBY 1 @type REDUCE COUNT 0 AS num_total
```

##### C#

```csharp
        AggregationResult res3 = db.FT().Aggregate(
            "idx:bicycle",
            new AggregationRequest("*")
                .Apply("'bicycle'", "type")
                .GroupBy("@type", Reducers.Count().As("num_total"))
        );
        Console.WriteLine(res3.TotalResults);   // >>> 1

        Row res3Row = res3.GetRow(0);
        Console.WriteLine($"Type: {res3Row["type"]}, Num total: {res3Row["num_total"]}");
        // >>> Type: bicycle, Num total: 10
```

##### Go

```go

	res3, err := rdb.FTAggregateWithArgs(ctx,
		"idx:bicycle", "*",
		&redis.FTAggregateOptions{
			Steps: []redis.FTAggregateStep{
				{Apply: &redis.FTAggregateApply{
					Field: "'bicycle'",
					As:    "type",
				}},
				{GroupBy: &redis.FTAggregateGroupBy{
					Fields: []interface{}{"@type"},
					Reduce: []redis.FTAggregateReducer{
						{
							Reducer: redis.SearchCount,
							As:      "num_total",
						},
					},
				}},
			},
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(len(res3.Rows)) // >>> 1

	for _, row := range res3.Rows {
		fmt.Printf(
			"type=%v, num_total=%v\n",
			row.Fields["type"],
			row.Fields["num_total"],
		)
	}
	// type=bicycle, num_total=10
```

##### Java (Asynchronous - Lettuce)

```java
            AggregateArgs<String, String> agg3Args = AggregateArgs.<String, String> builder().apply("'bicycle'", "type")
                    .groupBy(GroupBy.<String, String> of("type").reduce(Reducer.<String, String> count().as("num_total")))
                    .build();

            CompletableFuture<AggregationReply<String, String>> agg3 = asyncCommands.ftAggregate("idx:bicycle", "*", agg3Args)
                    .thenApply(result -> {
                        result.getReplies().get(0).getResults().stream()
                                .sorted((doc1, doc2) -> doc1.getFields().get("type").compareTo(doc2.getFields().get("type")))
                                .forEach(doc -> {
                                    System.out.printf("Type: %s, Total Count: %s\n", doc.getFields().get("type"),
                                            doc.getFields().get("num_total"));
                                });
                        // >>> Type: bicycle, Total Count: 10
                        return result;
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            AggregateArgs<String, String> agg3Args = AggregateArgs.<String, String> builder().apply("'bicycle'", "type")
                    .groupBy(GroupBy.<String, String> of("type").reduce(Reducer.<String, String> count().as("num_total")))
                    .build();

            Mono<AggregationReply<String, String>> agg3 = reactiveCommands.ftAggregate("idx:bicycle", "*", agg3Args)
                    .doOnNext(result -> {
                        result.getReplies().get(0).getResults().stream()
                                .sorted((doc1, doc2) -> doc1.getFields().get("type").compareTo(doc2.getFields().get("type")))
                                .forEach(doc -> {
                                    System.out.printf("Type: %s, Total Count: %s\n", doc.getFields().get("type"),
                                            doc.getFields().get("num_total"));
                                });
                        // >>> Type: bicycle, Total Count: 10
                    });
```

##### Java (Synchronous - Jedis)

```java
        AggregationResult res3 = jedis.ftAggregate("idx:bicycle",
            new AggregationBuilder("*")
                    .apply("'bicycle'", "type")
                    .groupBy("@type", Reducers.count().as("num_total"))
        );

        List<Row> rows3 = res3.getRows();
        System.out.println(rows3.size());   // >>> 1

        for (int i = 0; i < rows3.size(); i++) {
            System.out.println(rows3.get(i));
        }
        // >>> {type=bicycle, num_total=10}
```

##### JavaScript (Node.js)

```javascript
const res3 = await client.ft.aggregate('idx:bicycle', '*', {
  STEPS: [{
      type: FT_AGGREGATE_STEPS.APPLY,
      expression: "'bicycle'",
      AS: 'type'
    }, {
      type: FT_AGGREGATE_STEPS.GROUPBY,
      properties: '@type',
      REDUCE: [{
        type: FT_AGGREGATE_GROUP_BY_REDUCERS.COUNT,
        property: null,
        AS: 'num_total'
      }]
    }]
});
console.log(res3.results.length); // >>> 1
console.log(res3.results); // >>>
//[ [Object: null prototype] { type: 'bicycle', num_total: '10' } ]
```

##### Python

```python
search = Search(r, index_name="idx:bicycle")
aggregate_request = AggregateRequest(query='*') \
    .apply(type="'bicycle'") \
    .group_by('@type', reducers.count().alias('num_total'))
res = search.aggregate(aggregate_request)
print(len(res.rows)) # >>> 1
print(res.rows) # >>> [['type', 'bicycle', 'num_total', '10']]
```



The result is:

```
1) "1"
2) 1) "type"
   1) "bicycle"
   2) "num_total"
   3) "10"
```

## Grouping without aggregation

It's sometimes necessary to group your data without applying a mathematical aggregation function. If you need a grouped list of values, then the `TOLIST` function is helpful.

The following example shows how to group all bicycles by `condition`:

Grouping without aggregation: Use TOLIST to collect grouped values without applying mathematical functions when you need to organize results by category

**Difficulty:** Intermediate

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), Python

##### Redis CLI

```
FT.AGGREGATE idx:bicycle "*" LOAD 1 "__key" GROUPBY 1 "@condition" REDUCE TOLIST 1 "__key" AS bicycles
```

##### C#

```csharp

        // Not supported in NRedisStack.

```

##### Go

```go
	res4, err := rdb.FTAggregateWithArgs(ctx,
		"idx:bicycle", "*",
		&redis.FTAggregateOptions{
			Steps: []redis.FTAggregateStep{
				{Load: &redis.FTAggregateLoad{Field: "__key"}},
				{GroupBy: &redis.FTAggregateGroupBy{
					Fields: []interface{}{"@condition"},
					Reduce: []redis.FTAggregateReducer{
						{
							Reducer: redis.SearchToList,
							Args:    []interface{}{"__key"},
							As:      "bicycles",
						},
					},
				}},
			},
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(len(res4.Rows)) // >>> 3

	sort.Slice(res4.Rows, func(i, j int) bool {
		return res4.Rows[i].Fields["condition"].(string) <
			res4.Rows[j].Fields["condition"].(string)
	})

	for _, row := range res4.Rows {
		rowBikes := row.Fields["bicycles"].([]interface{})
		bikes := make([]string, len(rowBikes))

		for i, rowBike := range rowBikes {
			bikes[i] = rowBike.(string)
		}

		sort.Slice(bikes, func(i, j int) bool {
			return bikes[i] < bikes[j]
		})

		fmt.Printf(
			"condition=%v, bicycles=%v\n",
			row.Fields["condition"],
			bikes,
		)
	}
	// >>> condition=new, bicycles=[bicycle:0 bicycle:5 bicycle:6 bicycle:7 bicycle:8]
	// >>> condition=refurbished, bicycles=[bicycle:9]
	// >>> condition=used, bicycles=[bicycle:1 bicycle:2 bicycle:3 bicycle:4]
```

##### Java (Asynchronous - Lettuce)

```java

            // The `TOLIST` reducer is not currently available in Lettuce.

```

##### Java (Reactive - Lettuce)

```java

            // The `TOLIST` reducer is not currently available in Lettuce.

```

##### Java (Synchronous - Jedis)

```java
        AggregationResult res4 = jedis.ftAggregate("idx:bicycle",
            new AggregationBuilder("*")
                    .load("__key")
                    .groupBy("@condition",
                        Reducers.to_list("__key").as("bicycles"))
        );

        List<Row> rows4 = res4.getRows();
        System.out.println(rows4.size());   // >>> 3

        for (int i = 0; i < rows4.size(); i++) {
            System.out.println(rows4.get(i));
        }
        // >>> {condition=refurbished, bicycles=[bicycle:9]}
        // >>> {condition=used, bicycles=[bicycle:3, bicycle:4, bicycle:1, bicycle:2]}
        // >>> {condition=new, bicycles=[bicycle:7, bicycle:0, bicycle:5, bicycle:6, bicycle:8]}
```

##### JavaScript (Node.js)

```javascript
const res4 = await client.ft.aggregate('idx:bicycle', '*', {
  LOAD: ['__key'],
  STEPS: [{
      type: FT_AGGREGATE_STEPS.GROUPBY,
      properties: '@condition',
      REDUCE: [{
        type: FT_AGGREGATE_GROUP_BY_REDUCERS.TOLIST,
        property: '__key',
        AS: 'bicycles'
      }]
    }]
});
console.log(res4.results.length); // >>> 3
console.log(res4.results); // >>>
//[[Object: null prototype] {condition: 'refurbished', bicycles: [ 'bicycle:9' ]},
//  [Object: null prototype] {condition: 'used', bicycles: [ 'bicycle:1', 'bicycle:2', 'bicycle:3', 'bicycle:4' ]},
//  [Object: null prototype] {condition: 'new', bicycles: [ 'bicycle:5', 'bicycle:6', 'bicycle:7', 'bicycle:0', 'bicycle:8' ]}]
```

##### Python

```python
search = Search(r, index_name="idx:bicycle")
aggregate_request = AggregateRequest(query='*') \
    .load('__key') \
    .group_by('@condition', reducers.tolist('__key').alias('bicycles'))
res = search.aggregate(aggregate_request)
print(len(res.rows)) # >>> 3
print(res.rows) # >>>
#[['condition', 'refurbished', 'bicycles', ['bicycle:9']],
# ['condition', 'used', 'bicycles', ['bicycle:1', 'bicycle:2', 'bicycle:3', 'bicycle:4']],
# ['condition', 'new', 'bicycles', ['bicycle:5', 'bicycle:6', 'bicycle:7', 'bicycle:0', 'bicycle:8']]]
```



The output of this query is:

```
1) "3"
2) 1) "condition"
   1) "refurbished"
   2) "bicycles"
   3) 1) "bicycle:9"
3) 1) "condition"
   1) "used"
   2) "bicycles"
   3) 1) "bicycle:1"
      1) "bicycle:2"
      2) "bicycle:3"
      3) "bicycle:4"
4) 1) "condition"
   1) "new"
   2) "bicycles"
   3) 1) "bicycle:0"
      1) "bicycle:5"
      2) "bicycle:6"
      3) "bicycle:8"
      4) "bicycle:7"
```
