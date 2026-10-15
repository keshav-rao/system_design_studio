# Redis sorted sets

```json metadata
{
  "schema_version": 2,
  "title": "Redis sorted sets",
  "description": "Introduction to Redis sorted sets",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"operating-on-ranges","title":"Operating on ranges"},{"id":"lexicographical-scores","title":"Lexicographical scores"},{"id":"examples","title":"Examples"},{"id":"performance","title":"Performance"},{"id":"alternatives","title":"Alternatives"},{"id":"learn-more","title":"Learn more"}]}

,
  "codeExamples": [{"codetabsId":"ss_tutorial-stepzadd","commands":[{"acl_categories":["@write","@sortedset","@fast"],"complexity":"O(log(N)","name":"ZADD"}],"description":"Foundational: Add members to a sorted set with their scores (creates new members or updates existing ones)","difficulty":"beginner","id":"zadd","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_ss_tutorial-stepzadd"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_ss_tutorial-stepzadd"},{"id":"Node-js","panelId":"panel_Nodejs_ss_tutorial-stepzadd"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_ss_tutorial-stepzadd"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_ss_tutorial-stepzadd"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_ss_tutorial-stepzadd"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_ss_tutorial-stepzadd"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_ss_tutorial-stepzadd"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_ss_tutorial-stepzadd"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_ss_tutorial-stepzadd"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_ss_tutorial-stepzadd"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_ss_tutorial-stepzadd"}]},{"buildsUpon":["zadd"],"codetabsId":"ss_tutorial-stepzrange","commands":[{"acl_categories":["@read","@sortedset","@slow"],"complexity":"O(log(N)","name":"ZRANGE"},{"acl_categories":["@read","@sortedset","@slow"],"complexity":"O(log(N)","name":"ZREVRANGE"}],"description":"Retrieve members in ascending or descending order using ZRANGE and ZREVRANGE (no sorting needed, already ordered)","difficulty":"beginner","id":"zrange","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_ss_tutorial-stepzrange"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_ss_tutorial-stepzrange"},{"id":"Node-js","panelId":"panel_Nodejs_ss_tutorial-stepzrange"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_ss_tutorial-stepzrange"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_ss_tutorial-stepzrange"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_ss_tutorial-stepzrange"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_ss_tutorial-stepzrange"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_ss_tutorial-stepzrange"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_ss_tutorial-stepzrange"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_ss_tutorial-stepzrange"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_ss_tutorial-stepzrange"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_ss_tutorial-stepzrange"}]},{"buildsUpon":["zrange"],"codetabsId":"ss_tutorial-stepzrange_withscores","commands":[{"acl_categories":["@read","@sortedset","@slow"],"complexity":"O(log(N)","name":"ZRANGE"}],"description":"Retrieve members with their scores using WITHSCORES when you need both the member and its associated score value","difficulty":"beginner","id":"zrange_withscores","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_ss_tutorial-stepzrange_withscores"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_ss_tutorial-stepzrange_withscores"},{"id":"Node-js","panelId":"panel_Nodejs_ss_tutorial-stepzrange_withscores"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_ss_tutorial-stepzrange_withscores"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_ss_tutorial-stepzrange_withscores"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_ss_tutorial-stepzrange_withscores"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_ss_tutorial-stepzrange_withscores"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_ss_tutorial-stepzrange_withscores"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_ss_tutorial-stepzrange_withscores"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_ss_tutorial-stepzrange_withscores"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_ss_tutorial-stepzrange_withscores"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_ss_tutorial-stepzrange_withscores"}]},{"buildsUpon":["zadd"],"codetabsId":"ss_tutorial-stepzrangebyscore","commands":[{"acl_categories":["@read","@sortedset","@slow"],"complexity":"O(log(N)","name":"ZRANGEBYSCORE"}],"description":"Query by score range: Retrieve members within a score range using ZRANGEBYSCORE when you need to filter by numeric values","difficulty":"intermediate","id":"zrangebyscore","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_ss_tutorial-stepzrangebyscore"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_ss_tutorial-stepzrangebyscore"},{"id":"Node-js","panelId":"panel_Nodejs_ss_tutorial-stepzrangebyscore"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_ss_tutorial-stepzrangebyscore"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_ss_tutorial-stepzrangebyscore"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_ss_tutorial-stepzrangebyscore"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_ss_tutorial-stepzrangebyscore"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_ss_tutorial-stepzrangebyscore"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_ss_tutorial-stepzrangebyscore"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_ss_tutorial-stepzrangebyscore"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_ss_tutorial-stepzrangebyscore"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_ss_tutorial-stepzrangebyscore"}]},{"buildsUpon":["zadd"],"codetabsId":"ss_tutorial-stepzremrangebyscore","commands":[{"acl_categories":["@write","@sortedset","@fast"],"complexity":"O(M*log(N)","name":"ZREM"},{"acl_categories":["@write","@sortedset","@slow"],"complexity":"O(log(N)","name":"ZREMRANGEBYSCORE"},{"acl_categories":["@read","@sortedset","@slow"],"complexity":"O(log(N)","name":"ZRANGE"}],"description":"Remove members using ZREM for individual elements or ZREMRANGEBYSCORE for score ranges when you need to delete data","difficulty":"intermediate","id":"zremrangebyscore","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_ss_tutorial-stepzremrangebyscore"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_ss_tutorial-stepzremrangebyscore"},{"id":"Node-js","panelId":"panel_Nodejs_ss_tutorial-stepzremrangebyscore"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_ss_tutorial-stepzremrangebyscore"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_ss_tutorial-stepzremrangebyscore"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_ss_tutorial-stepzremrangebyscore"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_ss_tutorial-stepzremrangebyscore"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_ss_tutorial-stepzremrangebyscore"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_ss_tutorial-stepzremrangebyscore"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_ss_tutorial-stepzremrangebyscore"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_ss_tutorial-stepzremrangebyscore"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_ss_tutorial-stepzremrangebyscore"}]},{"buildsUpon":["zadd"],"codetabsId":"ss_tutorial-stepzrank","commands":[{"acl_categories":["@keyspace","@write","@slow"],"complexity":"O(N)","name":"DEL"},{"acl_categories":["@write","@sortedset","@fast"],"complexity":"O(log(N)","name":"ZADD"},{"acl_categories":["@read","@sortedset","@fast"],"complexity":"O(log(N)","name":"ZRANK"},{"acl_categories":["@read","@sortedset","@fast"],"complexity":"O(log(N)","name":"ZREVRANK"}],"description":"Get member position: Use ZRANK and ZREVRANK to find a member\u0026amp;#39;s position in the sorted set (useful for leaderboards)","difficulty":"intermediate","id":"zrank","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_ss_tutorial-stepzrank"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_ss_tutorial-stepzrank"},{"id":"Node-js","panelId":"panel_Nodejs_ss_tutorial-stepzrank"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_ss_tutorial-stepzrank"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_ss_tutorial-stepzrank"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_ss_tutorial-stepzrank"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_ss_tutorial-stepzrank"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_ss_tutorial-stepzrank"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_ss_tutorial-stepzrank"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_ss_tutorial-stepzrank"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_ss_tutorial-stepzrank"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_ss_tutorial-stepzrank"}]},{"buildsUpon":["zadd"],"codetabsId":"ss_tutorial-stepzadd_lex","commands":[{"acl_categories":["@write","@sortedset","@fast"],"complexity":"O(log(N)","name":"ZADD"},{"acl_categories":["@read","@sortedset","@slow"],"complexity":"O(log(N)","name":"ZRANGE"},{"acl_categories":["@read","@sortedset","@slow"],"complexity":"O(log(N)","name":"ZRANGEBYLEX"}],"description":"Lexicographical queries: Add members with identical scores and use ZRANGEBYLEX to query by string range (enables generic indexing)","difficulty":"intermediate","id":"zadd_lex","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_ss_tutorial-stepzadd_lex"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_ss_tutorial-stepzadd_lex"},{"id":"Node-js","panelId":"panel_Nodejs_ss_tutorial-stepzadd_lex"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_ss_tutorial-stepzadd_lex"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_ss_tutorial-stepzadd_lex"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_ss_tutorial-stepzadd_lex"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_ss_tutorial-stepzadd_lex"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_ss_tutorial-stepzadd_lex"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_ss_tutorial-stepzadd_lex"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_ss_tutorial-stepzadd_lex"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_ss_tutorial-stepzadd_lex"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_ss_tutorial-stepzadd_lex"}]},{"buildsUpon":["zadd"],"codetabsId":"ss_tutorial-stepleaderboard","commands":[{"acl_categories":["@write","@sortedset","@fast"],"complexity":"O(log(N)","name":"ZADD"},{"acl_categories":["@write","@sortedset","@fast"],"complexity":"O(log(N)","name":"ZINCRBY"}],"description":"Practical pattern: Use ZADD to set scores and ZINCRBY to increment them when you need to update leaderboards with atomic operations","difficulty":"intermediate","id":"leaderboard","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_ss_tutorial-stepleaderboard"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_ss_tutorial-stepleaderboard"},{"id":"Node-js","panelId":"panel_Nodejs_ss_tutorial-stepleaderboard"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_ss_tutorial-stepleaderboard"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_ss_tutorial-stepleaderboard"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_ss_tutorial-stepleaderboard"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_ss_tutorial-stepleaderboard"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_ss_tutorial-stepleaderboard"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_ss_tutorial-stepleaderboard"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_ss_tutorial-stepleaderboard"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_ss_tutorial-stepleaderboard"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_ss_tutorial-stepleaderboard"}]}]
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


### Sorted set command summary

**35 commands in this group:**

[View all sorted-set commands](https://redis.io/commands/?group=sorted-set)

| Command | Summary | Complexity | Since |
|---------|---------|------------|-------|
| [BZMPOP](https://redis.io/commands/bzmpop/) | Removes and returns a member by score from one or more sorted sets. Blocks until a member is available otherwise. Deletes the sorted set if the last element was popped. | O(K) + O(M*log(N)) where K is the number of pro... | 7.0.0 |
| [BZPOPMAX](https://redis.io/commands/bzpopmax/) | Removes and returns the member with the highest score from one or more sorted sets. Blocks until a member available otherwise.  Deletes the sorted set if the last element was popped. | O(log(N)) with N being the number of elements i... | 5.0.0 |
| [BZPOPMIN](https://redis.io/commands/bzpopmin/) | Removes and returns the member with the lowest score from one or more sorted sets. Blocks until a member is available otherwise. Deletes the sorted set if the last element was popped. | O(log(N)) with N being the number of elements i... | 5.0.0 |
| [ZADD](https://redis.io/commands/zadd/) | Adds one or more members to a sorted set, or updates their scores. Creates the key if it doesn't exist. | O(log(N)) for each item added, where N is the n... | 1.2.0 |
| [ZCARD](https://redis.io/commands/zcard/) | Returns the number of members in a sorted set. | O(1) | 1.2.0 |
| [ZCOUNT](https://redis.io/commands/zcount/) | Returns the count of members in a sorted set that have scores within a range. | O(log(N)) with N being the number of elements i... | 2.0.0 |
| [ZDIFF](https://redis.io/commands/zdiff/) | Returns the difference between multiple sorted sets. | O(L + (N-K)log(N)) worst case where L is the to... | 6.2.0 |
| [ZDIFFSTORE](https://redis.io/commands/zdiffstore/) | Stores the difference of multiple sorted sets in a key. | O(L + (N-K)log(N)) worst case where L is the to... | 6.2.0 |
| [ZINCRBY](https://redis.io/commands/zincrby/) | Increments the score of a member in a sorted set. | O(log(N)) where N is the number of elements in ... | 1.2.0 |
| [ZINTER](https://redis.io/commands/zinter/) | Returns the intersect of multiple sorted sets. | O(N*K)+O(M*log(M)) worst case with N being the ... | 6.2.0 |

#### Sorted set command summary (part 2)

| Command | Summary | Complexity | Since |
|---------|---------|------------|-------|
| [ZINTERCARD](https://redis.io/commands/zintercard/) | Returns the number of members of the intersect of multiple sorted sets. | O(N*K) worst case with N being the smallest inp... | 7.0.0 |
| [ZINTERSTORE](https://redis.io/commands/zinterstore/) | Stores the intersect of multiple sorted sets in a key. | O(N*K)+O(M*log(M)) worst case with N being the ... | 2.0.0 |
| [ZLEXCOUNT](https://redis.io/commands/zlexcount/) | Returns the number of members in a sorted set within a lexicographical range. | O(log(N)) with N being the number of elements i... | 2.8.9 |
| [ZMPOP](https://redis.io/commands/zmpop/) | Returns the highest- or lowest-scoring members from one or more sorted sets after removing them. Deletes the sorted set if the last member was popped. | O(K) + O(M*log(N)) where K is the number of pro... | 7.0.0 |
| [ZMSCORE](https://redis.io/commands/zmscore/) | Returns the score of one or more members in a sorted set. | O(N) where N is the number of members being req... | 6.2.0 |
| [ZPOPMAX](https://redis.io/commands/zpopmax/) | Returns the highest-scoring members from a sorted set after removing them. Deletes the sorted set if the last member was popped. | O(log(N)*M) with N being the number of elements... | 5.0.0 |
| [ZPOPMIN](https://redis.io/commands/zpopmin/) | Returns the lowest-scoring members from a sorted set after removing them. Deletes the sorted set if the last member was popped. | O(log(N)*M) with N being the number of elements... | 5.0.0 |
| [ZRANDMEMBER](https://redis.io/commands/zrandmember/) | Returns one or more random members from a sorted set. | O(N) where N is the number of members returned | 6.2.0 |
| [ZRANGE](https://redis.io/commands/zrange/) | Returns members in a sorted set within a range of indexes. | O(log(N)+M) with N being the number of elements... | 1.2.0 |
| [ZRANGEBYLEX](https://redis.io/commands/zrangebylex/) | Returns members in a sorted set within a lexicographical range. | O(log(N)+M) with N being the number of elements... | 2.8.9 |

#### Sorted set command summary (part 3)

| Command | Summary | Complexity | Since |
|---------|---------|------------|-------|
| [ZRANGEBYSCORE](https://redis.io/commands/zrangebyscore/) | Returns members in a sorted set within a range of scores. | O(log(N)+M) with N being the number of elements... | 1.0.5 |
| [ZRANGESTORE](https://redis.io/commands/zrangestore/) | Stores a range of members from sorted set in a key. | O(log(N)+M) with N being the number of elements... | 6.2.0 |
| [ZRANK](https://redis.io/commands/zrank/) | Returns the index of a member in a sorted set ordered by ascending scores. | O(log(N)) | 2.0.0 |
| [ZREM](https://redis.io/commands/zrem/) | Removes one or more members from a sorted set. Deletes the sorted set if all members were removed. | O(M*log(N)) with N being the number of elements... | 1.2.0 |
| [ZREMRANGEBYLEX](https://redis.io/commands/zremrangebylex/) | Removes members in a sorted set within a lexicographical range. Deletes the sorted set if all members were removed. | O(log(N)+M) with N being the number of elements... | 2.8.9 |
| [ZREMRANGEBYRANK](https://redis.io/commands/zremrangebyrank/) | Removes members in a sorted set within a range of indexes. Deletes the sorted set if all members were removed. | O(log(N)+M) with N being the number of elements... | 2.0.0 |
| [ZREMRANGEBYSCORE](https://redis.io/commands/zremrangebyscore/) | Removes members in a sorted set within a range of scores. Deletes the sorted set if all members were removed. | O(log(N)+M) with N being the number of elements... | 1.2.0 |
| [ZREVRANGE](https://redis.io/commands/zrevrange/) | Returns members in a sorted set within a range of indexes in reverse order. | O(log(N)+M) with N being the number of elements... | 1.2.0 |
| [ZREVRANGEBYLEX](https://redis.io/commands/zrevrangebylex/) | Returns members in a sorted set within a lexicographical range in reverse order. | O(log(N)+M) with N being the number of elements... | 2.8.9 |
| [ZREVRANGEBYSCORE](https://redis.io/commands/zrevrangebyscore/) | Returns members in a sorted set within a range of scores in reverse order. | O(log(N)+M) with N being the number of elements... | 2.2.0 |

#### Sorted set command summary (part 4)

| Command | Summary | Complexity | Since |
|---------|---------|------------|-------|
| [ZREVRANK](https://redis.io/commands/zrevrank/) | Returns the index of a member in a sorted set ordered by descending scores. | O(log(N)) | 2.0.0 |
| [ZSCAN](https://redis.io/commands/zscan/) | Iterates over members and scores of a sorted set. | O(1) for every call. O(N) for a complete iterat... | 2.8.0 |
| [ZSCORE](https://redis.io/commands/zscore/) | Returns the score of a member in a sorted set. | O(1) | 1.2.0 |
| [ZUNION](https://redis.io/commands/zunion/) | Returns the union of multiple sorted sets. | O(N)+O(M*log(M)) with N being the sum of the si... | 6.2.0 |
| [ZUNIONSTORE](https://redis.io/commands/zunionstore/) | Stores the union of multiple sorted sets in a key. | O(N)+O(M log(M)) with N being the sum of the si... | 2.0.0 |



A Redis sorted set is a collection of unique strings (members) ordered by an associated score.
When more than one string has the same score, the strings are ordered lexicographically.
Some use cases for sorted sets include:

* Leaderboards. For example, you can use sorted sets to easily maintain  ordered lists of the highest scores in a massive online game.
* Rate limiters. In particular, you can use a sorted set to build a sliding-window rate limiter to prevent excessive API requests.

You can think of sorted sets as a mix between a Set and
a Hash. Like sets, sorted sets are composed of unique, non-repeating
string elements, so in some sense a sorted set is a set as well.

However while elements inside sets are not ordered, every element in
a sorted set is associated with a floating point value, called *the score*
(this is why the type is also similar to a hash, since every element
is mapped to a value).

Moreover, elements in a sorted set are *taken in order* (so they are not
ordered on request, order is a peculiarity of the data structure used to
represent sorted sets). They are ordered according to the following rule:

* If B and A are two elements with a different score, then A > B if A.score is > B.score.
* If B and A have exactly the same score, then A > B if the A string is lexicographically greater than the B string. B and A strings can't be equal since sorted sets only have unique elements.

Let's start with a simple example, we'll add all our racers and the score they got in the first race:

Foundational: Add members to a sorted set with their scores (creates new members or updates existing ones)

**Commands:** ZADD

**Complexity:**
- ZADD: O(log(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> ZADD racer_scores 10 "Norem"
(integer) 1
> ZADD racer_scores 12 "Castilla"
(integer) 1
> ZADD racer_scores 8 "Sam-Bodden" 10 "Royce" 6 "Ford" 14 "Prickett"
(integer) 4
```

