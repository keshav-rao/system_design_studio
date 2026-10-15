# Redis lists

```json metadata
{
  "schema_version": 2,
  "title": "Redis lists",
  "description": "Introduction to Redis lists",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"children":[{"id":"what-are-lists","title":"What are Lists?"},{"id":"first-steps-with-redis-lists","title":"First steps with Redis Lists"},{"id":"common-use-cases-for-lists","title":"Common use cases for lists"},{"id":"capped-lists","title":"Capped lists"}],"id":"examples","title":"Examples"},{"id":"blocking-operations-on-lists","title":"Blocking operations on lists"},{"id":"automatic-creation-and-removal-of-keys","title":"Automatic creation and removal of keys"},{"id":"limits","title":"Limits"},{"id":"performance","title":"Performance"},{"id":"alternatives","title":"Alternatives"},{"id":"learn-more","title":"Learn more"}]}

,
  "codeExamples": [{"buildsUpon":["lpush_rpush","lpop_rpop"],"codetabsId":"list_tutorial-stepqueue","commands":[{"acl_categories":["@write","@list","@fast"],"complexity":"O(1)","name":"LPUSH"},{"acl_categories":["@write","@list","@fast"],"complexity":"O(N)","name":"RPOP"}],"description":"Queue pattern: Use LPUSH to add items and RPOP to remove them in FIFO order when you need to process items in the order they were added","difficulty":"beginner","id":"queue","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_list_tutorial-stepqueue"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_list_tutorial-stepqueue"},{"id":"Node-js","panelId":"panel_Nodejs_list_tutorial-stepqueue"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_list_tutorial-stepqueue"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_list_tutorial-stepqueue"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_list_tutorial-stepqueue"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_list_tutorial-stepqueue"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_list_tutorial-stepqueue"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_list_tutorial-stepqueue"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_list_tutorial-stepqueue"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_list_tutorial-stepqueue"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_list_tutorial-stepqueue"}]},{"buildsUpon":["lpush_rpush"],"codetabsId":"list_tutorial-stepstack","commands":[{"acl_categories":["@write","@list","@fast"],"complexity":"O(1)","name":"LPUSH"},{"acl_categories":["@write","@list","@fast"],"complexity":"O(N)","name":"LPOP"}],"description":"Stack pattern: Use LPUSH to add items and LPOP to remove them in LIFO order when you need to process items in reverse order","difficulty":"beginner","id":"stack","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_list_tutorial-stepstack"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_list_tutorial-stepstack"},{"id":"Node-js","panelId":"panel_Nodejs_list_tutorial-stepstack"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_list_tutorial-stepstack"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_list_tutorial-stepstack"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_list_tutorial-stepstack"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_list_tutorial-stepstack"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_list_tutorial-stepstack"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_list_tutorial-stepstack"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_list_tutorial-stepstack"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_list_tutorial-stepstack"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_list_tutorial-stepstack"}]},{"codetabsId":"list_tutorial-stepllen","commands":[{"acl_categories":["@read","@list","@fast"],"complexity":"O(1)","name":"LLEN"}],"description":"Foundational: Get the number of elements in a list using LLEN to check list size","difficulty":"beginner","id":"llen","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_list_tutorial-stepllen"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_list_tutorial-stepllen"},{"id":"Node-js","panelId":"panel_Nodejs_list_tutorial-stepllen"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_list_tutorial-stepllen"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_list_tutorial-stepllen"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_list_tutorial-stepllen"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_list_tutorial-stepllen"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_list_tutorial-stepllen"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_list_tutorial-stepllen"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_list_tutorial-stepllen"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_list_tutorial-stepllen"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_list_tutorial-stepllen"}]},{"buildsUpon":["lpush_rpush","lpop_rpop"],"codetabsId":"list_tutorial-steplmove_lrange","commands":[{"acl_categories":["@write","@list","@fast"],"complexity":"O(1)","name":"LPUSH"},{"acl_categories":["@write","@list","@slow"],"complexity":"O(1)","name":"LMOVE"},{"acl_categories":["@read","@list","@slow"],"complexity":"O(S+N)","name":"LRANGE"}],"description":"Atomic transfer: Use LMOVE to move elements between lists in a single operation when you need to transfer items without race conditions","difficulty":"intermediate","id":"lmove_lrange","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_list_tutorial-steplmove_lrange"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_list_tutorial-steplmove_lrange"},{"id":"Node-js","panelId":"panel_Nodejs_list_tutorial-steplmove_lrange"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_list_tutorial-steplmove_lrange"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_list_tutorial-steplmove_lrange"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_list_tutorial-steplmove_lrange"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_list_tutorial-steplmove_lrange"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_list_tutorial-steplmove_lrange"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_list_tutorial-steplmove_lrange"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_list_tutorial-steplmove_lrange"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_list_tutorial-steplmove_lrange"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_list_tutorial-steplmove_lrange"}]},{"buildsUpon":["lpush_rpush"],"codetabsId":"list_tutorial-stepltrim.1","commands":[{"acl_categories":["@keyspace","@write","@slow"],"complexity":"O(N)","name":"DEL"},{"acl_categories":["@write","@list","@fast"],"complexity":"O(1)","name":"RPUSH"},{"acl_categories":["@write","@list","@slow"],"complexity":"O(N)","name":"LTRIM"},{"acl_categories":["@read","@list","@slow"],"complexity":"O(S+N)","name":"LRANGE"}],"description":"Capped lists: Use LTRIM to keep only a specific range of elements when you need to maintain a fixed-size list","difficulty":"intermediate","id":"ltrim.1","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_list_tutorial-stepltrim.1"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_list_tutorial-stepltrim.1"},{"id":"Node-js","panelId":"panel_Nodejs_list_tutorial-stepltrim.1"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_list_tutorial-stepltrim.1"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_list_tutorial-stepltrim.1"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_list_tutorial-stepltrim.1"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_list_tutorial-stepltrim.1"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_list_tutorial-stepltrim.1"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_list_tutorial-stepltrim.1"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_list_tutorial-stepltrim.1"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_list_tutorial-stepltrim.1"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_list_tutorial-stepltrim.1"}]},{"codetabsId":"list_tutorial-steplpush_rpush","commands":[{"acl_categories":["@keyspace","@write","@slow"],"complexity":"O(N)","name":"DEL"},{"acl_categories":["@write","@list","@fast"],"complexity":"O(1)","name":"RPUSH"},{"acl_categories":["@write","@list","@fast"],"complexity":"O(1)","name":"LPUSH"},{"acl_categories":["@read","@list","@slow"],"complexity":"O(S+N)","name":"LRANGE"}],"description":"Foundational: Add elements to both ends of a list using LPUSH (left/head) and RPUSH (right/tail) to build ordered sequences","difficulty":"beginner","id":"lpush_rpush","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_list_tutorial-steplpush_rpush"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_list_tutorial-steplpush_rpush"},{"id":"Node-js","panelId":"panel_Nodejs_list_tutorial-steplpush_rpush"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_list_tutorial-steplpush_rpush"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_list_tutorial-steplpush_rpush"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_list_tutorial-steplpush_rpush"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_list_tutorial-steplpush_rpush"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_list_tutorial-steplpush_rpush"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_list_tutorial-steplpush_rpush"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_list_tutorial-steplpush_rpush"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_list_tutorial-steplpush_rpush"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_list_tutorial-steplpush_rpush"}]},{"buildsUpon":["lpush_rpush"],"codetabsId":"list_tutorial-stepvariadic","commands":[{"acl_categories":["@keyspace","@write","@slow"],"complexity":"O(N)","name":"DEL"},{"acl_categories":["@write","@list","@fast"],"complexity":"O(1)","name":"RPUSH"},{"acl_categories":["@write","@list","@fast"],"complexity":"O(1)","name":"LPUSH"},{"acl_categories":["@read","@list","@slow"],"complexity":"O(S+N)","name":"LRANGE"}],"description":"Variadic operations: Add multiple elements in a single command using LPUSH or RPUSH when you need to reduce round trips to the server","difficulty":"beginner","id":"variadic","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_list_tutorial-stepvariadic"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_list_tutorial-stepvariadic"},{"id":"Node-js","panelId":"panel_Nodejs_list_tutorial-stepvariadic"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_list_tutorial-stepvariadic"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_list_tutorial-stepvariadic"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_list_tutorial-stepvariadic"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_list_tutorial-stepvariadic"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_list_tutorial-stepvariadic"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_list_tutorial-stepvariadic"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_list_tutorial-stepvariadic"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_list_tutorial-stepvariadic"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_list_tutorial-stepvariadic"}]},{"codetabsId":"list_tutorial-steplpop_rpop","commands":[{"acl_categories":["@keyspace","@write","@slow"],"complexity":"O(N)","name":"DEL"},{"acl_categories":["@write","@list","@fast"],"complexity":"O(1)","name":"RPUSH"},{"acl_categories":["@write","@list","@fast"],"complexity":"O(N)","name":"RPOP"},{"acl_categories":["@write","@list","@fast"],"complexity":"O(N)","name":"LPOP"}],"description":"Foundational: Remove and retrieve elements from both ends of a list using LPOP (left/head) and RPOP (right/tail) to consume items","difficulty":"beginner","id":"lpop_rpop","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_list_tutorial-steplpop_rpop"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_list_tutorial-steplpop_rpop"},{"id":"Node-js","panelId":"panel_Nodejs_list_tutorial-steplpop_rpop"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_list_tutorial-steplpop_rpop"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_list_tutorial-steplpop_rpop"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_list_tutorial-steplpop_rpop"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_list_tutorial-steplpop_rpop"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_list_tutorial-steplpop_rpop"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_list_tutorial-steplpop_rpop"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_list_tutorial-steplpop_rpop"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_list_tutorial-steplpop_rpop"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_list_tutorial-steplpop_rpop"}]},{"buildsUpon":["lpush_rpush"],"codetabsId":"list_tutorial-stepltrim","commands":[{"acl_categories":["@keyspace","@write","@slow"],"complexity":"O(N)","name":"DEL"},{"acl_categories":["@write","@list","@fast"],"complexity":"O(1)","name":"RPUSH"},{"acl_categories":["@write","@list","@slow"],"complexity":"O(N)","name":"LTRIM"},{"acl_categories":["@read","@list","@slow"],"complexity":"O(S+N)","name":"LRANGE"}],"description":"Capped lists: Use LTRIM with positive indexes to keep a range of elements from the beginning when you need to maintain a fixed-size list","difficulty":"intermediate","id":"ltrim","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_list_tutorial-stepltrim"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_list_tutorial-stepltrim"},{"id":"Node-js","panelId":"panel_Nodejs_list_tutorial-stepltrim"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_list_tutorial-stepltrim"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_list_tutorial-stepltrim"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_list_tutorial-stepltrim"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_list_tutorial-stepltrim"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_list_tutorial-stepltrim"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_list_tutorial-stepltrim"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_list_tutorial-stepltrim"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_list_tutorial-stepltrim"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_list_tutorial-stepltrim"}]},{"buildsUpon":["lpush_rpush"],"codetabsId":"list_tutorial-stepltrim_end_of_list","commands":[{"acl_categories":["@keyspace","@write","@slow"],"complexity":"O(N)","name":"DEL"},{"acl_categories":["@write","@list","@fast"],"complexity":"O(1)","name":"RPUSH"},{"acl_categories":["@write","@list","@slow"],"complexity":"O(N)","name":"LTRIM"},{"acl_categories":["@read","@list","@slow"],"complexity":"O(S+N)","name":"LRANGE"}],"description":"Capped lists with negative indexes: Use LTRIM with negative indexes to keep the most recent elements when you need to maintain a fixed-size list of latest items","difficulty":"intermediate","id":"ltrim_end_of_list","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_list_tutorial-stepltrim_end_of_list"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_list_tutorial-stepltrim_end_of_list"},{"id":"Node-js","panelId":"panel_Nodejs_list_tutorial-stepltrim_end_of_list"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_list_tutorial-stepltrim_end_of_list"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_list_tutorial-stepltrim_end_of_list"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_list_tutorial-stepltrim_end_of_list"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_list_tutorial-stepltrim_end_of_list"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_list_tutorial-stepltrim_end_of_list"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_list_tutorial-stepltrim_end_of_list"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_list_tutorial-stepltrim_end_of_list"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_list_tutorial-stepltrim_end_of_list"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_list_tutorial-stepltrim_end_of_list"}]},{"buildsUpon":["lpush_rpush","lpop_rpop"],"codetabsId":"list_tutorial-stepbrpop","commands":[{"acl_categories":["@keyspace","@write","@slow"],"complexity":"O(N)","name":"DEL"},{"acl_categories":["@write","@list","@fast"],"complexity":"O(1)","name":"RPUSH"},{"acl_categories":["@write","@list","@slow","@blocking"],"complexity":"O(N)","name":"BRPOP"}],"description":"Blocking operations: Use BRPOP to wait for elements with a timeout when you need to implement producer-consumer patterns without polling","difficulty":"intermediate","id":"brpop","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_list_tutorial-stepbrpop"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_list_tutorial-stepbrpop"},{"id":"Node-js","panelId":"panel_Nodejs_list_tutorial-stepbrpop"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_list_tutorial-stepbrpop"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_list_tutorial-stepbrpop"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_list_tutorial-stepbrpop"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_list_tutorial-stepbrpop"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_list_tutorial-stepbrpop"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_list_tutorial-stepbrpop"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_list_tutorial-stepbrpop"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_list_tutorial-stepbrpop"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_list_tutorial-stepbrpop"}]},{"codetabsId":"list_tutorial-steprule_1","commands":[{"acl_categories":["@keyspace","@write","@slow"],"complexity":"O(N)","name":"DEL"},{"acl_categories":["@write","@list","@fast"],"complexity":"O(1)","name":"LPUSH"}],"description":"Automatic creation: Redis automatically creates a list when you push to a non-existent key, simplifying initialization","difficulty":"beginner","id":"rule_1","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_list_tutorial-steprule_1"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_list_tutorial-steprule_1"},{"id":"Node-js","panelId":"panel_Nodejs_list_tutorial-steprule_1"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_list_tutorial-steprule_1"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_list_tutorial-steprule_1"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_list_tutorial-steprule_1"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_list_tutorial-steprule_1"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_list_tutorial-steprule_1"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_list_tutorial-steprule_1"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_list_tutorial-steprule_1"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_list_tutorial-steprule_1"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_list_tutorial-steprule_1"}]},{"buildsUpon":["rule_1"],"codetabsId":"list_tutorial-steprule_1.1","commands":[{"acl_categories":["@keyspace","@write","@slow"],"complexity":"O(N)","name":"DEL"},{"acl_categories":["@write","@string","@slow"],"complexity":"O(1)","name":"SET"},{"acl_categories":["@keyspace","@read","@fast"],"complexity":"O(1)","name":"TYPE"},{"acl_categories":["@write","@list","@fast"],"complexity":"O(1)","name":"LPUSH"}],"description":"Type safety: Redis prevents operations on wrong data types, returning WRONGTYPE error when you try to use list commands on non-list keys","difficulty":"beginner","id":"rule_1.1","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_list_tutorial-steprule_1.1"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_list_tutorial-steprule_1.1"},{"id":"Node-js","panelId":"panel_Nodejs_list_tutorial-steprule_1.1"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_list_tutorial-steprule_1.1"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_list_tutorial-steprule_1.1"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_list_tutorial-steprule_1.1"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_list_tutorial-steprule_1.1"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_list_tutorial-steprule_1.1"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_list_tutorial-steprule_1.1"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_list_tutorial-steprule_1.1"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_list_tutorial-steprule_1.1"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_list_tutorial-steprule_1.1"}]},{"buildsUpon":["lpush_rpush","lpop_rpop"],"codetabsId":"list_tutorial-steprule_2","commands":[{"acl_categories":["@keyspace","@write","@slow"],"complexity":"O(N)","name":"DEL"},{"acl_categories":["@write","@list","@fast"],"complexity":"O(1)","name":"LPUSH"},{"acl_categories":["@keyspace","@read","@fast"],"complexity":"O(N)","name":"EXISTS"},{"acl_categories":["@write","@list","@fast"],"complexity":"O(N)","name":"LPOP"}],"description":"Automatic removal: Redis automatically deletes empty lists, freeing memory when the last element is removed","difficulty":"beginner","id":"rule_2","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_list_tutorial-steprule_2"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_list_tutorial-steprule_2"},{"id":"Node-js","panelId":"panel_Nodejs_list_tutorial-steprule_2"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_list_tutorial-steprule_2"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_list_tutorial-steprule_2"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_list_tutorial-steprule_2"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_list_tutorial-steprule_2"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_list_tutorial-steprule_2"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_list_tutorial-steprule_2"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_list_tutorial-steprule_2"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_list_tutorial-steprule_2"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_list_tutorial-steprule_2"}]},{"codetabsId":"list_tutorial-steprule_3","commands":[{"acl_categories":["@keyspace","@write","@slow"],"complexity":"O(N)","name":"DEL"},{"acl_categories":["@read","@list","@fast"],"complexity":"O(1)","name":"LLEN"},{"acl_categories":["@write","@list","@fast"],"complexity":"O(N)","name":"LPOP"}],"description":"Nil handling: Read-only commands on non-existent keys return empty results (0 or nil) instead of errors, treating them as empty lists","difficulty":"beginner","id":"rule_3","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_list_tutorial-steprule_3"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_list_tutorial-steprule_3"},{"id":"Node-js","panelId":"panel_Nodejs_list_tutorial-steprule_3"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_list_tutorial-steprule_3"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_list_tutorial-steprule_3"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_list_tutorial-steprule_3"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_list_tutorial-steprule_3"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_list_tutorial-steprule_3"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_list_tutorial-steprule_3"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_list_tutorial-steprule_3"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_list_tutorial-steprule_3"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_list_tutorial-steprule_3"}]}]
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


### List command summary

**24 commands in this group:**

[View all list commands](https://redis.io/commands/?group=list)

| Command | Summary | Complexity | Since |
|---------|---------|------------|-------|
| [BLMOVE](https://redis.io/commands/blmove/) | Pops an element from a list, pushes it to another list and returns it. Blocks until an element is available otherwise. Deletes the list if the last element was moved. | O(1) | 6.2.0 |
| [BLMOVEM](https://redis.io/commands/blmovem/) | Moves up to (or exactly) a number of elements from one list to another and returns them. Blocks until the elements are available otherwise. Deletes the source list if it becomes empty. | O(N) where N is the number of elements moved. | 8.10.0 |
| [BLMPOP](https://redis.io/commands/blmpop/) | Pops the first element from one of multiple lists. Blocks until an element is available otherwise. Deletes the list if the last element was popped. | O(N+M) where N is the number of provided keys a... | 7.0.0 |
| [BLPOP](https://redis.io/commands/blpop/) | Removes and returns the first element in a list. Blocks until an element is available otherwise. Deletes the list if the last element was popped. | O(N) where N is the number of provided keys. | 2.0.0 |
| [BRPOP](https://redis.io/commands/brpop/) | Removes and returns the last element in a list. Blocks until an element is available otherwise. Deletes the list if the last element was popped. | O(N) where N is the number of provided keys. | 2.0.0 |
| [BRPOPLPUSH](https://redis.io/commands/brpoplpush/) | Pops an element from a list, pushes it to another list and returns it. Block until an element is available otherwise. Deletes the list if the last element was popped. | O(1) | 2.2.0 |
| [LINDEX](https://redis.io/commands/lindex/) | Returns an element from a list by its index. | O(N) where N is the number of elements to trave... | 1.0.0 |
| [LINSERT](https://redis.io/commands/linsert/) | Inserts an element before or after another element in a list. | O(N) where N is the number of elements to trave... | 2.2.0 |
| [LLEN](https://redis.io/commands/llen/) | Returns the length of a list. | O(1) | 1.0.0 |
| [LMOVE](https://redis.io/commands/lmove/) | Returns an element after popping it from one list and pushing it to another. Deletes the list if the last element was moved. | O(1) | 6.2.0 |

#### List command summary (part 2)

| Command | Summary | Complexity | Since |
|---------|---------|------------|-------|
| [LMOVEM](https://redis.io/commands/lmovem/) | Moves up to (or exactly) a number of elements from one list to another and returns them. Deletes the source list if it becomes empty. | O(N) where N is the number of elements moved. | 8.10.0 |
| [LMPOP](https://redis.io/commands/lmpop/) | Returns multiple elements from a list after removing them. Deletes the list if the last element was popped. | O(N+M) where N is the number of provided keys a... | 7.0.0 |
| [LPOP](https://redis.io/commands/lpop/) | Returns the first elements in a list after removing it. Deletes the list if the last element was popped. | O(N) where N is the number of elements returned | 1.0.0 |
| [LPOS](https://redis.io/commands/lpos/) | Returns the index of matching elements in a list. | O(N) where N is the number of elements in the l... | 6.0.6 |
| [LPUSH](https://redis.io/commands/lpush/) | Prepends one or more elements to a list. Creates the key if it doesn't exist. | O(1) for each element added, so O(N) to add N e... | 1.0.0 |
| [LPUSHX](https://redis.io/commands/lpushx/) | Prepends one or more elements to a list only when the list exists. | O(1) for each element added, so O(N) to add N e... | 2.2.0 |
| [LRANGE](https://redis.io/commands/lrange/) | Returns a range of elements from a list. | O(S+N) where S is the distance of start offset ... | 1.0.0 |
| [LREM](https://redis.io/commands/lrem/) | Removes elements from a list. Deletes the list if the last element was removed. | O(N+M) where N is the length of the list and M ... | 1.0.0 |
| [LSET](https://redis.io/commands/lset/) | Sets the value of an element in a list by its index. | O(N) where N is the length of the list. Setting... | 1.0.0 |
| [LTRIM](https://redis.io/commands/ltrim/) | Removes elements from both ends a list. Deletes the list if all elements were trimmed. | O(N) where N is the number of elements to be re... | 1.0.0 |

#### List command summary (part 3)

| Command | Summary | Complexity | Since |
|---------|---------|------------|-------|
| [RPOP](https://redis.io/commands/rpop/) | Returns and removes the last elements of a list. Deletes the list if the last element was popped. | O(N) where N is the number of elements returned | 1.0.0 |
| [RPOPLPUSH](https://redis.io/commands/rpoplpush/) | Returns the last element of a list after removing and pushing it to another list. Deletes the list if the last element was popped. | O(1) | 1.2.0 |
| [RPUSH](https://redis.io/commands/rpush/) | Appends one or more elements to a list. Creates the key if it doesn't exist. | O(1) for each element added, so O(N) to add N e... | 1.0.0 |
| [RPUSHX](https://redis.io/commands/rpushx/) | Appends an element to a list only when the list exists. | O(1) for each element added, so O(N) to add N e... | 2.2.0 |



Redis lists are linked lists of string values.
Redis lists are frequently used to:

* Implement stacks and queues.
* Build queue management for background worker systems.

## Examples

* Treat a list like a queue (first in, first out):
Queue pattern: Use LPUSH to add items and RPOP to remove them in FIFO order when you need to process items in the order they were added

**Builds upon:** lpush_rpush, lpop_rpop

**Commands:** LPUSH, RPOP

**Complexity:**
- LPUSH: O(1)
- RPOP: O(N)

**Available in:** Redis CLI, C#, C#, Go, Java (Asynchronous - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> LPUSH bikes:repairs bike:1
(integer) 1
> LPUSH bikes:repairs bike:2
(integer) 2
> RPOP bikes:repairs
"bike:1"
> RPOP bikes:repairs
"bike:2"
```

