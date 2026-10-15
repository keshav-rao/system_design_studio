# Index and query documents

```json metadata
{
  "schema_version": 2,
  "title": "Index and query documents",
  "description": "Learn how to use Redis Search with JSON and hash documents.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "topics": ["Redis Search","JSON","hash"],
  "relatedPages": ["/develop/ai/search-and-query"],
  "scope": "example",
  "tableOfContents": {"sections":[{"id":"initialize","title":"Initialize"},{"id":"create-data","title":"Create data"},{"id":"add-the-index","title":"Add the index"},{"id":"add-the-data","title":"Add the data"},{"id":"query-the-data","title":"Query the data"},{"id":"differences-with-hash-documents","title":"Differences with hash documents"},{"id":"more-information","title":"More information"}]}

,
  "codeExamples": [{"codetabsId":"ruby_home_json-stepimport","description":"Foundational: Require the redis gem and alias the Query Engine namespace","difficulty":"beginner","id":"import","languages":[{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_ruby_home_json-stepimport"}]},{"codetabsId":"ruby_home_json-stepcreate_data","description":"Foundational: Define sample user data structures for indexing and querying","difficulty":"beginner","id":"create_data","languages":[{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_ruby_home_json-stepcreate_data"}]},{"codetabsId":"ruby_home_json-stepconnect","description":"Foundational: Establish a connection to a Redis server for query operations","difficulty":"beginner","id":"connect","languages":[{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_ruby_home_json-stepconnect"}]},{"codetabsId":"ruby_home_json-stepcleanup_json","description":"Foundational: Clean up existing indexes and data before creating new indexes","difficulty":"beginner","id":"cleanup_json","languages":[{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_ruby_home_json-stepcleanup_json"}]},{"codetabsId":"ruby_home_json-stepmake_index","description":"Foundational: Create a search index for JSON documents with field definitions and key prefix filtering","difficulty":"intermediate","id":"make_index","languages":[{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_ruby_home_json-stepmake_index"}]},{"codetabsId":"ruby_home_json-stepadd_data","description":"Foundational: Store JSON documents in Redis with automatic indexing based on key prefix","difficulty":"beginner","id":"add_data","languages":[{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_ruby_home_json-stepadd_data"}]},{"codetabsId":"ruby_home_json-stepquery1","description":"Query with filters: Search JSON documents using text matching and numeric range filters to find specific records","difficulty":"intermediate","id":"query1","languages":[{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_ruby_home_json-stepquery1"}]},{"codetabsId":"ruby_home_json-stepquery2","description":"Query with field projection: Retrieve only specific fields from search results to reduce data transfer","difficulty":"intermediate","id":"query2","languages":[{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_ruby_home_json-stepquery2"}]},{"codetabsId":"ruby_home_json-stepquery3","description":"Aggregation query: Group and count results by field values to analyze data patterns","difficulty":"intermediate","id":"query3","languages":[{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_ruby_home_json-stepquery3"}]},{"codetabsId":"ruby_home_json-stepcleanup_hash","description":"Foundational: Clean up existing hash indexes and data before creating new indexes","difficulty":"beginner","id":"cleanup_hash","languages":[{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_ruby_home_json-stepcleanup_hash"}]},{"codetabsId":"ruby_home_json-stepmake_hash_index","description":"Foundational: Create a search index for hash documents with field definitions and key prefix filtering","difficulty":"intermediate","id":"make_hash_index","languages":[{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_ruby_home_json-stepmake_hash_index"}]},{"codetabsId":"ruby_home_json-stepadd_hash_data","description":"Foundational: Store hash documents in Redis with automatic indexing based on key prefix","difficulty":"beginner","id":"add_hash_data","languages":[{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_ruby_home_json-stepadd_hash_data"}]},{"codetabsId":"ruby_home_json-stepquery1_hash","description":"Query with filters: Search hash documents using text matching and numeric range filters (same as JSON queries)","difficulty":"intermediate","id":"query1_hash","languages":[{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_ruby_home_json-stepquery1_hash"}]}]
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

Make sure that you have [Redis Open Source](https://redis.io/docs/latest/operate/oss_and_stack)
or another Redis server available. Also install the
[`redis-rb`](https://redis.io/docs/latest/develop/clients/ruby) client library if you
haven't already done so.

Require the `redis` gem. The Query Engine classes live under the
`Redis::Commands::Search` namespace, so the example below aliases it to
`Search` to keep the code concise.

Foundational: Require the redis gem and alias the Query Engine namespace

**Difficulty:** Beginner

**Available in:** Ruby

##### Ruby

```ruby
require 'redis'

