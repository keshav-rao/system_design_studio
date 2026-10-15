# Work with JSON documents

```json metadata
{
  "schema_version": 2,
  "title": "Work with JSON documents",
  "description": "Learn how to store, read, and update JSON documents with redis-rs.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "topics": ["JSON","Rust"],
  "relatedPages": ["/develop/data-types/json","/develop/data-types/json/path"],
  "scope": "example",
  "tableOfContents": {"sections":[{"id":"install","title":"Install"},{"id":"import-the-required-crates","title":"Import the required crates"},{"id":"create-some-json-data","title":"Create some JSON data"},{"id":"connect-to-redis","title":"Connect to Redis"},{"id":"store-and-retrieve-the-document","title":"Store and retrieve the document"},{"id":"read-nested-fields","title":"Read nested fields"},{"id":"update-part-of-the-document","title":"Update part of the document"},{"id":"append-to-an-array","title":"Append to an array"},{"id":"more-information","title":"More information"}]}

,
  "codeExamples": [{"codetabsId":"rust_home_json-stepimport","description":"Foundational: Import the Redis JSON traits and serde_json helpers needed to work with JSON documents in Rust","difficulty":"beginner","id":"import","languages":[{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_rust_home_json-stepimport"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_rust_home_json-stepimport"}]},{"codetabsId":"rust_home_json-stepcreate_data","description":"Foundational: Define a nested JSON document with objects and arrays using serde_json::json!","difficulty":"beginner","id":"create_data","languages":[{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_rust_home_json-stepcreate_data"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_rust_home_json-stepcreate_data"}]},{"codetabsId":"rust_home_json-stepconnect","description":"Foundational: Create a Redis client and open a sync or async connection from Rust","difficulty":"beginner","id":"connect","languages":[{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_rust_home_json-stepconnect"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_rust_home_json-stepconnect"}]},{"codetabsId":"rust_home_json-stepset_get_doc","description":"Foundational: Store a complete JSON document with JSON.SET and fetch it again with JSON.GET","difficulty":"beginner","id":"set_get_doc","languages":[{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_rust_home_json-stepset_get_doc"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_rust_home_json-stepset_get_doc"}]},{"codetabsId":"rust_home_json-stepget_fields","description":"Read nested data: Use JSON paths to retrieve selected fields and arrays without fetching the whole document","difficulty":"beginner","id":"get_fields","languages":[{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_rust_home_json-stepget_fields"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_rust_home_json-stepget_fields"}]},{"codetabsId":"rust_home_json-stepupdate_fields","description":"Update nested values: Modify individual fields in place with JSON.SET and JSON.NUMINCRBY","difficulty":"intermediate","id":"update_fields","languages":[{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_rust_home_json-stepupdate_fields"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_rust_home_json-stepupdate_fields"}]},{"codetabsId":"rust_home_json-stepupdate_array","description":"Update arrays: Append new elements to a JSON array and read back the updated value","difficulty":"intermediate","id":"update_array","languages":[{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_rust_home_json-stepupdate_array"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_rust_home_json-stepupdate_array"}]}]
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


This example shows how to work with a
[JSON](https://redis.io/docs/latest/develop/data-types/json)
document from Rust using [`redis-rs`](https://redis.io/docs/latest/develop/clients/rust).
It uses one `bike:1` document to demonstrate a simple workflow:
create the document, read nested fields, update part of the document,
and append data to an array.

Unlike some of the other client examples in this section, this page focuses on
Redis JSON commands directly rather than on Redis Search.

## Install

Add `serde_json` and enable the `json` feature for `redis`.
If you want to use the async API, also enable a runtime integration such as `tokio-comp`.

```toml
[dependencies]
serde_json = "1"

# Sync API
redis = { version = "1.0.4", features = ["json"] }

# Async API with Tokio
tokio = { version = "1", features = ["full"] }
redis = { version = "1.0.4", features = ["json", "tokio-comp"] }
```

## Import the required crates

The example uses `serde_json::json!()` to build the document and the
`JsonCommands` or `JsonAsyncCommands` trait to access Redis JSON commands.

Foundational: Import the Redis JSON traits and serde_json helpers needed to work with JSON documents in Rust

**Difficulty:** Beginner

**Available in:** Rust (Asynchronous), Rust (Synchronous)

##### Rust (Asynchronous)

```rust
    use redis::{cmd, AsyncCommands, JsonAsyncCommands};
    use serde_json::json;