##### C#

```csharp
        long res1 = db.ListLeftPush("bikes:repairs", "bike:1");
        Console.WriteLine(res1);    // >>> 1

        long res2 = db.ListLeftPush("bikes:repairs", "bike:2");
        Console.WriteLine(res2);    // >>> 2

        RedisValue res3 = db.ListRightPop("bikes:repairs");
        Console.WriteLine(res3);    // >>> "bike:1"

        RedisValue res4 = db.ListRightPop("bikes:repairs");
        Console.WriteLine(res4); // >>> "bike:2"
```

##### C#

```csharp
        long res1 = db.ListLeftPush("bikes:repairs", "bike:1");
        Console.WriteLine(res1);    // >>> 1

        long res2 = db.ListLeftPush("bikes:repairs", "bike:2");
        Console.WriteLine(res2);    // >>> 2

        RedisValue res3 = db.ListRightPop("bikes:repairs");
        Console.WriteLine(res3);    // >>> "bike:1"

        RedisValue res4 = db.ListRightPop("bikes:repairs");
        Console.WriteLine(res4); // >>> "bike:2"
```

##### C#

```csharp
        long res1 = db.ListLeftPush("bikes:repairs", "bike:1");
        Console.WriteLine(res1);    // >>> 1

        long res2 = db.ListLeftPush("bikes:repairs", "bike:2");
        Console.WriteLine(res2);    // >>> 2

        RedisValue res3 = db.ListRightPop("bikes:repairs");
        Console.WriteLine(res3);    // >>> "bike:1"

        RedisValue res4 = db.ListRightPop("bikes:repairs");
        Console.WriteLine(res4); // >>> "bike:2"
```

##### C#

```csharp
        long res1 = db.ListLeftPush("bikes:repairs", "bike:1");
        Console.WriteLine(res1);    // >>> 1

        long res2 = db.ListLeftPush("bikes:repairs", "bike:2");
        Console.WriteLine(res2);    // >>> 2

        RedisValue res3 = db.ListRightPop("bikes:repairs");
        Console.WriteLine(res3);    // >>> "bike:1"

        RedisValue res4 = db.ListRightPop("bikes:repairs");
        Console.WriteLine(res4); // >>> "bike:2"
```

##### Go

```go
	res1, err := rdb.LPush(ctx, "bikes:repairs", "bike:1").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // >>> 1

	res2, err := rdb.LPush(ctx, "bikes:repairs", "bike:2").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2) // >>> 2

	res3, err := rdb.RPop(ctx, "bikes:repairs").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3) // >>> bike:1

	res4, err := rdb.RPop(ctx, "bikes:repairs").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4) // >>> bike:2
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> queue = asyncCommands.lpush("bikes:repairs", "bike:1").thenCompose(res1 -> {
                System.out.println(res1); // >>> 1

                return asyncCommands.lpush("bikes:repairs", "bike:2");
            }).thenCompose(res2 -> {
                System.out.println(res2); // >>> 2

                return asyncCommands.rpop("bikes:repairs");
            }).thenCompose(res3 -> {
                System.out.println(res3); // >>> bike:1

                return asyncCommands.rpop("bikes:repairs");
            })
                    .thenAccept(System.out::println) // >>> bike:2
                    .toCompletableFuture();
```

##### Java (Synchronous - Jedis)

```java
        long res1 = jedis.lpush("bikes:repairs", "bike:1");
        System.out.println(res1);  // >>> 1

        long res2 = jedis.lpush("bikes:repairs", "bike:2");
        System.out.println(res2);  // >>> 2

        String res3 = jedis.rpop("bikes:repairs");
        System.out.println(res3);  // >>> bike:1

        String res4 = jedis.rpop("bikes:repairs");
        System.out.println(res4); // >>> bike:2
```

##### JavaScript (Node.js)

```javascript
const res1 = await client.lPush('bikes:repairs', 'bike:1');
console.log(res1);  // 1

const res2 = await client.lPush('bikes:repairs', 'bike:2');
console.log(res2);  // 2

const res3 = await client.rPop('bikes:repairs');
console.log(res3);  // bike:1

const res4 = await client.rPop('bikes:repairs');
console.log(res4);  // bike:2
```

##### PHP

```php
        $res1 = $r->lpush('bikes:repairs', 'bike:1');
        echo $res1 . PHP_EOL;
        // >>> 1

        $res2 = $r->lpush('bikes:repairs', 'bike:2');
        echo $res2 . PHP_EOL;
        // >>> 2

        $res3 = $r->rpop('bikes:repairs');
        echo $res3 . PHP_EOL;
        // >>> bike:1

        $res4 = $r->rpop('bikes:repairs');
        echo $res4 . PHP_EOL;
        // >>> bike:2
```

##### Python

```python
res1 = r.lpush("bikes:repairs", "bike:1")
print(res1)  # >>> 1

res2 = r.lpush("bikes:repairs", "bike:2")
print(res2)  # >>> 2

res3 = r.rpop("bikes:repairs")
print(res3)  # >>> bike:1

res4 = r.rpop("bikes:repairs")
print(res4)  # >>> bike:2
```

##### Ruby

```ruby
res1 = r.lpush('bikes:repairs', 'bike:1')
puts res1 # >>> 1

res2 = r.lpush('bikes:repairs', 'bike:2')
puts res2 # >>> 2

res3 = r.rpop('bikes:repairs')
puts res3 # >>> bike:1

res4 = r.rpop('bikes:repairs')
puts res4 # >>> bike:2
```

##### Rust (Asynchronous)

```rust
        if let Ok(res) = r.lpush("bikes:repairs", "bike:1").await {
            let res: usize = res;
            println!("{res}"); // >>> 1
        }

        if let Ok(res) = r.lpush("bikes:repairs", "bike:2").await {
            let res: usize = res;
            println!("{res}"); // >>> 2
        }

        if let Ok(res) = r.rpop("bikes:repairs", None).await {
            let res: Option<String> = res;
            print_optional_string(res.clone()); // >>> bike:1
        }

        if let Ok(res) = r.rpop("bikes:repairs", None).await {
            let res: Option<String> = res;
            print_optional_string(res.clone()); // >>> bike:2
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.lpush("bikes:repairs", "bike:1") {
            let res: usize = res;
            println!("{res}"); // >>> 1
        }

        if let Ok(res) = r.lpush("bikes:repairs", "bike:2") {
            let res: usize = res;
            println!("{res}"); // >>> 2
        }

        if let Ok(res) = r.rpop("bikes:repairs", None) {
            let res: Option<String> = res;
            print_optional_string(res.clone()); // >>> bike:1
        }

        if let Ok(res) = r.rpop("bikes:repairs", None) {
            let res: Option<String> = res;
            print_optional_string(res.clone()); // >>> bike:2
        }
```



* Treat a list like a stack (first in, last out):
Stack pattern: Use LPUSH to add items and LPOP to remove them in LIFO order when you need to process items in reverse order

**Builds upon:** lpush_rpush

**Commands:** LPUSH, LPOP

**Complexity:**
- LPUSH: O(1)
- LPOP: O(N)

**Available in:** Redis CLI, C#, C#, Go, Java (Asynchronous - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> LPUSH bikes:repairs bike:1
(integer) 1
> LPUSH bikes:repairs bike:2
(integer) 2
> LPOP bikes:repairs
"bike:2"
> LPOP bikes:repairs
"bike:1"
```

##### C#

```csharp
        long res5 = db.ListLeftPush("bikes:repairs", "bike:1");
        Console.WriteLine(res5);    // >>> 1

        long res6 = db.ListLeftPush("bikes:repairs", "bike:2");
        Console.WriteLine(res6);    // >>> 2

        RedisValue res7 = db.ListLeftPop("bikes:repairs");
        Console.WriteLine(res7);    // >>> "bike:2"

        RedisValue res8 = db.ListLeftPop("bikes:repairs");
        Console.WriteLine(res8);    // >>> "bike:1"
```

##### C#

```csharp
        long res5 = db.ListLeftPush("bikes:repairs", "bike:1");
        Console.WriteLine(res5);    // >>> 1

        long res6 = db.ListLeftPush("bikes:repairs", "bike:2");
        Console.WriteLine(res6);    // >>> 2

        RedisValue res7 = db.ListLeftPop("bikes:repairs");
        Console.WriteLine(res7);    // >>> "bike:2"

        RedisValue res8 = db.ListLeftPop("bikes:repairs");
        Console.WriteLine(res8);    // >>> "bike:1"
```

##### C#

```csharp
        long res5 = db.ListLeftPush("bikes:repairs", "bike:1");
        Console.WriteLine(res5);    // >>> 1

        long res6 = db.ListLeftPush("bikes:repairs", "bike:2");
        Console.WriteLine(res6);    // >>> 2

        RedisValue res7 = db.ListLeftPop("bikes:repairs");
        Console.WriteLine(res7);    // >>> "bike:2"

        RedisValue res8 = db.ListLeftPop("bikes:repairs");
        Console.WriteLine(res8);    // >>> "bike:1"
```

##### C#

```csharp
        long res5 = db.ListLeftPush("bikes:repairs", "bike:1");
        Console.WriteLine(res5);    // >>> 1

        long res6 = db.ListLeftPush("bikes:repairs", "bike:2");
        Console.WriteLine(res6);    // >>> 2

        RedisValue res7 = db.ListLeftPop("bikes:repairs");
        Console.WriteLine(res7);    // >>> "bike:2"

        RedisValue res8 = db.ListLeftPop("bikes:repairs");
        Console.WriteLine(res8);    // >>> "bike:1"
```

##### Go

```go
	res5, err := rdb.LPush(ctx, "bikes:repairs", "bike:1").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res5) // >>> 1

	res6, err := rdb.LPush(ctx, "bikes:repairs", "bike:2").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res6) // >>> 2

	res7, err := rdb.LPop(ctx, "bikes:repairs").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res7) // >>> bike:2

	res8, err := rdb.LPop(ctx, "bikes:repairs").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res8) // >>> bike:1
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> stack = asyncCommands.lpush("bikes:repairs", "bike:1").thenCompose(res4 -> {
                System.out.println(res4); // >>> 1

                return asyncCommands.lpush("bikes:repairs", "bike:2");
            }).thenCompose(res5 -> {
                System.out.println(res5); // >>> 2

                return asyncCommands.lpop("bikes:repairs");
            }).thenCompose(res6 -> {
                System.out.println(res6); // >>> bike:2

                return asyncCommands.lpop("bikes:repairs");
            })
                    .thenAccept(System.out::println) // >>> bike:1
                    .toCompletableFuture();
```

##### Java (Synchronous - Jedis)

```java
        long res5 = jedis.lpush("bikes:repairs", "bike:1");
        System.out.println(res5);  // >>> 1

        long res6 = jedis.lpush("bikes:repairs", "bike:2");
        System.out.println(res6);  // >>> 2

        String res7 = jedis.lpop("bikes:repairs");
        System.out.println(res7);  // >>> bike:2

        String res8 = jedis.lpop("bikes:repairs");
        System.out.println(res8);  // >>> bike:1
```

##### JavaScript (Node.js)

```javascript
const res5 = await client.lPush('bikes:repairs', 'bike:1');
console.log(res5);  // 1

const res6 = await client.lPush('bikes:repairs', 'bike:2');
console.log(res6); // 2

const res7 = await client.lPop('bikes:repairs');
console.log(res7);  // bike:2

const res8 = await client.lPop('bikes:repairs');
console.log(res8);  // bike:1
```

##### PHP

```php
        $res5 = $r->lpush('bikes:repairs', 'bike:1');
        echo $res5 . PHP_EOL;
        // >>> 1

        $res6 = $r->lpush('bikes:repairs', 'bike:2');
        echo $res6 . PHP_EOL;
        // >>> 2

        $res7 = $r->lpop('bikes:repairs');
        echo $res7 . PHP_EOL;
        // >>> bike:2

        $res8 = $r->lpop('bikes:repairs');
        echo $res8 . PHP_EOL;
        // >>> bike:1
```

##### Python

```python
res5 = r.lpush("bikes:repairs", "bike:1")
print(res5)  # >>> 1

res6 = r.lpush("bikes:repairs", "bike:2")
print(res6)  # >>> 2

res7 = r.lpop("bikes:repairs")
print(res7)  # >>> bike:2

res8 = r.lpop("bikes:repairs")
print(res8)  # >>> bike:1
```

##### Ruby

```ruby
res5 = r.lpush('bikes:repairs', 'bike:1')
puts res5 # >>> 1

res6 = r.lpush('bikes:repairs', 'bike:2')
puts res6 # >>> 2

res7 = r.lpop('bikes:repairs')
puts res7 # >>> bike:2

