# Pipelines and transactions

```json metadata
{
  "schema_version": 2,
  "title": "Pipelines and transactions",
  "description": "Learn how to use Redis pipelines and transactions",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"execute-a-pipeline","title":"Execute a pipeline"},{"id":"execute-a-transaction","title":"Execute a transaction"},{"id":"watch-keys-for-changes","title":"Watch keys for changes"}]}

,
  "codeExamples": [{"codetabsId":"pipe_trans_tutorial-stepbasic_pipe","description":"Foundational: Use pipelines to batch multiple commands together and reduce network round trips","difficulty":"beginner","id":"basic_pipe","languages":[{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_pipe_trans_tutorial-stepbasic_pipe"}]},{"codetabsId":"pipe_trans_tutorial-stepbasic_trans","description":"Foundational: Use transactions to execute multiple commands atomically without interruption from other clients","difficulty":"beginner","id":"basic_trans","languages":[{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_pipe_trans_tutorial-stepbasic_trans"}]},{"codetabsId":"pipe_trans_tutorial-steptrans_watch","description":"Optimistic locking: Use WATCH to monitor keys for changes and retry transactions when conflicts occur","difficulty":"intermediate","id":"trans_watch","languages":[{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_pipe_trans_tutorial-steptrans_watch"}]}]
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

To execute commands in a pipeline, you first create a pipeline object
and then add commands to it using methods that resemble the standard
command methods (for example, `set()` and `get()`). The commands are
buffered in the pipeline and only execute when you call the `sync()`
method on the pipeline object.

The main difference with the pipeline commands is that they return
`Response<Type>` objects, where `Type` is the return type of the
standard command method. A `Response` object contains a valid result
only after the pipeline has finished executing. You can access the
result using the `Response` object's `get()` method.

Foundational: Use pipelines to batch multiple commands together and reduce network round trips

**Difficulty:** Beginner

**Available in:** Java (Synchronous - Jedis)

##### Java (Synchronous - Jedis)

```java
        // Make sure you close the pipeline after use to release resources
        // and return the connection to the pool.
        try (AbstractPipeline pipe = jedis.pipelined()) {

            for (int i = 0; i < 5; i++) {
                pipe.set(String.format("seat:%d", i), String.format("#%d", i));
            }

            pipe.sync();
        }

        try (AbstractPipeline pipe = jedis.pipelined()) {

            Response<String> resp0 = pipe.get("seat:0");
            Response<String> resp3 = pipe.get("seat:3");
            Response<String> resp4 = pipe.get("seat:4");

            pipe.sync();

            // Responses are available after the pipeline has executed.
            System.out.println(resp0.get()); // >>> #0
            System.out.println(resp3.get()); // >>> #3
            System.out.println(resp4.get()); // >>> #4


        }
```



## Execute a transaction

A transaction works in a similar way to a pipeline. Create a
transaction object with the `multi()` command, call command methods
on that object, and then call the transaction object's
`exec()` method to execute it. You can access the results
from commands in the transaction using `Response` objects, as
you would with a pipeline. However, the `exec()` method also
returns a `List<Object>` value that contains all the result
values in the order the commands were executed (see
[Watch keys for changes](#watch-keys-for-changes) below for
an example that uses the results list).

Foundational: Use transactions to execute multiple commands atomically without interruption from other clients

**Difficulty:** Beginner

**Available in:** Java (Synchronous - Jedis)

##### Java (Synchronous - Jedis)

```java
        try ( AbstractTransaction trans = jedis.multi()) {

           trans.incrBy("counter:1", 1);
           trans.incrBy("counter:2", 2);
           trans.incrBy("counter:3", 3);

           trans.exec();
        }
        System.out.println(jedis.get("counter:1")); // >>> 1
        System.out.println(jedis.get("counter:2")); // >>> 2
        System.out.println(jedis.get("counter:3")); // >>> 3
```



## Watch keys for changes

Redis supports *optimistic locking* to avoid inconsistent updates
to different keys. The basic idea is to watch for changes to any
keys that you use in a transaction while you are processing the
updates. If the watched keys do change, you must restart the updates
with the latest data from the keys. See
[Transactions](https://redis.io/docs/latest/develop/using-commands/transactions)
for more information about optimistic locking.

The code below reads a string
that represents a `PATH` variable for a command shell, then appends a new
command path to the string before attempting to write it back. If the watched
key is modified by another client before writing, the transaction aborts.
Note that you should call read-only commands for the watched keys synchronously on
the usual client object (called `jedis` in our examples) but you still call commands
for the transaction on the transaction object.

For production usage, you would generally call code like the following in
a loop to retry it until it succeeds or else report or log the failure.

Optimistic locking: Use WATCH to monitor keys for changes and retry transactions when conflicts occur

**Difficulty:** Intermediate

**Available in:** Java (Synchronous - Jedis)

##### Java (Synchronous - Jedis)

```java
        // Set initial value of `shellpath`.
        jedis.set("shellpath", "/usr/syscmds/");

        // Start the transaction and watch the key we are about to update.
        try (AbstractTransaction trans = jedis.transaction(false)) { // create a Transaction object without sending MULTI command
            trans.watch("shellpath"); // send WATCH command(s)
            trans.multi(); // send MULTI command

            String currentPath = jedis.get("shellpath");
            String newPath = currentPath + ":/usr/mycmds/";

            // Commands added to the `trans` object
            // will be buffered until `trans.exec()` is called.
            Response<String> setResult = trans.set("shellpath", newPath);
            List<Object> transResults = trans.exec();

            // The `exec()` call returns null if the transaction failed.
            if (transResults != null) {
                // Responses are available if the transaction succeeded.
                System.out.println(setResult.get()); // >>> OK

                // You can also get the results from the list returned by
                // `trans.exec()`.
                for (Object item: transResults) {
                    System.out.println(item);
                }
                // >>> OK

                System.out.println(jedis.get("shellpath"));
                // >>> /usr/syscmds/:/usr/mycmds/
            }
        }
```



