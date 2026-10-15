# Index and query documents

```json metadata
{
  "schema_version": 2,
  "title": "Index and query documents",
  "description": "Learn how to use Redis Search with JSON and hash documents.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "topics": ["Redis Search","JSON","hash"],
  "relatedPages": ["/develop/clients/nodejs/vecsearch","/develop/ai/search-and-query"],
  "scope": "example",
  "tableOfContents": {"sections":[{"id":"initialize","title":"Initialize"},{"id":"create-data","title":"Create data"},{"id":"add-the-index","title":"Add the index"},{"id":"add-the-data","title":"Add the data"},{"id":"query-the-data","title":"Query the data"},{"id":"differences-with-hash-documents","title":"Differences with hash documents"},{"id":"more-information","title":"More information"}]}

,
  "codeExamples": [{"codetabsId":"js_home_query-stepimport","description":"Foundational: Import required modules for Redis client and query operations","difficulty":"beginner","id":"import","languages":[{"id":"Node-js","panelId":"panel_Nodejs_js_home_query-stepimport"}]},{"codetabsId":"js_home_query-stepcreate_data","description":"Foundational: Define sample data structures for indexing and querying examples","difficulty":"beginner","id":"create_data","languages":[{"id":"Node-js","panelId":"panel_Nodejs_js_home_query-stepcreate_data"}]},{"codetabsId":"js_home_query-stepconnect","description":"Foundational: Establish a connection to Redis for query operations","difficulty":"beginner","id":"connect","languages":[{"id":"Node-js","panelId":"panel_Nodejs_js_home_query-stepconnect"}]},{"codetabsId":"js_home_query-stepcleanup_json","description":"Foundational: Drop an existing search index safely using error handling to avoid collisions","difficulty":"intermediate","id":"cleanup_json","languages":[{"id":"Node-js","panelId":"panel_Nodejs_js_home_query-stepcleanup_json"}]},{"codetabsId":"js_home_query-stepcreate_index","description":"Foundational: Create a search index for JSON documents with field definitions and aliases","difficulty":"intermediate","id":"create_index","languages":[{"id":"Node-js","panelId":"panel_Nodejs_js_home_query-stepcreate_index"}]},{"codetabsId":"js_home_query-stepadd_data","description":"Foundational: Add JSON documents with indexed key prefixes using Promise.all() for efficient pipelining","difficulty":"intermediate","id":"add_data","languages":[{"id":"Node-js","panelId":"panel_Nodejs_js_home_query-stepadd_data"}]},{"codetabsId":"js_home_query-stepquery1","description":"Query data: Execute a full-text search combined with numeric range filtering on indexed JSON documents","difficulty":"intermediate","id":"query1","languages":[{"id":"Node-js","panelId":"panel_Nodejs_js_home_query-stepquery1"}]},{"codetabsId":"js_home_query-stepquery2","description":"Restrict query results: Project specific fields in query results to reduce data transfer and improve performance","difficulty":"intermediate","id":"query2","languages":[{"id":"Node-js","panelId":"panel_Nodejs_js_home_query-stepquery2"}]},{"codetabsId":"js_home_query-stepquery3","description":"Aggregate query results: Use aggregation queries to group and count results by field values for analytics","difficulty":"advanced","id":"query3","languages":[{"id":"Node-js","panelId":"panel_Nodejs_js_home_query-stepquery3"}]},{"codetabsId":"js_home_query-stepcleanup_hash","description":"Foundational: Drop an existing search index safely using error handling to avoid collisions","difficulty":"intermediate","id":"cleanup_hash","languages":[{"id":"Node-js","panelId":"panel_Nodejs_js_home_query-stepcleanup_hash"}]},{"codetabsId":"js_home_query-stepcreate_hash_index","description":"Foundational: Create a search index for hash documents with HASH type specification","difficulty":"intermediate","id":"create_hash_index","languages":[{"id":"Node-js","panelId":"panel_Nodejs_js_home_query-stepcreate_hash_index"}]},{"codetabsId":"js_home_query-stepadd_hash_data","description":"Foundational: Add hash documents with indexed key prefixes using hSet() for automatic indexing","difficulty":"intermediate","id":"add_hash_data","languages":[{"id":"Node-js","panelId":"panel_Nodejs_js_home_query-stepadd_hash_data"}]},{"codetabsId":"js_home_query-stepquery1_hash","description":"Query data: Execute the same full-text query pattern on hash documents as on JSON documents","difficulty":"intermediate","id":"query1_hash","languages":[{"id":"Node-js","panelId":"panel_Nodejs_js_home_query-stepquery1_hash"}]}]
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


This example shows how to create a
[search index](https://redis.io/docs/latest/develop/ai/search-and-query/indexing)
for [JSON](https://redis.io/docs/latest/develop/data-types/json) documents and
run queries against the index. It then goes on to show the slight differences
in the equivalent code for [hash](https://redis.io/docs/latest/develop/data-types/hashes)
documents.

> [!NOTE]
> From [v5.0.0](https://github.com/redis/node-redis/releases/tag/redis%405.0.0)
> onwards, `node-redis` uses query dialect 2 by default.
> Redis Search methods such as [`ft.search()`](https://redis.io/docs/latest/commands/ft.search)
> will explicitly request this dialect, overriding the default set for the server.
> See
> [Query dialects](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/dialects)
> for more information.

## Initialize

Make sure that you have [Redis Open Source](https://redis.io/docs/latest/operate/oss_and_stack)
or another Redis server available. Also install the
[`node-redis`](https://redis.io/docs/latest/develop/clients/nodejs) client library if you
haven't already done so.

Add the following dependencies:

Foundational: Import required modules for Redis client and query operations

**Difficulty:** Beginner

**Available in:** JavaScript (Node.js)

##### JavaScript (Node.js)

```javascript
import {
    createClient,
    SCHEMA_FIELD_TYPE,
    FT_AGGREGATE_GROUP_BY_REDUCERS,
    FT_AGGREGATE_STEPS,
} from 'redis';
```



## Create data

Create some test data to add to your database. The example data shown
below is compatible with both JSON and hash objects.

Foundational: Define sample data structures for indexing and querying examples

**Difficulty:** Beginner

**Available in:** JavaScript (Node.js)

##### JavaScript (Node.js)

```javascript
const user1 = {
    name: 'Paul John',
    email: 'paul.john@example.com',
    age: 42,
    city: 'London'
};