res8 = r.lpop('bikes:repairs')
puts res8 # >>> bike:1
```

##### Rust (Asynchronous)

```rust
        if let Ok(res) = r.lpush("bikes:repairs", "bike:1").await {
            let res: usize = res;
            println!("{res}"); // >>> 1
        }

        if let Ok(res) = r.lpush("bikes:repairs", "bike:2").await {
            let res: usize = res;
            println!("{res}"); // >>> 2
        }

        if let Ok(res) = r.lpop("bikes:repairs", None).await {
            let res: Option<String> = res;
            print_optional_string(res.clone()); // >>> bike:2
        }

        if let Ok(res) = r.lpop("bikes:repairs", None).await {
            let res: Option<String> = res;
            print_optional_string(res.clone()); // >>> bike:1
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.lpush("bikes:repairs", "bike:1") {
            let res: usize = res;
            println!("{res}"); // >>> 1
        }

        if let Ok(res) = r.lpush("bikes:repairs", "bike:2") {
            let res: usize = res;
            println!("{res}"); // >>> 2
        }

        if let Ok(res) = r.lpop("bikes:repairs", None) {
            let res: Option<String> = res;
            print_optional_string(res.clone()); // >>> bike:2
        }

        if let Ok(res) = r.lpop("bikes:repairs", None) {
            let res: Option<String> = res;
            print_optional_string(res.clone()); // >>> bike:1
        }
```



* Check the length of a list:
Foundational: Get the number of elements in a list using LLEN to check list size

**Commands:** LLEN

**Complexity:**
- LLEN: O(1)

**Available in:** Redis CLI, C#, C#, Go, Java (Asynchronous - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> LLEN bikes:repairs
(integer) 0
```

##### C#

```csharp
        long res9 = db.ListLength("bikes:repairs");
        Console.WriteLine(res9);    // >>> 0
```

##### C#

```csharp
        long res9 = db.ListLength("bikes:repairs");
        Console.WriteLine(res9);    // >>> 0
```

##### C#

```csharp
        long res9 = db.ListLength("bikes:repairs");
        Console.WriteLine(res9);    // >>> 0
```

##### C#

```csharp
        long res9 = db.ListLength("bikes:repairs");
        Console.WriteLine(res9);    // >>> 0
```

##### Go

```go
	res9, err := rdb.LLen(ctx, "bikes:repairs").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res9) // >>> 0
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> llen = asyncCommands.llen("bikes:repairs")
                    .thenAccept(System.out::println) // >>> 0
                    .toCompletableFuture();
```

##### Java (Synchronous - Jedis)

```java
        long res9 = jedis.llen("bikes:repairs");
        System.out.println(res9);  // >>> 0
```

##### JavaScript (Node.js)

```javascript
const res9 = await client.lLen('bikes:repairs');
console.log(res9); // 0
```

##### PHP

```php
        $res9 = $r->llen('bikes:repairs');
        echo $res9 . PHP_EOL;
        // >>> 0
```

##### Python

```python
res9 = r.llen("bikes:repairs")
print(res9)  # >>> 0
```

##### Ruby

```ruby
res9 = r.llen('bikes:repairs')
puts res9 # >>> 0
```

##### Rust (Asynchronous)

```rust
        if let Ok(res) = r.llen("bikes:repairs").await {
            let res: usize = res;
            println!("{res}"); // >>> 0
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.llen("bikes:repairs") {
            let res: usize = res;
            println!("{res}"); // >>> 0
        }
```



* Atomically pop an element from one list and push to another:
Atomic transfer: Use LMOVE to move elements between lists in a single operation when you need to transfer items without race conditions

**Difficulty:** Intermediate

**Builds upon:** lpush_rpush, lpop_rpop

**Commands:** LPUSH, LMOVE, LRANGE

**Complexity:**
- LPUSH: O(1)
- LMOVE: O(1)
- LRANGE: O(S+N)

**Available in:** Redis CLI, C#, C#, Go, Java (Asynchronous - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> LPUSH bikes:repairs bike:1
(integer) 1
> LPUSH bikes:repairs bike:2
(integer) 2
> LMOVE bikes:repairs bikes:finished LEFT LEFT
"bike:2"
> LRANGE bikes:repairs 0 -1
1) "bike:1"
> LRANGE bikes:finished 0 -1
1) "bike:2"
```

##### C#

```csharp
        long res10 = db.ListLeftPush("{bikes}:repairs", "bike:1");
        Console.WriteLine(res10);   // >>> 1

        long res11 = db.ListLeftPush("{bikes}:repairs", "bike:2");
        Console.WriteLine(res11);   // >>> 2

        RedisValue res12 = db.ListMove("{bikes}:repairs", "{bikes}:finished", ListSide.Left, ListSide.Left);
        Console.Write(res12);   // >>> "bike:2"

        RedisValue[] res13 = db.ListRange("{bikes}:repairs", 0, -1);
        Console.WriteLine(string.Join(", ", res13));    // >>> "bike:1"

        RedisValue[] res14 = db.ListRange("{bikes}:finished", 0, -1);
        Console.WriteLine(string.Join(", ", res14));    // >>> "bike:2"
```

##### C#

```csharp
        long res10 = db.ListLeftPush("{bikes}:repairs", "bike:1");
        Console.WriteLine(res10);   // >>> 1

        long res11 = db.ListLeftPush("{bikes}:repairs", "bike:2");
        Console.WriteLine(res11);   // >>> 2

        RedisValue res12 = db.ListMove("{bikes}:repairs", "{bikes}:finished", ListSide.Left, ListSide.Left);
        Console.Write(res12);   // >>> "bike:2"

        RedisValue[] res13 = db.ListRange("{bikes}:repairs", 0, -1);
        Console.WriteLine(string.Join(", ", res13));    // >>> "bike:1"

        RedisValue[] res14 = db.ListRange("{bikes}:finished", 0, -1);
        Console.WriteLine(string.Join(", ", res14));    // >>> "bike:2"
```

##### C#

```csharp
        long res10 = db.ListLeftPush("{bikes}:repairs", "bike:1");
        Console.WriteLine(res10);   // >>> 1

        long res11 = db.ListLeftPush("{bikes}:repairs", "bike:2");
        Console.WriteLine(res11);   // >>> 2

        RedisValue res12 = db.ListMove("{bikes}:repairs", "{bikes}:finished", ListSide.Left, ListSide.Left);
        Console.Write(res12);   // >>> "bike:2"

        RedisValue[] res13 = db.ListRange("{bikes}:repairs", 0, -1);
        Console.WriteLine(string.Join(", ", res13));    // >>> "bike:1"

        RedisValue[] res14 = db.ListRange("{bikes}:finished", 0, -1);
        Console.WriteLine(string.Join(", ", res14));    // >>> "bike:2"
```

##### C#

```csharp
        long res10 = db.ListLeftPush("{bikes}:repairs", "bike:1");
        Console.WriteLine(res10);   // >>> 1

        long res11 = db.ListLeftPush("{bikes}:repairs", "bike:2");
        Console.WriteLine(res11);   // >>> 2

        RedisValue res12 = db.ListMove("{bikes}:repairs", "{bikes}:finished", ListSide.Left, ListSide.Left);
        Console.Write(res12);   // >>> "bike:2"

        RedisValue[] res13 = db.ListRange("{bikes}:repairs", 0, -1);
        Console.WriteLine(string.Join(", ", res13));    // >>> "bike:1"

        RedisValue[] res14 = db.ListRange("{bikes}:finished", 0, -1);
        Console.WriteLine(string.Join(", ", res14));    // >>> "bike:2"
```

##### Go

```go
	res10, err := rdb.LPush(ctx, "bikes:repairs", "bike:1").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res10) // >>> 1

	res11, err := rdb.LPush(ctx, "bikes:repairs", "bike:2").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res11) // >>> 2

	res12, err := rdb.LMove(ctx, "bikes:repairs", "bikes:finished", "LEFT", "LEFT").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res12) // >>> bike:2

	res13, err := rdb.LRange(ctx, "bikes:repairs", 0, -1).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res13) // >>> [bike:1]

	res14, err := rdb.LRange(ctx, "bikes:finished", 0, -1).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res14) // >>> [bike:2]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> lmovelrange = asyncCommands.lpush("bikes:repairs", "bike:1").thenCompose(res7 -> {
                System.out.println(res7); // >>> 1

                return asyncCommands.lpush("bikes:repairs", "bike:2");
            }).thenCompose(res8 -> {
                System.out.println(res8); // >>> 2

                return asyncCommands.lmove("bikes:repairs", "bikes:finished", LMoveArgs.Builder.leftLeft());
            }).thenCompose(res9 -> {
                System.out.println(res9); // >>> bike:2

                return asyncCommands.lrange("bikes:repairs", 0, -1);
            }).thenCompose(res10 -> {
                System.out.println(res10); // >>> [bike:1]

                return asyncCommands.lrange("bikes:finished", 0, -1);
            })
                    .thenAccept(System.out::println) // >>> [bike:2]
                    .toCompletableFuture();
```

##### Java (Synchronous - Jedis)

```java
        long res10 = jedis.lpush("bikes:repairs", "bike:1");
        System.out.println(res10);  // >>> 1

        long res11 = jedis.lpush("bikes:repairs", "bike:2");
        System.out.println(res11);  // >>> 2

        String res12 = jedis.lmove("bikes:repairs", "bikes:finished", ListDirection.LEFT, ListDirection.LEFT);
        System.out.println(res12);  // >>> bike:2

        List<String> res13 = jedis.lrange("bikes:repairs", 0, -1);
        System.out.println(res13);  // >>> [bike:1]

        List<String> res14 = jedis.lrange("bikes:finished", 0, -1);
        System.out.println(res14);  // >>> [bike:2]
```

##### JavaScript (Node.js)

```javascript
const res10 = await client.lPush('bikes:repairs', 'bike:1');
console.log(res10);  // 1

const res11 = await client.lPush('bikes:repairs', 'bike:2');
console.log(res11);  // 2

const res12 = await client.lMove('bikes:repairs', 'bikes:finished', 'LEFT', 'LEFT');
console.log(res12);  // 'bike:2'

const res13 = await client.lRange('bikes:repairs', 0, -1);
console.log(res13);  // ['bike:1']

const res14 = await client.lRange('bikes:finished', 0, -1);
console.log(res14);  // ['bike:2']
```

##### PHP

```php
        $res10 = $r->lpush('bikes:repairs', 'bike:1');
        echo $res10 . PHP_EOL;
        // >>> 1

        $res11 = $r->lpush('bikes:repairs', 'bike:2');
        echo $res11 . PHP_EOL;
        // >>> 2

        $res12 = $r->lmove('bikes:repairs', 'bikes:finished', 'LEFT', 'LEFT');
        echo $res12 . PHP_EOL;
        // >>> 'bike:2'

        $res13 = $r->lrange('bikes:repairs', 0, -1);
        echo json_encode($res13) . PHP_EOL;
        // >>> ['bike:1']

        $res14 = $r->lrange('bikes:finished', 0, -1);
        echo json_encode($res14) . PHP_EOL;
        // >>> ['bike:2']
```

##### Python

```python
res10 = r.lpush("bikes:repairs", "bike:1")
print(res10)  # >>> 1

res11 = r.lpush("bikes:repairs", "bike:2")
print(res11)  # >>> 2

res12 = r.lmove("bikes:repairs", "bikes:finished", "LEFT", "LEFT")
print(res12)  # >>> 'bike:2'

res13 = r.lrange("bikes:repairs", 0, -1)
print(res13)  # >>> ['bike:1']

res14 = r.lrange("bikes:finished", 0, -1)
print(res14)  # >>> ['bike:2']
```

##### Ruby

```ruby
res10 = r.lpush('bikes:repairs', 'bike:1')
puts res10 # >>> 1

res11 = r.lpush('bikes:repairs', 'bike:2')
puts res11 # >>> 2

res12 = r.lmove('bikes:repairs', 'bikes:finished', 'LEFT', 'LEFT')
puts res12 # >>> bike:2

res13 = r.lrange('bikes:repairs', 0, -1)
puts res13.inspect # >>> ["bike:1"]

res14 = r.lrange('bikes:finished', 0, -1)
puts res14.inspect # >>> ["bike:2"]
```

##### Rust (Asynchronous)

```rust
        if let Ok(res) = r.lpush("bikes:repairs", "bike:1").await {
            let res: usize = res;
            println!("{res}"); // >>> 1
        }

        if let Ok(res) = r.lpush("bikes:repairs", "bike:2").await {
            let res: usize = res;
            println!("{res}"); // >>> 2
        }

        if let Ok(res) = r
            .lmove(
                "bikes:repairs",
                "bikes:finished",
                Direction::Left,
                Direction::Left,
            )
            .await
        {
            let res: String = res;
            println!("{res}"); // >>> bike:2
        }

        if let Ok(res) = r.lrange("bikes:repairs", 0, -1).await {
            let res: Vec<String> = res;
            println!("{res:?}"); // >>> ["bike:1"]
        }

        if let Ok(res) = r.lrange("bikes:finished", 0, -1).await {
            let res: Vec<String> = res;
            println!("{res:?}"); // >>> ["bike:2"]
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.lpush("bikes:repairs", "bike:1") {
            let res: usize = res;
            println!("{res}"); // >>> 1
        }

        if let Ok(res) = r.lpush("bikes:repairs", "bike:2") {
            let res: usize = res;
            println!("{res}"); // >>> 2
        }

        if let Ok(res) = r.lmove(
            "bikes:repairs",
            "bikes:finished",
            Direction::Left,
            Direction::Left,
        ) {
            let res: String = res;
            println!("{res}"); // >>> bike:2
        }

        if let Ok(res) = r.lrange("bikes:repairs", 0, -1) {
            let res: Vec<String> = res;
            println!("{res:?}"); // >>> ["bike:1"]
        }

        if let Ok(res) = r.lrange("bikes:finished", 0, -1) {
            let res: Vec<String> = res;
            println!("{res:?}"); // >>> ["bike:2"]
        }
```



* To limit the length of a list you can call [`LTRIM`](https://redis.io/docs/latest/commands/ltrim):
Capped lists: Use LTRIM to keep only a specific range of elements when you need to maintain a fixed-size list

**Difficulty:** Intermediate

**Builds upon:** lpush_rpush

**Commands:** DEL, RPUSH, LTRIM, LRANGE

**Complexity:**
- DEL: O(N)
- RPUSH: O(1)
- LTRIM: O(N)
- LRANGE: O(S+N)

**Available in:** Redis CLI, C#, C#, Go, Java (Asynchronous - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> DEL bikes:repairs
(integer) 1
> RPUSH bikes:repairs bike:1 bike:2 bike:3 bike:4 bike:5
(integer) 5
> LTRIM bikes:repairs 0 2
OK
> LRANGE bikes:repairs 0 -1
1) "bike:1"
2) "bike:2"
3) "bike:3"
```

##### C#

```csharp
        long res49 = db.ListLeftPush("bikes:repairs", ["bike:1", "bike:2", "bike:3", "bike:4", "bike:5"]);
        Console.WriteLine(res49);   // >>> 5

        db.ListTrim("bikes:repairs", 0, 2);
        RedisValue[] res50 = db.ListRange("bikes:repairs", 0, -1);
        Console.WriteLine(string.Join(", ", res50));    // >>> "bike:5, bike:4, bike:3"
```

##### C#

```csharp
        db.KeyDelete("bikes:repairs");

        long res49 = db.ListLeftPush("bikes:repairs", ["bike:1", "bike:2", "bike:3", "bike:4", "bike:5"]);
        Console.WriteLine(res49);   // >>> 5

        db.ListTrim("bikes:repairs", 0, 2);
        RedisValue[] res50 = db.ListRange("bikes:repairs", 0, -1);
        Console.WriteLine(string.Join(", ", res50));    // >>> "bike:5, bike:4, bike:3"
```

##### C#

```csharp
        long res49 = db.ListLeftPush("bikes:repairs", ["bike:1", "bike:2", "bike:3", "bike:4", "bike:5"]);
        Console.WriteLine(res49);   // >>> 5

        db.ListTrim("bikes:repairs", 0, 2);
        RedisValue[] res50 = db.ListRange("bikes:repairs", 0, -1);
        Console.WriteLine(string.Join(", ", res50));    // >>> "bike:5, bike:4, bike:3"
```

##### C#

```csharp
        db.KeyDelete("bikes:repairs");

        long res49 = db.ListLeftPush("bikes:repairs", ["bike:1", "bike:2", "bike:3", "bike:4", "bike:5"]);
        Console.WriteLine(res49);   // >>> 5

        db.ListTrim("bikes:repairs", 0, 2);
        RedisValue[] res50 = db.ListRange("bikes:repairs", 0, -1);
        Console.WriteLine(string.Join(", ", res50));    // >>> "bike:5, bike:4, bike:3"
```

##### Go

```go
	rdb.Del(ctx, "bikes:repairs")

	res51, err := rdb.LPush(ctx, "bikes:repairs", "bike:1", "bike:2", "bike:3", "bike:4", "bike:5").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res51) // >>> 5

	res52, err := rdb.LTrim(ctx, "bikes:repairs", 0, 2).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res52) // >>> OK

	res53, err := rdb.LRange(ctx, "bikes:repairs", 0, -1).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res53) // >>> [bike:5 bike:4 bike:3]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> ltrim1 = asyncCommands
                    .lpush("bikes:repairs", "bike:1", "bike:2", "bike:3", "bike:4", "bike:5").thenCompose(res37 -> {
                        System.out.println(res37); // >>> 5

                        return asyncCommands.ltrim("bikes:repairs", 0, 2);
                    }).thenCompose(res38 -> {
                        System.out.println(res38); // >>> OK

                        return asyncCommands.lrange("bikes:repairs", 0, -1);
                    })
                    .thenAccept(System.out::println) // >>> [bike:5, bike:4, bike:3]
                    .toCompletableFuture();
```

##### Java (Synchronous - Jedis)

```java
        jedis.del("bikes:repairs");

        long res48 = jedis.lpush("bikes:repairs", "bike:1", "bike:2", "bike:3", "bike:4", "bike:5");
        System.out.println(res48);  // >>> 5

        String res49 = jedis.ltrim("bikes:repairs", 0, 2);
        System.out.println(res49);  // >>> OK

        List<String> res50 = jedis.lrange("bikes:repairs", 0, -1);
        System.out.println(res50);  // >>> [bike:5, bike:4, bike:3]
```

##### JavaScript (Node.js)

```javascript
await client.del('bikes:repairs');

const res48 = await client.lPush(
  'bikes:repairs', ['bike:1', 'bike:2', 'bike:3', 'bike:4', 'bike:5']
);
console.log(res48);  // 5

const res49 = await client.lTrim('bikes:repairs', 0, 2);
console.log(res49);  // 'OK'

const res50 = await client.lRange('bikes:repairs', 0, -1);
console.log(res50);  // ['bike:5', 'bike:4', 'bike:3']
```

##### PHP

```php
        $res48 = $r->lpush('bikes:repairs', 'bike:1', 'bike:2', 'bike:3', 'bike:4', 'bike:5');
        echo $res48 . PHP_EOL;
        // >>> 5

        $res49 = $r->ltrim('bikes:repairs', 0, 2);
        echo $res49 . PHP_EOL;
        // >>> True

        $res50 = $r->lrange('bikes:repairs', 0, -1);
        echo json_encode($res50) . PHP_EOL;
        // >>> ['bike:5', 'bike:4', 'bike:3']
```

##### Python

```python
r.delete("bikes:repairs")

res48 = r.lpush("bikes:repairs", "bike:1", "bike:2", "bike:3", "bike:4", "bike:5")
print(res48)  # >>> 5

res49 = r.ltrim("bikes:repairs", 0, 2)
print(res49)  # >>> True

res50 = r.lrange("bikes:repairs", 0, -1)
print(res50)  # >>> ['bike:5', 'bike:4', 'bike:3']
```

##### Ruby

```ruby
r.del('bikes:repairs')

res15 = r.rpush('bikes:repairs', ['bike:1', 'bike:2', 'bike:3', 'bike:4', 'bike:5'])
puts res15 # >>> 5

res16 = r.ltrim('bikes:repairs', 0, 2)
puts res16 # >>> OK

res17 = r.lrange('bikes:repairs', 0, -1)
puts res17.inspect # >>> ["bike:1", "bike:2", "bike:3"]
```

##### Rust (Asynchronous)

```rust
        if let Ok(res) = r.del("bikes:repairs").await {
            let res: usize = res;
            println!("{res}"); // >>> 1
        }

        if let Ok(res) = r
            .rpush(
                "bikes:repairs",
                &["bike:1", "bike:2", "bike:3", "bike:4", "bike:5"],
            )
            .await
        {
            let res: usize = res;
            println!("{res}"); // >>> 5
        }

        if let Ok(res) = r.ltrim("bikes:repairs", 0, 2).await {
            let res: () = res;
            let _ = res;
            println!("OK"); // >>> OK
        }

        if let Ok(res) = r.lrange("bikes:repairs", 0, -1).await {
            let res: Vec<String> = res;
            println!("{res:?}"); // >>> ["bike:1", "bike:2", "bike:3"]
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.del("bikes:repairs") {
            let res: usize = res;
            println!("{res}"); // >>> 1
        }

        if let Ok(res) = r.rpush("bikes:repairs", &["bike:1", "bike:2", "bike:3", "bike:4", "bike:5"]) {
            let res: usize = res;
            println!("{res}"); // >>> 5
        }

        if let Ok(res) = r.ltrim("bikes:repairs", 0, 2) {
            let res: () = res;
            let _ = res;
            println!("OK"); // >>> OK
        }

        if let Ok(res) = r.lrange("bikes:repairs", 0, -1) {
            let res: Vec<String> = res;
            println!("{res:?}"); // >>> ["bike:1", "bike:2", "bike:3"]
        }
```



### What are Lists?

To explain the List data type it's better to start with a little bit of theory,
as the term *List* is often used in an improper way by information technology
folks. For instance "Python Lists" are not what the name may suggest (Linked
Lists), but rather Arrays (the same data type is called Array in
Ruby actually).

From a very general point of view a List is just a sequence of ordered
elements: 10,20,1,2,3 is a list. But the properties of a List implemented using
an Array are very different from the properties of a List implemented using a
*Linked List*.

Redis lists are implemented via Linked Lists. This means that even if you have
millions of elements inside a list, the operation of adding a new element in
the head or in the tail of the list is performed *in constant time*. The speed of adding a
new element with the [`LPUSH`](https://redis.io/docs/latest/commands/lpush) command to the head of a list with ten
elements is the same as adding an element to the head of list with 10
million elements.

What's the downside? Accessing an element *by index* is very fast in lists
implemented with an Array (constant time indexed access) and not so fast in
lists implemented by linked lists (where the operation requires an amount of
work proportional to the index of the accessed element).

Redis Lists are implemented with linked lists because for a database system it
is crucial to be able to add elements to a very long list in a very fast way.
Another strong advantage, as you'll see in a moment, is that Redis Lists can be
taken at constant length in constant time.

When fast access to the middle of a large collection of elements is important,
there is a different data structure that can be used, called sorted sets.
Sorted sets are covered in the [Sorted sets](https://redis.io/docs/latest/develop/data-types/sorted-sets) tutorial page.

### First steps with Redis Lists

The [`LPUSH`](https://redis.io/docs/latest/commands/lpush) command adds a new element into a list, on the
left (at the head), while the [`RPUSH`](https://redis.io/docs/latest/commands/rpush) command adds a new
element into a list, on the right (at the tail). Finally the
[`LRANGE`](https://redis.io/docs/latest/commands/lrange) command extracts ranges of elements from lists:

Foundational: Add elements to both ends of a list using LPUSH (left/head) and RPUSH (right/tail) to build ordered sequences

**Commands:** DEL, RPUSH, LPUSH, LRANGE

**Complexity:**
- DEL: O(N)
- RPUSH: O(1)
- LPUSH: O(1)
- LRANGE: O(S+N)

**Available in:** Redis CLI, C#, C#, Go, Java (Asynchronous - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> DEL bikes:repairs
(integer) 1
> RPUSH bikes:repairs bike:1
(integer) 1
> RPUSH bikes:repairs bike:2
(integer) 2
> LPUSH bikes:repairs bike:important_bike
(integer) 3
> LRANGE bikes:repairs 0 -1
1) "bike:important_bike"
2) "bike:1"
3) "bike:2"
```

##### C#

```csharp
        long res15 = db.ListRightPush("bikes:repairs", "bike:1");
        Console.WriteLine(res15);   // >>> 1

        long res16 = db.ListRightPush("bikes:repairs", "bike:2");
        Console.WriteLine(res16);   // >>> 2

        long res17 = db.ListLeftPush("bikes:repairs", "bike:important_bike");
        Console.WriteLine(res17);   // >>> 3

        RedisValue[] res18 = db.ListRange("bikes:repairs", 0, -1);
        Console.WriteLine(string.Join(", ", res18));    // >>> "bike:important_bike, bike:1, bike:2"
```

##### C#

```csharp
        db.KeyDelete("bikes:repairs");

        long res15 = db.ListRightPush("bikes:repairs", "bike:1");
        Console.WriteLine(res15);   // >>> 1

        long res16 = db.ListRightPush("bikes:repairs", "bike:2");
        Console.WriteLine(res16);   // >>> 2

        long res17 = db.ListLeftPush("bikes:repairs", "bike:important_bike");
        Console.WriteLine(res17);   // >>> 3

        RedisValue[] res18 = db.ListRange("bikes:repairs", 0, -1);
        Console.WriteLine(string.Join(", ", res18));    // >>> "bike:important_bike, bike:1, bike:2"
```

##### C#

```csharp
        long res15 = db.ListRightPush("bikes:repairs", "bike:1");
        Console.WriteLine(res15);   // >>> 1

        long res16 = db.ListRightPush("bikes:repairs", "bike:2");
        Console.WriteLine(res16);   // >>> 2

        long res17 = db.ListLeftPush("bikes:repairs", "bike:important_bike");
        Console.WriteLine(res17);   // >>> 3

        RedisValue[] res18 = db.ListRange("bikes:repairs", 0, -1);
        Console.WriteLine(string.Join(", ", res18));    // >>> "bike:important_bike, bike:1, bike:2"
```

##### C#

```csharp
        db.KeyDelete("bikes:repairs");

        long res15 = db.ListRightPush("bikes:repairs", "bike:1");
        Console.WriteLine(res15);   // >>> 1

        long res16 = db.ListRightPush("bikes:repairs", "bike:2");
        Console.WriteLine(res16);   // >>> 2

        long res17 = db.ListLeftPush("bikes:repairs", "bike:important_bike");
        Console.WriteLine(res17);   // >>> 3

        RedisValue[] res18 = db.ListRange("bikes:repairs", 0, -1);
        Console.WriteLine(string.Join(", ", res18));    // >>> "bike:important_bike, bike:1, bike:2"
```

##### Go

```go
	rdb.Del(ctx, "bikes:repairs")

	res15, err := rdb.RPush(ctx, "bikes:repairs", "bike:1").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res15) // >>> 1

	res16, err := rdb.RPush(ctx, "bikes:repairs", "bike:2").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res16) // >>> 2

	res17, err := rdb.LPush(ctx, "bikes:repairs", "bike:important_bike").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res17) // >>> 3

	res18, err := rdb.LRange(ctx, "bikes:repairs", 0, -1).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res18) // >>> [bike:important_bike bike:1 bike:2]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> lpushrpush = asyncCommands.rpush("bikes:repairs", "bike:1").thenCompose(res11 -> {
                System.out.println(res11); // >>> 1

                return asyncCommands.rpush("bikes:repairs", "bike:2");
            }).thenCompose(res12 -> {
                System.out.println(res12); // >>> 2

                return asyncCommands.lpush("bikes:repairs", "bike:important_bike");
            }).thenCompose(res13 -> {
                System.out.println(res13); // >>> 3

                return asyncCommands.lrange("bikes:repairs", 0, -1);
            })
                    .thenAccept(System.out::println)
                    // >>> [bike:important_bike, bike:1, bike:2]
                    .toCompletableFuture();
