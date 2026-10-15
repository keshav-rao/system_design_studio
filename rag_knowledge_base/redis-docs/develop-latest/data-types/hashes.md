# Redis hashes

```json metadata
{
  "schema_version": 2,
  "title": "Redis hashes",
  "description": "Introduction to Redis hashes",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"examples","title":"Examples"},{"children":[{"id":"common-field-expiration-use-cases","title":"Common field expiration use cases"},{"id":"field-expiration-examples","title":"Field expiration examples"}],"id":"field-expiration","title":"Field expiration"},{"children":[{"id":"bulk-import-with-himport","title":"Bulk import with HIMPORT"},{"id":"automatic-conversion","title":"Automatic conversion"}],"id":"compact-hashes","title":"Compact hashes"},{"id":"performance","title":"Performance"},{"id":"limits","title":"Limits"},{"id":"learn-more","title":"Learn more"}]}

,
  "codeExamples": [{"codetabsId":"hash_tutorial-stepset_get_all","commands":[{"acl_categories":["@write","@hash","@fast"],"complexity":"O(1)","name":"HSET"},{"acl_categories":["@read","@hash","@fast"],"complexity":"O(1)","name":"HGET"},{"acl_categories":["@read","@hash","@slow"],"complexity":"O(N)","name":"HGETALL"}],"description":"Foundational: Set and retrieve hash fields using HSET and HGET (overwrites existing field values)","difficulty":"beginner","id":"set_get_all","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_hash_tutorial-stepset_get_all"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_hash_tutorial-stepset_get_all"},{"id":"Node-js","panelId":"panel_Nodejs_hash_tutorial-stepset_get_all"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_hash_tutorial-stepset_get_all"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_hash_tutorial-stepset_get_all"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_hash_tutorial-stepset_get_all"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_hash_tutorial-stepset_get_all"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_hash_tutorial-stepset_get_all"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_hash_tutorial-stepset_get_all"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_hash_tutorial-stepset_get_all"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_hash_tutorial-stepset_get_all"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_hash_tutorial-stepset_get_all"}]},{"buildsUpon":["set_get_all"],"codetabsId":"hash_tutorial-stephmget","commands":[{"acl_categories":["@keyspace","@write","@slow"],"complexity":"O(N)","name":"DEL"},{"acl_categories":["@write","@hash","@fast"],"complexity":"O(1)","name":"HSET"},{"acl_categories":["@read","@hash","@fast"],"complexity":"O(N)","name":"HMGET"}],"description":"Retrieve multiple field values from a hash using HMGET when you need to reduce round trips to the server","difficulty":"beginner","id":"hmget","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_hash_tutorial-stephmget"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_hash_tutorial-stephmget"},{"id":"Node-js","panelId":"panel_Nodejs_hash_tutorial-stephmget"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_hash_tutorial-stephmget"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_hash_tutorial-stephmget"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_hash_tutorial-stephmget"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_hash_tutorial-stephmget"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_hash_tutorial-stephmget"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_hash_tutorial-stephmget"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_hash_tutorial-stephmget"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_hash_tutorial-stephmget"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_hash_tutorial-stephmget"}]},{"buildsUpon":["set_get_all"],"codetabsId":"hash_tutorial-stephincrby","commands":[{"acl_categories":["@keyspace","@write","@slow"],"complexity":"O(N)","name":"DEL"},{"acl_categories":["@write","@hash","@fast"],"complexity":"O(1)","name":"HSET"},{"acl_categories":["@write","@hash","@fast"],"complexity":"O(1)","name":"HINCRBY"}],"description":"Increment hash field values for counters using HINCRBY (creates field if missing, initializes to 0)","difficulty":"beginner","id":"hincrby","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_hash_tutorial-stephincrby"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_hash_tutorial-stephincrby"},{"id":"Node-js","panelId":"panel_Nodejs_hash_tutorial-stephincrby"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_hash_tutorial-stephincrby"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_hash_tutorial-stephincrby"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_hash_tutorial-stephincrby"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_hash_tutorial-stephincrby"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_hash_tutorial-stephincrby"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_hash_tutorial-stephincrby"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_hash_tutorial-stephincrby"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_hash_tutorial-stephincrby"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_hash_tutorial-stephincrby"}]},{"buildsUpon":["hincrby","hmget"],"codetabsId":"hash_tutorial-stepincrby_get_mget","commands":[{"acl_categories":["@write","@hash","@fast"],"complexity":"O(1)","name":"HINCRBY"},{"acl_categories":["@read","@hash","@fast"],"complexity":"O(1)","name":"HGET"},{"acl_categories":["@read","@hash","@fast"],"complexity":"O(N)","name":"HMGET"}],"description":"Practical pattern: Combine HINCRBY and HMGET to track multiple counters when you need atomic updates across multiple fields","difficulty":"intermediate","id":"incrby_get_mget","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_hash_tutorial-stepincrby_get_mget"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_hash_tutorial-stepincrby_get_mget"},{"id":"Node-js","panelId":"panel_Nodejs_hash_tutorial-stepincrby_get_mget"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_hash_tutorial-stepincrby_get_mget"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_hash_tutorial-stepincrby_get_mget"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_hash_tutorial-stepincrby_get_mget"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_hash_tutorial-stepincrby_get_mget"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_hash_tutorial-stepincrby_get_mget"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_hash_tutorial-stepincrby_get_mget"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_hash_tutorial-stepincrby_get_mget"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_hash_tutorial-stepincrby_get_mget"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_hash_tutorial-stepincrby_get_mget"}]},{"buildsUpon":["set_get_all"],"codetabsId":"hash_tutorial-stephexpire","commands":[{"acl_categories":["@keyspace","@write","@slow"],"complexity":"O(N)","name":"DEL"},{"acl_categories":["@write","@hash","@fast"],"complexity":"O(1)","name":"HSET"},{"acl_categories":["@write","@hash","@fast"],"complexity":"O(N)","name":"HEXPIRE"},{"acl_categories":["@read","@hash","@fast"],"complexity":"O(N)","name":"HTTL"}],"description":"Field expiration: Set a TTL in seconds on individual hash fields using HEXPIRE, then read the remaining TTL with HTTL","difficulty":"intermediate","id":"hexpire","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_hash_tutorial-stephexpire"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_hash_tutorial-stephexpire"},{"id":"Node-js","panelId":"panel_Nodejs_hash_tutorial-stephexpire"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_hash_tutorial-stephexpire"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_hash_tutorial-stephexpire"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_hash_tutorial-stephexpire"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_hash_tutorial-stephexpire"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_hash_tutorial-stephexpire"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_hash_tutorial-stephexpire"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_hash_tutorial-stephexpire"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_hash_tutorial-stephexpire"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_hash_tutorial-stephexpire"}]},{"buildsUpon":["set_get_all"],"codetabsId":"hash_tutorial-stephpexpire","commands":[{"acl_categories":["@keyspace","@write","@slow"],"complexity":"O(N)","name":"DEL"},{"acl_categories":["@write","@hash","@fast"],"complexity":"O(1)","name":"HSET"},{"acl_categories":["@write","@hash","@fast"],"complexity":"O(N)","name":"HPEXPIRE"},{"acl_categories":["@read","@hash","@fast"],"complexity":"O(N)","name":"HPTTL"}],"description":"Field expiration: Set a TTL in milliseconds on a hash field using HPEXPIRE, then read the remaining TTL with HPTTL","difficulty":"intermediate","id":"hpexpire","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_hash_tutorial-stephpexpire"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_hash_tutorial-stephpexpire"},{"id":"Node-js","panelId":"panel_Nodejs_hash_tutorial-stephpexpire"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_hash_tutorial-stephpexpire"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_hash_tutorial-stephpexpire"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_hash_tutorial-stephpexpire"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_hash_tutorial-stephpexpire"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_hash_tutorial-stephpexpire"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_hash_tutorial-stephpexpire"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_hash_tutorial-stephpexpire"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_hash_tutorial-stephpexpire"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_hash_tutorial-stephpexpire"}]},{"buildsUpon":["set_get_all"],"codetabsId":"hash_tutorial-stephexpireat","commands":[{"acl_categories":["@keyspace","@write","@slow"],"complexity":"O(N)","name":"DEL"},{"acl_categories":["@write","@hash","@fast"],"complexity":"O(1)","name":"HSET"},{"acl_categories":["@write","@hash","@fast"],"complexity":"O(N)","name":"HEXPIREAT"},{"acl_categories":["@read","@hash","@fast"],"complexity":"O(N)","name":"HEXPIRETIME"}],"description":"Field expiration: Set an absolute expiration timestamp on a hash field using HEXPIREAT, then read it back with HEXPIRETIME","difficulty":"intermediate","id":"hexpireat","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_hash_tutorial-stephexpireat"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_hash_tutorial-stephexpireat"},{"id":"Node-js","panelId":"panel_Nodejs_hash_tutorial-stephexpireat"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_hash_tutorial-stephexpireat"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_hash_tutorial-stephexpireat"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_hash_tutorial-stephexpireat"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_hash_tutorial-stephexpireat"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_hash_tutorial-stephexpireat"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_hash_tutorial-stephexpireat"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_hash_tutorial-stephexpireat"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_hash_tutorial-stephexpireat"}]},{"codetabsId":"hash_import-stephimport_basic","commands":[{"acl_categories":["@hash","@slow"],"complexity":"Depends on subcommand","name":"HIMPORT"},{"acl_categories":["@read","@hash","@slow"],"complexity":"O(N)","name":"HGETALL"}],"description":"Foundational: Declare shared field names once with HIMPORT PREPARE, then create each hash by sending only its values with HIMPORT SET","difficulty":"intermediate","id":"himport_basic","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_hash_import-stephimport_basic"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_hash_import-stephimport_basic"},{"id":"Node-js","panelId":"panel_Nodejs_hash_import-stephimport_basic"},{"clientId":"ioredis","clientName":"ioredis","id":"ioredis","langId":"javascript","panelId":"panel_ioredis_hash_import-stephimport_basic"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_hash_import-stephimport_basic"},{"clientId":"lettuce","clientName":"Lettuce","id":"Lettuce-Sync","langId":"java","panelId":"panel_Lettuce-Sync_hash_import-stephimport_basic"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_hash_import-stephimport_basic"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_hash_import-stephimport_basic"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_hash_import-stephimport_basic"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_hash_import-stephimport_basic"},{"id":"dotnet-Async (SE-Redis)","panelId":"panel_Csharp-Async (SERedis)_hash_import-stephimport_basic"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_hash_import-stephimport_basic"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_hash_import-stephimport_basic"}]},{"buildsUpon":["himport_basic"],"codetabsId":"hash_import-stephimport_pipeline","commands":[{"acl_categories":["@hash","@slow"],"complexity":"Depends on subcommand","name":"HIMPORT"},{"acl_categories":["@read","@hash","@fast"],"complexity":"O(1)","name":"HGET"}],"description":"Bulk ingestion: Pipeline many HIMPORT SET calls that share one fieldset to load a large number of hashes with few network round trips","difficulty":"intermediate","id":"himport_pipeline","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_hash_import-stephimport_pipeline"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_hash_import-stephimport_pipeline"},{"id":"Node-js","panelId":"panel_Nodejs_hash_import-stephimport_pipeline"},{"clientId":"ioredis","clientName":"ioredis","id":"ioredis","langId":"javascript","panelId":"panel_ioredis_hash_import-stephimport_pipeline"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_hash_import-stephimport_pipeline"},{"clientId":"lettuce","clientName":"Lettuce","id":"Lettuce-Sync","langId":"java","panelId":"panel_Lettuce-Sync_hash_import-stephimport_pipeline"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_hash_import-stephimport_pipeline"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_hash_import-stephimport_pipeline"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_hash_import-stephimport_pipeline"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_hash_import-stephimport_pipeline"},{"id":"dotnet-Async (SE-Redis)","panelId":"panel_Csharp-Async (SERedis)_hash_import-stephimport_pipeline"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_hash_import-stephimport_pipeline"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_hash_import-stephimport_pipeline"}]}]
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


### Hash command summary

**33 commands in this group:**

[View all hash commands](https://redis.io/commands/?group=hash)

| Command | Summary | Complexity | Since |
|---------|---------|------------|-------|
| [HDEL](https://redis.io/commands/hdel/) | Deletes one or more fields and their values from a hash. Deletes the hash if no fields remain. | O(N) where N is the number of fields to be remo... | 2.0.0 |
| [HEXISTS](https://redis.io/commands/hexists/) | Determines whether a field exists in a hash. | O(1) | 2.0.0 |
| [HEXPIRE](https://redis.io/commands/hexpire/) | Set expiry for hash field using relative time to expire (seconds) | O(N) where N is the number of specified fields | 7.4.0 |
| [HEXPIREAT](https://redis.io/commands/hexpireat/) | Set expiry for hash field using an absolute Unix timestamp (seconds) | O(N) where N is the number of specified fields | 7.4.0 |
| [HEXPIRETIME](https://redis.io/commands/hexpiretime/) | Returns the expiration time of a hash field as a Unix timestamp, in seconds. | O(N) where N is the number of specified fields | 7.4.0 |
| [HGET](https://redis.io/commands/hget/) | Returns the value of a field in a hash. | O(1) | 2.0.0 |
| [HGETALL](https://redis.io/commands/hgetall/) | Returns all fields and values in a hash. | O(N) where N is the size of the hash. | 2.0.0 |
| [HGETDEL](https://redis.io/commands/hgetdel/) | Returns the value of a field and deletes it from the hash. | O(N) where N is the number of specified fields | 8.0.0 |
| [HGETEX](https://redis.io/commands/hgetex/) | Get the value of one or more fields of a given hash key, and optionally set their expiration. | O(N) where N is the number of specified fields | 8.0.0 |
| [HIMPORT](https://redis.io/commands/himport/) | A container for session-based hash import commands using fieldsets. | Depends on subcommand. | 8.10.0 |

#### Hash command summary (part 2)

| Command | Summary | Complexity | Since |
|---------|---------|------------|-------|
| [HIMPORT DISCARD](https://redis.io/commands/himport-discard/) | Removes a single session-local fieldset by name. | O(N) where N is the number of session-local fie... | 8.10.0 |
| [HIMPORT DISCARDALL](https://redis.io/commands/himport-discardall/) | Removes all session-local fieldsets for the connection. | O(N) where N is the number of session-local fie... | 8.10.0 |
| [HIMPORT PREPARE](https://redis.io/commands/himport-prepare/) | Defines a session-local fieldset that maps a name to a sorted set of field names. | O(N*log(N)) where N is the number of fields. | 8.10.0 |
| [HIMPORT SET](https://redis.io/commands/himport-set/) | Creates a fieldset-based hash from values supplied in the order matching a previously prepared fieldset. | O(N) where N is the number of fields in the fie... | 8.10.0 |
| [HINCRBY](https://redis.io/commands/hincrby/) | Increments the integer value of a field in a hash by a number. Uses 0 as initial value if the field doesn't exist. | O(1) | 2.0.0 |
| [HINCRBYFLOAT](https://redis.io/commands/hincrbyfloat/) | Increments the floating point value of a field by a number. Uses 0 as initial value if the field doesn't exist. | O(1) | 2.6.0 |
| [HKEYS](https://redis.io/commands/hkeys/) | Returns all fields in a hash. | O(N) where N is the size of the hash. | 2.0.0 |
| [HLEN](https://redis.io/commands/hlen/) | Returns the number of fields in a hash. | O(1) | 2.0.0 |
| [HMGET](https://redis.io/commands/hmget/) | Returns the values of all fields in a hash. | O(N) where N is the number of fields being requ... | 2.0.0 |
| [HMSET](https://redis.io/commands/hmset/) | Sets the values of multiple fields. | O(N) where N is the number of fields being set. | 2.0.0 |

#### Hash command summary (part 3)

| Command | Summary | Complexity | Since |
|---------|---------|------------|-------|
| [HPERSIST](https://redis.io/commands/hpersist/) | Removes the expiration time for each specified field | O(N) where N is the number of specified fields | 7.4.0 |
| [HPEXPIRE](https://redis.io/commands/hpexpire/) | Set expiry for hash field using relative time to expire (milliseconds) | O(N) where N is the number of specified fields | 7.4.0 |
| [HPEXPIREAT](https://redis.io/commands/hpexpireat/) | Set expiry for hash field using an absolute Unix timestamp (milliseconds) | O(N) where N is the number of specified fields | 7.4.0 |
| [HPEXPIRETIME](https://redis.io/commands/hpexpiretime/) | Returns the expiration time of a hash field as a Unix timestamp, in msec. | O(N) where N is the number of specified fields | 7.4.0 |
| [HPTTL](https://redis.io/commands/hpttl/) | Returns the TTL in milliseconds of a hash field. | O(N) where N is the number of specified fields | 7.4.0 |
| [HRANDFIELD](https://redis.io/commands/hrandfield/) | Returns one or more random fields from a hash. | O(N) where N is the number of fields returned | 6.2.0 |
| [HSCAN](https://redis.io/commands/hscan/) | Iterates over fields and values of a hash. | O(1) for every call. O(N) for a complete iterat... | 2.8.0 |
| [HSET](https://redis.io/commands/hset/) | Creates or modifies the value of a field in a hash. | O(1) for each field/value pair added, so O(N) t... | 2.0.0 |
| [HSETEX](https://redis.io/commands/hsetex/) | Set the value of one or more fields of a given hash key, and optionally set their expiration. | O(N) where N is the number of fields being set. | 8.0.0 |
| [HSETNX](https://redis.io/commands/hsetnx/) | Sets the value of a field in a hash only when the field doesn't exist. | O(1) | 2.0.0 |

#### Hash command summary (part 4)

| Command | Summary | Complexity | Since |
|---------|---------|------------|-------|
| [HSTRLEN](https://redis.io/commands/hstrlen/) | Returns the length of the value of a field. | O(1) | 3.2.0 |
| [HTTL](https://redis.io/commands/httl/) | Returns the TTL in seconds of a hash field. | O(N) where N is the number of specified fields | 7.4.0 |
| [HVALS](https://redis.io/commands/hvals/) | Returns all values in a hash. | O(N) where N is the size of the hash. | 2.0.0 |



Redis hashes are record types structured as collections of field-value pairs.
You can use hashes to represent basic objects and to store groupings of counters, among other things.

Foundational: Set and retrieve hash fields using HSET and HGET (overwrites existing field values)

**Commands:** HSET, HGET, HGETALL

**Complexity:**
- HSET: O(1)
- HGET: O(1)
- HGETALL: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> HSET bike:1 model Deimos brand Ergonom type 'Enduro bikes' price 4972
(integer) 4
> HGET bike:1 model
"Deimos"
> HGET bike:1 price
"4972"
> HGETALL bike:1
1) "model"
2) "Deimos"
3) "brand"
4) "Ergonom"
5) "type"
6) "Enduro bikes"
7) "price"
8) "4972"
```

