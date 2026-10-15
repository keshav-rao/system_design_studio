# Pipelines and transactions

```json metadata
{
  "schema_version": 2,
  "title": "Pipelines and transactions",
  "description": "Learn how to use Redis pipelines and transactions",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"execute-a-pipeline","title":"Execute a pipeline"},{"id":"execute-a-transaction","title":"Execute a transaction"},{"id":"watch-keys-for-changes","title":"Watch keys for changes"}]}

,
  "codeExamples": [{"codetabsId":"pipe_trans_tutorial-stepbasic_pipe","description":"Foundational: Batch multiple Lettuce commands and flush them to the server together","difficulty":"beginner","id":"basic_pipe","languages":[{"clientId":"lettuce","clientName":"Lettuce","id":"Lettuce-Sync","langId":"java","panelId":"panel_Lettuce-Sync_pipe_trans_tutorial-stepbasic_pipe"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_pipe_trans_tutorial-stepbasic_pipe"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_pipe_trans_tutorial-stepbasic_pipe"}]},{"codetabsId":"pipe_trans_tutorial-stepbasic_trans","description":"Foundational: Use MULTI and EXEC with Lettuce to execute multiple commands atomically","difficulty":"beginner","id":"basic_trans","languages":[{"clientId":"lettuce","clientName":"Lettuce","id":"Lettuce-Sync","langId":"java","panelId":"panel_Lettuce-Sync_pipe_trans_tutorial-stepbasic_trans"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_pipe_trans_tutorial-stepbasic_trans"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_pipe_trans_tutorial-stepbasic_trans"}]},{"codetabsId":"pipe_trans_tutorial-steptrans_watch","description":"Optimistic locking: Use WATCH with EXEC and check whether Lettuce discarded the transaction","difficulty":"intermediate","id":"trans_watch","languages":[{"clientId":"lettuce","clientName":"Lettuce","id":"Lettuce-Sync","langId":"java","panelId":"panel_Lettuce-Sync_pipe_trans_tutorial-steptrans_watch"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_pipe_trans_tutorial-steptrans_watch"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_pipe_trans_tutorial-steptrans_watch"}]}]
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

With Lettuce, you pipeline commands by buffering them on the client and then
flushing them to the server together. The synchronous and asynchronous APIs do
this by temporarily disabling auto-flushing with `setAutoFlushCommands()` and
then calling `flushCommands()`; each buffered command returns a `RedisFuture`
that you can inspect after the batch is flushed. The reactive API pipelines
commands by composing the corresponding `Mono` and `Flux` publishers:

Foundational: Batch multiple Lettuce commands and flush them to the server together

**Difficulty:** Beginner

**Available in:** Java, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce)

##### Java

```java
            // Lettuce pipelines commands by buffering them on the client while
            // auto-flushing is disabled. Use the asynchronous API to obtain a
            // `RedisFuture` for each buffered command, then read the results
            // after the batch has been flushed to the server.
            RedisAsyncCommands<String, String> async = connection.async();
            connection.setAutoFlushCommands(false);

            for (int i = 0; i < 5; i++) {
                async.set("seat:" + i, "#" + i);
            }

            RedisFuture<String> seat0 = async.get("seat:0");
            RedisFuture<String> seat3 = async.get("seat:3");
            RedisFuture<String> seat4 = async.get("seat:4");

            connection.flushCommands();
            connection.setAutoFlushCommands(true);

            System.out.println(seat0.get()); // >>> #0
            System.out.println(seat3.get()); // >>> #3
            System.out.println(seat4.get()); // >>> #4
```

##### Java (Asynchronous - Lettuce)

```java
            // Disable auto-flushing to buffer the commands on the client, then
            // flush them to the server as a single batch. Each command returns
            // a `RedisFuture` that completes when its response arrives.
            connection.setAutoFlushCommands(false);

            for (int i = 0; i < 5; i++) {
                async.set("seat:" + i, "#" + i);
            }

            RedisFuture<String> seat0 = async.get("seat:0");
            RedisFuture<String> seat3 = async.get("seat:3");
            RedisFuture<String> seat4 = async.get("seat:4");

            connection.flushCommands();
            connection.setAutoFlushCommands(true);

            System.out.println(seat0.get()); // >>> #0
            System.out.println(seat3.get()); // >>> #3
            System.out.println(seat4.get()); // >>> #4
```

##### Java (Reactive - Lettuce)

```java
            // Reactive commands are pipelined automatically: the writes below are
            // sent to the server back to back, then the reads are sent as a batch
            // once you subscribe (here, by calling `block()`).
            List<String> seats = Flux.range(0, 5)
                    .flatMap(i -> reactive.set("seat:" + i, "#" + i))
                    .thenMany(Flux.just("seat:0", "seat:3", "seat:4")
                            .flatMapSequential(reactive::get))
                    .collectList()
                    .block();

            System.out.println(seats.get(0)); // >>> #0
            System.out.println(seats.get(1)); // >>> #3
            System.out.println(seats.get(2)); // >>> #4
