# Probabilistic data types

```json metadata
{
  "schema_version": 2,
  "title": "Probabilistic data types",
  "description": "Learn how to use Bloom filter set membership and HyperLogLog approximate cardinality with redis-rs.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"set-membership","title":"Set membership"},{"id":"set-cardinality","title":"Set cardinality"},{"id":"more-information","title":"More information"}]}

,
  "codeExamples": [{"codetabsId":"home_prob_dts-stepbloom","description":"Set membership: Use Bloom filter to efficiently track item presence with minimal memory overhead","difficulty":"beginner","id":"bloom","languages":[{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_home_prob_dts-stepbloom"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_home_prob_dts-stepbloom"}]},{"codetabsId":"home_prob_dts-stephyperloglog","description":"Set cardinality: Estimate distinct item count using HyperLogLog with minimal memory usage","difficulty":"beginner","id":"hyperloglog","languages":[{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_home_prob_dts-stephyperloglog"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_home_prob_dts-stephyperloglog"}]}]
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


Redis supports several
[probabilistic data types](https://redis.io/docs/latest/develop/data-types/probabilistic)
that let you calculate values approximately rather than exactly.
The `redis-rs` high-level command traits include support for
[Bloom filter](https://redis.io/docs/latest/develop/data-types/probabilistic/bloom-filter)
set membership and
[HyperLogLog](https://redis.io/docs/latest/develop/data-types/probabilistic/hyperloglogs)
cardinality estimation.

> [!NOTE]
> This page covers Bloom filters and HyperLogLog because `redis-rs` provides
> dedicated high-level methods for them. Other probabilistic data types,
> such as Cuckoo filters, Count-min sketch, t-digest, and Top-K, can still be
> called with low-level Redis commands, but they don't currently have dedicated
> high-level `redis-rs` methods.

## Set membership

A [Bloom filter](https://redis.io/docs/latest/develop/data-types/probabilistic/bloom-filter)
lets you track whether or not a particular item has been added to a set.
Instead of storing the items themselves, like a
[set](https://redis.io/docs/latest/develop/data-types/sets), a Bloom filter records the
presence or absence of the
[hash value](https://en.wikipedia.org/wiki/Hash_function) of each item. This
gives a very compact representation of the set's membership with a fixed memory
size, regardless of how many items you add. Note that there is an asymmetry
between presence and absence of items in the set: if an item is reported as
absent, then it is definitely absent, but if it is reported as present, then
there is a small chance it may really be absent.

The `redis-rs` command traits provide high-level `bf_add`, `bf_madd`,
`bf_exists`, and `bf_mexists` methods, among others. The following example adds
some names to a Bloom filter representing a list of users and then checks for
the presence or absence of users in the list.

Set membership: Use Bloom filter to efficiently track item presence with minimal memory overhead

**Difficulty:** Beginner

**Available in:** Rust (Asynchronous), Rust (Synchronous)

##### Rust (Asynchronous)

```rust
        let res1: Vec<bool> = r
            .bf_madd(
                "recorded_users",
                &["andy", "cameron", "david", "michelle"],
            )
            .await
            .expect("Failed to add users to Bloom filter");
        println!("{res1:?}"); // >>> [true, true, true, true]

        let res2: bool = r
            .bf_exists("recorded_users", "cameron")
            .await
            .expect("Failed to check Bloom filter");
        println!("{res2}"); // >>> true

        let res3: bool = r
            .bf_exists("recorded_users", "kaitlyn")
            .await
            .expect("Failed to check Bloom filter");
        println!("{res3}"); // >>> false
```

##### Rust (Synchronous)

```rust
        let res1: Vec<bool> = r
            .bf_madd(
                "recorded_users",
                &["andy", "cameron", "david", "michelle"],
            )
            .expect("Failed to add users to Bloom filter");
        println!("{res1:?}"); // >>> [true, true, true, true]

        let res2: bool = r
            .bf_exists("recorded_users", "cameron")
            .expect("Failed to check Bloom filter");
        println!("{res2}"); // >>> true

        let res3: bool = r
            .bf_exists("recorded_users", "kaitlyn")
            .expect("Failed to check Bloom filter");
        println!("{res3}"); // >>> false
```



## Set cardinality

A HyperLogLog object calculates the approximate cardinality of a set. As you add
items, the HyperLogLog tracks the number of distinct set members, but it doesn't
let you retrieve those members or test whether a specific item was added.

You can also merge two or more HyperLogLogs to find the approximate cardinality
of the [union](https://en.wikipedia.org/wiki/Union_(set_theory)) of the sets
they represent.

Set cardinality: Estimate distinct item count using HyperLogLog with minimal memory usage

**Difficulty:** Beginner

**Available in:** Rust (Asynchronous), Rust (Synchronous)

##### Rust (Asynchronous)

```rust
        let group1_added: bool = r
            .pfadd("group:1", &["andy", "cameron", "david"])
            .await
            .expect("Failed to add items to group:1");
        println!("{group1_added}"); // >>> true

        let group1: usize = r.pfcount("group:1").await.expect("Failed to count group:1");
        println!("{group1}"); // >>> 3

        let group2_added: bool = r
            .pfadd("group:2", &["kaitlyn", "michelle", "paolo", "rachel"])
            .await
            .expect("Failed to add items to group:2");
        println!("{group2_added}"); // >>> true

        let group2: usize = r.pfcount("group:2").await.expect("Failed to count group:2");
        println!("{group2}"); // >>> 4

        let _: () = r
            .pfmerge("both_groups", &["group:1", "group:2"])
            .await
            .expect("Failed to merge HyperLogLogs");
        println!("OK"); // >>> OK

        let both_groups: usize = r
            .pfcount("both_groups")
            .await
            .expect("Failed to count both_groups");
        println!("{both_groups}"); // >>> 7

```

##### Rust (Synchronous)

```rust
        let group1_added: bool = r
            .pfadd("group:1", &["andy", "cameron", "david"])
            .expect("Failed to add items to group:1");
        println!("{group1_added}"); // >>> true

        let group1: usize = r.pfcount("group:1").expect("Failed to count group:1");
        println!("{group1}"); // >>> 3

        let group2_added: bool = r
            .pfadd("group:2", &["kaitlyn", "michelle", "paolo", "rachel"])
            .expect("Failed to add items to group:2");
        println!("{group2_added}"); // >>> true

        let group2: usize = r.pfcount("group:2").expect("Failed to count group:2");
        println!("{group2}"); // >>> 4

        let _: () = r
            .pfmerge("both_groups", &["group:1", "group:2"])
            .expect("Failed to merge HyperLogLogs");
        println!("OK"); // >>> OK

        let both_groups: usize = r
            .pfcount("both_groups")
            .expect("Failed to count both_groups");
        println!("{both_groups}"); // >>> 7

```



The main benefit that HyperLogLogs offer is their very low memory usage. They
can count up to 2^64 items with less than 1% standard error using a maximum
12KB of memory.

## More information

See the following pages to learn more:

- [HyperLogLog](https://redis.io/docs/latest/develop/data-types/probabilistic/hyperloglogs)
- [`redis-rs` command trait](https://docs.rs/redis/latest/redis/trait.Commands.html)
- [`redis-rs` async command trait](https://docs.rs/redis/latest/redis/trait.AsyncCommands.html)

