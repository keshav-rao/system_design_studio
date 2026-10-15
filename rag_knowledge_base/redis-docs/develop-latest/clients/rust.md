# redis-rs guide (Rust)

```json metadata
{
  "schema_version": 2,
  "title": "redis-rs guide (Rust)",
  "description": "Connect your Rust application to a Redis database",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"install","title":"Install"},{"id":"connect","title":"Connect"},{"id":"more-information","title":"More information"}]}

,
  "codeExamples": [{"codetabsId":"landing-stepimport","description":"Foundational: Import the Commands trait to access Redis command methods","difficulty":"beginner","id":"import","languages":[{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_landing-stepimport"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_landing-stepimport"}]},{"codetabsId":"landing-stepconnect","description":"Foundational: Connect to a Redis server and establish a client connection","difficulty":"beginner","id":"connect","languages":[{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_landing-stepconnect"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_landing-stepconnect"}]},{"codetabsId":"landing-stepset_get_string","description":"Foundational: Set and retrieve string values using SET and GET commands","difficulty":"beginner","id":"set_get_string","languages":[{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_landing-stepset_get_string"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_landing-stepset_get_string"}]},{"codetabsId":"landing-stepset_get_hash","description":"Foundational: Store and retrieve hash data structures using HSET and HGETALL","difficulty":"beginner","id":"set_get_hash","languages":[{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_landing-stepset_get_hash"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_landing-stepset_get_hash"}]}]
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


[`redis-rs`](https://github.com/redis-rs/redis-rs) is the [Rust](https://www.rust-lang.org/) client for Redis.
The sections below explain how to install `redis-rs` and connect your application to a Redis database.

> [!NOTE]
> Although we provide basic documentation for `redis-rs`, it is a third-party
> client library and is not developed or supported directly by Redis.

`redis-rs` requires a running Redis server. See [here](https://redis.io/docs/latest/operate/oss_and_stack/install) for Redis Open Source installation instructions.

## Install

To use the synchronous API, add the `redis` crate as a dependency in your
`Cargo.toml` file:

```toml
[dependencies]
redis = "1.0.4"
```

If you want to use the asynchronous API, you should also enable either
[`tokio`](https://tokio.rs/) or [`smol`](https://crates.io/crates/smol)
as your async platform:

```toml
[dependencies]
# if you use tokio
tokio = { version = "1.32.0", features = ["full"] }
redis = { version = "1.0.4", features = ["tokio-comp"] }

# if you use smol
smol = "2.0.2"
redis = { version = "1.0.4", features = ["smol-comp"] }
```

## Connect

Start by importing the `Commands` or `AsyncCommands` trait from the `redis` crate:

Foundational: Import the Commands trait to access Redis command methods

**Difficulty:** Beginner

**Available in:** Rust (Asynchronous), Rust (Synchronous)

##### Rust (Asynchronous)

```rust
    use redis::AsyncCommands;
```

##### Rust (Synchronous)

```rust
    use redis::Commands;
```



The following example shows the simplest way to connect to a Redis server:

Foundational: Connect to a Redis server and establish a client connection

**Difficulty:** Beginner

**Available in:** Rust (Asynchronous), Rust (Synchronous)

##### Rust (Asynchronous)

```rust
        let mut r = match redis::Client::open("redis://127.0.0.1") {
            Ok(client) => {
                match client.get_multiplexed_async_connection().await {
                    Ok(conn) => conn,
                    Err(e) => {
                        println!("Failed to connect to Redis: {e}");
                        return;
                    }
                }
            },
            Err(e) => {
                println!("Failed to create Redis client: {e}");
                return;
            }
        };
```

##### Rust (Synchronous)

```rust
        let mut r = match redis::Client::open("redis://127.0.0.1") {
            Ok(client) => {
                match client.get_connection() {
                    Ok(conn) => conn,
                    Err(e) => {
                        println!("Failed to connect to Redis: {e}");
                        return;
                    }
                }
            },
            Err(e) => {
                println!("Failed to create Redis client: {e}");
                return;
            }
        };