##### C#

```csharp
        bool res1 = db.SortedSetAdd("racer_scores", "Norem", 10);
        Console.WriteLine(res1); // >>> True

        bool res2 = db.SortedSetAdd("racer_scores", "Castilla", 12);
        Console.WriteLine(res2); // >>> True

        long res3 = db.SortedSetAdd("racer_scores", [
            new("Sam-Bodden", 8),
            new("Royce", 10),
            new("Ford", 6),
            new("Prickett", 14),
            new("Castilla", 12)
        ]);
        Console.WriteLine(res3); // >>> 4
```

##### Go

```go
	res1, err := rdb.ZAdd(ctx, "racer_scores",
		redis.Z{Member: "Norem", Score: 10},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // >>> 1

	res2, err := rdb.ZAdd(ctx, "racer_scores",
		redis.Z{Member: "Castilla", Score: 12},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2) // >>> 1

	res3, err := rdb.ZAdd(ctx, "racer_scores",
		redis.Z{Member: "Norem", Score: 10},
		redis.Z{Member: "Sam-Bodden", Score: 8},
		redis.Z{Member: "Royce", Score: 10},
		redis.Z{Member: "Ford", Score: 6},
		redis.Z{Member: "Prickett", Score: 14},
		redis.Z{Member: "Castilla", Score: 12},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3) // >>> 4
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> zadd = asyncCommands.zadd("racer_scores", ScoredValue.just(10d, "Norem"))
                    .thenCompose(res1 -> {
                        System.out.println(res1); // >>> 1

                        return asyncCommands.zadd("racer_scores", ScoredValue.just(12d, "Castilla"));
                    }).thenCompose(res2 -> {
                        System.out.println(res2); // >>> 1

                        return asyncCommands.zadd("racer_scores", ScoredValue.just(8d, "Sam-Bodden"),
                                ScoredValue.just(10d, "Royce"), ScoredValue.just(6d, "Ford"),
                                ScoredValue.just(14d, "Prickett"));
                    })
                    .thenAccept(System.out::println) // >>> 4
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> zadd = reactiveCommands.zadd("racer_scores", ScoredValue.just(10d, "Norem")).doOnNext(result -> {
                System.out.println(result); // >>> 1
            }).flatMap(v -> reactiveCommands.zadd("racer_scores", ScoredValue.just(12d, "Castilla"))).doOnNext(result -> {
                System.out.println(result); // >>> 1
            }).flatMap(v -> reactiveCommands.zadd("racer_scores", ScoredValue.just(8d, "Sam-Bodden"),
                    ScoredValue.just(10d, "Royce"), ScoredValue.just(6d, "Ford"),
                    ScoredValue.just(14d, "Prickett"))).doOnNext(result -> {
                        System.out.println(result); // >>> 4
                    }).then();
```