##### C#

```csharp
        db.HashSet("bike:1", [
            new("model", "Deimos"),
            new("brand", "Ergonom"),
            new("type", "Enduro bikes"),
            new("price", 4972)
        ]);

        Console.WriteLine("Hash Created");
        // Hash Created

        var model = db.HashGet("bike:1", "model");
        Console.WriteLine($"Model: {model}");
        // Model: Deimos

        var price = db.HashGet("bike:1", "price");
        Console.WriteLine($"Price: {price}");
        // Price: 4972

        var bike = db.HashGetAll("bike:1");
        Console.WriteLine("bike:1");
        Console.WriteLine(string.Join("\n", bike.Select(b => $"{b.Name}: {b.Value}")));
        // Bike:1:
        // model: Deimos
        // brand: Ergonom
        // type: Enduro bikes
        // price: 4972
```

##### Go

```go
	hashFields := []string{
		"model", "Deimos",
		"brand", "Ergonom",
		"type", "Enduro bikes",
		"price", "4972",
	}

	res1, err := rdb.HSet(ctx, "bike:1", hashFields).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // >>> 4

	res2, err := rdb.HGet(ctx, "bike:1", "model").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2) // >>> Deimos

	res3, err := rdb.HGet(ctx, "bike:1", "price").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3) // >>> 4972

	cmdReturn := rdb.HGetAll(ctx, "bike:1")
	res4, err := cmdReturn.Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4)
	// >>> map[brand:Ergonom model:Deimos price:4972 type:Enduro bikes]

	type BikeInfo struct {
		Model string `redis:"model"`
		Brand string `redis:"brand"`
		Type  string `redis:"type"`
		Price int    `redis:"price"`
	}

	var res4a BikeInfo

	if err := cmdReturn.Scan(&res4a); err != nil {
		panic(err)
	}

	fmt.Printf("Model: %v, Brand: %v, Type: %v, Price: $%v\n",
		res4a.Model, res4a.Brand, res4a.Type, res4a.Price)
	// >>> Model: Deimos, Brand: Ergonom, Type: Enduro bikes, Price: $4972
```

##### Java (Asynchronous - Lettuce)

```java
            Map<String, String> bike1 = new HashMap<>();
            bike1.put("model", "Deimos");
            bike1.put("brand", "Ergonom");
            bike1.put("type", "Enduro bikes");
            bike1.put("price", "4972");

            CompletableFuture<Void> setGetAll = asyncCommands.hset("bike:1", bike1).thenCompose(res1 -> {
                System.out.println(res1); // >>> 4
                return asyncCommands.hget("bike:1", "model");
            }).thenCompose(res2 -> {
                System.out.println(res2); // >>> Deimos
                return asyncCommands.hget("bike:1", "price");
            }).thenCompose(res3 -> {
                System.out.println(res3); // >>> 4972
                return asyncCommands.hgetall("bike:1");
            })
                    .thenAccept(System.out::println)
                    // >>> {type=Enduro bikes, brand=Ergonom, price=4972, model=Deimos}
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Map<String, String> bike1 = new HashMap<>();
            bike1.put("model", "Deimos");
            bike1.put("brand", "Ergonom");
            bike1.put("type", "Enduro bikes");
            bike1.put("price", "4972");

            Mono<Long> setGetAll = reactiveCommands.hset("bike:1", bike1).doOnNext(result -> {
                System.out.println(result); // >>> 4
            });

            setGetAll.block();

            Mono<String> getModel = reactiveCommands.hget("bike:1", "model").doOnNext(result -> {
                System.out.println(result); // >>> Deimos
            });

            Mono<String> getPrice = reactiveCommands.hget("bike:1", "price").doOnNext(result -> {
                System.out.println(result); // >>> 4972
            });

            Mono<List<KeyValue<String, String>>> getAll = reactiveCommands.hgetall("bike:1").collectList().doOnNext(result -> {
                System.out.println(result);
                // >>> [KeyValue[type, Enduro bikes], KeyValue[brand, Ergonom],
                // KeyValue[price, 4972], KeyValue[model, Deimos]]
            });
```

##### Java (Synchronous - Jedis)

```java
      Map<String, String> bike1 = new HashMap<>();
      bike1.put("model", "Deimos");
      bike1.put("brand", "Ergonom");
      bike1.put("type", "Enduro bikes");
      bike1.put("price", "4972");

      Long res1 = jedis.hset("bike:1", bike1);
      System.out.println(res1); // 4

      String res2 = jedis.hget("bike:1", "model");
      System.out.println(res2); // Deimos

      String res3 = jedis.hget("bike:1", "price");
      System.out.println(res3); // 4972

      Map<String, String> res4 = jedis.hgetAll("bike:1");
      System.out.println(res4); // {type=Enduro bikes, brand=Ergonom, price=4972, model=Deimos}
```

##### JavaScript (Node.js)

```javascript
const res1 = await client.hSet(
  'bike:1',
  {
    'model': 'Deimos',
    'brand': 'Ergonom',
    'type': 'Enduro bikes',
    'price': 4972,
  }
)
console.log(res1) // 4

const res2 = await client.hGet('bike:1', 'model')
console.log(res2)  // 'Deimos'

const res3 = await client.hGet('bike:1', 'price')
console.log(res3)  // '4972'

const res4 = await client.hGetAll('bike:1')
console.log(res4)  
/*
{
  brand: 'Ergonom',
  model: 'Deimos',
  price: '4972',
  type: 'Enduro bikes'
}
*/
```

##### PHP

```php
        $res1 = $r->hmset('bike:1', [
            'model' => 'Deimos',
            'brand' => 'Ergonom',
            'type' => 'Enduro bikes',
            'price' => 4972,
        ]);

        echo $res1 . PHP_EOL;
        // >>> 4

        $res2 = $r->hget('bike:1', 'model');
        echo $res2 . PHP_EOL;
        // >>> Deimos

        $res3 = $r->hget('bike:1', 'price');
        echo $res3 . PHP_EOL;
        // >>> 4972

        $res4 = $r->hgetall('bike:1');
        echo json_encode($res3) . PHP_EOL;
        // >>> {"name":"Deimos","brand":"Ergonom","type":"Enduro bikes","price":"4972"}
```

##### Python

```python
res1 = r.hset(
    "bike:1",
    mapping={
        "model": "Deimos",
        "brand": "Ergonom",
        "type": "Enduro bikes",
        "price": 4972,
    },
)
print(res1)
# >>> 4

res2 = r.hget("bike:1", "model")
print(res2)
# >>> 'Deimos'

res3 = r.hget("bike:1", "price")
print(res3)
# >>> '4972'

res4 = r.hgetall("bike:1")
print(res4)
# >>> {'model': 'Deimos', 'brand': 'Ergonom', 'type': 'Enduro bikes', 'price': '4972'}

```

##### Ruby

```ruby
res1 = r.hset('bike:1', {
  'model' => 'Deimos',
  'brand' => 'Ergonom',
  'type' => 'Enduro bikes',
  'price' => 4972
})
puts res1 # >>> 4

res2 = r.hget('bike:1', 'model')
puts res2 # >>> Deimos

res3 = r.hget('bike:1', 'price')
puts res3 # >>> 4972

res4 = r.hgetall('bike:1')
puts res4.inspect
# >>> {"model" => "Deimos", "brand" => "Ergonom", "type" => "Enduro bikes", "price" => "4972"}
```

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
            println!("{res}");    // >>> OK
        }

        match r.hget("bike:1", "model").await {
            Ok(res) => {
                let res: String = res;
                println!("{res}");   // >>> Deimos
            },
            Err(e) => {
                println!("Error getting bike:1 model: {e}");
                return;
            }
        };

        match r.hget("bike:1", "price").await {
            Ok(res) => {
                let res: String = res;
                println!("{res}");   // >>> 4972
            },
            Err(e) => {
                println!("Error getting bike:1 price: {e}");
                return;
            }
        };

        match r.hgetall("bike:1").await {
            Ok(res) => {
                let res: Vec<(String, String)> = res;
                println!("{res:?}");
                // >>> [("model", "Deimos"), ("brand", "Ergonom"), ("type", "Enduro bikes"), ("price", "4972")]
            },
            Err(e) => {
                println!("Error getting bike:1: {e}");
                return;
            }
        };
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
            println!("{res}");    // >>> OK
        }

        match r.hget("bike:1", "model") {
            Ok(res) => {
                let res: String = res;
                println!("{res}");   // >>> Deimos
            },
            Err(e) => {
                println!("Error getting bike:1 model: {e}");
                return;
            }
        };

        match r.hget("bike:1", "price") {
            Ok(res) => {
                let res: String = res;
                println!("{res}");   // >>> 4972
            },
            Err(e) => {
                println!("Error getting bike:1 price: {e}");
                return;
            }
        };

        match r.hgetall("bike:1") {
            Ok(res) => {
                let res: Vec<(String, String)> = res;
                println!("{res:?}");
                // >>> [("model", "Deimos"), ("brand", "Ergonom"), ("type", "Enduro bikes"), ("price", "4972")]
            },
            Err(e) => {
                println!("Error getting bike:1: {e}");
                return;
            }
        };
```



While hashes are handy to represent *objects*, actually the number of fields you can
put inside a hash has no practical limits (other than available memory), so you can use
hashes in many different ways inside your application.

The command [`HSET`](https://redis.io/docs/latest/commands/hset) sets multiple fields of the hash, while [`HGET`](https://redis.io/docs/latest/commands/hget) retrieves
a single field. [`HMGET`](https://redis.io/docs/latest/commands/hmget) is similar to [`HGET`](https://redis.io/docs/latest/commands/hget) but returns an array of values:

Retrieve multiple field values from a hash using HMGET when you need to reduce round trips to the server

**Builds upon:** set_get_all

**Commands:** DEL, HSET, HMGET

**Complexity:**
- DEL: O(N)
- HSET: O(1)
- HMGET: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
# Recreate the bike:1 hash so this example runs on its own.
> DEL bike:1
(integer) 1
> HSET bike:1 model Deimos brand Ergonom type 'Enduro bikes' price 4972
(integer) 4
> HMGET bike:1 model price no-such-field
1) "Deimos"
2) "4972"
3) (nil)
```

##### C#

