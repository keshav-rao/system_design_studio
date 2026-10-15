# Redis geospatial

```json metadata
{
  "schema_version": 2,
  "title": "Redis geospatial",
  "description": "Introduction to the Redis Geospatial data type",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"examples","title":"Examples"},{"id":"learn-more","title":"Learn more"}]}

,
  "codeExamples": [{"codetabsId":"geo_tutorial-stepgeoadd","commands":[{"acl_categories":["@write","@geo","@slow"],"complexity":"O(log(N)","name":"GEOADD"}],"description":"Foundational: Add geographic coordinates to a geospatial index using GEOADD to store location data","difficulty":"beginner","id":"geoadd","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_geo_tutorial-stepgeoadd"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_geo_tutorial-stepgeoadd"},{"id":"Node-js","panelId":"panel_Nodejs_geo_tutorial-stepgeoadd"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_geo_tutorial-stepgeoadd"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_geo_tutorial-stepgeoadd"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_geo_tutorial-stepgeoadd"}]},{"buildsUpon":["geoadd"],"codetabsId":"geo_tutorial-stepgeosearch","commands":[{"acl_categories":["@read","@geo","@slow"],"complexity":"O(N+log(M)","name":"GEOSEARCH"}],"description":"Proximity search: Use GEOSEARCH to find locations within a radius or bounding box when you need to discover nearby points","difficulty":"intermediate","id":"geosearch","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_geo_tutorial-stepgeosearch"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_geo_tutorial-stepgeosearch"},{"id":"Node-js","panelId":"panel_Nodejs_geo_tutorial-stepgeosearch"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_geo_tutorial-stepgeosearch"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_geo_tutorial-stepgeosearch"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_geo_tutorial-stepgeosearch"}]}]
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


### Geospatial command summary

**10 commands in this group:**

[View all geo commands](https://redis.io/commands/?group=geo)

| Command | Summary | Complexity | Since |
|---------|---------|------------|-------|
| [GEOADD](https://redis.io/commands/geoadd/) | Adds one or more members to a geospatial index. The key is created if it doesn't exist. | O(log(N)) for each item added, where N is the n... | 3.2.0 |
| [GEODIST](https://redis.io/commands/geodist/) | Returns the distance between two members of a geospatial index. | O(1) | 3.2.0 |
| [GEOHASH](https://redis.io/commands/geohash/) | Returns members from a geospatial index as geohash strings. | O(1) for each member requested. | 3.2.0 |
| [GEOPOS](https://redis.io/commands/geopos/) | Returns the longitude and latitude of members from a geospatial index. | O(1) for each member requested. | 3.2.0 |
| [GEORADIUS](https://redis.io/commands/georadius/) | Queries a geospatial index for members within a distance from a coordinate, optionally stores the result. | O(N+log(M)) where N is the number of elements i... | 3.2.0 |
| [GEORADIUS_RO](https://redis.io/commands/georadius_ro/) | Returns members from a geospatial index that are within a distance from a coordinate. | O(N+log(M)) where N is the number of elements i... | 3.2.10 |
| [GEORADIUSBYMEMBER](https://redis.io/commands/georadiusbymember/) | Queries a geospatial index for members within a distance from a member, optionally stores the result. | O(N+log(M)) where N is the number of elements i... | 3.2.0 |
| [GEORADIUSBYMEMBER_RO](https://redis.io/commands/georadiusbymember_ro/) | Returns members from a geospatial index that are within a distance from a member. | O(N+log(M)) where N is the number of elements i... | 3.2.10 |
| [GEOSEARCH](https://redis.io/commands/geosearch/) | Queries a geospatial index for members inside an area of a box or a circle. | O(N+log(M)) where N is the number of elements i... | 6.2.0 |
| [GEOSEARCHSTORE](https://redis.io/commands/geosearchstore/) | Queries a geospatial index for members inside an area of a box or a circle, optionally stores the result. | O(N+log(M)) where N is the number of elements i... | 6.2.0 |



Redis geospatial indexes let you store coordinates and search for them.
This data structure is useful for finding nearby points within a given radius or bounding box.

> [!NOTE]
> Take care not to confuse the Geospatial data type with the
> [Geospatial](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/geo)
> features in [Redis Search](https://redis.io/docs/latest/develop/ai/search-and-query).
> Although there are some similarities between these two features, the data type is intended
> for simpler use cases and doesn't have the range of format options and queries
> available in Redis Search.

## Examples

Suppose you're building a mobile app that lets you find all of the bike rental stations closest to your current location.

Add several locations to a geospatial index:
Foundational: Add geographic coordinates to a geospatial index using GEOADD to store location data

**Commands:** GEOADD

**Complexity:**
- GEOADD: O(log(N)

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python

##### Redis CLI

```
> GEOADD bikes:rentable -122.27652 37.805186 station:1
(integer) 1
> GEOADD bikes:rentable -122.2674626 37.8062344 station:2
(integer) 1
> GEOADD bikes:rentable -122.2469854 37.8104049 station:3
(integer) 1
```

##### C#

```csharp
        bool res1 = db.GeoAdd("bikes:rentable", -122.27652, 37.805186, "station:1");
        Console.WriteLine(res1);    // >>> True

        bool res2 = db.GeoAdd("bikes:rentable", -122.2674626, 37.8062344, "station:2");
        Console.WriteLine(res2);    // >>> True

        bool res3 = db.GeoAdd("bikes:rentable", -122.2469854, 37.8104049, "station:3");
        Console.WriteLine(res3);    // >>> True