const user2 = {
    name: 'Eden Zamir',
    email: 'eden.zamir@example.com',
    age: 29,
    city: 'Tel Aviv'
};

const user3 = {
    name: 'Paul Zamir',
    email: 'paul.zamir@example.com',
    age: 35,
    city: 'Tel Aviv'
};
```



## Add the index

Connect to your Redis database. The code below shows the most
basic connection but see
[Connect to the server](https://redis.io/docs/latest/develop/clients/nodejs/connect)
to learn more about the available connection options.

Foundational: Establish a connection to Redis for query operations

**Difficulty:** Beginner

**Available in:** JavaScript (Node.js)

##### JavaScript (Node.js)

```javascript
const client = await createClient();
await client.connect();
```



Create an index. In this example, only JSON documents with the key prefix `user:` are indexed. For more information, see [Query syntax](https://redis.io/docs/latest/develop/ai/search-and-query/query).

First, drop any existing index to avoid a collision. (The callback is required
to avoid an error if the index doesn't already exist.)

Foundational: Drop an existing search index safely using error handling to avoid collisions

**Difficulty:** Intermediate

**Available in:** JavaScript (Node.js)

##### JavaScript (Node.js)

```javascript
await client.ft.dropIndex('idx:users', { DD: true }).then(() => {}, () => {});
```



Then create the index:

Foundational: Create a search index for JSON documents with field definitions and aliases

**Difficulty:** Intermediate

**Available in:** JavaScript (Node.js)

##### JavaScript (Node.js)

```javascript
await client.ft.create('idx:users', {
    '$.name': {
        type: SCHEMA_FIELD_TYPE.TEXT,
        AS: 'name'
    },
    '$.city': {
        type: SCHEMA_FIELD_TYPE.TEXT,
        AS: 'city'
    },
    '$.age': {
        type: SCHEMA_FIELD_TYPE.NUMERIC,
        AS: 'age'
    }
}, {
    ON: 'JSON',
    PREFIX: 'user:'
});
```



## Add the data

Add the three sets of user data to the database as
[JSON](https://redis.io/docs/latest/develop/data-types/json) objects.
If you use keys with the `user:` prefix then Redis will index the
objects automatically as you add them. Note that placing
the commands in a `Promise.all()` call is an easy way to create a
[pipeline](https://redis.io/docs/latest/develop/clients/nodejs/transpipe),
which is more efficient than sending the commands individually.

Foundational: Add JSON documents with indexed key prefixes using Promise.all() for efficient pipelining

**Difficulty:** Intermediate

**Available in:** JavaScript (Node.js)

##### JavaScript (Node.js)

```javascript
const [user1Reply, user2Reply, user3Reply] = await Promise.all([
    client.json.set('user:1', '$', user1),
    client.json.set('user:2', '$', user2),
    client.json.set('user:3', '$', user3)
]);
```



## Query the data

You can now use the index to search the JSON objects. The
[query](https://redis.io/docs/latest/develop/ai/search-and-query/query)
below searches for objects that have the text "Paul" in any field
and have an `age` value in the range 30 to 40:

Query data: Execute a full-text search combined with numeric range filtering on indexed JSON documents

**Difficulty:** Intermediate

**Available in:** JavaScript (Node.js)

##### JavaScript (Node.js)

```javascript
let findPaulResult = await client.ft.search('idx:users', 'Paul @age:[30 40]');