```



## Execute a transaction

Lettuce transactions use the Redis `MULTI` and `EXEC` commands. Commands issued
between `multi()` and `exec()` are queued on the server and only run when
`exec()` completes. The return value from `exec()` is a `TransactionResult`
that contains the results in order:

Foundational: Use MULTI and EXEC with Lettuce to execute multiple commands atomically

**Difficulty:** Beginner

**Available in:** Java, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce)

##### Java

```java
            commands.multi();

            commands.incrby("counter:1", 1);
            commands.incrby("counter:2", 2);
            commands.incrby("counter:3", 3);

            TransactionResult transResult = commands.exec();

            System.out.println((Long) transResult.get(0)); // >>> 1
            System.out.println((Long) transResult.get(1)); // >>> 2
            System.out.println((Long) transResult.get(2)); // >>> 3
```

##### Java (Asynchronous - Lettuce)

```java
            // Commands issued between `multi()` and `exec()` are queued on the
            // server. Their futures only complete when `exec()` runs.
            async.multi();

            RedisFuture<Long> counter1 = async.incrby("counter:1", 1);
            RedisFuture<Long> counter2 = async.incrby("counter:2", 2);
            RedisFuture<Long> counter3 = async.incrby("counter:3", 3);

            RedisFuture<TransactionResult> execResult = async.exec();
            execResult.get();

            System.out.println(counter1.get()); // >>> 1
            System.out.println(counter2.get()); // >>> 2
            System.out.println(counter3.get()); // >>> 3
```

##### Java (Reactive - Lettuce)

```java
            // Queue the commands between `multi()` and `exec()`. Subscribing to
            // each one inside the `multi()` callback sends it to the server, where
            // it is held until `exec()` runs the transaction.
            TransactionResult transResult = reactive.multi()
                    .flatMap(ok -> {
                        reactive.incrby("counter:1", 1).subscribe();
                        reactive.incrby("counter:2", 2).subscribe();
                        reactive.incrby("counter:3", 3).subscribe();
                        return reactive.exec();
                    })
                    .block();

            System.out.println((Long) transResult.get(0)); // >>> 1
            System.out.println((Long) transResult.get(1)); // >>> 2
            System.out.println((Long) transResult.get(2)); // >>> 3
```



## Watch keys for changes

Redis supports *optimistic locking* to avoid inconsistent updates to keys that
several clients may modify at the same time. The basic idea is to watch for
changes to any keys that you use in a transaction while you are preparing the
update. If the watched keys do change, Redis discards the transaction and you
must retry using the latest value from Redis. See
[Transactions](https://redis.io/docs/latest/develop/using-commands/transactions)
for more information about optimistic locking.

The example below watches a key, reads its current value, queues an update
inside `MULTI`, and then checks `TransactionResult.wasDiscarded()` after
`EXEC`:

Optimistic locking: Use WATCH with EXEC and check whether Lettuce discarded the transaction

**Difficulty:** Intermediate

**Available in:** Java, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce)

##### Java

```java
            commands.set("shellpath", "/usr/syscmds/");

            // Watch the key for changes while we prepare the update.
            commands.watch("shellpath");

            String currentPath = commands.get("shellpath");
            String newPath = currentPath + ":/usr/mycmds/";

            commands.multi();
            commands.set("shellpath", newPath);

            TransactionResult watchedResult = commands.exec();

            // `exec()` returns an empty result that reports `wasDiscarded()` if
            // the watched key changed before the transaction ran.
            if (!watchedResult.wasDiscarded()) {
                System.out.println(commands.get("shellpath"));
                // >>> /usr/syscmds/:/usr/mycmds/
            }
```

##### Java (Asynchronous - Lettuce)

```java
            async.set("shellpath", "/usr/syscmds/").get();

            // Watch the key for changes while we prepare the update.
            async.watch("shellpath").get();

            String currentPath = async.get("shellpath").get();
            String newPath = currentPath + ":/usr/mycmds/";

            async.multi().get();
            async.set("shellpath", newPath);

            TransactionResult watchedResult = async.exec().get();

            // `exec()` reports `wasDiscarded()` if the watched key changed
            // before the transaction ran.
            if (!watchedResult.wasDiscarded()) {
                System.out.println(async.get("shellpath").get());
                // >>> /usr/syscmds/:/usr/mycmds/
            }
```

##### Java (Reactive - Lettuce)

```java
            reactive.set("shellpath", "/usr/syscmds/").block();

            // Watch the key, read its current value, then queue the update in a
            // transaction. `exec()` reports `wasDiscarded()` if the watched key
            // changed before the transaction ran.
            TransactionResult watchedResult = reactive.watch("shellpath")
                    .then(reactive.get("shellpath"))
                    .flatMap(currentPath -> reactive.multi()
                            .flatMap(ok -> {
                                reactive.set("shellpath", currentPath + ":/usr/mycmds/").subscribe();
                                return reactive.exec();
                            }))
                    .block();

            if (!watchedResult.wasDiscarded()) {
                System.out.println(reactive.get("shellpath").block());
                // >>> /usr/syscmds/:/usr/mycmds/
            }
```