```csharp
        // Recreate the bike:1 hash so this example runs on its own.
        db.KeyDelete("bike:1");
        db.HashSet("bike:1", [
            new("model", "Deimos"),
            new("brand", "Ergonom"),
            new("type", "Enduro bikes"),
            new("price", 4972)
        ]);

        var values = db.HashGet("bike:1", ["model", "price"]);
        Console.WriteLine(string.Join(" ", values));
        // Deimos 4972
```

##### Go

```go
	// Recreate the bike:1 hash so this example runs on its own.
	rdb.Del(ctx, "bike:1")
	hashFields := []string{
		"model", "Deimos",
		"brand", "Ergonom",
		"type", "Enduro bikes",
		"price", "4972",
	}
	rdb.HSet(ctx, "bike:1", hashFields)

	cmdReturn := rdb.HMGet(ctx, "bike:1", "model", "price")
	res5, err := cmdReturn.Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res5) // >>> [Deimos 4972]

	type BikeInfo struct {
		Model string `redis:"model"`
		Brand string `redis:"-"`
		Type  string `redis:"-"`
		Price int    `redis:"price"`
	}

	var res5a BikeInfo

	if err := cmdReturn.Scan(&res5a); err != nil {
		panic(err)
	}

	fmt.Printf("Model: %v, Price: $%v\n", res5a.Model, res5a.Price)
	// >>> Model: Deimos, Price: $4972
```

##### Java (Asynchronous - Lettuce)

```java
            // Recreate the bike:1 hash so this example runs on its own.
            CompletableFuture<Void> hmGet = setGetAll
                    .thenCompose(res4 -> asyncCommands.del("bike:1"))
                    .thenCompose(delRes -> asyncCommands.hset("bike:1", bike1))
                    .thenCompose(hsetRes -> asyncCommands.hmget("bike:1", "model", "price"))
                    .thenAccept(System.out::println)
                    // [KeyValue[model, Deimos], KeyValue[price, 4972]]
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            // Recreate the bike:1 hash so this example runs on its own.
            Mono<List<KeyValue<String, String>>> hmGet = reactiveCommands.del("bike:1")
                    .then(reactiveCommands.hset("bike:1", bike1))
                    .then(reactiveCommands.hmget("bike:1", "model", "price").collectList())
                    .doOnNext(result -> {
                        System.out.println(result);
                        // >>> [KeyValue[model, Deimos], KeyValue[price, 4972]]
                    });
```

##### Java (Synchronous - Jedis)

```java
      // Recreate the bike:1 hash so this example runs on its own.
      jedis.del("bike:1");
      jedis.hset("bike:1", bike1);

      List<String> res5 = jedis.hmget("bike:1", "model", "price");
      System.out.println(res5); // [Deimos, 4972]
```

##### JavaScript (Node.js)

```javascript
// Recreate the bike:1 hash so this example runs on its own.
await client.del('bike:1')
await client.hSet(
  'bike:1',
  {
    'model': 'Deimos',
    'brand': 'Ergonom',
    'type': 'Enduro bikes',
    'price': 4972,
  }
)

const res5 = await client.hmGet('bike:1', ['model', 'price'])
console.log(res5)  // ['Deimos', '4972']
```

##### PHP

```php
        // Recreate the bike:1 hash so this example runs on its own.
        $r->del('bike:1');
        $r->hmset('bike:1', [
            'model' => 'Deimos',
            'brand' => 'Ergonom',
            'type' => 'Enduro bikes',
            'price' => 4972,
        ]);

        $res5 = $r->hmget('bike:1', ['model', 'price']);
        echo json_encode($res5) . PHP_EOL;
        // >>> ["Deimos","4972"]
```

##### Python

```python
# Recreate the bike:1 hash so this example runs on its own.
r.delete("bike:1")
r.hset(
    "bike:1",
    mapping={
        "model": "Deimos",
        "brand": "Ergonom",
        "type": "Enduro bikes",
        "price": 4972,
    },
)

res5 = r.hmget("bike:1", ["model", "price"])
print(res5)
# >>> ['Deimos', '4972']
```

##### Ruby

```ruby
# Recreate the bike:1 hash so this example runs on its own.
r.del('bike:1')
r.hset('bike:1', {
  'model' => 'Deimos',
  'brand' => 'Ergonom',
  'type' => 'Enduro bikes',
  'price' => 4972
})

res5 = r.hmget('bike:1', 'model', 'price', 'no-such-field')
puts res5.inspect # >>> ["Deimos", "4972", nil]
```

##### Rust (Asynchronous)

```rust
        // Recreate the bike:1 hash so this example runs on its own.
        let _: () = r.del("bike:1").await.expect("Failed to del");
        let _: () = r.hset_multiple(
            "bike:1",
            &[("model", "Deimos"), ("brand", "Ergonom"), ("type", "Enduro bikes"), ("price", "4972")],
        ).await.expect("Failed to hset");

        match r.hmget("bike:1", &["model", "price"]).await {
            Ok(res) => {
                let res: Vec<String> = res;
                println!("{res:?}");   // >>> ["Deimos", "4972"]
            },
            Err(e) => {
                println!("Error getting bike:1: {e}");
                return;
            }
        };
```

##### Rust (Synchronous)

```rust
        // Recreate the bike:1 hash so this example runs on its own.
        let _: () = r.del("bike:1").expect("Failed to del");
        let _: () = r.hset_multiple(
            "bike:1",
            &[("model", "Deimos"), ("brand", "Ergonom"), ("type", "Enduro bikes"), ("price", "4972")],
        ).expect("Failed to hset");

        match r.hmget("bike:1", &["model", "price"]) {
            Ok(res) => {
                let res: Vec<String> = res;
                println!("{res:?}");   // >>> ["Deimos", "4972"]
            },
            Err(e) => {
                println!("Error getting bike:1: {e}");
                return;
            }
        };
```



There are commands that are able to perform operations on individual fields
as well, like [`HINCRBY`](https://redis.io/docs/latest/commands/hincrby):

Increment hash field values for counters using HINCRBY (creates field if missing, initializes to 0)

**Builds upon:** set_get_all

**Commands:** DEL, HSET, HINCRBY

**Complexity:**
- DEL: O(N)
- HSET: O(1)
- HINCRBY: O(1)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
# Recreate the bike:1 hash so this example runs on its own.
> DEL bike:1
(integer) 1
> HSET bike:1 model Deimos brand Ergonom type 'Enduro bikes' price 4972
(integer) 4
> HINCRBY bike:1 price 100
(integer) 5072
> HINCRBY bike:1 price -100
(integer) 4972
```

##### C#

```csharp
        // Recreate the bike:1 hash so this example runs on its own.
        db.KeyDelete("bike:1");
        db.HashSet("bike:1", [
            new("model", "Deimos"),
            new("brand", "Ergonom"),
            new("type", "Enduro bikes"),
            new("price", 4972)
        ]);

        var newPrice = db.HashIncrement("bike:1", "price", 100);
        Console.WriteLine($"New price: {newPrice}");
        // New price: 5072

        newPrice = db.HashIncrement("bike:1", "price", -100);
        Console.WriteLine($"New price: {newPrice}");
        // New price: 4972
```

##### Go

```go
	// Recreate the bike:1 hash so this example runs on its own.
	rdb.Del(ctx, "bike:1")
	hashFields := []string{
		"model", "Deimos",
		"brand", "Ergonom",
		"type", "Enduro bikes",
		"price", "4972",
	}
	rdb.HSet(ctx, "bike:1", hashFields)

	res6, err := rdb.HIncrBy(ctx, "bike:1", "price", 100).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res6) // >>> 5072

	res7, err := rdb.HIncrBy(ctx, "bike:1", "price", -100).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res7) // >>> 4972
```

##### Java (Asynchronous - Lettuce)

```java
            // Recreate the bike:1 hash so this example runs on its own.
            CompletableFuture<Void> hIncrBy = hmGet
                    .thenCompose(r -> asyncCommands.del("bike:1"))
                    .thenCompose(delRes -> asyncCommands.hset("bike:1", bike1))
                    .thenCompose(hsetRes -> asyncCommands.hincrby("bike:1", "price", 100))
                    .thenCompose(res6 -> {
                        System.out.println(res6); // >>> 5072
                        return asyncCommands.hincrby("bike:1", "price", -100);
                    })
                    .thenAccept(System.out::println)
                    // >>> 4972
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            // Recreate the bike:1 hash so this example runs on its own.
            Mono<Void> hIncrBy = reactiveCommands.del("bike:1")
                    .then(reactiveCommands.hset("bike:1", bike1))
                    .then(reactiveCommands.hincrby("bike:1", "price", 100)).doOnNext(result -> {
                System.out.println(result); // >>> 5072
            }).flatMap(v -> reactiveCommands.hincrby("bike:1", "price", -100)).doOnNext(result -> {
                System.out.println(result); // >>> 4972
            }).then();
```

##### Java (Synchronous - Jedis)

```java
      // Recreate the bike:1 hash so this example runs on its own.
      jedis.del("bike:1");
      jedis.hset("bike:1", bike1);

      Long res6 = jedis.hincrBy("bike:1", "price", 100);
      System.out.println(res6); // 5072
      Long res7 = jedis.hincrBy("bike:1", "price", -100);
      System.out.println(res7); // 4972
```

##### JavaScript (Node.js)

```javascript
// Recreate the bike:1 hash so this example runs on its own.
await client.del('bike:1')
await client.hSet(
  'bike:1',
  {
    'model': 'Deimos',
    'brand': 'Ergonom',
    'type': 'Enduro bikes',
    'price': 4972,
  }
)

const res6 = await client.hIncrBy('bike:1', 'price', 100)
console.log(res6)  // 5072
const res7 = await client.hIncrBy('bike:1', 'price', -100)
console.log(res7)  // 4972
```

##### PHP

```php
        // Recreate the bike:1 hash so this example runs on its own.
        $r->del('bike:1');
        $r->hmset('bike:1', [
            'model' => 'Deimos',
            'brand' => 'Ergonom',
            'type' => 'Enduro bikes',
            'price' => 4972,
        ]);

        $res6 = $r->hincrby('bike:1', 'price', 100);
        echo $res6 . PHP_EOL;
        // >>> 5072

        $res7 = $r->hincrby('bike:1', 'price', -100);
        echo $res7 . PHP_EOL;
        // >>> 4972
```

##### Python

```python
# Recreate the bike:1 hash so this example runs on its own.
r.delete("bike:1")
r.hset(
    "bike:1",
    mapping={
        "model": "Deimos",
        "brand": "Ergonom",
        "type": "Enduro bikes",
        "price": 4972,
    },
)

res6 = r.hincrby("bike:1", "price", 100)
print(res6)
# >>> 5072
res7 = r.hincrby("bike:1", "price", -100)
print(res7)
# >>> 4972
```

##### Ruby

```ruby
# Recreate the bike:1 hash so this example runs on its own.
r.del('bike:1')
r.hset('bike:1', {
  'model' => 'Deimos',
  'brand' => 'Ergonom',
  'type' => 'Enduro bikes',
  'price' => 4972
})

res6 = r.hincrby('bike:1', 'price', 100)
puts res6 # >>> 5072

res7 = r.hincrby('bike:1', 'price', -100)
puts res7 # >>> 4972
```

##### Rust (Asynchronous)

```rust
        // Recreate the bike:1 hash so this example runs on its own.
        let _: () = r.del("bike:1").await.expect("Failed to del");
        let _: () = r.hset_multiple(
            "bike:1",
            &[("model", "Deimos"), ("brand", "Ergonom"), ("type", "Enduro bikes"), ("price", "4972")],
        ).await.expect("Failed to hset");

        if let Ok(res) = r.hincr("bike:1", "price", 100).await {
            let res: i32 = res;
            println!("{res}");    // >>> 5072
        }

        if let Ok(res) = r.hincr("bike:1", "price", -100).await {
            let res: i32 = res;
            println!("{res}");    // >>> 4972
        }
```

##### Rust (Synchronous)

```rust
        // Recreate the bike:1 hash so this example runs on its own.
        let _: () = r.del("bike:1").expect("Failed to del");
        let _: () = r.hset_multiple(
            "bike:1",
            &[("model", "Deimos"), ("brand", "Ergonom"), ("type", "Enduro bikes"), ("price", "4972")],
        ).expect("Failed to hset");

        if let Ok(res) = r.hincr("bike:1", "price", 100) {
            let res: i32 = res;
            println!("{res}");    // >>> 5072
        }

        if let Ok(res) = r.hincr("bike:1", "price", -100) {
            let res: i32 = res;
            println!("{res}");    // >>> 4972
        }
```



You can find the [full list of hash commands in the documentation](/commands?group=hash).

It is worth noting that small hashes (i.e., a few elements with small values) are
encoded in special way in memory that make them very memory efficient.

## Examples

* Store counters for the number of times bike:1 has been ridden, has crashed, or has changed owners:
Practical pattern: Combine HINCRBY and HMGET to track multiple counters when you need atomic updates across multiple fields

**Difficulty:** Intermediate

**Builds upon:** hincrby, hmget

**Commands:** HINCRBY, HGET, HMGET

**Complexity:**
- HINCRBY: O(1)
- HGET: O(1)
- HMGET: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> HINCRBY bike:1:stats rides 1
(integer) 1
> HINCRBY bike:1:stats rides 1
(integer) 2
> HINCRBY bike:1:stats rides 1
(integer) 3
> HINCRBY bike:1:stats crashes 1
(integer) 1
> HINCRBY bike:1:stats owners 1
(integer) 1
> HGET bike:1:stats rides
"3"
> HMGET bike:1:stats owners crashes
1) "1"
2) "1"
```

##### C#

```csharp
        var rides = db.HashIncrement("bike:1", "rides");
        Console.WriteLine($"Rides: {rides}");
        // Rides: 1

        rides = db.HashIncrement("bike:1", "rides");
        Console.WriteLine($"Rides: {rides}");
        // Rides: 2

        rides = db.HashIncrement("bike:1", "rides");
        Console.WriteLine($"Rides: {rides}");
        // Rides: 3

        var crashes = db.HashIncrement("bike:1", "crashes");
        Console.WriteLine($"Crashes: {crashes}");
        // Crashes: 1

        var owners = db.HashIncrement("bike:1", "owners");
        Console.WriteLine($"Owners: {owners}");
        // Owners: 1

        var stats = db.HashGet("bike:1", ["crashes", "owners"]);
        Console.WriteLine($"Bike stats: crashes={stats[0]}, owners={stats[1]}");
        // Bike stats: crashes=1, owners=1
```

##### Go