```

##### Rust (Synchronous)

```rust
    use redis::{cmd, Commands, JsonCommands};
    use serde_json::json;
```



## Create some JSON data

Create a sample document representing a bike listing.
The nested `specs` and `inventory` objects and the `colors` array let you see how
JSON paths work with more realistic data than a flat object.

Foundational: Define a nested JSON document with objects and arrays using serde_json::json!

**Difficulty:** Beginner

**Available in:** Rust (Asynchronous), Rust (Synchronous)

##### Rust (Asynchronous)

```rust
        let bike = json!({
            "model": "Deimos",
            "brand": "Ergonom",
            "price": 4972,
            "specs": {
                "material": "carbon",
                "weight": 8.7
            },
            "colors": ["black", "silver"],
            "inventory": {
                "in_stock": 12,
                "warehouse": "w1"
            }
        });
```

##### Rust (Synchronous)

```rust
        let bike = json!({
            "model": "Deimos",
            "brand": "Ergonom",
            "price": 4972,
            "specs": {
                "material": "carbon",
                "weight": 8.7
            },
            "colors": ["black", "silver"],
            "inventory": {
                "in_stock": 12,
                "warehouse": "w1"
            }
        });
```



## Connect to Redis

Connect to your Redis server in the usual way.
See [Connect to the server](https://redis.io/docs/latest/develop/clients/rust)
for more connection options.

Foundational: Create a Redis client and open a sync or async connection from Rust

**Difficulty:** Beginner

**Available in:** Rust (Asynchronous), Rust (Synchronous)

##### Rust (Asynchronous)

```rust
        let client =
            redis::Client::open("redis://127.0.0.1").expect("Failed to create Redis client");
        let mut r = client
            .get_multiplexed_async_connection()
            .await
            .expect("Failed to connect to Redis");
```

##### Rust (Synchronous)

```rust
        let client =
            redis::Client::open("redis://127.0.0.1").expect("Failed to create Redis client");
        let mut r = client.get_connection().expect("Failed to connect to Redis");
```



## Store and retrieve the document

Use [`JSON.SET`](https://redis.io/docs/latest/commands/json.set) to store the whole document at the root path `$`.
You can then retrieve the document again with [`JSON.GET`](https://redis.io/docs/latest/commands/json.get).

Foundational: Store a complete JSON document with JSON.SET and fetch it again with JSON.GET

**Difficulty:** Beginner

**Available in:** Rust (Asynchronous), Rust (Synchronous)

##### Rust (Asynchronous)

```rust
        let stored: bool = r
            .json_set("bike:1", "$", &bike)
            .await
            .expect("Failed to run JSON.SET");
        println!("{}", if stored { "OK" } else { "(nil)" }); // >>> OK

        let bike_json: String = r
            .json_get("bike:1", "$")
            .await
            .expect("Failed to run JSON.GET");
        println!("{bike_json}");
        // >>> [{"model":"Deimos","brand":"Ergonom","price":4972,"specs":{"material":"carbon","weight":8.7},"colors":["black","silver"],"inventory":{"in_stock":12,"warehouse":"w1"}}]
```

##### Rust (Synchronous)

```rust
        let stored: bool = r
            .json_set("bike:1", "$", &bike)
            .expect("Failed to run JSON.SET");
        println!("{}", if stored { "OK" } else { "(nil)" }); // >>> OK

        let bike_json: String = r.json_get("bike:1", "$").expect("Failed to run JSON.GET");
        println!("{bike_json}");
        // >>> [{"model":"Deimos","brand":"Ergonom","price":4972,"specs":{"material":"carbon","weight":8.7},"colors":["black","silver"],"inventory":{"in_stock":12,"warehouse":"w1"}}]
```



## Read nested fields

JSON paths let you retrieve only the parts of the document you need.
This is useful when your application only needs a small subset of the data.

Read nested data: Use JSON paths to retrieve selected fields and arrays without fetching the whole document

**Difficulty:** Beginner

**Available in:** Rust (Asynchronous), Rust (Synchronous)

##### Rust (Asynchronous)

```rust
        let material: String = r
            .json_get("bike:1", "$.specs.material")
            .await
            .expect("Failed to run JSON.GET");
        println!("{material}"); // >>> ["carbon"]

        let colors: String = r
            .json_get("bike:1", "$.colors")
            .await
            .expect("Failed to run JSON.GET");
        println!("{colors}"); // >>> [["black","silver"]]

        let stock: String = r
            .json_get("bike:1", "$.inventory.in_stock")
            .await
            .expect("Failed to run JSON.GET");
        println!("{stock}"); // >>> [12]