# A short alias for the Query Engine namespace to keep the code below readable.
Search = Redis::Commands::Search
```



## Create data

Create some test data to add to the database:

Foundational: Define sample user data structures for indexing and querying

**Difficulty:** Beginner

**Available in:** Ruby

##### Ruby

```ruby
user1 = {
  'name' => 'Paul John',
  'email' => 'paul.john@example.com',
  'age' => 42,
  'city' => 'London'
}

user2 = {
  'name' => 'Eden Zamir',
  'email' => 'eden.zamir@example.com',
  'age' => 29,
  'city' => 'Tel Aviv'
}

user3 = {
  'name' => 'Paul Zamir',
  'email' => 'paul.zamir@example.com',
  'age' => 35,
  'city' => 'Tel Aviv'
}
```



## Add the index

Connect to your Redis database. The code below shows the most
basic connection but see the
[`redis-rb` guide](https://redis.io/docs/latest/develop/clients/ruby)
to learn more about the available connection options.

Foundational: Establish a connection to a Redis server for query operations

**Difficulty:** Beginner

**Available in:** Ruby

##### Ruby

```ruby
r = Redis.new
```



Delete any existing index called `idx:users` and any keys that start with `user:`.

Foundational: Clean up existing indexes and data before creating new indexes

**Difficulty:** Beginner

**Available in:** Ruby

##### Ruby

```ruby
begin
  r.ft_dropindex('idx:users', delete_documents: true)
rescue Redis::CommandError
  # Index doesn't exist, so there is nothing to drop.
end

r.del('user:1', 'user:2', 'user:3')
```



Create an index. In this example, only JSON documents with the key prefix `user:` are indexed. For more information, see [Query syntax](https://redis.io/docs/latest/develop/ai/search-and-query/query).

Build the schema with the field type helpers (`text_field`, `tag_field`,
`numeric_field`) inside a `Search::Schema.build` block. Each field's first
argument is the [JSON path](https://redis.io/docs/latest/develop/data-types/json/path) to
the value, and the `as:` option gives the field an alias you can refer to in
queries.

Foundational: Create a search index for JSON documents with field definitions and key prefix filtering

**Difficulty:** Intermediate

**Available in:** Ruby

##### Ruby

```ruby
schema = Search::Schema.build do
  text_field '$.name', as: 'name'
  tag_field '$.city', as: 'city'
  numeric_field '$.age', as: 'age'
end

definition = Search::IndexDefinition.new(
  prefix: ['user:'],
  index_type: Search::IndexType::JSON
)

index = r.create_index('idx:users', schema, definition: definition)
puts index.name # >>> idx:users
```



## Add the data

Add the three sets of user data to the database as
[JSON](https://redis.io/docs/latest/develop/data-types/json) objects.
If you use keys with the `user:` prefix then Redis will index the
objects automatically as you add them:

Foundational: Store JSON documents in Redis with automatic indexing based on key prefix

**Difficulty:** Beginner

**Available in:** Ruby

##### Ruby

```ruby
user1_set = r.json_set('user:1', '$', user1)
user2_set = r.json_set('user:2', '$', user2)
user3_set = r.json_set('user:3', '$', user3)
puts [user1_set, user2_set, user3_set].inspect # >>> ["OK", "OK", "OK"]
```



## Query the data

You can now use the index to search the JSON objects. The
[query](https://redis.io/docs/latest/develop/ai/search-and-query/query)
below searches for objects that have the text "Paul" in any field
and have an `age` value in the range 30 to 40:

Query with filters: Search JSON documents using text matching and numeric range filters to find specific records

**Difficulty:** Intermediate

**Available in:** Ruby

##### Ruby

```ruby
find_paul_result = index.search('Paul @age:[30 40]')