```go
	res8, err := rdb.HIncrBy(ctx, "bike:1:stats", "rides", 1).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res8) // >>> 1

	res9, err := rdb.HIncrBy(ctx, "bike:1:stats", "rides", 1).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res9) // >>> 2

	res10, err := rdb.HIncrBy(ctx, "bike:1:stats", "rides", 1).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res10) // >>> 3

	res11, err := rdb.HIncrBy(ctx, "bike:1:stats", "crashes", 1).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res11) // >>> 1

	res12, err := rdb.HIncrBy(ctx, "bike:1:stats", "owners", 1).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res12) // >>> 1

	res13, err := rdb.HGet(ctx, "bike:1:stats", "rides").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res13) // >>> 3

	res14, err := rdb.HMGet(ctx, "bike:1:stats", "crashes", "owners").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res14) // >>> [1 1]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> incrByGetMget = asyncCommands.hincrby("bike:1:stats", "rides", 1).thenCompose(res7 -> {
                System.out.println(res7); // >>> 1
                return asyncCommands.hincrby("bike:1:stats", "rides", 1);
            }).thenCompose(res8 -> {
                System.out.println(res8); // >>> 2
                return asyncCommands.hincrby("bike:1:stats", "rides", 1);
            }).thenCompose(res9 -> {
                System.out.println(res9); // >>> 3
                return asyncCommands.hincrby("bike:1:stats", "crashes", 1);
            }).thenCompose(res10 -> {
                System.out.println(res10); // >>> 1
                return asyncCommands.hincrby("bike:1:stats", "owners", 1);
            }).thenCompose(res11 -> {
                System.out.println(res11); // >>> 1
                return asyncCommands.hget("bike:1:stats", "rides");
            }).thenCompose(res12 -> {
                System.out.println(res12); // >>> 3
                return asyncCommands.hmget("bike:1:stats", "crashes", "owners");
            })
                    .thenAccept(System.out::println)
                    // >>> [KeyValue[crashes, 1], KeyValue[owners, 1]]
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> incrByGetMget = reactiveCommands.hincrby("bike:1:stats", "rides", 1).doOnNext(result -> {
                System.out.println(result); // >>> 1
            }).flatMap(v -> reactiveCommands.hincrby("bike:1:stats", "rides", 1)).doOnNext(result -> {
                System.out.println(result); // >>> 2
            }).flatMap(v -> reactiveCommands.hincrby("bike:1:stats", "rides", 1)).doOnNext(result -> {
                System.out.println(result); // >>> 3
            }).flatMap(v -> reactiveCommands.hincrby("bike:1:stats", "crashes", 1)).doOnNext(result -> {
                System.out.println(result); // >>> 1
            }).flatMap(v -> reactiveCommands.hincrby("bike:1:stats", "owners", 1)).doOnNext(result -> {
                System.out.println(result); // >>> 1
            }).then();

            incrByGetMget.block();

            Mono<String> getRides = reactiveCommands.hget("bike:1:stats", "rides").doOnNext(result -> {
                System.out.println(result); // >>> 3
            });

            Mono<List<KeyValue<String, String>>> getCrashesOwners = reactiveCommands.hmget("bike:1:stats", "crashes", "owners")
                    .collectList().doOnNext(result -> {
                        System.out.println(result);
                        // >>> [KeyValue[crashes, 1], KeyValue[owners, 1]]
                    });
```

##### Java (Synchronous - Jedis)

```java
      Long res8 = jedis.hincrBy("bike:1:stats", "rides", 1);
      System.out.println(res8); // 1
      Long res9 = jedis.hincrBy("bike:1:stats", "rides", 1);
      System.out.println(res9); // 2
      Long res10 = jedis.hincrBy("bike:1:stats", "rides", 1);
      System.out.println(res10); // 3
      Long res11 = jedis.hincrBy("bike:1:stats", "crashes", 1);
      System.out.println(res11); // 1
      Long res12 = jedis.hincrBy("bike:1:stats", "owners", 1);
      System.out.println(res12); // 1
      String res13 = jedis.hget("bike:1:stats", "rides");
      System.out.println(res13); // 3
      List<String> res14 = jedis.hmget("bike:1:stats", "crashes", "owners");
      System.out.println(res14); // [1, 1]
```

##### JavaScript (Node.js)

```javascript
const res11 = await client.hIncrBy('bike:1:stats', 'rides', 1)
console.log(res11)  // 1
const res12 = await client.hIncrBy('bike:1:stats', 'rides', 1)
console.log(res12)  // 2
const res13 = await client.hIncrBy('bike:1:stats', 'rides', 1)
console.log(res13)  // 3
const res14 = await client.hIncrBy('bike:1:stats', 'crashes', 1)
console.log(res14)  // 1
const res15 = await client.hIncrBy('bike:1:stats', 'owners', 1)
console.log(res15)  // 1
const res16 = await client.hGet('bike:1:stats', 'rides')
console.log(res16)  // 3
const res17 = await client.hmGet('bike:1:stats', ['crashes', 'owners'])
console.log(res17)  // ['1', '1']
```

##### PHP

```php
        $res8 = $r->hincrby('bike:1:stats', 'rides', 1);
        echo $res8 . PHP_EOL;
        // >>> 1

        $res9 = $r->hincrby('bike:1:stats', 'rides', 1);
        echo $res9 . PHP_EOL;
        // >>> 2

        $res10 = $r->hincrby('bike:1:stats', 'rides', 1);
        echo $res10 . PHP_EOL;
        // >>> 3

        $res11 = $r->hincrby('bike:1:stats', 'crashes', 1);
        echo $res11 . PHP_EOL;
        // >>> 1

        $res12 = $r->hincrby('bike:1:stats', 'owners', 1);
        echo $res12 . PHP_EOL;
        // >>> 1

        $res13 = $r->hget('bike:1:stats', 'rides');
        echo $res13 . PHP_EOL;
        // >>> 3

        $res14 = $r->hmget('bike:1:stats', ['crashes', 'owners']);
        echo json_encode($res14) . PHP_EOL;
        // >>> ["1","1"]
```

##### Python

```python
res11 = r.hincrby("bike:1:stats", "rides", 1)
print(res11)
# >>> 1
res12 = r.hincrby("bike:1:stats", "rides", 1)
print(res12)
# >>> 2
res13 = r.hincrby("bike:1:stats", "rides", 1)
print(res13)
# >>> 3
res14 = r.hincrby("bike:1:stats", "crashes", 1)
print(res14)
# >>> 1
res15 = r.hincrby("bike:1:stats", "owners", 1)
print(res15)
# >>> 1
res16 = r.hget("bike:1:stats", "rides")
print(res16)
# >>> 3
res17 = r.hmget("bike:1:stats", ["crashes", "owners"])
print(res17)
# >>> ['1', '1']
```

##### Ruby

```ruby
res8 = r.hincrby('bike:1:stats', 'rides', 1)
puts res8 # >>> 1

res9 = r.hincrby('bike:1:stats', 'rides', 1)
puts res9 # >>> 2

res10 = r.hincrby('bike:1:stats', 'rides', 1)
puts res10 # >>> 3

res11 = r.hincrby('bike:1:stats', 'crashes', 1)
puts res11 # >>> 1

res12 = r.hincrby('bike:1:stats', 'owners', 1)
puts res12 # >>> 1

res13 = r.hget('bike:1:stats', 'rides')
puts res13 # >>> 3

res14 = r.hmget('bike:1:stats', 'owners', 'crashes')
puts res14.inspect # >>> ["1", "1"]
```

##### Rust (Asynchronous)

```rust
        if let Ok(res) = r.hincr("bike:1:stats", "rides", 1).await {
            let res: i32 = res;
            println!("{res}");    // >>> 1
        }

        if let Ok(res) = r.hincr("bike:1:stats", "rides", 1).await {
            let res: i32 = res;
            println!("{res}");    // >>> 2
        }

        if let Ok(res) = r.hincr("bike:1:stats", "rides", 1).await {
            let res: i32 = res;
            println!("{res}");    // >>> 3
        }

        if let Ok(res) = r.hincr("bike:1:stats", "crashes", 1).await {
            let res: i32 = res;
            println!("{res}");    // >>> 1
        }

        if let Ok(res) = r.hincr("bike:1:stats", "owners", 1).await {
            let res: i32 = res;
            println!("{res}");    // >>> 1
        }

        match r.hget("bike:1:stats", "rides").await {
            Ok(res) => {
                let res: i32 = res;
                println!("{res}");   // >>> 3
            },
            Err(e) => {
                println!("Error getting bike:1:stats rides: {e}");
                return;
            }
        };

        match r.hmget("bike:1:stats", &["crashes", "owners"]).await {
            Ok(res) => {
                let res: Vec<i32> = res;
                println!("{res:?}");   // >>> [1, 1]
            },
            Err(e) => {
                println!("Error getting bike:1:stats crashes and owners: {e}");
                return;
            }
        };
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.hincr("bike:1:stats", "rides", 1) {
            let res: i32 = res;
            println!("{res}");    // >>> 1
        }

        if let Ok(res) = r.hincr("bike:1:stats", "rides", 1) {
            let res: i32 = res;
            println!("{res}");    // >>> 2
        }

        if let Ok(res) = r.hincr("bike:1:stats", "rides", 1) {
            let res: i32 = res;
            println!("{res}");    // >>> 3
        }

        if let Ok(res) = r.hincr("bike:1:stats", "crashes", 1) {
            let res: i32 = res;
            println!("{res}");    // >>> 1
        }

        if let Ok(res) = r.hincr("bike:1:stats", "owners", 1) {
            let res: i32 = res;
            println!("{res}");    // >>> 1
        }

        match r.hget("bike:1:stats", "rides") {
            Ok(res) => {
                let res: i32 = res;
                println!("{res}");   // >>> 3
            },
            Err(e) => {
                println!("Error getting bike:1:stats rides: {e}");
                return;
            }
        };

        match r.hmget("bike:1:stats", &["crashes", "owners"]) {
            Ok(res) => {
                let res: Vec<i32> = res;
                println!("{res:?}");   // >>> [1, 1]
            },
            Err(e) => {
                println!("Error getting bike:1:stats crashes and owners: {e}");
                return;
            }
        };
```



## Field expiration