```



> [!NOTE]
> redis-rs supports [connection URLs](https://redis.io/docs/latest/develop/clients/connection-urls#redis-rs-rust) through `Client::open()`.
> A URL can set the host, port, credentials, database, and whether to use TLS,
> so you can use one instead of passing those options separately.

After connecting, you can test the connection by  storing and retrieving
a simple [string](https://redis.io/docs/latest/develop/data-types/strings):

Foundational: Set and retrieve string values using SET and GET commands

**Difficulty:** Beginner

**Available in:** Rust (Asynchronous), Rust (Synchronous)

##### Rust (Asynchronous)

```rust
        if let Ok(res) = r.set("foo", "bar").await {
            let res: String = res;
            println!("{res}"); // >>> OK
        } else {
            println!("Error setting foo");
        }

        match r.get("foo").await {
            Ok(res) => {
                let res: String = res;
                println!("{res}"); // >>> bar
            },
            Err(e) => {
                println!("Error getting foo: {e}");
                return;
            }
        };
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.set("foo", "bar") {
            let res: String = res;
            println!("{res}");    // >>> OK
        } else {
            println!("Error setting foo");
        }
        
        match r.get("foo") {
            Ok(res) => {
                let res: String = res;
                println!("{res}");   // >>> bar
            },
            Err(e) => {
                println!("Error getting foo: {e}");
                return;
            }
        };
```



You can also easily store and retrieve a [hash](https://redis.io/docs/latest/develop/data-types/hashes):

Foundational: Store and retrieve hash data structures using HSET and HGETALL

**Difficulty:** Beginner

**Available in:** Rust (Asynchronous), Rust (Synchronous)

##### Rust (Asynchronous)

```rust
        let hash_fields = [
            ("model", "Deimos"),
            ("brand", "Ergonom"),
            ("type", "Enduro bikes"),
            ("price", "4972"),
        ];

        if let Ok(res) = r.hset_multiple("bike:1", &hash_fields).await {
            let res: String = res;
            println!("{res}"); // >>> OK
        } else {
            println!("Error setting bike:1");
        }

        match r.hget("bike:1", "model").await {
            Ok(res) => {
                let res: String = res;
                println!("{res}"); // >>> Deimos
            },
            Err(e) => {
                println!("Error getting bike:1 model: {e}");
                return;
            }
        }

        match r.hget("bike:1", "price").await {
            Ok(res) => {
                let res: String = res;
                println!("{res}"); // >>> 4972
            },
            Err(e) => {
                println!("Error getting bike:1 price: {e}");
                return;
            }
        }

        match r.hgetall("bike:1").await {
            Ok(res) => {
                let res: Vec<(String, String)> = res;

                for (key, value) in res {
                    println!("{key}: {value}");
                }
                // >>> model: Deimos
                // >>> brand: Ergonom
                // >>> type: Enduro bikes
                // >>> price: 4972
            },
            Err(e) => {
                println!("Error getting bike:1: {e}");
                return;
            }
```

##### Rust (Synchronous)

```rust
        let hash_fields = [
            ("model", "Deimos"),
            ("brand", "Ergonom"),
            ("type", "Enduro bikes"),
            ("price", "4972"),
        ];
    
        if let Ok(res) = r.hset_multiple("bike:1", &hash_fields) {
            let res: String = res;
            println!("{res}"); // >>> OK
        } else {
            println!("Error setting bike:1");
        }
    
        match r.hget("bike:1", "model") {
            Ok(res) => {
                let res: String = res;
                println!("{res}"); // >>> Deimos
            },
            Err(e) => {
                println!("Error getting bike:1 model: {e}");
                return;
            }   
        }
    
        match r.hget("bike:1", "price") {
            Ok(res) => {
                let res: String = res;
                println!("{res}"); // >>> 4972
            },
            Err(e) => {
                println!("Error getting bike:1 price: {e}");
                return;
            }   
        }
    
        match r.hgetall("bike:1") {
            Ok(res) => {
                let res: Vec<(String, String)> = res;
                
                for (key, value) in res {
                    println!("{key}: {value}");
                }
                // >>> model: Deimos
                // >>> brand: Ergonom
                // >>> type: Enduro bikes
                // >>> price: 4972
            },
            Err(e) => {
                println!("Error getting bike:1: {e}");
                return;
            }   
        }
```



To connect to a cluster, through Redis Sentinel, or over TLS, see
[Connect to the server](https://redis.io/docs/latest/develop/clients/rust/connect).

## More information

See the [`redis-rs`](https://docs.rs/redis/latest/redis/) documentation
and the [GitHub repository](https://github.com/redis-rs/redis-rs) for more
information and examples.