```

##### Rust (Synchronous)

```rust
        let material: String = r
            .json_get("bike:1", "$.specs.material")
            .expect("Failed to run JSON.GET");
        println!("{material}"); // >>> ["carbon"]

        let colors: String = r
            .json_get("bike:1", "$.colors")
            .expect("Failed to run JSON.GET");
        println!("{colors}"); // >>> [["black","silver"]]

        let stock: String = r
            .json_get("bike:1", "$.inventory.in_stock")
            .expect("Failed to run JSON.GET");
        println!("{stock}"); // >>> [12]
```



## Update part of the document

You can update individual fields without replacing the whole document.
The example below changes the stock count and then applies a price change with
[`JSON.NUMINCRBY`](https://redis.io/docs/latest/commands/json.numincrby).

Update nested values: Modify individual fields in place with JSON.SET and JSON.NUMINCRBY

**Difficulty:** Intermediate

**Available in:** Rust (Asynchronous), Rust (Synchronous)

##### Rust (Asynchronous)

```rust
        let stock_set: bool = r
            .json_set("bike:1", "$.inventory.in_stock", &json!(8))
            .await
            .expect("Failed to update stock");
        println!("{}", if stock_set { "OK" } else { "(nil)" }); // >>> OK

        let new_price: String = cmd("JSON.NUMINCRBY")
            .arg("bike:1")
            .arg("$.price")
            .arg(-500)
            .query_async(&mut r)
            .await
            .expect("Failed to run JSON.NUMINCRBY");
        println!("{new_price}"); // >>> [4472]

        let updated_fields: String = r
            .json_get("bike:1", &["$.price", "$.inventory.in_stock"])
            .await
            .expect("Failed to read updated fields");
        println!("{updated_fields}"); // >>> {"$.price":[4472],"$.inventory.in_stock":[8]}
```

##### Rust (Synchronous)

```rust
        let stock_set: bool = r
            .json_set("bike:1", "$.inventory.in_stock", &json!(8))
            .expect("Failed to update stock");
        println!("{}", if stock_set { "OK" } else { "(nil)" }); // >>> OK

        let new_price: String = cmd("JSON.NUMINCRBY")
            .arg("bike:1")
            .arg("$.price")
            .arg(-500)
            .query(&mut r)
            .expect("Failed to run JSON.NUMINCRBY");
        println!("{new_price}"); // >>> [4472]

        let updated_fields: String = r
            .json_get("bike:1", &["$.price", "$.inventory.in_stock"])
            .expect("Failed to read updated fields");
        println!("{updated_fields}"); // >>> {"$.price":[4472],"$.inventory.in_stock":[8]}
```



## Append to an array

You can also update arrays in place.
This example adds another color to the bike and then retrieves the updated array.

Update arrays: Append new elements to a JSON array and read back the updated value

**Difficulty:** Intermediate

**Available in:** Rust (Asynchronous), Rust (Synchronous)

##### Rust (Asynchronous)

```rust
        let _: redis::Value = cmd("JSON.ARRAPPEND")
            .arg("bike:1")
            .arg("$.colors")
            .arg("\"red\"")
            .query_async(&mut r)
            .await
            .expect("Failed to run JSON.ARRAPPEND");

        let updated_colors: String = r
            .json_get("bike:1", "$.colors")
            .await
            .expect("Failed to read updated colors");
        println!("{updated_colors}"); // >>> [["black","silver","red"]]
```

##### Rust (Synchronous)

```rust
        let _: redis::Value = cmd("JSON.ARRAPPEND")
            .arg("bike:1")
            .arg("$.colors")
            .arg("\"red\"")
            .query(&mut r)
            .expect("Failed to run JSON.ARRAPPEND");

        let updated_colors: String = r
            .json_get("bike:1", "$.colors")
            .expect("Failed to read updated colors");
        println!("{updated_colors}"); // >>> [["black","silver","red"]]
```



## More information

See the following pages to learn more:

- [JSON data type](https://redis.io/docs/latest/develop/data-types/json)
- [JSON path syntax](https://redis.io/docs/latest/develop/data-types/json/path)
- [`redis-rs` documentation](https://docs.rs/redis/latest/redis/)