Redis 7.4 introduced the ability to specify an expiration time or a time-to-live (TTL) value for individual hash fields.
This capability is comparable to [key expiration](https://redis.io/docs/latest/develop/using-commands/keyspace#key-expiration) and includes a number of similar commands.

Use the following commands to set either an exact expiration time or a TTL value for specific fields:

* [`HEXPIRE`](https://redis.io/docs/latest/commands/hexpire): set the remaining TTL in seconds.
* [`HPEXPIRE`](https://redis.io/docs/latest/commands/hpexpire): set the remaining TTL in milliseconds.
* [`HEXPIREAT`](https://redis.io/docs/latest/commands/hexpireat): set the expiration time to a timestamp[^1] specified in seconds.
* [`HPEXPIREAT`](https://redis.io/docs/latest/commands/hpexpireat): set the expiration time to a timestamp specified in milliseconds.

[^1]: all timestamps are specified in seconds or milliseconds since the [Unix epoch](https://en.wikipedia.org/wiki/Unix_time).

Use the following commands to retrieve either the exact time when or the remaining TTL until specific fields will expire:

* [`HEXPIRETIME`](https://redis.io/docs/latest/commands/hexpiretime): get the expiration time as a timestamp in seconds.
* [`HPEXPIRETIME`](https://redis.io/docs/latest/commands/hpexpiretime): get the expiration time as a timestamp in milliseconds.
* [`HTTL`](https://redis.io/docs/latest/commands/httl): get the remaining TTL in seconds.
* [`HPTTL`](https://redis.io/docs/latest/commands/hpttl): get the remaining TTL in milliseconds.

Use the following command to remove the expiration of specific fields:

* [`HPERSIST`](https://redis.io/docs/latest/commands/hpersist): remove the expiration.

Redis 8.0 introduced the following commands:

* [`HGETEX`](https://redis.io/docs/latest/commands/hgetex): Get the value of one or more fields of a given hash key and optionally set their expiration time or time-to-live (TTL).
* [`HSETEX`](https://redis.io/docs/latest/commands/hsetex): Set the value of one or more fields of a given hash key and optionally set their expiration time or time-to-live (TTL).

### Common field expiration use cases

1. **Event Tracking**: Use a hash key to store events from the last hour. Set each event's TTL to one hour. Use `HLEN` to count events from the past hour.

1. **Fraud Detection**: Create a hash with hourly counters for events. Set each field's TTL to 48 hours. Query the hash to get the number of events per hour for the last 48 hours.

1. **Customer Session Management**: Store customer data in hash keys. Create a new hash key for each session and add a session field to the customer’s hash key. Expire both the session key and the session field in the customer’s hash key automatically when the session expires.

1. **Active Session Tracking**: Store all active sessions in a hash key. Set each session's TTL to expire automatically after inactivity. Use `HLEN` to count active sessions.

### Field expiration examples

Hash field expiration is supported by the official client libraries. The examples below
demonstrate the field expiration commands using a hash that stores sensor data with the
following structure:

| Field           | Value |
| :-------------- | :---- |
| `air_quality`   | 256   |
| `battery_level` | 89    |

Because the fields expire, each example recreates the `sensor:sensor1` hash first so that
it runs on its own.

Set a TTL of 60 seconds for two fields of a hash and then retrieve the remaining TTL for
those fields:

Field expiration: Set a TTL in seconds on individual hash fields using HEXPIRE, then read the remaining TTL with HTTL

**Difficulty:** Intermediate

**Builds upon:** set_get_all

**Commands:** DEL, HSET, HEXPIRE, HTTL

**Complexity:**
- DEL: O(N)
- HSET: O(1)
- HEXPIRE: O(N)
- HTTL: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> DEL sensor:sensor1
(integer) 0
> HSET sensor:sensor1 air_quality 256 battery_level 89
(integer) 2
> HEXPIRE sensor:sensor1 60 FIELDS 2 air_quality battery_level
1) (integer) 1
2) (integer) 1
> HTTL sensor:sensor1 FIELDS 2 air_quality battery_level
1) (integer) 60
2) (integer) 60
```

##### C#

```csharp
        db.KeyDelete("sensor:sensor1");
        db.HashSet("sensor:sensor1", [
            new("air_quality", 256),
            new("battery_level", 89)
        ]);

        // Set a TTL of 60 seconds on two fields of the hash.
        ExpireResult[] hexpireResult = db.HashFieldExpire(
            "sensor:sensor1",
            new RedisValue[] { "air_quality", "battery_level" },
            TimeSpan.FromSeconds(60)
        );
        Console.WriteLine(string.Join(", ", hexpireResult));
        // Success, Success

        // Retrieve the remaining TTL for those fields.
        long[] httlResult = db.HashFieldGetTimeToLive(
            "sensor:sensor1",
            new RedisValue[] { "air_quality", "battery_level" }
        );
        Console.WriteLine(httlResult.Length);
        // 2
```

##### Go

```go
	rdb.Del(ctx, "sensor:sensor1")
	rdb.HSet(ctx, "sensor:sensor1", "air_quality", 256, "battery_level", 89)

	// Set a TTL of 60 seconds on two fields of the hash.
	res18, err := rdb.HExpire(ctx, "sensor:sensor1", 60*time.Second,
		"air_quality", "battery_level").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res18) // >>> [1 1]

	// Retrieve the remaining TTL for those fields (returns one value per field).
	res19, err := rdb.HTTL(ctx, "sensor:sensor1", "air_quality", "battery_level").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(len(res19)) // >>> 2
```

##### Java (Asynchronous - Lettuce)

```java
            Map<String, String> sensor1 = new HashMap<>();
            sensor1.put("air_quality", "256");
            sensor1.put("battery_level", "89");

            CompletableFuture<Void> hExpire = asyncCommands.del("sensor:sensor1")
                    .thenCompose(delRes -> asyncCommands.hset("sensor:sensor1", sensor1))
                    // Set a TTL of 60 seconds on two fields of the hash.
                    .thenCompose(hsetRes -> asyncCommands.hexpire("sensor:sensor1", 60, "air_quality", "battery_level"))
                    .thenCompose(res15 -> {
                        System.out.println(res15); // >>> [1, 1]
                        // Retrieve the remaining TTL for those fields.
                        return asyncCommands.httl("sensor:sensor1", "air_quality", "battery_level");
                    })
                    .thenAccept(res16 -> System.out.println(res16.size()))
                    // >>> 2
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Map<String, String> sensor1 = new HashMap<>();
            sensor1.put("air_quality", "256");
            sensor1.put("battery_level", "89");

            // Set a TTL of 60 seconds on two fields of the hash.
            Mono<List<Long>> hExpire = reactiveCommands.del("sensor:sensor1")
                    .then(reactiveCommands.hset("sensor:sensor1", sensor1))
                    .then(reactiveCommands.hexpire("sensor:sensor1", 60, "air_quality", "battery_level").collectList())
                    .doOnNext(result -> {
                        System.out.println(result);
                        // >>> [1, 1]
                    });

            hExpire.block();

            // Retrieve the remaining TTL for those fields.
            Mono<List<Long>> hTtl = reactiveCommands.httl("sensor:sensor1", "air_quality", "battery_level")
                    .collectList().doOnNext(result -> {
                        System.out.println(result.size());
                        // >>> 2
                    });

            hTtl.block();
```

##### Java (Synchronous - Jedis)

```java
      jedis.del("sensor:sensor1");
      Map<String, String> sensor1 = new HashMap<>();
      sensor1.put("air_quality", "256");
      sensor1.put("battery_level", "89");
      jedis.hset("sensor:sensor1", sensor1);

      // Set a TTL of 60 seconds on two fields of the hash.
      List<Long> res15 = jedis.hexpire("sensor:sensor1", 60, "air_quality", "battery_level");
      System.out.println(res15); // [1, 1]

      // Retrieve the remaining TTL for those fields.
      List<Long> res16 = jedis.httl("sensor:sensor1", "air_quality", "battery_level");
      System.out.println(res16.size()); // 2
```

##### JavaScript (Node.js)

```javascript
await client.del('sensor:sensor1')
await client.hSet('sensor:sensor1', { 'air_quality': 256, 'battery_level': 89 })

// Set a TTL of 60 seconds on two fields of the hash.
const res18 = await client.hExpire('sensor:sensor1', ['air_quality', 'battery_level'], 60)
console.log(res18)  // [1, 1]

// Retrieve the remaining TTL for those fields.
const res19 = await client.hTTL('sensor:sensor1', ['air_quality', 'battery_level'])
console.log(res19)  // [60, 60] (or close to 60)
```

##### PHP

```php
        $r->del('sensor:sensor1');
        $r->hmset('sensor:sensor1', [
            'air_quality' => 256,
            'battery_level' => 89,
        ]);

        // Set a TTL of 60 seconds on two fields of the hash.
        $res15 = $r->hexpire('sensor:sensor1', 60, ['air_quality', 'battery_level']);
        echo json_encode($res15) . PHP_EOL;
        // >>> [1,1]

        // Retrieve the remaining TTL for those fields.
        $res16 = $r->httl('sensor:sensor1', ['air_quality', 'battery_level']);
        echo count($res16) . PHP_EOL;
        // >>> 2
```

##### Python

```python
r.delete("sensor:sensor1")
r.hset("sensor:sensor1", mapping={"air_quality": 256, "battery_level": 89})

# Set a TTL of 60 seconds on two fields of the hash.
res18 = r.hexpire("sensor:sensor1", 60, "air_quality", "battery_level")
print(res18)
# >>> [1, 1]

# Retrieve the remaining TTL for those fields.
res19 = r.httl("sensor:sensor1", "air_quality", "battery_level")
print(res19)
# >>> [60, 60]
# (your actual values may be slightly lower)
```

##### Ruby

```ruby
r.del('sensor:sensor1')
r.hset('sensor:sensor1', { 'air_quality' => 256, 'battery_level' => 89 })

# Set a TTL of 60 seconds on two fields of the hash.
res15 = r.hexpire('sensor:sensor1', 60, 'air_quality', 'battery_level')
puts res15.inspect # >>> [1, 1]

# Retrieve the remaining TTL for those fields.
res16 = r.httl('sensor:sensor1', 'air_quality', 'battery_level')
puts res16.inspect # >>> [60, 60]
# (your actual values may be slightly lower)
```

##### Rust (Asynchronous)

```rust
        let _: () = r.del("sensor:sensor1").await.expect("Failed to del");
        let _: () = r.hset_multiple(
            "sensor:sensor1",
            &[("air_quality", "256"), ("battery_level", "89")],
        ).await.expect("Failed to hset");

        // Set a TTL of 60 seconds on two fields of the hash.
        match r.hexpire("sensor:sensor1", 60, redis::ExpireOption::NONE, &["air_quality", "battery_level"]).await {
            Ok(res18) => {
                let res18: Vec<i64> = res18;
                println!("{:?}", res18);    // >>> [1, 1]
            },
            Err(e) => {
                println!("Error setting expiration: {e}");
                return;
            }
        }

        // Retrieve the remaining TTL for those fields.
        match r.httl("sensor:sensor1", &["air_quality", "battery_level"]).await {
            Ok(res19) => {
                let res19: Vec<i64> = res19;
                println!("{}", res19.len());    // >>> 2
            },
            Err(e) => {
                println!("Error getting TTL: {e}");
                return;
            }
        }
```

##### Rust (Synchronous)

```rust
        let _: () = r.del("sensor:sensor1").expect("Failed to del");
        let _: () = r.hset_multiple(
            "sensor:sensor1",
            &[("air_quality", "256"), ("battery_level", "89")],
        ).expect("Failed to hset");

        // Set a TTL of 60 seconds on two fields of the hash.
        match r.hexpire("sensor:sensor1", 60, redis::ExpireOption::NONE, &["air_quality", "battery_level"]) {
            Ok(res18) => {
                let res18: Vec<i64> = res18;
                println!("{:?}", res18);    // >>> [1, 1]
            },
            Err(e) => {
                println!("Error setting expiration: {e}");
                return;
            }
        }

        // Retrieve the remaining TTL for those fields.
        match r.httl("sensor:sensor1", &["air_quality", "battery_level"]) {
            Ok(res19) => {
                let res19: Vec<i64> = res19;
                println!("{}", res19.len());    // >>> 2
            },
            Err(e) => {
                println!("Error getting TTL: {e}");
                return;
            }
        }
```



Set a hash field's TTL in milliseconds and then retrieve the remaining TTL in milliseconds:

Field expiration: Set a TTL in milliseconds on a hash field using HPEXPIRE, then read the remaining TTL with HPTTL

**Difficulty:** Intermediate

**Builds upon:** set_get_all

**Commands:** DEL, HSET, HPEXPIRE, HPTTL

**Complexity:**
- DEL: O(N)
- HSET: O(1)
- HPEXPIRE: O(N)
- HPTTL: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> DEL sensor:sensor1
(integer) 1
> HSET sensor:sensor1 air_quality 256 battery_level 89
(integer) 2
> HPEXPIRE sensor:sensor1 60000 FIELDS 1 air_quality
1) (integer) 1
> HPTTL sensor:sensor1 FIELDS 1 air_quality
1) (integer) 59994
```

##### C#

```csharp
        db.KeyDelete("sensor:sensor1");
        db.HashSet("sensor:sensor1", [
            new("air_quality", 256),
            new("battery_level", 89)
        ]);

        // Set the TTL of the 'air_quality' field, expressed in milliseconds.
        ExpireResult[] hpexpireResult = db.HashFieldExpire(
            "sensor:sensor1",
            new RedisValue[] { "air_quality" },
            TimeSpan.FromMilliseconds(60000)
        );
        Console.WriteLine(string.Join(", ", hpexpireResult));
        // Success

        // Retrieve the remaining TTL.
        long[] hpttlResult = db.HashFieldGetTimeToLive(
            "sensor:sensor1",
            new RedisValue[] { "air_quality" }
        );
        Console.WriteLine(hpttlResult.Length);
        // 1
```

##### Go

```go
	rdb.Del(ctx, "sensor:sensor1")
	rdb.HSet(ctx, "sensor:sensor1", "air_quality", 256, "battery_level", 89)

	// Set the TTL of the 'air_quality' field in milliseconds.
	res20, err := rdb.HPExpire(ctx, "sensor:sensor1", 60000*time.Millisecond,
		"air_quality").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res20) // >>> [1]

	// Retrieve the remaining TTL in milliseconds (returns one value per field).
	res21, err := rdb.HPTTL(ctx, "sensor:sensor1", "air_quality").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(len(res21)) // >>> 1
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> hpExpire = hExpire
                    .thenCompose(prev -> asyncCommands.del("sensor:sensor1"))
                    .thenCompose(delRes -> asyncCommands.hset("sensor:sensor1", sensor1))
                    // Set the TTL of the 'air_quality' field in milliseconds.
                    .thenCompose(hsetRes -> asyncCommands.hpexpire("sensor:sensor1", 60000, "air_quality"))
                    .thenCompose(res17 -> {
                        System.out.println(res17); // >>> [1]
                        // Retrieve the remaining TTL in milliseconds.
                        return asyncCommands.hpttl("sensor:sensor1", "air_quality");
                    })
                    .thenAccept(res18 -> System.out.println(res18.size()))
                    // >>> 1
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            // Set the TTL of the 'air_quality' field in milliseconds.
            Mono<List<Long>> hpExpire = reactiveCommands.del("sensor:sensor1")
                    .then(reactiveCommands.hset("sensor:sensor1", sensor1))
                    .then(reactiveCommands.hpexpire("sensor:sensor1", 60000, "air_quality").collectList())
                    .doOnNext(result -> {
                        System.out.println(result);
                        // >>> [1]
                    });

            hpExpire.block();

            // Retrieve the remaining TTL in milliseconds.
            Mono<List<Long>> hpTtl = reactiveCommands.hpttl("sensor:sensor1", "air_quality")
                    .collectList().doOnNext(result -> {
                        System.out.println(result.size());
                        // >>> 1
                    });

            hpTtl.block();
```

##### Java (Synchronous - Jedis)

```java
      jedis.del("sensor:sensor1");
      jedis.hset("sensor:sensor1", sensor1);

      // Set the TTL of the 'air_quality' field in milliseconds.
      List<Long> res17 = jedis.hpexpire("sensor:sensor1", 60000, "air_quality");
      System.out.println(res17); // [1]

      // Retrieve the remaining TTL in milliseconds.
      List<Long> res18 = jedis.hpttl("sensor:sensor1", "air_quality");
      System.out.println(res18.size()); // 1
```

##### JavaScript (Node.js)

```javascript
await client.del('sensor:sensor1')
await client.hSet('sensor:sensor1', { 'air_quality': 256, 'battery_level': 89 })

// Set the TTL of the 'air_quality' field in milliseconds.
const res20 = await client.hpExpire('sensor:sensor1', ['air_quality'], 60000)
console.log(res20)  // [1]

// Retrieve the remaining TTL in milliseconds.
const res21 = await client.hpTTL('sensor:sensor1', ['air_quality'])
console.log(res21)  // [59994] (your actual value may vary)
```

##### PHP

```php
        $r->del('sensor:sensor1');
        $r->hmset('sensor:sensor1', [
            'air_quality' => 256,
            'battery_level' => 89,
        ]);

        // Set the TTL of the 'air_quality' field in milliseconds.
        $res17 = $r->hpexpire('sensor:sensor1', 60000, ['air_quality']);
        echo json_encode($res17) . PHP_EOL;
        // >>> [1]

        // Retrieve the remaining TTL in milliseconds.
        $res18 = $r->hpttl('sensor:sensor1', ['air_quality']);
        echo count($res18) . PHP_EOL;
        // >>> 1
```

##### Python

```python
r.delete("sensor:sensor1")
r.hset("sensor:sensor1", mapping={"air_quality": 256, "battery_level": 89})

# Set the TTL of the 'air_quality' field in milliseconds.
res20 = r.hpexpire("sensor:sensor1", 60000, "air_quality")
print(res20)
# >>> [1]

# Retrieve the remaining TTL in milliseconds.
res21 = r.hpttl("sensor:sensor1", "air_quality")
print(res21)
# >>> [59994]
# (your actual value may vary)
```

##### Ruby

```ruby
r.del('sensor:sensor1')
r.hset('sensor:sensor1', { 'air_quality' => 256, 'battery_level' => 89 })

# Set the TTL of the 'air_quality' field in milliseconds.
res17 = r.hpexpire('sensor:sensor1', 60_000, 'air_quality')
puts res17.inspect # >>> [1]

# Retrieve the remaining TTL in milliseconds.
res18 = r.hpttl('sensor:sensor1', 'air_quality')
puts res18.inspect # >>> [59999]
# (your actual value may vary)
```

##### Rust (Asynchronous)

```rust
        let _: () = r.del("sensor:sensor1").await.expect("Failed to del");
        let _: () = r.hset_multiple(
            "sensor:sensor1",
            &[("air_quality", "256"), ("battery_level", "89")],
        ).await.expect("Failed to hset");

        // Set the TTL of the 'air_quality' field in milliseconds.
        match r.hpexpire("sensor:sensor1", 60000, redis::ExpireOption::NONE, &["air_quality"]).await {
            Ok(res20) => {
                let res20: Vec<i64> = res20;
                println!("{:?}", res20);    // >>> [1]
            },
            Err(e) => {
                println!("Error setting expiration: {e}");
                return;
            }
        }

        // Retrieve the remaining TTL in milliseconds.
        match r.hpttl("sensor:sensor1", &["air_quality"]).await {
            Ok(res21) => {
                let res21: Vec<i64> = res21;
                println!("{}", res21.len());    // >>> 1
            },
            Err(e) => {
                println!("Error getting PTTL: {e}");
                return;
            }
        }
```

##### Rust (Synchronous)

```rust
        let _: () = r.del("sensor:sensor1").expect("Failed to del");
        let _: () = r.hset_multiple(
            "sensor:sensor1",
            &[("air_quality", "256"), ("battery_level", "89")],
        ).expect("Failed to hset");

        // Set the TTL of the 'air_quality' field in milliseconds.
        match r.hpexpire("sensor:sensor1", 60000, redis::ExpireOption::NONE, &["air_quality"]) {
            Ok(res20) => {
                let res20: Vec<i64> = res20;
                println!("{:?}", res20);    // >>> [1]
            },
            Err(e) => {
                println!("Error setting expiration: {e}");
                return;
            }
        }

        // Retrieve the remaining TTL in milliseconds.
        match r.hpttl("sensor:sensor1", &["air_quality"]) {
            Ok(res21) => {
                let res21: Vec<i64> = res21;
                println!("{}", res21.len());    // >>> 1
            },
            Err(e) => {
                println!("Error getting PTTL: {e}");
                return;
            }
        }
```



Set a hash field's expiration to a specific timestamp and then retrieve that expiration
time (both as a Unix time in seconds):

Field expiration: Set an absolute expiration timestamp on a hash field using HEXPIREAT, then read it back with HEXPIRETIME

**Difficulty:** Intermediate

**Builds upon:** set_get_all

**Commands:** DEL, HSET, HEXPIREAT, HEXPIRETIME

**Complexity:**
- DEL: O(N)
- HSET: O(1)
- HEXPIREAT: O(N)
- HEXPIRETIME: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> DEL sensor:sensor1
(integer) 1
> HSET sensor:sensor1 air_quality 256 battery_level 89
(integer) 2
# Set the expiration to a Unix time in the future
# (4102444800 is just an example; use a timestamp appropriate for your use case).
> HEXPIREAT sensor:sensor1 4102444800 FIELDS 1 air_quality
1) (integer) 1
> HEXPIRETIME sensor:sensor1 FIELDS 1 air_quality
1) (integer) 4102444800
```

##### C#

```csharp
        db.KeyDelete("sensor:sensor1");
        db.HashSet("sensor:sensor1", [
            new("air_quality", 256),
            new("battery_level", 89)
        ]);

        // Set the expiration of 'air_quality' to a time 24 hours from now.
        ExpireResult[] hexpireAtResult = db.HashFieldExpire(
            "sensor:sensor1",
            new RedisValue[] { "air_quality" },
            DateTime.UtcNow.AddHours(24)
        );
        Console.WriteLine(string.Join(", ", hexpireAtResult));
        // Success

        // Retrieve the expiration time as a Unix timestamp.
        long[] hexpireTimeResult = db.HashFieldGetExpireDateTime(
            "sensor:sensor1",
            new RedisValue[] { "air_quality" }
        );
        Console.WriteLine(hexpireTimeResult.Length);
        // 1
```

##### Go

```go
	rdb.Del(ctx, "sensor:sensor1")
	rdb.HSet(ctx, "sensor:sensor1", "air_quality", 256, "battery_level", 89)

	// Set the expiration of 'air_quality' to a time 24 hours from now.
	res22, err := rdb.HExpireAt(ctx, "sensor:sensor1", time.Now().Add(24*time.Hour),
		"air_quality").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res22) // >>> [1]

	// Retrieve the expiration time as a Unix timestamp (returns one value per field).
	res23, err := rdb.HExpireTime(ctx, "sensor:sensor1", "air_quality").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(len(res23)) // >>> 1
```

##### Java (Asynchronous - Lettuce)

```java
            long expireAtSeconds = System.currentTimeMillis() / 1000L + 24 * 60 * 60;
            CompletableFuture<Void> hExpireAt = hpExpire
                    .thenCompose(prev -> asyncCommands.del("sensor:sensor1"))
                    .thenCompose(delRes -> asyncCommands.hset("sensor:sensor1", sensor1))
                    // Set the expiration of 'air_quality' to a Unix time 24 hours from now.
                    .thenCompose(hsetRes -> asyncCommands.hexpireat("sensor:sensor1", expireAtSeconds, "air_quality"))
                    .thenCompose(res19 -> {
                        System.out.println(res19); // >>> [1]
                        // Retrieve the expiration time as a Unix timestamp in seconds.
                        return asyncCommands.hexpiretime("sensor:sensor1", "air_quality");
                    })
                    .thenAccept(res20 -> System.out.println(res20.size()))
                    // >>> 1
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            long expireAtSeconds = System.currentTimeMillis() / 1000L + 24 * 60 * 60;

            // Set the expiration of 'air_quality' to a Unix time 24 hours from now.
            Mono<List<Long>> hExpireAt = reactiveCommands.del("sensor:sensor1")
                    .then(reactiveCommands.hset("sensor:sensor1", sensor1))
                    .then(reactiveCommands.hexpireat("sensor:sensor1", expireAtSeconds, "air_quality").collectList())
                    .doOnNext(result -> {
                        System.out.println(result);
                        // >>> [1]
                    });

            hExpireAt.block();

            // Retrieve the expiration time as a Unix timestamp in seconds.
            Mono<List<Long>> hExpireTime = reactiveCommands.hexpiretime("sensor:sensor1", "air_quality")
                    .collectList().doOnNext(result -> {
                        System.out.println(result.size());
                        // >>> 1
                    });

            hExpireTime.block();
```

##### Java (Synchronous - Jedis)

```java
      jedis.del("sensor:sensor1");
      jedis.hset("sensor:sensor1", sensor1);

      // Set the expiration of 'air_quality' to a Unix time 24 hours from now.
      long expireAt = System.currentTimeMillis() / 1000L + 24 * 60 * 60;
      List<Long> res19 = jedis.hexpireAt("sensor:sensor1", expireAt, "air_quality");
      System.out.println(res19); // [1]

      // Retrieve the expiration time as a Unix timestamp in seconds.
      List<Long> res20 = jedis.hexpireTime("sensor:sensor1", "air_quality");
      System.out.println(res20.size()); // 1
```

##### JavaScript (Node.js)

```javascript
await client.del('sensor:sensor1')
await client.hSet('sensor:sensor1', { 'air_quality': 256, 'battery_level': 89 })

// Set the expiration of 'air_quality' to a Unix time 24 hours from now.
const expireAt = Math.floor(Date.now() / 1000) + 24 * 60 * 60
const res22 = await client.hExpireAt('sensor:sensor1', ['air_quality'], expireAt)
console.log(res22)  // [1]

// Retrieve the expiration time as a Unix timestamp in seconds.
const res23 = await client.hExpireTime('sensor:sensor1', ['air_quality'])
console.log(res23)  // [1717668041] (your actual value will vary)
```

##### PHP

```php
        $r->del('sensor:sensor1');
        $r->hmset('sensor:sensor1', [
            'air_quality' => 256,
            'battery_level' => 89,
        ]);

        // Set the expiration of 'air_quality' to a Unix time 24 hours from now.
        $res19 = $r->hexpireat('sensor:sensor1', time() + 24 * 60 * 60, ['air_quality']);
        echo json_encode($res19) . PHP_EOL;
        // >>> [1]

        // Retrieve the expiration time as a Unix timestamp in seconds.
        $res20 = $r->hexpiretime('sensor:sensor1', ['air_quality']);
        echo count($res20) . PHP_EOL;
        // >>> 1
```

##### Python

```python
r.delete("sensor:sensor1")
r.hset("sensor:sensor1", mapping={"air_quality": 256, "battery_level": 89})

# Set the expiration of 'air_quality' to a Unix time 24 hours from now.
res22 = r.hexpireat(
    "sensor:sensor1",
    int(time.time()) + 24 * 60 * 60,
    "air_quality",
)
print(res22)
# >>> [1]

# Retrieve the expiration time as a Unix timestamp in seconds.
res23 = r.hexpiretime("sensor:sensor1", "air_quality")
print(res23)
# >>> [1717668041]
# (your actual value will vary)
```

##### Rust (Asynchronous)

```rust
        let _: () = r.del("sensor:sensor1").await.expect("Failed to del");
        let _: () = r.hset_multiple(
            "sensor:sensor1",
            &[("air_quality", "256"), ("battery_level", "89")],
        ).await.expect("Failed to hset");

        // Set the expiration of 'air_quality' to a Unix time 24 hours from now.
        let now = std::time::SystemTime::now()
            .duration_since(std::time::UNIX_EPOCH)
            .expect("Time went backwards")
            .as_secs() as i64;

        match r.hexpire_at("sensor:sensor1", now + 24 * 60 * 60, redis::ExpireOption::NONE, &["air_quality"]).await {
            Ok(res22) => {
                let res22: Vec<i64> = res22;
                println!("{:?}", res22);    // >>> [1]
            },
            Err(e) => {
                println!("Error setting expiration: {e}");
                return;
            }
        }

        // Retrieve the expiration time as a Unix timestamp in seconds.
        match r.hexpire_time("sensor:sensor1", &["air_quality"]).await {
            Ok(res23) => {
                let res23: Vec<i64> = res23;
                println!("{}", res23.len());    // >>> 1
            },
            Err(e) => {
                println!("Error getting expiration time: {e}");
                return;
            }
        }
```

##### Rust (Synchronous)

```rust
        let _: () = r.del("sensor:sensor1").expect("Failed to del");
        let _: () = r.hset_multiple(
            "sensor:sensor1",
            &[("air_quality", "256"), ("battery_level", "89")],
        ).expect("Failed to hset");

        // Set the expiration of 'air_quality' to a Unix time 24 hours from now.
        let now = std::time::SystemTime::now()
            .duration_since(std::time::UNIX_EPOCH)
            .expect("Time went backwards")
            .as_secs() as i64;

        match r.hexpire_at("sensor:sensor1", now + 24 * 60 * 60, redis::ExpireOption::NONE, &["air_quality"]) {
            Ok(res22) => {
                let res22: Vec<i64> = res22;
                println!("{:?}", res22);    // >>> [1]
            },
            Err(e) => {
                println!("Error setting expiration: {e}");
                return;
            }
        }

        // Retrieve the expiration time as a Unix timestamp in seconds.
        match r.hexpire_time("sensor:sensor1", &["air_quality"]) {
            Ok(res23) => {
                let res23: Vec<i64> = res23;
                println!("{}", res23.len());    // >>> 1
            },
            Err(e) => {
                println!("Error getting expiration time: {e}");
                return;
            }
        }
```



## Compact hashes

Redis 8.10 introduced *compact hashes*, a way to reduce the memory used by hashes that share the same field names. When many hashes have the same layout (for example, one hash per user, each with `name`, `email`, and `age`), Redis can store the shared set of field names once and keep only the values, plus a small reference to that set, in each key. This is an internal encoding: existing hash commands keep working exactly as before, with the same semantics and replies. The hash just uses less memory.

**Compact hashes work well when:**

- Many keys share the same, mostly stable set of field names — classic object mapping, such as one hash per user, order, or session. The more keys that share a field set, the greater the memory saving.
- Reads and value updates stay as fast as on a regular hash. Reading any field (for example, [`HGET`](https://redis.io/docs/latest/commands/hget), [`HGETALL`](https://redis.io/docs/latest/commands/hgetall), or [`HRANDFIELD`](https://redis.io/docs/latest/commands/hrandfield)) and overwriting an existing field's value (`HSET key field value` where `field` already exists) are unaffected.

**Compact hashes are not a good fit when:**

- **Field names change often.** Adding a new field with [`HSET`](https://redis.io/docs/latest/commands/hset) or removing one with [`HDEL`](https://redis.io/docs/latest/commands/hdel) detaches the key from its shared field-name set and re-resolves it against the new set, creating a new one if that layout hasn't been seen before. A workload that constantly adds or removes field names erodes the benefit. Note also that once a hash becomes a compact hash, it stays one for the life of the key: it moves between field-name sets as its fields change, but never reverts to a plain hash.
- **Field names are unique or highly dynamic per key.** With little sharing, a key ends up with its own field-name set, which carries some metadata overhead. A set used by only a few keys can therefore consume more memory than a plain hash. Compact hashes pay off when hundreds or thousands of keys share a set.
- **Hashes are very large.** Because a compact hash is transferred as a single blob during replication and slot migration, very large hash keys may reduce or negate the benefit.

There are two ways to opt in.

### Bulk import with HIMPORT

The [`HIMPORT`](https://redis.io/docs/latest/commands/himport) command family lets a client import many hashes that share the same field names efficiently. You declare the shared field names once with [`HIMPORT PREPARE`](https://redis.io/docs/latest/commands/himport-prepare), then create each key with [`HIMPORT SET`](https://redis.io/docs/latest/commands/himport-set) by sending only its values. This reduces network traffic and per-command work compared with running [`HSET`](https://redis.io/docs/latest/commands/hset) once per key, and hints Redis to store the new keys as compact hashes. See [`HIMPORT`](https://redis.io/docs/latest/commands/himport) for the full workflow and its subcommands.

Foundational: Declare shared field names once with HIMPORT PREPARE, then create each hash by sending only its values with HIMPORT SET

**Difficulty:** Intermediate

**Commands:** HIMPORT, HGETALL

**Complexity:**
- HIMPORT: Depends on subcommand
- HGETALL: O(N)

**Available in:** Redis CLI, C#, C#, Go, Java, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), JavaScript (Node.js), PHP, Python, Ruby

##### Redis CLI

```
> HIMPORT PREPARE user name email age
OK
> HIMPORT SET user:1 user Alice alice@example.com 34
OK
> HIMPORT SET user:2 user Bob bob@example.com 41
OK
> HIMPORT SET user:3 user Carol carol@example.com 29
OK
> HGETALL user:2
1) "age"
2) "41"
3) "name"
4) "Bob"
5) "email"
6) "bob@example.com"
```

##### C#

```csharp
        // Declare the field names once.
        await using var fields = HashImport.Create("name", "email", "age");

        // Create each hash by sending only its values.
        await db.HashImportAsync("user:1", fields, new RedisValue[] { "Alice", "alice@example.com", "34" });
        await db.HashImportAsync("user:2", fields, new RedisValue[] { "Bob", "bob@example.com", "41" });
        await db.HashImportAsync("user:3", fields, new RedisValue[] { "Carol", "carol@example.com", "29" });

        // The result is an ordinary hash.
        HashEntry[] res1 = await db.HashGetAllAsync("user:2");
        Console.WriteLine(string.Join(", ", res1.Select(h => $"{h.Name}: {h.Value}")));
        // >>> age: 41, name: Bob, email: bob@example.com
