# Pipelines and transactions

```json metadata
{
  "schema_version": 2,
  "title": "Pipelines and transactions",
  "description": "Learn how to use Redis pipelines and transactions",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"execute-a-pipeline","title":"Execute a pipeline"},{"id":"execute-a-transaction","title":"Execute a transaction"},{"id":"watch-keys-for-changes","title":"Watch keys for changes"}]}

,
  "codeExamples": [{"codetabsId":"pipe_trans_tutorial-stepbasic_pipe","description":"Basic pipeline: Execute multiple commands in a single batch using Pipeline and Exec","difficulty":"beginner","id":"basic_pipe","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_pipe_trans_tutorial-stepbasic_pipe"}]},{"codetabsId":"pipe_trans_tutorial-stepbasic_pipe_pipelined","description":"Pipeline with callback: Use Pipelined method for automatic execution of batched commands","difficulty":"beginner","id":"basic_pipe_pipelined","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_pipe_trans_tutorial-stepbasic_pipe_pipelined"}]},{"codetabsId":"pipe_trans_tutorial-stepbasic_trans","description":"Basic transaction: Execute commands atomically using TxPipeline to ensure consistency","difficulty":"beginner","id":"basic_trans","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_pipe_trans_tutorial-stepbasic_trans"}]},{"codetabsId":"pipe_trans_tutorial-stepbasic_trans_txpipelined","description":"Transaction with callback: Use TxPipelined for automatic atomic execution with callback syntax","difficulty":"beginner","id":"basic_trans_txpipelined","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_pipe_trans_tutorial-stepbasic_trans_txpipelined"}]},{"codetabsId":"pipe_trans_tutorial-steptrans_watch","description":"Optimistic locking: Watch keys for changes and retry transactions when watched keys are modified","difficulty":"advanced","id":"trans_watch","languages":[{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_pipe_trans_tutorial-steptrans_watch"}]}]
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

If you want the client to batch concurrent commands into pipelines for you
without writing any pipeline code, see
[Automatic pipelining](https://redis.io/docs/latest/develop/clients/go/autopipeline).

Both types of batch run on a separate pool of connections that the client keeps
for them, so a burst of batches doesn't compete with your ordinary commands for
the same connections. See
[Connection pooling](https://redis.io/docs/latest/develop/clients/go/produsage#connection-pooling)
for how to size that pool.

## Execute a pipeline

To execute commands in a pipeline, you first create a pipeline object
and then add commands to it using methods that resemble the standard
command methods (for example, `Set()` and `Get()`). The commands are
buffered in the pipeline and only execute when you call the `Exec()`
method on the pipeline object.

The main difference with the pipeline commands is that their return
values contain a valid result only after the pipeline has finished executing.
You can access the result using the `Val()` method instead of
`Result()` (note that errors are reported by the `Exec()` method rather
than by the individual commands).

Basic pipeline: Execute multiple commands in a single batch using Pipeline and Exec

**Difficulty:** Beginner

**Available in:** Go

##### Go

```go
	pipe := rdb.Pipeline()

	for i := 0; i < 5; i++ {
		pipe.Set(ctx, fmt.Sprintf("seat:%v", i), fmt.Sprintf("#%v", i), 0)
	}

	cmds, err := pipe.Exec(ctx)

	if err != nil {
		panic(err)
	}

	for _, c := range cmds {
		fmt.Printf("%v;", c.(*redis.StatusCmd).Val())
	}

	fmt.Println("")
	// >>> OK;OK;OK;OK;OK;

	pipe = rdb.Pipeline()

	get0Result := pipe.Get(ctx, "seat:0")
	get3Result := pipe.Get(ctx, "seat:3")
	get4Result := pipe.Get(ctx, "seat:4")

	cmds, err = pipe.Exec(ctx)

	// The results are available only after the pipeline
	// has finished executing.
	fmt.Println(get0Result.Val()) // >>> #0
	fmt.Println(get3Result.Val()) // >>> #3
	fmt.Println(get4Result.Val()) // >>> #4