```

##### Java (Synchronous - Jedis)

```java
        jedis.del("bikes:repairs");

        long res15 = jedis.rpush("bikes:repairs", "bike:1");
        System.out.println(res15);  // >>> 1

        long res16 = jedis.rpush("bikes:repairs", "bike:2");
        System.out.println(res16);  // >>> 2

        long res17 = jedis.lpush("bikes:repairs", "bike:important_bike");
        System.out.println(res17);  // >>> 3

        List<String> res18 = jedis.lrange("bikes:repairs", 0, -1);
        System.out.println(res18);  // >>> [bike:important_bike, bike:1, bike:2]
```

##### JavaScript (Node.js)

```javascript
await client.del('bikes:repairs');

const res15 = await client.rPush('bikes:repairs', 'bike:1');
console.log(res15);  // 1

const res16 = await client.rPush('bikes:repairs', 'bike:2');
console.log(res16);  // 2

const res17 = await client.lPush('bikes:repairs', 'bike:important_bike');
console.log(res17);  // 3

const res18 = await client.lRange('bikes:repairs', 0, -1);
console.log(res18);  // ['bike:important_bike', 'bike:1', 'bike:2']
```

##### PHP

```php
        $r->del('bikes:repairs');
        
        $res15 = $r->rpush('bikes:repairs', 'bike:1');
        echo $res15 . PHP_EOL;
        // >>> 1

        $res16 = $r->rpush('bikes:repairs', 'bike:2');
        echo $res16 . PHP_EOL;
        // >>> 2

        $res17 = $r->lpush('bikes:repairs', 'bike:important_bike');
        echo $res17 . PHP_EOL;
        // >>> 3

        $res18 = $r->lrange('bikes:repairs', 0, -1);
        echo json_encode($res18) . PHP_EOL;
        // >>> ['bike:important_bike', 'bike:1', 'bike:2']
```

##### Python

```python
r.delete("bikes:repairs")

res15 = r.rpush("bikes:repairs", "bike:1")
print(res15)  # >>> 1

res16 = r.rpush("bikes:repairs", "bike:2")
print(res16)  # >>> 2

res17 = r.lpush("bikes:repairs", "bike:important_bike")
print(res17)  # >>> 3

res18 = r.lrange("bikes:repairs", 0, -1)
print(res18)  # >>> ['bike:important_bike', 'bike:1', 'bike:2']
```

##### Ruby

```ruby
r.del('bikes:repairs')

res18 = r.rpush('bikes:repairs', 'bike:1')
puts res18 # >>> 1

res19 = r.rpush('bikes:repairs', 'bike:2')
puts res19 # >>> 2

res20 = r.lpush('bikes:repairs', 'bike:important_bike')
puts res20 # >>> 3

res21 = r.lrange('bikes:repairs', 0, -1)
puts res21.inspect # >>> ["bike:important_bike", "bike:1", "bike:2"]
```

##### Rust (Asynchronous)

```rust
        let _: usize = r.del("bikes:repairs").await.unwrap_or(0);

        if let Ok(res) = r.rpush("bikes:repairs", "bike:1").await {
            let res: usize = res;
            println!("{res}"); // >>> 1
        }

        if let Ok(res) = r.rpush("bikes:repairs", "bike:2").await {
            let res: usize = res;
            println!("{res}"); // >>> 2
        }

        if let Ok(res) = r.lpush("bikes:repairs", "bike:important_bike").await {
            let res: usize = res;
            println!("{res}"); // >>> 3
        }

        if let Ok(res) = r.lrange("bikes:repairs", 0, -1).await {
            let res: Vec<String> = res;
            println!("{res:?}"); // >>> ["bike:important_bike", "bike:1", "bike:2"]
        }
```

##### Rust (Synchronous)

```rust
        let _: usize = r.del("bikes:repairs").unwrap_or(0);

        if let Ok(res) = r.rpush("bikes:repairs", "bike:1") {
            let res: usize = res;
            println!("{res}"); // >>> 1
        }

        if let Ok(res) = r.rpush("bikes:repairs", "bike:2") {
            let res: usize = res;
            println!("{res}"); // >>> 2
        }

        if let Ok(res) = r.lpush("bikes:repairs", "bike:important_bike") {
            let res: usize = res;
            println!("{res}"); // >>> 3
        }

        if let Ok(res) = r.lrange("bikes:repairs", 0, -1) {
            let res: Vec<String> = res;
            println!("{res:?}"); // >>> ["bike:important_bike", "bike:1", "bike:2"]
        }
```



Note that [`LRANGE`](https://redis.io/docs/latest/commands/lrange) takes two indexes, the first and the last
element of the range to return. Both the indexes can be negative, telling Redis
to start counting from the end: so -1 is the last element, -2 is the
penultimate element of the list, and so forth.

As you can see [`RPUSH`](https://redis.io/docs/latest/commands/rpush) appended the elements on the right of the list, while
the final [`LPUSH`](https://redis.io/docs/latest/commands/lpush) appended the element on the left.

Both commands are *variadic commands*, meaning that you are free to push
multiple elements into a list in a single call:

Variadic operations: Add multiple elements in a single command using LPUSH or RPUSH when you need to reduce round trips to the server

**Builds upon:** lpush_rpush

**Commands:** DEL, RPUSH, LPUSH, LRANGE

**Complexity:**
- DEL: O(N)
- RPUSH: O(1)
- LPUSH: O(1)
- LRANGE: O(S+N)

**Available in:** Redis CLI, C#, C#, Go, Java (Asynchronous - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> DEL bikes:repairs
(integer) 1
> RPUSH bikes:repairs bike:1 bike:2 bike:3
(integer) 3
> LPUSH bikes:repairs bike:important_bike bike:very_important_bike
> LRANGE bikes:repairs 0 -1
1) "bike:very_important_bike"
2) "bike:important_bike"
3) "bike:1"
4) "bike:2"
5) "bike:3"
```

##### C#

```csharp
        long res19 = db.ListRightPush("bikes:repairs", ["bike:1", "bike:2", "bike:3"]);
        Console.WriteLine(res19);   // >>> 3

        long res20 = db.ListLeftPush("bikes:repairs", ["bike:important_bike", "bike:very_important_bike"]);
        Console.WriteLine(res20);   // >>> 5

        RedisValue[] res21 = db.ListRange("bikes:repairs", 0, -1);
        Console.WriteLine(string.Join(", ", res21));
        // >>> "bike:very_important_bike, bike:important_bike, bike:1, bike:2, bike:3"
```

##### C#

```csharp
        db.KeyDelete("bikes:repairs");
        
        long res19 = db.ListRightPush("bikes:repairs", ["bike:1", "bike:2", "bike:3"]);
        Console.WriteLine(res19);   // >>> 3

        long res20 = db.ListLeftPush("bikes:repairs", ["bike:important_bike", "bike:very_important_bike"]);
        Console.WriteLine(res20);   // >>> 5

        RedisValue[] res21 = db.ListRange("bikes:repairs", 0, -1);
        Console.WriteLine(string.Join(", ", res21));
        // >>> "bike:very_important_bike, bike:important_bike, bike:1, bike:2, bike:3"
```

##### C#

```csharp
        long res19 = db.ListRightPush("bikes:repairs", ["bike:1", "bike:2", "bike:3"]);
        Console.WriteLine(res19);   // >>> 3

        long res20 = db.ListLeftPush("bikes:repairs", ["bike:important_bike", "bike:very_important_bike"]);
        Console.WriteLine(res20);   // >>> 5

        RedisValue[] res21 = db.ListRange("bikes:repairs", 0, -1);
        Console.WriteLine(string.Join(", ", res21));
        // >>> "bike:very_important_bike, bike:important_bike, bike:1, bike:2, bike:3"
```

##### C#

```csharp
        db.KeyDelete("bikes:repairs");
        
        long res19 = db.ListRightPush("bikes:repairs", ["bike:1", "bike:2", "bike:3"]);
        Console.WriteLine(res19);   // >>> 3

        long res20 = db.ListLeftPush("bikes:repairs", ["bike:important_bike", "bike:very_important_bike"]);
        Console.WriteLine(res20);   // >>> 5

        RedisValue[] res21 = db.ListRange("bikes:repairs", 0, -1);
        Console.WriteLine(string.Join(", ", res21));
        // >>> "bike:very_important_bike, bike:important_bike, bike:1, bike:2, bike:3"
```

##### Go

```go
	rdb.Del(ctx, "bikes:repairs")

	res19, err := rdb.RPush(ctx, "bikes:repairs", "bike:1", "bike:2", "bike:3").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res19) // >>> 3

	res20, err := rdb.LPush(ctx, "bikes:repairs", "bike:important_bike", "bike:very_important_bike").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res20) // >>> 5

	res21, err := rdb.LRange(ctx, "bikes:repairs", 0, -1).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res21) // >>> [bike:very_important_bike bike:important_bike bike:1 bike:2 bike:3]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> variadic = asyncCommands.rpush("bikes:repairs", "bike:1", "bike:2", "bike:3")
                    .thenCompose(res14 -> {
                        System.out.println(res14); // >>> 3

                        return asyncCommands.lpush("bikes:repairs", "bike:important_bike", "bike:very_important_bike");
                    }).thenCompose(res15 -> {
                        System.out.println(res15); // >>> 5

                        return asyncCommands.lrange("bikes:repairs", 0, -1);
                    })
                    .thenAccept(System.out::println)
                    // >>> [bike:very_important_bike, bike:important_bike, bike:1, bike:2, bike:3]
                    .toCompletableFuture();
```

##### Java (Synchronous - Jedis)

```java
        jedis.del("bikes:repairs");
        
        long res19 = jedis.rpush("bikes:repairs", "bike:1", "bike:2", "bike:3");
        System.out.println(res19);  // >>> 3

        long res20 = jedis.lpush("bikes:repairs", "bike:important_bike", "bike:very_important_bike");
        System.out.println(res20);  // >>> 5

        List<String> res21 = jedis.lrange("bikes:repairs", 0, -1);
        System.out.println(res21);  // >>> [bike:very_important_bike, bike:important_bike, bike:1, bike:2, bike:3]
```

##### JavaScript (Node.js)

```javascript
await client.del('bikes:repairs');

const res19 = await client.rPush('bikes:repairs', ['bike:1', 'bike:2', 'bike:3']);
console.log(res19);  // 3

const res20 = await client.lPush(
  'bikes:repairs', ['bike:important_bike', 'bike:very_important_bike']
);
console.log(res20);  // 5

const res21 = await client.lRange('bikes:repairs', 0, -1);
console.log(res21);  // ['bike:very_important_bike', 'bike:important_bike', 'bike:1', 'bike:2', 'bike:3']
```

##### PHP