console.log(findPaulResult.total); // >>> 1

findPaulResult.documents.forEach(doc => {
    console.log(`ID: ${doc.id}, name: ${doc.value.name}, age: ${doc.value.age}`);
});
// >>> ID: user:3, name: Paul Zamir, age: 35
```



Specify query options to return only the `city` field:

Restrict query results: Project specific fields in query results to reduce data transfer and improve performance

**Difficulty:** Intermediate

**Available in:** JavaScript (Node.js)

##### JavaScript (Node.js)

```javascript
let citiesResult = await client.ft.search('idx:users', '*',{
    RETURN: 'city'
});

console.log(citiesResult.total); // >>> 3

citiesResult.documents.forEach(cityDoc => {
    console.log(cityDoc.value);
});
// >>> { city: 'London' }
// >>> { city: 'Tel Aviv' }
// >>> { city: 'Tel Aviv' }
```



Use an
[aggregation query](https://redis.io/docs/latest/develop/ai/search-and-query/query/aggregation)
to count all users in each city.

Aggregate query results: Use aggregation queries to group and count results by field values for analytics

**Difficulty:** Advanced

**Available in:** JavaScript (Node.js)

##### JavaScript (Node.js)

```javascript
let aggResult = await client.ft.aggregate('idx:users', '*', {
    STEPS: [{
        type: FT_AGGREGATE_STEPS.GROUPBY,
        properties: '@city',
        REDUCE: [{
            type: FT_AGGREGATE_GROUP_BY_REDUCERS.COUNT,
            AS: 'count'
        }]
    }]
});

console.log(aggResult.total); // >>> 2

aggResult.results.forEach(result => {
    console.log(`${result.city} - ${result.count}`);
});
// >>> London - 1
// >>> Tel Aviv - 2
```



## Differences with hash documents

Indexing for hash documents is very similar to JSON indexing but you
need to specify some slightly different options.

When you create the schema for a hash index, you don't need to
add aliases for the fields, since you use the basic names to access
the fields anyway. Also, you must use `HASH` for the `ON` option
when you create the index. The code below shows these changes with
a new index called `hash-idx:users`, which is otherwise the same as
the `idx:users` index used for JSON documents in the previous examples.

First, drop any existing index to avoid a collision.

Foundational: Drop an existing search index safely using error handling to avoid collisions

**Difficulty:** Intermediate

**Available in:** JavaScript (Node.js)

##### JavaScript (Node.js)

```javascript
await client.ft.dropIndex('hash-idx:users', { DD: true }).then(() => {}, () => {});
```



Then create the new index:

Foundational: Create a search index for hash documents with HASH type specification

**Difficulty:** Intermediate

**Available in:** JavaScript (Node.js)

##### JavaScript (Node.js)

```javascript
await client.ft.create('hash-idx:users', {
    'name': {
        type: SCHEMA_FIELD_TYPE.TEXT
    },
    'city': {
        type: SCHEMA_FIELD_TYPE.TEXT
    },
    'age': {
        type: SCHEMA_FIELD_TYPE.NUMERIC
    }
}, {
    ON: 'HASH',
    PREFIX: 'huser:'
});
```



You use [`hSet()`](https://redis.io/docs/latest/commands/hset) to add the hash
documents instead of [`json.set()`](https://redis.io/docs/latest/commands/json.set),
but the same flat `userX` objects work equally well with either
hash or JSON:

Foundational: Add hash documents with indexed key prefixes using hSet() for automatic indexing

**Difficulty:** Intermediate

**Available in:** JavaScript (Node.js)

##### JavaScript (Node.js)

```javascript
const [huser1Reply, huser2Reply, huser3Reply] = await Promise.all([
    client.hSet('huser:1', user1),
    client.hSet('huser:2', user2),
    client.hSet('huser:3', user3)
]);
```



The query commands work the same here for hash as they do for JSON (but
the name of the hash index is different). The format of the result is
also the same:

Query data: Execute the same full-text query pattern on hash documents as on JSON documents

**Difficulty:** Intermediate

**Available in:** JavaScript (Node.js)

##### JavaScript (Node.js)

```javascript
let findPaulHashResult = await client.ft.search(
    'hash-idx:users', 'Paul @age:[30 40]'
);

console.log(findPaulHashResult.total); // >>> 1

findPaulHashResult.documents.forEach(doc => {
    console.log(`ID: ${doc.id}, name: ${doc.value.name}, age: ${doc.value.age}`);
});
// >>> ID: huser:3, name: Paul Zamir, age: 35
```



## More information

See the [Redis Search](https://redis.io/docs/latest/develop/ai/search-and-query) docs
for a full description of all query features with examples.

