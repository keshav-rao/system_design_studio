# redis-rb guide (Ruby)

```json metadata
{
  "schema_version": 2,
  "title": "redis-rb guide (Ruby)",
  "description": "Connect your Ruby application to a Redis database",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"install","title":"Install"},{"id":"connect-and-test","title":"Connect and test"},{"id":"more-information","title":"More information"}]}

,
  "codeExamples": []
}
```


[redis-rb](https://github.com/redis/redis-rb) is the Ruby client for Redis.
The sections below explain how to install `redis-rb` and connect your application
to a Redis database.

`redis-rb` requires a running Redis server. See [here](https://redis.io/docs/latest/operate/oss_and_stack/install) for Redis Open Source installation instructions.

## Install

To install `redis-rb`, run the following command:

```bash
gem install redis
```

## Connect and test

Connect to localhost on port 6379:

Foundational: Connect to a Redis server and establish a client connection

```ruby
require 'redis'
r = Redis.new
```



> [!NOTE]
> redis-rb supports [connection URLs](https://redis.io/docs/latest/develop/clients/connection-urls#redis-rb-ruby) through the `url` option of `Redis.new`.
> A URL can set the host, port, credentials, database, and whether to use TLS,
> so you can use one instead of passing those options separately.

Store and retrieve a simple string.

Foundational: Set and retrieve string values using SET and GET commands

```ruby
r.set 'foo', 'bar'
value = r.get('foo')
puts value
```



Store and retrieve a dict.

Foundational: Store and retrieve hash data structures using HSET and HGETALL

```ruby
r.hset 'user-session:123', 'name', 'John'
r.hset 'user-session:123', 'surname', 'Smith'
r.hset 'user-session:123', 'company', 'Redis'
r.hset 'user-session:123', 'age', 29

hash_value = r.hgetall('user-session:123')
puts hash_value
```



Close the connection when you're done.

Foundational: Properly close a Redis client connection to release resources

```ruby
r.close()
```



To connect to a cluster, through Redis Sentinel, or over TLS, see
[Connect to the server](https://redis.io/docs/latest/develop/clients/ruby/connect).

## More information

The
[GitHub repository](https://github.com/redis/redis-rb) for `redis-rb` has a
set of [examples](https://github.com/redis/redis-rb/tree/master/examples)
and further information about using redis-rb.