```

##### Go

```go
	res1, err := rdb.GeoAdd(ctx, "bikes:rentable",
		&redis.GeoLocation{
			Longitude: -122.27652,
			Latitude:  37.805186,
			Name:      "station:1",
		}).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // >>> 1

	res2, err := rdb.GeoAdd(ctx, "bikes:rentable",
		&redis.GeoLocation{
			Longitude: -122.2674626,
			Latitude:  37.8062344,
			Name:      "station:2",
		}).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2) // >>> 1

	res3, err := rdb.GeoAdd(ctx, "bikes:rentable",
		&redis.GeoLocation{
			Longitude: -122.2469854,
			Latitude:  37.8104049,
			Name:      "station:3",
		}).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3) // >>> 1
```

##### Java (Synchronous - Jedis)

```java
      long res1 = jedis.geoadd("bikes:rentable", -122.27652, 37.805186, "station:1");
      System.out.println(res1); // 1

      long res2 = jedis.geoadd("bikes:rentable", -122.2674626, 37.8062344, "station:2");
      System.out.println(res2); // 1

      long res3 = jedis.geoadd("bikes:rentable", -122.2469854, 37.8104049, "station:3");
      System.out.println(res2); // 1
```

##### JavaScript (Node.js)

```javascript
const res1 = await client.geoAdd('bikes:rentable', { 
  longitude: -122.27652,
  latitude: 37.805186,
  member: 'station:1'
});
console.log(res1)  // 1

const res2 = await client.geoAdd('bikes:rentable', {
  longitude: -122.2674626,
  latitude: 37.8062344,
  member: 'station:2'
});
console.log(res2)  // 1

const res3 = await client.geoAdd('bikes:rentable', {
  longitude: -122.2469854,
  latitude: 37.8104049,
  member: 'station:3'
})
console.log(res3)  // 1
```

##### Python

```python
res1 = r.geoadd("bikes:rentable", [-122.27652, 37.805186, "station:1"])
print(res1)  # >>> 1

res2 = r.geoadd("bikes:rentable", [-122.2674626, 37.8062344, "station:2"])
print(res2)  # >>> 1

res3 = r.geoadd("bikes:rentable", [-122.2469854, 37.8104049, "station:3"])
print(res3)  # >>> 1
```



Find all locations within a 5 kilometer radius of a given location, and return the distance to each location:
Proximity search: Use GEOSEARCH to find locations within a radius or bounding box when you need to discover nearby points

**Difficulty:** Intermediate

**Builds upon:** geoadd

**Commands:** GEOSEARCH

**Complexity:**
- GEOSEARCH: O(N+log(M)

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python

##### Redis CLI

```
> GEOSEARCH bikes:rentable FROMLONLAT -122.2612767 37.7936847 BYRADIUS 5 km WITHDIST
1) 1) "station:1"
   2) "1.8523"
2) 1) "station:2"
   2) "1.4979"
3) 1) "station:3"
   2) "2.2441"
```

##### C#

```csharp
        GeoRadiusResult[] res4 = db.GeoSearch("bikes:rentable",
            -122.27652,
            37.805186,
            new GeoSearchCircle(5, GeoUnit.Kilometers)
        );

        foreach (GeoRadiusResult member in res4)
        {
            Console.WriteLine($"Member: '{member.Member}', distance: {member.Distance}, position: {member.Position}");
        }
        // >>> Member: 'station:1', distance: 0.0001, position: -122.27652043104172 37.80518485897756
        // >>> Member: 'station:2', distance: 0.8047, position: -122.26745992898941 37.80623423353753
        // >>> Member: 'station:3', distance: 2.6596, position: -122.24698394536972 37.81040384984464
```

##### Go

```go
	res4, err := rdb.GeoSearch(ctx, "bikes:rentable",
		&redis.GeoSearchQuery{
			Longitude:  -122.27652,
			Latitude:   37.805186,
			Radius:     5,
			RadiusUnit: "km",
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4) // >>> [station:1 station:2 station:3]
```

##### Java (Synchronous - Jedis)

```java
      List<GeoRadiusResponse> res4 = jedis.geosearch(
          "bikes:rentable",
          new GeoCoordinate(-122.27652, 37.805186),
          5,
          GeoUnit.KM
      );
      List<String> members = res4.stream() //
          .map(GeoRadiusResponse::getMemberByString) //
          .collect(Collectors.toList());
      System.out.println(members); // [station:1, station:2, station:3]
```

##### JavaScript (Node.js)

```javascript
const res4 = await client.geoSearch(
  'bikes:rentable', {
    longitude: -122.27652,
    latitude: 37.805186,
  },
  { radius: 5,
    unit: 'km'
  }
);
console.log(res4)  // ['station:1', 'station:2', 'station:3']
```

##### Python

```python
res4 = r.geosearch(
    "bikes:rentable",
    longitude=-122.27652,
    latitude=37.805186,
    radius=5,
    unit="km",
)
print(res4)  # >>> ['station:1', 'station:2', 'station:3']
```



## Learn more

* [Redis Geospatial Explained](https://www.youtube.com/watch?v=qftiVQraxmI) introduces geospatial indexes by showing you how to build a map of local park attractions.
* [Redis University's RU101](https://university.redis.com/courses/ru101/) covers Redis geospatial indexes in detail.