```php
        $r->del('bikes:repairs');

        $res19 = $r->rpush('bikes:repairs', 'bike:1', 'bike:2', 'bike:3');
        echo $res19 . PHP_EOL;
        // >>> 3

        $res20 = $r->lpush('bikes:repairs', 'bike:important_bike', 'bike:very_important_bike');
        echo $res20 . PHP_EOL;
        // >>> 5

        $res21 = $r->lrange('bikes:repairs', 0, -1);
        echo json_encode($res21) . PHP_EOL;
        // >>> ['bike:very_important_bike', 'bike:important_bike', 'bike:1', ...
```

##### Python

```python
r.delete("bikes:repairs")

res19 = r.rpush("bikes:repairs", "bike:1", "bike:2", "bike:3")
print(res19)  # >>> 3

res20 = r.lpush("bikes:repairs", "bike:important_bike", "bike:very_important_bike")
print(res20)  # >>> 5

res21 = r.lrange("bikes:repairs", 0, -1)
print(
    res21
)  # >>> ['bike:very_important_bike', 'bike:important_bike', 'bike:1', ...
```

##### Ruby

```ruby
r.del('bikes:repairs')

res22 = r.rpush('bikes:repairs', ['bike:1', 'bike:2', 'bike:3'])
puts res22 # >>> 3

res23 = r.lpush('bikes:repairs', ['bike:important_bike', 'bike:very_important_bike'])
puts res23 # >>> 5

res24 = r.lrange('bikes:repairs', 0, -1)
puts res24.inspect
# >>> ["bike:very_important_bike", "bike:important_bike", "bike:1", "bike:2", "bike:3"]
```

##### Rust (Asynchronous)

```rust
        let _: usize = r.del("bikes:repairs").await.unwrap_or(0);

        if let Ok(res) = r.rpush("bikes:repairs", &["bike:1", "bike:2", "bike:3"]).await {
            let res: usize = res;
            println!("{res}"); // >>> 3
        }

        if let Ok(res) = r
            .lpush("bikes:repairs", &["bike:important_bike", "bike:very_important_bike"])
            .await
        {
            let res: usize = res;
            println!("{res}"); // >>> 5
        }

        if let Ok(res) = r.lrange("bikes:repairs", 0, -1).await {
            let res: Vec<String> = res;
            println!("{res:?}");
            // >>> ["bike:very_important_bike", "bike:important_bike", "bike:1", "bike:2", "bike:3"]
        }
```

##### Rust (Synchronous)

```rust
        let _: usize = r.del("bikes:repairs").unwrap_or(0);

        if let Ok(res) = r.rpush("bikes:repairs", &["bike:1", "bike:2", "bike:3"]) {
            let res: usize = res;
            println!("{res}"); // >>> 3
        }

        if let Ok(res) = r.lpush("bikes:repairs", &["bike:important_bike", "bike:very_important_bike"]) {
            let res: usize = res;
            println!("{res}"); // >>> 5
        }

        if let Ok(res) = r.lrange("bikes:repairs", 0, -1) {
            let res: Vec<String> = res;
            println!("{res:?}");
            // >>> ["bike:very_important_bike", "bike:important_bike", "bike:1", "bike:2", "bike:3"]
        }
```



An important operation defined on Redis lists is the ability to *pop elements*.
Popping elements is the operation of both retrieving the element from the list,
and eliminating it from the list, at the same time. You can pop elements
from left and right, similarly to how you can push elements in both sides
of the list. We'll add three elements and pop three elements, so at the end of this
sequence of commands the list is empty and there are no more elements to
pop:

Foundational: Remove and retrieve elements from both ends of a list using LPOP (left/head) and RPOP (right/tail) to consume items

**Commands:** DEL, RPUSH, RPOP, LPOP

**Complexity:**
- DEL: O(N)
- RPUSH: O(1)
- RPOP: O(N)
- LPOP: O(N)

**Available in:** Redis CLI, C#, C#, Go, Java (Asynchronous - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> DEL bikes:repairs
(integer) 1
> RPUSH bikes:repairs bike:1 bike:2 bike:3
(integer) 3
> RPOP bikes:repairs
"bike:3"
> LPOP bikes:repairs
"bike:1"
> RPOP bikes:repairs
"bike:2"
> RPOP bikes:repairs
(nil)
```

##### C#

```csharp
        long res22 = db.ListRightPush("bikes:repairs", ["bike:1", "bike:2", "bike:3"]);
        Console.WriteLine(res22);   // >>> 3

        RedisValue res23 = db.ListRightPop("bikes:repairs");
        Console.WriteLine(res23);   // >>> "bike:3"

        RedisValue res24 = db.ListLeftPop("bikes:repairs");
        Console.WriteLine(res24);   // >>> "bike:1"

        RedisValue res25 = db.ListRightPop("bikes:repairs");
        Console.WriteLine(res25);   // >>> "bike:2"

        RedisValue res26 = db.ListRightPop("bikes:repairs");
        Console.WriteLine(res26);   // >>> <Empty string>
```

##### C#

```csharp
        db.KeyDelete("bikes:repairs");

        long res22 = db.ListRightPush("bikes:repairs", ["bike:1", "bike:2", "bike:3"]);
        Console.WriteLine(res22);   // >>> 3

        RedisValue res23 = db.ListRightPop("bikes:repairs");
        Console.WriteLine(res23);   // >>> "bike:3"

        RedisValue res24 = db.ListLeftPop("bikes:repairs");
        Console.WriteLine(res24);   // >>> "bike:1"

        RedisValue res25 = db.ListRightPop("bikes:repairs");
        Console.WriteLine(res25);   // >>> "bike:2"

        RedisValue res26 = db.ListRightPop("bikes:repairs");
        Console.WriteLine(res26);   // >>> <Empty string>
```

##### C#

```csharp
        long res22 = db.ListRightPush("bikes:repairs", ["bike:1", "bike:2", "bike:3"]);
        Console.WriteLine(res22);   // >>> 3

        RedisValue res23 = db.ListRightPop("bikes:repairs");
        Console.WriteLine(res23);   // >>> "bike:3"

        RedisValue res24 = db.ListLeftPop("bikes:repairs");
        Console.WriteLine(res24);   // >>> "bike:1"

        RedisValue res25 = db.ListRightPop("bikes:repairs");
        Console.WriteLine(res25);   // >>> "bike:2"

        RedisValue res26 = db.ListRightPop("bikes:repairs");
        Console.WriteLine(res26);   // >>> <Empty string>
```

##### C#

```csharp
        db.KeyDelete("bikes:repairs");

        long res22 = db.ListRightPush("bikes:repairs", ["bike:1", "bike:2", "bike:3"]);
        Console.WriteLine(res22);   // >>> 3

        RedisValue res23 = db.ListRightPop("bikes:repairs");
        Console.WriteLine(res23);   // >>> "bike:3"

        RedisValue res24 = db.ListLeftPop("bikes:repairs");
        Console.WriteLine(res24);   // >>> "bike:1"

        RedisValue res25 = db.ListRightPop("bikes:repairs");
        Console.WriteLine(res25);   // >>> "bike:2"

        RedisValue res26 = db.ListRightPop("bikes:repairs");
        Console.WriteLine(res26);   // >>> <Empty string>
```

##### Go

```go
	rdb.Del(ctx, "bikes:repairs")

	res22, err := rdb.RPush(ctx, "bikes:repairs", "bike:1", "bike:2", "bike:3").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res22) // >>> 3

	res23, err := rdb.RPop(ctx, "bikes:repairs").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res23) // >>> bike:3

	res24, err := rdb.LPop(ctx, "bikes:repairs").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res24) // >>> bike:1

	res25, err := rdb.RPop(ctx, "bikes:repairs").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res25) // >>> bike:2

	res26, err := rdb.RPop(ctx, "bikes:repairs").Result()

	if err != nil {
		fmt.Println(err) // >>> redis: nil
	}

	fmt.Println(res26) // >>> <empty string>

```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> lpoprpop = asyncCommands.rpush("bikes:repairs", "bike:1", "bike:2", "bike:3")
                    .thenCompose(res16 -> {
                        System.out.println(res16); // >>> 3

                        return asyncCommands.rpop("bikes:repairs");
                    }).thenCompose(res17 -> {
                        System.out.println(res17); // >>> bike:3

                        return asyncCommands.lpop("bikes:repairs");
                    }).thenCompose(res18 -> {
                        System.out.println(res18); // >>> bike:1

                        return asyncCommands.rpop("bikes:repairs");
                    }).thenCompose(res19 -> {
                        System.out.println(res19); // >>> bike:2

                        return asyncCommands.rpop("bikes:repairs");
                    })
                    .thenAccept(System.out::println) // >>> null
                    .toCompletableFuture();
```

##### Java (Synchronous - Jedis)

```java
        jedis.del("bikes:repairs");

        long res22 = jedis.rpush("bikes:repairs", "bike:1", "bike:2", "bike:3");
        System.out.println(res22);  // >>> 3

        String res23 = jedis.rpop("bikes:repairs");
        System.out.println(res23);  // >>> bike:3

        String res24 = jedis.lpop("bikes:repairs");
        System.out.println(res24);  // >>> bike:1

        String res25 = jedis.rpop("bikes:repairs");
        System.out.println(res25);  // >>> bike:2

        String res26 = jedis.rpop("bikes:repairs");
        System.out.println(res26);  // >>> null
```

##### JavaScript (Node.js)

```javascript
await client.del('bikes:repairs');

const res22 = await client.rPush('bikes:repairs', ['bike:1', 'bike:2', 'bike:3']);
console.log(res22);  // 3

const res23 = await client.rPop('bikes:repairs');
console.log(res23);  // 'bike:3'

const res24 = await client.lPop('bikes:repairs');
console.log(res24);  // 'bike:1'

const res25 = await client.rPop('bikes:repairs');
console.log(res25);  // 'bike:2'

const res26 = await client.rPop('bikes:repairs');
console.log(res26);  // null
```

##### PHP

```php
        $r->del('bikes:repairs');
        
        $res22 = $r->rpush('bikes:repairs', 'bike:1', 'bike:2', 'bike:3');
        echo $res22 . PHP_EOL;
        // >>> 3

        $res23 = $r->rpop('bikes:repairs');
        echo $res23 . PHP_EOL;
        // >>> 'bike:3'

        $res24 = $r->lpop('bikes:repairs');
        echo $res24 . PHP_EOL;
        // >>> 'bike:1'

        $res25 = $r->rpop('bikes:repairs');
        echo $res25 . PHP_EOL;
        // >>> 'bike:2'

        $res26 = $r->rpop('bikes:repairs');
        echo $res26 . PHP_EOL;
        // >>> None
```

##### Python

```python
r.delete("bikes:repairs")

res22 = r.rpush("bikes:repairs", "bike:1", "bike:2", "bike:3")
print(res22)  # >>> 3

res23 = r.rpop("bikes:repairs")
print(res23)  # >>> 'bike:3'

res24 = r.lpop("bikes:repairs")
print(res24)  # >>> 'bike:1'

res25 = r.rpop("bikes:repairs")
print(res25)  # >>> 'bike:2'

res26 = r.rpop("bikes:repairs")
print(res26)  # >>> None
```

##### Ruby

```ruby
r.del('bikes:repairs')

res25 = r.rpush('bikes:repairs', ['bike:1', 'bike:2', 'bike:3'])
puts res25 # >>> 3

res26 = r.rpop('bikes:repairs')
puts res26 # >>> bike:3

res27 = r.lpop('bikes:repairs')
puts res27 # >>> bike:1

res28 = r.rpop('bikes:repairs')
puts res28 # >>> bike:2

res29 = r.rpop('bikes:repairs')
puts res29.inspect # >>> nil
```

##### Rust (Asynchronous)

```rust
        let _: usize = r.del("bikes:repairs").await.unwrap_or(0);

        if let Ok(res) = r.rpush("bikes:repairs", &["bike:1", "bike:2", "bike:3"]).await {
            let res: usize = res;
            println!("{res}"); // >>> 3
        }

        if let Ok(res) = r.rpop("bikes:repairs", None).await {
            let res: Option<String> = res;
            print_optional_string(res.clone()); // >>> bike:3
        }

        if let Ok(res) = r.lpop("bikes:repairs", None).await {
            let res: Option<String> = res;
            print_optional_string(res.clone()); // >>> bike:1
        }

        if let Ok(res) = r.rpop("bikes:repairs", None).await {
            let res: Option<String> = res;
            print_optional_string(res.clone()); // >>> bike:2
        }

        if let Ok(res) = r.rpop("bikes:repairs", None).await {
            let res: Option<String> = res;
            print_optional_string(res.clone()); // >>> (nil)
        }
```

##### Rust (Synchronous)

```rust
        let _: usize = r.del("bikes:repairs").unwrap_or(0);

        if let Ok(res) = r.rpush("bikes:repairs", &["bike:1", "bike:2", "bike:3"]) {
            let res: usize = res;
            println!("{res}"); // >>> 3
        }

        if let Ok(res) = r.rpop("bikes:repairs", None) {
            let res: Option<String> = res;
            print_optional_string(res.clone()); // >>> bike:3
        }

        if let Ok(res) = r.lpop("bikes:repairs", None) {
            let res: Option<String> = res;
            print_optional_string(res.clone()); // >>> bike:1
        }

        if let Ok(res) = r.rpop("bikes:repairs", None) {
            let res: Option<String> = res;
            print_optional_string(res.clone()); // >>> bike:2
        }

        if let Ok(res) = r.rpop("bikes:repairs", None) {
            let res: Option<String> = res;
            print_optional_string(res.clone()); // >>> (nil)
        }
```



Redis returned a NULL value to signal that there are no elements in the
list.

### Common use cases for lists

Lists are useful for a number of tasks, two very representative use cases
are the following:

* Remember the latest updates posted by users into a social network.
* Communication between processes, using a consumer-producer pattern where the producer pushes items into a list, and a consumer (usually a *worker*) consumes those items and executes actions. Redis has special list commands to make this use case both more reliable and efficient.

For example both the popular Ruby libraries [resque](https://github.com/resque/resque) and
[sidekiq](https://github.com/mperham/sidekiq) use Redis lists under the hood in order to
implement background jobs.

The popular Twitter social network [takes the latest tweets](http://www.infoq.com/presentations/Real-Time-Delivery-Twitter)
posted by users into Redis lists.

To describe a common use case step by step, imagine your home page shows the latest
photos published in a photo sharing social network and you want to speedup access.

* Every time a user posts a new photo, we add its ID into a list with [`LPUSH`](https://redis.io/docs/latest/commands/lpush).
* When users visit the home page, we use `LRANGE 0 9` in order to get the latest 10 posted items.

### Capped lists

In many use cases we just want to use lists to store the *latest items*,
whatever they are: social network updates, logs, or anything else.

Redis allows us to use lists as a capped collection, only remembering the latest
N items and discarding all the oldest items using the [`LTRIM`](https://redis.io/docs/latest/commands/ltrim) command.

The [`LTRIM`](https://redis.io/docs/latest/commands/ltrim) command is similar to [`LRANGE`](https://redis.io/docs/latest/commands/lrange), but **instead of displaying the
specified range of elements** it sets this range as the new list value. All
the elements outside the given range are removed.

For example, if you're adding bikes on the end of a list of repairs, but only
want to worry about the 3 that have been on the list the longest:

Capped lists: Use LTRIM with positive indexes to keep a range of elements from the beginning when you need to maintain a fixed-size list

**Difficulty:** Intermediate

**Builds upon:** lpush_rpush

**Commands:** DEL, RPUSH, LTRIM, LRANGE

**Complexity:**
- DEL: O(N)
- RPUSH: O(1)
- LTRIM: O(N)
- LRANGE: O(S+N)

**Available in:** Redis CLI, C#, C#, Go, Java (Asynchronous - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> DEL bikes:repairs
(integer) 0
> RPUSH bikes:repairs bike:1 bike:2 bike:3 bike:4 bike:5
(integer) 5
> LTRIM bikes:repairs 0 2
OK
> LRANGE bikes:repairs 0 -1
1) "bike:1"
2) "bike:2"
3) "bike:3"
```

##### C#

```csharp
        long res27 = db.ListLeftPush("bikes:repairs", ["bike:1", "bike:2", "bike:3", "bike:4", "bike:5"]);
        Console.WriteLine(res27);   // >>> 5

        db.ListTrim("bikes:repairs", 0, 2);
        RedisValue[] res28 = db.ListRange("bikes:repairs", 0, -1);
        Console.WriteLine(string.Join(", ", res28));    // "bike:5, bike:4, bike:3"
```

##### C#

```csharp
        long res27 = db.ListLeftPush("bikes:repairs", ["bike:1", "bike:2", "bike:3", "bike:4", "bike:5"]);
        Console.WriteLine(res27);   // >>> 5

        db.ListTrim("bikes:repairs", 0, 2);
        RedisValue[] res28 = db.ListRange("bikes:repairs", 0, -1);
        Console.WriteLine(string.Join(", ", res28));    // "bike:5, bike:4, bike:3"
```

##### C#

```csharp
        long res27 = db.ListLeftPush("bikes:repairs", ["bike:1", "bike:2", "bike:3", "bike:4", "bike:5"]);
        Console.WriteLine(res27);   // >>> 5

        db.ListTrim("bikes:repairs", 0, 2);
        RedisValue[] res28 = db.ListRange("bikes:repairs", 0, -1);
        Console.WriteLine(string.Join(", ", res28));    // "bike:5, bike:4, bike:3"
```

##### C#

```csharp
        long res27 = db.ListLeftPush("bikes:repairs", ["bike:1", "bike:2", "bike:3", "bike:4", "bike:5"]);
        Console.WriteLine(res27);   // >>> 5

        db.ListTrim("bikes:repairs", 0, 2);
        RedisValue[] res28 = db.ListRange("bikes:repairs", 0, -1);
        Console.WriteLine(string.Join(", ", res28));    // "bike:5, bike:4, bike:3"
```

##### Go

```go
	rdb.Del(ctx, "bikes:repairs")

	res27, err := rdb.RPush(ctx, "bikes:repairs", "bike:1", "bike:2", "bike:3", "bike:4", "bike:5").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res27) // >>> 5

	res28, err := rdb.LTrim(ctx, "bikes:repairs", 0, 2).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res28) // >>> OK

	res29, err := rdb.LRange(ctx, "bikes:repairs", 0, -1).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res29) // >>> [bike:1 bike:2 bike:3]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> ltrim = asyncCommands
                    .lpush("bikes:repairs", "bike:1", "bike:2", "bike:3", "bike:4", "bike:5").thenCompose(res20 -> {
                        System.out.println(res20); // >>> 5

                        return asyncCommands.ltrim("bikes:repairs", 0, 2);
                    }).thenCompose(res21 -> {
                        System.out.println(res21); // >>> OK

                        return asyncCommands.lrange("bikes:repairs", 0, -1);
                    })
                    .thenAccept(System.out::println)
                    // >>> [bike:5, bike:4, bike:3]
                    .toCompletableFuture();