##### Java (Synchronous - Jedis)

```java
    long res1 = jedis.zadd("racer_scores", 10d, "Norem");
    System.out.println(res1); // >>> 1

    long res2 = jedis.zadd("racer_scores", 12d, "Castilla");
    System.out.println(res2); // >>> 1

    long res3 = jedis.zadd("racer_scores", new HashMap<String,Double>() {{
      put("Sam-Bodden", 8d);
      put("Royce", 10d);
      put("Ford", 6d);
      put("Prickett", 14d);
      put("Castilla", 12d);
    }});
    System.out.println(res3); // >>> 4
```

##### JavaScript (Node.js)

```javascript
const res1 = await client.zAdd('racer_scores', { score: 10, value: 'Norem' });
console.log(res1);  // >>> 1

const res2 = await client.zAdd('racer_scores', { score: 12, value: 'Castilla' });
console.log(res2);  // >>> 1

const res3 = await client.zAdd('racer_scores', [
  { score: 8, value: 'Sam-Bodden' },
  { score: 10, value: 'Royce' },
  { score: 6, value: 'Ford' },
  { score: 14, value: 'Prickett' },
  { score: 12, value: 'Castilla' }
]);
console.log(res3);  // >>> 4
```

##### PHP

```php
        $res1 = $r->zadd('racer_scores', ['Norem' => 10]);
        echo $res1 . PHP_EOL;
        // >>> 1

        $res2 = $r->zadd('racer_scores', ['Castilla' => 12]);
        echo $res2 . PHP_EOL;
        // >>> 1

        $res3 = $r->zadd('racer_scores', [
            'Sam-Bodden' => 8,
            'Royce' => 10,
            'Ford' => 6,
            'Prickett' => 14,
            'Castilla' => 12,
        ]);
        echo $res3 . PHP_EOL;
        // >>> 4
```

##### Python

```python
res1 = r.zadd("racer_scores", {"Norem": 10})
print(res1)  # >>> 1

res2 = r.zadd("racer_scores", {"Castilla": 12})
print(res2)  # >>> 1

res3 = r.zadd(
    "racer_scores",
    {"Sam-Bodden": 8, "Royce": 10, "Ford": 6, "Prickett": 14, "Castilla": 12},
)
print(res3)  # >>> 4
```

##### Ruby

```ruby
res1 = r.zadd('racer_scores', [[10, 'Norem']])
puts res1 # >>> 1

res2 = r.zadd('racer_scores', [[12, 'Castilla']])
puts res2 # >>> 1

res3 = r.zadd('racer_scores', [
  [8, 'Sam-Bodden'],
  [10, 'Royce'],
  [6, 'Ford'],
  [14, 'Prickett'],
  [12, 'Castilla']
])
puts res3 # >>> 4
```

##### Rust (Asynchronous)

```rust
        if let Ok(res) = r.zadd("racer_scores", "Norem", 10).await {
            let res: usize = res;
            println!("{res}"); // >>> 1
        }

        if let Ok(res) = r.zadd("racer_scores", "Castilla", 12).await {
            let res: usize = res;
            println!("{res}"); // >>> 1
        }

        if let Ok(res) = r
            .zadd_multiple(
                "racer_scores",
                &[
                    (8, "Sam-Bodden"),
                    (10, "Royce"),
                    (6, "Ford"),
                    (14, "Prickett"),
                    (12, "Castilla"),
                ],
            )
            .await
        {
            let res: usize = res;
            println!("{res}"); // >>> 4
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.zadd("racer_scores", "Norem", 10) {
            let res: usize = res;
            println!("{res}"); // >>> 1
        }

        if let Ok(res) = r.zadd("racer_scores", "Castilla", 12) {
            let res: usize = res;
            println!("{res}"); // >>> 1
        }

        if let Ok(res) = r.zadd_multiple(
            "racer_scores",
            &[
                (8, "Sam-Bodden"),
                (10, "Royce"),
                (6, "Ford"),
                (14, "Prickett"),
                (12, "Castilla"),
            ],
        ) {
            let res: usize = res;
            println!("{res}"); // >>> 4
        }
```




As you can see [`ZADD`](https://redis.io/docs/latest/commands/zadd) is similar to [`SADD`](https://redis.io/docs/latest/commands/sadd), but takes one additional argument
(placed before the element to be added) which is the score.
[`ZADD`](https://redis.io/docs/latest/commands/zadd) is also variadic, so you are free to specify multiple score-value
pairs, as shown in the example above.

With sorted sets it is trivial to return a list of racers sorted by their
score because actually *they are already sorted*.

Implementation note: Sorted sets are implemented via a
dual-ported data structure containing both a skip list and a hash table, so
every time we add an element Redis performs an O(log(N)) operation. That's
good, so when we ask for sorted elements, Redis does not have to do any work at
all, it's already sorted. Note that the [`ZRANGE`](https://redis.io/docs/latest/commands/zrange) order is low to high, while the [`ZREVRANGE`](https://redis.io/docs/latest/commands/zrevrange) order is high to low:

Retrieve members in ascending or descending order using ZRANGE and ZREVRANGE (no sorting needed, already ordered)

**Builds upon:** zadd

**Commands:** ZRANGE, ZREVRANGE

**Complexity:**
- ZRANGE: O(log(N)
- ZREVRANGE: O(log(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> ZRANGE racer_scores 0 -1
1) "Ford"
2) "Sam-Bodden"
3) "Norem"
4) "Royce"
5) "Castilla"
6) "Prickett"
> ZREVRANGE racer_scores 0 -1
1) "Prickett"
2) "Castilla"
3) "Royce"
4) "Norem"
5) "Sam-Bodden"
6) "Ford"
```

##### C#

```csharp
        RedisValue[] res4 = db.SortedSetRangeByRank("racer_scores", 0, -1);
        Console.WriteLine(string.Join(", ", res4)); // >>> Ford, Sam-Bodden, Norem, Royce, Castilla, Prickett

        RedisValue[] res5 = db.SortedSetRangeByRank("racer_scores", 0, -1, Order.Descending);
        Console.WriteLine(string.Join(", ", res5)); // >>> Prickett, Castilla, Royce, Norem, Sam-Bodden, Ford