```

##### C#

```csharp
        // Declare the field names once.
        using var fields = HashImport.Create("name", "email", "age");

        // Create each hash by sending only its values.
        db.HashImport("user:1", fields, new RedisValue[] { "Alice", "alice@example.com", "34" });
        db.HashImport("user:2", fields, new RedisValue[] { "Bob", "bob@example.com", "41" });
        db.HashImport("user:3", fields, new RedisValue[] { "Carol", "carol@example.com", "29" });

        // The result is an ordinary hash.
        HashEntry[] res1 = db.HashGetAll("user:2");
        Console.WriteLine(string.Join(", ", res1.Select(h => $"{h.Name}: {h.Value}")));
        // >>> age: 41, name: Bob, email: bob@example.com
```

##### C#

```csharp
        // Declare the field names once.
        await using var fields = HashImport.Create("name", "email", "age");

        // Create each hash by sending only its values.
        await db.HashImportAsync("user:1", fields, new RedisValue[] { "Alice", "alice@example.com", "34" });
        await db.HashImportAsync("user:2", fields, new RedisValue[] { "Bob", "bob@example.com", "41" });
        await db.HashImportAsync("user:3", fields, new RedisValue[] { "Carol", "carol@example.com", "29" });

        // The result is an ordinary hash.
        HashEntry[] res1 = await db.HashGetAllAsync("user:2");
        Console.WriteLine(string.Join(", ", res1.Select(h => $"{h.Name}: {h.Value}")));
        // >>> age: 41, name: Bob, email: bob@example.com