```

##### Java (Synchronous - Jedis)

```java
        long res27 = jedis.rpush("bikes:repairs", "bike:1", "bike:2", "bike:3", "bike:4", "bike:5");
        System.out.println(res27);  // >>> 5

        String res28 = jedis.ltrim("bikes:repairs", 0, 2);
        System.out.println(res28);  // >>> OK

        List<String> res29 = jedis.lrange("bikes:repairs", 0, -1);
        System.out.println(res29);  // >>> [bike:1, bike:2, bike:3]
```

##### JavaScript (Node.js)

```javascript
const res27 = await client.lPush(
  'bikes:repairs', ['bike:1', 'bike:2', 'bike:3', 'bike:4', 'bike:5']
);
console.log(res27);  // 5

const res28 = await client.lTrim('bikes:repairs', 0, 2);
console.log(res28);  // OK

const res29 = await client.lRange('bikes:repairs', 0, -1);
console.log(res29);  // ['bike:5', 'bike:4', 'bike:3']
```

##### PHP

```php
        $res27 = $r->rpush('bikes:repairs', 'bike:1', 'bike:2', 'bike:3', 'bike:4', 'bike:5');
        echo $res27 . PHP_EOL;
        // >>> 5

        $res28 = $r->ltrim('bikes:repairs', 0, 2);
        echo $res28 . PHP_EOL;
        // >>> True

        $res29 = $r->lrange('bikes:repairs', 0, -1);
        echo json_encode($res29) . PHP_EOL;
        // >>> ['bike:1', 'bike:2', 'bike:3']
```

##### Python

```python
res27 = r.rpush("bikes:repairs", "bike:1", "bike:2", "bike:3", "bike:4", "bike:5")
print(res27)  # >>> 5

res28 = r.ltrim("bikes:repairs", 0, 2)
print(res28)  # >>> True

res29 = r.lrange("bikes:repairs", 0, -1)
print(res29)  # >>> ['bike:1', 'bike:2', 'bike:3']
```

##### Ruby

```ruby
r.del('bikes:repairs')

res30 = r.rpush('bikes:repairs', ['bike:1', 'bike:2', 'bike:3', 'bike:4', 'bike:5'])
puts res30 # >>> 5

res31 = r.ltrim('bikes:repairs', 0, 2)
puts res31 # >>> OK

