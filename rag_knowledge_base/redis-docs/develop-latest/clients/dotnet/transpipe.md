# Pipelines and transactions

```json metadata
{
  "schema_version": 2,
  "title": "Pipelines and transactions",
  "description": "Learn how to use Redis pipelines and transactions",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"execute-a-pipeline","title":"Execute a pipeline"},{"id":"execute-a-transaction","title":"Execute a transaction"},{"id":"watch-keys-for-changes","title":"Watch keys for changes"}]}

,
  "codeExamples": [{"codetabsId":"pipe_trans_tutorial-stepbasic_pipe","description":"Foundational: Use pipelines to batch multiple commands together and reduce network round trips","difficulty":"beginner","id":"basic_pipe","languages":[{"id":"dotnet-Async (SE-Redis)","panelId":"panel_Csharp-Async (SERedis)_pipe_trans_tutorial-stepbasic_pipe"}]},{"codetabsId":"pipe_trans_tutorial-stepbasic_trans","description":"Foundational: Use transactions to execute multiple commands atomically without interruption from other clients","difficulty":"beginner","id":"basic_trans","languages":[{"id":"dotnet-Async (SE-Redis)","panelId":"panel_Csharp-Async (SERedis)_pipe_trans_tutorial-stepbasic_trans"}]},{"codetabsId":"pipe_trans_tutorial-steptrans_watch","description":"Optimistic locking: Use conditions to monitor keys for changes and abort transactions when conflicts occur","difficulty":"intermediate","id":"trans_watch","languages":[{"id":"dotnet-Async (SE-Redis)","panelId":"panel_Csharp-Async (SERedis)_pipe_trans_tutorial-steptrans_watch"}]}]
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

`StackExchange.Redis` pipelines commands by using its asynchronous command
methods. Start the operations without waiting for each one immediately, then
wait for their tasks after you have queued the commands. The multiplexer sends
the requests as soon as possible and processes the responses when they arrive.
See the StackExchange.Redis
[Pipelines and Multiplexers](https://seredis.dev/PipelinesMultiplexers.html)
page for more information.

Foundational: Use pipelines to batch multiple commands together and reduce network round trips

**Difficulty:** Beginner

**Available in:** C#

##### C#

```csharp
        var setTasks = new[]
        {
            db.StringSetAsync("seat:0", "#0"),
            db.StringSetAsync("seat:1", "#1"),
            db.StringSetAsync("seat:2", "#2"),
            db.StringSetAsync("seat:3", "#3"),
            db.StringSetAsync("seat:4", "#4")
        };
        foreach (var setTask in setTasks)
        {
            db.Wait(setTask);
        }

        var resp1Task = db.StringGetAsync("seat:0");
        var resp2Task = db.StringGetAsync("seat:3");
        var resp3Task = db.StringGetAsync("seat:4");

        var resp1 = db.Wait(resp1Task);
        Console.WriteLine(resp1); // >>> #0

        var resp2 = db.Wait(resp2Task);
        Console.WriteLine(resp2); // >>> #3

        var resp3 = db.Wait(resp3Task);
        Console.WriteLine(resp3); // >>> #4
```



## Execute a transaction

A transaction queues commands on an `ITransaction` object that you create with
`CreateTransaction()`. Call async command methods on that object, then call
`Execute()` or `ExecuteAsync()` to attempt the transaction. The queued command
tasks complete after the transaction executes.

Foundational: Use transactions to execute multiple commands atomically without interruption from other clients

**Difficulty:** Beginner

**Available in:** C#

##### C#

```csharp
        var trans = db.CreateTransaction();

        var incr1 = trans.StringIncrementAsync("counter:1", 1);
        var incr2 = trans.StringIncrementAsync("counter:2", 2);
        var incr3 = trans.StringIncrementAsync("counter:3", 3);

        bool committed = db.Wait(trans.ExecuteAsync());

        var resp4 = db.Wait(incr1);
        Console.WriteLine(resp4); // >>> 1

        var resp5 = db.Wait(incr2);
        Console.WriteLine(resp5); // >>> 2

        var resp6 = db.Wait(incr3);
        Console.WriteLine(resp6);  // >>> 3
```



## Watch keys for changes

Redis supports *optimistic locking* to avoid inconsistent updates
to different keys. The basic idea is to watch for changes to any
keys that you use in a transaction while you are processing the
updates. If the watched keys do change, you must restart the updates
with the latest data from the keys. See
[Transactions](https://redis.io/docs/latest/develop/using-commands/transactions)
for more information about optimistic locking.

The approach to optimistic locking that other clients use
(adding the [`WATCH`](https://redis.io/docs/latest/commands/watch) command
explicitly to a transaction) doesn't work well with the
[multiplexing](https://redis.io/docs/latest/develop/clients/pools-and-muxing)
system that `StackExchange.Redis` uses.
Instead, `StackExchange.Redis` relies on conditional execution of commands
to get a similar effect.

Use the `AddCondition()` method to abort a transaction if a particular
condition doesn't hold throughout its execution. If the transaction
does abort then the `Execute()` method returns a `false` value,
but otherwise returns `true`.

For example, the `KeyNotExists` condition aborts the transaction
if a specified key exists or is added by another client while the
transaction executes:

Optimistic locking: Use conditions to monitor keys for changes and abort transactions when conflicts occur

**Difficulty:** Intermediate

**Available in:** C#

##### C#

```csharp
        var watchedTrans = db.CreateTransaction();

        watchedTrans.AddCondition(Condition.KeyNotExists("customer:39182"));

        var hashSetTask = watchedTrans.HashSetAsync(
            "customer:39182",
            [
                new("name", "David"),
                new("age", "27")
            ]
        );

        bool succeeded = db.Wait(watchedTrans.ExecuteAsync());
        db.Wait(hashSetTask);
        Console.WriteLine(succeeded); // >>> true
```



You can also use a `When` condition on certain individual commands to
specify that they only execute when a certain condition holds
(for example, the command does not change an existing key).
See
[Conditional execution](https://redis.io/docs/latest/develop/clients/dotnet/condexec)
for a full description of transaction and command conditions.