```

##### Go

```go
	res4, err := rdb.ZRange(ctx, "racer_scores", 0, -1).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4)
	// >>> [Ford Sam-Bodden Norem Royce Castilla Prickett]

	res5, err := rdb.ZRevRange(ctx, "racer_scores", 0, -1).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res5)
	// >>> [Prickett Castilla Royce Norem Sam-Bodden Ford]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> zrange = asyncCommands.zrange("racer_scores", 0, -1).thenCompose(res3 -> {
                System.out.println(res3);
                // >>> [Ford, Sam-Bodden, Norem, Royce, Castilla, Prickett]

                return asyncCommands.zrevrange("racer_scores", 0, -1);
            })
                    .thenAccept(System.out::println)
                    // >>> [Prickett, Castilla, Royce, Norem, Sam-Bodden, Ford]
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> zrange = reactiveCommands.zrange("racer_scores", 0, -1).collectList().doOnNext(result -> {
                System.out.println(result);
                // >>> [Ford, Sam-Bodden, Norem, Royce, Castilla, Prickett]
            }).flatMap(v -> reactiveCommands.zrevrange("racer_scores", 0, -1).collectList()).doOnNext(result -> {
                System.out.println(result);
                // >>> [Prickett, Castilla, Royce, Norem, Sam-Bodden, Ford]
            }).then();
```

##### Java (Synchronous - Jedis)

```java
    List<String> res4 = jedis.zrange("racer_scores", 0, -1);
    System.out.println(res4); // >>> [Ford, Sam-Bodden, Norem, Royce, Castil, Castilla, Prickett]

    List<String> res5 = jedis.zrevrange("racer_scores", 0, -1);
    System.out.println(res5); // >>> [Prickett, Castilla, Castil, Royce, Norem, Sam-Bodden, Ford]
```

##### JavaScript (Node.js)

```javascript
const res4 = await client.zRange('racer_scores', 0, -1);
console.log(res4);  // >>> ['Ford', 'Sam-Bodden', 'Norem', 'Royce', 'Castilla', 'Prickett']
```

##### PHP

```php
        $res4 = $r->zrange('racer_scores', 0, -1);
        echo json_encode($res4) . PHP_EOL;
        // >>> ["Ford","Sam-Bodden","Norem","Royce","Castilla","Prickett"]

        $res5 = $r->zrevrange('racer_scores', 0, -1);
        echo json_encode($res5) . PHP_EOL;
        // >>> ["Prickett","Castilla","Royce","Norem","Sam-Bodden","Ford"]
```

##### Python

```python
res4 = r.zrange("racer_scores", 0, -1)
print(res4)  # >>> ['Ford', 'Sam-Bodden', 'Norem', 'Royce', 'Castilla', 'Prickett']

res5 = r.zrevrange("racer_scores", 0, -1)
print(res5)  # >>> ['Prickett', 'Castilla', 'Royce', 'Norem', 'Sam-Bodden', 'Ford']
```

##### Ruby

```ruby
res4 = r.zrange('racer_scores', 0, -1)
puts res4.inspect # >>> ["Ford", "Sam-Bodden", "Norem", "Royce", "Castilla", "Prickett"]

res5 = r.zrevrange('racer_scores', 0, -1)
puts res5.inspect # >>> ["Prickett", "Castilla", "Royce", "Norem", "Sam-Bodden", "Ford"]
```

##### Rust (Asynchronous)

```rust
        if let Ok(res) = r.zrange("racer_scores", 0, -1).await {
            let res: Vec<String> = res;
            println!("{res:?}");
            // >>> ["Ford", "Sam-Bodden", "Norem", "Royce", "Castilla", "Prickett"]
        }

        if let Ok(res) = r.zrevrange("racer_scores", 0, -1).await {
            let res: Vec<String> = res;
            println!("{res:?}");
            // >>> ["Prickett", "Castilla", "Royce", "Norem", "Sam-Bodden", "Ford"]
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.zrange("racer_scores", 0, -1) {
            let res: Vec<String> = res;
            println!("{res:?}");
            // >>> ["Ford", "Sam-Bodden", "Norem", "Royce", "Castilla", "Prickett"]
        }

        if let Ok(res) = r.zrevrange("racer_scores", 0, -1) {
            let res: Vec<String> = res;
            println!("{res:?}");
            // >>> ["Prickett", "Castilla", "Royce", "Norem", "Sam-Bodden", "Ford"]
        }
```



Note: 0 and -1 means from element index 0 to the last element (-1 works
here just as it does in the case of the [`LRANGE`](https://redis.io/docs/latest/commands/lrange) command).

It is possible to return scores as well, using the `WITHSCORES` argument:

Retrieve members with their scores using WITHSCORES when you need both the member and its associated score value

**Builds upon:** zrange

**Commands:** ZRANGE

**Complexity:**
- ZRANGE: O(log(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> ZRANGE racer_scores 0 -1 withscores
 1) "Ford"
 2) "6"
 3) "Sam-Bodden"
 4) "8"
 5) "Norem"
 6) "10"
 7) "Royce"
 8) "10"
 9) "Castilla"
10) "12"
11) "Prickett"
12) "14"
```

##### C#

```csharp
        SortedSetEntry[] res6 = db.SortedSetRangeByRankWithScores("racer_scores", 0, -1);
        Console.WriteLine(string.Join(", ", res6)); // >>> Ford: 6, Sam-Bodden: 8, Norem: 10, Royce: 10, Castilla: 12, Prickett: 14
```

##### Go

```go
	res6, err := rdb.ZRangeWithScores(ctx, "racer_scores", 0, -1).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res6)
	// >>> [{6 Ford} {8 Sam-Bodden} {10 Norem} {10 Royce} {12 Castilla} {14 Prickett}]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> zrangeWithScores = asyncCommands.zrangeWithScores("racer_scores", 0, -1)
                    .thenAccept(System.out::println)
                    // >>> [ScoredValue[6.000000, Ford], ScoredValue[8.000000, Sam-Bodden]...
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> zrangeWithScores = reactiveCommands.zrangeWithScores("racer_scores", 0, -1).collectList()
                    .doOnNext(result -> {
                        System.out.println(result);
                        // >>> [ScoredValue[6.000000, Ford], ScoredValue[8.000000, Sam-Bodden]...
                    }).then();
```

##### Java (Synchronous - Jedis)

```java
    List<Tuple> res6 = jedis.zrangeWithScores("racer_scores", 0, -1);
    System.out.println(res6); // >>> [[Ford,6.0], [Sam-Bodden,8.0], [Norem,10.0], [Royce,10.0], [Castil,12.0], [Castilla,12.0], [Prickett,14.0]]
```

##### JavaScript (Node.js)

```javascript
const res6 = await client.zRangeWithScores('racer_scores', 0, -1);
console.log(res6);
// >>> [
//       { value: 'Ford', score: 6 }, { value: 'Sam-Bodden', score: 8 },
//       { value: 'Norem', score: 10 }, { value: 'Royce', score: 10 },
//       { value: 'Castilla', score: 12 }, { value: 'Prickett', score: 14 }
// ]
```

##### PHP

```php
        $res6 = $r->zrange('racer_scores', 0, -1,[
            'withscores' => true,
        ]);
        echo json_encode($res6) . PHP_EOL;
        // >>> {"Ford":"6","Sam-Bodden":"8","Norem":"10","Royce":"10","Castilla":"12","Prickett":"14"}
```

##### Python

```python
res6 = r.zrange("racer_scores", 0, -1, withscores=True)
print(
    res6
)
# >>> [
#       ('Ford', 6.0), ('Sam-Bodden', 8.0), ('Norem', 10.0), ('Royce', 10.0),
#       ('Castilla', 12.0), ('Prickett', 14.0)
# ]
```

##### Ruby

```ruby
res6 = r.zrange('racer_scores', 0, -1, with_scores: true)
puts res6.inspect
# >>> [["Ford", 6.0], ["Sam-Bodden", 8.0], ["Norem", 10.0], ["Royce", 10.0],
#  ["Castilla", 12.0], ["Prickett", 14.0]]
```

##### Rust (Asynchronous)

```rust
        if let Ok(res) = r.zrange_withscores("racer_scores", 0, -1).await {
            let res: Vec<(String, f64)> = res;
            println!("{res:?}");
            // >>> [("Ford", 6.0), ("Sam-Bodden", 8.0), ("Norem", 10.0), ("Royce", 10.0), ("Castilla", 12.0), ("Prickett", 14.0)]
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.zrange_withscores("racer_scores", 0, -1) {
            let res: Vec<(String, f64)> = res;
            println!("{res:?}");
            // >>> [("Ford", 6.0), ("Sam-Bodden", 8.0), ("Norem", 10.0), ("Royce", 10.0), ("Castilla", 12.0), ("Prickett", 14.0)]
        }
```



## Operating on ranges

Sorted sets are more powerful than this. They can operate on ranges.
Let's get all the racers with 10 or fewer points. We
use the [`ZRANGEBYSCORE`](https://redis.io/docs/latest/commands/zrangebyscore) command to do it:

Query by score range: Retrieve members within a score range using ZRANGEBYSCORE when you need to filter by numeric values

**Difficulty:** Intermediate

**Builds upon:** zadd

**Commands:** ZRANGEBYSCORE

**Complexity:**
- ZRANGEBYSCORE: O(log(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> ZRANGEBYSCORE racer_scores -inf 10
1) "Ford"
2) "Sam-Bodden"
3) "Norem"
4) "Royce"
```

##### C#

```csharp
        RedisValue[] res7 = db.SortedSetRangeByScore("racer_scores", double.NegativeInfinity, 10);
        Console.WriteLine(string.Join(", ", res7)); // >>> Ford, Sam-Bodden, Norem, Royce