```

##### C#

```csharp
        // Declare the field names once.
        using var fields = HashImport.Create("name", "email", "age");

        // Create each hash by sending only its values.
        db.HashImport("user:1", fields, new RedisValue[] { "Alice", "alice@example.com", "34" });
        db.HashImport("user:2", fields, new RedisValue[] { "Bob", "bob@example.com", "41" });
        db.HashImport("user:3", fields, new RedisValue[] { "Carol", "carol@example.com", "29" });

        // The result is an ordinary hash.
        HashEntry[] res1 = db.HashGetAll("user:2");
        Console.WriteLine(string.Join(", ", res1.Select(h => $"{h.Name}: {h.Value}")));
        // >>> age: 41, name: Bob, email: bob@example.com
```

##### Go

```go
	// Declare the field names once.
	if err := rdb.HImportPrepare(ctx, "user", "name", "email", "age").Err(); err != nil {
		panic(err)
	}

	// Create each hash by sending only its values.
	res1, err := rdb.HImportSet(ctx, "user:1", "user", "Alice", "alice@example.com", "34").Result()
	if err != nil {
		panic(err)
	}
	fmt.Println(res1) // >>> OK

	if err := rdb.HImportSet(ctx, "user:2", "user", "Bob", "bob@example.com", "41").Err(); err != nil {
		panic(err)
	}
	if err := rdb.HImportSet(ctx, "user:3", "user", "Carol", "carol@example.com", "29").Err(); err != nil {
		panic(err)
	}

	// The result is an ordinary hash.
	res2, err := rdb.HGetAll(ctx, "user:2").Result()
	if err != nil {
		panic(err)
	}
	fmt.Println(res2) // >>> map[age:41 email:bob@example.com name:Bob]
```

##### Java

```java
            // Declare the field names once.
            try (HashImport<String> fieldset = HashImport.of("name", "email", "age")) {
                // Create each hash by sending only its values.
                String res1 = syncCommands.himportSet("user:1", fieldset, "Alice", "alice@example.com", "34");
                System.out.println(res1); // >>> OK

                syncCommands.himportSet("user:2", fieldset, "Bob", "bob@example.com", "41");
                syncCommands.himportSet("user:3", fieldset, "Carol", "carol@example.com", "29");
            }

            // The result is an ordinary hash.
            Map<String, String> res2 = syncCommands.hgetall("user:2");
            System.out.println(res2);
            // >>> {age=41, name=Bob, email=bob@example.com}
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> basicOps;

            // Declare the field names once.
            try (HashImport<String> fieldset = HashImport.of("name", "email", "age")) {
                // Create each hash by sending only its values.
                RedisFuture<String> import1 = asyncCommands.himportSet(
                        "user:1", fieldset, "Alice", "alice@example.com", "34");
                asyncCommands.himportSet("user:2", fieldset, "Bob", "bob@example.com", "41");
                asyncCommands.himportSet("user:3", fieldset, "Carol", "carol@example.com", "29");

                basicOps = import1.thenCompose(res1 -> {
                    System.out.println(res1); // >>> OK
                    // The result is an ordinary hash.
                    return asyncCommands.hgetall("user:2");
                }).thenAccept(res2 -> {
                    System.out.println(res2);
                    // >>> {age=41, name=Bob, email=bob@example.com}
                }).toCompletableFuture();
            }

            basicOps.join();
```

##### Java (Reactive - Lettuce)

```java
            // Declare the field names once.
            try (HashImport<String> fieldset = HashImport.of("name", "email", "age")) {
                // Create each hash by sending only its values.
                Mono<String> import1 = reactiveCommands
                    .himportSet("user:1", fieldset, "Alice", "alice@example.com", "34")
                    .doOnNext(res1 -> {
                        System.out.println(res1); // >>> OK
                    });

                Mono<String> import2 = reactiveCommands
                    .himportSet("user:2", fieldset, "Bob", "bob@example.com", "41");
                Mono<String> import3 = reactiveCommands
                    .himportSet("user:3", fieldset, "Carol", "carol@example.com", "29");

                // Subscribe before the fieldset closes.
                Mono.when(import1, import2, import3).block();
            }

            // The result is an ordinary hash.
            Mono<List<KeyValue<String, String>>> getAll = reactiveCommands.hgetall("user:2")
                .collectList()
                .doOnNext(res2 -> {
                    System.out.println(res2);
                    // >>> [KeyValue[age, 41], KeyValue[name, Bob], KeyValue[email, bob@example.com]]
                });

            getAll.block();
```

##### Java (Synchronous - Jedis)

```java
        // Declare the field names once.
        try (HashImport fields = HashImport.of("name", "email", "age")) {
            // Create each hash by sending only its values.
            String res1 = jedis.himportSet("user:1", fields, "Alice", "alice@example.com", "34");
            System.out.println(res1); // >>> OK

            jedis.himportSet("user:2", fields, "Bob", "bob@example.com", "41");
            jedis.himportSet("user:3", fields, "Carol", "carol@example.com", "29");
        }

        // The result is an ordinary hash.
        Map<String, String> res2 = jedis.hgetAll("user:2");
        System.out.println(res2);
        // >>> {name=Bob, age=41, email=bob@example.com}
```

##### JavaScript (Node.js)

```javascript
// Declare the field names once.
await client.hImportPrepare('user', ['name', 'email', 'age']);

// Create each hash by sending only its values.
const res1 = await client.hImportSet('user:1', 'user', ['Alice', 'alice@example.com', '34']);
console.log(res1); // >>> OK

await client.hImportSet('user:2', 'user', ['Bob', 'bob@example.com', '41']);
await client.hImportSet('user:3', 'user', ['Carol', 'carol@example.com', '29']);

// The result is an ordinary hash.
const res2 = await client.hGetAll('user:2');
console.log(res2);
// >>> { age: '41', name: 'Bob', email: 'bob@example.com' }
```

##### JavaScript (Node.js)

```javascript
// Declare the field names once, when you create the client.
const redis = new Redis({
  himportFieldsets: [{ name: 'user', fields: ['name', 'email', 'age'] }],
});

// Create each hash by sending only its values.
const res1 = await redis.himport('SET', 'user:1', 'user', 'Alice', 'alice@example.com', '34');
console.log(res1); // >>> OK

await redis.himport('SET', 'user:2', 'user', 'Bob', 'bob@example.com', '41');
await redis.himport('SET', 'user:3', 'user', 'Carol', 'carol@example.com', '29');

// The result is an ordinary hash.
const res2 = await redis.hgetall('user:2');
console.log(res2);
// >>> { age: '41', name: 'Bob', email: 'bob@example.com' }
```

##### JavaScript (Node.js)

```javascript
// Declare the field names once.
await client.hImportPrepare('user', ['name', 'email', 'age']);

// Create each hash by sending only its values.
const res1 = await client.hImportSet('user:1', 'user', ['Alice', 'alice@example.com', '34']);
console.log(res1); // >>> OK

await client.hImportSet('user:2', 'user', ['Bob', 'bob@example.com', '41']);
await client.hImportSet('user:3', 'user', ['Carol', 'carol@example.com', '29']);

// The result is an ordinary hash.
const res2 = await client.hGetAll('user:2');
console.log(res2);
// >>> { age: '41', name: 'Bob', email: 'bob@example.com' }
```

##### JavaScript (Node.js)

```javascript
// Declare the field names once, when you create the client.
const redis = new Redis({
  himportFieldsets: [{ name: 'user', fields: ['name', 'email', 'age'] }],
});

// Create each hash by sending only its values.
const res1 = await redis.himport('SET', 'user:1', 'user', 'Alice', 'alice@example.com', '34');
console.log(res1); // >>> OK

await redis.himport('SET', 'user:2', 'user', 'Bob', 'bob@example.com', '41');
await redis.himport('SET', 'user:3', 'user', 'Carol', 'carol@example.com', '29');

// The result is an ordinary hash.
const res2 = await redis.hgetall('user:2');
console.log(res2);
// >>> { age: '41', name: 'Bob', email: 'bob@example.com' }
```

##### PHP

```php
        // Declare the field names once.
        $r->himport->prepare('user', ['name', 'email', 'age']);

        // Create each hash by sending only its values.
        $res1 = $r->himport->set('user:1', 'user', ['Alice', 'alice@example.com', '34']);
        echo $res1 . PHP_EOL; // >>> OK

        $r->himport->set('user:2', 'user', ['Bob', 'bob@example.com', '41']);
        $r->himport->set('user:3', 'user', ['Carol', 'carol@example.com', '29']);

        // The result is an ordinary hash.
        $res2 = $r->hgetall('user:2');
        echo json_encode($res2) . PHP_EOL;
        // >>> {"age":"41","name":"Bob","email":"bob@example.com"}
```

##### Python

```python
# Declare the field names once.
r.himport_prepare("user", ["name", "email", "age"])

# Create each hash by sending only its values.
res1 = r.himport_set("user:1", "user", ["Alice", "alice@example.com", "34"])
print(res1)
# >>> True

r.himport_set("user:2", "user", ["Bob", "bob@example.com", "41"])
r.himport_set("user:3", "user", ["Carol", "carol@example.com", "29"])

# The result is an ordinary hash.
res2 = r.hgetall("user:2")
print(res2)
# >>> {'age': '41', 'name': 'Bob', 'email': 'bob@example.com'}
```

##### Ruby

```ruby
# Declare the field names once.
r.himport_prepare('user', %w[name email age])

# Create each hash by sending only its values.
res1 = r.himport_set('user:1', 'user', ['Alice', 'alice@example.com', '34'])
puts res1 # >>> OK

r.himport_set('user:2', 'user', ['Bob', 'bob@example.com', '41'])
r.himport_set('user:3', 'user', ['Carol', 'carol@example.com', '29'])

# The result is an ordinary hash.
res2 = r.hgetall('user:2')
puts res2.inspect
# >>> {"age" => "41", "name" => "Bob", "email" => "bob@example.com"}
```



Each key you create this way is an ordinary hash. Note that:

- [`HIMPORT SET`](https://redis.io/docs/latest/commands/himport-set) replaces an existing key rather than merging into it.
- [`HGETALL`](https://redis.io/docs/latest/commands/hgetall) can return the fields in a different order from the one you declared.

A fieldset belongs to the connection that declared it. Client libraries that support `HIMPORT` track your fieldsets and declare them again on each connection they use, including pooled connections, reconnections, and cluster nodes, so you don't manage this yourself. Some clients, such as Jedis, Lettuce, and StackExchange.Redis, have no prepare method: you create a fieldset object and the client declares it when it's first used. Most client libraries mark their `HIMPORT` support as experimental, so its API might change, and some clients don't support it inside a transaction.

To import many hashes, send the imports in a [pipeline](https://redis.io/docs/latest/develop/using-commands/pipelining) so they share network round trips instead of waiting for each reply in turn:

Bulk ingestion: Pipeline many HIMPORT SET calls that share one fieldset to load a large number of hashes with few network round trips

**Difficulty:** Intermediate

**Builds upon:** himport_basic

**Commands:** HIMPORT, HGET

**Complexity:**
- HIMPORT: Depends on subcommand
- HGET: O(1)

**Available in:** Redis CLI, C#, C#, Go, Java, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), JavaScript (Node.js), PHP, Python, Ruby

##### Redis CLI

```
> HIMPORT PREPARE user name email age
OK
> HIMPORT SET user:1000 user user1000 user1000@example.com 20
OK
> HGET user:1000 email
"user1000@example.com"
```

##### C#

```csharp
        await using var bulkFields = HashImport.Create("name", "email", "age");

        // Start many imports without awaiting each one, so they share round trips.
        var imports = new List<Task>();

        for (int i = 1; i <= 1000; i++)
        {
            imports.Add(db.HashImportAsync(
                $"user:{i}",
                bulkFields,
                new RedisValue[] { $"user{i}", $"user{i}@example.com", (20 + i % 50).ToString() }
            ));
        }

        await Task.WhenAll(imports);

        int res2 = imports.Count(t => t.Status == TaskStatus.RanToCompletion);
        Console.WriteLine(res2);    // >>> 1000

        RedisValue res3 = await db.HashGetAsync("user:1000", "email");
        Console.WriteLine(res3);    // >>> user1000@example.com