```



You can also create a pipeline using the `Pipelined()` method.
This executes pipeline commands in a callback function that you
provide and calls `Exec()` automatically after it returns:

Pipeline with callback: Use Pipelined method for automatic execution of batched commands

**Difficulty:** Beginner

**Available in:** Go

##### Go

```go
	var pd0Result *redis.StatusCmd
	var pd3Result *redis.StatusCmd
	var pd4Result *redis.StatusCmd

	cmds, err = rdb.Pipelined(ctx, func(pipe redis.Pipeliner) error {
		pd0Result = (*redis.StatusCmd)(pipe.Get(ctx, "seat:0"))
		pd3Result = (*redis.StatusCmd)(pipe.Get(ctx, "seat:3"))
		pd4Result = (*redis.StatusCmd)(pipe.Get(ctx, "seat:4"))
		return nil
	})

	if err != nil {
		panic(err)
	}

	// The results are available only after the pipeline
	// has finished executing.
	fmt.Println(pd0Result.Val()) // >>> #0
	fmt.Println(pd3Result.Val()) // >>> #3
	fmt.Println(pd4Result.Val()) // >>> #4
```



## Execute a transaction

A transaction works in a similar way to a pipeline. Create a
transaction object with the `TxPipeline()` method, call command methods
on that object, and then call the transaction object's
`Exec()` method to execute it. You can access the results
from commands in the transaction after it completes using the
`Val()` method.

Basic transaction: Execute commands atomically using TxPipeline to ensure consistency

**Difficulty:** Beginner

**Available in:** Go

##### Go

```go
	trans := rdb.TxPipeline()

	trans.IncrBy(ctx, "counter:1", 1)
	trans.IncrBy(ctx, "counter:2", 2)
	trans.IncrBy(ctx, "counter:3", 3)

	cmds, err = trans.Exec(ctx)

	for _, c := range cmds {
		fmt.Println(c.(*redis.IntCmd).Val())
	}
	// >>> 1
	// >>> 2
	// >>> 3
```



There is also a `TxPipelined()` method that works in a similar way
to `Pipelined()`, described above:

Transaction with callback: Use TxPipelined for automatic atomic execution with callback syntax

**Difficulty:** Beginner

**Available in:** Go

##### Go

```go
	var tx1Result *redis.IntCmd
	var tx2Result *redis.IntCmd
	var tx3Result *redis.IntCmd

	cmds, err = rdb.TxPipelined(ctx, func(trans redis.Pipeliner) error {
		tx1Result = trans.IncrBy(ctx, "counter:1", 1)
		tx2Result = trans.IncrBy(ctx, "counter:2", 2)
		tx3Result = trans.IncrBy(ctx, "counter:3", 3)
		return nil
	})

	if err != nil {
		panic(err)
	}

	fmt.Println(tx1Result.Val()) // >>> 2
	fmt.Println(tx2Result.Val()) // >>> 4
	fmt.Println(tx3Result.Val()) // >>> 6
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
The `Watch()` method receives a callback function where you execute the
commands you want to watch. In the body of this callback, you can execute
read-only commands before the transaction using the usual client object
(called `rdb` in our examples) and receive an immediate result. Start the
transaction itself by calling `TxPipeline()` or `TxPipelined()` on the
`Tx` object passed to the callback. `Watch()` also receives one or more
`string` parameters after the callback that represent the keys you want
to watch.

For production usage, you would generally call code like the following in
a loop to retry it until it succeeds or else report or log the failure:

Optimistic locking: Watch keys for changes and retry transactions when watched keys are modified

**Difficulty:** Advanced

**Available in:** Go

##### Go

```go
	// Set initial value of `shellpath`.
	rdb.Set(ctx, "shellpath", "/usr/syscmds/", 0)

	const maxRetries = 1000

	// Retry if the key has been changed.
	for i := 0; i < maxRetries; i++ {
		err := rdb.Watch(ctx,
			func(tx *redis.Tx) error {
				currentPath, err := rdb.Get(ctx, "shellpath").Result()
				newPath := currentPath + ":/usr/mycmds/"

				_, err = tx.TxPipelined(ctx, func(pipe redis.Pipeliner) error {
					pipe.Set(ctx, "shellpath", newPath, 0)
					return nil
				})

				return err
			},
			"shellpath",
		)

		if err == nil {
			// Success.
			break
		} else if err == redis.TxFailedErr {
			// Optimistic lock lost. Retry the transaction.
			continue
		} else {
			// Panic for any other error.
			panic(err)
		}
	}

	fmt.Println(rdb.Get(ctx, "shellpath").Val())
	// >>> /usr/syscmds/:/usr/mycmds/
```