```

##### Go

```go
	res7, err := rdb.ZRangeByScore(ctx, "racer_scores",
		&redis.ZRangeBy{Min: "-inf", Max: "10"},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res7)
	// >>> [Ford Sam-Bodden Norem Royce]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> zrangebyscore = asyncCommands
                    .zrangebyscore("racer_scores", Range.create(Double.NEGATIVE_INFINITY, 10))
                    .thenAccept(System.out::println)
                    // >>> [Ford, Sam-Bodden, Norem, Royce]
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> zrangebyscore = reactiveCommands
                    .zrangebyscore("racer_scores", Range.create(Double.NEGATIVE_INFINITY, 10)).collectList().doOnNext(result -> {
                        System.out.println(result); // >>> [Ford, Sam-Bodden, Norem, Royce]
                    }).then();
```

##### Java (Synchronous - Jedis)

```java
    List<String> res7 = jedis.zrangeByScore("racer_scores", Double.NEGATIVE_INFINITY, 10d);
    System.out.println(res7); // >>> [Ford, Sam-Bodden, Norem, Royce]
```

##### JavaScript (Node.js)

```javascript
const res7 = await client.zRangeByScore('racer_scores', '-inf', 10);
console.log(res7);  // >>> ['Ford', 'Sam-Bodden', 'Norem', 'Royce']
```

##### PHP

```php
        $res7 = $r->zrangebyscore('racer_scores', '-inf', 10);
        echo json_encode($res7) . PHP_EOL;
        // >>> ["Ford","Sam-Bodden","Norem","Royce"]