```

##### C#

```csharp
        using var bulkFields = HashImport.Create("name", "email", "age");

        // Queue many imports and send them in one round trip.
        var batch = db.CreateBatch();
        var imports = new List<Task>();

        for (int i = 1; i <= 1000; i++)
        {
            imports.Add(batch.HashImportAsync(
                $"user:{i}",
                bulkFields,
                new RedisValue[] { $"user{i}", $"user{i}@example.com", (20 + i % 50).ToString() }
            ));
        }

        batch.Execute();
        Task.WaitAll(imports.ToArray());

        int res2 = imports.Count(t => t.Status == TaskStatus.RanToCompletion);
        Console.WriteLine(res2);    // >>> 1000

        RedisValue res3 = db.HashGet("user:1000", "email");
        Console.WriteLine(res3);    // >>> user1000@example.com
```

##### C#

```csharp
        await using var bulkFields = HashImport.Create("name", "email", "age");

        // Start many imports without awaiting each one, so they share round trips.
        var imports = new List<Task>();

        for (int i = 1; i <= 1000; i++)
        {
            imports.Add(db.HashImportAsync(
                $"user:{i}",
                bulkFields,
                new RedisValue[] { $"user{i}", $"user{i}@example.com", (20 + i % 50).ToString() }
            ));
        }

        await Task.WhenAll(imports);

        int res2 = imports.Count(t => t.Status == TaskStatus.RanToCompletion);
        Console.WriteLine(res2);    // >>> 1000

        RedisValue res3 = await db.HashGetAsync("user:1000", "email");
        Console.WriteLine(res3);    // >>> user1000@example.com
```

##### C#

```csharp
        using var bulkFields = HashImport.Create("name", "email", "age");

        // Queue many imports and send them in one round trip.
        var batch = db.CreateBatch();
        var imports = new List<Task>();

        for (int i = 1; i <= 1000; i++)
        {
            imports.Add(batch.HashImportAsync(
                $"user:{i}",
                bulkFields,
                new RedisValue[] { $"user{i}", $"user{i}@example.com", (20 + i % 50).ToString() }
            ));
        }

        batch.Execute();
        Task.WaitAll(imports.ToArray());

        int res2 = imports.Count(t => t.Status == TaskStatus.RanToCompletion);
        Console.WriteLine(res2);    // >>> 1000

        RedisValue res3 = db.HashGet("user:1000", "email");
        Console.WriteLine(res3);    // >>> user1000@example.com
```

##### Go

```go
	if err := rdb.HImportPrepare(ctx, "user", "name", "email", "age").Err(); err != nil {
		panic(err)
	}

	// Queue many imports and send them in one round trip.
	pipe := rdb.Pipeline()
	for i := 1; i <= 1000; i++ {
		pipe.HImportSet(ctx, fmt.Sprintf("user:%d", i), "user",
			fmt.Sprintf("user%d", i), fmt.Sprintf("user%d@example.com", i), fmt.Sprint(20+i%50))
	}
	res3, err := pipe.Exec(ctx)
	if err != nil {
		panic(err)
	}

	allOK := true
	for _, cmd := range res3 {
		if cmd.Err() != nil {
			allOK = false
		}
	}
	fmt.Println(len(res3), allOK) // >>> 1000 true

	res4, err := rdb.HGet(ctx, "user:1000", "email").Result()
	if err != nil {
		panic(err)
	}
	fmt.Println(res4) // >>> user1000@example.com
```

##### Java

```java
            List<String> res3 = new ArrayList<>();

            // The sync API waits for each reply, so these imports aren't pipelined.
            // To pipeline them, use the async or reactive API.
            try (HashImport<String> fieldset = HashImport.of("name", "email", "age")) {
                for (int i = 1; i <= 1000; i++) {
                    res3.add(syncCommands.himportSet("user:" + i, fieldset,
                            "user" + i, "user" + i + "@example.com", String.valueOf(20 + i % 50)));
                }
            }

            boolean allOk = res3.stream().allMatch("OK"::equals);
            System.out.println(res3.size() + " " + allOk); // >>> 1000 true

            String res4 = syncCommands.hget("user:1000", "email");
            System.out.println(res4); // >>> user1000@example.com
```

##### Java (Asynchronous - Lettuce)

```java
            List<RedisFuture<String>> res3 = new ArrayList<>();

            // Issue many imports without waiting for each reply.
            try (HashImport<String> fieldset = HashImport.of("name", "email", "age")) {
                for (int i = 1; i <= 1000; i++) {
                    res3.add(asyncCommands.himportSet("user:" + i, fieldset,
                            "user" + i, "user" + i + "@example.com", String.valueOf(20 + i % 50)));
                }
            }

            LettuceFutures.awaitAll(5, TimeUnit.SECONDS, res3.toArray(new RedisFuture[0]));

            boolean allOk = res3.stream().allMatch(f -> "OK".equals(f.toCompletableFuture().join()));
            System.out.println(res3.size() + " " + allOk); // >>> 1000 true

            CompletableFuture<Void> getEmail = asyncCommands.hget("user:1000", "email")
                .thenAccept(res4 -> {
                    System.out.println(res4); // >>> user1000@example.com
                })
                .toCompletableFuture();

            getEmail.join();
```

##### Java (Reactive - Lettuce)

```java
            List<String> res3;

            // Issue many imports without waiting for each reply.
            try (HashImport<String> fieldset = HashImport.of("name", "email", "age")) {
                res3 = Flux.range(1, 1000)
                    .flatMap(i -> reactiveCommands.himportSet("user:" + i, fieldset,
                            "user" + i, "user" + i + "@example.com", String.valueOf(20 + i % 50)))
                    .collectList()
                    .block();
            }

            boolean allOk = res3.stream().allMatch("OK"::equals);
            System.out.println(res3.size() + " " + allOk); // >>> 1000 true

            Mono<String> getEmail = reactiveCommands.hget("user:1000", "email").doOnNext(res4 -> {
                System.out.println(res4); // >>> user1000@example.com
            });

            getEmail.block();
```

##### Java (Synchronous - Jedis)

```java
        List<Response<String>> res3 = new ArrayList<>();

        // Queue many imports and send them in one round trip.
        try (HashImport fields = HashImport.of("name", "email", "age");
                Pipeline pipeline = jedis.pipelined()) {
            for (int i = 1; i <= 1000; i++) {
                res3.add(pipeline.himportSet("user:" + i, fields,
                        "user" + i, "user" + i + "@example.com", String.valueOf(20 + i % 50)));
            }
            pipeline.sync();
        }

        boolean allOk = res3.stream().allMatch(r -> "OK".equals(r.get()));
        System.out.println(res3.size() + " " + allOk); // >>> 1000 true

        String res4 = jedis.hget("user:1000", "email");
        System.out.println(res4); // >>> user1000@example.com
```

##### JavaScript (Node.js)

```javascript
await client.hImportPrepare('user', ['name', 'email', 'age']);

// Commands issued together are automatically pipelined.
const imports = [];
for (let i = 1; i <= 1000; i++) {
  imports.push(
    client.hImportSet(`user:${i}`, 'user', [`user${i}`, `user${i}@example.com`, String(20 + i % 50)])
  );
}
const res3 = await Promise.all(imports);

console.log(res3.length, res3.every((r) => r === 'OK'));
// >>> 1000 true

const res4 = await client.hGet('user:1000', 'email');
console.log(res4); // >>> user1000@example.com
```

##### JavaScript (Node.js)

```javascript
const redis = new Redis({
  himportFieldsets: [{ name: 'user', fields: ['name', 'email', 'age'] }],
});

// Queue many imports and send them in one round trip.
const pipeline = redis.pipeline();
for (let i = 1; i <= 1000; i++) {
  pipeline.himport('SET', `user:${i}`, 'user', `user${i}`, `user${i}@example.com`, String(20 + i % 50));
}
const res3 = await pipeline.exec();

console.log(res3.length, res3.every(([err]) => err === null));
// >>> 1000 true

const res4 = await redis.hget('user:1000', 'email');
console.log(res4); // >>> user1000@example.com
```

##### JavaScript (Node.js)

```javascript
await client.hImportPrepare('user', ['name', 'email', 'age']);

// Commands issued together are automatically pipelined.
const imports = [];
for (let i = 1; i <= 1000; i++) {
  imports.push(
    client.hImportSet(`user:${i}`, 'user', [`user${i}`, `user${i}@example.com`, String(20 + i % 50)])
  );
}
const res3 = await Promise.all(imports);

console.log(res3.length, res3.every((r) => r === 'OK'));
// >>> 1000 true

const res4 = await client.hGet('user:1000', 'email');
console.log(res4); // >>> user1000@example.com
```

##### JavaScript (Node.js)

```javascript
const redis = new Redis({
  himportFieldsets: [{ name: 'user', fields: ['name', 'email', 'age'] }],
});

// Queue many imports and send them in one round trip.
const pipeline = redis.pipeline();
for (let i = 1; i <= 1000; i++) {
  pipeline.himport('SET', `user:${i}`, 'user', `user${i}`, `user${i}@example.com`, String(20 + i % 50));
}
const res3 = await pipeline.exec();

console.log(res3.length, res3.every(([err]) => err === null));
// >>> 1000 true

const res4 = await redis.hget('user:1000', 'email');
console.log(res4); // >>> user1000@example.com
```

##### PHP

```php
        // Queue many imports and send them in one round trip. The fieldset is
        // declared inside the pipeline so it runs on the same connection.
        $replies = $r->pipeline(function ($pipe) {
            $pipe->himport('PREPARE', 'user', ['name', 'email', 'age']);

            for ($i = 1; $i <= 1000; $i++) {
                $pipe->himport('SET', "user:$i", 'user', ["user$i", "user$i@example.com", (string) (20 + $i % 50)]);
            }
        });

        // The first reply is for PREPARE.
        $res3 = array_slice($replies, 1);
        $allOk = true;
        foreach ($res3 as $reply) {
            $allOk = $allOk && $reply == 'OK';
        }
        echo count($res3) . ' ' . var_export($allOk, true) . PHP_EOL; // >>> 1000 true

        $res4 = $r->hget('user:1000', 'email');
        echo $res4 . PHP_EOL; // >>> user1000@example.com
```

##### Python

```python
r.himport_prepare("user", ["name", "email", "age"])

# Queue many imports and send them in one round trip.
with r.pipeline(transaction=False) as pipe:
    for i in range(1, 1001):
        pipe.himport_set(
            f"user:{i}", "user", [f"user{i}", f"user{i}@example.com", str(20 + i % 50)]
        )
    res3 = pipe.execute()

print(len(res3), all(res3))
# >>> 1000 True

res4 = r.hget("user:1000", "email")
print(res4)
# >>> user1000@example.com
```

##### Ruby

```ruby
# Queue many imports and send them in one round trip. The fieldset is
# declared inside the pipeline so it runs on the same connection.
replies = r.pipelined do |pipe|
  pipe.himport_prepare('user', %w[name email age])
  (1..1000).each do |i|
    pipe.himport_set("user:#{i}", 'user', ["user#{i}", "user#{i}@example.com", (20 + i % 50).to_s])
  end
end

# The first reply is for PREPARE.
res3 = replies.drop(1)
puts "#{res3.length} #{res3.all?('OK')}" # >>> 1000 true

res4 = r.hget('user:1000', 'email')
puts res4 # >>> user1000@example.com
```



### Automatic conversion

For workloads that can't adopt a new command, Redis can convert eligible hashes to compact hashes on its own, with no code change. All the following settings default to `0` (off) and can be changed at runtime with [`CONFIG SET`](https://redis.io/docs/latest/commands/config-set).

#### On the write path

These convert hashes created or modified by normal commands (such as [`HSET`](https://redis.io/docs/latest/commands/hset)), so an existing application gains the memory saving with no code change. They take effect lazily, like `hash-max-listpack-entries`: a change applies to a given hash only on its next write, not the moment you run [`CONFIG SET`](https://redis.io/docs/latest/commands/config-set).

| Config | Meaning |
|---|---|
| `hash-min-template-entries` | Minimum field count for a hash to be auto-converted to a compact hash on its next write. `0` disables auto-conversion. |
| `hash-max-template-entries` | Maximum field count for auto-conversion: a hash wider than this is left a plain hash (keeps very wide hashes out of the shared registry). `0` means no upper bound. |

A hash is not converted if it uses [field expiration](#field-expiration), even when its field count meets the minimum. After a hash has been converted, it stays a compact hash even if its field count later grows beyond `hash-max-template-entries`.

#### On RDB load

An RDB saved before this feature contains only plain hashes. These configs let Redis convert them to compact hashes *as the RDB loads*, so an upgrade reclaims memory without rewriting data. They apply only to RDBs without compact hashes; an RDB that already contains them is loaded as-is, with no load-time conversion. In effect these are one-time upgrade configs: they have no effect once the RDB contains at least one compact hash.

| Config | Meaning |
|---|---|
| `hash-rdb-load-min-template-entries` | Minimum field count to convert a plain hash to a compact hash during load. `0` disables load-time conversion. |
| `hash-rdb-load-max-template-entries` | Maximum field count for load-time conversion. `0` means no upper bound. |
| `hash-rdb-load-template-disassembly-threshold` | Minimum number of keys that must end up sharing a converted field-name set for it to be kept. `0` keeps every converted set. |

The disassembly threshold avoids wasting memory on field-name sets shared by only a few keys: at the end of the load, if a set is used by fewer keys than the threshold, those keys are converted back to plain hashes and the shared set is freed. It also acts as a safety valve during the load. Redis tracks how many converted sets are still below the threshold; once at least 1,000 have been created, if more than half of them are still below the threshold, Redis assumes the dataset is a poor fit for compact hashes and stops creating new ones partway through the load. From that point, only hashes whose field set matches one already created during this load are converted; the rest stay plain.

## Performance

Most Redis hash commands are O(1).

A few commands, such as [`HKEYS`](https://redis.io/docs/latest/commands/hkeys), [`HVALS`](https://redis.io/docs/latest/commands/hvals), [`HGETALL`](https://redis.io/docs/latest/commands/hgetall), and most of the expiration-related commands, are O(n), where _n_ is the number of field-value pairs.

## Limits

Every hash can store up to 4,294,967,295 (2^32 - 1) field-value pairs.
In practice, your hashes are limited only by the overall memory on the VMs hosting your Redis deployment.

## Learn more

* [Redis Hashes Explained](https://www.youtube.com/watch?v=-KdITaRkQ-U) is a short, comprehensive video explainer covering Redis hashes.
* [Redis University's RU101](https://university.redis.com/courses/ru101/) covers Redis hashes in detail.