puts find_paul_result.total # >>> 1
# The index has the key prefix `user:`, so the client returns the
# logical document id with that prefix removed.
find_paul_result.each { |doc| puts doc.id } # >>> 3
```



Because the index has the key prefix `user:`, the client strips that prefix
from the returned document IDs and reports the logical ID (for example, `3`
rather than `user:3`).

Use a `Search::Query` object to specify query options, such as returning only
the `city` field:

Query with field projection: Retrieve only specific fields from search results to reduce data transfer

**Difficulty:** Intermediate

**Available in:** Ruby

##### Ruby

```ruby
cities_query = Search::Query.new('Paul').return_field('$.city', as_field: 'city')
cities_result = index.search(cities_query)

cities_result.documents.sort_by(&:id).each do |doc|
  puts "#{doc.id}: #{doc['city']}"
end
# >>> 1: London
# >>> 3: Tel Aviv
```



Use an
[aggregation query](https://redis.io/docs/latest/develop/ai/search-and-query/query/aggregation)
to count all users in each city.

Aggregation query: Group and count results by field values to analyze data patterns

**Difficulty:** Intermediate

**Available in:** Ruby

##### Ruby

```ruby
request = Search::AggregateRequest.new('*')
                                  .group_by('@city', Search::Reducers.count.as('count'))

agg_result = index.aggregate(request)

agg_result.rows.sort_by { |row| row['city'] }.each do |row|
  puts "#{row['city']} - #{row['count']}"
end
# >>> London - 1
# >>> Tel Aviv - 2
```



## Differences with hash documents

Indexing for hash documents is very similar to JSON indexing but you
need to specify some slightly different options.

When you create the schema for a hash index, you don't need to
add aliases for the fields, since you use the basic names to access
the fields anyway. Also, you must use `Search::IndexType::HASH` for the
`index_type:` option of the `IndexDefinition` when you create the index. The code
below shows these changes with a new index called `hash-idx:users`, which is
otherwise the same as the `idx:users` index used for JSON documents in the
previous examples.

First, delete any existing index called `hash-idx:users` and any keys that start with `huser:`.

Foundational: Clean up existing hash indexes and data before creating new indexes

**Difficulty:** Beginner

**Available in:** Ruby

##### Ruby

```ruby
begin
  r.ft_dropindex('hash-idx:users', delete_documents: true)
rescue Redis::CommandError
  # Index doesn't exist, so there is nothing to drop.
end

r.del('huser:1', 'huser:2', 'huser:3')
```



Now create the new index:

Foundational: Create a search index for hash documents with field definitions and key prefix filtering

**Difficulty:** Intermediate

**Available in:** Ruby

##### Ruby

```ruby
hash_schema = Search::Schema.build do
  text_field 'name'
  tag_field 'city'
  numeric_field 'age'
end

hash_definition = Search::IndexDefinition.new(
  prefix: ['huser:'],
  index_type: Search::IndexType::HASH
)

hash_index = r.create_index('hash-idx:users', hash_schema, definition: hash_definition)
puts hash_index.name # >>> hash-idx:users
```



Use [`hset()`](https://redis.io/docs/latest/commands/hset) to add the hash
documents instead of [`json_set()`](https://redis.io/docs/latest/commands/json.set).

Foundational: Store hash documents in Redis with automatic indexing based on key prefix

**Difficulty:** Beginner

**Available in:** Ruby

##### Ruby

```ruby
huser1_set = r.hset('huser:1', user1)
huser2_set = r.hset('huser:2', user2)
huser3_set = r.hset('huser:3', user3)
puts [huser1_set, huser2_set, huser3_set].inspect # >>> [4, 4, 4]
```



The query commands work the same here for hash as they do for JSON (but
the name of the hash index is different). The results are returned as
`Document` objects, as with JSON:

Query with filters: Search hash documents using text matching and numeric range filters (same as JSON queries)

**Difficulty:** Intermediate

**Available in:** Ruby

##### Ruby

```ruby
find_paul_hash_result = hash_index.search('Paul @age:[30 40]')

puts find_paul_hash_result.total # >>> 1
find_paul_hash_result.each do |doc|
  puts "#{doc.id}: #{doc['name']}, #{doc['city']}"
end
# >>> 3: Paul Zamir, Tel Aviv
```



## More information

See the [Redis Search](https://redis.io/docs/latest/develop/ai/search-and-query) docs
for a full description of all query features with examples.