```

##### Python

```python
res7 = r.zrangebyscore("racer_scores", "-inf", 10)
print(res7)  # >>> ['Ford', 'Sam-Bodden', 'Norem', 'Royce']
```

##### Ruby

```ruby
res7 = r.zrangebyscore('racer_scores', '-inf', 10)
puts res7.inspect # >>> ["Ford", "Sam-Bodden", "Norem", "Royce"]
```

##### Rust (Asynchronous)

```rust
        if let Ok(res) = r.zrangebyscore("racer_scores", "-inf", 10).await {
            let res: Vec<String> = res;
            println!("{res:?}"); // >>> ["Ford", "Sam-Bodden", "Norem", "Royce"]
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.zrangebyscore("racer_scores", "-inf", 10) {
            let res: Vec<String> = res;
            println!("{res:?}"); // >>> ["Ford", "Sam-Bodden", "Norem", "Royce"]
        }
```



We asked Redis to return all the elements with a score between negative
infinity and 10 (both extremes are included).

To remove an element we'd simply call [`ZREM`](https://redis.io/docs/latest/commands/zrem) with the racer's name.
It's also possible to remove ranges of elements. Let's remove racer Castilla along with all
the racers with strictly fewer than 10 points:

Remove members using ZREM for individual elements or ZREMRANGEBYSCORE for score ranges when you need to delete data

**Difficulty:** Intermediate

**Builds upon:** zadd

**Commands:** ZREM, ZREMRANGEBYSCORE, ZRANGE

**Complexity:**
- ZREM: O(M*log(N)
- ZREMRANGEBYSCORE: O(log(N)
- ZRANGE: O(log(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> ZREM racer_scores "Castilla"
(integer) 1
> ZREMRANGEBYSCORE racer_scores -inf 9
(integer) 2
> ZRANGE racer_scores 0 -1
1) "Norem"
2) "Royce"
3) "Prickett"
```

##### C#

```csharp
        bool res8 = db.SortedSetRemove("racer_scores", "Castilla");
        Console.WriteLine(res8); // >>> True

        long res9 = db.SortedSetRemoveRangeByScore("racer_scores", double.NegativeInfinity, 9);
        Console.WriteLine(res9); // >>> 2

        RedisValue[] res10 = db.SortedSetRangeByRank("racer_scores", 0, -1);
        Console.WriteLine(string.Join(", ", res10)); // >>> Norem, Royce, Prickett
```

##### Go

```go
	res8, err := rdb.ZRem(ctx, "racer_scores", "Castilla").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res8) // >>> 1

	res9, err := rdb.ZRemRangeByScore(ctx, "racer_scores", "-inf", "9").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res9) // >>> 2

	res10, err := rdb.ZRange(ctx, "racer_scores", 0, -1).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res10)
	// >>> [Norem Royce Prickett]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> zremrangebyscore = asyncCommands.zrem("racer_scores", "Castilla").thenCompose(res4 -> {
                System.out.println(res4); // >>> 1

                return asyncCommands.zremrangebyscore("racer_scores", Range.create(Double.NEGATIVE_INFINITY, 9));
            }).thenCompose(res5 -> {
                System.out.println(res5); // >>> 2

                return asyncCommands.zrange("racer_scores", 0, -1);
            })
                    .thenAccept(System.out::println)
                    // >>> [Norem, Royce, Prickett]
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> zremrangebyscore = reactiveCommands.zrem("racer_scores", "Castilla").doOnNext(result -> {
                System.out.println(result); // >>> 1
            }).flatMap(v -> reactiveCommands.zremrangebyscore("racer_scores", Range.create(Double.NEGATIVE_INFINITY, 9)))
                    .doOnNext(result -> {
                        System.out.println(result); // >>> 2
                    }).flatMap(v -> reactiveCommands.zrange("racer_scores", 0, -1).collectList()).doOnNext(result -> {
                        System.out.println(result); // >>> [Norem, Royce, Prickett]
                    }).then();
```

##### Java (Synchronous - Jedis)

```java
    long res8 = jedis.zrem("racer_scores", "Castilla");
    System.out.println(res8); // >>> 1

    long res9 = jedis.zremrangeByScore("racer_scores", Double.NEGATIVE_INFINITY, 9d);
    System.out.println(res9); // >>> 2

    List<String> res10 = jedis.zrange("racer_scores", 0, -1);
    System.out.println(res10); // >>> [Norem, Royce, Prickett]
```

##### JavaScript (Node.js)

```javascript
const res8 = await client.zRem('racer_scores', 'Castilla');
console.log(res8);  // >>> 1

const res9 = await client.zRemRangeByScore('racer_scores', '-inf', 9);
console.log(res9);  // >>> 2


const res10 = await client.zRange('racer_scores', 0, -1);
console.log(res10);  // >>> ['Norem', 'Royce', 'Prickett']
```

##### PHP

```php
        $res8 = $r->zrem('racer_scores', 'Castilla');
        echo $res8 . PHP_EOL;
        // >>> 1

        $res9 = $r->zremrangebyscore('racer_scores', '-inf', 9);
        echo $res9 . PHP_EOL;
        // >>> 2

        $res10 = $r->zrange('racer_scores', 0, -1);
        echo json_encode($res10) . PHP_EOL;
        // >>> ["Norem","Royce","Prickett"]
```

##### Python

```python
res8 = r.zrem("racer_scores", "Castilla")
print(res8)  # >>> 1

res9 = r.zremrangebyscore("racer_scores", "-inf", 9)
print(res9)  # >>> 2

res10 = r.zrange("racer_scores", 0, -1)
print(res10)  # >>> ['Norem', 'Royce', 'Prickett']
```

##### Ruby

```ruby
res8 = r.zrem('racer_scores', ['Castilla'])
puts res8 # >>> 1

res9 = r.zremrangebyscore('racer_scores', '-inf', 9)
puts res9 # >>> 2

res10 = r.zrange('racer_scores', 0, -1)
puts res10.inspect # >>> ["Norem", "Royce", "Prickett"]
```

##### Rust (Asynchronous)

```rust
        if let Ok(res) = r.zrem("racer_scores", "Castilla").await {
            let res: usize = res;
            println!("{res}"); // >>> 1
        }

        if let Ok(res) = r.zrembyscore("racer_scores", "-inf", 9).await {
            let res: usize = res;
            println!("{res}"); // >>> 2
        }

        if let Ok(res) = r.zrange("racer_scores", 0, -1).await {
            let res: Vec<String> = res;
            println!("{res:?}"); // >>> ["Norem", "Royce", "Prickett"]
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.zrem("racer_scores", "Castilla") {
            let res: usize = res;
            println!("{res}"); // >>> 1
        }

        if let Ok(res) = r.zrembyscore("racer_scores", "-inf", 9) {
            let res: usize = res;
            println!("{res}"); // >>> 2
        }

        if let Ok(res) = r.zrange("racer_scores", 0, -1) {
            let res: Vec<String> = res;
            println!("{res:?}"); // >>> ["Norem", "Royce", "Prickett"]
        }
```



[`ZREMRANGEBYSCORE`](https://redis.io/docs/latest/commands/zremrangebyscore) is perhaps not the best command name,
but it can be very useful, and returns the number of removed elements.

Another extremely useful operation defined for sorted set elements
is the get-rank operation. It is possible to ask what is the
position of an element in the set of ordered elements.
The [`ZREVRANK`](https://redis.io/docs/latest/commands/zrevrank) command is also available in order to get the rank, considering
the elements sorted in a descending way.

Get member position: Use ZRANK and ZREVRANK to find a member's position in the sorted set (useful for leaderboards)

**Difficulty:** Intermediate

**Builds upon:** zadd

**Commands:** DEL, ZADD, ZRANK, ZREVRANK

**Complexity:**
- DEL: O(N)
- ZADD: O(log(N)
- ZRANK: O(log(N)
- ZREVRANK: O(log(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
# Recreate the three remaining racers so this example runs on its own.
> DEL racer_scores
(integer) 1
> ZADD racer_scores 10 "Norem" 10 "Royce" 14 "Prickett"
(integer) 3
> ZRANK racer_scores "Norem"
(integer) 0
> ZREVRANK racer_scores "Norem"
(integer) 2
```

##### C#

```csharp
        // Recreate the three remaining racers so this example runs on its own.
        db.KeyDelete("racer_scores");
        db.SortedSetAdd("racer_scores", [
            new("Norem", 10),
            new("Royce", 10),
            new("Prickett", 14)
        ]);

        long? res11 = db.SortedSetRank("racer_scores", "Norem");
        Console.WriteLine(res11); // >>> 0

        long? res12 = db.SortedSetRank("racer_scores", "Norem", Order.Descending);
        Console.WriteLine(res12); // >>> 2
```

##### Go

```go
	// Recreate the three remaining racers so this example runs on its own.
	rdb.Del(ctx, "racer_scores")
	rdb.ZAdd(ctx, "racer_scores",
		redis.Z{Member: "Norem", Score: 10},
		redis.Z{Member: "Royce", Score: 10},
		redis.Z{Member: "Prickett", Score: 14},
	)

	res11, err := rdb.ZRank(ctx, "racer_scores", "Norem").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res11) // >>> 0

	res12, err := rdb.ZRevRank(ctx, "racer_scores", "Norem").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res12) // >>> 2
```

##### Java (Asynchronous - Lettuce)

```java
            // Recreate the three remaining racers so this example runs on its own.
            CompletableFuture<Void> zrank = asyncCommands.del("racer_scores")
                    .thenCompose(delRes -> asyncCommands.zadd("racer_scores", ScoredValue.just(10d, "Norem"),
                            ScoredValue.just(10d, "Royce"), ScoredValue.just(14d, "Prickett")))
                    .thenCompose(addRes -> asyncCommands.zrank("racer_scores", "Norem"))
                    .thenCompose(res6 -> {
                        System.out.println(res6); // >>> 0

                        return asyncCommands.zrevrank("racer_scores", "Norem");
                    })
                    .thenAccept(System.out::println) // >>> 2
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            // Recreate the three remaining racers so this example runs on its own.
            Mono<Void> zrank = reactiveCommands.del("racer_scores")
                    .flatMap(v -> reactiveCommands.zadd("racer_scores", ScoredValue.just(10d, "Norem"),
                            ScoredValue.just(10d, "Royce"), ScoredValue.just(14d, "Prickett")))
                    .flatMap(v -> reactiveCommands.zrank("racer_scores", "Norem")).doOnNext(result -> {
                        System.out.println(result); // >>> 0
                    }).flatMap(v -> reactiveCommands.zrevrank("racer_scores", "Norem")).doOnNext(result -> {
                        System.out.println(result); // >>> 2
                    }).then();
```

##### Java (Synchronous - Jedis)

```java
    // Recreate the three remaining racers so this example runs on its own.
    jedis.del("racer_scores");
    jedis.zadd("racer_scores", new HashMap<String,Double>() {{
      put("Norem", 10d);
      put("Royce", 10d);
      put("Prickett", 14d);
    }});

    long res11 = jedis.zrank("racer_scores", "Norem");
    System.out.println(res11); // >>> 0

    long res12 = jedis.zrevrank("racer_scores", "Norem");
    System.out.println(res12); // >>> 2
```

##### JavaScript (Node.js)

```javascript
// Recreate the three remaining racers so this example runs on its own.
await client.del('racer_scores');
await client.zAdd('racer_scores', [
  { score: 10, value: 'Norem' },
  { score: 10, value: 'Royce' },
  { score: 14, value: 'Prickett' }
]);

const res11 = await client.zRank('racer_scores', 'Norem');
console.log(res11);  // >>> 0

const res12 = await client.zRevRank('racer_scores', 'Norem');
console.log(res12);  // >>> 2
```

##### PHP

```php
        // Recreate the three remaining racers so this example runs on its own.
        $r->del('racer_scores');
        $r->zadd('racer_scores', [
            'Norem' => 10,
            'Royce' => 10,
            'Prickett' => 14,
        ]);

        $res11 = $r->zrank('racer_scores', 'Norem');
        echo $res11 . PHP_EOL;
        // >>> 0

        $res12 = $r->zrevrank('racer_scores', 'Norem');
        echo $res12 . PHP_EOL;
        // >>> 2
```

##### Python

```python
# Recreate the three remaining racers so this example runs on its own.
r.delete("racer_scores")
r.zadd(
    "racer_scores",
    {"Norem": 10, "Royce": 10, "Prickett": 14},
)

res11 = r.zrank("racer_scores", "Norem")
print(res11)  # >>> 0

res12 = r.zrevrank("racer_scores", "Norem")
print(res12)  # >>> 2
```

##### Ruby

```ruby
# Recreate the three remaining racers so this example runs on its own.
r.del('racer_scores')
r.zadd('racer_scores', [[10, 'Norem'], [10, 'Royce'], [14, 'Prickett']])

res11 = r.zrank('racer_scores', 'Norem')
puts res11 # >>> 0

res12 = r.zrevrank('racer_scores', 'Norem')
puts res12 # >>> 2
```

##### Rust (Asynchronous)

```rust
        // Recreate the three remaining racers so this example runs on its own.
        let _: () = r.del("racer_scores").await.expect("Failed to del");
        let _: usize = r
            .zadd_multiple(
                "racer_scores",
                &[(10, "Norem"), (10, "Royce"), (14, "Prickett")],
            )
            .await
            .expect("Failed to zadd");

        if let Ok(res) = r.zrank("racer_scores", "Norem").await {
            let res: Option<usize> = res;
            if let Some(res) = res {
                println!("{res}"); // >>> 0
            }
        }

        if let Ok(res) = r.zrevrank("racer_scores", "Norem").await {
            let res: Option<usize> = res;
            if let Some(res) = res {
                println!("{res}"); // >>> 2
            }
        }
```

##### Rust (Synchronous)

```rust
        // Recreate the three remaining racers so this example runs on its own.
        let _: () = r.del("racer_scores").expect("Failed to del");
        let _: usize = r
            .zadd_multiple(
                "racer_scores",
                &[(10, "Norem"), (10, "Royce"), (14, "Prickett")],
            )
            .expect("Failed to zadd");

        if let Ok(res) = r.zrank("racer_scores", "Norem") {
            let res: Option<usize> = res;
            if let Some(res) = res {
                println!("{res}"); // >>> 0
            }
        }

        if let Ok(res) = r.zrevrank("racer_scores", "Norem") {
            let res: Option<usize> = res;
            if let Some(res) = res {
                println!("{res}"); // >>> 2
            }
        }
```



## Lexicographical scores

In version Redis 2.8, a new feature was introduced that allows
getting ranges lexicographically, assuming elements in a sorted set are all
inserted with the same identical score (elements are compared with the C
`memcmp` function, so it is guaranteed that there is no collation, and every
Redis instance will reply with the same output).

The main commands to operate with lexicographical ranges are [`ZRANGEBYLEX`](https://redis.io/docs/latest/commands/zrangebylex),
[`ZREVRANGEBYLEX`](https://redis.io/docs/latest/commands/zrevrangebylex), [`ZREMRANGEBYLEX`](https://redis.io/docs/latest/commands/zremrangebylex) and [`ZLEXCOUNT`](https://redis.io/docs/latest/commands/zlexcount).

For example, let's add again our list of famous racers, but this time
using a score of zero for all the elements. We'll see that because of the sorted sets ordering rules, they are already sorted lexicographically. Using [`ZRANGEBYLEX`](https://redis.io/docs/latest/commands/zrangebylex) we can ask for lexicographical ranges:

Lexicographical queries: Add members with identical scores and use ZRANGEBYLEX to query by string range (enables generic indexing)

**Difficulty:** Intermediate

**Builds upon:** zadd

**Commands:** ZADD, ZRANGE, ZRANGEBYLEX

**Complexity:**
- ZADD: O(log(N)
- ZRANGE: O(log(N)
- ZRANGEBYLEX: O(log(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> ZADD racer_scores 0 "Norem" 0 "Sam-Bodden" 0 "Royce" 0 "Castilla" 0 "Prickett" 0 "Ford"
(integer) 3
> ZRANGE racer_scores 0 -1
1) "Castilla"
2) "Ford"
3) "Norem"
4) "Prickett"
5) "Royce"
6) "Sam-Bodden"
> ZRANGEBYLEX racer_scores [A [L
1) "Castilla"
2) "Ford"
```

##### C#

```csharp
        long res13 = db.SortedSetAdd("racer_scores", [
            new("Norem", 0),
            new("Sam-Bodden", 0),
            new("Royce", 0),
            new("Ford", 0),
            new("Prickett", 0),
            new("Castilla", 0)
        ]);
        Console.WriteLine(res13); // >>> 3

        RedisValue[] res14 = db.SortedSetRangeByRank("racer_scores", 0, -1);
        Console.WriteLine(string.Join(", ", res14)); // >>> Castilla, Ford, Norem, Pricket, Royce, Sam-Bodden

        RedisValue[] res15 = db.SortedSetRangeByValue("racer_scores", "A", "L", Exclude.None);
        Console.WriteLine(string.Join(", ", res15)); // >>> Castilla, Ford
```

##### Go

```go
	res13, err := rdb.ZAdd(ctx, "racer_scores",
		redis.Z{Member: "Norem", Score: 0},
		redis.Z{Member: "Sam-Bodden", Score: 0},
		redis.Z{Member: "Royce", Score: 0},
		redis.Z{Member: "Ford", Score: 0},
		redis.Z{Member: "Prickett", Score: 0},
		redis.Z{Member: "Castilla", Score: 0},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res13) // >>> 3

	res14, err := rdb.ZRange(ctx, "racer_scores", 0, -1).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res14)
	// >>> [Castilla Ford Norem Prickett Royce Sam-Bodden]

	res15, err := rdb.ZRangeByLex(ctx, "racer_scores", &redis.ZRangeBy{
		Min: "[A", Max: "[L",
	}).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res15) // >>> [Castilla Ford]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> zaddLex = asyncCommands.zadd("racer_scores", ScoredValue.just(0d, "Norem"),
                    ScoredValue.just(0d, "Sam-Bodden"), ScoredValue.just(0d, "Royce"), ScoredValue.just(0d, "Castilla"),
                    ScoredValue.just(0d, "Prickett"), ScoredValue.just(0d, "Ford")).thenCompose(res7 -> {
                        System.out.println(res7); // >>> 3

                        return asyncCommands.zrange("racer_scores", 0, -1);
                    }).thenCompose(res8 -> {
                        System.out.println(res8);
                        // >>> [Castilla, Ford, Norem, Prickett, Royce, Sam-Bodden]

                        return asyncCommands.zrangebylex("racer_scores", Range.create("A", "L"));
                    })
                    .thenAccept(System.out::println)
                    // >>> [Castilla, Ford]
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> zaddLex = reactiveCommands
                    .zadd("racer_scores", ScoredValue.just(0d, "Norem"), ScoredValue.just(0d, "Sam-Bodden"),
                            ScoredValue.just(0d, "Royce"), ScoredValue.just(0d, "Castilla"),
                            ScoredValue.just(0d, "Prickett"), ScoredValue.just(0d, "Ford"))
                    .doOnNext(result -> {
                        System.out.println(result); // >>> 3
                    }).flatMap(v -> reactiveCommands.zrange("racer_scores", 0, -1).collectList()).doOnNext(result -> {
                        System.out.println(result);
                        // >>> [Castilla, Ford, Norem, Prickett, Royce, Sam-Bodden]
                    }).flatMap(v -> reactiveCommands.zrangebylex("racer_scores", Range.create("A", "L")).collectList())
                    .doOnNext(result -> {
                        System.out.println(result); // >>> [Castilla, Ford]
                    }).then();
```

##### Java (Synchronous - Jedis)

```java
    long res13 = jedis.zadd("racer_scores", new HashMap<String,Double>() {{
      put("Norem", 0d);
      put("Sam-Bodden", 0d);
      put("Royce", 0d);
      put("Ford", 0d);
      put("Prickett", 0d);
      put("Castilla", 0d);
    }});
    System.out.println(res13); // >>> 3

    List<String> res14 = jedis.zrange("racer_scores", 0, -1);
    System.out.println(res14); // >>> [Castilla, Ford, Norem, Prickett, Royce, Sam-Bodden]

    List<String> res15 = jedis.zrangeByLex("racer_scores", "[A", "[L");
    System.out.println(res15); // >>> [Castilla, Ford]
```

##### JavaScript (Node.js)

```javascript
const res13 = await client.zAdd('racer_scores', [
  { score: 0, value: 'Norem' },
  { score: 0, value: 'Sam-Bodden' },
  { score: 0, value: 'Royce' },
  { score: 0, value: 'Ford' },
  { score: 0, value: 'Prickett' },
  { score: 0, value: 'Castilla' }
]);
console.log(res13);  // >>> 3


const res14 = await client.zRange('racer_scores', 0, -1);
console.log(res14);  // >>> ['Castilla', 'Ford', 'Norem', 'Prickett', 'Royce', 'Sam-Bodden']

const res15 = await client.zRangeByLex('racer_scores', '[A', '[L');
console.log(res15);  // >>> ['Castilla', 'Ford']
```

##### PHP

```php
        $res13 = $r->zadd('racer_scores', [
            'Norem' => 0,
            'Sam-Bodden' => 0,
            'Royce' => 0,
            'Ford' => 0,
            'Prickett' => 0,
            'Castilla' => 0,
        ]);
        echo $res13 . PHP_EOL;
        // >>> 3

        $res14 = $r->zrange('racer_scores', 0, -1);
        echo json_encode($res14) . PHP_EOL;
        // >>> ["Castilla","Ford","Norem","Prickett","Royce","Sam-Bodden"]

        $res15 = $r->zrangebylex('racer_scores', '[A', '[L');
        echo json_encode($res15) . PHP_EOL;
        // >>> ["Castilla","Ford"]
```

##### Python

```python
res13 = r.zadd(
    "racer_scores",
    {
        "Norem": 0,
        "Sam-Bodden": 0,
        "Royce": 0,
        "Ford": 0,
        "Prickett": 0,
        "Castilla": 0,
    },
)
print(res13)  # >>> 3

res14 = r.zrange("racer_scores", 0, -1)
print(res14)  # >>> ['Castilla', 'Ford', 'Norem', 'Prickett', 'Royce', 'Sam-Bodden']

res15 = r.zrangebylex("racer_scores", "[A", "[L")
print(res15)  # >>> ['Castilla', 'Ford']
```

##### Ruby

```ruby
res13 = r.zadd('racer_scores', [
  [0, 'Norem'],
  [0, 'Sam-Bodden'],
  [0, 'Royce'],
  [0, 'Ford'],
  [0, 'Prickett'],
  [0, 'Castilla']
])
puts res13 # >>> 3

res14 = r.zrange('racer_scores', 0, -1)
puts res14.inspect # >>> ["Castilla", "Ford", "Norem", "Prickett", "Royce", "Sam-Bodden"]

res15 = r.zrangebylex('racer_scores', '[A', '[L')
puts res15.inspect # >>> ["Castilla", "Ford"]
```

##### Rust (Asynchronous)

```rust
        if let Ok(res) = r
            .zadd_multiple(
                "racer_scores",
                &[
                    (0, "Norem"),
                    (0, "Sam-Bodden"),
                    (0, "Royce"),
                    (0, "Ford"),
                    (0, "Prickett"),
                    (0, "Castilla"),
                ],
            )
            .await
        {
            let res: usize = res;
            println!("{res}"); // >>> 3
        }

        if let Ok(res) = r.zrange("racer_scores", 0, -1).await {
            let res: Vec<String> = res;
            println!("{res:?}");
            // >>> ["Castilla", "Ford", "Norem", "Prickett", "Royce", "Sam-Bodden"]
        }

        if let Ok(res) = r.zrangebylex("racer_scores", "[A", "[L").await {
            let res: Vec<String> = res;
            println!("{res:?}"); // >>> ["Castilla", "Ford"]
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.zadd_multiple(
            "racer_scores",
            &[
                (0, "Norem"),
                (0, "Sam-Bodden"),
                (0, "Royce"),
                (0, "Ford"),
                (0, "Prickett"),
                (0, "Castilla"),
            ],
        ) {
            let res: usize = res;
            println!("{res}"); // >>> 3
        }

        if let Ok(res) = r.zrange("racer_scores", 0, -1) {
            let res: Vec<String> = res;
            println!("{res:?}");
            // >>> ["Castilla", "Ford", "Norem", "Prickett", "Royce", "Sam-Bodden"]
        }

        if let Ok(res) = r.zrangebylex("racer_scores", "[A", "[L") {
            let res: Vec<String> = res;
            println!("{res:?}"); // >>> ["Castilla", "Ford"]
        }
```



Ranges can be inclusive or exclusive (depending on the first character),
also string infinite and minus infinite are specified respectively with
the `+` and `-` strings. See the documentation for more information.

This feature is important because it allows us to use sorted sets as a generic
index. For example, if you want to index elements by a 128-bit unsigned
integer argument, all you need to do is to add elements into a sorted
set with the same score (for example 0) but with a 16 byte prefix
consisting of **the 128 bit number in big endian**. Since numbers in big
endian, when ordered lexicographically (in raw bytes order) are actually
ordered numerically as well, you can ask for ranges in the 128 bit space,
and get the element's value discarding the prefix

Updating the score: leaderboards
---

Just a final note about sorted sets before switching to the next topic.
Sorted sets' scores can be updated at any time. Just calling [`ZADD`](https://redis.io/docs/latest/commands/zadd) against
an element already included in the sorted set will update its score
(and position) with O(log(N)) time complexity.  As such, sorted sets are suitable
when there are tons of updates.

Because of this characteristic a common use case is leaderboards.
The typical application is a Facebook game where you combine the ability to
take users sorted by their high score, plus the get-rank operation, in order
to show the top-N users, and the user rank in the leader board (e.g., "you are
the #4932 best score here").

## Examples

* There are two ways we can use a sorted set to represent a leaderboard. If we know a racer's new score, we can update it directly via the [`ZADD`](https://redis.io/docs/latest/commands/zadd) command. However, if we want to add points to an existing score, we can use the [`ZINCRBY`](https://redis.io/docs/latest/commands/zincrby) command.
Practical pattern: Use ZADD to set scores and ZINCRBY to increment them when you need to update leaderboards with atomic operations

**Difficulty:** Intermediate

**Builds upon:** zadd

**Commands:** ZADD, ZINCRBY

**Complexity:**
- ZADD: O(log(N)
- ZINCRBY: O(log(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> ZADD racer_scores 100 "Wood"
(integer) 1
> ZADD racer_scores 100 "Henshaw"
(integer) 1
> ZADD racer_scores 150 "Henshaw"
(integer) 0
> ZINCRBY racer_scores 50 "Wood"
"150"
> ZINCRBY racer_scores 50 "Henshaw"
"200"
```

##### C#

```csharp
        bool res16 = db.SortedSetAdd("racer_scores", "Wood", 100);
        Console.WriteLine(res16); // >>> True

        bool res17 = db.SortedSetAdd("racer_scores", "Henshaw", 100);
        Console.WriteLine(res17); // >>> True

        bool res18 = db.SortedSetAdd("racer_scores", "Henshaw", 150);
        Console.WriteLine(res18); // >>> False

        double res19 = db.SortedSetIncrement("racer_scores", "Wood", 50);
        Console.WriteLine(res19); // >>> 150.0

        double res20 = db.SortedSetIncrement("racer_scores", "Henshaw", 50);
        Console.WriteLine(res20); // >>> 200.0
```

##### Go

```go
	res16, err := rdb.ZAdd(ctx, "racer_scores",
		redis.Z{Member: "Wood", Score: 100},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res16) // >>> 1

	res17, err := rdb.ZAdd(ctx, "racer_scores",
		redis.Z{Member: "Henshaw", Score: 100},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res17) // >>> 1

	res18, err := rdb.ZAdd(ctx, "racer_scores",
		redis.Z{Member: "Henshaw", Score: 150},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res18) // >>> 0

	res19, err := rdb.ZIncrBy(ctx, "racer_scores", 50, "Wood").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res19) // >>> 150

	res20, err := rdb.ZIncrBy(ctx, "racer_scores", 50, "Henshaw").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res20) // >>> 200
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> leaderboard = asyncCommands.zadd("racer_scores", ScoredValue.just(100, "Wood"))
                    .thenCompose(res9 -> {
                        System.out.println(res9); // >>> 1

                        return asyncCommands.zadd("racer_scores", ScoredValue.just(100, "Henshaw"));
                    }).thenCompose(res10 -> {
                        System.out.println(res10); // >>> 1

                        return asyncCommands.zadd("racer_scores", ScoredValue.just(150, "Henshaw"));
                    }).thenCompose(res11 -> {
                        System.out.println(res11); // >>> 0

                        return asyncCommands.zincrby("racer_scores", 50, "Wood");
                    }).thenCompose(res12 -> {
                        System.out.println(res12); // >>> 150

                        return asyncCommands.zincrby("racer_scores", 50, "Henshaw");
                    })
                    .thenAccept(System.out::println) // >>> 200
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> leaderboard = reactiveCommands.zadd("racer_scores", ScoredValue.just(100, "Wood"))
                    .doOnNext(result -> {
                        System.out.println(result); // >>> 1
                    }).flatMap(v -> reactiveCommands.zadd("racer_scores", ScoredValue.just(100, "Henshaw")))
                    .doOnNext(result -> {
                        System.out.println(result); // >>> 1
                    }).flatMap(v -> reactiveCommands.zadd("racer_scores", ScoredValue.just(150, "Henshaw")))
                    .doOnNext(result -> {
                        System.out.println(result); // >>> 0
                    }).flatMap(v -> reactiveCommands.zincrby("racer_scores", 50, "Wood")).doOnNext(result -> {
                        System.out.println(result); // >>> 150
                    }).flatMap(v -> reactiveCommands.zincrby("racer_scores", 50, "Henshaw")).doOnNext(result -> {
                        System.out.println(result); // >>> 200
                    }).then();
```

##### Java (Synchronous - Jedis)

```java
    long res16 = jedis.zadd("racer_scores", 100d, "Wood");
    System.out.println(res16); // >>> 1

    long res17 = jedis.zadd("racer_scores", 100d, "Henshaw");
    System.out.println(res17); // >>> 1

    long res18 = jedis.zadd("racer_scores", 150d, "Henshaw");
    System.out.println(res18); // >>> 0

    double res19 = jedis.zincrby("racer_scores", 50d, "Wood");
    System.out.println(res19); // >>> 150.0

    double res20 = jedis.zincrby("racer_scores", 50d, "Henshaw");
    System.out.println(res20); // >>> 200.0
```

##### JavaScript (Node.js)

```javascript
const res16 = await client.zAdd('racer_scores', { score: 100, value: 'Wood' });
console.log(res16);  // >>> 1

const res17 = await client.zAdd('racer_scores', { score: 100, value: 'Henshaw' });
console.log(res17);  // >>> 1

const res18 = await client.zAdd('racer_scores', { score: 150, value: 'Henshaw' }, { nx: true });
console.log(res18);  // >>> 0

const res19 = await client.zIncrBy('racer_scores', 50, 'Wood');
console.log(res19);  // >>> 150.0

const res20 = await client.zIncrBy('racer_scores', 50, 'Henshaw');
console.log(res20);  // >>> 200.0
```

##### PHP

```php
        $res16 = $r->zadd('racer_scores', ['Wood' => 100]);
        echo $res16 . PHP_EOL;
        // >>> 1

        $res17 = $r->zadd('racer_scores', ['Henshaw' => 100]);
        echo $res17 . PHP_EOL;
        // >>> 1

        $res18 = $r->zadd('racer_scores', ['Henshaw' => 150]);
        echo $res18 . PHP_EOL;
        // >>> 0

        $res19 = $r->zincrby('racer_scores', 50, 'Wood');
        echo $res19 . PHP_EOL;
        // >>> 150

        $res20 = $r->zincrby('racer_scores', 50, 'Henshaw');
        echo $res20 . PHP_EOL;
        // >>> 200
```

##### Python

```python
res16 = r.zadd("racer_scores", {"Wood": 100})
print(res16)  # >>> 1

res17 = r.zadd("racer_scores", {"Henshaw": 100})
print(res17)  # >>> 1

res18 = r.zadd("racer_scores", {"Henshaw": 150})
print(res18)  # >>> 0

res19 = r.zincrby("racer_scores", 50, "Wood")
print(res19)  # >>> 150.0

res20 = r.zincrby("racer_scores", 50, "Henshaw")
print(res20)  # >>> 200.0
```

##### Ruby

```ruby
res16 = r.zadd('racer_scores', [[100, 'Wood']])
puts res16 # >>> 1

res17 = r.zadd('racer_scores', [[100, 'Henshaw']])
puts res17 # >>> 1

res18 = r.zadd('racer_scores', [[150, 'Henshaw']])
puts res18 # >>> 0

res19 = r.zincrby('racer_scores', 50, 'Wood')
puts res19 # >>> 150.0

res20 = r.zincrby('racer_scores', 50, 'Henshaw')
puts res20 # >>> 200.0
```

##### Rust (Asynchronous)

```rust
        if let Ok(res) = r.zadd("racer_scores", "Wood", 100).await {
            let res: usize = res;
            println!("{res}"); // >>> 1
        }

        if let Ok(res) = r.zadd("racer_scores", "Henshaw", 100).await {
            let res: usize = res;
            println!("{res}"); // >>> 1
        }

        if let Ok(res) = r.zadd("racer_scores", "Henshaw", 150).await {
            let res: usize = res;
            println!("{res}"); // >>> 0
        }

        if let Ok(res) = r.zincr("racer_scores", "Wood", 50).await {
            let res: f64 = res;
            println!("{res}"); // >>> 150
        }

        if let Ok(res) = r.zincr("racer_scores", "Henshaw", 50).await {
            let res: f64 = res;
            println!("{res}"); // >>> 200
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.zadd("racer_scores", "Wood", 100) {
            let res: usize = res;
            println!("{res}"); // >>> 1
        }

        if let Ok(res) = r.zadd("racer_scores", "Henshaw", 100) {
            let res: usize = res;
            println!("{res}"); // >>> 1
        }

        if let Ok(res) = r.zadd("racer_scores", "Henshaw", 150) {
            let res: usize = res;
            println!("{res}"); // >>> 0
        }

        if let Ok(res) = r.zincr("racer_scores", "Wood", 50) {
            let res: f64 = res;
            println!("{res}"); // >>> 150
        }

        if let Ok(res) = r.zincr("racer_scores", "Henshaw", 50) {
            let res: f64 = res;
            println!("{res}"); // >>> 200
        }
```



You'll see that [`ZADD`](https://redis.io/docs/latest/commands/zadd) returns 0 when the member already exists (the score is updated), while [`ZINCRBY`](https://redis.io/docs/latest/commands/zincrby) returns the new score. The score for racer Henshaw went from 100, was changed to 150 with no regard for what score was there before, and then was incremented by 50 to 200.

## Performance

Most sorted set operations are O(log(n)), where _n_ is the number of members.

Exercise some caution when running the [`ZRANGE`](https://redis.io/docs/latest/commands/zrange) command with large returns values (e.g., in the tens of thousands or more).
This command's time complexity is O(log(n) + m), where _m_ is the number of results returned. 

## Alternatives

Redis sorted sets are sometimes used for indexing other Redis data structures.
If you need to index and query your data, consider the [JSON](https://redis.io/docs/latest/develop/data-types/json) data type and the [Redis Search](https://redis.io/docs/latest/develop/ai/search-and-query) features.

## Learn more

* [Redis Sorted Sets Explained](https://www.youtube.com/watch?v=MUKlxdBQZ7g) is an entertaining introduction to sorted sets in Redis.
* [Redis University's RU101](https://university.redis.com/courses/ru101/) explores Redis sorted sets in detail.

