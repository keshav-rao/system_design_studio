# Geospatial queries

```json metadata
{
  "schema_version": 2,
  "title": "Geospatial queries",
  "description": "Query based on geographic data",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"radius","title":"Radius"},{"id":"shape","title":"Shape"}]}

,
  "codeExamples": [{"codetabsId":"query_geo-stepgeo1","description":"Foundational: Query geographic locations within a radius using center coordinates and distance when you need to find nearby points of interest","difficulty":"beginner","id":"geo1","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_query_geo-stepgeo1"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_query_geo-stepgeo1"},{"id":"Node-js","panelId":"panel_Nodejs_query_geo-stepgeo1"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_query_geo-stepgeo1"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_query_geo-stepgeo1"}]},{"codetabsId":"query_geo-stepgeo2","description":"Spatial operators: Query geometric shapes using CONTAINS to test which shapes enclose another shape when you need to find bounding regions","difficulty":"intermediate","id":"geo2","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_query_geo-stepgeo2"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_query_geo-stepgeo2"},{"id":"Node-js","panelId":"panel_Nodejs_query_geo-stepgeo2"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_query_geo-stepgeo2"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_query_geo-stepgeo2"}]},{"codetabsId":"query_geo-stepgeo3","description":"Spatial operators: Query geometric shapes using the WITHIN operator to find shapes contained in a region when you need to identify items within geographic boundaries","difficulty":"intermediate","id":"geo3","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_query_geo-stepgeo3"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_query_geo-stepgeo3"},{"id":"Node-js","panelId":"panel_Nodejs_query_geo-stepgeo3"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_query_geo-stepgeo3"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_query_geo-stepgeo3"}]}]
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


The geospatial feature in Redis Open Source allows you to query for data associated with geographic locations. You can either query for locations within a specific radius or based on geometric shapes, such as polygons. A polygon shape could, for instance, represent a lake or the layout of a building.

The examples in this article use the following schema:

| Field name       | Field type   |
| --------------   | ----------   |
| `store_location` | `GEO`        |
| `pickup_zone`    | `GEOSHAPE`   |


> [!NOTE]
> Redis version 7.2.0 or higher is required to use the `GEOSHAPE` field type.

## Radius

You can construct a radius query by passing the center coordinates (longitude, latitude), the radius, and the distance unit to the [FT.SEARCH](https://redis.io/docs/latest/commands/ft.search) command.

```
FT.SEARCH index "@geo_field:[lon lat radius unit]"
```

Allowed units are `m`, `km`, `mi`, and `ft`.

The following query finds all bicycle stores within a radius of 20 miles around London:

Foundational: Query geographic locations within a radius using center coordinates and distance when you need to find nearby points of interest

**Difficulty:** Beginner

**Available in:** Redis CLI, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python

##### Redis CLI

```
FT.SEARCH idx:bicycle "@store_location:[-0.1778 51.5524 20 mi]"
```

##### Go

```go
	res1, err := rdb.FTSearchWithArgs(ctx,
		"idx:bicycle", "@store_location:[$lon $lat $radius $units]",
		&redis.FTSearchOptions{
			Params: map[string]interface{}{
				"lon":    -0.1778,
				"lat":    51.5524,
				"radius": 20,
				"units":  "mi",
			},
			DialectVersion: 2,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1.Total) // >>> 1

	for _, doc := range res1.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:5
```

##### Java (Synchronous - Jedis)

```java
        SearchResult res1 = jedis.ftSearch("idx:bicycle",
            "@store_location:[$lon $lat $radius $units]",
            FTSearchParams.searchParams()
                    .addParam("lon", -0.1778)
                    .addParam("lat", 51.5524)
                    .addParam("radius", 20)
                    .addParam("units", "mi")
                    .dialect(2)
        );
        System.out.println(res1.getTotalResults()); // >>> 1

        List<Document> docs1 = res1.getDocuments();

        for (Document document : docs1) {
            System.out.println(document.getId());
        }
        // >>> bicycle:5
```

##### JavaScript (Node.js)

```javascript
const res1= await client.ft.search('idx:bicycle', '@store_location:[-0.1778 51.5524 20 mi]');
console.log(res1.total); // >>> 1
console.log(res1); // >>> {total: 1, documents: [ { id: 'bicycle:5', value: [Object: null prototype] } ]}
```

##### Python

```python
params_dict = {"lon": -0.1778, "lat": 51.5524, "radius": 20, "units": "mi"}
q = Query("@store_location:[$lon $lat $radius $units]").dialect(2)
res = index.search(q, query_params=params_dict)
print(res)
# >>> Result{1 total, docs: [Document {'id': 'bicycle:5', ...
```



## Shape

The only supported shapes are points and polygons. You can query for polygons or points that either contain or are within a given geometric shape.

```
FT.SEARCH index "@geo_shape_field:[{WITHIN|CONTAINS|INTERSECTS|DISJOINT} $shape] PARAMS 2 shape "shape_as_wkt" DIALECT 3
```

Here is a more detailed explanation of this query:

1. **Field name**: you need to replace `geo_shape_field` with the `GEOSHAPE` field's name on which you want to query.
2. **Spatial operator**: spatial operators define the relationship between the shapes in the database and the shape you are searching for. You can either use `WITHIN`, `CONTAINS`, `INTERSECTS`, or `DISJOINT`. `WITHIN` finds any shape in the database that is inside the given shape. `CONTAINS` queries for any shape that surrounds the given shape. `INTERSECTS` finds any shape that has coordinates in common with the provided shape. `DISJOINT` finds any shapes that have nothing in common with the provided shape. `INTERSECTS` and `DISJOINT` were introduced in v2.10.
3. **Parameter**: the query refers to a parameter named `shape`. You can use any parameter name here. You need to use the `PARAMS` clause to set the parameter value. The value follows the [well-known text representation of a geometry](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry). Supported types are `POINT(x y)` and `POLYGON((x1 y1, x2 y2, ...))`.
4. **Dialect**: Shape-based queries are not supported in `DIALECT 1`.

The following example query verifies if a bicycle is within a pickup zone:

Spatial operators: Query geometric shapes using CONTAINS to test which shapes enclose another shape when you need to find bounding regions

**Difficulty:** Intermediate

**Available in:** Redis CLI, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python

##### Redis CLI

```
FT.SEARCH idx:bicycle "@pickup_zone:[CONTAINS $bike]" PARAMS 2 bike "POINT(-0.1278 51.5074)" DIALECT 2
```

##### Go

```go
	res2, err := rdb.FTSearchWithArgs(ctx,
		"idx:bicycle",
		"@pickup_zone:[CONTAINS $bike]",
		&redis.FTSearchOptions{
			Params: map[string]interface{}{
				"bike": "POINT(-0.1278 51.5074)",
			},
			DialectVersion: 3,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2.Total) // >>> 1

	for _, doc := range res2.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:5
```

##### Java (Synchronous - Jedis)

```java
        SearchResult res2 = jedis.ftSearch("idx:bicycle",
            "@pickup_zone:[CONTAINS $bike]",
            FTSearchParams.searchParams()
                    .addParam("bike", "POINT(-0.1278 51.5074)")
                    .dialect(3)
        );
        System.out.println(res2.getTotalResults());   // >>> 1

        List<Document> docs2 = res2.getDocuments();

        for (Document document : docs2) {
            System.out.println(document.getId());
        }
        // >>> bicycle:5
```

##### JavaScript (Node.js)

```javascript
const params_dict_geo2 = { bike: 'POINT(-0.1278 51.5074)' };
const q_geo2 = '@pickup_zone:[CONTAINS $bike]';
const res2 = await client.ft.search('idx:bicycle', q_geo2, { PARAMS: params_dict_geo2, DIALECT: 3 });
console.log(res2.total); // >>> 1
console.log(res2); // >>> {total: 1, documents: [ { id: 'bicycle:5', value: [Object: null prototype] } ]}
```

##### Python

```python
params_dict = {"bike": "POINT(-0.1278 51.5074)"}
q = Query("@pickup_zone:[CONTAINS $bike]").dialect(3)
res = index.search(q, query_params=params_dict)
print(res.total) # >>> 1
```



If you want to find all pickup zones that are approximately within Europe, then you can use the following query:

Spatial operators: Query geometric shapes using the WITHIN operator to find shapes contained in a region when you need to identify items within geographic boundaries

**Difficulty:** Intermediate

**Available in:** Redis CLI, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python

##### Redis CLI

```
FT.SEARCH idx:bicycle "@pickup_zone:[WITHIN $europe]" PARAMS 2 europe "POLYGON((-25 35, 40 35, 40 70, -25 70, -25 35))" DIALECT 2
```

##### Go

```go
	res3, err := rdb.FTSearchWithArgs(ctx,
		"idx:bicycle",
		"@pickup_zone:[WITHIN $europe]",
		&redis.FTSearchOptions{
			Params: map[string]interface{}{
				"europe": "POLYGON((-25 35, 40 35, 40 70, -25 70, -25 35))",
			},
			DialectVersion: 3,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3.Total) // >>> 5

	sort.Slice(res3.Docs, func(i, j int) bool {
		return res3.Docs[i].ID < res3.Docs[j].ID
	})

	for _, doc := range res3.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:5
	// >>> bicycle:6
	// >>> bicycle:7
	// >>> bicycle:8
	// >>> bicycle:9
```

##### Java (Synchronous - Jedis)

```java
        SearchResult res3 = jedis.ftSearch("idx:bicycle",
            "@pickup_zone:[WITHIN $europe]",
            FTSearchParams.searchParams()
                    .addParam("europe", "POLYGON((-25 35, 40 35, 40 70, -25 70, -25 35))")
                    .dialect(3)
        );
        System.out.println(res3.getTotalResults()); // >>> 5

        List<Document> docs3 = res3.getDocuments();

        for (Document document : docs3) {
            System.out.println(document.getId());
        }
        // >>> bicycle:5
        // >>> bicycle:6
        // >>> bicycle:7
        // >>> bicycle:8
        // >>> bicycle:9
```

##### JavaScript (Node.js)

```javascript
const params_dict_geo3 = { europe: 'POLYGON((-25 35, 40 35, 40 70, -25 70, -25 35))' };
const q_geo3 = '@pickup_zone:[WITHIN $europe]';
const res3 = await client.ft.search('idx:bicycle', q_geo3, { PARAMS: params_dict_geo3, DIALECT: 3 });
console.log(res3.total); // >>> 5
console.log(res3); // >>>
// {
//   total: 5,
//   documents: [
//     { id: 'bicycle:5', value: [Object: null prototype] },
//     { id: 'bicycle:6', value: [Object: null prototype] },
//     { id: 'bicycle:7', value: [Object: null prototype] },
//     { id: 'bicycle:8', value: [Object: null prototype] },
//     { id: 'bicycle:9', value: [Object: null prototype] }
//   ]
// }
```

##### Python

```python
params_dict = {"europe": "POLYGON((-25 35, 40 35, 40 70, -25 70, -25 35))"}
q = Query("@pickup_zone:[WITHIN $europe]").dialect(3)
res = index.search(q, query_params=params_dict)
print(res.total) # >>> 5
```



