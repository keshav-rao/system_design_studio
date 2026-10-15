# Pipelines and transactions

```json metadata
{
  "schema_version": 2,
  "title": "Pipelines and transactions",
  "description": "Learn how to use Redis pipelines and transactions",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"execute-a-pipeline","title":"Execute a pipeline"},{"id":"execute-a-transaction","title":"Execute a transaction"},{"id":"watch-keys-for-changes","title":"Watch keys for changes"}]}

,
  "codeExamples": [{"codetabsId":"pipe_trans_tutorial-stepbasic_pipe","description":"Foundational: Use pipelined to batch multiple commands together and reduce network round trips","difficulty":"beginner","id":"basic_pipe","languages":[{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_pipe_trans_tutorial-stepbasic_pipe"}]},{"codetabsId":"pipe_trans_tutorial-stepbasic_trans","description":"Foundational: Use multi to execute multiple commands atomically without interruption from other clients","difficulty":"beginner","id":"basic_trans","languages":[{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_pipe_trans_tutorial-stepbasic_trans"}]},{"codetabsId":"pipe_trans_tutorial-steptrans_watch","description":"Optimistic locking: Use watch with multi and retry when another client modifies the watched key","difficulty":"intermediate","id":"trans_watch","languages":[{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_pipe_trans_tutorial-steptrans_watch"}]}]
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


Redis lets you send a sequence of commands to the server together in a batch.
There are two types of batch that you can use:

-   **Pipelines** avoid network and processing overhead by sending several commands
    to the server together in a single communication. The server then sends back
    a single communication with all the responses. See the
    [Pipelining](https://redis.io/docs/latest/develop/using-commands/pipelining) page for more
    information.
-   **Transactions** guarantee that all the included commands will execute
    to completion without being interrupted by commands from other clients.
    See the [Transactions](https://redis.io/docs/latest/develop/using-commands/transactions)
    page for more information.

## Execute a pipeline

To execute commands in a pipeline with `redis-rb`, call `pipelined()` and queue
commands in the block. Redis executes them as a batch and `pipelined()` returns
the results in order:

Foundational: Use pipelined to batch multiple commands together and reduce network round trips

**Difficulty:** Beginner

**Available in:** Ruby

##### Ruby

```ruby
r.pipelined do |pipe|
  (0..4).each { |i| pipe.set("seat:#{i}", "##{i}") }
end

seats = r.pipelined do |pipe|
  pipe.get('seat:0')
  pipe.get('seat:3')
  pipe.get('seat:4')
end

puts seats[0] # >>> #0
puts seats[1] # >>> #3
puts seats[2] # >>> #4
```



## Execute a transaction

Transactions use `multi()`. Commands queued inside the block run atomically
when the block finishes, and `multi()` returns the results in order:

Foundational: Use multi to execute multiple commands atomically without interruption from other clients

**Difficulty:** Beginner

**Available in:** Ruby

##### Ruby

```ruby
trans_results = r.multi do |tx|
  tx.incrby('counter:1', 1)
  tx.incrby('counter:2', 2)
  tx.incrby('counter:3', 3)
end

puts trans_results[0] # >>> 1
puts trans_results[1] # >>> 2
puts trans_results[2] # >>> 3
```



## Watch keys for changes

Redis supports *optimistic locking* to avoid inconsistent updates to keys that
several clients may modify at the same time. The basic idea is to watch for
changes to any keys that you use in a transaction while you are preparing the
update. If the watched keys do change, the transaction returns `nil` and you
must retry using the latest value from Redis. See
[Transactions](https://redis.io/docs/latest/develop/using-commands/transactions)
for more information about optimistic locking.

The example below watches a key, reads its current value, and then updates it
inside `multi()`:

Optimistic locking: Use watch with multi and retry when another client modifies the watched key

**Difficulty:** Intermediate

**Available in:** Ruby

##### Ruby

```ruby
r.set('shellpath', '/usr/syscmds/')

# Watch the key, read its current value, then queue the update in a
# transaction. `multi` returns `nil` if the watched key changed before
# `EXEC` ran, in which case you would retry with the latest value.
result = r.watch('shellpath') do |client|
  current_path = client.get('shellpath')
  new_path = current_path + ':/usr/mycmds/'

  client.multi do |tx|
    tx.set('shellpath', new_path)
  end
end

if result.nil?
  puts 'Transaction aborted; retry with the latest value'
else
  puts r.get('shellpath')
  # >>> /usr/syscmds/:/usr/mycmds/
end
```



