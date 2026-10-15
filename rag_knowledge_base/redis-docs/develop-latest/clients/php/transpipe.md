# Pipelines and transactions

```json metadata
{
  "schema_version": 2,
  "title": "Pipelines and transactions",
  "description": "Learn how to use Redis pipelines and transactions",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "scope": "example",
  "tableOfContents": {"sections":[{"id":"execute-a-pipeline","title":"Execute a pipeline"},{"id":"execute-a-transaction","title":"Execute a transaction"},{"id":"watch-keys-for-changes","title":"Watch keys for changes"}]}

,
  "codeExamples": [{"codetabsId":"pipe_trans_tutorial-stepbasic_pipe","description":"Foundational: Use pipelines to batch multiple commands together and reduce network round trips","difficulty":"beginner","id":"basic_pipe","languages":[{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_pipe_trans_tutorial-stepbasic_pipe"}]},{"codetabsId":"pipe_trans_tutorial-stepbasic_trans","description":"Basic transaction: Execute commands atomically using transaction() to group related writes","difficulty":"beginner","id":"basic_trans","languages":[{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_pipe_trans_tutorial-stepbasic_trans"}]},{"codetabsId":"pipe_trans_tutorial-steptrans_watch","description":"Optimistic locking: Use WATCH with a CAS transaction to retry updates when another client modifies the key","difficulty":"intermediate","id":"trans_watch","languages":[{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_pipe_trans_tutorial-steptrans_watch"}]}]
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

To execute commands in a pipeline, create a pipeline object with
[`pipeline()`](https://github.com/predis/predis) and then add commands to it
using methods that resemble the standard command methods (for example,
`set()` and `get()`). The commands are buffered in the pipeline and only
execute when you call the `execute()` method on the pipeline object. This
method returns an array containing the results from all the commands in order.

The command methods for a pipeline always return the original pipeline object,
so you can chain several commands together. You can also pass a callback to
`pipeline()` and let Predis execute the batch automatically when the callback
returns, as the example below shows:

Foundational: Use pipelines to batch multiple commands together and reduce network round trips

**Difficulty:** Beginner

**Available in:** PHP

##### PHP

```php
$pipe = $r->pipeline();
$pipe->set('seat:0', '#0')
    ->set('seat:1', '#1')
    ->set('seat:2', '#2')
    ->set('seat:3', '#3')
    ->set('seat:4', '#4');
$pipe->execute();

$pipe = $r->pipeline();
$pipe->get('seat:0')
    ->get('seat:1')
    ->get('seat:2')
    ->get('seat:3')
    ->get('seat:4');
$seats = $pipe->execute();

echo implode(', ', $seats), PHP_EOL;
// >>> #0, #1, #2, #3, #4

$responses = $r->pipeline(function ($pipe) {
    $pipe->set('seat:5', '#5');
    $pipe->set('seat:6', '#6');
    $pipe->set('seat:7', '#7');
    $pipe->get('seat:5');
    $pipe->get('seat:6');
    $pipe->get('seat:7');
});

echo implode(', ', array_slice($responses, 3)), PHP_EOL;
// >>> #5, #6, #7
```



## Execute a transaction

A transaction works in a similar way to a pipeline, but all the queued commands
execute atomically. With Predis, you can create a transaction by calling
`transaction()` and adding commands in a callback. Predis wraps those commands
with `MULTI` and `EXEC` automatically:

Basic transaction: Execute commands atomically using transaction() to group related writes

**Difficulty:** Beginner

**Available in:** PHP

##### PHP

```php
$r->transaction(function (MultiExec $tx) {
    $tx->incr('counter:1');
    $tx->incrby('counter:2', 2);
    $tx->incrby('counter:3', 3);
});

echo implode(', ', $r->mget('counter:1', 'counter:2', 'counter:3')), PHP_EOL;
// >>> 1, 2, 3
```



## Watch keys for changes

Redis supports *optimistic locking* to avoid inconsistent updates to keys that
several clients may modify at the same time. The basic idea is to watch for
changes to any keys that you use in a transaction while you are preparing the
update. If the watched keys do change, you must restart the update using the
latest value from Redis. See
[Transactions](https://redis.io/docs/latest/develop/using-commands/transactions)
for more information about optimistic locking.

The example below reads a string that represents a `PATH` variable for a
command shell, appends a new command path, and then writes it back inside a
transaction. The `cas` option enables check-and-set behavior, `watch` tells
Predis which key to monitor for changes, and `retry` lets Predis retry the
transaction automatically if another client changes the watched key before
`EXEC` runs:

Optimistic locking: Use WATCH with a CAS transaction to retry updates when another client modifies the key

**Difficulty:** Intermediate

**Available in:** PHP

##### PHP

```php
$r->set('shellpath', '/usr/syscmds/');

$r->transaction(
    ['cas' => true, 'watch' => 'shellpath', 'retry' => 3],
    function (MultiExec $tx) {
        $path = $tx->get('shellpath');
        $tx->multi();
        $tx->set('shellpath', $path . ':/usr/mycmds/');
    }
);

echo $r->get('shellpath'), PHP_EOL;
// >>> /usr/syscmds/:/usr/mycmds/
```