res32 = r.lrange('bikes:repairs', 0, -1)
puts res32.inspect # >>> ["bike:1", "bike:2", "bike:3"]
```

##### Rust (Asynchronous)

```rust
        if let Ok(res) = r
            .rpush(
                "bikes:repairs",
                &["bike:1", "bike:2", "bike:3", "bike:4", "bike:5"],
            )
            .await
        {
            let res: usize = res;
            println!("{res}"); // >>> 5
        }

        if let Ok(res) = r.ltrim("bikes:repairs", 0, 2).await {
            let res: () = res;
            let _ = res;
            println!("OK"); // >>> OK
        }

        if let Ok(res) = r.lrange("bikes:repairs", 0, -1).await {
            let res: Vec<String> = res;
            println!("{res:?}"); // >>> ["bike:1", "bike:2", "bike:3"]
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.rpush("bikes:repairs", &["bike:1", "bike:2", "bike:3", "bike:4", "bike:5"]) {
            let res: usize = res;
            println!("{res}"); // >>> 5
        }

        if let Ok(res) = r.ltrim("bikes:repairs", 0, 2) {
            let res: () = res;
            let _ = res;
            println!("OK"); // >>> OK
        }

        if let Ok(res) = r.lrange("bikes:repairs", 0, -1) {
            let res: Vec<String> = res;
            println!("{res:?}"); // >>> ["bike:1", "bike:2", "bike:3"]
        }
```



The above [`LTRIM`](https://redis.io/docs/latest/commands/ltrim) command tells Redis to keep just list elements from index
0 to 2, everything else will be discarded. This allows for a very simple but
useful pattern: doing a List push operation + a List trim operation together 
to add a new element and discard elements exceeding a limit. Using 
[`LTRIM`](https://redis.io/docs/latest/commands/ltrim) with negative indexes can then be used to keep only the 3 most recently added:

Capped lists with negative indexes: Use LTRIM with negative indexes to keep the most recent elements when you need to maintain a fixed-size list of latest items

**Difficulty:** Intermediate

**Builds upon:** lpush_rpush

**Commands:** DEL, RPUSH, LTRIM, LRANGE

**Complexity:**
- DEL: O(N)
- RPUSH: O(1)
- LTRIM: O(N)
- LRANGE: O(S+N)

**Available in:** Redis CLI, C#, C#, Go, Java (Asynchronous - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> DEL bikes:repairs
(integer) 1
> RPUSH bikes:repairs bike:1 bike:2 bike:3 bike:4 bike:5
(integer) 5
> LTRIM bikes:repairs -3 -1
OK
> LRANGE bikes:repairs 0 -1
1) "bike:3"
2) "bike:4"
3) "bike:5"
```

##### C#

```csharp
        long res29 = db.ListRightPush("bikes:repairs", ["bike:1", "bike:2", "bike:3", "bike:4", "bike:5"]);
        Console.WriteLine(res29);   // >>> 5

        db.ListTrim("bikes:repairs", -3, -1);
        RedisValue[] res30 = db.ListRange("bikes:repairs", 0, -1);
        Console.WriteLine(string.Join(", ", res30));    // >>> "bike:3, bike:4, bike:5"
```

##### C#

```csharp
        db.KeyDelete("bikes:repairs");

        long res29 = db.ListRightPush("bikes:repairs", ["bike:1", "bike:2", "bike:3", "bike:4", "bike:5"]);
        Console.WriteLine(res29);   // >>> 5

        db.ListTrim("bikes:repairs", -3, -1);
        RedisValue[] res30 = db.ListRange("bikes:repairs", 0, -1);
        Console.WriteLine(string.Join(", ", res30));    // >>> "bike:3, bike:4, bike:5"
```

##### C#

```csharp
        long res29 = db.ListRightPush("bikes:repairs", ["bike:1", "bike:2", "bike:3", "bike:4", "bike:5"]);
        Console.WriteLine(res29);   // >>> 5

        db.ListTrim("bikes:repairs", -3, -1);
        RedisValue[] res30 = db.ListRange("bikes:repairs", 0, -1);
        Console.WriteLine(string.Join(", ", res30));    // >>> "bike:3, bike:4, bike:5"
```

##### C#

```csharp
        db.KeyDelete("bikes:repairs");

        long res29 = db.ListRightPush("bikes:repairs", ["bike:1", "bike:2", "bike:3", "bike:4", "bike:5"]);
        Console.WriteLine(res29);   // >>> 5

        db.ListTrim("bikes:repairs", -3, -1);
        RedisValue[] res30 = db.ListRange("bikes:repairs", 0, -1);
        Console.WriteLine(string.Join(", ", res30));    // >>> "bike:3, bike:4, bike:5"
```

##### Go

```go
	rdb.Del(ctx, "bikes:repairs")

	res30, err := rdb.RPush(ctx, "bikes:repairs", "bike:1", "bike:2", "bike:3", "bike:4", "bike:5").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res30) // >>> 5

	res31, err := rdb.LTrim(ctx, "bikes:repairs", -3, -1).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res31) // >>> OK

	res32, err := rdb.LRange(ctx, "bikes:repairs", 0, -1).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res32) // >>> [bike:3 bike:4 bike:5]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> ltrimendoflist = asyncCommands
                    .rpush("bikes:repairs", "bike:1", "bike:2", "bike:3", "bike:4", "bike:5").thenCompose(res22 -> {
                        System.out.println(res22); // >>> 5

                        return asyncCommands.ltrim("bikes:repairs", -3, -1);
                    }).thenCompose(res23 -> {
                        System.out.println(res23); // >>> OK

                        return asyncCommands.lrange("bikes:repairs", 0, -1);
                    })
                    .thenAccept(System.out::println)
                    // >>> [bike:3, bike:4, bike:5]
                    .toCompletableFuture();
```

##### Java (Synchronous - Jedis)

```java
        jedis.del("bikes:repairs");
        
        res27 = jedis.rpush("bikes:repairs", "bike:1", "bike:2", "bike:3", "bike:4", "bike:5");
        System.out.println(res27);  // >>> 5

        res28 = jedis.ltrim("bikes:repairs", -3, -1);
        System.out.println(res2);  // >>> OK

        res29 = jedis.lrange("bikes:repairs", 0, -1);
        System.out.println(res29);  // >>> [bike:3, bike:4, bike:5]
```

##### JavaScript (Node.js)

```javascript
await client.del('bikes:repairs');

const res27eol = await client.rPush(
  'bikes:repairs', ['bike:1', 'bike:2', 'bike:3', 'bike:4', 'bike:5']
);
console.log(res27eol);  // 5

const res28eol = await client.lTrim('bikes:repairs', -3, -1);
console.log(res28eol);  // 'OK'

const res29eol = await client.lRange('bikes:repairs', 0, -1);
console.log(res29eol);  // ['bike:3', 'bike:4', 'bike:5']
```

##### PHP

```php
        $r->del('bikes:repairs');

        $res27 = $r->rpush('bikes:repairs', 'bike:1', 'bike:2', 'bike:3', 'bike:4', 'bike:5');
        echo $res27 . PHP_EOL;
        // >>> 5

        $res28 = $r->ltrim('bikes:repairs', -3, -1);
        echo $res28 . PHP_EOL;
        // >>> True

        $res29 = $r->lrange('bikes:repairs', 0, -1);
        echo json_encode($res29) . PHP_EOL;
        // >>> ['bike:3', 'bike:4', 'bike:5']
```

##### Python

```python
r.delete("bikes:repairs")

res27 = r.rpush("bikes:repairs", "bike:1", "bike:2", "bike:3", "bike:4", "bike:5")
print(res27)  # >>> 5

res28 = r.ltrim("bikes:repairs", -3, -1)
print(res28)  # >>> True

res29 = r.lrange("bikes:repairs", 0, -1)
print(res29)  # >>> ['bike:3', 'bike:4', 'bike:5']
```

##### Ruby

```ruby
r.del('bikes:repairs')

res33 = r.rpush('bikes:repairs', ['bike:1', 'bike:2', 'bike:3', 'bike:4', 'bike:5'])
puts res33 # >>> 5

res34 = r.ltrim('bikes:repairs', -3, -1)
puts res34 # >>> OK

res35 = r.lrange('bikes:repairs', 0, -1)
puts res35.inspect # >>> ["bike:3", "bike:4", "bike:5"]
```

##### Rust (Asynchronous)

```rust
        let _: usize = r.del("bikes:repairs").await.unwrap_or(0);

        if let Ok(res) = r
            .rpush(
                "bikes:repairs",
                &["bike:1", "bike:2", "bike:3", "bike:4", "bike:5"],
            )
            .await
        {
            let res: usize = res;
            println!("{res}"); // >>> 5
        }

        if let Ok(res) = r.ltrim("bikes:repairs", -3, -1).await {
            let res: () = res;
            let _ = res;
            println!("OK"); // >>> OK
        }

        if let Ok(res) = r.lrange("bikes:repairs", 0, -1).await {
            let res: Vec<String> = res;
            println!("{res:?}"); // >>> ["bike:3", "bike:4", "bike:5"]
        }
```

##### Rust (Synchronous)

```rust
        let _: usize = r.del("bikes:repairs").unwrap_or(0);

        if let Ok(res) = r.rpush("bikes:repairs", &["bike:1", "bike:2", "bike:3", "bike:4", "bike:5"]) {
            let res: usize = res;
            println!("{res}"); // >>> 5
        }

        if let Ok(res) = r.ltrim("bikes:repairs", -3, -1) {
            let res: () = res;
            let _ = res;
            println!("OK"); // >>> OK
        }

        if let Ok(res) = r.lrange("bikes:repairs", 0, -1) {
            let res: Vec<String> = res;
            println!("{res:?}"); // >>> ["bike:3", "bike:4", "bike:5"]
        }
```



The above combination adds new elements and keeps only the 3
newest elements into the list. With [`LRANGE`](https://redis.io/docs/latest/commands/lrange) you can access the top items
without any need to remember very old data.

Note: while [`LRANGE`](https://redis.io/docs/latest/commands/lrange) is technically an O(N) command, accessing small ranges
towards the head or the tail of the list is a constant time operation.

## Blocking operations on lists

Lists have a special feature that make them suitable to implement queues,
and in general as a building block for inter process communication systems:
blocking operations.

Imagine you want to push items into a list with one process, and use
a different process in order to actually do some kind of work with those
items. This is the usual producer / consumer setup, and can be implemented
in the following simple way:

* To push items into the list, producers call [`LPUSH`](https://redis.io/docs/latest/commands/lpush).
* To extract / process items from the list, consumers call [`RPOP`](https://redis.io/docs/latest/commands/rpop).

However it is possible that sometimes the list is empty and there is nothing
to process, so [`RPOP`](https://redis.io/docs/latest/commands/rpop) just returns NULL. In this case a consumer is forced to wait
some time and retry again with [`RPOP`](https://redis.io/docs/latest/commands/rpop). This is called *polling*, and is not
a good idea in this context because it has several drawbacks:

1. Forces Redis and clients to process useless commands (all the requests when the list is empty will get no actual work done, they'll just return NULL).
2. Adds a delay to the processing of items, since after a worker receives a NULL, it waits some time. To make the delay smaller, we could wait less between calls to [`RPOP`](https://redis.io/docs/latest/commands/rpop), with the effect of amplifying problem number 1, i.e. more useless calls to Redis.

So Redis implements commands called [`BRPOP`](https://redis.io/docs/latest/commands/brpop) and [`BLPOP`](https://redis.io/docs/latest/commands/blpop) which are versions
of [`RPOP`](https://redis.io/docs/latest/commands/rpop) and [`LPOP`](https://redis.io/docs/latest/commands/lpop) able to block if the list is empty: they'll return to
the caller only when a new element is added to the list, or when a user-specified
timeout is reached.

This is an example of a [`BRPOP`](https://redis.io/docs/latest/commands/brpop) call we could use in the worker:

Blocking operations: Use BRPOP to wait for elements with a timeout when you need to implement producer-consumer patterns without polling

**Difficulty:** Intermediate

**Builds upon:** lpush_rpush, lpop_rpop

**Commands:** DEL, RPUSH, BRPOP

**Complexity:**
- DEL: O(N)
- RPUSH: O(1)
- BRPOP: O(N)

**Available in:** Redis CLI, C#, C#, Go, Java (Asynchronous - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> DEL bikes:repairs
(integer) 1
> RPUSH bikes:repairs bike:1 bike:2
(integer) 2
> BRPOP bikes:repairs 1
1) "bikes:repairs"
2) "bike:2"
> BRPOP bikes:repairs 1
1) "bikes:repairs"
2) "bike:1"
> BRPOP bikes:repairs 1
(nil)
(2.01s)
```

##### C#

```csharp
        long res31 = db.ListRightPush("bikes:repairs", ["bike:1", "bike:2"]);
        Console.WriteLine(res31);   // >>> 2

        Tuple<RedisKey, RedisValue>? res32 = db.BRPop(["bikes:repairs"], 1);

        if (res32 != null)
            Console.WriteLine($"{res32.Item1} -> {res32.Item2}"); // >>> "bikes:repairs -> bike:2"

        Tuple<RedisKey, RedisValue>? res33 = db.BRPop(["bikes:repairs"], 1);

        if (res33 != null)
            Console.WriteLine($"{res33.Item1} -> {res33.Item2}"); // >>> "bikes:repairs -> bike:1"

        Tuple<RedisKey, RedisValue>? res34 = db.BRPop(["bikes:repairs"], 1);
        Console.WriteLine(res34);   // >>> "Null"
```

##### C#

```csharp
        db.KeyDelete("bikes:repairs");

        long res31 = db.ListRightPush("bikes:repairs", ["bike:1", "bike:2"]);
        Console.WriteLine(res31);   // >>> 2

        Tuple<RedisKey, RedisValue>? res32 = db.BRPop(["bikes:repairs"], 1);

        if (res32 != null)
            Console.WriteLine($"{res32.Item1} -> {res32.Item2}"); // >>> "bikes:repairs -> bike:2"

        Tuple<RedisKey, RedisValue>? res33 = db.BRPop(["bikes:repairs"], 1);

        if (res33 != null)
            Console.WriteLine($"{res33.Item1} -> {res33.Item2}"); // >>> "bikes:repairs -> bike:1"

        Tuple<RedisKey, RedisValue>? res34 = db.BRPop(["bikes:repairs"], 1);
        Console.WriteLine(res34);   // >>> "Null"
```

##### C#

```csharp
        long res31 = db.ListRightPush("bikes:repairs", ["bike:1", "bike:2"]);
        Console.WriteLine(res31);   // >>> 2

        Tuple<RedisKey, RedisValue>? res32 = db.BRPop(["bikes:repairs"], 1);

        if (res32 != null)
            Console.WriteLine($"{res32.Item1} -> {res32.Item2}"); // >>> "bikes:repairs -> bike:2"

        Tuple<RedisKey, RedisValue>? res33 = db.BRPop(["bikes:repairs"], 1);

        if (res33 != null)
            Console.WriteLine($"{res33.Item1} -> {res33.Item2}"); // >>> "bikes:repairs -> bike:1"

        Tuple<RedisKey, RedisValue>? res34 = db.BRPop(["bikes:repairs"], 1);
        Console.WriteLine(res34);   // >>> "Null"
```

##### C#

```csharp
        db.KeyDelete("bikes:repairs");

        long res31 = db.ListRightPush("bikes:repairs", ["bike:1", "bike:2"]);
        Console.WriteLine(res31);   // >>> 2

        Tuple<RedisKey, RedisValue>? res32 = db.BRPop(["bikes:repairs"], 1);

        if (res32 != null)
            Console.WriteLine($"{res32.Item1} -> {res32.Item2}"); // >>> "bikes:repairs -> bike:2"

        Tuple<RedisKey, RedisValue>? res33 = db.BRPop(["bikes:repairs"], 1);

        if (res33 != null)
            Console.WriteLine($"{res33.Item1} -> {res33.Item2}"); // >>> "bikes:repairs -> bike:1"

        Tuple<RedisKey, RedisValue>? res34 = db.BRPop(["bikes:repairs"], 1);
        Console.WriteLine(res34);   // >>> "Null"
```

##### Go

```go
	rdb.Del(ctx, "bikes:repairs")

	res33, err := rdb.RPush(ctx, "bikes:repairs", "bike:1", "bike:2").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res33) // >>> 2

	res34, err := rdb.BRPop(ctx, 1, "bikes:repairs").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res34) // >>> [bikes:repairs bike:2]

	res35, err := rdb.BRPop(ctx, 1, "bikes:repairs").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res35) // >>> [bikes:repairs bike:1]

	res36, err := rdb.BRPop(ctx, 1, "bikes:repairs").Result()

	if err != nil {
		fmt.Println(err) // >>> redis: nil
	}

	fmt.Println(res36) // >>> []
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> brpop = asyncCommands.rpush("bikes:repairs", "bike:1", "bike:2").thenCompose(res24 -> {
                System.out.println(res24); // >>> 2

                return asyncCommands.brpop(1, "bikes:repairs");
            }).thenCompose(res25 -> {
                System.out.println(res25);
                // >>> KeyValue[bikes:repairs, bike:2]

                return asyncCommands.brpop(1, "bikes:repairs");
            }).thenCompose(res26 -> {
                System.out.println(res26);
                // >>> KeyValue[bikes:repairs, bike:1]

                return asyncCommands.brpop(1, "bikes:repairs");
            })
                    .thenAccept(System.out::println) // >>> null
                    .toCompletableFuture();
```

##### Java (Synchronous - Jedis)

```java
        jedis.del("bikes:repairs");

        long res31 = jedis.rpush("bikes:repairs", "bike:1", "bike:2");
        System.out.println(res31);  // >>> 2

        List<String> res32 = jedis.brpop(1, "bikes:repairs");
        System.out.println(res32);  // >>> (bikes:repairs, bike:2)

        List<String>  res33 = jedis.brpop(1,"bikes:repairs");
        System.out.println(res33);  // >>> (bikes:repairs, bike:1)

        List<String>  res34 = jedis.brpop(1,"bikes:repairs");
        System.out.println(res34);  // >>> null
```

##### JavaScript (Node.js)

```javascript
await client.del('bikes:repairs');

const res31 = await client.rPush('bikes:repairs', ['bike:1', 'bike:2']);
console.log(res31);  // 2

const res32 = await client.brPop('bikes:repairs', 1);
console.log(res32);  // { key: 'bikes:repairs', element: 'bike:2' }

const res33 = await client.brPop('bikes:repairs', 1);
console.log(res33);  // { key: 'bikes:repairs', element: 'bike:1' }

const res34 = await client.brPop('bikes:repairs', 1);
console.log(res34);  // null
```

##### PHP

```php
        $r->del('bikes:repairs');

        $res31 = $r->rpush('bikes:repairs', 'bike:1', 'bike:2');
        echo $res31 . PHP_EOL;
        // >>> 2

        $res32 = $r->brpop('bikes:repairs', 1);
        echo json_encode($res32) . PHP_EOL;
        // >>> ['bikes:repairs', 'bike:2']

        $res33 = $r->brpop('bikes:repairs', 1);
        echo json_encode($res33) . PHP_EOL;
        // >>> ['bikes:repairs', 'bike:1']

        $res34 = $r->brpop('bikes:repairs', 1);
        echo json_encode($res34) . PHP_EOL;
        // >>> None
```

##### Python

```python
r.delete("bikes:repairs")

res31 = r.rpush("bikes:repairs", "bike:1", "bike:2")
print(res31)  # >>> 2

res32 = r.brpop("bikes:repairs", timeout=1)
print(res32)  # >>> ('bikes:repairs', 'bike:2')

res33 = r.brpop("bikes:repairs", timeout=1)
print(res33)  # >>> ('bikes:repairs', 'bike:1')

res34 = r.brpop("bikes:repairs", timeout=1)
print(res34)  # >>> None
```

##### Ruby

```ruby
r.del('bikes:repairs')

res36 = r.rpush('bikes:repairs', ['bike:1', 'bike:2'])
puts res36 # >>> 2

res37 = r.brpop('bikes:repairs', timeout: 1)
puts res37.inspect # >>> ["bikes:repairs", "bike:2"]

res38 = r.brpop('bikes:repairs', timeout: 1)
puts res38.inspect # >>> ["bikes:repairs", "bike:1"]

res39 = r.brpop('bikes:repairs', timeout: 1)
puts res39.inspect # >>> nil
```

##### Rust (Asynchronous)

```rust
        let _: usize = r.del("bikes:repairs").await.unwrap_or(0);

        if let Ok(res) = r.rpush("bikes:repairs", &["bike:1", "bike:2"]).await {
            let res: usize = res;
            println!("{res}"); // >>> 2
        }

        if let Ok(res) = r.brpop("bikes:repairs", 1.0).await {
            let res: Option<[String; 2]> = res;
            println!("{res:?}"); // >>> Some(["bikes:repairs", "bike:2"])
        }

        if let Ok(res) = r.brpop("bikes:repairs", 1.0).await {
            let res: Option<[String; 2]> = res;
            println!("{res:?}"); // >>> Some(["bikes:repairs", "bike:1"])
        }

        if let Ok(res) = r.brpop("bikes:repairs", 1.0).await {
            let res: Option<[String; 2]> = res;
            println!("{res:?}"); // >>> None
        }
```

##### Rust (Synchronous)

```rust
        let _: usize = r.del("bikes:repairs").unwrap_or(0);

        if let Ok(res) = r.rpush("bikes:repairs", &["bike:1", "bike:2"]) {
            let res: usize = res;
            println!("{res}"); // >>> 2
        }

        if let Ok(res) = r.brpop("bikes:repairs", 1.0) {
            let res: Option<[String; 2]> = res;
            println!("{res:?}"); // >>> Some(["bikes:repairs", "bike:2"])
        }

        if let Ok(res) = r.brpop("bikes:repairs", 1.0) {
            let res: Option<[String; 2]> = res;
            println!("{res:?}"); // >>> Some(["bikes:repairs", "bike:1"])
        }

        if let Ok(res) = r.brpop("bikes:repairs", 1.0) {
            let res: Option<[String; 2]> = res;
            println!("{res:?}"); // >>> None
        }
```



It means: "wait for elements in the list `bikes:repairs`, but return if after 1 second
no element is available".

Note that you can use 0 as timeout to wait for elements forever, and you can
also specify multiple lists and not just one, in order to wait on multiple
lists at the same time, and get notified when the first list receives an
element.

A few things to note about [`BRPOP`](https://redis.io/docs/latest/commands/brpop):

1. Clients are served in an ordered way: the first client that blocked waiting for a list, is served first when an element is pushed by some other client, and so forth.
2. The return value is different compared to [`RPOP`](https://redis.io/docs/latest/commands/rpop): it is a two-element array since it also includes the name of the key, because [`BRPOP`](https://redis.io/docs/latest/commands/brpop) and [`BLPOP`](https://redis.io/docs/latest/commands/blpop) are able to block waiting for elements from multiple lists.
3. If the timeout is reached, NULL is returned.

There are more things you should know about lists and blocking ops. We
suggest that you read more on the following:

* It is possible to build safer queues or rotating queues using [`LMOVE`](https://redis.io/docs/latest/commands/lmove).
* There is also a blocking variant of the command, called [`BLMOVE`](https://redis.io/docs/latest/commands/blmove).

## Automatic creation and removal of keys

So far in our examples we never had to create empty lists before pushing
elements, or removing empty lists when they no longer have elements inside.
It is Redis' responsibility to delete keys when lists are left empty, or to create
an empty list if the key does not exist and we are trying to add elements
to it, for example, with [`LPUSH`](https://redis.io/docs/latest/commands/lpush).

This is not specific to lists, it applies to all the Redis data types
composed of multiple elements -- Streams, Sets, Sorted Sets and Hashes.

Basically we can summarize the behavior with three rules:

1. When we add an element to an aggregate data type, if the target key does not exist, an empty aggregate data type is created before adding the element.
2. When we remove elements from an aggregate data type, if the value remains empty, the key is automatically destroyed. The Stream data type is the only exception to this rule.
3. Calling a read-only command such as [`LLEN`](https://redis.io/docs/latest/commands/llen) (which returns the length of the list), or a write command removing elements, with an empty key, always produces the same result as if the key is holding an empty aggregate type of the type the command expects to find.

Examples of rule 1:

Automatic creation: Redis automatically creates a list when you push to a non-existent key, simplifying initialization

**Commands:** DEL, LPUSH

**Complexity:**
- DEL: O(N)
- LPUSH: O(1)

**Available in:** Redis CLI, C#, C#, Go, Java (Asynchronous - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> DEL new_bikes
(integer) 0
> LPUSH new_bikes bike:1 bike:2 bike:3
(integer) 3
```

##### C#

```csharp
        bool res35 = db.KeyDelete("new_bikes");
        Console.WriteLine(res35);   // >>> False

        long res36 = db.ListRightPush("new_bikes", ["bike:1", "bike:2", "bike:3"]);
        Console.WriteLine(res36);   // >>> 3
```

##### C#

```csharp
        db.KeyDelete("new_bikes");

        long res36 = db.ListRightPush("new_bikes", ["bike:1", "bike:2", "bike:3"]);
        Console.WriteLine(res36);   // >>> 3
```

##### C#

```csharp
        bool res35 = db.KeyDelete("new_bikes");
        Console.WriteLine(res35);   // >>> False

        long res36 = db.ListRightPush("new_bikes", ["bike:1", "bike:2", "bike:3"]);
        Console.WriteLine(res36);   // >>> 3
```

##### C#

```csharp
        db.KeyDelete("new_bikes");

        long res36 = db.ListRightPush("new_bikes", ["bike:1", "bike:2", "bike:3"]);
        Console.WriteLine(res36);   // >>> 3
```

##### Go

```go
	res37, err := rdb.Del(ctx, "new_bikes").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res37) // >>> 0

	res38, err := rdb.LPush(ctx, "new_bikes", "bike:1", "bike:2", "bike:3").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res38) // >>> 3
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> rule1 = asyncCommands.del("new_bikes").thenCompose(res27 -> {
                System.out.println(res27); // >>> 0

                return asyncCommands.lpush("new_bikes", "bike:1", "bike:2", "bike:3");
            })
                    .thenAccept(System.out::println) // >>> 3
                    .toCompletableFuture();
```

##### Java (Synchronous - Jedis)

```java
        jedis.del("new_bikes");

        long res36 = jedis.lpush("new_bikes", "bike:1", "bike:2", "bike:3");
        System.out.println(res36);  // >>> 3
```

##### JavaScript (Node.js)

```javascript
const res35 = await client.del('new_bikes');
console.log(res35); // 0

const res36 = await client.lPush('new_bikes', ['bike:1', 'bike:2', 'bike:3']);
console.log(res36); // 3
```

##### PHP

```php
        $res35 = $r->del('new_bikes');
        echo $res35 . PHP_EOL;
        // >>> 0

        $res36 = $r->lpush('new_bikes', 'bike:1', 'bike:2', 'bike:3');
        echo $res36 . PHP_EOL;
        // >>> 3
```

##### Python

```python
res35 = r.delete("new_bikes")
print(res35)  # >>> 0

res36 = r.lpush("new_bikes", "bike:1", "bike:2", "bike:3")
print(res36)  # >>> 3
```

##### Ruby

```ruby
res40 = r.del('new_bikes')
puts res40 # >>> 0

res41 = r.lpush('new_bikes', ['bike:1', 'bike:2', 'bike:3'])
puts res41 # >>> 3
```

##### Rust (Asynchronous)

```rust
        if let Ok(res) = r.del("new_bikes").await {
            let res: usize = res;
            println!("{res}"); // >>> 0
        }

        if let Ok(res) = r.lpush("new_bikes", &["bike:1", "bike:2", "bike:3"]).await {
            let res: usize = res;
            println!("{res}"); // >>> 3
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.del("new_bikes") {
            let res: usize = res;
            println!("{res}"); // >>> 0
        }

        if let Ok(res) = r.lpush("new_bikes", &["bike:1", "bike:2", "bike:3"]) {
            let res: usize = res;
            println!("{res}"); // >>> 3
        }
```



However we can't perform operations against the wrong type if the key exists:

Type safety: Redis prevents operations on wrong data types, returning WRONGTYPE error when you try to use list commands on non-list keys

**Builds upon:** rule_1

**Commands:** DEL, SET, TYPE, LPUSH

**Complexity:**
- DEL: O(N)
- SET: O(1)
- TYPE: O(1)
- LPUSH: O(1)

**Available in:** Redis CLI, C#, C#, Go, Java (Asynchronous - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> DEL new_bikes
(integer) 1
> SET new_bikes bike:1
OK
> TYPE new_bikes
string
> LPUSH new_bikes bike:2 bike:3
(error) WRONGTYPE Operation against a key holding the wrong kind of value
```

##### C#

```csharp
        bool res37 = db.StringSet("new_bikes", "bike:1");
        Console.WriteLine(res37);   // >>> True

        RedisType res38 = db.KeyType("new_bikes");
        Console.WriteLine(res38);   // >>> RedisType.String

        try
        {
            long res39 = db.ListRightPush("new_bikes", ["bike:2", "bike:3"]);
        }
        catch (Exception e)
        {
            Console.WriteLine(e);
        }
```

##### C#

```csharp
        db.KeyDelete("new_bikes");
        
        bool res37 = db.StringSet("new_bikes", "bike:1");
        Console.WriteLine(res37);   // >>> True

        RedisType res38 = db.KeyType("new_bikes");
        Console.WriteLine(res38);   // >>> RedisType.String

        try
        {
            long res39 = db.ListRightPush("new_bikes", ["bike:2", "bike:3"]);
        }
        catch (Exception e)
        {
            Console.WriteLine(e);
        }
```

##### C#

```csharp
        bool res37 = db.StringSet("new_bikes", "bike:1");
        Console.WriteLine(res37);   // >>> True

        RedisType res38 = db.KeyType("new_bikes");
        Console.WriteLine(res38);   // >>> RedisType.String

        try
        {
            long res39 = db.ListRightPush("new_bikes", ["bike:2", "bike:3"]);
        }
        catch (Exception e)
        {
            Console.WriteLine(e);
        }
```

##### C#

```csharp
        db.KeyDelete("new_bikes");
        
        bool res37 = db.StringSet("new_bikes", "bike:1");
        Console.WriteLine(res37);   // >>> True

        RedisType res38 = db.KeyType("new_bikes");
        Console.WriteLine(res38);   // >>> RedisType.String

        try
        {
            long res39 = db.ListRightPush("new_bikes", ["bike:2", "bike:3"]);
        }
        catch (Exception e)
        {
            Console.WriteLine(e);
        }
```

##### Go

```go
	rdb.Del(ctx, "new_bikes")

	res39, err := rdb.Set(ctx, "new_bikes", "bike:1", 0).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res39) // >>> OK

	res40, err := rdb.Type(ctx, "new_bikes").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res40) // >>> string

	res41, err := rdb.LPush(ctx, "new_bikes", "bike:2", "bike:3").Result()

	if err != nil {
		fmt.Println(err)
		// >>> WRONGTYPE Operation against a key holding the wrong kind of value
	}

	fmt.Println(res41)
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> rule11 = asyncCommands.set("new_bikes_string", "bike:1").thenCompose(res28 -> {
                System.out.println(res28); // >>> OK

                return asyncCommands.type("new_bikes_string");
            }).thenCompose(res29 -> {
                System.out.println(res29); // >>> string

                return asyncCommands.lpush("new_bikes_string", "bike:2", "bike:3");
            }).handle((res, ex) -> {
                if (ex == null) {
                    return res;
                } else {
                    System.out.println(ex);
                    // >>> java.util.concurrent.CompletionException:
                    // >>> io.lettuce.core.RedisCommandExecutionException:
                    // >>> WRONGTYPE Operation against a key holding the wrong
                    // >>> kind of value

                    return -1L;
                }
            })
                    .thenAccept(System.out::println) // >>> -1
                    .toCompletableFuture();
```

##### Java (Synchronous - Jedis)

```java
        jedis.del("new_bikes");
        
        String res37 = jedis.set("new_bikes", "bike:1");
        System.out.println(res37);  // >>> OK

        String res38 = jedis.type("new_bikes");
        System.out.println(res38);  // >>> string

        try {
            long res39  = jedis.lpush("new_bikes", "bike:2", "bike:3");
        } catch (Exception e) {
            e.printStackTrace();
            // >>> redis.clients.jedis.exceptions.JedisDataException:
            // >>> WRONGTYPE Operation against a key holding the wrong kind of value
        }
```

##### JavaScript (Node.js)

```javascript
await client.del('new_bikes');

const res37 = await client.set('new_bikes', 'bike:1');
console.log(res37);  // 'OK'

const res38 = await client.type('new_bikes');
console.log(res38);  // 'string'

try {
  const res39 = await client.lPush('new_bikes', 'bike:2', 'bike:3');
  // redis.exceptions.ResponseError:
  // [SimpleError: WRONGTYPE Operation against a key holding the wrong kind of value]
}
catch(e){
  console.log(e);
}
```

##### PHP

```php
        $r->del('new_bikes');

        $res37 = $r->set('new_bikes', 'bike:1');
        echo $res37 . PHP_EOL;
        // >>> True

        $res38 = $r->type('new_bikes');
        echo $res38 . PHP_EOL;
        // >>> 'string'

        try {
            $res39 = $r->lpush('new_bikes', 'bike:2', 'bike:3');
            // >>> redis.exceptions.ResponseError:
            // >>> WRONGTYPE Operation against a key holding the wrong kind of value
        } catch (\Predis\Response\ServerException $e) {
            echo $e->getMessage() . PHP_EOL;
        }
```

##### Python

```python
r.delete("new_bikes")

res37 = r.set("new_bikes", "bike:1")
print(res37)  # >>> True

res38 = r.type("new_bikes")
print(res38)  # >>> 'string'

try:
    res39 = r.lpush("new_bikes", "bike:2", "bike:3")
    # >>> redis.exceptions.ResponseError:
    # >>> WRONGTYPE Operation against a key holding the wrong kind of value
except redis.exceptions.ResponseError as e:
    print(e)
```

##### Ruby

```ruby
r.del('new_bikes')

res42 = r.set('new_bikes', 'bike:1')
puts res42 # >>> OK

res43 = r.type('new_bikes')
puts res43 # >>> string

wrong_type_error = nil
begin
  r.lpush('new_bikes', ['bike:2', 'bike:3'])
rescue Redis::CommandError => e
  wrong_type_error = e
  puts e.message # >>> WRONGTYPE Operation against a key holding the wrong kind of value
end
```

##### Rust (Asynchronous)

```rust
        if let Ok(res) = r.del("new_bikes").await {
            let res: usize = res;
            println!("{res}"); // >>> 1
        }

        if let Ok(res) = r.set("new_bikes", "bike:1").await {
            let res: String = res;
            println!("{res}"); // >>> OK
        }

        if let Ok(res) = r.key_type("new_bikes").await {
            let res: ValueType = res;
            let res: String = res.into();
            println!("{res}"); // >>> string
        }

        let res: redis::RedisResult<usize> = r.lpush("new_bikes", &["bike:2", "bike:3"]).await;
        match res {
            Ok(_) => {}
            Err(e) => {
                let msg = e.to_string();
                if let Some((_, tail)) = msg.split_once("WRONGTYPE ") {
                    println!("WRONGTYPE {tail}");
                } else {
                    println!("{msg}");
                }
            }
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.del("new_bikes") {
            let res: usize = res;
            println!("{res}"); // >>> 1
        }

        if let Ok(res) = r.set("new_bikes", "bike:1") {
            let res: String = res;
            println!("{res}"); // >>> OK
        }

        if let Ok(res) = r.key_type("new_bikes") {
            let res: ValueType = res;
            let res: String = res.into();
            println!("{res}"); // >>> string
        }

        let res: redis::RedisResult<usize> = r.lpush("new_bikes", &["bike:2", "bike:3"]);
        match res {
            Ok(_) => {}
            Err(e) => {
                let msg = e.to_string();
                if let Some((_, tail)) = msg.split_once("WRONGTYPE ") {
                    println!("WRONGTYPE {tail}");
                } else {
                    println!("{msg}");
                }
            }
        }
```



Example of rule 2:

Automatic removal: Redis automatically deletes empty lists, freeing memory when the last element is removed

**Builds upon:** lpush_rpush, lpop_rpop

**Commands:** DEL, LPUSH, EXISTS, LPOP

**Complexity:**
- DEL: O(N)
- LPUSH: O(1)
- EXISTS: O(N)
- LPOP: O(N)

**Available in:** Redis CLI, C#, C#, Go, Java (Asynchronous - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> DEL bikes:repairs
(integer) 1
> LPUSH bikes:repairs bike:1 bike:2 bike:3
(integer) 3
> EXISTS bikes:repairs
(integer) 1
> LPOP bikes:repairs
"bike:3"
> LPOP bikes:repairs
"bike:2"
> LPOP bikes:repairs
"bike:1"
> EXISTS bikes:repairs
(integer) 0
```

##### C#

```csharp
        long res40 = db.ListLeftPush("bikes:repairs", ["bike:1", "bike:2", "bike:3"]);
        Console.WriteLine(res40);   // >>> 3

        bool res41 = db.KeyExists("bikes:repairs");
        Console.WriteLine(res41);   // >>> True

        RedisValue res42 = db.ListLeftPop("bikes:repairs");
        Console.WriteLine(res42);   // >>> "bike:3"

        RedisValue res43 = db.ListLeftPop("bikes:repairs");
        Console.WriteLine(res43);   // >>> "bike:2"

        RedisValue res44 = db.ListLeftPop("bikes:repairs");
        Console.WriteLine(res44);   //  >>> "bike:1"

        bool res45 = db.KeyExists("bikes:repairs");
        Console.WriteLine(res45);   // >>> False
```

##### C#

```csharp
        db.KeyDelete("bikes:repairs");

        long res40 = db.ListLeftPush("bikes:repairs", ["bike:1", "bike:2", "bike:3"]);
        Console.WriteLine(res40);   // >>> 3

        bool res41 = db.KeyExists("bikes:repairs");
        Console.WriteLine(res41);   // >>> True

        RedisValue res42 = db.ListLeftPop("bikes:repairs");
        Console.WriteLine(res42);   // >>> "bike:3"

        RedisValue res43 = db.ListLeftPop("bikes:repairs");
        Console.WriteLine(res43);   // >>> "bike:2"

        RedisValue res44 = db.ListLeftPop("bikes:repairs");
        Console.WriteLine(res44);   //  >>> "bike:1"

        bool res45 = db.KeyExists("bikes:repairs");
        Console.WriteLine(res45);   // >>> False
```

##### C#

```csharp
        long res40 = db.ListLeftPush("bikes:repairs", ["bike:1", "bike:2", "bike:3"]);
        Console.WriteLine(res40);   // >>> 3

        bool res41 = db.KeyExists("bikes:repairs");
        Console.WriteLine(res41);   // >>> True

        RedisValue res42 = db.ListLeftPop("bikes:repairs");
        Console.WriteLine(res42);   // >>> "bike:3"

        RedisValue res43 = db.ListLeftPop("bikes:repairs");
        Console.WriteLine(res43);   // >>> "bike:2"

        RedisValue res44 = db.ListLeftPop("bikes:repairs");
        Console.WriteLine(res44);   //  >>> "bike:1"

        bool res45 = db.KeyExists("bikes:repairs");
        Console.WriteLine(res45);   // >>> False
```

##### C#

```csharp
        db.KeyDelete("bikes:repairs");

        long res40 = db.ListLeftPush("bikes:repairs", ["bike:1", "bike:2", "bike:3"]);
        Console.WriteLine(res40);   // >>> 3

        bool res41 = db.KeyExists("bikes:repairs");
        Console.WriteLine(res41);   // >>> True

        RedisValue res42 = db.ListLeftPop("bikes:repairs");
        Console.WriteLine(res42);   // >>> "bike:3"

        RedisValue res43 = db.ListLeftPop("bikes:repairs");
        Console.WriteLine(res43);   // >>> "bike:2"

        RedisValue res44 = db.ListLeftPop("bikes:repairs");
        Console.WriteLine(res44);   //  >>> "bike:1"

        bool res45 = db.KeyExists("bikes:repairs");
        Console.WriteLine(res45);   // >>> False
```

##### Go

```go
	rdb.Del(ctx, "bikes:repairs")
	res42, err := rdb.LPush(ctx, "bikes:repairs", "bike:1", "bike:2", "bike:3").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res42) // >>> 3

	res43, err := rdb.Exists(ctx, "bikes:repairs").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res43) // >>> 1

	res44, err := rdb.LPop(ctx, "bikes:repairs").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res44) // >>> bike:3

	res45, err := rdb.LPop(ctx, "bikes:repairs").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res45) // >>> bike:2

	res46, err := rdb.LPop(ctx, "bikes:repairs").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res46) // >>> bike:1

	res47, err := rdb.Exists(ctx, "bikes:repairs").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res47) // >>> 0
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> rule2 = asyncCommands.lpush("bikes:repairs", "bike:1", "bike:2", "bike:3")
                    .thenCompose(res30 -> {
                        System.out.println(res30); // >>> 3

                        return asyncCommands.exists("bikes:repairs");
                    }).thenCompose(res31 -> {
                        System.out.println(res31); // >>> 1

                        return asyncCommands.lpop("bikes:repairs");
                    }).thenCompose(res32 -> {
                        System.out.println(res32); // >>> bike:3

                        return asyncCommands.lpop("bikes:repairs");
                    }).thenCompose(res33 -> {
                        System.out.println(res33); // >>> bike:2

                        return asyncCommands.lpop("bikes:repairs");
                    }).thenCompose(res34 -> {
                        System.out.println(res34); // >>> bike:1

                        return asyncCommands.exists("bikes:repairs");
                    })
                    .thenAccept(System.out::println) // >>> 0
                    .toCompletableFuture();
```

##### Java (Synchronous - Jedis)

```java
        jedis.del("bikes:repairs");

        jedis.lpush("bikes:repairs", "bike:1", "bike:2", "bike:3");
        System.out.println(res36);  // >>> 3

        boolean res40 = jedis.exists("bikes:repairs");
        System.out.println(res40);  // >>> true

        String res41 = jedis.lpop("bikes:repairs");
        System.out.println(res41);  // >>> bike:3

        String res42 = jedis.lpop("bikes:repairs");
        System.out.println(res42);  // >>> bike:2

        String res43 = jedis.lpop("bikes:repairs");
        System.out.println(res43);  // >>> bike:1

        boolean res44 = jedis.exists("bikes:repairs");
        System.out.println(res44);  // >>> false
```

##### JavaScript (Node.js)

```javascript
await client.del('bikes:repairs');

await client.lPush('bikes:repairs', ['bike:1', 'bike:2', 'bike:3']);
console.log(res36);  // 3

const res40 = await client.exists('bikes:repairs')
console.log(res40);  // 1

const res41 = await client.lPop('bikes:repairs');
console.log(res41);  // 'bike:3'

const res42 = await client.lPop('bikes:repairs');
console.log(res42);  // 'bike:2'

const res43 = await client.lPop('bikes:repairs');
console.log(res43);  // 'bike:1'

const res44 = await client.exists('bikes:repairs');
console.log(res44);  // 0
```

##### PHP

```php
        $r->del('bikes:repairs');
        $res36 = $r->lpush('bikes:repairs', 'bike:1', 'bike:2', 'bike:3');
        echo $res36 . PHP_EOL;
        // >>> 3

        $res40 = $r->exists('bikes:repairs');
        echo $res40 . PHP_EOL;
        // >>> 1

        $res41 = $r->lpop('bikes:repairs');
        echo $res41 . PHP_EOL;
        // >>> 'bike:3'

        $res42 = $r->lpop('bikes:repairs');
        echo $res42 . PHP_EOL;
        // >>> 'bike:2'

        $res43 = $r->lpop('bikes:repairs');
        echo $res43 . PHP_EOL;
        // >>> 'bike:1'

        $res44 = $r->exists('bikes:repairs');
        echo $res44 . PHP_EOL;
        // >>> False
```

##### Python

```python
r.delete("bikes:repairs")

r.lpush("bikes:repairs", "bike:1", "bike:2", "bike:3")
print(res36)  # >>> 3

res40 = r.exists("bikes:repairs")
print(res40)  # >>> 1

res41 = r.lpop("bikes:repairs")
print(res41)  # >>> 'bike:3'

res42 = r.lpop("bikes:repairs")
print(res42)  # >>> 'bike:2'

res43 = r.lpop("bikes:repairs")
print(res43)  # >>> 'bike:1'

res44 = r.exists("bikes:repairs")
print(res44)  # >>> False
```

##### Ruby

```ruby
r.del('bikes:repairs')

res44 = r.lpush('bikes:repairs', ['bike:1', 'bike:2', 'bike:3'])
puts res44 # >>> 3

res45 = r.exists('bikes:repairs')
puts res45 # >>> 1

res46 = r.lpop('bikes:repairs')
puts res46 # >>> bike:3

res47 = r.lpop('bikes:repairs')
puts res47 # >>> bike:2

res48 = r.lpop('bikes:repairs')
puts res48 # >>> bike:1

res49 = r.exists('bikes:repairs')
puts res49 # >>> 0
```

##### Rust (Asynchronous)

```rust
        let _: usize = r.rpush("bikes:repairs", "bike:placeholder").await.unwrap_or(0);
        if let Ok(res) = r.del("bikes:repairs").await {
            let res: usize = res;
            println!("{res}"); // >>> 1
        }

        if let Ok(res) = r.lpush("bikes:repairs", &["bike:1", "bike:2", "bike:3"]).await {
            let res: usize = res;
            println!("{res}"); // >>> 3
        }

        if let Ok(res) = r.exists("bikes:repairs").await {
            let res: bool = res;
            println!("{}", i32::from(res)); // >>> 1
        }

        if let Ok(res) = r.lpop("bikes:repairs", None).await {
            let res: Option<String> = res;
            print_optional_string(res.clone()); // >>> bike:3
        }

        if let Ok(res) = r.lpop("bikes:repairs", None).await {
            let res: Option<String> = res;
            print_optional_string(res.clone()); // >>> bike:2
        }

        if let Ok(res) = r.lpop("bikes:repairs", None).await {
            let res: Option<String> = res;
            print_optional_string(res.clone()); // >>> bike:1
        }

        if let Ok(res) = r.exists("bikes:repairs").await {
            let res: bool = res;
            println!("{}", i32::from(res)); // >>> 0
        }
```

##### Rust (Synchronous)

```rust
        let _: usize = r.rpush("bikes:repairs", "bike:placeholder").unwrap_or(0);
        if let Ok(res) = r.del("bikes:repairs") {
            let res: usize = res;
            println!("{res}"); // >>> 1
        }

        if let Ok(res) = r.lpush("bikes:repairs", &["bike:1", "bike:2", "bike:3"]) {
            let res: usize = res;
            println!("{res}"); // >>> 3
        }

        if let Ok(res) = r.exists("bikes:repairs") {
            let res: bool = res;
            println!("{}", i32::from(res)); // >>> 1
        }

        if let Ok(res) = r.lpop("bikes:repairs", None) {
            let res: Option<String> = res;
            print_optional_string(res.clone()); // >>> bike:3
        }

        if let Ok(res) = r.lpop("bikes:repairs", None) {
            let res: Option<String> = res;
            print_optional_string(res.clone()); // >>> bike:2
        }

        if let Ok(res) = r.lpop("bikes:repairs", None) {
            let res: Option<String> = res;
            print_optional_string(res.clone()); // >>> bike:1
        }

        if let Ok(res) = r.exists("bikes:repairs") {
            let res: bool = res;
            println!("{}", i32::from(res)); // >>> 0
        }
```



The key no longer exists after all the elements are popped.

Example of rule 3:

Nil handling: Read-only commands on non-existent keys return empty results (0 or nil) instead of errors, treating them as empty lists

**Commands:** DEL, LLEN, LPOP

**Complexity:**
- DEL: O(N)
- LLEN: O(1)
- LPOP: O(N)

**Available in:** Redis CLI, C#, C#, Go, Java (Asynchronous - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> DEL bikes:repairs
(integer) 1
> LLEN bikes:repairs
(integer) 0
> LPOP bikes:repairs
(nil)
```

##### C#

```csharp
        bool res46 = db.KeyDelete("bikes:repairs");
        Console.WriteLine(res46);   // >>> False

        long res47 = db.ListLength("bikes:repairs");
        Console.WriteLine(res47);   // >>> 0

        RedisValue res48 = db.ListLeftPop("bikes:repairs");
        Console.WriteLine(res48);   // >>> Null
```

##### C#

```csharp
        db.KeyDelete("bikes:repairs");

        long res47 = db.ListLength("bikes:repairs");
        Console.WriteLine(res47);   // >>> 0

        RedisValue res48 = db.ListLeftPop("bikes:repairs");
        Console.WriteLine(res48);   // >>> Null
```

##### C#

```csharp
        bool res46 = db.KeyDelete("bikes:repairs");
        Console.WriteLine(res46);   // >>> False

        long res47 = db.ListLength("bikes:repairs");
        Console.WriteLine(res47);   // >>> 0

        RedisValue res48 = db.ListLeftPop("bikes:repairs");
        Console.WriteLine(res48);   // >>> Null
```

##### C#

```csharp
        db.KeyDelete("bikes:repairs");

        long res47 = db.ListLength("bikes:repairs");
        Console.WriteLine(res47);   // >>> 0

        RedisValue res48 = db.ListLeftPop("bikes:repairs");
        Console.WriteLine(res48);   // >>> Null
```

##### Go

```go
	rdb.Del(ctx, "bikes:repairs")

	res48, err := rdb.Del(ctx, "bikes:repairs").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res48) // >>> 0

	res49, err := rdb.LLen(ctx, "bikes:repairs").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res49) // >>> 0

	res50, err := rdb.LPop(ctx, "bikes:repairs").Result()

	if err != nil {
		fmt.Println(err) // >>> redis: nil
	}

	fmt.Println(res50) // >>> <empty string>
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> rule3 = asyncCommands.del("bikes:repairs").thenCompose(res35 -> {
                System.out.println(res35); // >>> 0

                return asyncCommands.llen("bikes:repairs");
            }).thenCompose(res36 -> {
                System.out.println(res36); // >>> 0

                return asyncCommands.lpop("bikes:repairs");
            })
                    .thenAccept(System.out::println) // >>> null
                    .toCompletableFuture();
```

##### Java (Synchronous - Jedis)

```java
        jedis.del("bikes:repairs");

        long res46 = jedis.llen("bikes:repairs");
        System.out.println(res46);  // >>> 0

        String res47 = jedis.lpop("bikes:repairs");
        System.out.println(res47);  // >>> null
```

##### JavaScript (Node.js)

```javascript
await client.del('bikes:repairs');

const res45 = await client.del('bikes:repairs');
console.log(res45);  // 0

const res46 = await client.lLen('bikes:repairs');
console.log(res46);  // 0

const res47 = await client.lPop('bikes:repairs');
console.log(res47);  // null
```

##### PHP

```php
        $res45 = $r->del('bikes:repairs');
        echo $res45 . PHP_EOL;
        // >>> 0

        $res46 = $r->llen('bikes:repairs');
        echo $res46 . PHP_EOL;
        // >>> 0

        $res47 = $r->lpop('bikes:repairs');
        echo $res47 . PHP_EOL;
        // >>> None
```

##### Python

```python
r.delete("bikes:repairs")

res45 = r.delete("bikes:repairs")
print(res45)  # >>> 0

res46 = r.llen("bikes:repairs")
print(res46)  # >>> 0

res47 = r.lpop("bikes:repairs")
print(res47)  # >>> None
```

##### Ruby

```ruby
r.del('bikes:repairs')

res50 = r.del('bikes:repairs')
puts res50 # >>> 0

res51 = r.llen('bikes:repairs')
puts res51 # >>> 0

res52 = r.lpop('bikes:repairs')
puts res52.inspect # >>> nil
```

##### Rust (Asynchronous)

```rust
        if let Ok(res) = r.del("bikes:repairs").await {
            let res: usize = res;
            println!("{res}"); // >>> 0
        }

        if let Ok(res) = r.llen("bikes:repairs").await {
            let res: usize = res;
            println!("{res}"); // >>> 0
        }

        if let Ok(res) = r.lpop("bikes:repairs", None).await {
            let res: Option<String> = res;
            print_optional_string(res.clone()); // >>> (nil)
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.del("bikes:repairs") {
            let res: usize = res;
            println!("{res}"); // >>> 0
        }

        if let Ok(res) = r.llen("bikes:repairs") {
            let res: usize = res;
            println!("{res}"); // >>> 0
        }

        if let Ok(res) = r.lpop("bikes:repairs", None) {
            let res: Option<String> = res;
            print_optional_string(res.clone()); // >>> (nil)
        }
```




## Limits

The maximum length of a Redis list is 2^32 - 1 (4,294,967,295) elements.

## Performance

List operations that access its head or tail are O(1), which means they're highly efficient.
However, commands that manipulate elements within a list are usually O(n).
Examples of these include [`LINDEX`](https://redis.io/docs/latest/commands/lindex), [`LINSERT`](https://redis.io/docs/latest/commands/linsert), and [`LSET`](https://redis.io/docs/latest/commands/lset).
Exercise caution when running these commands, mainly when operating on large lists.

## Alternatives

Consider [Redis streams](https://redis.io/docs/latest/develop/data-types/streams) as an alternative to lists when you need to store and process an indeterminate series of events.

## Learn more

* [Redis Lists Explained](https://www.youtube.com/watch?v=PB5SeOkkxQc) is a short, comprehensive video explainer on Redis lists.
* [Redis University's RU101](https://university.redis.com/courses/ru101/) covers Redis lists in detail.

