# Path

```json metadata
{
  "schema_version": 2,
  "title": "Path",
  "description": "Access specific elements within a JSON document",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"jsonpath-support","title":"JSONPath support"},{"id":"jsonpath-syntax","title":"JSONPath syntax"},{"id":"evaluation-semantics","title":"Evaluation semantics"},{"children":[{"id":"access-examples","title":"Access examples"},{"id":"filter-examples","title":"Filter examples"},{"id":"update-examples","title":"Update examples"}],"id":"jsonpath-examples","title":"JSONPath examples"},{"id":"projection-expressions","title":"Projection expressions"},{"children":[{"id":"json-key-names-and-path-compatibility","title":"JSON key names and path compatibility"}],"id":"legacy-path-syntax","title":"Legacy path syntax"},{"id":"time-complexity-of-path-evaluation","title":"Time complexity of path evaluation"}]}

,
  "codeExamples": [{"codetabsId":"json_tutorial-stepset_bikes","commands":[{"acl_categories":["@write","@json"],"complexity":"O(M+N)","name":"JSON.SET"}],"description":"Setup: Create a complex JSON document with nested objects and arrays to use in JSONPath examples","difficulty":"beginner","id":"set_bikes","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_json_tutorial-stepset_bikes"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_json_tutorial-stepset_bikes"},{"id":"Node-js","panelId":"panel_Nodejs_json_tutorial-stepset_bikes"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_json_tutorial-stepset_bikes"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_json_tutorial-stepset_bikes"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_json_tutorial-stepset_bikes"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_json_tutorial-stepset_bikes"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_json_tutorial-stepset_bikes"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_json_tutorial-stepset_bikes"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_json_tutorial-stepset_bikes"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_json_tutorial-stepset_bikes"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_json_tutorial-stepset_bikes"}]},{"buildsUpon":["set_bikes"],"codetabsId":"json_tutorial-stepget_bikes","commands":[{"acl_categories":["@read","@json"],"complexity":"O(N)","name":"JSON.GET"}],"description":"Wildcard queries: Use the * operator to retrieve all items in a collection when you need to access all elements at a specific level","difficulty":"beginner","id":"get_bikes","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_json_tutorial-stepget_bikes"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_json_tutorial-stepget_bikes"},{"id":"Node-js","panelId":"panel_Nodejs_json_tutorial-stepget_bikes"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_json_tutorial-stepget_bikes"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_json_tutorial-stepget_bikes"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_json_tutorial-stepget_bikes"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_json_tutorial-stepget_bikes"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_json_tutorial-stepget_bikes"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_json_tutorial-stepget_bikes"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_json_tutorial-stepget_bikes"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_json_tutorial-stepget_bikes"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_json_tutorial-stepget_bikes"}]},{"buildsUpon":["get_bikes"],"codetabsId":"json_tutorial-stepget_mtnbikes","commands":[{"acl_categories":["@read","@json"],"complexity":"O(N)","name":"JSON.GET"}],"description":"Array element access: Use bracket notation and array subscripts to access specific array elements or all elements with [*] when you need to retrieve values from arrays","difficulty":"intermediate","id":"get_mtnbikes","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_json_tutorial-stepget_mtnbikes"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_json_tutorial-stepget_mtnbikes"},{"id":"Node-js","panelId":"panel_Nodejs_json_tutorial-stepget_mtnbikes"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_json_tutorial-stepget_mtnbikes"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_json_tutorial-stepget_mtnbikes"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_json_tutorial-stepget_mtnbikes"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_json_tutorial-stepget_mtnbikes"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_json_tutorial-stepget_mtnbikes"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_json_tutorial-stepget_mtnbikes"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_json_tutorial-stepget_mtnbikes"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_json_tutorial-stepget_mtnbikes"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_json_tutorial-stepget_mtnbikes"}]},{"buildsUpon":["get_mtnbikes"],"codetabsId":"json_tutorial-stepget_models","commands":[{"acl_categories":["@read","@json"],"complexity":"O(N)","name":"JSON.GET"}],"description":"Recursive descent: Use the .. operator to search for a field at any depth in the JSON document when you need to find values across multiple nesting levels","difficulty":"intermediate","id":"get_models","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_json_tutorial-stepget_models"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_json_tutorial-stepget_models"},{"id":"Node-js","panelId":"panel_Nodejs_json_tutorial-stepget_models"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_json_tutorial-stepget_models"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_json_tutorial-stepget_models"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_json_tutorial-stepget_models"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_json_tutorial-stepget_models"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_json_tutorial-stepget_models"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_json_tutorial-stepget_models"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_json_tutorial-stepget_models"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_json_tutorial-stepget_models"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_json_tutorial-stepget_models"}]},{"buildsUpon":["get_mtnbikes"],"codetabsId":"json_tutorial-stepget2mtnbikes","commands":[{"acl_categories":["@read","@json"],"complexity":"O(N)","name":"JSON.GET"}],"description":"Array slicing: Use [start:end] syntax to select a range of array elements when you need to retrieve a subset of items from an array","difficulty":"intermediate","id":"get2mtnbikes","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_json_tutorial-stepget2mtnbikes"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_json_tutorial-stepget2mtnbikes"},{"id":"Node-js","panelId":"panel_Nodejs_json_tutorial-stepget2mtnbikes"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_json_tutorial-stepget2mtnbikes"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_json_tutorial-stepget2mtnbikes"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_json_tutorial-stepget2mtnbikes"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_json_tutorial-stepget2mtnbikes"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_json_tutorial-stepget2mtnbikes"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_json_tutorial-stepget2mtnbikes"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_json_tutorial-stepget2mtnbikes"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_json_tutorial-stepget2mtnbikes"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_json_tutorial-stepget2mtnbikes"}]},{"buildsUpon":["get_models"],"codetabsId":"json_tutorial-stepfilter1","commands":[{"acl_categories":["@read","@json"],"complexity":"O(N)","name":"JSON.GET"}],"description":"Filter expressions: Use ?() with comparison and logical operators to select elements matching specific conditions when you need to query based on multiple criteria","difficulty":"advanced","id":"filter1","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_json_tutorial-stepfilter1"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_json_tutorial-stepfilter1"},{"id":"Node-js","panelId":"panel_Nodejs_json_tutorial-stepfilter1"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_json_tutorial-stepfilter1"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_json_tutorial-stepfilter1"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_json_tutorial-stepfilter1"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_json_tutorial-stepfilter1"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_json_tutorial-stepfilter1"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_json_tutorial-stepfilter1"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_json_tutorial-stepfilter1"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_json_tutorial-stepfilter1"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_json_tutorial-stepfilter1"}]},{"buildsUpon":["filter1"],"codetabsId":"json_tutorial-stepfilter2","commands":[{"acl_categories":["@read","@json"],"complexity":"O(N)","name":"JSON.GET"}],"description":"Equality filters: Use == operator in filter expressions to select elements with specific field values when you need to find items matching exact criteria","difficulty":"advanced","id":"filter2","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_json_tutorial-stepfilter2"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_json_tutorial-stepfilter2"},{"id":"Node-js","panelId":"panel_Nodejs_json_tutorial-stepfilter2"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_json_tutorial-stepfilter2"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_json_tutorial-stepfilter2"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_json_tutorial-stepfilter2"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_json_tutorial-stepfilter2"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_json_tutorial-stepfilter2"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_json_tutorial-stepfilter2"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_json_tutorial-stepfilter2"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_json_tutorial-stepfilter2"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_json_tutorial-stepfilter2"}]},{"buildsUpon":["filter2"],"codetabsId":"json_tutorial-stepfilter3","commands":[{"acl_categories":["@read","@json"],"complexity":"O(N)","name":"JSON.GET"}],"description":"Regex filters: Use =~ operator with regular expressions in filter expressions to match patterns in string values when you need flexible pattern-based filtering","difficulty":"advanced","id":"filter3","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_json_tutorial-stepfilter3"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_json_tutorial-stepfilter3"},{"id":"Node-js","panelId":"panel_Nodejs_json_tutorial-stepfilter3"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_json_tutorial-stepfilter3"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_json_tutorial-stepfilter3"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_json_tutorial-stepfilter3"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_json_tutorial-stepfilter3"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_json_tutorial-stepfilter3"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_json_tutorial-stepfilter3"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_json_tutorial-stepfilter3"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_json_tutorial-stepfilter3"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_json_tutorial-stepfilter3"}]},{"buildsUpon":["filter3"],"codetabsId":"json_tutorial-stepfilter4","commands":[{"acl_categories":["@write","@json"],"complexity":"O(M+N)","name":"JSON.SET"},{"acl_categories":["@read","@json"],"complexity":"O(N)","name":"JSON.GET"}],"description":"Dynamic regex filters: Use regex patterns stored in JSON properties to filter elements when you need to apply patterns defined within the document itself","difficulty":"advanced","id":"filter4","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_json_tutorial-stepfilter4"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_json_tutorial-stepfilter4"},{"id":"Node-js","panelId":"panel_Nodejs_json_tutorial-stepfilter4"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_json_tutorial-stepfilter4"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_json_tutorial-stepfilter4"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_json_tutorial-stepfilter4"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_json_tutorial-stepfilter4"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_json_tutorial-stepfilter4"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_json_tutorial-stepfilter4"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_json_tutorial-stepfilter4"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_json_tutorial-stepfilter4"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_json_tutorial-stepfilter4"}]},{"codetabsId":"json_path_ops-stepfilter_negation","commands":[{"acl_categories":["@write","@json"],"complexity":"O(M+N)","name":"JSON.SET"},{"acl_categories":["@read","@json"],"complexity":"O(N)","name":"JSON.GET"}],"description":"Filter negation: Use the ! operator to invert a filter condition when you need to select elements that do not match","difficulty":"advanced","id":"filter_negation","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_json_path_ops-stepfilter_negation"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_json_path_ops-stepfilter_negation"},{"id":"Node-js","panelId":"panel_Nodejs_json_path_ops-stepfilter_negation"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_json_path_ops-stepfilter_negation"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_json_path_ops-stepfilter_negation"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_json_path_ops-stepfilter_negation"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_json_path_ops-stepfilter_negation"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_json_path_ops-stepfilter_negation"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_json_path_ops-stepfilter_negation"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_json_path_ops-stepfilter_negation"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_json_path_ops-stepfilter_negation"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_json_path_ops-stepfilter_negation"}]},{"codetabsId":"json_path_ops-stepfilter_literal_eq","commands":[{"acl_categories":["@write","@json"],"complexity":"O(M+N)","name":"JSON.SET"},{"acl_categories":["@read","@json"],"complexity":"O(N)","name":"JSON.GET"}],"description":"Literal comparison: Use == and != to compare array and object literals by structural equality when you need to match a whole nested value","difficulty":"advanced","id":"filter_literal_eq","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_json_path_ops-stepfilter_literal_eq"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_json_path_ops-stepfilter_literal_eq"},{"id":"Node-js","panelId":"panel_Nodejs_json_path_ops-stepfilter_literal_eq"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_json_path_ops-stepfilter_literal_eq"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_json_path_ops-stepfilter_literal_eq"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_json_path_ops-stepfilter_literal_eq"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_json_path_ops-stepfilter_literal_eq"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_json_path_ops-stepfilter_literal_eq"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_json_path_ops-stepfilter_literal_eq"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_json_path_ops-stepfilter_literal_eq"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_json_path_ops-stepfilter_literal_eq"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_json_path_ops-stepfilter_literal_eq"}]},{"codetabsId":"json_path_ops-stepfilter_arithmetic","commands":[{"acl_categories":["@write","@json"],"complexity":"O(M+N)","name":"JSON.SET"},{"acl_categories":["@read","@json"],"complexity":"O(N)","name":"JSON.GET"}],"description":"Arithmetic in filters: Use \u0026#43;, -, *, / and % inside a filter condition when you need to compute a value before comparing it","difficulty":"advanced","id":"filter_arithmetic","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_json_path_ops-stepfilter_arithmetic"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_json_path_ops-stepfilter_arithmetic"},{"id":"Node-js","panelId":"panel_Nodejs_json_path_ops-stepfilter_arithmetic"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_json_path_ops-stepfilter_arithmetic"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_json_path_ops-stepfilter_arithmetic"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_json_path_ops-stepfilter_arithmetic"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_json_path_ops-stepfilter_arithmetic"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_json_path_ops-stepfilter_arithmetic"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_json_path_ops-stepfilter_arithmetic"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_json_path_ops-stepfilter_arithmetic"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_json_path_ops-stepfilter_arithmetic"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_json_path_ops-stepfilter_arithmetic"}]},{"codetabsId":"json_path_ops-stepfilter_membership","commands":[{"acl_categories":["@write","@json"],"complexity":"O(M+N)","name":"JSON.SET"},{"acl_categories":["@read","@json"],"complexity":"O(N)","name":"JSON.GET"}],"description":"Membership filters: Use in and nin to test whether a value is a member of an array when you need set-style matching","difficulty":"advanced","id":"filter_membership","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_json_path_ops-stepfilter_membership"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_json_path_ops-stepfilter_membership"},{"id":"Node-js","panelId":"panel_Nodejs_json_path_ops-stepfilter_membership"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_json_path_ops-stepfilter_membership"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_json_path_ops-stepfilter_membership"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_json_path_ops-stepfilter_membership"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_json_path_ops-stepfilter_membership"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_json_path_ops-stepfilter_membership"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_json_path_ops-stepfilter_membership"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_json_path_ops-stepfilter_membership"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_json_path_ops-stepfilter_membership"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_json_path_ops-stepfilter_membership"}]},{"codetabsId":"json_path_ops-stepfilter_set_relations","commands":[{"acl_categories":["@write","@json"],"complexity":"O(M+N)","name":"JSON.SET"},{"acl_categories":["@read","@json"],"complexity":"O(N)","name":"JSON.GET"}],"description":"Set relation filters: Use subsetof, anyof, and noneof to compare two arrays when you need to match based on their overlap","difficulty":"advanced","id":"filter_set_relations","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_json_path_ops-stepfilter_set_relations"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_json_path_ops-stepfilter_set_relations"},{"id":"Node-js","panelId":"panel_Nodejs_json_path_ops-stepfilter_set_relations"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_json_path_ops-stepfilter_set_relations"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_json_path_ops-stepfilter_set_relations"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_json_path_ops-stepfilter_set_relations"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_json_path_ops-stepfilter_set_relations"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_json_path_ops-stepfilter_set_relations"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_json_path_ops-stepfilter_set_relations"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_json_path_ops-stepfilter_set_relations"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_json_path_ops-stepfilter_set_relations"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_json_path_ops-stepfilter_set_relations"}]},{"codetabsId":"json_path_ops-stepfilter_size_empty","commands":[{"acl_categories":["@write","@json"],"complexity":"O(M+N)","name":"JSON.SET"},{"acl_categories":["@read","@json"],"complexity":"O(N)","name":"JSON.GET"}],"description":"Size and emptiness filters: Use sizeof and empty to filter by the size or emptiness of a string, array, or object","difficulty":"advanced","id":"filter_size_empty","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_json_path_ops-stepfilter_size_empty"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_json_path_ops-stepfilter_size_empty"},{"id":"Node-js","panelId":"panel_Nodejs_json_path_ops-stepfilter_size_empty"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_json_path_ops-stepfilter_size_empty"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_json_path_ops-stepfilter_size_empty"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_json_path_ops-stepfilter_size_empty"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_json_path_ops-stepfilter_size_empty"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_json_path_ops-stepfilter_size_empty"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_json_path_ops-stepfilter_size_empty"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_json_path_ops-stepfilter_size_empty"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_json_path_ops-stepfilter_size_empty"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_json_path_ops-stepfilter_size_empty"}]},{"codetabsId":"json_path_ops-stepfilter_getkeys","commands":[{"acl_categories":["@write","@json"],"complexity":"O(M+N)","name":"JSON.SET"},{"acl_categories":["@read","@json"],"complexity":"O(N)","name":"JSON.GET"}],"description":"Get-keys filter: Use the ~ operator to retrieve an object\u0026amp;#39;s member names as a list of strings","difficulty":"advanced","id":"filter_getkeys","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_json_path_ops-stepfilter_getkeys"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_json_path_ops-stepfilter_getkeys"},{"id":"Node-js","panelId":"panel_Nodejs_json_path_ops-stepfilter_getkeys"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_json_path_ops-stepfilter_getkeys"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_json_path_ops-stepfilter_getkeys"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_json_path_ops-stepfilter_getkeys"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_json_path_ops-stepfilter_getkeys"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_json_path_ops-stepfilter_getkeys"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_json_path_ops-stepfilter_getkeys"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_json_path_ops-stepfilter_getkeys"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_json_path_ops-stepfilter_getkeys"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_json_path_ops-stepfilter_getkeys"}]},{"codetabsId":"json_path_ops-stepfunc_length","commands":[{"acl_categories":["@write","@json"],"complexity":"O(M+N)","name":"JSON.SET"},{"acl_categories":["@read","@json"],"complexity":"O(N)","name":"JSON.GET"}],"description":"Length function: Use length() to get the number of characters in a string, elements in an array, or members in an object","difficulty":"advanced","id":"func_length","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_json_path_ops-stepfunc_length"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_json_path_ops-stepfunc_length"},{"id":"Node-js","panelId":"panel_Nodejs_json_path_ops-stepfunc_length"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_json_path_ops-stepfunc_length"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_json_path_ops-stepfunc_length"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_json_path_ops-stepfunc_length"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_json_path_ops-stepfunc_length"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_json_path_ops-stepfunc_length"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_json_path_ops-stepfunc_length"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_json_path_ops-stepfunc_length"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_json_path_ops-stepfunc_length"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_json_path_ops-stepfunc_length"}]},{"codetabsId":"json_path_ops-stepfunc_count","commands":[{"acl_categories":["@write","@json"],"complexity":"O(M+N)","name":"JSON.SET"},{"acl_categories":["@read","@json"],"complexity":"O(N)","name":"JSON.GET"}],"description":"Count function: Use count() to get the number of nodes selected by a query","difficulty":"advanced","id":"func_count","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_json_path_ops-stepfunc_count"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_json_path_ops-stepfunc_count"},{"id":"Node-js","panelId":"panel_Nodejs_json_path_ops-stepfunc_count"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_json_path_ops-stepfunc_count"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_json_path_ops-stepfunc_count"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_json_path_ops-stepfunc_count"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_json_path_ops-stepfunc_count"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_json_path_ops-stepfunc_count"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_json_path_ops-stepfunc_count"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_json_path_ops-stepfunc_count"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_json_path_ops-stepfunc_count"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_json_path_ops-stepfunc_count"}]},{"codetabsId":"json_path_ops-stepfunc_value","commands":[{"acl_categories":["@write","@json"],"complexity":"O(M+N)","name":"JSON.SET"},{"acl_categories":["@read","@json"],"complexity":"O(N)","name":"JSON.GET"}],"description":"Value function: Use value() to get the value of a query that selects exactly one node","difficulty":"advanced","id":"func_value","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_json_path_ops-stepfunc_value"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_json_path_ops-stepfunc_value"},{"id":"Node-js","panelId":"panel_Nodejs_json_path_ops-stepfunc_value"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_json_path_ops-stepfunc_value"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_json_path_ops-stepfunc_value"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_json_path_ops-stepfunc_value"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_json_path_ops-stepfunc_value"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_json_path_ops-stepfunc_value"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_json_path_ops-stepfunc_value"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_json_path_ops-stepfunc_value"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_json_path_ops-stepfunc_value"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_json_path_ops-stepfunc_value"}]},{"codetabsId":"json_path_ops-stepfunc_keys","commands":[{"acl_categories":["@write","@json"],"complexity":"O(M+N)","name":"JSON.SET"},{"acl_categories":["@read","@json"],"complexity":"O(N)","name":"JSON.GET"}],"description":"Keys function: Use keys() to get an object\u0026amp;#39;s member names as a composable, chainable list of strings","difficulty":"advanced","id":"func_keys","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_json_path_ops-stepfunc_keys"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_json_path_ops-stepfunc_keys"},{"id":"Node-js","panelId":"panel_Nodejs_json_path_ops-stepfunc_keys"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_json_path_ops-stepfunc_keys"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_json_path_ops-stepfunc_keys"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_json_path_ops-stepfunc_keys"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_json_path_ops-stepfunc_keys"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_json_path_ops-stepfunc_keys"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_json_path_ops-stepfunc_keys"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_json_path_ops-stepfunc_keys"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_json_path_ops-stepfunc_keys"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_json_path_ops-stepfunc_keys"}]},{"codetabsId":"json_path_ops-stepfunc_match_search","commands":[{"acl_categories":["@write","@json"],"complexity":"O(M+N)","name":"JSON.SET"},{"acl_categories":["@read","@json"],"complexity":"O(N)","name":"JSON.GET"}],"description":"Regex functions: Use match() for an anchored (whole-string) regular expression match and search() for a partial match","difficulty":"advanced","id":"func_match_search","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_json_path_ops-stepfunc_match_search"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_json_path_ops-stepfunc_match_search"},{"id":"Node-js","panelId":"panel_Nodejs_json_path_ops-stepfunc_match_search"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_json_path_ops-stepfunc_match_search"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_json_path_ops-stepfunc_match_search"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_json_path_ops-stepfunc_match_search"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_json_path_ops-stepfunc_match_search"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_json_path_ops-stepfunc_match_search"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_json_path_ops-stepfunc_match_search"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_json_path_ops-stepfunc_match_search"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_json_path_ops-stepfunc_match_search"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_json_path_ops-stepfunc_match_search"}]},{"codetabsId":"json_path_ops-stepfunc_concat","commands":[{"acl_categories":["@write","@json"],"complexity":"O(M+N)","name":"JSON.SET"},{"acl_categories":["@read","@json"],"complexity":"O(N)","name":"JSON.GET"}],"description":"Concat function: Use concat() to join string arguments into a single string for comparison in a filter","difficulty":"advanced","id":"func_concat","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_json_path_ops-stepfunc_concat"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_json_path_ops-stepfunc_concat"},{"id":"Node-js","panelId":"panel_Nodejs_json_path_ops-stepfunc_concat"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_json_path_ops-stepfunc_concat"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_json_path_ops-stepfunc_concat"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_json_path_ops-stepfunc_concat"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_json_path_ops-stepfunc_concat"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_json_path_ops-stepfunc_concat"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_json_path_ops-stepfunc_concat"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_json_path_ops-stepfunc_concat"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_json_path_ops-stepfunc_concat"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_json_path_ops-stepfunc_concat"}]},{"codetabsId":"json_path_ops-stepfunc_math","commands":[{"acl_categories":["@write","@json"],"complexity":"O(M+N)","name":"JSON.SET"},{"acl_categories":["@read","@json"],"complexity":"O(N)","name":"JSON.GET"}],"description":"Numeric functions: Use abs(), ceiling(), and floor() to transform a number before comparing it in a filter","difficulty":"advanced","id":"func_math","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_json_path_ops-stepfunc_math"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_json_path_ops-stepfunc_math"},{"id":"Node-js","panelId":"panel_Nodejs_json_path_ops-stepfunc_math"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_json_path_ops-stepfunc_math"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_json_path_ops-stepfunc_math"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_json_path_ops-stepfunc_math"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_json_path_ops-stepfunc_math"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_json_path_ops-stepfunc_math"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_json_path_ops-stepfunc_math"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_json_path_ops-stepfunc_math"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_json_path_ops-stepfunc_math"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_json_path_ops-stepfunc_math"}]},{"codetabsId":"json_path_ops-stepfunc_array_access","commands":[{"acl_categories":["@write","@json"],"complexity":"O(M+N)","name":"JSON.SET"},{"acl_categories":["@read","@json"],"complexity":"O(N)","name":"JSON.GET"}],"description":"Array access functions: Use first(), last(), and index() to pick a single element out of an array before comparing it","difficulty":"advanced","id":"func_array_access","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_json_path_ops-stepfunc_array_access"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_json_path_ops-stepfunc_array_access"},{"id":"Node-js","panelId":"panel_Nodejs_json_path_ops-stepfunc_array_access"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_json_path_ops-stepfunc_array_access"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_json_path_ops-stepfunc_array_access"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_json_path_ops-stepfunc_array_access"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_json_path_ops-stepfunc_array_access"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_json_path_ops-stepfunc_array_access"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_json_path_ops-stepfunc_array_access"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_json_path_ops-stepfunc_array_access"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_json_path_ops-stepfunc_array_access"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_json_path_ops-stepfunc_array_access"}]},{"codetabsId":"json_path_ops-stepfunc_aggregate","commands":[{"acl_categories":["@write","@json"],"complexity":"O(M+N)","name":"JSON.SET"},{"acl_categories":["@read","@json"],"complexity":"O(N)","name":"JSON.GET"}],"description":"Aggregation functions: Use sum(), avg(), min(), max(), or stddev() to reduce an array of numbers to a single value in a filter","difficulty":"advanced","id":"func_aggregate","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_json_path_ops-stepfunc_aggregate"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_json_path_ops-stepfunc_aggregate"},{"id":"Node-js","panelId":"panel_Nodejs_json_path_ops-stepfunc_aggregate"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_json_path_ops-stepfunc_aggregate"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_json_path_ops-stepfunc_aggregate"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_json_path_ops-stepfunc_aggregate"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_json_path_ops-stepfunc_aggregate"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_json_path_ops-stepfunc_aggregate"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_json_path_ops-stepfunc_aggregate"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_json_path_ops-stepfunc_aggregate"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_json_path_ops-stepfunc_aggregate"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_json_path_ops-stepfunc_aggregate"}]},{"codetabsId":"json_path_ops-stepfunc_append","commands":[{"acl_categories":["@write","@json"],"complexity":"O(M+N)","name":"JSON.SET"},{"acl_categories":["@read","@json"],"complexity":"O(N)","name":"JSON.GET"}],"description":"Append function: Use append() as a read-only, query-time projection that adds a value after an array\u0026amp;#39;s elements without modifying the stored document","difficulty":"advanced","id":"func_append","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_json_path_ops-stepfunc_append"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_json_path_ops-stepfunc_append"},{"id":"Node-js","panelId":"panel_Nodejs_json_path_ops-stepfunc_append"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_json_path_ops-stepfunc_append"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_json_path_ops-stepfunc_append"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_json_path_ops-stepfunc_append"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_json_path_ops-stepfunc_append"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_json_path_ops-stepfunc_append"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_json_path_ops-stepfunc_append"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_json_path_ops-stepfunc_append"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_json_path_ops-stepfunc_append"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_json_path_ops-stepfunc_append"}]},{"buildsUpon":["get_bikes"],"codetabsId":"json_tutorial-stepupdate_bikes","commands":[{"acl_categories":["@read","@json"],"complexity":"O(N)","name":"JSON.GET"},{"acl_categories":["@write","@json"],"complexity":"O(1)","name":"JSON.NUMINCRBY"}],"description":"Bulk updates: Use JSONPath with JSON.NUMINCRBY to update multiple numeric values across the document when you need to apply arithmetic operations to multiple fields","difficulty":"intermediate","id":"update_bikes","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_json_tutorial-stepupdate_bikes"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_json_tutorial-stepupdate_bikes"},{"id":"Node-js","panelId":"panel_Nodejs_json_tutorial-stepupdate_bikes"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_json_tutorial-stepupdate_bikes"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_json_tutorial-stepupdate_bikes"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_json_tutorial-stepupdate_bikes"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_json_tutorial-stepupdate_bikes"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_json_tutorial-stepupdate_bikes"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_json_tutorial-stepupdate_bikes"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_json_tutorial-stepupdate_bikes"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_json_tutorial-stepupdate_bikes"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_json_tutorial-stepupdate_bikes"}]},{"buildsUpon":["filter1"],"codetabsId":"json_tutorial-stepupdate_filters1","commands":[{"acl_categories":["@write","@json"],"complexity":"O(M+N)","name":"JSON.SET"},{"acl_categories":["@read","@json"],"complexity":"O(N)","name":"JSON.GET"}],"description":"Conditional updates: Use filter expressions with JSON.SET to update only elements matching specific conditions when you need selective modifications","difficulty":"advanced","id":"update_filters1","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_json_tutorial-stepupdate_filters1"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_json_tutorial-stepupdate_filters1"},{"id":"Node-js","panelId":"panel_Nodejs_json_tutorial-stepupdate_filters1"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_json_tutorial-stepupdate_filters1"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_json_tutorial-stepupdate_filters1"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_json_tutorial-stepupdate_filters1"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_json_tutorial-stepupdate_filters1"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_json_tutorial-stepupdate_filters1"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_json_tutorial-stepupdate_filters1"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_json_tutorial-stepupdate_filters1"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_json_tutorial-stepupdate_filters1"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_json_tutorial-stepupdate_filters1"}]},{"buildsUpon":["update_filters1"],"codetabsId":"json_tutorial-stepupdate_filters2","commands":[{"acl_categories":["@write","@json"],"complexity":"O(1)","name":"JSON.ARRAPPEND"},{"acl_categories":["@read","@json"],"complexity":"O(N)","name":"JSON.GET"}],"description":"Array updates with filters: Use JSON.ARRAPPEND with filter expressions to add elements to arrays matching conditions when you need to modify collections selectively","difficulty":"advanced","id":"update_filters2","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_json_tutorial-stepupdate_filters2"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_json_tutorial-stepupdate_filters2"},{"id":"Node-js","panelId":"panel_Nodejs_json_tutorial-stepupdate_filters2"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_json_tutorial-stepupdate_filters2"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_json_tutorial-stepupdate_filters2"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_json_tutorial-stepupdate_filters2"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_json_tutorial-stepupdate_filters2"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_json_tutorial-stepupdate_filters2"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_json_tutorial-stepupdate_filters2"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_json_tutorial-stepupdate_filters2"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_json_tutorial-stepupdate_filters2"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_json_tutorial-stepupdate_filters2"}]},{"codetabsId":"json_path_ops-stepproj_basic","commands":[{"acl_categories":["@write","@json"],"complexity":"O(M+N)","name":"JSON.SET"},{"acl_categories":["@read","@json"],"complexity":"O(N)","name":"JSON.GET"}],"description":"Projection expressions: Use arithmetic, a function call, or the length of a path as a top-level query that computes a value instead of only selecting nodes","difficulty":"advanced","id":"proj_basic","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_json_path_ops-stepproj_basic"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_json_path_ops-stepproj_basic"},{"id":"Node-js","panelId":"panel_Nodejs_json_path_ops-stepproj_basic"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_json_path_ops-stepproj_basic"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_json_path_ops-stepproj_basic"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_json_path_ops-stepproj_basic"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_json_path_ops-stepproj_basic"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_json_path_ops-stepproj_basic"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_json_path_ops-stepproj_basic"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_json_path_ops-stepproj_basic"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_json_path_ops-stepproj_basic"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_json_path_ops-stepproj_basic"}]},{"codetabsId":"json_path_ops-stepproj_multipath","commands":[{"acl_categories":["@read","@json"],"complexity":"O(N)","name":"JSON.GET"}],"description":"Multi-path queries: Pass more than one path to JSON.GET to have each path\u0026amp;#39;s result returned under its own key in a single reply","difficulty":"advanced","id":"proj_multipath","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_json_path_ops-stepproj_multipath"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_json_path_ops-stepproj_multipath"},{"id":"Node-js","panelId":"panel_Nodejs_json_path_ops-stepproj_multipath"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_json_path_ops-stepproj_multipath"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_json_path_ops-stepproj_multipath"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_json_path_ops-stepproj_multipath"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_json_path_ops-stepproj_multipath"},{"id":"dotnet-Sync (NRedisStack)","panelId":"panel_Csharp-Sync (NRedisStack)_json_path_ops-stepproj_multipath"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_json_path_ops-stepproj_multipath"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_json_path_ops-stepproj_multipath"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_json_path_ops-stepproj_multipath"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_json_path_ops-stepproj_multipath"}]}]
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


Paths let you access specific elements within a JSON document. Since no standard for JSON path syntax exists, Redis JSON implements its own. JSON's syntax is based on common best practices and intentionally resembles [JSONPath](http://goessner.net/articles/JsonPath/).

JSON supports two query syntaxes: [JSONPath syntax](#jsonpath-syntax) and the [legacy path syntax](#legacy-path-syntax) from the first version of JSON.

JSON knows which syntax to use depending on the first character of the path query. If the query starts with the character `$`, it uses JSONPath syntax. Otherwise, it defaults to the legacy path syntax.

The returned value is a JSON string with a top-level array of JSON serialized strings. 
And if multi-paths are used, the return value is a JSON string with a top-level object with values that are arrays of serialized JSON values.

## JSONPath support

RedisJSON v2.0 introduced [JSONPath](http://goessner.net/articles/JsonPath/) support. It follows the syntax described by Goessner in his [article](http://goessner.net/articles/JsonPath/).

A JSONPath query can resolve to several locations in a JSON document. In this case, the JSON commands apply the operation to every possible location. This is a major improvement over [legacy path](#legacy-path-syntax) queries, which only operate on the first path.

Notice that the structure of the command response often differs when using JSONPath. See the [Commands](/commands/?group=json) page for more details.

The new syntax supports bracket notation, which allows the use of special characters like colon ":" or whitespace in key names.

If you want to include double quotes in a query from the CLI, enclose the JSONPath within single quotes. For example:

```bash
JSON.GET store '$.inventory["mountain_bikes"]'
```


## JSONPath syntax

The following JSONPath syntax table was adapted from Goessner's [path syntax comparison](https://goessner.net/articles/JsonPath/index.html#e2).

| Syntax&nbsp;element | Description |
|----------------|-------------|
| $ | The root (outermost JSON element), starts the path. |
| . or [] | Selects a child element. |
| .. | Recursively descends through the JSON document. |
| * | Wildcard, returns all elements. |
| [] | Subscript operator, accesses an array element. |
| [,] | Union, selects multiple elements. |
| [start\:end\:step] | Array slice where *start*, *end*, and *step* are index values. You can omit values from the slice (for example, `[3:]`, `[:8:2]`) to use the default values: *start* defaults to the first index, *end* defaults to the last index, and *step* defaults to `1`. Use `[*]` or `[:]` to select all elements. |
| ?() | Filters a JSON object or array. Supports comparison operators <nobr>(`==`, `!=`, `<`, `<=`, `>`, `>=`, `=~`)</nobr>, logical operators <nobr>(`&&`, `\|\|`, `!`)</nobr>, arithmetic operators <nobr>(`+`, `-`, `*`, `/`, `%`)</nobr>, membership operators <nobr>(`in`, `nin`)</nobr>, set-relation operators <nobr>(`subsetof`, `anyof`, `noneof`)</nobr>, the <nobr>(`size`/`sizeof`, `empty`)</nobr> operators, and parenthesis <nobr>(`(`, `)`)</nobr>. |
| () | Script expression. |
| @ | The current element, used in filter or script expressions. |
| ~ | Returns the names of an object's members as a list of strings. |

Beginning with Redis 8.10, the JSON data type supports a richer JSONPath syntax, with additional operators and functions:

- [Projection expressions](#projection-expressions) at the top level of a JSONPath query
- [`==` and `!=`](#comparing-array-and-object-literals) can now compare any literal, including array and object literals
- Filter negation operator: [`!`](#negation-)
- [`size`/`sizeof` and `empty`](#size-sizeof-and-empty) operators on string, array, object, and nodelist
- [`in` and `nin`](#membership-in-and-nin) operators: membership test on an array and nodelist
- [Operators on numbers](#arithmetic-operators): binary `-`, `+`, `*`, `/`, `%`, and unary `-` and `+`
- Operator on object: [`~`](#get-keys-operator-)
- [`length()`](#length) function on array, object, and string
- Functions on number: [`abs()`, `ceiling()`, `floor()`](#abs-ceiling-and-floor)
- Functions on string: [`match()`, `search()`](#match-and-search)
- Strings concatenation with [`concat()`](#concat)
- Functions on array: [`first()`, `last()`, `index()`](#first-last-and-index), [`append()`](#append)
- Aggregation functions on array: [`min()`, `max()`, `avg()`, `sum()`, `stddev()`](#min-max-avg-sum-and-stddev)
- Function on object: [`keys()`](#keys)
- Function on nodelist: [`count()`](#count)
- Function on nodelist with exactly one node: [`value()`](#value)
- Relations functions on array and nodelist: [`subsetof()`, `anyof()`, `noneof()`](#set-relations-subsetof-anyof-and-noneof)

These operators can be used within a filter expression (`?()`). Functions can appear inside filter expressions and, when they return a value, as top-level [projection expressions](#projection-expressions). A function can be written in prefix form, `length($.arr)`, or in postfix (method) form, `$.arr.length()`. A path segment immediately followed by `(` is a method call, so `$.arr.length()` is a function call while `$.arr.length` is a reference to a field named `length`.

> [!WARNING]
> Beginning with Redis 8.10, two changes to path parsing may affect existing queries:
>
> - To access a field whose name contains a tilde (`~`), use bracket notation, for example `$["a~b"]`. A tilde is no longer valid in a field name using dot notation.
> - The words `in`, `nin`, `subsetof`, `anyof`, `noneof`, `size`, `sizeof`, and `empty` are now reserved as operators. To access a field with one of these names, use `$.size` or `$["size"]`.

## Evaluation semantics

The following rules apply to the operators and functions described below:

- **The "Nothing" result.** Any operand that cannot be evaluated — a non-numeric arithmetic operand, division or modulo by zero, an out-of-range index, a wrong argument count, a type mismatch, or an arithmetic overflow to a non-finite value — evaluates to *Nothing*. Inside a filter, a *Nothing* result makes the surrounding condition false, so the element is skipped. As a projection, it produces an empty reply (`[]`). Evaluation never returns an error and never fails the query for these cases.
- **Number coercion.** The `==`, `!=`, `in`, `nin`, and set-relation operators treat integer and floating-point numbers with the same value as equal (for example, `1` equals `1.0`). The ordering operators (`<`, `<=`, `>`, `>=`) cannot compare against an array or object literal, so such a comparison never matches.
- **Node lists match on "any".** When an operand selects more than one node (for example, `@.*`), a comparison or operator holds if *any* selected node satisfies it.
- **Arithmetic operators must be surrounded by spaces.** `@.a + 1` is addition, but `@.a+1` is a reference to a field literally named `a+1`, because the field-name character set includes characters such as `+`, `-`, `/`, `%`, `$`, `^`, `:`, and `_`.
- **Functions are arity-checked.** Calling a function with the wrong number of arguments produces *Nothing* rather than silently using a subset of the arguments.

## JSONPath examples

The following examples use this JSON document, which stores details about items in a store's inventory:

```json
{
    "inventory": {
        "mountain_bikes": [
            {
                "id": "bike:1",
                "model": "Phoebe",
                "description": "This is a mid-travel trail slayer that is a fantastic daily driver or one bike quiver. The Shimano Claris 8-speed groupset gives plenty of gear range to tackle hills and there\u2019s room for mudguards and a rack too.  This is the bike for the rider who wants trail manners with low fuss ownership.",
                "price": 1920,
                "specs": {"material": "carbon", "weight": 13.1},
                "colors": ["black", "silver"],
            },
... output truncated for AI-facing Markdown ...
                "description": "A real joy to ride, this bike got very high scores in last years Bike of the year report. The carefully crafted 50-34 tooth chainset and 11-32 tooth cassette give an easy-on-the-legs bottom gear for climbing, and the high-quality Vittoria Zaffiro tires give balance and grip.It includes a low-step frame , our memory foam seat, bump-resistant shocks and conveniently placed thumb throttle. Put it all together and you get a bike that helps redefine what can be done for this price.",
                "price": 3941,
                "specs": {"material": "alloy", "weight": 11.6},
            },
        ],
    }
}
```

First, create the JSON document in your database:

Setup: Create a complex JSON document with nested objects and arrays to use in JSONPath examples

**Commands:** JSON.SET

**Complexity:**
- JSON.SET: O(M+N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> JSON.SET bikes:inventory $ '{ "inventory": { "mountain_bikes": [ { "id": "bike:1", "model": "Phoebe", "description": "This is a mid-travel trail slayer that is a fantastic daily driver or one bike quiver. The Shimano Claris 8-speed groupset gives plenty of gear range to tackle hills and there\'s room for mudguards and a rack too. This is the bike for the rider who wants trail manners with low fuss ownership.", "price": 1920, "specs": {"material": "carbon", "weight": 13.1}, "colors": ["black", "silver"] }, { "id": "bike:2", "model": "Quaoar", "description": "Redesigned for the 2020 model year, this bike impressed our testers and is the best all-around trail bike we\'ve ever tested. The Shimano gear system effectively does away with an external cassette, so is super low maintenance in terms of wear and tear. All in all it\'s an impressive package for the price, making it very competitive.", "price": 2072, "specs": {"material": "aluminium", "weight": 7.9}, "colors": ["black", "white"] }, { "id": "bike:3", "model": "Weywot", "description": "This bike gives kids aged six years and older a durable and uberlight mountain bike for their first experience on tracks and easy cruising through forests and fields. A set of powerful Shimano hydraulic disc brakes provide ample stopping ability. If you\'re after a budget option, this is one of the best bikes you could get.", "price": 3264, "specs": {"material": "alloy", "weight": 13.8} } ], "commuter_bikes": [ { "id": "bike:4", "model": "Salacia", "description": "This bike is a great option for anyone who just wants a bike to get about on With a slick-shifting Claris gears from Shimano\'s, this is a bike which doesn\'t break the bank and delivers craved performance. It\'s for the rider who wants both efficiency and capability.", "price": 1475, "specs": {"material": "aluminium", "weight": 16.6}, "colors": ["black", "silver"] }, { "id": "bike:5", "model": "Mimas", "description": "A real joy to ride, this bike got very high scores in last years Bike of the year report. The carefully crafted 50-34 tooth chainset and 11-32 tooth cassette give an easy-on-the-legs bottom gear for climbing, and the high-quality Vittoria Zaffiro tires give balance and grip.It includes a low-step frame , our memory foam seat, bump-resistant shocks and conveniently placed thumb throttle. Put it all together and you get a bike that helps redefine what can be done for this price.", "price": 3941, "specs": {"material": "alloy", "weight": 11.6} } ] }}'
... output truncated for AI-facing Markdown ...
> JSON.SET bikes:inventory $ '{ "inventory": { "mountain_bikes": [ { "id": "bike:1", "model": "Phoebe", "description": "This is a mid-travel trail slayer that is a fantastic daily driver or one bike quiver. The Shimano Claris 8-speed groupset gives plenty of gear range to tackle hills and there\'s room for mudguards and a rack too. This is the bike for the rider who wants trail manners with low fuss ownership.", "price": 1920, "specs": {"material": "carbon", "weight": 13.1}, "colors": ["black", "silver"] }, { "id": "bike:2", "model": "Quaoar", "description": "Redesigned for the 2020 model year, this bike impressed our testers and is the best all-around trail bike we\'ve ever tested. The Shimano gear system effectively does away with an external cassette, so is super low maintenance in terms of wear and tear. All in all it\'s an impressive package for the price, making it very competitive.", "price": 2072, "specs": {"material": "aluminium", "weight": 7.9}, "colors": ["black", "white"] }, { "id": "bike:3", "model": "Weywot", "description": "This bike gives kids aged six years and older a durable and uberlight mountain bike for their first experience on tracks and easy cruising through forests and fields. A set of powerful Shimano hydraulic disc brakes provide ample stopping ability. If you\'re after a budget option, this is one of the best bikes you could get.", "price": 3264, "specs": {"material": "alloy", "weight": 13.8} } ], "commuter_bikes": [ { "id": "bike:4", "model": "Salacia", "description": "This bike is a great option for anyone who just wants a bike to get about on With a slick-shifting Claris gears from Shimano\'s, this is a bike which doesn\'t break the bank and delivers craved performance. It\'s for the rider who wants both efficiency and capability.", "price": 1475, "specs": {"material": "aluminium", "weight": 16.6}, "colors": ["black", "silver"] }, { "id": "bike:5", "model": "Mimas", "description": "A real joy to ride, this bike got very high scores in last years Bike of the year report. The carefully crafted 50-34 tooth chainset and 11-32 tooth cassette give an easy-on-the-legs bottom gear for climbing, and the high-quality Vittoria Zaffiro tires give balance and grip.It includes a low-step frame , our memory foam seat, bump-resistant shocks and conveniently placed thumb throttle. Put it all together and you get a bike that helps redefine what can be done for this price.", "price": 3941, "specs": {"material": "alloy", "weight": 11.6} } ] }}'
```

##### C#

```csharp
        string inventoryJson = @"
{
    ""inventory"": {
        ""mountain_bikes"": [
            {
                ""id"": ""bike:1"",
                ""model"": ""Phoebe"",
                ""description"": ""This is a mid-travel trail slayer that is a fantastic daily driver or one bike quiver. The Shimano Claris 8-speed groupset gives plenty of gear range to tackle hills and there\u2019s room for mudguards and a rack too.  This is the bike for the rider who wants trail manners with low fuss ownership."",
                ""price"": 1920,
                ""specs"": {""material"": ""carbon"", ""weight"": 13.1},
                ""colors"": [""black"", ""silver""]
            },
            {
                ""id"": ""bike:2"",
                ""model"": ""Quaoar"",
                ""description"": ""Redesigned for the 2020 model year, this bike impressed our testers and is the best all-around trail bike we've ever tested. The Shimano gear system effectively does away with an external cassette, so is super low maintenance in terms of wear and tear. All in all it's an impressive package for the price, making it very competitive."",
                ""price"": 2072,
                ""specs"": {""material"": ""aluminium"", ""weight"": 7.9},
                ""colors"": [""black"", ""white""]
            },
            {
                ""id"": ""bike:3"",
                ""model"": ""Weywot"",
                ""description"": ""This bike gives kids aged six years and older a durable and uberlight mountain bike for their first experience on tracks and easy cruising through forests and fields. A set of powerful Shimano hydraulic disc brakes provide ample stopping ability. If you're after a budget option, this is one of the best bikes you could get."",
                ""price"": 3264,
                ""specs"": {""material"": ""alloy"", ""weight"": 13.8}
            }
        ],
        ""commuter_bikes"": [
            {
                ""id"": ""bike:4"",
                ""model"": ""Salacia"",
                ""description"": ""This bike is a great option for anyone who just wants a bike to get about on With a slick-shifting Claris gears from Shimano\u2019s, this is a bike which doesn\u2019t break the bank and delivers craved performance.  It\u2019s for the rider who wants both efficiency and capability."",
                ""price"": 1475,
                ""specs"": {""material"": ""aluminium"", ""weight"": 16.6},
                ""colors"": [""black"", ""silver""]
            },
            {
                ""id"": ""bike:5"",
                ""model"": ""Mimas"",
                ""description"": ""A real joy to ride, this bike got very high scores in last years Bike of the year report. The carefully crafted 50-34 tooth chainset and 11-32 tooth cassette give an easy-on-the-legs bottom gear for climbing, and the high-quality Vittoria Zaffiro tires give balance and grip.It includes a low-step frame , our memory foam seat, bump-resistant shocks and conveniently placed thumb throttle. Put it all together and you get a bike that helps redefine what can be done for this price."",
                ""price"": 3941,
                ""specs"": {""material"": ""alloy"", ""weight"": 11.6}
            }
        ]
    }
}";

        bool res28 = db.JSON().Set("bikes:inventory", "$", inventoryJson);
        Console.WriteLine(res28);   // >>> True
```

##### Go

```go
	var inventory_json = map[string]interface{}{
		"inventory": map[string]interface{}{
			"mountain_bikes": []interface{}{
				map[string]interface{}{
					"id":    "bike:1",
					"model": "Phoebe",
					"description": "This is a mid-travel trail slayer that is a fantastic " +
						"daily driver or one bike quiver. The Shimano Claris 8-speed groupset " +
						"gives plenty of gear range to tackle hills and there\u2019s room for " +
						"mudguards and a rack too.  This is the bike for the rider who wants " +
						"trail manners with low fuss ownership.",
					"price":  1920,
					"specs":  map[string]interface{}{"material": "carbon", "weight": 13.1},
					"colors": []interface{}{"black", "silver"},
				},
				map[string]interface{}{
					"id":    "bike:2",
					"model": "Quaoar",
					"description": "Redesigned for the 2020 model year, this bike " +
						"impressed our testers and is the best all-around trail bike we've " +
						"ever tested. The Shimano gear system effectively does away with an " +
						"external cassette, so is super low maintenance in terms of wear " +
						"and tear. All in all it's an impressive package for the price, " +
						"making it very competitive.",
					"price":  2072,
					"specs":  map[string]interface{}{"material": "aluminium", "weight": 7.9},
					"colors": []interface{}{"black", "white"},
				},
				map[string]interface{}{
					"id":    "bike:3",
					"model": "Weywot",
					"description": "This bike gives kids aged six years and older " +
						"a durable and uberlight mountain bike for their first experience " +
						"on tracks and easy cruising through forests and fields. A set of " +
						"powerful Shimano hydraulic disc brakes provide ample stopping " +
						"ability. If you're after a budget option, this is one of the best " +
						"bikes you could get.",
					"price": 3264,
					"specs": map[string]interface{}{"material": "alloy", "weight": 13.8},
				},
			},
			"commuter_bikes": []interface{}{
				map[string]interface{}{
					"id":    "bike:4",
					"model": "Salacia",
					"description": "This bike is a great option for anyone who just " +
						"wants a bike to get about on With a slick-shifting Claris gears " +
						"from Shimano\u2019s, this is a bike which doesn\u2019t break the " +
						"bank and delivers craved performance.  It\u2019s for the rider " +
						"who wants both efficiency and capability.",
					"price":  1475,
					"specs":  map[string]interface{}{"material": "aluminium", "weight": 16.6},
					"colors": []interface{}{"black", "silver"},
				},
				map[string]interface{}{
					"id":    "bike:5",
					"model": "Mimas",
					"description": "A real joy to ride, this bike got very high " +
						"scores in last years Bike of the year report. The carefully " +
						"crafted 50-34 tooth chainset and 11-32 tooth cassette give an " +
						"easy-on-the-legs bottom gear for climbing, and the high-quality " +
						"Vittoria Zaffiro tires give balance and grip.It includes " +
						"a low-step frame , our memory foam seat, bump-resistant shocks and " +
						"conveniently placed thumb throttle. Put it all together and you " +
						"get a bike that helps redefine what can be done for this price.",
					"price": 3941,
					"specs": map[string]interface{}{"material": "alloy", "weight": 11.6},
				},
			},
		},
	}

	res1, err := rdb.JSONSet(ctx, "bikes:inventory", "$", inventory_json).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // >>> OK
```

##### Java (Asynchronous - Lettuce)

```java
            String inventory_json_str = "{" + "    \"inventory\": {" + "        \"mountain_bikes\": [" + "            {"
                    + "                \"id\": \"bike:1\"," + "                \"model\": \"Phoebe\","
                    + "                \"description\": \"This is a mid-travel trail slayer that is a "
                    + "fantastic daily driver or one bike quiver. The Shimano Claris 8-speed groupset "
                    + "gives plenty of gear range to tackle hills and there\u2019s room for mudguards "
                    + "and a rack too.  This is the bike for the rider who wants trail manners with " + "low fuss ownership.\","
                    + "                \"price\": 1920,"
                    + "                \"specs\": {\"material\": \"carbon\", \"weight\": 13.1},"
                    + "                \"colors\": [\"black\", \"silver\"]" + "            }," + "            {"
                    + "                \"id\": \"bike:2\"," + "                \"model\": \"Quaoar\","
                    + "                \"description\": \"Redesigned for the 2020 model year, this "
                    + "bike impressed our testers and is the best all-around trail bike we've ever "
                    + "tested. The Shimano gear system effectively does away with an external cassette, "
                    + "so is super low maintenance in terms of wear and tear. All in all it's an "
                    + "impressive package for the price, making it very competitive.\"," + "                \"price\": 2072,"
                    + "                \"specs\": {\"material\": \"aluminium\", \"weight\": 7.9},"
                    + "                \"colors\": [\"black\", \"white\"]" + "            }," + "            {"
                    + "                \"id\": \"bike:3\"," + "                \"model\": \"Weywot\","
                    + "                \"description\": \"This bike gives kids aged six years and older "
                    + "a durable and uberlight mountain bike for their first experience on tracks and easy "
                    + "cruising through forests and fields. A set of powerful Shimano hydraulic disc brakes "
                    + "provide ample stopping ability. If you're after a budget option, this is one of the "
                    + "best bikes you could get.\"," + "                \"price\": 3264,"
                    + "                \"specs\": {\"material\": \"alloy\", \"weight\": 13.8}" + "            }" + "        ],"
                    + "        \"commuter_bikes\": [" + "            {" + "                \"id\": \"bike:4\","
                    + "                \"model\": \"Salacia\","
                    + "                \"description\": \"This bike is a great option for anyone who just "
                    + "wants a bike to get about on With a slick-shifting Claris gears from Shimano\u2019s, "
                    + "this is a bike which doesn\u2019t break the bank and delivers craved performance.  "
                    + "It\u2019s for the rider who wants both efficiency and capability.\","
                    + "                \"price\": 1475,"
                    + "                \"specs\": {\"material\": \"aluminium\", \"weight\": 16.6},"
                    + "                \"colors\": [\"black\", \"silver\"]" + "            }," + "            {"
                    + "                \"id\": \"bike:5\"," + "                \"model\": \"Mimas\","
                    + "                \"description\": \"A real joy to ride, this bike got very high scores "
                    + "in last years Bike of the year report. The carefully crafted 50-34 tooth chainset "
                    + "and 11-32 tooth cassette give an easy-on-the-legs bottom gear for climbing, and the "
                    + "high-quality Vittoria Zaffiro tires give balance and grip.It includes a low-step "
                    + "frame , our memory foam seat, bump-resistant shocks and conveniently placed thumb "
                    + "throttle. Put it all together and you get a bike that helps redefine what can be "
                    + "done for this price.\"," + "                \"price\": 3941,"
                    + "                \"specs\": {\"material\": \"alloy\", \"weight\": 11.6}" + "            }" + "        ]"
                    + "    }" + "}";

            Charset charset = Charset.forName("UTF-8");
            ByteBuffer inventory_json = charset.encode(inventory_json_str);

            CompletableFuture<Void> setBikes = asyncCommands
                    .jsonSet("bikes:inventory", JsonPath.ROOT_PATH, parser.loadJsonValue(inventory_json))
                    .thenAccept(System.out::println) // >>> OK
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            String inventory_json_str = "{" + "    \"inventory\": {" + "        \"mountain_bikes\": [" + "            {"
                    + "                \"id\": \"bike:1\"," + "                \"model\": \"Phoebe\","
                    + "                \"description\": \"This is a mid-travel trail slayer that is a "
                    + "fantastic daily driver or one bike quiver. The Shimano Claris 8-speed groupset "
                    + "gives plenty of gear range to tackle hills and there\u2019s room for mudguards "
                    + "and a rack too.  This is the bike for the rider who wants trail manners with " + "low fuss ownership.\","
                    + "                \"price\": 1920,"
                    + "                \"specs\": {\"material\": \"carbon\", \"weight\": 13.1},"
                    + "                \"colors\": [\"black\", \"silver\"]" + "            }," + "            {"
                    + "                \"id\": \"bike:2\"," + "                \"model\": \"Quaoar\","
                    + "                \"description\": \"Redesigned for the 2020 model year, this "
                    + "bike impressed our testers and is the best all-around trail bike we've ever "
                    + "tested. The Shimano gear system effectively does away with an external cassette, "
                    + "so is super low maintenance in terms of wear and tear. All in all it's an "
                    + "impressive package for the price, making it very competitive.\"," + "                \"price\": 2072,"
                    + "                \"specs\": {\"material\": \"aluminium\", \"weight\": 7.9},"
                    + "                \"colors\": [\"black\", \"white\"]" + "            }," + "            {"
                    + "                \"id\": \"bike:3\"," + "                \"model\": \"Weywot\","
                    + "                \"description\": \"This bike gives kids aged six years and older "
                    + "a durable and uberlight mountain bike for their first experience on tracks and easy "
                    + "cruising through forests and fields. A set of powerful Shimano hydraulic disc brakes "
                    + "provide ample stopping ability. If you're after a budget option, this is one of the "
                    + "best bikes you could get.\"," + "                \"price\": 3264,"
                    + "                \"specs\": {\"material\": \"alloy\", \"weight\": 13.8}" + "            }" + "        ],"
                    + "        \"commuter_bikes\": [" + "            {" + "                \"id\": \"bike:4\","
                    + "                \"model\": \"Salacia\","
                    + "                \"description\": \"This bike is a great option for anyone who just "
                    + "wants a bike to get about on With a slick-shifting Claris gears from Shimano\u2019s, "
                    + "this is a bike which doesn\u2019t break the bank and delivers craved performance.  "
                    + "It\u2019s for the rider who wants both efficiency and capability.\","
                    + "                \"price\": 1475,"
                    + "                \"specs\": {\"material\": \"aluminium\", \"weight\": 16.6},"
                    + "                \"colors\": [\"black\", \"silver\"]" + "            }," + "            {"
                    + "                \"id\": \"bike:5\"," + "                \"model\": \"Mimas\","
                    + "                \"description\": \"A real joy to ride, this bike got very high scores "
                    + "in last years Bike of the year report. The carefully crafted 50-34 tooth chainset "
                    + "and 11-32 tooth cassette give an easy-on-the-legs bottom gear for climbing, and the "
                    + "high-quality Vittoria Zaffiro tires give balance and grip.It includes a low-step "
                    + "frame , our memory foam seat, bump-resistant shocks and conveniently placed thumb "
                    + "throttle. Put it all together and you get a bike that helps redefine what can be "
                    + "done for this price.\"," + "                \"price\": 3941,"
                    + "                \"specs\": {\"material\": \"alloy\", \"weight\": 11.6}" + "            }" + "        ]"
                    + "    }" + "}";

            Charset charset = Charset.forName("UTF-8");
            ByteBuffer inventory_json = charset.encode(inventory_json_str);

            Mono<Void> setBikes = reactiveCommands
                    .jsonSet("bikes:inventory", JsonPath.ROOT_PATH, parser.loadJsonValue(inventory_json))
                    .doOnNext(System.out::println) // >>> OK
                    .then();
```

##### Java (Synchronous - Jedis)

```java
        String inventory_json = "{"
        + "    \"inventory\": {"
        + "        \"mountain_bikes\": ["
        + "            {"
        + "                \"id\": \"bike:1\","
        + "                \"model\": \"Phoebe\","
        + "                \"description\": \"This is a mid-travel trail slayer that is a "
        + "fantastic daily driver or one bike quiver. The Shimano Claris 8-speed groupset "
        + "gives plenty of gear range to tackle hills and there\u2019s room for mudguards "
        + "and a rack too.  This is the bike for the rider who wants trail manners with "
        + "low fuss ownership.\","
        + "                \"price\": 1920,"
        + "                \"specs\": {\"material\": \"carbon\", \"weight\": 13.1},"
        + "                \"colors\": [\"black\", \"silver\"]"
        + "            },"
        + "            {"
        + "                \"id\": \"bike:2\","
        + "                \"model\": \"Quaoar\","
        + "                \"description\": \"Redesigned for the 2020 model year, this "
        + "bike impressed our testers and is the best all-around trail bike we've ever "
        + "tested. The Shimano gear system effectively does away with an external cassette, "
        + "so is super low maintenance in terms of wear and tear. All in all it's an "
        + "impressive package for the price, making it very competitive.\","
        + "                \"price\": 2072,"
        + "                \"specs\": {\"material\": \"aluminium\", \"weight\": 7.9},"
        + "                \"colors\": [\"black\", \"white\"]"
        + "            },"
        + "            {"
        + "                \"id\": \"bike:3\","
        + "                \"model\": \"Weywot\","
        + "                \"description\": \"This bike gives kids aged six years and older "
        + "a durable and uberlight mountain bike for their first experience on tracks and easy "
        + "cruising through forests and fields. A set of powerful Shimano hydraulic disc brakes "
        + "provide ample stopping ability. If you're after a budget option, this is one of the "
        + "best bikes you could get.\","
        + "                \"price\": 3264,"
        + "                \"specs\": {\"material\": \"alloy\", \"weight\": 13.8}"
        + "            }"
        + "        ],"
        + "        \"commuter_bikes\": ["
        + "            {"
        + "                \"id\": \"bike:4\","
        + "                \"model\": \"Salacia\","
        + "                \"description\": \"This bike is a great option for anyone who just "
        + "wants a bike to get about on With a slick-shifting Claris gears from Shimano\u2019s, "
        + "this is a bike which doesn\u2019t break the bank and delivers craved performance.  "
        + "It\u2019s for the rider who wants both efficiency and capability.\","
        + "                \"price\": 1475,"
        + "                \"specs\": {\"material\": \"aluminium\", \"weight\": 16.6},"
        + "                \"colors\": [\"black\", \"silver\"]"
        + "            },"
        + "            {"
        + "                \"id\": \"bike:5\","
        + "                \"model\": \"Mimas\","
        + "                \"description\": \"A real joy to ride, this bike got very high scores "
        + "in last years Bike of the year report. The carefully crafted 50-34 tooth chainset "
        + "and 11-32 tooth cassette give an easy-on-the-legs bottom gear for climbing, and the "
        + "high-quality Vittoria Zaffiro tires give balance and grip.It includes a low-step "
        + "frame , our memory foam seat, bump-resistant shocks and conveniently placed thumb "
        + "throttle. Put it all together and you get a bike that helps redefine what can be "
        + "done for this price.\","
        + "                \"price\": 3941,"
        + "                \"specs\": {\"material\": \"alloy\", \"weight\": 11.6}"
        + "            }"
        + "        ]"
        + "    }"
        + "}";

        String res28 = jedis.jsonSet("bikes:inventory", new Path2("$"), inventory_json);
        System.out.println(res28);  // >>> OK
```

##### JavaScript (Node.js)

```javascript
const inventoryJSON = {
  "inventory": {
    "mountain_bikes": [{
        "id": "bike:1",
        "model": "Phoebe",
        "description": "This is a mid-travel trail slayer that is a fantastic daily driver or one bike quiver. The Shimano Claris 8-speed groupset gives plenty of gear range to tackle hills and there\u2019s room for mudguards and a rack too.  This is the bike for the rider who wants trail manners with low fuss ownership.",
        "price": 1920,
        "specs": {
          "material": "carbon",
          "weight": 13.1
        },
        "colors": ["black", "silver"],
      },
      {
        "id": "bike:2",
        "model": "Quaoar",
        "description": "Redesigned for the 2020 model year, this bike impressed our testers and is the best all-around trail bike we've ever tested. The Shimano gear system effectively does away with an external cassette, so is super low maintenance in terms of wear and teaawait client. All in all it's an impressive package for the price, making it very competitive.",
        "price": 2072,
        "specs": {
          "material": "aluminium",
          "weight": 7.9
        },
        "colors": ["black", "white"],
      },
      {
        "id": "bike:3",
        "model": "Weywot",
        "description": "This bike gives kids aged six years and older a durable and uberlight mountain bike for their first experience on tracks and easy cruising through forests and fields. A set of powerful Shimano hydraulic disc brakes provide ample stopping ability. If you're after a budget option, this is one of the best bikes you could get.",
        "price": 3264,
        "specs": {
          "material": "alloy",
          "weight": 13.8
        },
      },
    ],
    "commuter_bikes": [{
        "id": "bike:4",
        "model": "Salacia",
        "description": "This bike is a great option for anyone who just wants a bike to get about on With a slick-shifting Claris gears from Shimano\u2019s, this is a bike which doesn\u2019t break the bank and delivers craved performance.  It\u2019s for the rider who wants both efficiency and capability.",
        "price": 1475,
        "specs": {
          "material": "aluminium",
          "weight": 16.6
        },
        "colors": ["black", "silver"],
      },
      {
        "id": "bike:5",
        "model": "Mimas",
        "description": "A real joy to ride, this bike got very high scores in last years Bike of the year report. The carefully crafted 50-34 tooth chainset and 11-32 tooth cassette give an easy-on-the-legs bottom gear for climbing, and the high-quality Vittoria Zaffiro tires give balance and grip.It includes a low-step frame , our memory foam seat, bump-resistant shocks and conveniently placed thumb throttle. Put it all together and you get a bike that helps redefine what can be done for this price.",
        "price": 3941,
        "specs": {
          "material": "alloy",
          "weight": 11.6
        },
      },
    ],
  }
};

const res28 = await client.json.set("bikes:inventory", "$", inventoryJSON);
console.log(res28); //  OK
```

##### PHP

```php
        $inventory = [
            'inventory' => [
                'mountain_bikes' => [
                    [
                        'id' => 'bike:1',
                        'model' => 'Phoebe',
                        'description' => 'This is a mid-travel trail slayer that is a fantastic daily driver or one bike quiver. The Shimano Claris 8-speed groupset gives plenty of gear range to tackle hills and there’s room for mudguards and a rack too.  This is the bike for the rider who wants trail manners with low fuss ownership.',
                        'price' => 1920,
                        'specs' => ['material' => 'carbon', 'weight' => 13.1],
                        'colors' => ['black', 'silver'],
                    ],
                    [
                        'id' => 'bike:2',
                        'model' => 'Quaoar',
                        'description' => "Redesigned for the 2020 model year, this bike impressed our testers and is the best all-around trail bike we've ever tested. The Shimano gear system effectively does away with an external cassette, so is super low maintenance in terms of wear and tear. All in all it's an impressive package for the price, making it very competitive.",
                        'price' => 2072,
                        'specs' => ['material' => 'aluminium', 'weight' => 7.9],
                        'colors' => ['black', 'white'],
                    ],
                    [
                        'id' => 'bike:3',
                        'model' => 'Weywot',
                        'description' => 'This bike gives kids aged six years and older a durable and uberlight mountain bike for their first experience on tracks and easy cruising through forests and fields. A set of powerful Shimano hydraulic disc brakes provide ample stopping ability. If you\'re after a budget option, this is one of the best bikes you could get.',
                        'price' => 3264,
                        'specs' => ['material' => 'alloy', 'weight' => 13.8],
                    ],
                ],
                'commuter_bikes' => [
                    [
                        'id' => 'bike:4',
                        'model' => 'Salacia',
                        'description' => 'This bike is a great option for anyone who just wants a bike to get about on With a slick-shifting Claris gears from Shimano’s, this is a bike which doesn’t break the bank and delivers craved performance.  It’s for the rider who wants both efficiency and capability.',
                        'price' => 1475,
                        'specs' => ['material' => 'aluminium', 'weight' => 16.6],
                        'colors' => ['black', 'silver'],
                    ],
                    [
                        'id' => 'bike:5',
                        'model' => 'Mimas',
                        'description' => 'A real joy to ride, this bike got very high scores in last years Bike of the year report. The carefully crafted 50-34 tooth chainset and 11-32 tooth cassette give an easy-on-the-legs bottom gear for climbing, and the high-quality Vittoria Zaffiro tires give balance and grip.It includes a low-step frame , our memory foam seat, bump-resistant shocks and conveniently placed thumb throttle. Put it all together and you get a bike that helps redefine what can be done for this price.',
                        'price' => 3941,
                        'specs' => ['material' => 'alloy', 'weight' => 11.6],
                    ],
                ],
            ],
        ];
        $res1b = $r->jsonset('bikes:inventory', '$', json_encode($inventory, JSON_THROW_ON_ERROR));
        echo $res1b . PHP_EOL;
        // >>> OK
```

##### Python

```python
inventory_json = {
    "inventory": {
        "mountain_bikes": [
            {
                "id": "bike:1",
                "model": "Phoebe",
                "description": "This is a mid-travel trail slayer that is a fantastic "
                "daily driver or one bike quiver. The Shimano Claris 8-speed groupset "
                "gives plenty of gear range to tackle hills and there\u2019s room for "
                "mudguards and a rack too.  This is the bike for the rider who wants "
                "trail manners with low fuss ownership.",
                "price": 1920,
                "specs": {"material": "carbon", "weight": 13.1},
                "colors": ["black", "silver"],
            },
            {
                "id": "bike:2",
                "model": "Quaoar",
                "description": "Redesigned for the 2020 model year, this bike "
                "impressed our testers and is the best all-around trail bike we've "
                "ever tested. The Shimano gear system effectively does away with an "
                "external cassette, so is super low maintenance in terms of wear "
                "and tear. All in all it's an impressive package for the price, "
                "making it very competitive.",
                "price": 2072,
                "specs": {"material": "aluminium", "weight": 7.9},
                "colors": ["black", "white"],
            },
            {
                "id": "bike:3",
                "model": "Weywot",
                "description": "This bike gives kids aged six years and older "
                "a durable and uberlight mountain bike for their first experience "
                "on tracks and easy cruising through forests and fields. A set of "
                "powerful Shimano hydraulic disc brakes provide ample stopping "
                "ability. If you're after a budget option, this is one of the best "
                "bikes you could get.",
                "price": 3264,
                "specs": {"material": "alloy", "weight": 13.8},
            },
        ],
        "commuter_bikes": [
            {
                "id": "bike:4",
                "model": "Salacia",
                "description": "This bike is a great option for anyone who just "
                "wants a bike to get about on With a slick-shifting Claris gears "
                "from Shimano\u2019s, this is a bike which doesn\u2019t break the "
                "bank and delivers craved performance.  It\u2019s for the rider "
                "who wants both efficiency and capability.",
                "price": 1475,
                "specs": {"material": "aluminium", "weight": 16.6},
                "colors": ["black", "silver"],
            },
            {
                "id": "bike:5",
                "model": "Mimas",
                "description": "A real joy to ride, this bike got very high "
                "scores in last years Bike of the year report. The carefully "
                "crafted 50-34 tooth chainset and 11-32 tooth cassette give an "
                "easy-on-the-legs bottom gear for climbing, and the high-quality "
                "Vittoria Zaffiro tires give balance and grip.It includes "
                "a low-step frame , our memory foam seat, bump-resistant shocks and "
                "conveniently placed thumb throttle. Put it all together and you "
                "get a bike that helps redefine what can be done for this price.",
                "price": 3941,
                "specs": {"material": "alloy", "weight": 11.6},
            },
        ],
    }
}

res1 = r.json().set("bikes:inventory", "$", inventory_json)
print(res1)  # >>> True
```

##### Ruby

```ruby
inventory_json = {
  'inventory' => {
    'mountain_bikes' => [
      {
        'id' => 'bike:1',
        'model' => 'Phoebe',
        'description' => 'This is a mid-travel trail slayer that is a fantastic ' \
          'daily driver or one bike quiver. The Shimano Claris 8-speed groupset ' \
          'gives plenty of gear range to tackle hills and there’s room for ' \
          'mudguards and a rack too.  This is the bike for the rider who wants ' \
          'trail manners with low fuss ownership.',
        'price' => 1920,
        'specs' => { 'material' => 'carbon', 'weight' => 13.1 },
        'colors' => %w[black silver]
      },
      {
        'id' => 'bike:2',
        'model' => 'Quaoar',
        'description' => 'Redesigned for the 2020 model year, this bike ' \
          "impressed our testers and is the best all-around trail bike we've " \
          'ever tested. The Shimano gear system effectively does away with an ' \
          'external cassette, so is super low maintenance in terms of wear ' \
          "and tear. All in all it's an impressive package for the price, " \
          'making it very competitive.',
        'price' => 2072,
        'specs' => { 'material' => 'aluminium', 'weight' => 7.9 },
        'colors' => %w[black white]
      },
      {
        'id' => 'bike:3',
        'model' => 'Weywot',
        'description' => 'This bike gives kids aged six years and older ' \
          'a durable and uberlight mountain bike for their first experience ' \
          'on tracks and easy cruising through forests and fields. A set of ' \
          'powerful Shimano hydraulic disc brakes provide ample stopping ' \
          "ability. If you're after a budget option, this is one of the best " \
          'bikes you could get.',
        'price' => 3264,
        'specs' => { 'material' => 'alloy', 'weight' => 13.8 }
      }
    ],
    'commuter_bikes' => [
      {
        'id' => 'bike:4',
        'model' => 'Salacia',
        'description' => 'This bike is a great option for anyone who just ' \
          'wants a bike to get about on With a slick-shifting Claris gears ' \
          'from Shimano’s, this is a bike which doesn’t break the ' \
          "bank and delivers craved performance.  It's for the rider " \
          'who wants both efficiency and capability.',
        'price' => 1475,
        'specs' => { 'material' => 'aluminium', 'weight' => 16.6 },
        'colors' => %w[black silver]
      },
      {
        'id' => 'bike:5',
        'model' => 'Mimas',
        'description' => 'A real joy to ride, this bike got very high ' \
          'scores in last years Bike of the year report. The carefully ' \
          'crafted 50-34 tooth chainset and 11-32 tooth cassette give an ' \
          'easy-on-the-legs bottom gear for climbing, and the high-quality ' \
          'Vittoria Zaffiro tires give balance and grip.It includes ' \
          'a low-step frame , our memory foam seat, bump-resistant shocks and ' \
          'conveniently placed thumb throttle. Put it all together and you ' \
          'get a bike that helps redefine what can be done for this price.',
        'price' => 3941,
        'specs' => { 'material' => 'alloy', 'weight' => 11.6 }
      }
    ]
  }
}

res1 = r.json_set('bikes:inventory', '$', inventory_json)
puts res1 # >>> OK
```

##### Rust (Asynchronous)

```rust
        let res29: bool = r
            .json_set("bikes:inventory", "$", &inventory_json())
            .await
            .expect("Failed to run JSON.SET");
        print_set_result(res29); // >>> OK
```

##### Rust (Synchronous)

```rust
        let res29: bool = r
            .json_set("bikes:inventory", "$", &inventory_json())
            .expect("Failed to run JSON.SET");
        print_set_result(res29); // >>> OK
```



### Access examples

The following examples use the [`JSON.GET`](https://redis.io/docs/latest/commands/json.get) command to retrieve data from various paths in the JSON document.

You can use the wildcard operator `*` to return a list of all items in the inventory:

Wildcard queries: Use the * operator to retrieve all items in a collection when you need to access all elements at a specific level

**Builds upon:** set_bikes

**Commands:** JSON.GET

**Complexity:**
- JSON.GET: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> JSON.GET bikes:inventory $.inventory.*
"[[{\"id\":\"bike:1\",\"model\":\"Phoebe\",\"description\":\"This is a mid-travel trail slayer that is a fantastic daily driver or one bike quiver. The Shimano Claris 8-speed groupset gives plenty of gear range to tackle hills and there's room for mudguards and a rack too. This is the bike for the rider who wants trail manners with low fuss ownership.\",\"price\":1920,\"specs\":{\"material\":\"carbon\",\"weight\":13.1},\"colors\":[\"black\",\"silver\"]},{\"id\":\"bike:2\",\"model\":\"Quaoar\",\"description\":\"Redesigned for the 2020 model year, this bike impressed our testers and is the best all-around trail bike we've ever tested. The Shimano gear system effectively does away with an external cassette, so is super low maintenance in terms of wear and tear. All in all it's an impressive package for the price, making it very competitive.\",\"price\":2072,\"specs\":{\"material\":\"aluminium\",\"weight\":7.9},\"colors\":[\"black\",\"white\"]},{\"id\":\"bike:3\",\"model\":\"Weywot\",\"description\":\"This bike gives kids aged six years and older a durable and uberlight mountain bike for their first experience on tracks and easy cruising through forests and fields. A set of powerful Shimano hydraulic disc brakes provide ample stopping ability. If you're after a budget option, this is one of the best bikes you could get.\",\"price\":3264,\"specs\":{\"material\":\"alloy\",\"weight\":13.8}}],[{\"id\":\"bike:4\",\"model\":\"Salacia\",\"description\":\"This bike is a great option for anyone who just wants a bike to get about on With a slick-shifting Claris gears from Shimano's, this is a bike which doesn't break the bank and delivers craved performance. It's for the rider who wants both efficiency and capability.\",\"price\":1475,\"specs\":{\"material\":\"aluminium\",\"weight\":16.6},\"colors\":[\"black\",\"silver\"]},{\"id\":\"bike:5\",\"model\":\"Mimas\",\"description\":\"A real joy to ride, this bike got very high scores in last years Bike of the year report. The carefully crafted 50-34 tooth chainset and 11-32 tooth cassette give an easy-on-the-legs bottom gear for climbing, and the high-quality Vittoria Zaffiro tires give balance and grip.It includes a low-step frame , our memory foam seat, bump-resistant shocks and conveniently placed thumb throttle. Put it all together and you get a bike that helps redefine what can be done for this price.\",\"price\":3941,\"specs\":{\"material\":\"alloy\",\"weight\":11.6}}]]"
```

##### C#

```csharp
        RedisResult res29 = db.JSON().Get("bikes:inventory", path: "$.inventory.*");
        Console.WriteLine(res29);   // >>> {[[{"id":"bike:1","model":"Phoebe", ...
```

##### Go

```go
	res2, err := rdb.JSONGetWithArgs(ctx, "bikes:inventory",
		&redis.JSONGetArgs{Indent: "  ", Newline: "\n", Space: " "},
		"$.inventory.*",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2)
	// >>>
	// [
	//   [
	//     {
	//       "colors": [
	//         "black",
	//         "silver"
	// ...
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> getBikes = asyncCommands.jsonGet("bikes:inventory", JsonPath.of("$.inventory.*"))
                    .thenAccept(System.out::println)
                    // >>> [[[{"id":"bike:1","model":"Phoebe",...
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> getBikes = reactiveCommands.jsonGet("bikes:inventory", JsonPath.of("$.inventory.*")).collectList()
                    .doOnNext(System.out::println) // >>> [[[{"id":"bike:1","model":"Phoebe",...
                    .then();
```

##### Java (Synchronous - Jedis)

```java
        Object res29 = jedis.jsonGet("bikes:inventory", new Path2("$.inventory.*"));
        System.out.println(res29);
        // >>> [[{"specs":{"material":"carbon","weight":13.1},"price":1920, ...
```

##### JavaScript (Node.js)

```javascript
const res29 = await client.json.get("bikes:inventory", {
  path: "$.inventory.*"
});
console.log(res29);
/*
[
  [
    {
      id: 'bike:1',
      model: 'Phoebe',
      description: 'This is a mid-travel trail slayer that is a fantastic daily driver or one bike quiver. The Shimano Claris 8-speed groupset gives plenty of gear range to tackle hills and there’s room for mudguards and a rack too.  This is the bike for the rider who wants trail manners with low fuss ownership.',
      price: 1920,
      specs: [Object],
      colors: [Array]
    },
    {
      id: 'bike:2',
      model: 'Quaoar',
      description: "Redesigned for the 2020 model year, this bike impressed our testers and is the best all-around trail bike we've ever tested. The Shimano gear system effectively does away with an external cassette, so is super low maintenance in terms of wear and teaawait client. All in all it's an impressive package for the price, making it very competitive.",
      price: 2072,
      specs: [Object],
      colors: [Array]
    },
    {
      id: 'bike:3',
      model: 'Weywot',
      description: "This bike gives kids aged six years and older a durable and uberlight mountain bike for their first experience on tracks and easy cruising through forests and fields. A set of powerful Shimano hydraulic disc brakes provide ample stopping ability. If you're after a budget option, this is one of the best bikes you could get.",
      price: 3264,
      specs: [Object]
    }
  ],
  [
    {
      id: 'bike:4',
      model: 'Salacia',
      description: 'This bike is a great option for anyone who just wants a bike to get about on With a slick-shifting Claris gears from Shimano’s, this is a bike which doesn’t break the bank and delivers craved performance.  It’s for the rider who wants both efficiency and capability.',
      price: 1475,
      specs: [Object],
      colors: [Array]
    },
    {
      id: 'bike:5',
      model: 'Mimas',
      description: 'A real joy to ride, this bike got very high scores in last years Bike of the year report. The carefully crafted 50-34 tooth chainset and 11-32 tooth cassette give an easy-on-the-legs bottom gear for climbing, and the high-quality Vittoria Zaffiro tires give balance and grip.It includes a low-step frame , our memory foam seat, bump-resistant shocks and conveniently placed thumb throttle. Put it all together and you get a bike that helps redefine what can be done for this price.',
      price: 3941,
      specs: [Object]
    }
  ]
]
*/
```

##### PHP

```php
        $res2b = $r->jsonget('bikes:inventory', '', '', '', '$.inventory.*');
        echo $res2b . PHP_EOL;
        // >>> [{'id': 'bike:1', 'model': 'Phoebe',
```

##### Python

```python
res2 = r.json().get("bikes:inventory", "$.inventory.*")
print(res2)
# >>>    [[{'id': 'bike:1', 'model': 'Phoebe',
# >>>       'description': 'This is a mid-travel trail slayer...
```

##### Ruby

```ruby
res2 = r.json_get('bikes:inventory', '$.inventory.*')
p res2
# >>> [[{"id"=>"bike:1", "model"=>"Phoebe",
# >>>    "description"=>"This is a mid-travel trail slayer...
```

##### Rust (Asynchronous)

```rust
        let res30: String = r
            .json_get("bikes:inventory", "$.inventory.*")
            .await
            .expect("Failed to run JSON.GET");
        println!("{res30}");
        // >>> [[{"id":"bike:1","model":"Phoebe","description":"This is a mid-travel trail slayer...
```

##### Rust (Synchronous)

```rust
        let res30: String = r
            .json_get("bikes:inventory", "$.inventory.*")
            .expect("Failed to run JSON.GET");
        println!("{res30}");
        // >>> [[{"id":"bike:1","model":"Phoebe","description":"This is a mid-travel trail slayer...
```



For some queries, multiple paths can produce the same results. For example, the following paths return the names of all mountain bikes:

Array element access: Use bracket notation and array subscripts to access specific array elements or all elements with [*] when you need to retrieve values from arrays

**Difficulty:** Intermediate

**Builds upon:** get_bikes

**Commands:** JSON.GET

**Complexity:**
- JSON.GET: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> JSON.GET bikes:inventory $.inventory.mountain_bikes[*].model
"[\"Phoebe\",\"Quaoar\",\"Weywot\"]"
> JSON.GET bikes:inventory '$.inventory["mountain_bikes"][*].model'
"[\"Phoebe\",\"Quaoar\",\"Weywot\"]"
> JSON.GET bikes:inventory '$..mountain_bikes[*].model'
"[\"Phoebe\",\"Quaoar\",\"Weywot\"]"
```

##### C#

```csharp
        RedisResult res30 = db.JSON().Get("bikes:inventory", path: "$.inventory.mountain_bikes[*].model");
        Console.WriteLine(res30);   // >>> ["Phoebe","Quaoar","Weywot"]

        RedisResult res31 = db.JSON().Get("bikes:inventory", path: "$.inventory[\"mountain_bikes\"][*].model");
        Console.WriteLine(res31);   // >>> ["Phoebe","Quaoar","Weywot"]

        RedisResult res32 = db.JSON().Get("bikes:inventory", path: "$..mountain_bikes[*].model");
        Console.WriteLine(res32);   // >>> ["Phoebe","Quaoar","Weywot"]
```

##### Go

```go
	res3, err := rdb.JSONGet(ctx, "bikes:inventory",
		"$.inventory.mountain_bikes[*].model",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3)
	// >>> ["Phoebe","Quaoar","Weywot"]

	res4, err := rdb.JSONGet(ctx,
		"bikes:inventory", "$.inventory[\"mountain_bikes\"][*].model",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4)
	// >>> ["Phoebe","Quaoar","Weywot"]

	res5, err := rdb.JSONGet(ctx,
		"bikes:inventory", "$..mountain_bikes[*].model",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res5)
	// >>> ["Phoebe","Quaoar","Weywot"]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> getMtnBikes = asyncCommands
                    .jsonGet("bikes:inventory", JsonPath.of("$.inventory.mountain_bikes[*].model")).thenCompose(res19 -> {
                        System.out.println(res19); // >>> [["Phoebe","Quaoar","Weywot"]]
                        return asyncCommands.jsonGet("bikes:inventory",
                                JsonPath.of("$.inventory[\"mountain_bikes\"][*].model"));
                    }).thenCompose(res20 -> {
                        System.out.println(res20); // >>> [["Phoebe","Quaoar","Weywot"]]
                        return asyncCommands.jsonGet("bikes:inventory", JsonPath.of("$..mountain_bikes[*].model"));
                    })
                    .thenAccept(System.out::println)
                    // >>> [["Phoebe","Quaoar","Weywot"]]
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> getMtnBikes = reactiveCommands
                    .jsonGet("bikes:inventory", JsonPath.of("$.inventory.mountain_bikes[*].model")).collectList()
                    .doOnNext(res19 -> {
                        System.out.println(res19); // >>> [["Phoebe","Quaoar","Weywot"]]
                    })
                    .flatMap(res19 -> reactiveCommands
                            .jsonGet("bikes:inventory", JsonPath.of("$.inventory[\"mountain_bikes\"][*].model")).collectList())
                    .doOnNext(res20 -> {
                        System.out.println(res20); // >>> [["Phoebe","Quaoar","Weywot"]]
                    })
                    .flatMap(res20 -> reactiveCommands.jsonGet("bikes:inventory", JsonPath.of("$..mountain_bikes[*].model"))
                            .collectList())
                    .doOnNext(System.out::println) // >>> [["Phoebe","Quaoar","Weywot"]]
                    .then();
```

##### Java (Synchronous - Jedis)

```java
        Object res30 = jedis.jsonGet(
            "bikes:inventory", new Path2("$.inventory.mountain_bikes[*].model")
        );
        System.out.println(res30);  // >>> ["Phoebe","Quaoar","Weywot"]

        Object res31 = jedis.jsonGet(
            "bikes:inventory", new Path2("$.inventory[\"mountain_bikes\"][*].model")
        );
        System.out.println(res31);  // >>> ["Phoebe","Quaoar","Weywot"]

        Object res32 = jedis.jsonGet(
            "bikes:inventory", new Path2("$..mountain_bikes[*].model")
        );
        System.out.println(res32);  // >>> ["Phoebe","Quaoar","Weywot"]
```

##### JavaScript (Node.js)

```javascript
const res30 = await client.json.get("bikes:inventory", {
  path: "$.inventory.mountain_bikes[*].model"
});
console.log(res30); //  ['Phoebe', 'Quaoar', 'Weywot']

const res31 = await client.json.get("bikes:inventory", {
  path: '$.inventory["mountain_bikes"][*].model'
});
console.log(res31); //  ['Phoebe', 'Quaoar', 'Weywot']

const res32 = await client.json.get("bikes:inventory", {
  path: "$..mountain_bikes[*].model"
});
console.log(res32); //  ['Phoebe', 'Quaoar', 'Weywot']
```

##### PHP

```php
        $res3b = $r->jsonget('bikes:inventory', '', '', '', '$.inventory.mountain_bikes[*].model');
        echo $res3b . PHP_EOL;
        // >>> ["Phoebe","Quaoar","Weywot"]

        $res4b = $r->jsonget('bikes:inventory', '', '', '', '$.inventory["mountain_bikes"][*].model');
        echo $res4b . PHP_EOL;
        // >>> ["Phoebe","Quaoar","Weywot"]

        $res5b = $r->jsonget('bikes:inventory', '', '', '', '$..mountain_bikes[*].model');
        echo $res5b . PHP_EOL;
        // >>> ["Phoebe","Quaoar","Weywot"]
```

##### Python

```python
res3 = r.json().get("bikes:inventory", "$.inventory.mountain_bikes[*].model")
print(res3)  # >>> [['Phoebe', 'Quaoar', 'Weywot']]

res4 = r.json().get("bikes:inventory", '$.inventory["mountain_bikes"][*].model')
print(res4)  # >>> [['Phoebe', 'Quaoar', 'Weywot']]

res5 = r.json().get("bikes:inventory", "$..mountain_bikes[*].model")
print(res5)  # >>> [['Phoebe', 'Quaoar', 'Weywot']]
```

##### Ruby

```ruby
res3 = r.json_get('bikes:inventory', '$.inventory.mountain_bikes[*].model')
p res3 # >>> ["Phoebe", "Quaoar", "Weywot"]

res4 = r.json_get('bikes:inventory', '$.inventory["mountain_bikes"][*].model')
p res4 # >>> ["Phoebe", "Quaoar", "Weywot"]

res5 = r.json_get('bikes:inventory', '$..mountain_bikes[*].model')
p res5 # >>> ["Phoebe", "Quaoar", "Weywot"]
```

##### Rust (Asynchronous)

```rust
        let res31: String = r
            .json_get("bikes:inventory", "$.inventory.mountain_bikes[*].model")
            .await
            .expect("Failed to run JSON.GET");
        println!("{res31}"); // >>> [["Phoebe","Quaoar","Weywot"]]

        let res32: String = r
            .json_get(
                "bikes:inventory",
                r#"$.inventory["mountain_bikes"][*].model"#,
            )
            .await
            .expect("Failed to run JSON.GET");
        println!("{res32}"); // >>> [["Phoebe","Quaoar","Weywot"]]

        let res33: String = r
            .json_get("bikes:inventory", "$..mountain_bikes[*].model")
            .await
            .expect("Failed to run JSON.GET");
        println!("{res33}"); // >>> [["Phoebe","Quaoar","Weywot"]]
```

##### Rust (Synchronous)

```rust
        let res31: String = r
            .json_get("bikes:inventory", "$.inventory.mountain_bikes[*].model")
            .expect("Failed to run JSON.GET");
        println!("{res31}"); // >>> [["Phoebe","Quaoar","Weywot"]]

        let res32: String = r
            .json_get(
                "bikes:inventory",
                r#"$.inventory["mountain_bikes"][*].model"#,
            )
            .expect("Failed to run JSON.GET");
        println!("{res32}"); // >>> [["Phoebe","Quaoar","Weywot"]]

        let res33: String = r
            .json_get("bikes:inventory", "$..mountain_bikes[*].model")
            .expect("Failed to run JSON.GET");
        println!("{res33}"); // >>> [["Phoebe","Quaoar","Weywot"]]
```



The recursive descent operator `..` can retrieve a field from multiple sections of a JSON document. The following example returns the names of all inventory items:

Recursive descent: Use the .. operator to search for a field at any depth in the JSON document when you need to find values across multiple nesting levels

**Difficulty:** Intermediate

**Builds upon:** get_mtnbikes

**Commands:** JSON.GET

**Complexity:**
- JSON.GET: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> JSON.GET bikes:inventory $..model
"[\"Phoebe\",\"Quaoar\",\"Weywot\",\"Salacia\",\"Mimas\"]"
```

##### C#

```csharp
        RedisResult res33 = db.JSON().Get("bikes:inventory", path: "$..model");
        Console.WriteLine(res33);   // >>> ["Phoebe","Quaoar","Weywot","Salacia","Mimas"]
```

##### Go

```go
	res6, err := rdb.JSONGet(ctx, "bikes:inventory", "$..model").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res6) // >>> ["Salacia","Mimas","Phoebe","Quaoar","Weywot"]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> getModels = asyncCommands.jsonGet("bikes:inventory", JsonPath.of("$..model"))
                    .thenAccept(System.out::println)
                    // >>> [["Phoebe","Quaoar","Weywot","Salacia","Mimas"]]
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> getModels = reactiveCommands.jsonGet("bikes:inventory", JsonPath.of("$..model")).collectList()
                    .doOnNext(System.out::println) // >>> [["Phoebe","Quaoar","Weywot","Salacia","Mimas"]]
                    .then();
```

##### Java (Synchronous - Jedis)

```java
        Object res33 = jedis.jsonGet("bikes:inventory", new Path2("$..model"));
        System.out.println(res33);
        // >>> ["Phoebe","Quaoar","Weywot","Salacia","Mimas"]
```

##### JavaScript (Node.js)

```javascript
const res33 = await client.json.get("bikes:inventory", {
  path: "$..model"
});
console.log(res33); //  ['Phoebe', 'Quaoar', 'Weywot', 'Salacia', 'Mimas']
```

##### PHP

```php
        $res6b = $r->jsonget('bikes:inventory', '', '', '', '$..model');
        echo $res6b . PHP_EOL;
        // >>> ["Phoebe","Quaoar","Weywot","Salacia","Mimas"]
```

##### Python

```python
res6 = r.json().get("bikes:inventory", "$..model")
print(res6)  # >>> [['Phoebe', 'Quaoar', 'Weywot', 'Salacia', 'Mimas']]
```

##### Ruby

```ruby
res6 = r.json_get('bikes:inventory', '$..model')
p res6 # >>> ["Phoebe", "Quaoar", "Weywot", "Salacia", "Mimas"]
```

##### Rust (Asynchronous)

```rust
        let res34: String = r
            .json_get("bikes:inventory", "$..model")
            .await
            .expect("Failed to run JSON.GET");
        println!("{res34}"); // >>> [["Phoebe","Quaoar","Weywot","Salacia","Mimas"]]
```

##### Rust (Synchronous)

```rust
        let res34: String = r
            .json_get("bikes:inventory", "$..model")
            .expect("Failed to run JSON.GET");
        println!("{res34}"); // >>> [["Phoebe","Quaoar","Weywot","Salacia","Mimas"]]
```



You can use an array slice to select a range of elements from an array. This example returns the names of the first 2 mountain bikes:

Array slicing: Use [start:end] syntax to select a range of array elements when you need to retrieve a subset of items from an array

**Difficulty:** Intermediate

**Builds upon:** get_mtnbikes

**Commands:** JSON.GET

**Complexity:**
- JSON.GET: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> JSON.GET bikes:inventory $..mountain_bikes[0:2].model
"[\"Phoebe\",\"Quaoar\"]"
```

##### C#

```csharp
        RedisResult res34 = db.JSON().Get("bikes:inventory", path: "$..mountain_bikes[0:2].model");
        Console.WriteLine(res34);   // >>> ["Phoebe","Quaoar"]
```

##### Go

```go
	res7, err := rdb.JSONGet(ctx, "bikes:inventory", "$..mountain_bikes[0:2].model").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res7) // >>> ["Phoebe","Quaoar"]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> get2MtnBikes = asyncCommands
                    .jsonGet("bikes:inventory", JsonPath.of("$..mountain_bikes[0:2].model"))
                    .thenAccept(System.out::println)
                    // >>> [["Phoebe","Quaoar"]]
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> get2MtnBikes = reactiveCommands.jsonGet("bikes:inventory", JsonPath.of("$..mountain_bikes[0:2].model"))
                    .collectList()
                    .doOnNext(System.out::println) // >>> [["Phoebe","Quaoar"]]
                    .then();
```

##### Java (Synchronous - Jedis)

```java
        Object res34 = jedis.jsonGet(
            "bikes:inventory", new Path2("$..mountain_bikes[0:2].model")
        );
        System.out.println(res34);  // >>> ["Phoebe","Quaoar"]
```

##### JavaScript (Node.js)

```javascript
const res34 = await client.json.get("bikes:inventory", {
  path: "$..mountain_bikes[0:2].model"
});
console.log(res34); //  ['Phoebe', 'Quaoar']
```

##### PHP

```php
        $res7b = $r->jsonget('bikes:inventory', '', '', '', '$..mountain_bikes[0:2].model');
        echo $res7b . PHP_EOL;
        // >>> ["Phoebe","Quaoar"]
```

##### Python

```python
res7 = r.json().get("bikes:inventory", "$..mountain_bikes[0:2].model")
print(res7)  # >>> [['Phoebe', 'Quaoar']]
```

##### Ruby

```ruby
res7 = r.json_get('bikes:inventory', '$..mountain_bikes[0:2].model')
p res7 # >>> ["Phoebe", "Quaoar"]
```

##### Rust (Asynchronous)

```rust
        let res35: String = r
            .json_get("bikes:inventory", "$..mountain_bikes[0:2].model")
            .await
            .expect("Failed to run JSON.GET");
        println!("{res35}"); // >>> [["Phoebe","Quaoar"]]
```

##### Rust (Synchronous)

```rust
        let res35: String = r
            .json_get("bikes:inventory", "$..mountain_bikes[0:2].model")
            .expect("Failed to run JSON.GET");
        println!("{res35}"); // >>> [["Phoebe","Quaoar"]]
```



Filter expressions `?()` let you select JSON elements based on certain conditions. You can use comparison operators (`==`, `!=`, `<`, `<=`, `>`, `>=`, and starting with version v2.4.2, also `=~`), logical operators (`&&`, `||`), and parenthesis (`(`, `)`) within these expressions. A filter expression can be applied on an array or on an object, iterating over all the **elements** in the array or all the **values** in the object, retrieving only the ones that match the filter condition. 

Paths within the filter condition use the dot notation with either `@` to denote the current array element or the current object value, or `$` to denote the top-level element. For example, use `@.key_name` to refer to a nested value and `$.top_level_key_name` to refer to a top-level value.

From version v2.4.2 onward, you can use the comparison operator `=~` to match a path of a string value on the left side against a regular expression pattern on the right side. For more information, see the [supported regular expression syntax docs](https://docs.rs/regex/latest/regex/#syntax).

Non-string values do not match. A match can only occur when the left side is a path of a string value and the right side is either a hard-coded string, or a path of a string value. See [examples](#json-filter-examples) below.

The regex match is partial, meaning a regex pattern like `"foo"` matches a string such as `"barefoots"`.
To make the match exact, use the regex pattern `"^foo$"`.

Other JSONPath engines may use regex patterns between slashes (for example, `/foo/`),
and their match is exact. They can perform partial matches using a regex pattern such
as `/.*foo.*/`.

### Filter examples

In the following example, the filter only returns mountain bikes with a price less than 3000 and
a weight less than 10:

Filter expressions: Use ?() with comparison and logical operators to select elements matching specific conditions when you need to query based on multiple criteria

**Difficulty:** Advanced

**Builds upon:** get_models

**Commands:** JSON.GET

**Complexity:**
- JSON.GET: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> JSON.GET bikes:inventory '$..mountain_bikes[?(@.price < 3000 && @.specs.weight < 10)]'
"[{\"id\":\"bike:2\",\"model\":\"Quaoar\",\"description\":\"Redesigned for the 2020 model year, this bike impressed our testers and is the best all-around trail bike we've ever tested. The Shimano gear system effectively does away with an external cassette, so is super low maintenance in terms of wear and tear. All in all it's an impressive package for the price, making it very competitive.\",\"price\":2072,\"specs\":{\"material\":\"aluminium\",\"weight\":7.9},\"colors\":[\"black\",\"white\"]}]"
```

##### C#

```csharp
        RedisResult res35 = db.JSON().Get(
            "bikes:inventory",
            path: "$..mountain_bikes[?(@.price < 3000 && @.specs.weight < 10)]"
        );
        Console.WriteLine(res35);
        // >>> [{"id":"bike:2","model":"Quaoar","description":"Redesigned for the 2020 model year...
```

##### Go

```go
	res8, err := rdb.JSONGetWithArgs(ctx, "bikes:inventory",
		&redis.JSONGetArgs{Indent: "  ", Newline: "\n", Space: " "},
		"$..mountain_bikes[?(@.price < 3000 && @.specs.weight < 10)]",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res8)
	// >>>
	// [
	//   {
	//     "colors": [
	//       "black",
	//       "white"
	//     ],
	//     "description": "Redesigned for the 2020 model year
	// ...
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> filter1 = asyncCommands
                    .jsonGet("bikes:inventory", JsonPath.of("$..mountain_bikes[?(@.price < 3000 && @.specs.weight < 10)]"))
                    .thenAccept(System.out::println)
                    // >>> [[{"id":"bike:2","model":"Quaoar","description":...
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> filter1 = reactiveCommands
                    .jsonGet("bikes:inventory", JsonPath.of("$..mountain_bikes[?(@.price < 3000 && @.specs.weight < 10)]"))
                    .collectList()
                    .doOnNext(System.out::println) // >>> [[{"id":"bike:2","model":"Quaoar","description":...
                    .then();
```

##### Java (Synchronous - Jedis)

```java
        Object res35 = jedis.jsonGet(
            "bikes:inventory",
            new Path2("$..mountain_bikes[?(@.price < 3000 && @.specs.weight < 10)]")
        );
        System.out.println(res35);
        // >>> [{"specs":{"material":"aluminium","weight":7.9},"price":2072,...
```

##### JavaScript (Node.js)

```javascript
const res35 = await client.json.get("bikes:inventory", {
  path: "$..mountain_bikes[?(@.price < 3000 && @.specs.weight < 10)]"
});
console.log(res35);
/*
[
  {
    id: 'bike:2',
    model: 'Quaoar',
    description: "Redesigned for the 2020 model year, this bike impressed our testers and is the best all-around trail bike we've ever tested. The Shimano gear system effectively does away with an external cassette, so is super low maintenance in terms of wear and teaawait client. All in all it's an impressive package for the price, making it very competitive.",
    price: 2072,
    specs: { material: 'aluminium', weight: 7.9 },
    colors: [ 'black', 'white' ]
  }
]
*/
```

##### PHP

```php
        $res8b = $r->jsonget(
            'bikes:inventory',
            '',
            '',
            '',
            '$..mountain_bikes[?(@.price < 3000 && @.specs.weight < 10)]'
        );
        echo $res8b . PHP_EOL;
        // >>> [{"id":"bike:2","model":"Quaoar",...}]
```

##### Python

```python
res8 = r.json().get(
    "bikes:inventory",
    "$..mountain_bikes[?(@.price < 3000 && @.specs.weight < 10)]",
)
print(res8)
# >>> [{'id': 'bike:2', 'model': 'Quaoar',
#           'description': "Redesigned for the 2020 model year...
```

##### Ruby

```ruby
res8 = r.json_get(
  'bikes:inventory',
  '$..mountain_bikes[?(@.price < 3000 && @.specs.weight < 10)]'
)
p res8
# >>> [{"id"=>"bike:2", "model"=>"Quaoar",
# >>>   "description"=>"Redesigned for the 2020 model year...
```

##### Rust (Asynchronous)

```rust
        let res36: String = r
            .json_get(
                "bikes:inventory",
                "$..mountain_bikes[?(@.price < 3000 && @.specs.weight < 10)]",
            )
            .await
            .expect("Failed to run JSON.GET");
        println!("{res36}");
        // >>> [[{"id":"bike:2","model":"Quaoar","description":"Redesigned for the 2020 model year...
```

##### Rust (Synchronous)

```rust
        let res36: String = r
            .json_get(
                "bikes:inventory",
                "$..mountain_bikes[?(@.price < 3000 && @.specs.weight < 10)]",
            )
            .expect("Failed to run JSON.GET");
        println!("{res36}");
        // >>> [[{"id":"bike:2","model":"Quaoar","description":"Redesigned for the 2020 model year...
```



This example filters the inventory for the model names of bikes made from alloy:

Equality filters: Use == operator in filter expressions to select elements with specific field values when you need to find items matching exact criteria

**Difficulty:** Advanced

**Builds upon:** filter1

**Commands:** JSON.GET

**Complexity:**
- JSON.GET: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> JSON.GET bikes:inventory '$..[?(@.specs.material == "alloy")].model'
"[\"Weywot\",\"Mimas\"]"
```

##### C#

```csharp
        RedisResult res36 = db.JSON().Get(
            "bikes:inventory",
            path: "$..[?(@.specs.material == 'alloy')].model"
        );
        Console.WriteLine(res36);   // >>> ["Weywot","Mimas"]
```

##### Go

```go
	res9, err := rdb.JSONGet(ctx,
		"bikes:inventory",
		"$..[?(@.specs.material == 'alloy')].model",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res9) // >>> ["Mimas","Weywot"]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> filter2 = asyncCommands
                    .jsonGet("bikes:inventory", JsonPath.of("$..[?(@.specs.material == 'alloy')].model"))
                    .thenAccept(System.out::println)
                    // >>> [["Weywot","Mimas"]]
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> filter2 = reactiveCommands
                    .jsonGet("bikes:inventory", JsonPath.of("$..[?(@.specs.material == 'alloy')].model")).collectList()
                    .doOnNext(System.out::println) // >>> [["Weywot","Mimas"]]
                    .then();
```

##### Java (Synchronous - Jedis)

```java
        Object res36 = jedis.jsonGet(
            "bikes:inventory", new Path2("$..[?(@.specs.material == 'alloy')].model")
        );
        System.out.println(res36);  // >>> ["Weywot","Mimas"]
```

##### JavaScript (Node.js)

```javascript
//  names of bikes made from an alloy
const res36 = await client.json.get("bikes:inventory", {
  path: "$..[?(@.specs.material == 'alloy')].model"
});
console.log(res36); //  ['Weywot', 'Mimas']
```

##### PHP

```php
        $res9b = $r->jsonget('bikes:inventory', '', '', '', "$..[?(@.specs.material == 'alloy')].model");
        echo $res9b . PHP_EOL;
        // >>> ["Weywot","Mimas"]
```

##### Python

```python
res9 = r.json().get("bikes:inventory", "$..[?(@.specs.material == 'alloy')].model")
print(res9)  # >>> ['Weywot', 'Mimas']
```

##### Ruby

```ruby
res9 = r.json_get('bikes:inventory', "$..[?(@.specs.material == 'alloy')].model")
p res9 # >>> ["Weywot", "Mimas"]
```

##### Rust (Asynchronous)

```rust
        let res37: String = r
            .json_get(
                "bikes:inventory",
                "$..[?(@.specs.material == 'alloy')].model",
            )
            .await
            .expect("Failed to run JSON.GET");
        println!("{res37}"); // >>> [["Weywot","Mimas"]]
```

##### Rust (Synchronous)

```rust
        let res37: String = r
            .json_get(
                "bikes:inventory",
                "$..[?(@.specs.material == 'alloy')].model",
            )
            .expect("Failed to run JSON.GET");
        println!("{res37}"); // >>> [["Weywot","Mimas"]]
```



This example, valid from version v2.4.2 onwards, filters only bikes whose material begins with
"al-" using regex match. Note that this match is case-insensitive because of the prefix `(?i)` in
the regular expression pattern `"(?i)al"`:

Regex filters: Use =~ operator with regular expressions in filter expressions to match patterns in string values when you need flexible pattern-based filtering

**Difficulty:** Advanced

**Builds upon:** filter2

**Commands:** JSON.GET

**Complexity:**
- JSON.GET: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> JSON.GET bikes:inventory '$..[?(@.specs.material =~ "(?i)al")].model'
"[\"Quaoar\",\"Weywot\",\"Salacia\",\"Mimas\"]"
```

##### C#

```csharp
        RedisResult res37 = db.JSON().Get(
            "bikes:inventory",
            path: "$..[?(@.specs.material =~ '(?i)al')].model"
        );
        Console.WriteLine(res37);   // >>> ["Quaoar","Weywot","Salacia","Mimas"]
```

##### Go

```go
	res10, err := rdb.JSONGet(ctx,
		"bikes:inventory",
		"$..[?(@.specs.material =~ '(?i)al')].model",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res10) // >>> ["Salacia","Mimas","Quaoar","Weywot"]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> filter3 = asyncCommands
                    .jsonGet("bikes:inventory", JsonPath.of("$..[?(@.specs.material =~ '(?i)al')].model"))
                    .thenAccept(System.out::println)
                    // >>> [["Quaoar","Weywot","Salacia","Mimas"]]
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> filter3 = reactiveCommands
                    .jsonGet("bikes:inventory", JsonPath.of("$..[?(@.specs.material =~ '(?i)al')].model")).collectList()
                    .doOnNext(System.out::println) // >>> [["Quaoar","Weywot","Salacia","Mimas"]]
                    .then();
```

##### Java (Synchronous - Jedis)

```java
        Object res37 = jedis.jsonGet(
            "bikes:inventory", new Path2("$..[?(@.specs.material =~ '(?i)al')].model")
        );
        System.out.println(res37);
        // >>> ["Quaoar","Weywot","Salacia","Mimas"]
```

##### JavaScript (Node.js)

```javascript
const res37 = await client.json.get("bikes:inventory", {
  path: "$..[?(@.specs.material =~ '(?i)al')].model"
});
console.log(res37); //  ['Quaoar', 'Weywot', 'Salacia', 'Mimas']
```

##### PHP

```php
        $res10b = $r->jsonget('bikes:inventory', '', '', '', "$..[?(@.specs.material =~ '(?i)al')].model");
        echo $res10b . PHP_EOL;
        // >>> ["Quaoar","Weywot","Salacia","Mimas"]
```

##### Python

```python
res10 = r.json().get("bikes:inventory", "$..[?(@.specs.material =~ '(?i)al')].model")
print(res10)  # >>> ['Quaoar', 'Weywot', 'Salacia', 'Mimas']
```

##### Ruby

```ruby
res10 = r.json_get('bikes:inventory', "$..[?(@.specs.material =~ '(?i)al')].model")
p res10 # >>> ["Quaoar", "Weywot", "Salacia", "Mimas"]
```

##### Rust (Asynchronous)

```rust
        let res38: String = r
            .json_get(
                "bikes:inventory",
                "$..[?(@.specs.material =~ '(?i)al')].model",
            )
            .await
            .expect("Failed to run JSON.GET");
        println!("{res38}"); // >>> [["Quaoar","Weywot","Salacia","Mimas"]]
```

##### Rust (Synchronous)

```rust
        let res38: String = r
            .json_get(
                "bikes:inventory",
                "$..[?(@.specs.material =~ '(?i)al')].model",
            )
            .expect("Failed to run JSON.GET");
        println!("{res38}"); // >>> [["Quaoar","Weywot","Salacia","Mimas"]]
```



You can also specify a regex pattern using a property from the JSON object itself.
For example, we can add a string property named `regex_pat` to each mountain bike,
with the value `"(?i)al"` to match the material, as in the previous example. We
can then match `regex_pat` against the bike's material: 

Dynamic regex filters: Use regex patterns stored in JSON properties to filter elements when you need to apply patterns defined within the document itself

**Difficulty:** Advanced

**Builds upon:** filter3

**Commands:** JSON.SET, JSON.GET

**Complexity:**
- JSON.SET: O(M+N)
- JSON.GET: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> JSON.SET bikes:inventory $.inventory.mountain_bikes[0].regex_pat '"(?i)al"'
OK
> JSON.SET bikes:inventory $.inventory.mountain_bikes[1].regex_pat '"(?i)al"'
OK
> JSON.SET bikes:inventory $.inventory.mountain_bikes[2].regex_pat '"(?i)al"'
OK
> JSON.GET bikes:inventory '$.inventory.mountain_bikes[?(@.specs.material =~ @.regex_pat)].model'
"[\"Quaoar\",\"Weywot\"]"
```

##### C#

```csharp
        bool res38 = db.JSON().Set(
            "bikes:inventory",
            "$.inventory.mountain_bikes[0].regex_pat",
            "\"(?i)al\""
        );
        Console.WriteLine(res38);   // >>> True

        bool res39 = db.JSON().Set(
            "bikes:inventory",
            "$.inventory.mountain_bikes[1].regex_pat",
            "\"(?i)al\""
        );
        Console.WriteLine(res39);   // >>> True

        bool res40 = db.JSON().Set(
            "bikes:inventory",
            "$.inventory.mountain_bikes[2].regex_pat",
            "\"(?i)al\""
        );
        Console.WriteLine(res40);   // >>> True

        RedisResult res41 = db.JSON().Get(
            "bikes:inventory",
            path: "$.inventory.mountain_bikes[?(@.specs.material =~ @.regex_pat)].model"
        );
        Console.WriteLine(res41);   // >>> ["Quaoar","Weywot"]
```

##### Go

```go
	res11, err := rdb.JSONSet(ctx,
		"bikes:inventory",
		"$.inventory.mountain_bikes[0].regex_pat",
		"\"(?i)al\"",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res11) // >>> OK

	res12, err := rdb.JSONSet(ctx,
		"bikes:inventory",
		"$.inventory.mountain_bikes[1].regex_pat",
		"\"(?i)al\"",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res12) // >>> OK

	res13, err := rdb.JSONSet(ctx,
		"bikes:inventory",
		"$.inventory.mountain_bikes[2].regex_pat",
		"\"(?i)al\"",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res13) // >>> OK

	res14, err := rdb.JSONGet(ctx,
		"bikes:inventory",
		"$.inventory.mountain_bikes[?(@.specs.material =~ @.regex_pat)].model",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res14) // >>> ["Quaoar","Weywot"]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> filter4 = asyncCommands.jsonSet("bikes:inventory",
                    JsonPath.of("$.inventory.mountain_bikes[0].regex_pat"), parser.createJsonValue("\"(?i)al\""))
                    .thenCompose(r -> {
                        System.out.println(r); // >>> OK

                        return asyncCommands.jsonSet("bikes:inventory", JsonPath.of("$.inventory.mountain_bikes[1].regex_pat"),
                                parser.createJsonValue("\"(?i)al\""));
                    }).thenCompose(r -> {
                        System.out.println(r); // >>> OK

                        return asyncCommands.jsonSet("bikes:inventory", JsonPath.of("$.inventory.mountain_bikes[2].regex_pat"),
                                parser.createJsonValue("\"(?i)al\""));
                    }).thenCompose(res22 -> {
                        System.out.println(res22); // >>> OK

                        return asyncCommands.jsonGet("bikes:inventory",
                                JsonPath.of("$.inventory.mountain_bikes[?(@.specs.material =~ @.regex_pat)].model"));
                    })
                    .thenAccept(System.out::println)
                    // >>> [["Quaoar","Weywot"]]
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> filter4 = reactiveCommands.jsonSet("bikes:inventory",
                    JsonPath.of("$.inventory.mountain_bikes[0].regex_pat"), parser.createJsonValue("\"(?i)al\""))
                    .doOnNext(r -> {
                        System.out.println(r); // >>> OK
                    })
                    .flatMap(r -> reactiveCommands.jsonSet("bikes:inventory",
                            JsonPath.of("$.inventory.mountain_bikes[1].regex_pat"), parser.createJsonValue("\"(?i)al\"")))
                    .doOnNext(r -> {
                        System.out.println(r); // >>> OK
                    })
                    .flatMap(r -> reactiveCommands.jsonSet("bikes:inventory",
                            JsonPath.of("$.inventory.mountain_bikes[2].regex_pat"), parser.createJsonValue("\"(?i)al\"")))
                    .doOnNext(res22 -> {
                        System.out.println(res22); // >>> OK
                    })
                    .flatMap(res22 -> reactiveCommands
                            .jsonGet("bikes:inventory",
                                    JsonPath.of("$.inventory.mountain_bikes[?(@.specs.material =~ @.regex_pat)].model"))
                            .collectList())
                    .doOnNext(System.out::println) // >>> [["Quaoar","Weywot"]]
                    .then();
```

##### Java (Synchronous - Jedis)

```java
        jedis.jsonSet(
            "bikes:inventory", new Path2("$.inventory.mountain_bikes[0].regex_pat"),
            "\"(?i)al\""
        );
        jedis.jsonSet(
            "bikes:inventory", new Path2("$.inventory.mountain_bikes[1].regex_pat"),
            "\"(?i)al\""
        );
        jedis.jsonSet(
            "bikes:inventory", new Path2("$.inventory.mountain_bikes[2].regex_pat"),
            "\"(?i)al\""
        );
        
        Object res38 = jedis.jsonGet(
            "bikes:inventory",
            new Path2("$.inventory.mountain_bikes[?(@.specs.material =~ @.regex_pat)].model")
        );
        System.out.println(res38);  // >>> ["Quaoar","Weywot"]
```

##### JavaScript (Node.js)

```javascript
const res37a = await client.json.set(
  'bikes:inventory', 
  '$.inventory.mountain_bikes[0].regex_pat', 
  '(?i)al'
);

const res37b = await client.json.set(
  'bikes:inventory', 
  '$.inventory.mountain_bikes[1].regex_pat', 
  '(?i)al'
);

const res37c = await client.json.set(
  'bikes:inventory', 
  '$.inventory.mountain_bikes[2].regex_pat', 
  '(?i)al'
);

const res37d = await client.json.get(
  'bikes:inventory',
  { path: '$.inventory.mountain_bikes[?(@.specs.material =~ @.regex_pat)].model' }
);
console.log(res37d); // ['Quaoar', 'Weywot']
```

##### PHP

```php
        $r->jsonset('bikes:inventory', '$.inventory.mountain_bikes[0].regex_pat', '"(?i)al"');
        $r->jsonset('bikes:inventory', '$.inventory.mountain_bikes[1].regex_pat', '"(?i)al"');
        $r->jsonset('bikes:inventory', '$.inventory.mountain_bikes[2].regex_pat', '"(?i)al"');

        $res14b = $r->jsonget(
            'bikes:inventory',
            '',
            '',
            '',
            '$.inventory.mountain_bikes[?(@.specs.material =~ @.regex_pat)].model'
        );
        echo $res14b . PHP_EOL;
        // >>> ["Quaoar","Weywot"]
```

##### Python

```python
res11 = r.json().set(
    "bikes:inventory", "$.inventory.mountain_bikes[0].regex_pat", "(?i)al"
)
res12 = r.json().set(
    "bikes:inventory", "$.inventory.mountain_bikes[1].regex_pat", "(?i)al"
)
res13 = r.json().set(
    "bikes:inventory", "$.inventory.mountain_bikes[2].regex_pat", "(?i)al"
)

res14 = r.json().get(
    "bikes:inventory",
    "$.inventory.mountain_bikes[?(@.specs.material =~ @.regex_pat)].model",
)
print(res14)  # >>> ['Quaoar', 'Weywot']
```

##### Ruby

```ruby
res11 = r.json_set(
  'bikes:inventory', '$.inventory.mountain_bikes[0].regex_pat', '(?i)al'
)
res12 = r.json_set(
  'bikes:inventory', '$.inventory.mountain_bikes[1].regex_pat', '(?i)al'
)
res13 = r.json_set(
  'bikes:inventory', '$.inventory.mountain_bikes[2].regex_pat', '(?i)al'
)

res14 = r.json_get(
  'bikes:inventory',
  '$.inventory.mountain_bikes[?(@.specs.material =~ @.regex_pat)].model'
)
p res14 # >>> ["Quaoar", "Weywot"]
```

##### Rust (Asynchronous)

```rust
        let _: bool = r
            .json_set(
                "bikes:inventory",
                "$.inventory.mountain_bikes[0].regex_pat",
                &json!("(?i)al"),
            )
            .await
            .expect("Failed to run JSON.SET");
        let _: bool = r
            .json_set(
                "bikes:inventory",
                "$.inventory.mountain_bikes[1].regex_pat",
                &json!("(?i)al"),
            )
            .await
            .expect("Failed to run JSON.SET");
        let _: bool = r
            .json_set(
                "bikes:inventory",
                "$.inventory.mountain_bikes[2].regex_pat",
                &json!("(?i)al"),
            )
            .await
            .expect("Failed to run JSON.SET");

        let res39: String = r
            .json_get(
                "bikes:inventory",
                "$.inventory.mountain_bikes[?(@.specs.material =~ @.regex_pat)].model",
            )
            .await
            .expect("Failed to run JSON.GET");
        println!("{res39}"); // >>> [["Quaoar","Weywot"]]
```

##### Rust (Synchronous)

```rust
        let _: bool = r
            .json_set(
                "bikes:inventory",
                "$.inventory.mountain_bikes[0].regex_pat",
                &json!("(?i)al"),
            )
            .expect("Failed to run JSON.SET");
        let _: bool = r
            .json_set(
                "bikes:inventory",
                "$.inventory.mountain_bikes[1].regex_pat",
                &json!("(?i)al"),
            )
            .expect("Failed to run JSON.SET");
        let _: bool = r
            .json_set(
                "bikes:inventory",
                "$.inventory.mountain_bikes[2].regex_pat",
                &json!("(?i)al"),
            )
            .expect("Failed to run JSON.SET");

        let res39: String = r
            .json_get(
                "bikes:inventory",
                "$.inventory.mountain_bikes[?(@.specs.material =~ @.regex_pat)].model",
            )
            .expect("Failed to run JSON.GET");
        println!("{res39}"); // >>> [["Quaoar","Weywot"]]
```



Beginning with Redis 8.10, the JSONPath filter syntax supports the following operators.

#### Negation `!`

The `!` operator negates a filter condition. It binds more tightly than the logical `&&` and `||` operators, so use parentheses to negate a compound condition. A double negation (`!!`) is equivalent to an existence test.

Filter negation: Use the ! operator to invert a filter condition when you need to select elements that do not match

**Difficulty:** Advanced

**Commands:** JSON.SET, JSON.GET

**Complexity:**
- JSON.SET: O(M+N)
- JSON.GET: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> JSON.SET doc $ '[{"a":1,"b":1},{"b":2},{"a":1},{"c":3}]'
OK
> JSON.GET doc '$[?!@.a]'
"[{\"b\":2},{\"c\":3}]"
> JSON.GET doc '$[?!(@.a==1)]'
"[{\"b\":2},{\"c\":3}]"
> JSON.GET doc '$[?!@.a && @.b]'
"[{\"b\":2}]"
```

##### C#

```csharp
        bool res1 = db.JSON().Set("doc", "$", "[{\"a\":1,\"b\":1},{\"b\":2},{\"a\":1},{\"c\":3}]");
        Console.WriteLine(res1);    // >>> True

        RedisResult res2 = db.JSON().Get("doc", path: "$[?!@.a]");
        Console.WriteLine(res2);    // >>> [{"b":2},{"c":3}]

        RedisResult res3 = db.JSON().Get("doc", path: "$[?!(@.a==1)]");
        Console.WriteLine(res3);    // >>> [{"b":2},{"c":3}]

        RedisResult res4 = db.JSON().Get("doc", path: "$[?!@.a && @.b]");
        Console.WriteLine(res4);    // >>> [{"b":2}]
```

##### Go

```go
	res1, err := rdb.JSONSet(ctx, "doc", "$",
		`[{"a":1,"b":1},{"b":2},{"a":1},{"c":3}]`,
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // >>> OK

	res2, err := rdb.JSONGet(ctx, "doc", `$[?!@.a]`).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2) // >>> [{"b":2},{"c":3}]

	res3, err := rdb.JSONGet(ctx, "doc", `$[?!(@.a==1)]`).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3) // >>> [{"b":2},{"c":3}]

	res4, err := rdb.JSONGet(ctx, "doc", `$[?!@.a && @.b]`).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4) // >>> [{"b":2}]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> filterNegationExample = asyncCommands
                    .jsonSet("doc", JsonPath.ROOT_PATH,
                            parser.createJsonValue("[{\"a\":1,\"b\":1},{\"b\":2},{\"a\":1},{\"c\":3}]"))
                    .thenCompose(res1 -> {
                        System.out.println(res1); // >>> OK
                        return asyncCommands.jsonGet("doc", JsonPath.of("$[?!@.a]"));
                    }).thenCompose(res2 -> {
                        System.out.println(res2); // >>> [[{"b":2},{"c":3}]]
                        return asyncCommands.jsonGet("doc", JsonPath.of("$[?!(@.a==1)]"));
                    }).thenCompose(res3 -> {
                        System.out.println(res3); // >>> [[{"b":2},{"c":3}]]
                        return asyncCommands.jsonGet("doc", JsonPath.of("$[?!@.a && @.b]"));
                    }).thenAccept(res4 -> {
                        System.out.println(res4); // >>> [[{"b":2}]]
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> filterNegationExample = reactiveCommands
                    .jsonSet("doc", JsonPath.ROOT_PATH,
                            parser.createJsonValue("[{\"a\":1,\"b\":1},{\"b\":2},{\"a\":1},{\"c\":3}]"))
                    .doOnNext(res1 -> {
                        System.out.println(res1); // >>> OK
                    })
                    .flatMap(res1 -> reactiveCommands.jsonGet("doc", JsonPath.of("$[?!@.a]")).collectList())
                    .doOnNext(res2 -> {
                        System.out.println(res2); // >>> [[{"b":2},{"c":3}]]
                    })
                    .flatMap(res2 -> reactiveCommands.jsonGet("doc", JsonPath.of("$[?!(@.a==1)]")).collectList())
                    .doOnNext(res3 -> {
                        System.out.println(res3); // >>> [[{"b":2},{"c":3}]]
                    })
                    .flatMap(res3 -> reactiveCommands.jsonGet("doc", JsonPath.of("$[?!@.a && @.b]")).collectList())
                    .doOnNext(res4 -> {
                        System.out.println(res4); // >>> [[{"b":2}]]
                    })
                    .then();
```

##### Java (Synchronous - Jedis)

```java
        String res1 = jedis.jsonSet("doc", new Path2("$"), "[{\"a\":1,\"b\":1},{\"b\":2},{\"a\":1},{\"c\":3}]");
        System.out.println(res1);    // >>> OK

        Object res2 = jedis.jsonGet("doc", new Path2("$[?!@.a]"));
        System.out.println(res2);    // >>> [{"b":2},{"c":3}]

        Object res3 = jedis.jsonGet("doc", new Path2("$[?!(@.a==1)]"));
        System.out.println(res3);    // >>> [{"b":2},{"c":3}]

        Object res4 = jedis.jsonGet("doc", new Path2("$[?!@.a && @.b]"));
        System.out.println(res4);    // >>> [{"b":2}]
```

##### JavaScript (Node.js)

```javascript
const res1 = await client.json.set('doc', '$', [{ a: 1, b: 1 }, { b: 2 }, { a: 1 }, { c: 3 }]);
console.log(res1); // >>> OK

const res2 = await client.json.get('doc', { path: '$[?!@.a]' });
console.log(res2); // >>> [ { b: 2 }, { c: 3 } ]

const res3 = await client.json.get('doc', { path: '$[?!(@.a==1)]' });
console.log(res3); // >>> [ { b: 2 }, { c: 3 } ]

const res4 = await client.json.get('doc', { path: '$[?!@.a && @.b]' });
console.log(res4); // >>> [ { b: 2 } ]
```

##### PHP

```php
        $res1 = $this->redis->jsonset('doc', '$', json_encode(
            [["a" => 1, "b" => 1], ["b" => 2], ["a" => 1], ["c" => 3]]
        ));
        echo $res1 . PHP_EOL; // >>> OK

        $res2 = $this->redis->jsonget('doc', '', '', '', '$[?!@.a]');
        echo $res2 . PHP_EOL; // >>> [{"b":2},{"c":3}]

        $res3 = $this->redis->jsonget('doc', '', '', '', '$[?!(@.a==1)]');
        echo $res3 . PHP_EOL; // >>> [{"b":2},{"c":3}]

        $res4 = $this->redis->jsonget('doc', '', '', '', '$[?!@.a && @.b]');
        echo $res4 . PHP_EOL; // >>> [{"b":2}]
```

##### Python

```python
res1 = r.json().set("doc", "$", [{"a": 1, "b": 1}, {"b": 2}, {"a": 1}, {"c": 3}])
print(res1)
# >>> True

res2 = r.json().get("doc", "$[?!@.a]")
print(res2)
# >>> [{'b': 2}, {'c': 3}]

res3 = r.json().get("doc", "$[?!(@.a==1)]")
print(res3)
# >>> [{'b': 2}, {'c': 3}]

res4 = r.json().get("doc", "$[?!@.a && @.b]")
print(res4)
# >>> [{'b': 2}]
```

##### Ruby

```ruby
res1 = r.json_set('doc', '$', [{ 'a' => 1, 'b' => 1 }, { 'b' => 2 }, { 'a' => 1 }, { 'c' => 3 }])
puts res1 # >>> OK

res2 = r.json_get('doc', '$[?!@.a]')
p res2 # >>> [{"b"=>2}, {"c"=>3}]

res3 = r.json_get('doc', '$[?!(@.a==1)]')
p res3 # >>> [{"b"=>2}, {"c"=>3}]

res4 = r.json_get('doc', '$[?!@.a && @.b]')
p res4 # >>> [{"b"=>2}]
```

##### Rust (Asynchronous)

```rust
        let _: bool = match r.json_set("doc", "$", &json!([{"a":1,"b":1},{"b":2},{"a":1},{"c":3}])).await {
            Ok(v) => v,
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        };

        match r.json_get("doc", "$[?!@.a]").await {
            Ok(res1) => {
                let res1: String = res1;
                println!("{res1}");    // >>> [{"b":2},{"c":3}]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$[?!(@.a==1)]").await {
            Ok(res2) => {
                let res2: String = res2;
                println!("{res2}");    // >>> [{"b":2},{"c":3}]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$[?!@.a && @.b]").await {
            Ok(res3) => {
                let res3: String = res3;
                println!("{res3}");    // >>> [{"b":2}]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

```

##### Rust (Synchronous)

```rust
        match r.json_set("doc", "$", &json!([{"a":1,"b":1},{"b":2},{"a":1},{"c":3}])) {
            Ok(res1) => {
                let res1: bool = res1;
                println!("{}", if res1 { "OK" } else { "(nil)" });    // >>> OK
            },
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$[?!@.a]") {
            Ok(res2) => {
                let res2: String = res2;
                println!("{res2}");    // >>> [{"b":2},{"c":3}]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$[?!(@.a==1)]") {
            Ok(res3) => {
                let res3: String = res3;
                println!("{res3}");    // >>> [{"b":2},{"c":3}]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$[?!@.a && @.b]") {
            Ok(res4) => {
                let res4: String = res4;
                println!("{res4}");    // >>> [{"b":2}]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

```



#### Comparing array and object literals

The `==` and `!=` operators can compare any JSON literal, including array and object literals, on either side of the operator. Comparison is by structural (deep) equality. A comparison between values of different types is always false.

Literal comparison: Use == and != to compare array and object literals by structural equality when you need to match a whole nested value

**Difficulty:** Advanced

**Commands:** JSON.SET, JSON.GET

**Complexity:**
- JSON.SET: O(M+N)
- JSON.GET: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> JSON.SET doc $ '{"arrs":[[1],[2],[1,2],[1,[2]]],"objs":[{"x":1},{"x":2},{"y":1}]}'
OK
> JSON.GET doc '$.arrs[?(@ == [1])]'
"[[1]]"
> JSON.GET doc '$.arrs[?(@ == [1,[2]])]'
"[[1,[2]]]"
> JSON.GET doc '$.objs[?(@ == {"x":1})]'
"[{\"x\":1}]"
```

##### C#

```csharp
        bool res5 = db.JSON().Set(
            "doc",
            "$",
            "{\"arrs\":[[1],[2],[1,2],[1,[2]]],\"objs\":[{\"x\":1},{\"x\":2},{\"y\":1}]}"
        );
        Console.WriteLine(res5);    // >>> True

        RedisResult res6 = db.JSON().Get("doc", path: "$.arrs[?(@ == [1])]");
        Console.WriteLine(res6);    // >>> [[1]]

        RedisResult res7 = db.JSON().Get("doc", path: "$.arrs[?(@ == [1,[2]])]");
        Console.WriteLine(res7);    // >>> [[1,[2]]]

        RedisResult res8 = db.JSON().Get("doc", path: "$.objs[?(@ == {\"x\":1})]");
        Console.WriteLine(res8);    // >>> [{"x":1}]
```

##### Go

```go
	res1, err := rdb.JSONSet(ctx, "doc", "$",
		`{"arrs":[[1],[2],[1,2],[1,[2]]],"objs":[{"x":1},{"x":2},{"y":1}]}`,
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // >>> OK

	res2, err := rdb.JSONGet(ctx, "doc", `$.arrs[?(@ == [1])]`).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2) // >>> [[1]]

	res3, err := rdb.JSONGet(ctx, "doc", `$.arrs[?(@ == [1,[2]])]`).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3) // >>> [[1,[2]]]

	res4, err := rdb.JSONGet(ctx, "doc", `$.objs[?(@ == {"x":1})]`).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4) // >>> [{"x":1}]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> filterLiteralEqExample = asyncCommands
                    .jsonSet("doc", JsonPath.ROOT_PATH,
                            parser.createJsonValue(
                                    "{\"arrs\":[[1],[2],[1,2],[1,[2]]],\"objs\":[{\"x\":1},{\"x\":2},{\"y\":1}]}"))
                    .thenCompose(res1 -> {
                        System.out.println(res1); // >>> OK
                        return asyncCommands.jsonGet("doc", JsonPath.of("$.arrs[?(@ == [1])]"));
                    }).thenCompose(res2 -> {
                        System.out.println(res2); // >>> [[[1]]]
                        return asyncCommands.jsonGet("doc", JsonPath.of("$.arrs[?(@ == [1,[2]])]"));
                    }).thenCompose(res3 -> {
                        System.out.println(res3); // >>> [[[1,[2]]]]
                        return asyncCommands.jsonGet("doc", JsonPath.of("$.objs[?(@ == {\"x\":1})]"));
                    }).thenAccept(res4 -> {
                        System.out.println(res4); // >>> [[{"x":1}]]
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> filterLiteralEqExample = reactiveCommands
                    .jsonSet("doc", JsonPath.ROOT_PATH,
                            parser.createJsonValue(
                                    "{\"arrs\":[[1],[2],[1,2],[1,[2]]],\"objs\":[{\"x\":1},{\"x\":2},{\"y\":1}]}"))
                    .doOnNext(res1 -> {
                        System.out.println(res1); // >>> OK
                    })
                    .flatMap(res1 -> reactiveCommands.jsonGet("doc", JsonPath.of("$.arrs[?(@ == [1])]")).collectList())
                    .doOnNext(res2 -> {
                        System.out.println(res2); // >>> [[[1]]]
                    })
                    .flatMap(res2 -> reactiveCommands.jsonGet("doc", JsonPath.of("$.arrs[?(@ == [1,[2]])]")).collectList())
                    .doOnNext(res3 -> {
                        System.out.println(res3); // >>> [[[1,[2]]]]
                    })
                    .flatMap(res3 -> reactiveCommands.jsonGet("doc", JsonPath.of("$.objs[?(@ == {\"x\":1})]")).collectList())
                    .doOnNext(res4 -> {
                        System.out.println(res4); // >>> [[{"x":1}]]
                    })
                    .then();
```

##### Java (Synchronous - Jedis)

```java
        String res5 = jedis.jsonSet(
            "doc",
            new Path2("$"),
            "{\"arrs\":[[1],[2],[1,2],[1,[2]]],\"objs\":[{\"x\":1},{\"x\":2},{\"y\":1}]}"
        );
        System.out.println(res5);    // >>> OK

        Object res6 = jedis.jsonGet("doc", new Path2("$.arrs[?(@ == [1])]"));
        System.out.println(res6);    // >>> [[1]]

        Object res7 = jedis.jsonGet("doc", new Path2("$.arrs[?(@ == [1,[2]])]"));
        System.out.println(res7);    // >>> [[1,[2]]]

        Object res8 = jedis.jsonGet("doc", new Path2("$.objs[?(@ == {\"x\":1})]"));
        System.out.println(res8);    // >>> [{"x":1}]
```

##### JavaScript (Node.js)

```javascript
const res5 = await client.json.set('doc', '$', {
  arrs: [[1], [2], [1, 2], [1, [2]]],
  objs: [{ x: 1 }, { x: 2 }, { y: 1 }]
});
console.log(res5); // >>> OK

const res6 = await client.json.get('doc', { path: '$.arrs[?(@ == [1])]' });
console.log(res6); // >>> [ [ 1 ] ]

const res7 = await client.json.get('doc', { path: '$.arrs[?(@ == [1,[2]])]' });
console.log(res7); // >>> [ [ 1, [ 2 ] ] ]

const res8 = await client.json.get('doc', { path: '$.objs[?(@ == {"x":1})]' });
console.log(res8); // >>> [ { x: 1 } ]
```

##### PHP

```php
        $res5 = $this->redis->jsonset('doc', '$', json_encode([
            "arrs" => [[1], [2], [1, 2], [1, [2]]],
            "objs" => [["x" => 1], ["x" => 2], ["y" => 1]],
        ]));
        echo $res5 . PHP_EOL; // >>> OK

        $res6 = $this->redis->jsonget('doc', '', '', '', '$.arrs[?(@ == [1])]');
        echo $res6 . PHP_EOL; // >>> [[1]]

        $res7 = $this->redis->jsonget('doc', '', '', '', '$.arrs[?(@ == [1,[2]])]');
        echo $res7 . PHP_EOL; // >>> [[1,[2]]]

        $res8 = $this->redis->jsonget('doc', '', '', '', '$.objs[?(@ == {"x":1})]');
        echo $res8 . PHP_EOL; // >>> [{"x":1}]
```

##### Python

```python
res1 = r.json().set(
    "doc",
    "$",
    {"arrs": [[1], [2], [1, 2], [1, [2]]], "objs": [{"x": 1}, {"x": 2}, {"y": 1}]},
)
print(res1)
# >>> True

res2 = r.json().get("doc", "$.arrs[?(@ == [1])]")
print(res2)
# >>> [[1]]

res3 = r.json().get("doc", "$.arrs[?(@ == [1,[2]])]")
print(res3)
# >>> [[1, [2]]]

res4 = r.json().get("doc", '$.objs[?(@ == {"x":1})]')
print(res4)
# >>> [{'x': 1}]
```

##### Ruby

```ruby
res1 = r.json_set(
  'doc', '$',
  { 'arrs' => [[1], [2], [1, 2], [1, [2]]], 'objs' => [{ 'x' => 1 }, { 'x' => 2 }, { 'y' => 1 }] }
)
puts res1 # >>> OK

res2 = r.json_get('doc', '$.arrs[?(@ == [1])]')
p res2 # >>> [[1]]

res3 = r.json_get('doc', '$.arrs[?(@ == [1,[2]])]')
p res3 # >>> [[1, [2]]]

res4 = r.json_get('doc', '$.objs[?(@ == {"x":1})]')
p res4 # >>> [{"x"=>1}]
```

##### Rust (Asynchronous)

```rust
        let _: bool = match r.json_set(
            "doc",
            "$",
            &json!({"arrs":[[1],[2],[1,2],[1,[2]]],"objs":[{"x":1},{"x":2},{"y":1}]}),
        ).await {
            Ok(v) => v,
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        };

        match r.json_get("doc", "$.arrs[?(@ == [1])]").await {
            Ok(res4) => {
                let res4: String = res4;
                println!("{res4}");    // >>> [[1]]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$.arrs[?(@ == [1,[2]])]").await {
            Ok(res5) => {
                let res5: String = res5;
                println!("{res5}");    // >>> [[1,[2]]]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", r#"$.objs[?(@ == {"x":1})]"#).await {
            Ok(res6) => {
                let res6: String = res6;
                println!("{res6}");    // >>> [{"x":1}]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

```

##### Rust (Synchronous)

```rust
        match r.json_set(
            "doc",
            "$",
            &json!({"arrs":[[1],[2],[1,2],[1,[2]]],"objs":[{"x":1},{"x":2},{"y":1}]}),
        ) {
            Ok(res5) => {
                let res5: bool = res5;
                println!("{}", if res5 { "OK" } else { "(nil)" });    // >>> OK
            },
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$.arrs[?(@ == [1])]") {
            Ok(res6) => {
                let res6: String = res6;
                println!("{res6}");    // >>> [[1]]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$.arrs[?(@ == [1,[2]])]") {
            Ok(res7) => {
                let res7: String = res7;
                println!("{res7}");    // >>> [[1,[2]]]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", r#"$.objs[?(@ == {"x":1})]"#) {
            Ok(res8) => {
                let res8: String = res8;
                println!("{res8}");    // >>> [{"x":1}]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

```



#### Arithmetic operators

The binary operators `+`, `-`, `*`, `/`, and `%` and the unary operators `-` and `+` operate on numbers. Precedence, from highest to lowest, is: unary `-`/`+`, then `*`/`/`/`%`, then `+`/`-`. Use parentheses to override precedence. Division always produces a floating-point result. Division or modulo by zero produces *Nothing*, so no element matches.

Remember that arithmetic operators must be surrounded by spaces (see [Evaluation semantics](#evaluation-semantics)).

Arithmetic in filters: Use +, -, *, / and % inside a filter condition when you need to compute a value before comparing it

**Difficulty:** Advanced

**Commands:** JSON.SET, JSON.GET

**Complexity:**
- JSON.SET: O(M+N)
- JSON.GET: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> JSON.SET doc $ '[{"a":2,"b":3},{"a":5,"b":2}]'
OK
> JSON.GET doc '$[?@.a + 1 == 3]'
"[{\"a\":2,\"b\":3}]"
> JSON.GET doc '$[?@.a + @.b * 2 == 8]'
"[{\"a\":2,\"b\":3}]"
> JSON.GET doc '$[?(@.a + @.b) * 2 == 10]'
"[{\"a\":2,\"b\":3}]"
```

##### C#

```csharp
        bool res9 = db.JSON().Set("doc", "$", "[{\"a\":2,\"b\":3},{\"a\":5,\"b\":2}]");
        Console.WriteLine(res9);    // >>> True

        RedisResult res10 = db.JSON().Get("doc", path: "$[?@.a + 1 == 3]");
        Console.WriteLine(res10);   // >>> [{"a":2,"b":3}]

        RedisResult res11 = db.JSON().Get("doc", path: "$[?@.a + @.b * 2 == 8]");
        Console.WriteLine(res11);   // >>> [{"a":2,"b":3}]

        RedisResult res12 = db.JSON().Get("doc", path: "$[?(@.a + @.b) * 2 == 10]");
        Console.WriteLine(res12);   // >>> [{"a":2,"b":3}]
```

##### Go

```go
	res1, err := rdb.JSONSet(ctx, "doc", "$",
		`[{"a":2,"b":3},{"a":5,"b":2}]`,
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // >>> OK

	res2, err := rdb.JSONGet(ctx, "doc", `$[?@.a + 1 == 3]`).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2) // >>> [{"a":2,"b":3}]

	res3, err := rdb.JSONGet(ctx, "doc", `$[?@.a + @.b * 2 == 8]`).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3) // >>> [{"a":2,"b":3}]

	res4, err := rdb.JSONGet(ctx, "doc", `$[?(@.a + @.b) * 2 == 10]`).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4) // >>> [{"a":2,"b":3}]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> filterArithmeticExample = asyncCommands
                    .jsonSet("doc", JsonPath.ROOT_PATH,
                            parser.createJsonValue("[{\"a\":2,\"b\":3},{\"a\":5,\"b\":2}]"))
                    .thenCompose(res1 -> {
                        System.out.println(res1); // >>> OK
                        return asyncCommands.jsonGet("doc", JsonPath.of("$[?@.a + 1 == 3]"));
                    }).thenCompose(res2 -> {
                        System.out.println(res2); // >>> [[{"a":2,"b":3}]]
                        return asyncCommands.jsonGet("doc", JsonPath.of("$[?@.a + @.b * 2 == 8]"));
                    }).thenCompose(res3 -> {
                        System.out.println(res3); // >>> [[{"a":2,"b":3}]]
                        return asyncCommands.jsonGet("doc", JsonPath.of("$[?(@.a + @.b) * 2 == 10]"));
                    }).thenAccept(res4 -> {
                        System.out.println(res4); // >>> [[{"a":2,"b":3}]]
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> filterArithmeticExample = reactiveCommands
                    .jsonSet("doc", JsonPath.ROOT_PATH, parser.createJsonValue("[{\"a\":2,\"b\":3},{\"a\":5,\"b\":2}]"))
                    .doOnNext(res1 -> {
                        System.out.println(res1); // >>> OK
                    })
                    .flatMap(res1 -> reactiveCommands.jsonGet("doc", JsonPath.of("$[?@.a + 1 == 3]")).collectList())
                    .doOnNext(res2 -> {
                        System.out.println(res2); // >>> [[{"a":2,"b":3}]]
                    })
                    .flatMap(res2 -> reactiveCommands.jsonGet("doc", JsonPath.of("$[?@.a + @.b * 2 == 8]")).collectList())
                    .doOnNext(res3 -> {
                        System.out.println(res3); // >>> [[{"a":2,"b":3}]]
                    })
                    .flatMap(res3 -> reactiveCommands.jsonGet("doc", JsonPath.of("$[?(@.a + @.b) * 2 == 10]")).collectList())
                    .doOnNext(res4 -> {
                        System.out.println(res4); // >>> [[{"a":2,"b":3}]]
                    })
                    .then();
```

##### Java (Synchronous - Jedis)

```java
        String res9 = jedis.jsonSet("doc", new Path2("$"), "[{\"a\":2,\"b\":3},{\"a\":5,\"b\":2}]");
        System.out.println(res9);    // >>> OK

        Object res10 = jedis.jsonGet("doc", new Path2("$[?@.a + 1 == 3]"));
        System.out.println(res10);    // >>> [{"a":2,"b":3}]

        Object res11 = jedis.jsonGet("doc", new Path2("$[?@.a + @.b * 2 == 8]"));
        System.out.println(res11);    // >>> [{"a":2,"b":3}]

        Object res12 = jedis.jsonGet("doc", new Path2("$[?(@.a + @.b) * 2 == 10]"));
        System.out.println(res12);    // >>> [{"a":2,"b":3}]
```

##### JavaScript (Node.js)

```javascript
const res9 = await client.json.set('doc', '$', [{ a: 2, b: 3 }, { a: 5, b: 2 }]);
console.log(res9); // >>> OK

const res10 = await client.json.get('doc', { path: '$[?@.a + 1 == 3]' });
console.log(res10); // >>> [ { a: 2, b: 3 } ]

const res11 = await client.json.get('doc', { path: '$[?@.a + @.b * 2 == 8]' });
console.log(res11); // >>> [ { a: 2, b: 3 } ]

const res12 = await client.json.get('doc', { path: '$[?(@.a + @.b) * 2 == 10]' });
console.log(res12); // >>> [ { a: 2, b: 3 } ]
```

##### PHP

```php
        $res9 = $this->redis->jsonset('doc', '$', json_encode(
            [["a" => 2, "b" => 3], ["a" => 5, "b" => 2]]
        ));
        echo $res9 . PHP_EOL; // >>> OK

        $res10 = $this->redis->jsonget('doc', '', '', '', '$[?@.a + 1 == 3]');
        echo $res10 . PHP_EOL; // >>> [{"a":2,"b":3}]

        $res11 = $this->redis->jsonget('doc', '', '', '', '$[?@.a + @.b * 2 == 8]');
        echo $res11 . PHP_EOL; // >>> [{"a":2,"b":3}]

        $res12 = $this->redis->jsonget('doc', '', '', '', '$[?(@.a + @.b) * 2 == 10]');
        echo $res12 . PHP_EOL; // >>> [{"a":2,"b":3}]
```

##### Python

```python
res1 = r.json().set("doc", "$", [{"a": 2, "b": 3}, {"a": 5, "b": 2}])
print(res1)
# >>> True

res2 = r.json().get("doc", "$[?@.a + 1 == 3]")
print(res2)
# >>> [{'a': 2, 'b': 3}]

res3 = r.json().get("doc", "$[?@.a + @.b * 2 == 8]")
print(res3)
# >>> [{'a': 2, 'b': 3}]

res4 = r.json().get("doc", "$[?(@.a + @.b) * 2 == 10]")
print(res4)
# >>> [{'a': 2, 'b': 3}]
```

##### Ruby

```ruby
res1 = r.json_set('doc', '$', [{ 'a' => 2, 'b' => 3 }, { 'a' => 5, 'b' => 2 }])
puts res1 # >>> OK

res2 = r.json_get('doc', '$[?@.a + 1 == 3]')
p res2 # >>> [{"a"=>2, "b"=>3}]

res3 = r.json_get('doc', '$[?@.a + @.b * 2 == 8]')
p res3 # >>> [{"a"=>2, "b"=>3}]

res4 = r.json_get('doc', '$[?(@.a + @.b) * 2 == 10]')
p res4 # >>> [{"a"=>2, "b"=>3}]
```

##### Rust (Asynchronous)

```rust
        let _: bool = match r.json_set("doc", "$", &json!([{"a":2,"b":3},{"a":5,"b":2}])).await {
            Ok(v) => v,
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        };

        match r.json_get("doc", "$[?@.a + 1 == 3]").await {
            Ok(res7) => {
                let res7: String = res7;
                println!("{res7}");    // >>> [{"a":2,"b":3}]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$[?@.a + @.b * 2 == 8]").await {
            Ok(res8) => {
                let res8: String = res8;
                println!("{res8}");    // >>> [{"a":2,"b":3}]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$[?(@.a + @.b) * 2 == 10]").await {
            Ok(res9) => {
                let res9: String = res9;
                println!("{res9}");    // >>> [{"a":2,"b":3}]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

```

##### Rust (Synchronous)

```rust
        match r.json_set("doc", "$", &json!([{"a":2,"b":3},{"a":5,"b":2}])) {
            Ok(res9) => {
                let res9: bool = res9;
                println!("{}", if res9 { "OK" } else { "(nil)" });    // >>> OK
            },
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$[?@.a + 1 == 3]") {
            Ok(res10) => {
                let res10: String = res10;
                println!("{res10}");    // >>> [{"a":2,"b":3}]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$[?@.a + @.b * 2 == 8]") {
            Ok(res11) => {
                let res11: String = res11;
                println!("{res11}");    // >>> [{"a":2,"b":3}]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$[?(@.a + @.b) * 2 == 10]") {
            Ok(res12) => {
                let res12: String = res12;
                println!("{res12}");    // >>> [{"a":2,"b":3}]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

```



#### Membership: `in` and `nin`

`value in array` matches when `value` is a member of `array`; `value nin array` is its strict negation. The right-hand side can be an array literal or a path to an array. Membership uses the same structural comparison and number coercion as `==`. If the right-hand side is not an array, `in` is false (so `nin` is true).

Membership filters: Use in and nin to test whether a value is a member of an array when you need set-style matching

**Difficulty:** Advanced

**Commands:** JSON.SET, JSON.GET

**Complexity:**
- JSON.SET: O(M+N)
- JSON.GET: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> JSON.SET doc $ '{"a":[1,2,3,4],"allow":[2,3]}'
OK
> JSON.GET doc '$.a[?@ in [2,4]]'
"[2,4]"
> JSON.GET doc '$.a[?@ nin [2,4]]'
"[1,3]"
> JSON.GET doc '$.a[?@ in $.allow]'
"[2,3]"
```

##### C#

```csharp
        bool res13 = db.JSON().Set("doc", "$", "{\"a\":[1,2,3,4],\"allow\":[2,3]}");
        Console.WriteLine(res13);   // >>> True

        RedisResult res14 = db.JSON().Get("doc", path: "$.a[?@ in [2,4]]");
        Console.WriteLine(res14);   // >>> [2,4]

        RedisResult res15 = db.JSON().Get("doc", path: "$.a[?@ nin [2,4]]");
        Console.WriteLine(res15);   // >>> [1,3]

        RedisResult res16 = db.JSON().Get("doc", path: "$.a[?@ in $.allow]");
        Console.WriteLine(res16);   // >>> [2,3]
```

##### Go

```go
	res1, err := rdb.JSONSet(ctx, "doc", "$",
		`{"a":[1,2,3,4],"allow":[2,3]}`,
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // >>> OK

	res2, err := rdb.JSONGet(ctx, "doc", `$.a[?@ in [2,4]]`).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2) // >>> [2,4]

	res3, err := rdb.JSONGet(ctx, "doc", `$.a[?@ nin [2,4]]`).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3) // >>> [1,3]

	res4, err := rdb.JSONGet(ctx, "doc", `$.a[?@ in $.allow]`).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4) // >>> [2,3]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> filterMembershipExample = asyncCommands
                    .jsonSet("doc", JsonPath.ROOT_PATH,
                            parser.createJsonValue("{\"a\":[1,2,3,4],\"allow\":[2,3]}"))
                    .thenCompose(res1 -> {
                        System.out.println(res1); // >>> OK
                        return asyncCommands.jsonGet("doc", JsonPath.of("$.a[?@ in [2,4]]"));
                    }).thenCompose(res2 -> {
                        System.out.println(res2); // >>> [[2,4]]
                        return asyncCommands.jsonGet("doc", JsonPath.of("$.a[?@ nin [2,4]]"));
                    }).thenCompose(res3 -> {
                        System.out.println(res3); // >>> [[1,3]]
                        return asyncCommands.jsonGet("doc", JsonPath.of("$.a[?@ in $.allow]"));
                    }).thenAccept(res4 -> {
                        System.out.println(res4); // >>> [[2,3]]
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> filterMembershipExample = reactiveCommands
                    .jsonSet("doc", JsonPath.ROOT_PATH, parser.createJsonValue("{\"a\":[1,2,3,4],\"allow\":[2,3]}"))
                    .doOnNext(res1 -> {
                        System.out.println(res1); // >>> OK
                    })
                    .flatMap(res1 -> reactiveCommands.jsonGet("doc", JsonPath.of("$.a[?@ in [2,4]]")).collectList())
                    .doOnNext(res2 -> {
                        System.out.println(res2); // >>> [[2,4]]
                    })
                    .flatMap(res2 -> reactiveCommands.jsonGet("doc", JsonPath.of("$.a[?@ nin [2,4]]")).collectList())
                    .doOnNext(res3 -> {
                        System.out.println(res3); // >>> [[1,3]]
                    })
                    .flatMap(res3 -> reactiveCommands.jsonGet("doc", JsonPath.of("$.a[?@ in $.allow]")).collectList())
                    .doOnNext(res4 -> {
                        System.out.println(res4); // >>> [[2,3]]
                    })
                    .then();
```

##### Java (Synchronous - Jedis)

```java
        String res13 = jedis.jsonSet("doc", new Path2("$"), "{\"a\":[1,2,3,4],\"allow\":[2,3]}");
        System.out.println(res13);    // >>> OK

        Object res14 = jedis.jsonGet("doc", new Path2("$.a[?@ in [2,4]]"));
        System.out.println(res14);    // >>> [2,4]

        Object res15 = jedis.jsonGet("doc", new Path2("$.a[?@ nin [2,4]]"));
        System.out.println(res15);    // >>> [1,3]

        Object res16 = jedis.jsonGet("doc", new Path2("$.a[?@ in $.allow]"));
        System.out.println(res16);    // >>> [2,3]
```

##### JavaScript (Node.js)

```javascript
const res13 = await client.json.set('doc', '$', { a: [1, 2, 3, 4], allow: [2, 3] });
console.log(res13); // >>> OK

const res14 = await client.json.get('doc', { path: '$.a[?@ in [2,4]]' });
console.log(res14); // >>> [ 2, 4 ]

const res15 = await client.json.get('doc', { path: '$.a[?@ nin [2,4]]' });
console.log(res15); // >>> [ 1, 3 ]

const res16 = await client.json.get('doc', { path: '$.a[?@ in $.allow]' });
console.log(res16); // >>> [ 2, 3 ]
```

##### PHP

```php
        $res13 = $this->redis->jsonset('doc', '$', json_encode(
            ["a" => [1, 2, 3, 4], "allow" => [2, 3]]
        ));
        echo $res13 . PHP_EOL; // >>> OK

        $res14 = $this->redis->jsonget('doc', '', '', '', '$.a[?@ in [2,4]]');
        echo $res14 . PHP_EOL; // >>> [2,4]

        $res15 = $this->redis->jsonget('doc', '', '', '', '$.a[?@ nin [2,4]]');
        echo $res15 . PHP_EOL; // >>> [1,3]

        $res16 = $this->redis->jsonget('doc', '', '', '', '$.a[?@ in $.allow]');
        echo $res16 . PHP_EOL; // >>> [2,3]
```

##### Python

```python
res1 = r.json().set("doc", "$", {"a": [1, 2, 3, 4], "allow": [2, 3]})
print(res1)
# >>> True

res2 = r.json().get("doc", "$.a[?@ in [2,4]]")
print(res2)
# >>> [2, 4]

res3 = r.json().get("doc", "$.a[?@ nin [2,4]]")
print(res3)
# >>> [1, 3]

res4 = r.json().get("doc", "$.a[?@ in $.allow]")
print(res4)
# >>> [2, 3]
```

##### Ruby

```ruby
res1 = r.json_set('doc', '$', { 'a' => [1, 2, 3, 4], 'allow' => [2, 3] })
puts res1 # >>> OK

res2 = r.json_get('doc', '$.a[?@ in [2,4]]')
p res2 # >>> [2, 4]

res3 = r.json_get('doc', '$.a[?@ nin [2,4]]')
p res3 # >>> [1, 3]

res4 = r.json_get('doc', '$.a[?@ in $.allow]')
p res4 # >>> [2, 3]
```

##### Rust (Asynchronous)

```rust
        let _: bool = match r.json_set("doc", "$", &json!({"a":[1,2,3,4],"allow":[2,3]})).await {
            Ok(v) => v,
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        };

        match r.json_get("doc", "$.a[?@ in [2,4]]").await {
            Ok(res10) => {
                let res10: String = res10;
                println!("{res10}");    // >>> [2,4]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$.a[?@ nin [2,4]]").await {
            Ok(res11) => {
                let res11: String = res11;
                println!("{res11}");    // >>> [1,3]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$.a[?@ in $.allow]").await {
            Ok(res12) => {
                let res12: String = res12;
                println!("{res12}");    // >>> [2,3]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

```

##### Rust (Synchronous)

```rust
        match r.json_set("doc", "$", &json!({"a":[1,2,3,4],"allow":[2,3]})) {
            Ok(res13) => {
                let res13: bool = res13;
                println!("{}", if res13 { "OK" } else { "(nil)" });    // >>> OK
            },
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$.a[?@ in [2,4]]") {
            Ok(res14) => {
                let res14: String = res14;
                println!("{res14}");    // >>> [2,4]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$.a[?@ nin [2,4]]") {
            Ok(res15) => {
                let res15: String = res15;
                println!("{res15}");    // >>> [1,3]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$.a[?@ in $.allow]") {
            Ok(res16) => {
                let res16: String = res16;
                println!("{res16}");    // >>> [2,3]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

```



#### Set relations: `subsetof`, `anyof`, and `noneof`

These operators compare two arrays (each side can be an array literal or a path to an array):

- `subsetof` matches when every element of the left array is a member of the right array. An empty array is a subset of any array.
- `anyof` matches when the two arrays have a non-empty intersection. An empty array never matches.
- `noneof` matches when the two arrays have an empty intersection. An empty array always matches.

Set relation filters: Use subsetof, anyof, and noneof to compare two arrays when you need to match based on their overlap

**Difficulty:** Advanced

**Commands:** JSON.SET, JSON.GET

**Complexity:**
- JSON.SET: O(M+N)
- JSON.GET: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> JSON.SET doc $ '{"a":[[1,2],[1,5],[]]}'
OK
> JSON.GET doc '$.a[?@ subsetof [1,2,3]]'
"[[1,2],[]]"
> JSON.SET doc $ '{"a":[[1,9],[8,9],[]]}'
OK
> JSON.GET doc '$.a[?@ anyof [1,2,3]]'
"[[1,9]]"
> JSON.SET doc $ '{"a":[[4,5],[1,9],[]]}'
OK
> JSON.GET doc '$.a[?@ noneof [1,2,3]]'
"[[4,5],[]]"
```

##### C#

```csharp
        bool res17 = db.JSON().Set("doc", "$", "{\"a\":[[1,2],[1,5],[]]}");
        Console.WriteLine(res17);   // >>> True

        RedisResult res18 = db.JSON().Get("doc", path: "$.a[?@ subsetof [1,2,3]]");
        Console.WriteLine(res18);   // >>> [[1,2],[]]

        bool res19 = db.JSON().Set("doc", "$", "{\"a\":[[1,9],[8,9],[]]}");
        Console.WriteLine(res19);   // >>> True

        RedisResult res20 = db.JSON().Get("doc", path: "$.a[?@ anyof [1,2,3]]");
        Console.WriteLine(res20);   // >>> [[1,9]]

        bool res21 = db.JSON().Set("doc", "$", "{\"a\":[[4,5],[1,9],[]]}");
        Console.WriteLine(res21);   // >>> True

        RedisResult res22 = db.JSON().Get("doc", path: "$.a[?@ noneof [1,2,3]]");
        Console.WriteLine(res22);   // >>> [[4,5],[]]
```

##### Go

```go
	res1, err := rdb.JSONSet(ctx, "doc", "$",
		`{"a":[[1,2],[1,5],[]]}`,
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // >>> OK

	res2, err := rdb.JSONGet(ctx, "doc", `$.a[?@ subsetof [1,2,3]]`).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2) // >>> [[1,2],[]]

	res3, err := rdb.JSONSet(ctx, "doc", "$",
		`{"a":[[1,9],[8,9],[]]}`,
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3) // >>> OK

	res4, err := rdb.JSONGet(ctx, "doc", `$.a[?@ anyof [1,2,3]]`).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4) // >>> [[1,9]]

	res5, err := rdb.JSONSet(ctx, "doc", "$",
		`{"a":[[4,5],[1,9],[]]}`,
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res5) // >>> OK

	res6, err := rdb.JSONGet(ctx, "doc", `$.a[?@ noneof [1,2,3]]`).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res6) // >>> [[4,5],[]]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> filterSetRelationsExample = asyncCommands
                    .jsonSet("doc", JsonPath.ROOT_PATH, parser.createJsonValue("{\"a\":[[1,2],[1,5],[]]}"))
                    .thenCompose(res1 -> {
                        System.out.println(res1); // >>> OK
                        return asyncCommands.jsonGet("doc", JsonPath.of("$.a[?@ subsetof [1,2,3]]"));
                    }).thenCompose(res2 -> {
                        System.out.println(res2); // >>> [[[1,2],[]]]
                        return asyncCommands.jsonSet("doc", JsonPath.ROOT_PATH,
                                parser.createJsonValue("{\"a\":[[1,9],[8,9],[]]}"));
                    }).thenCompose(res3 -> {
                        System.out.println(res3); // >>> OK
                        return asyncCommands.jsonGet("doc", JsonPath.of("$.a[?@ anyof [1,2,3]]"));
                    }).thenCompose(res4 -> {
                        System.out.println(res4); // >>> [[[1,9]]]
                        return asyncCommands.jsonSet("doc", JsonPath.ROOT_PATH,
                                parser.createJsonValue("{\"a\":[[4,5],[1,9],[]]}"));
                    }).thenCompose(res5 -> {
                        System.out.println(res5); // >>> OK
                        return asyncCommands.jsonGet("doc", JsonPath.of("$.a[?@ noneof [1,2,3]]"));
                    }).thenAccept(res6 -> {
                        System.out.println(res6); // >>> [[[4,5],[]]]
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> filterSetRelationsExample = reactiveCommands
                    .jsonSet("doc", JsonPath.ROOT_PATH, parser.createJsonValue("{\"a\":[[1,2],[1,5],[]]}"))
                    .doOnNext(res1 -> {
                        System.out.println(res1); // >>> OK
                    })
                    .flatMap(res1 -> reactiveCommands.jsonGet("doc", JsonPath.of("$.a[?@ subsetof [1,2,3]]")).collectList())
                    .doOnNext(res2 -> {
                        System.out.println(res2); // >>> [[[1,2],[]]]
                    })
                    .flatMap(res2 -> reactiveCommands.jsonSet("doc", JsonPath.ROOT_PATH,
                            parser.createJsonValue("{\"a\":[[1,9],[8,9],[]]}")))
                    .doOnNext(res3 -> {
                        System.out.println(res3); // >>> OK
                    })
                    .flatMap(res3 -> reactiveCommands.jsonGet("doc", JsonPath.of("$.a[?@ anyof [1,2,3]]")).collectList())
                    .doOnNext(res4 -> {
                        System.out.println(res4); // >>> [[[1,9]]]
                    })
                    .flatMap(res4 -> reactiveCommands.jsonSet("doc", JsonPath.ROOT_PATH,
                            parser.createJsonValue("{\"a\":[[4,5],[1,9],[]]}")))
                    .doOnNext(res5 -> {
                        System.out.println(res5); // >>> OK
                    })
                    .flatMap(res5 -> reactiveCommands.jsonGet("doc", JsonPath.of("$.a[?@ noneof [1,2,3]]")).collectList())
                    .doOnNext(res6 -> {
                        System.out.println(res6); // >>> [[[4,5],[]]]
                    })
                    .then();
```

##### Java (Synchronous - Jedis)

```java
        String res17 = jedis.jsonSet("doc", new Path2("$"), "{\"a\":[[1,2],[1,5],[]]}");
        System.out.println(res17);    // >>> OK

        Object res18 = jedis.jsonGet("doc", new Path2("$.a[?@ subsetof [1,2,3]]"));
        System.out.println(res18);    // >>> [[1,2],[]]

        String res19 = jedis.jsonSet("doc", new Path2("$"), "{\"a\":[[1,9],[8,9],[]]}");
        System.out.println(res19);    // >>> OK

        Object res20 = jedis.jsonGet("doc", new Path2("$.a[?@ anyof [1,2,3]]"));
        System.out.println(res20);    // >>> [[1,9]]

        String res21 = jedis.jsonSet("doc", new Path2("$"), "{\"a\":[[4,5],[1,9],[]]}");
        System.out.println(res21);    // >>> OK

        Object res22 = jedis.jsonGet("doc", new Path2("$.a[?@ noneof [1,2,3]]"));
        System.out.println(res22);    // >>> [[4,5],[]]
```

##### JavaScript (Node.js)

```javascript
const res17 = await client.json.set('doc', '$', { a: [[1, 2], [1, 5], []] });
console.log(res17); // >>> OK

const res18 = await client.json.get('doc', { path: '$.a[?@ subsetof [1,2,3]]' });
console.log(res18); // >>> [ [ 1, 2 ], [] ]

const res19 = await client.json.set('doc', '$', { a: [[1, 9], [8, 9], []] });
console.log(res19); // >>> OK

const res20 = await client.json.get('doc', { path: '$.a[?@ anyof [1,2,3]]' });
console.log(res20); // >>> [ [ 1, 9 ] ]

const res21 = await client.json.set('doc', '$', { a: [[4, 5], [1, 9], []] });
console.log(res21); // >>> OK

const res22 = await client.json.get('doc', { path: '$.a[?@ noneof [1,2,3]]' });
console.log(res22); // >>> [ [ 4, 5 ], [] ]
```

##### PHP

```php
        $res17 = $this->redis->jsonset('doc', '$', json_encode(
            ["a" => [[1, 2], [1, 5], []]]
        ));
        echo $res17 . PHP_EOL; // >>> OK

        $res18 = $this->redis->jsonget('doc', '', '', '', '$.a[?@ subsetof [1,2,3]]');
        echo $res18 . PHP_EOL; // >>> [[1,2],[]]

        $res19 = $this->redis->jsonset('doc', '$', json_encode(
            ["a" => [[1, 9], [8, 9], []]]
        ));
        echo $res19 . PHP_EOL; // >>> OK

        $res20 = $this->redis->jsonget('doc', '', '', '', '$.a[?@ anyof [1,2,3]]');
        echo $res20 . PHP_EOL; // >>> [[1,9]]

        $res21 = $this->redis->jsonset('doc', '$', json_encode(
            ["a" => [[4, 5], [1, 9], []]]
        ));
        echo $res21 . PHP_EOL; // >>> OK

        $res22 = $this->redis->jsonget('doc', '', '', '', '$.a[?@ noneof [1,2,3]]');
        echo $res22 . PHP_EOL; // >>> [[4,5],[]]
```

##### Python

```python
res1 = r.json().set("doc", "$", {"a": [[1, 2], [1, 5], []]})
print(res1)
# >>> True

res2 = r.json().get("doc", "$.a[?@ subsetof [1,2,3]]")
print(res2)
# >>> [[1, 2], []]

res3 = r.json().set("doc", "$", {"a": [[1, 9], [8, 9], []]})
print(res3)
# >>> True

res4 = r.json().get("doc", "$.a[?@ anyof [1,2,3]]")
print(res4)
# >>> [[1, 9]]

res5 = r.json().set("doc", "$", {"a": [[4, 5], [1, 9], []]})
print(res5)
# >>> True

res6 = r.json().get("doc", "$.a[?@ noneof [1,2,3]]")
print(res6)
# >>> [[4, 5], []]
```

##### Ruby

```ruby
res1 = r.json_set('doc', '$', { 'a' => [[1, 2], [1, 5], []] })
puts res1 # >>> OK

res2 = r.json_get('doc', '$.a[?@ subsetof [1,2,3]]')
p res2 # >>> [[1, 2], []]

res3 = r.json_set('doc', '$', { 'a' => [[1, 9], [8, 9], []] })
puts res3 # >>> OK

res4 = r.json_get('doc', '$.a[?@ anyof [1,2,3]]')
p res4 # >>> [[1, 9]]

res5 = r.json_set('doc', '$', { 'a' => [[4, 5], [1, 9], []] })
puts res5 # >>> OK

res6 = r.json_get('doc', '$.a[?@ noneof [1,2,3]]')
p res6 # >>> [[4, 5], []]
```

##### Rust (Asynchronous)

```rust
        let _: bool = match r.json_set("doc", "$", &json!({"a":[[1,2],[1,5],[]]})).await {
            Ok(v) => v,
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        };

        match r.json_get("doc", "$.a[?@ subsetof [1,2,3]]").await {
            Ok(res13) => {
                let res13: String = res13;
                println!("{res13}");    // >>> [[1,2],[]]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        let _: bool = match r.json_set("doc", "$", &json!({"a":[[1,9],[8,9],[]]})).await {
            Ok(v) => v,
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        };

        match r.json_get("doc", "$.a[?@ anyof [1,2,3]]").await {
            Ok(res14) => {
                let res14: String = res14;
                println!("{res14}");    // >>> [[1,9]]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        let _: bool = match r.json_set("doc", "$", &json!({"a":[[4,5],[1,9],[]]})).await {
            Ok(v) => v,
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        };

        match r.json_get("doc", "$.a[?@ noneof [1,2,3]]").await {
            Ok(res15) => {
                let res15: String = res15;
                println!("{res15}");    // >>> [[4,5],[]]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

```

##### Rust (Synchronous)

```rust
        match r.json_set("doc", "$", &json!({"a":[[1,2],[1,5],[]]})) {
            Ok(res17) => {
                let res17: bool = res17;
                println!("{}", if res17 { "OK" } else { "(nil)" });    // >>> OK
            },
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$.a[?@ subsetof [1,2,3]]") {
            Ok(res18) => {
                let res18: String = res18;
                println!("{res18}");    // >>> [[1,2],[]]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_set("doc", "$", &json!({"a":[[1,9],[8,9],[]]})) {
            Ok(res19) => {
                let res19: bool = res19;
                println!("{}", if res19 { "OK" } else { "(nil)" });    // >>> OK
            },
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$.a[?@ anyof [1,2,3]]") {
            Ok(res20) => {
                let res20: String = res20;
                println!("{res20}");    // >>> [[1,9]]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_set("doc", "$", &json!({"a":[[4,5],[1,9],[]]})) {
            Ok(res21) => {
                let res21: bool = res21;
                println!("{}", if res21 { "OK" } else { "(nil)" });    // >>> OK
            },
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$.a[?@ noneof [1,2,3]]") {
            Ok(res22) => {
                let res22: String = res22;
                println!("{res22}");    // >>> [[4,5],[]]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

```



#### `size` (`sizeof`) and `empty`

`left sizeof n` matches when the size of `left` equals the integer `n`, where size is the number of characters in a string, the number of elements in an array, or the number of members in an object. A non-integer `n` is truncated toward zero; a non-numeric `n` never matches. `size` is an alias for `sizeof`.

`left empty true` matches an empty string, array, or object; `left empty false` matches a non-empty one.

Size and emptiness filters: Use sizeof and empty to filter by the size or emptiness of a string, array, or object

**Difficulty:** Advanced

**Commands:** JSON.SET, JSON.GET

**Complexity:**
- JSON.SET: O(M+N)
- JSON.GET: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> JSON.SET doc $ '{"a":[[4,5],[1],[7,8,9]]}'
OK
> JSON.GET doc '$.a[?@ sizeof 2]'
"[[4,5]]"
> JSON.SET doc $ '{"a":[[],[1],"",[2,3],{},{"k":1}]}'
OK
> JSON.GET doc '$.a[?@ empty true]'
"[[],\"\",{}]"
> JSON.GET doc '$.a[?@ empty false]'
"[[1],[2,3],{\"k\":1}]"
```

##### C#

```csharp
        bool res23 = db.JSON().Set("doc", "$", "{\"a\":[[4,5],[1],[7,8,9]]}");
        Console.WriteLine(res23);   // >>> True

        RedisResult res24 = db.JSON().Get("doc", path: "$.a[?@ sizeof 2]");
        Console.WriteLine(res24);   // >>> [[4,5]]

        bool res25 = db.JSON().Set("doc", "$", "{\"a\":[[],[1],\"\",[2,3],{},{\"k\":1}]}");
        Console.WriteLine(res25);   // >>> True

        RedisResult res26 = db.JSON().Get("doc", path: "$.a[?@ empty true]");
        Console.WriteLine(res26);   // >>> [[],"",{}]

        RedisResult res27 = db.JSON().Get("doc", path: "$.a[?@ empty false]");
        Console.WriteLine(res27);   // >>> [[1],[2,3],{"k":1}]
```

##### Go

```go
	res1, err := rdb.JSONSet(ctx, "doc", "$",
		`{"a":[[4,5],[1],[7,8,9]]}`,
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // >>> OK

	res2, err := rdb.JSONGet(ctx, "doc", `$.a[?@ sizeof 2]`).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2) // >>> [[4,5]]

	res3, err := rdb.JSONSet(ctx, "doc", "$",
		`{"a":[[],[1],"",[2,3],{},{"k":1}]}`,
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3) // >>> OK

	res4, err := rdb.JSONGet(ctx, "doc", `$.a[?@ empty true]`).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4) // >>> [[],"",{}]

	res5, err := rdb.JSONGet(ctx, "doc", `$.a[?@ empty false]`).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res5) // >>> [[1],[2,3],{"k":1}]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> filterSizeEmptyExample = asyncCommands
                    .jsonSet("doc", JsonPath.ROOT_PATH, parser.createJsonValue("{\"a\":[[4,5],[1],[7,8,9]]}"))
                    .thenCompose(res1 -> {
                        System.out.println(res1); // >>> OK
                        return asyncCommands.jsonGet("doc", JsonPath.of("$.a[?@ sizeof 2]"));
                    }).thenCompose(res2 -> {
                        System.out.println(res2); // >>> [[[4,5]]]
                        return asyncCommands.jsonSet("doc", JsonPath.ROOT_PATH,
                                parser.createJsonValue("{\"a\":[[],[1],\"\",[2,3],{},{\"k\":1}]}"));
                    }).thenCompose(res3 -> {
                        System.out.println(res3); // >>> OK
                        return asyncCommands.jsonGet("doc", JsonPath.of("$.a[?@ empty true]"));
                    }).thenCompose(res4 -> {
                        System.out.println(res4); // >>> [[[],"",{}]]
                        return asyncCommands.jsonGet("doc", JsonPath.of("$.a[?@ empty false]"));
                    }).thenAccept(res5 -> {
                        System.out.println(res5); // >>> [[[1],[2,3],{"k":1}]]
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> filterSizeEmptyExample = reactiveCommands
                    .jsonSet("doc", JsonPath.ROOT_PATH, parser.createJsonValue("{\"a\":[[4,5],[1],[7,8,9]]}"))
                    .doOnNext(res1 -> {
                        System.out.println(res1); // >>> OK
                    })
                    .flatMap(res1 -> reactiveCommands.jsonGet("doc", JsonPath.of("$.a[?@ sizeof 2]")).collectList())
                    .doOnNext(res2 -> {
                        System.out.println(res2); // >>> [[[4,5]]]
                    })
                    .flatMap(res2 -> reactiveCommands.jsonSet("doc", JsonPath.ROOT_PATH,
                            parser.createJsonValue("{\"a\":[[],[1],\"\",[2,3],{},{\"k\":1}]}")))
                    .doOnNext(res3 -> {
                        System.out.println(res3); // >>> OK
                    })
                    .flatMap(res3 -> reactiveCommands.jsonGet("doc", JsonPath.of("$.a[?@ empty true]")).collectList())
                    .doOnNext(res4 -> {
                        System.out.println(res4); // >>> [[[],"",{}]]
                    })
                    .flatMap(res4 -> reactiveCommands.jsonGet("doc", JsonPath.of("$.a[?@ empty false]")).collectList())
                    .doOnNext(res5 -> {
                        System.out.println(res5); // >>> [[[1],[2,3],{"k":1}]]
                    })
                    .then();
```

##### Java (Synchronous - Jedis)

```java
        String res23 = jedis.jsonSet("doc", new Path2("$"), "{\"a\":[[4,5],[1],[7,8,9]]}");
        System.out.println(res23);    // >>> OK

        Object res24 = jedis.jsonGet("doc", new Path2("$.a[?@ sizeof 2]"));
        System.out.println(res24);    // >>> [[4,5]]

        String res25 = jedis.jsonSet("doc", new Path2("$"), "{\"a\":[[],[1],\"\",[2,3],{},{\"k\":1}]}");
        System.out.println(res25);    // >>> OK

        Object res26 = jedis.jsonGet("doc", new Path2("$.a[?@ empty true]"));
        System.out.println(res26);    // >>> [[],"",{}]

        Object res27 = jedis.jsonGet("doc", new Path2("$.a[?@ empty false]"));
        System.out.println(res27);    // >>> [[1],[2,3],{"k":1}]
```

##### JavaScript (Node.js)

```javascript
const res23 = await client.json.set('doc', '$', { a: [[4, 5], [1], [7, 8, 9]] });
console.log(res23); // >>> OK

const res24 = await client.json.get('doc', { path: '$.a[?@ sizeof 2]' });
console.log(res24); // >>> [ [ 4, 5 ] ]

const res25 = await client.json.set('doc', '$', { a: [[], [1], '', [2, 3], {}, { k: 1 }] });
console.log(res25); // >>> OK

const res26 = await client.json.get('doc', { path: '$.a[?@ empty true]' });
console.log(res26); // >>> [ [], '', {} ]

const res27 = await client.json.get('doc', { path: '$.a[?@ empty false]' });
console.log(res27); // >>> [ [ 1 ], [ 2, 3 ], { k: 1 } ]
```

##### PHP

```php
        $res23 = $this->redis->jsonset('doc', '$', json_encode(
            ["a" => [[4, 5], [1], [7, 8, 9]]]
        ));
        echo $res23 . PHP_EOL; // >>> OK

        $res24 = $this->redis->jsonget('doc', '', '', '', '$.a[?@ sizeof 2]');
        echo $res24 . PHP_EOL; // >>> [[4,5]]

        $res25 = $this->redis->jsonset('doc', '$', json_encode(
            ["a" => [[], [1], "", [2, 3], new \stdClass(), ["k" => 1]]]
        ));
        echo $res25 . PHP_EOL; // >>> OK

        $res26 = $this->redis->jsonget('doc', '', '', '', '$.a[?@ empty true]');
        echo $res26 . PHP_EOL; // >>> [[],"",{}]

        $res27 = $this->redis->jsonget('doc', '', '', '', '$.a[?@ empty false]');
        echo $res27 . PHP_EOL; // >>> [[1],[2,3],{"k":1}]
```

##### Python

```python
res1 = r.json().set("doc", "$", {"a": [[4, 5], [1], [7, 8, 9]]})
print(res1)
# >>> True

res2 = r.json().get("doc", "$.a[?@ sizeof 2]")
print(res2)
# >>> [[4, 5]]

res3 = r.json().set("doc", "$", {"a": [[], [1], "", [2, 3], {}, {"k": 1}]})
print(res3)
# >>> True

res4 = r.json().get("doc", "$.a[?@ empty true]")
print(res4)
# >>> [[], '', {}]

res5 = r.json().get("doc", "$.a[?@ empty false]")
print(res5)
# >>> [[1], [2, 3], {'k': 1}]
```

##### Ruby

```ruby
res1 = r.json_set('doc', '$', { 'a' => [[4, 5], [1], [7, 8, 9]] })
puts res1 # >>> OK

res2 = r.json_get('doc', '$.a[?@ sizeof 2]')
p res2 # >>> [[4, 5]]

res3 = r.json_set('doc', '$', { 'a' => [[], [1], '', [2, 3], {}, { 'k' => 1 }] })
puts res3 # >>> OK

res4 = r.json_get('doc', '$.a[?@ empty true]')
p res4 # >>> [[], "", {}]

res5 = r.json_get('doc', '$.a[?@ empty false]')
p res5 # >>> [[1], [2, 3], {"k"=>1}]
```

##### Rust (Asynchronous)

```rust
        let _: bool = match r.json_set("doc", "$", &json!({"a":[[4,5],[1],[7,8,9]]})).await {
            Ok(v) => v,
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        };

        match r.json_get("doc", "$.a[?@ sizeof 2]").await {
            Ok(res16) => {
                let res16: String = res16;
                println!("{res16}");    // >>> [[4,5]]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        let _: bool = match r.json_set("doc", "$", &json!({"a":[[],[1],"",[2,3],{},{"k":1}]})).await {
            Ok(v) => v,
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        };

        match r.json_get("doc", "$.a[?@ empty true]").await {
            Ok(res17) => {
                let res17: String = res17;
                println!("{res17}");    // >>> [[],"",{}]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$.a[?@ empty false]").await {
            Ok(res18) => {
                let res18: String = res18;
                println!("{res18}");    // >>> [[1],[2,3],{"k":1}]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

```

##### Rust (Synchronous)

```rust
        match r.json_set("doc", "$", &json!({"a":[[4,5],[1],[7,8,9]]})) {
            Ok(res23) => {
                let res23: bool = res23;
                println!("{}", if res23 { "OK" } else { "(nil)" });    // >>> OK
            },
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$.a[?@ sizeof 2]") {
            Ok(res24) => {
                let res24: String = res24;
                println!("{res24}");    // >>> [[4,5]]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_set("doc", "$", &json!({"a":[[],[1],"",[2,3],{},{"k":1}]})) {
            Ok(res25) => {
                let res25: bool = res25;
                println!("{}", if res25 { "OK" } else { "(nil)" });    // >>> OK
            },
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$.a[?@ empty true]") {
            Ok(res26) => {
                let res26: String = res26;
                println!("{res26}");    // >>> [[],"",{}]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$.a[?@ empty false]") {
            Ok(res27) => {
                let res27: String = res27;
                println!("{res27}");    // >>> [[1],[2,3],{"k":1}]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

```



#### Get-keys operator `~`

The terminal `~` operator returns the member names of an object as a flat list of strings. Applied to the root (`$~`), it returns the top-level keys. Applied to a multiple-match receiver, it flattens the keys of every matched object. A non-object receiver contributes no keys.

Because `~` is terminal, expressions such as `$.obj~.x`, `$.obj~~`, and `$.obj.keys()~` are parse errors. For a composable alternative that can be chained with other functions, use the [`keys()`](#keys) function.

Get-keys filter: Use the ~ operator to retrieve an object's member names as a list of strings

**Difficulty:** Advanced

**Commands:** JSON.SET, JSON.GET

**Complexity:**
- JSON.SET: O(M+N)
- JSON.GET: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> JSON.SET doc $ '{"obj":{"x":1,"y":2},"books":[{"t":"a"},{"t":"b"}]}'
OK
> JSON.GET doc '$.obj~'
"[\"x\",\"y\"]"
> JSON.GET doc '$~'
"[\"obj\",\"books\"]"
> JSON.GET doc '$.books~'
"[]"
```

##### C#

```csharp
        bool res28 = db.JSON().Set(
            "doc",
            "$",
            "{\"obj\":{\"x\":1,\"y\":2},\"books\":[{\"t\":\"a\"},{\"t\":\"b\"}]}"
        );
        Console.WriteLine(res28);   // >>> True

        RedisResult res29 = db.JSON().Get("doc", path: "$.obj~");
        Console.WriteLine(res29);   // >>> ["x","y"]

        RedisResult res30 = db.JSON().Get("doc", path: "$~");
        Console.WriteLine(res30);   // >>> ["obj","books"]

        RedisResult res31 = db.JSON().Get("doc", path: "$.books~");
        Console.WriteLine(res31);   // >>> []
```

##### Go

```go
	res1, err := rdb.JSONSet(ctx, "doc", "$",
		`{"obj":{"x":1,"y":2},"books":[{"t":"a"},{"t":"b"}]}`,
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // >>> OK

	res2, err := rdb.JSONGet(ctx, "doc", `$.obj~`).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2) // >>> ["x","y"]

	res3, err := rdb.JSONGet(ctx, "doc", `$~`).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3) // >>> ["obj","books"]

	res4, err := rdb.JSONGet(ctx, "doc", `$.books~`).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4) // >>> []
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> filterGetkeysExample = asyncCommands
                    .jsonSet("doc", JsonPath.ROOT_PATH,
                            parser.createJsonValue(
                                    "{\"obj\":{\"x\":1,\"y\":2},\"books\":[{\"t\":\"a\"},{\"t\":\"b\"}]}"))
                    .thenCompose(res1 -> {
                        System.out.println(res1); // >>> OK
                        return asyncCommands.jsonGet("doc", JsonPath.of("$.obj~"));
                    }).thenCompose(res2 -> {
                        System.out.println(res2); // >>> [["x","y"]]
                        return asyncCommands.jsonGet("doc", JsonPath.of("$~"));
                    }).thenCompose(res3 -> {
                        System.out.println(res3); // >>> [["obj","books"]]
                        return asyncCommands.jsonGet("doc", JsonPath.of("$.books~"));
                    }).thenAccept(res4 -> {
                        System.out.println(res4); // >>> [[]]
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> filterGetkeysExample = reactiveCommands
                    .jsonSet("doc", JsonPath.ROOT_PATH,
                            parser.createJsonValue("{\"obj\":{\"x\":1,\"y\":2},\"books\":[{\"t\":\"a\"},{\"t\":\"b\"}]}"))
                    .doOnNext(res1 -> {
                        System.out.println(res1); // >>> OK
                    })
                    .flatMap(res1 -> reactiveCommands.jsonGet("doc", JsonPath.of("$.obj~")).collectList())
                    .doOnNext(res2 -> {
                        System.out.println(res2); // >>> [["x","y"]]
                    })
                    .flatMap(res2 -> reactiveCommands.jsonGet("doc", JsonPath.of("$~")).collectList())
                    .doOnNext(res3 -> {
                        System.out.println(res3); // >>> [["obj","books"]]
                    })
                    .flatMap(res3 -> reactiveCommands.jsonGet("doc", JsonPath.of("$.books~")).collectList())
                    .doOnNext(res4 -> {
                        System.out.println(res4); // >>> [[]]
                    })
                    .then();
```

##### Java (Synchronous - Jedis)

```java
        String res28 = jedis.jsonSet(
            "doc",
            new Path2("$"),
            "{\"obj\":{\"x\":1,\"y\":2},\"books\":[{\"t\":\"a\"},{\"t\":\"b\"}]}"
        );
        System.out.println(res28);    // >>> OK

        Object res29 = jedis.jsonGet("doc", new Path2("$.obj~"));
        System.out.println(res29);    // >>> ["x","y"]

        Object res30 = jedis.jsonGet("doc", new Path2("$~"));
        System.out.println(res30);    // >>> ["obj","books"]

        Object res31 = jedis.jsonGet("doc", new Path2("$.books~"));
        System.out.println(res31);    // >>> []
```

##### JavaScript (Node.js)

```javascript
const res28 = await client.json.set('doc', '$', {
  obj: { x: 1, y: 2 },
  books: [{ t: 'a' }, { t: 'b' }]
});
console.log(res28); // >>> OK

const res29 = await client.json.get('doc', { path: '$.obj~' });
console.log(res29); // >>> [ 'x', 'y' ]

const res30 = await client.json.get('doc', { path: '$~' });
console.log(res30); // >>> [ 'obj', 'books' ]

const res31 = await client.json.get('doc', { path: '$.books~' });
console.log(res31); // >>> []
```

##### PHP

```php
        $res28 = $this->redis->jsonset('doc', '$', json_encode([
            "obj" => ["x" => 1, "y" => 2],
            "books" => [["t" => "a"], ["t" => "b"]],
        ]));
        echo $res28 . PHP_EOL; // >>> OK

        $res29 = $this->redis->jsonget('doc', '', '', '', '$.obj~');
        echo $res29 . PHP_EOL; // >>> ["x","y"]

        $res30 = $this->redis->jsonget('doc', '', '', '', '$~');
        echo $res30 . PHP_EOL; // >>> ["obj","books"]

        $res31 = $this->redis->jsonget('doc', '', '', '', '$.books~');
        echo $res31 . PHP_EOL; // >>> []
```

##### Python

```python
res1 = r.json().set("doc", "$", {"obj": {"x": 1, "y": 2}, "books": [{"t": "a"}, {"t": "b"}]})
print(res1)
# >>> True

res2 = r.json().get("doc", "$.obj~")
print(res2)
# >>> ['x', 'y']

res3 = r.json().get("doc", "$~")
print(res3)
# >>> ['obj', 'books']

res4 = r.json().get("doc", "$.books~")
print(res4)
# >>> []
```

##### Ruby

```ruby
res1 = r.json_set('doc', '$', { 'obj' => { 'x' => 1, 'y' => 2 }, 'books' => [{ 't' => 'a' }, { 't' => 'b' }] })
puts res1 # >>> OK

res2 = r.json_get('doc', '$.obj~')
p res2 # >>> ["x", "y"]

res3 = r.json_get('doc', '$~')
p res3 # >>> ["obj", "books"]

res4 = r.json_get('doc', '$.books~')
p res4 # >>> []
```

##### Rust (Asynchronous)

```rust
        let _: bool = match r.json_set(
            "doc",
            "$",
            &json!({"obj":{"x":1,"y":2},"books":[{"t":"a"},{"t":"b"}]}),
        ).await {
            Ok(v) => v,
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        };

        match r.json_get("doc", "$.obj~").await {
            Ok(res19) => {
                let res19: String = res19;
                println!("{res19}");    // >>> ["x","y"]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$~").await {
            Ok(res20) => {
                let res20: String = res20;
                println!("{res20}");    // >>> ["obj","books"]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$.books~").await {
            Ok(res21) => {
                let res21: String = res21;
                println!("{res21}");    // >>> []
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

```

##### Rust (Synchronous)

```rust
        match r.json_set(
            "doc",
            "$",
            &json!({"obj":{"x":1,"y":2},"books":[{"t":"a"},{"t":"b"}]}),
        ) {
            Ok(res28) => {
                let res28: bool = res28;
                println!("{}", if res28 { "OK" } else { "(nil)" });    // >>> OK
            },
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$.obj~") {
            Ok(res29) => {
                let res29: String = res29;
                println!("{res29}");    // >>> ["x","y"]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$~") {
            Ok(res30) => {
                let res30: String = res30;
                println!("{res30}");    // >>> ["obj","books"]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$.books~") {
            Ok(res31) => {
                let res31: String = res31;
                println!("{res31}");    // >>> []
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

```



Functions can appear inside filter expressions and, when they return a value, as top-level [projection expressions](#projection-expressions). Beginning with Redis 8.10, JSONPath supports the following functions.

#### `length()`

Returns the number of characters in a string, elements in an array, or members in an object. Any other type produces *Nothing*.

Length function: Use length() to get the number of characters in a string, elements in an array, or members in an object

**Difficulty:** Advanced

**Commands:** JSON.SET, JSON.GET

**Complexity:**
- JSON.SET: O(M+N)
- JSON.GET: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> JSON.SET doc $ '{"a":[[1,2,3],[1],"abcd","x"]}'
OK
> JSON.GET doc '$.a[?length(@) > 2]'
"[[1,2,3],\"abcd\"]"
```

##### C#

```csharp
        bool res32 = db.JSON().Set("doc", "$", "{\"a\":[[1,2,3],[1],\"abcd\",\"x\"]}");
        Console.WriteLine(res32);   // >>> True

        RedisResult res33 = db.JSON().Get("doc", path: "$.a[?length(@) > 2]");
        Console.WriteLine(res33);   // >>> [[1,2,3],"abcd"]
```

##### Go

```go
	res1, err := rdb.JSONSet(ctx, "doc", "$",
		`{"a":[[1,2,3],[1],"abcd","x"]}`,
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // >>> OK

	res2, err := rdb.JSONGet(ctx, "doc", `$.a[?length(@) > 2]`).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2) // >>> [[1,2,3],"abcd"]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> funcLengthExample = asyncCommands
                    .jsonSet("doc", JsonPath.ROOT_PATH,
                            parser.createJsonValue("{\"a\":[[1,2,3],[1],\"abcd\",\"x\"]}"))
                    .thenCompose(res1 -> {
                        System.out.println(res1); // >>> OK
                        return asyncCommands.jsonGet("doc", JsonPath.of("$.a[?length(@) > 2]"));
                    }).thenAccept(res2 -> {
                        System.out.println(res2); // >>> [[[1,2,3],"abcd"]]
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> funcLengthExample = reactiveCommands
                    .jsonSet("doc", JsonPath.ROOT_PATH,
                            parser.createJsonValue("{\"a\":[[1,2,3],[1],\"abcd\",\"x\"]}"))
                    .doOnNext(res1 -> {
                        System.out.println(res1); // >>> OK
                    })
                    .flatMap(res1 -> reactiveCommands.jsonGet("doc", JsonPath.of("$.a[?length(@) > 2]")).collectList())
                    .doOnNext(res2 -> {
                        System.out.println(res2); // >>> [[[1,2,3],"abcd"]]
                    })
                    .then();
```

##### Java (Synchronous - Jedis)

```java
        String res32 = jedis.jsonSet("doc", new Path2("$"), "{\"a\":[[1,2,3],[1],\"abcd\",\"x\"]}");
        System.out.println(res32);    // >>> OK

        Object res33 = jedis.jsonGet("doc", new Path2("$.a[?length(@) > 2]"));
        System.out.println(res33);    // >>> [[1,2,3],"abcd"]
```

##### JavaScript (Node.js)

```javascript
const res32 = await client.json.set('doc', '$', { a: [[1, 2, 3], [1], 'abcd', 'x'] });
console.log(res32); // >>> OK

const res33 = await client.json.get('doc', { path: '$.a[?length(@) > 2]' });
console.log(res33); // >>> [ [ 1, 2, 3 ], 'abcd' ]
```

##### PHP

```php
        $res32 = $this->redis->jsonset('doc', '$', json_encode(
            ["a" => [[1, 2, 3], [1], "abcd", "x"]]
        ));
        echo $res32 . PHP_EOL; // >>> OK

        $res33 = $this->redis->jsonget('doc', '', '', '', '$.a[?length(@) > 2]');
        echo $res33 . PHP_EOL; // >>> [[1,2,3],"abcd"]
```

##### Python

```python
res1 = r.json().set("doc", "$", {"a": [[1, 2, 3], [1], "abcd", "x"]})
print(res1)
# >>> True

res2 = r.json().get("doc", "$.a[?length(@) > 2]")
print(res2)
# >>> [[1, 2, 3], 'abcd']
```

##### Ruby

```ruby
res1 = r.json_set('doc', '$', { 'a' => [[1, 2, 3], [1], 'abcd', 'x'] })
puts res1 # >>> OK

res2 = r.json_get('doc', '$.a[?length(@) > 2]')
p res2 # >>> [[1, 2, 3], "abcd"]
```

##### Rust (Asynchronous)

```rust
        let _: bool = match r.json_set("doc", "$", &json!({"a":[[1,2,3],[1],"abcd","x"]})).await {
            Ok(v) => v,
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        };

        match r.json_get("doc", "$.a[?length(@) > 2]").await {
            Ok(res1) => {
                let res1: String = res1;
                println!("{res1}");    // >>> [[1,2,3],"abcd"]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

```

##### Rust (Synchronous)

```rust
        match r.json_set("doc", "$", &json!({"a":[[1,2,3],[1],"abcd","x"]})) {
            Ok(res32) => {
                let res32: bool = res32;
                println!("{}", if res32 { "OK" } else { "(nil)" });    // >>> OK
            },
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$.a[?length(@) > 2]") {
            Ok(res33) => {
                let res33: String = res33;
                println!("{res33}");    // >>> [[1,2,3],"abcd"]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

```



#### `count()`

Returns the number of nodes selected by a query. An absent path counts as `0`; a single node counts as `1`.

Count function: Use count() to get the number of nodes selected by a query

**Difficulty:** Advanced

**Commands:** JSON.SET, JSON.GET

**Complexity:**
- JSON.SET: O(M+N)
- JSON.GET: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> JSON.SET doc $ '[{"a":1,"b":2,"c":3},{"a":1}]'
OK
> JSON.GET doc '$[?count(@.*) == 3]'
"[{\"a\":1,\"b\":2,\"c\":3}]"
```

##### C#

```csharp
        bool res34 = db.JSON().Set("doc", "$", "[{\"a\":1,\"b\":2,\"c\":3},{\"a\":1}]");
        Console.WriteLine(res34);   // >>> True

        RedisResult res35 = db.JSON().Get("doc", path: "$[?count(@.*) == 3]");
        Console.WriteLine(res35);   // >>> [{"a":1,"b":2,"c":3}]
```

##### Go

```go
	res1, err := rdb.JSONSet(ctx, "doc", "$",
		`[{"a":1,"b":2,"c":3},{"a":1}]`,
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // >>> OK

	res2, err := rdb.JSONGet(ctx, "doc", `$[?count(@.*) == 3]`).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2) // >>> [{"a":1,"b":2,"c":3}]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> funcCountExample = asyncCommands
                    .jsonSet("doc", JsonPath.ROOT_PATH,
                            parser.createJsonValue("[{\"a\":1,\"b\":2,\"c\":3},{\"a\":1}]"))
                    .thenCompose(res1 -> {
                        System.out.println(res1); // >>> OK
                        return asyncCommands.jsonGet("doc", JsonPath.of("$[?count(@.*) == 3]"));
                    }).thenAccept(res2 -> {
                        System.out.println(res2); // >>> [[{"a":1,"b":2,"c":3}]]
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> funcCountExample = reactiveCommands
                    .jsonSet("doc", JsonPath.ROOT_PATH, parser.createJsonValue("[{\"a\":1,\"b\":2,\"c\":3},{\"a\":1}]"))
                    .doOnNext(res1 -> {
                        System.out.println(res1); // >>> OK
                    })
                    .flatMap(res1 -> reactiveCommands.jsonGet("doc", JsonPath.of("$[?count(@.*) == 3]")).collectList())
                    .doOnNext(res2 -> {
                        System.out.println(res2); // >>> [[{"a":1,"b":2,"c":3}]]
                    })
                    .then();
```

##### Java (Synchronous - Jedis)

```java
        String res34 = jedis.jsonSet("doc", new Path2("$"), "[{\"a\":1,\"b\":2,\"c\":3},{\"a\":1}]");
        System.out.println(res34);    // >>> OK

        Object res35 = jedis.jsonGet("doc", new Path2("$[?count(@.*) == 3]"));
        System.out.println(res35);    // >>> [{"a":1,"b":2,"c":3}]
```

##### JavaScript (Node.js)

```javascript
const res34 = await client.json.set('doc', '$', [{ a: 1, b: 2, c: 3 }, { a: 1 }]);
console.log(res34); // >>> OK

const res35 = await client.json.get('doc', { path: '$[?count(@.*) == 3]' });
console.log(res35); // >>> [ { a: 1, b: 2, c: 3 } ]
```

##### PHP

```php
        $res34 = $this->redis->jsonset('doc', '$', json_encode(
            [["a" => 1, "b" => 2, "c" => 3], ["a" => 1]]
        ));
        echo $res34 . PHP_EOL; // >>> OK

        $res35 = $this->redis->jsonget('doc', '', '', '', '$[?count(@.*) == 3]');
        echo $res35 . PHP_EOL; // >>> [{"a":1,"b":2,"c":3}]
```

##### Python

```python
res1 = r.json().set("doc", "$", [{"a": 1, "b": 2, "c": 3}, {"a": 1}])
print(res1)
# >>> True

res2 = r.json().get("doc", "$[?count(@.*) == 3]")
print(res2)
# >>> [{'a': 1, 'b': 2, 'c': 3}]
```

##### Ruby

```ruby
res1 = r.json_set('doc', '$', [{ 'a' => 1, 'b' => 2, 'c' => 3 }, { 'a' => 1 }])
puts res1 # >>> OK

res2 = r.json_get('doc', '$[?count(@.*) == 3]')
p res2 # >>> [{"a"=>1, "b"=>2, "c"=>3}]
```

##### Rust (Asynchronous)

```rust
        let _: bool = match r.json_set("doc", "$", &json!([{"a":1,"b":2,"c":3},{"a":1}])).await {
            Ok(v) => v,
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        };

        match r.json_get("doc", "$[?count(@.*) == 3]").await {
            Ok(res1) => {
                let res1: String = res1;
                println!("{res1}");    // >>> [{"a":1,"b":2,"c":3}]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

```

##### Rust (Synchronous)

```rust
        match r.json_set("doc", "$", &json!([{"a":1,"b":2,"c":3},{"a":1}])) {
            Ok(res34) => {
                let res34: bool = res34;
                println!("{}", if res34 { "OK" } else { "(nil)" });    // >>> OK
            },
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$[?count(@.*) == 3]") {
            Ok(res35) => {
                let res35: String = res35;
                println!("{res35}");    // >>> [{"a":1,"b":2,"c":3}]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

```



#### `value()`

Returns the value of a query that selects exactly one node. A query that selects zero or more than one node produces *Nothing*.

Value function: Use value() to get the value of a query that selects exactly one node

**Difficulty:** Advanced

**Commands:** JSON.SET, JSON.GET

**Complexity:**
- JSON.SET: O(M+N)
- JSON.GET: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> JSON.SET doc $ '[{"a":1},{"a":2}]'
OK
> JSON.GET doc '$[?value(@.a) == 1]'
"[{\"a\":1}]"
```

##### C#

```csharp
        bool res36 = db.JSON().Set("doc", "$", "[{\"a\":1},{\"a\":2}]");
        Console.WriteLine(res36);   // >>> True

        RedisResult res37 = db.JSON().Get("doc", path: "$[?value(@.a) == 1]");
        Console.WriteLine(res37);   // >>> [{"a":1}]
```

##### Go

```go
	res1, err := rdb.JSONSet(ctx, "doc", "$",
		`[{"a":1},{"a":2}]`,
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // >>> OK

	res2, err := rdb.JSONGet(ctx, "doc", `$[?value(@.a) == 1]`).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2) // >>> [{"a":1}]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> funcValueExample = asyncCommands
                    .jsonSet("doc", JsonPath.ROOT_PATH, parser.createJsonValue("[{\"a\":1},{\"a\":2}]"))
                    .thenCompose(res1 -> {
                        System.out.println(res1); // >>> OK
                        return asyncCommands.jsonGet("doc", JsonPath.of("$[?value(@.a) == 1]"));
                    }).thenAccept(res2 -> {
                        System.out.println(res2); // >>> [[{"a":1}]]
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> funcValueExample = reactiveCommands
                    .jsonSet("doc", JsonPath.ROOT_PATH, parser.createJsonValue("[{\"a\":1},{\"a\":2}]"))
                    .doOnNext(res1 -> {
                        System.out.println(res1); // >>> OK
                    })
                    .flatMap(res1 -> reactiveCommands.jsonGet("doc", JsonPath.of("$[?value(@.a) == 1]")).collectList())
                    .doOnNext(res2 -> {
                        System.out.println(res2); // >>> [[{"a":1}]]
                    })
                    .then();
```

##### Java (Synchronous - Jedis)

```java
        String res36 = jedis.jsonSet("doc", new Path2("$"), "[{\"a\":1},{\"a\":2}]");
        System.out.println(res36);    // >>> OK

        Object res37 = jedis.jsonGet("doc", new Path2("$[?value(@.a) == 1]"));
        System.out.println(res37);    // >>> [{"a":1}]
```

##### JavaScript (Node.js)

```javascript
const res36 = await client.json.set('doc', '$', [{ a: 1 }, { a: 2 }]);
console.log(res36); // >>> OK

const res37 = await client.json.get('doc', { path: '$[?value(@.a) == 1]' });
console.log(res37); // >>> [ { a: 1 } ]
```

##### PHP

```php
        $res36 = $this->redis->jsonset('doc', '$', json_encode(
            [["a" => 1], ["a" => 2]]
        ));
        echo $res36 . PHP_EOL; // >>> OK

        $res37 = $this->redis->jsonget('doc', '', '', '', '$[?value(@.a) == 1]');
        echo $res37 . PHP_EOL; // >>> [{"a":1}]
```

##### Python

```python
res1 = r.json().set("doc", "$", [{"a": 1}, {"a": 2}])
print(res1)
# >>> True

res2 = r.json().get("doc", "$[?value(@.a) == 1]")
print(res2)
# >>> [{'a': 1}]
```

##### Ruby

```ruby
res1 = r.json_set('doc', '$', [{ 'a' => 1 }, { 'a' => 2 }])
puts res1 # >>> OK

res2 = r.json_get('doc', '$[?value(@.a) == 1]')
p res2 # >>> [{"a"=>1}]
```

##### Rust (Asynchronous)

```rust
        let _: bool = match r.json_set("doc", "$", &json!([{"a":1},{"a":2}])).await {
            Ok(v) => v,
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        };

        match r.json_get("doc", "$[?value(@.a) == 1]").await {
            Ok(res1) => {
                let res1: String = res1;
                println!("{res1}");    // >>> [{"a":1}]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

```

##### Rust (Synchronous)

```rust
        match r.json_set("doc", "$", &json!([{"a":1},{"a":2}])) {
            Ok(res36) => {
                let res36: bool = res36;
                println!("{}", if res36 { "OK" } else { "(nil)" });    // >>> OK
            },
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$[?value(@.a) == 1]") {
            Ok(res37) => {
                let res37: String = res37;
                println!("{res37}");    // >>> [{"a":1}]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

```



#### `keys()`

Returns the member names of an object as a list of strings, like the `~` operator. Unlike `~`, `keys()` is composable and can be chained with other functions.

Keys function: Use keys() to get an object's member names as a composable, chainable list of strings

**Difficulty:** Advanced

**Commands:** JSON.SET, JSON.GET

**Complexity:**
- JSON.SET: O(M+N)
- JSON.GET: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> JSON.SET doc $ '{"obj":{"x":1,"y":2}}'
OK
> JSON.GET doc '$.obj.keys()'
"[\"x\",\"y\"]"
> JSON.GET doc '$.obj.keys().count()'
"[2]"
```

##### C#

```csharp
        bool res38 = db.JSON().Set("doc", "$", "{\"obj\":{\"x\":1,\"y\":2}}");
        Console.WriteLine(res38);   // >>> True

        RedisResult res39 = db.JSON().Get("doc", path: "$.obj.keys()");
        Console.WriteLine(res39);   // >>> ["x","y"]

        RedisResult res40 = db.JSON().Get("doc", path: "$.obj.keys().count()");
        Console.WriteLine(res40);   // >>> [2]
```

##### Go

```go
	res1, err := rdb.JSONSet(ctx, "doc", "$",
		`{"obj":{"x":1,"y":2}}`,
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // >>> OK

	res2, err := rdb.JSONGet(ctx, "doc", `$.obj.keys()`).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2) // >>> ["x","y"]

	res3, err := rdb.JSONGet(ctx, "doc", `$.obj.keys().count()`).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3) // >>> [2]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> funcKeysExample = asyncCommands
                    .jsonSet("doc", JsonPath.ROOT_PATH, parser.createJsonValue("{\"obj\":{\"x\":1,\"y\":2}}"))
                    .thenCompose(res1 -> {
                        System.out.println(res1); // >>> OK
                        return asyncCommands.jsonGet("doc", JsonPath.of("$.obj.keys()"));
                    }).thenCompose(res2 -> {
                        System.out.println(res2); // >>> [["x","y"]]
                        return asyncCommands.jsonGet("doc", JsonPath.of("$.obj.keys().count()"));
                    }).thenAccept(res3 -> {
                        System.out.println(res3); // >>> [[2]]
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> funcKeysExample = reactiveCommands
                    .jsonSet("doc", JsonPath.ROOT_PATH, parser.createJsonValue("{\"obj\":{\"x\":1,\"y\":2}}"))
                    .doOnNext(res1 -> {
                        System.out.println(res1); // >>> OK
                    })
                    .flatMap(res1 -> reactiveCommands.jsonGet("doc", JsonPath.of("$.obj.keys()")).collectList())
                    .doOnNext(res2 -> {
                        System.out.println(res2); // >>> [["x","y"]]
                    })
                    .flatMap(res2 -> reactiveCommands.jsonGet("doc", JsonPath.of("$.obj.keys().count()")).collectList())
                    .doOnNext(res3 -> {
                        System.out.println(res3); // >>> [[2]]
                    })
                    .then();
```

##### Java (Synchronous - Jedis)

```java
        String res38 = jedis.jsonSet("doc", new Path2("$"), "{\"obj\":{\"x\":1,\"y\":2}}");
        System.out.println(res38);    // >>> OK

        Object res39 = jedis.jsonGet("doc", new Path2("$.obj.keys()"));
        System.out.println(res39);    // >>> ["x","y"]

        Object res40 = jedis.jsonGet("doc", new Path2("$.obj.keys().count()"));
        System.out.println(res40);    // >>> [2]
```

##### JavaScript (Node.js)

```javascript
const res38 = await client.json.set('doc', '$', { obj: { x: 1, y: 2 } });
console.log(res38); // >>> OK

const res39 = await client.json.get('doc', { path: '$.obj.keys()' });
console.log(res39); // >>> [ 'x', 'y' ]

const res40 = await client.json.get('doc', { path: '$.obj.keys().count()' });
console.log(res40); // >>> [ 2 ]
```

##### PHP

```php
        $res38 = $this->redis->jsonset('doc', '$', json_encode(
            ["obj" => ["x" => 1, "y" => 2]]
        ));
        echo $res38 . PHP_EOL; // >>> OK

        $res39 = $this->redis->jsonget('doc', '', '', '', '$.obj.keys()');
        echo $res39 . PHP_EOL; // >>> ["x","y"]

        $res40 = $this->redis->jsonget('doc', '', '', '', '$.obj.keys().count()');
        echo $res40 . PHP_EOL; // >>> [2]
```

##### Python

```python
res1 = r.json().set("doc", "$", {"obj": {"x": 1, "y": 2}})
print(res1)
# >>> True

res2 = r.json().get("doc", "$.obj.keys()")
print(res2)
# >>> ['x', 'y']

res3 = r.json().get("doc", "$.obj.keys().count()")
print(res3)
# >>> [2]
```

##### Ruby

```ruby
res1 = r.json_set('doc', '$', { 'obj' => { 'x' => 1, 'y' => 2 } })
puts res1 # >>> OK

res2 = r.json_get('doc', '$.obj.keys()')
p res2 # >>> ["x", "y"]

res3 = r.json_get('doc', '$.obj.keys().count()')
p res3 # >>> [2]
```

##### Rust (Asynchronous)

```rust
        let _: bool = match r.json_set("doc", "$", &json!({"obj":{"x":1,"y":2}})).await {
            Ok(v) => v,
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        };

        match r.json_get("doc", "$.obj.keys()").await {
            Ok(res1) => {
                let res1: String = res1;
                println!("{res1}");    // >>> ["x","y"]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$.obj.keys().count()").await {
            Ok(res2) => {
                let res2: String = res2;
                println!("{res2}");    // >>> [2]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

```

##### Rust (Synchronous)

```rust
        match r.json_set("doc", "$", &json!({"obj":{"x":1,"y":2}})) {
            Ok(res38) => {
                let res38: bool = res38;
                println!("{}", if res38 { "OK" } else { "(nil)" });    // >>> OK
            },
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$.obj.keys()") {
            Ok(res39) => {
                let res39: String = res39;
                println!("{res39}");    // >>> ["x","y"]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$.obj.keys().count()") {
            Ok(res40) => {
                let res40: String = res40;
                println!("{res40}");    // >>> [2]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

```



#### `match()` and `search()`

Both test a string against a regular expression pattern ([RFC 9485](https://datatracker.ietf.org/doc/rfc9485/) I-Regexp). `match()` requires the whole string to match (anchored), while `search()` matches any substring (the same behavior as the `=~` operator). An invalid pattern produces no match.

Regex functions: Use match() for an anchored (whole-string) regular expression match and search() for a partial match

**Difficulty:** Advanced

**Commands:** JSON.SET, JSON.GET

**Complexity:**
- JSON.SET: O(M+N)
- JSON.GET: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> JSON.SET doc $ '{"a":["abc","xabc","a","b"]}'
OK
> JSON.GET doc '$.a[?match(@, "a.*")]'
"[\"abc\",\"a\"]"
> JSON.SET doc $ '{"a":["abc","xyz","b"]}'
OK
> JSON.GET doc '$.a[?search(@, "b")]'
"[\"abc\",\"b\"]"
```

##### C#

```csharp
        bool res41 = db.JSON().Set("doc", "$", "{\"a\":[\"abc\",\"xabc\",\"a\",\"b\"]}");
        Console.WriteLine(res41);   // >>> True

        RedisResult res42 = db.JSON().Get("doc", path: "$.a[?match(@, \"a.*\")]");
        Console.WriteLine(res42);   // >>> ["abc","a"]

        bool res43 = db.JSON().Set("doc", "$", "{\"a\":[\"abc\",\"xyz\",\"b\"]}");
        Console.WriteLine(res43);   // >>> True

        RedisResult res44 = db.JSON().Get("doc", path: "$.a[?search(@, \"b\")]");
        Console.WriteLine(res44);   // >>> ["abc","b"]
```

##### Go

```go
	res1, err := rdb.JSONSet(ctx, "doc", "$",
		`{"a":["abc","xabc","a","b"]}`,
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // >>> OK

	res2, err := rdb.JSONGet(ctx, "doc", `$.a[?match(@, "a.*")]`).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2) // >>> ["abc","a"]

	res3, err := rdb.JSONSet(ctx, "doc", "$",
		`{"a":["abc","xyz","b"]}`,
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3) // >>> OK

	res4, err := rdb.JSONGet(ctx, "doc", `$.a[?search(@, "b")]`).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4) // >>> ["abc","b"]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> funcMatchSearchExample = asyncCommands
                    .jsonSet("doc", JsonPath.ROOT_PATH,
                            parser.createJsonValue("{\"a\":[\"abc\",\"xabc\",\"a\",\"b\"]}"))
                    .thenCompose(res1 -> {
                        System.out.println(res1); // >>> OK
                        return asyncCommands.jsonGet("doc", JsonPath.of("$.a[?match(@, \"a.*\")]"));
                    }).thenCompose(res2 -> {
                        System.out.println(res2); // >>> [["abc","a"]]
                        return asyncCommands.jsonSet("doc", JsonPath.ROOT_PATH,
                                parser.createJsonValue("{\"a\":[\"abc\",\"xyz\",\"b\"]}"));
                    }).thenCompose(res3 -> {
                        System.out.println(res3); // >>> OK
                        return asyncCommands.jsonGet("doc", JsonPath.of("$.a[?search(@, \"b\")]"));
                    }).thenAccept(res4 -> {
                        System.out.println(res4); // >>> [["abc","b"]]
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> funcMatchSearchExample = reactiveCommands
                    .jsonSet("doc", JsonPath.ROOT_PATH, parser.createJsonValue("{\"a\":[\"abc\",\"xabc\",\"a\",\"b\"]}"))
                    .doOnNext(res1 -> {
                        System.out.println(res1); // >>> OK
                    })
                    .flatMap(res1 -> reactiveCommands.jsonGet("doc", JsonPath.of("$.a[?match(@, \"a.*\")]")).collectList())
                    .doOnNext(res2 -> {
                        System.out.println(res2); // >>> [["abc","a"]]
                    })
                    .flatMap(res2 -> reactiveCommands.jsonSet("doc", JsonPath.ROOT_PATH,
                            parser.createJsonValue("{\"a\":[\"abc\",\"xyz\",\"b\"]}")))
                    .doOnNext(res3 -> {
                        System.out.println(res3); // >>> OK
                    })
                    .flatMap(res3 -> reactiveCommands.jsonGet("doc", JsonPath.of("$.a[?search(@, \"b\")]")).collectList())
                    .doOnNext(res4 -> {
                        System.out.println(res4); // >>> [["abc","b"]]
                    })
                    .then();
```

##### Java (Synchronous - Jedis)

```java
        String res41 = jedis.jsonSet("doc", new Path2("$"), "{\"a\":[\"abc\",\"xabc\",\"a\",\"b\"]}");
        System.out.println(res41);    // >>> OK

        Object res42 = jedis.jsonGet("doc", new Path2("$.a[?match(@, \"a.*\")]"));
        System.out.println(res42);    // >>> ["abc","a"]

        String res43 = jedis.jsonSet("doc", new Path2("$"), "{\"a\":[\"abc\",\"xyz\",\"b\"]}");
        System.out.println(res43);    // >>> OK

        Object res44 = jedis.jsonGet("doc", new Path2("$.a[?search(@, \"b\")]"));
        System.out.println(res44);    // >>> ["abc","b"]
```

##### JavaScript (Node.js)

```javascript
const res41 = await client.json.set('doc', '$', { a: ['abc', 'xabc', 'a', 'b'] });
console.log(res41); // >>> OK

const res42 = await client.json.get('doc', { path: '$.a[?match(@, "a.*")]' });
console.log(res42); // >>> [ 'abc', 'a' ]

const res43 = await client.json.set('doc', '$', { a: ['abc', 'xyz', 'b'] });
console.log(res43); // >>> OK

const res44 = await client.json.get('doc', { path: '$.a[?search(@, "b")]' });
console.log(res44); // >>> [ 'abc', 'b' ]
```

##### PHP

```php
        $res41 = $this->redis->jsonset('doc', '$', json_encode(
            ["a" => ["abc", "xabc", "a", "b"]]
        ));
        echo $res41 . PHP_EOL; // >>> OK

        $res42 = $this->redis->jsonget('doc', '', '', '', '$.a[?match(@, "a.*")]');
        echo $res42 . PHP_EOL; // >>> ["abc","a"]

        $res43 = $this->redis->jsonset('doc', '$', json_encode(
            ["a" => ["abc", "xyz", "b"]]
        ));
        echo $res43 . PHP_EOL; // >>> OK

        $res44 = $this->redis->jsonget('doc', '', '', '', '$.a[?search(@, "b")]');
        echo $res44 . PHP_EOL; // >>> ["abc","b"]
```

##### Python

```python
res1 = r.json().set("doc", "$", {"a": ["abc", "xabc", "a", "b"]})
print(res1)
# >>> True

res2 = r.json().get("doc", '$.a[?match(@, "a.*")]')
print(res2)
# >>> ['abc', 'a']

res3 = r.json().set("doc", "$", {"a": ["abc", "xyz", "b"]})
print(res3)
# >>> True

res4 = r.json().get("doc", '$.a[?search(@, "b")]')
print(res4)
# >>> ['abc', 'b']
```

##### Ruby

```ruby
res1 = r.json_set('doc', '$', { 'a' => ['abc', 'xabc', 'a', 'b'] })
puts res1 # >>> OK

res2 = r.json_get('doc', '$.a[?match(@, "a.*")]')
p res2 # >>> ["abc", "a"]

res3 = r.json_set('doc', '$', { 'a' => ['abc', 'xyz', 'b'] })
puts res3 # >>> OK

res4 = r.json_get('doc', '$.a[?search(@, "b")]')
p res4 # >>> ["abc", "b"]
```

##### Rust (Asynchronous)

```rust
        let _: bool = match r.json_set("doc", "$", &json!({"a":["abc","xabc","a","b"]})).await {
            Ok(v) => v,
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        };

        match r.json_get("doc", r#"$.a[?match(@, "a.*")]"#).await {
            Ok(res1) => {
                let res1: String = res1;
                println!("{res1}");    // >>> ["abc","a"]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        let _: bool = match r.json_set("doc", "$", &json!({"a":["abc","xyz","b"]})).await {
            Ok(v) => v,
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        };

        match r.json_get("doc", r#"$.a[?search(@, "b")]"#).await {
            Ok(res2) => {
                let res2: String = res2;
                println!("{res2}");    // >>> ["abc","b"]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

```

##### Rust (Synchronous)

```rust
        match r.json_set("doc", "$", &json!({"a":["abc","xabc","a","b"]})) {
            Ok(res41) => {
                let res41: bool = res41;
                println!("{}", if res41 { "OK" } else { "(nil)" });    // >>> OK
            },
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", r#"$.a[?match(@, "a.*")]"#) {
            Ok(res42) => {
                let res42: String = res42;
                println!("{res42}");    // >>> ["abc","a"]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_set("doc", "$", &json!({"a":["abc","xyz","b"]})) {
            Ok(res43) => {
                let res43: bool = res43;
                println!("{}", if res43 { "OK" } else { "(nil)" });    // >>> OK
            },
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", r#"$.a[?search(@, "b")]"#) {
            Ok(res44) => {
                let res44: String = res44;
                println!("{res44}");    // >>> ["abc","b"]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

```



#### `concat()`

Concatenates its string arguments into a single string. It requires at least one argument, and any non-string argument produces *Nothing*.

Concat function: Use concat() to join string arguments into a single string for comparison in a filter

**Difficulty:** Advanced

**Commands:** JSON.SET, JSON.GET

**Complexity:**
- JSON.SET: O(M+N)
- JSON.GET: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> JSON.SET doc $ '{"a":[{"x":"a","y":"b"},{"x":"a","y":"c"}]}'
OK
> JSON.GET doc '$.a[?concat(@.x, @.y) == "ab"]'
"[{\"x\":\"a\",\"y\":\"b\"}]"
```

##### C#

```csharp
        bool res45 = db.JSON().Set("doc", "$", "{\"a\":[{\"x\":\"a\",\"y\":\"b\"},{\"x\":\"a\",\"y\":\"c\"}]}");
        Console.WriteLine(res45);   // >>> True

        RedisResult res46 = db.JSON().Get("doc", path: "$.a[?concat(@.x, @.y) == \"ab\"]");
        Console.WriteLine(res46);   // >>> [{"x":"a","y":"b"}]
```

##### Go

```go
	res1, err := rdb.JSONSet(ctx, "doc", "$",
		`{"a":[{"x":"a","y":"b"},{"x":"a","y":"c"}]}`,
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // >>> OK

	res2, err := rdb.JSONGet(ctx, "doc", `$.a[?concat(@.x, @.y) == "ab"]`).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2) // >>> [{"x":"a","y":"b"}]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> funcConcatExample = asyncCommands
                    .jsonSet("doc", JsonPath.ROOT_PATH,
                            parser.createJsonValue("{\"a\":[{\"x\":\"a\",\"y\":\"b\"},{\"x\":\"a\",\"y\":\"c\"}]}"))
                    .thenCompose(res1 -> {
                        System.out.println(res1); // >>> OK
                        return asyncCommands.jsonGet("doc", JsonPath.of("$.a[?concat(@.x, @.y) == \"ab\"]"));
                    }).thenAccept(res2 -> {
                        System.out.println(res2); // >>> [[{"x":"a","y":"b"}]]
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> funcConcatExample = reactiveCommands
                    .jsonSet("doc", JsonPath.ROOT_PATH,
                            parser.createJsonValue("{\"a\":[{\"x\":\"a\",\"y\":\"b\"},{\"x\":\"a\",\"y\":\"c\"}]}"))
                    .doOnNext(res1 -> {
                        System.out.println(res1); // >>> OK
                    })
                    .flatMap(res1 -> reactiveCommands.jsonGet("doc", JsonPath.of("$.a[?concat(@.x, @.y) == \"ab\"]"))
                            .collectList())
                    .doOnNext(res2 -> {
                        System.out.println(res2); // >>> [[{"x":"a","y":"b"}]]
                    })
                    .then();
```

##### Java (Synchronous - Jedis)

```java
        String res45 = jedis.jsonSet("doc", new Path2("$"), "{\"a\":[{\"x\":\"a\",\"y\":\"b\"},{\"x\":\"a\",\"y\":\"c\"}]}");
        System.out.println(res45);    // >>> OK

        Object res46 = jedis.jsonGet("doc", new Path2("$.a[?concat(@.x, @.y) == \"ab\"]"));
        System.out.println(res46);    // >>> [{"x":"a","y":"b"}]
```

##### JavaScript (Node.js)

```javascript
const res45 = await client.json.set('doc', '$', { a: [{ x: 'a', y: 'b' }, { x: 'a', y: 'c' }] });
console.log(res45); // >>> OK

const res46 = await client.json.get('doc', { path: '$.a[?concat(@.x, @.y) == "ab"]' });
console.log(res46); // >>> [ { x: 'a', y: 'b' } ]
```

##### PHP

```php
        $res45 = $this->redis->jsonset('doc', '$', json_encode(
            ["a" => [["x" => "a", "y" => "b"], ["x" => "a", "y" => "c"]]]
        ));
        echo $res45 . PHP_EOL; // >>> OK

        $res46 = $this->redis->jsonget('doc', '', '', '', '$.a[?concat(@.x, @.y) == "ab"]');
        echo $res46 . PHP_EOL; // >>> [{"x":"a","y":"b"}]
```

##### Python

```python
res1 = r.json().set("doc", "$", {"a": [{"x": "a", "y": "b"}, {"x": "a", "y": "c"}]})
print(res1)
# >>> True

res2 = r.json().get("doc", '$.a[?concat(@.x, @.y) == "ab"]')
print(res2)
# >>> [{'x': 'a', 'y': 'b'}]
```

##### Ruby

```ruby
res1 = r.json_set('doc', '$', { 'a' => [{ 'x' => 'a', 'y' => 'b' }, { 'x' => 'a', 'y' => 'c' }] })
puts res1 # >>> OK

res2 = r.json_get('doc', '$.a[?concat(@.x, @.y) == "ab"]')
p res2 # >>> [{"x"=>"a", "y"=>"b"}]
```

##### Rust (Asynchronous)

```rust
        let _: bool = match r.json_set(
            "doc",
            "$",
            &json!({"a":[{"x":"a","y":"b"},{"x":"a","y":"c"}]}),
        ).await {
            Ok(v) => v,
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        };

        match r.json_get("doc", r#"$.a[?concat(@.x, @.y) == "ab"]"#).await {
            Ok(res1) => {
                let res1: String = res1;
                println!("{res1}");    // >>> [{"x":"a","y":"b"}]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

```

##### Rust (Synchronous)

```rust
        match r.json_set("doc", "$", &json!({"a":[{"x":"a","y":"b"},{"x":"a","y":"c"}]})) {
            Ok(res45) => {
                let res45: bool = res45;
                println!("{}", if res45 { "OK" } else { "(nil)" });    // >>> OK
            },
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", r#"$.a[?concat(@.x, @.y) == "ab"]"#) {
            Ok(res46) => {
                let res46: String = res46;
                println!("{res46}");    // >>> [{"x":"a","y":"b"}]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

```



#### `abs()`, `ceiling()`, and `floor()`

Operate on a number: `abs()` returns the absolute value, `ceiling()` rounds up to the nearest integer, and `floor()` rounds down. An integer argument stays an integer and a floating-point argument stays a float. A result that overflows the signed 64-bit integer range produces *Nothing*.

Numeric functions: Use abs(), ceiling(), and floor() to transform a number before comparing it in a filter

**Difficulty:** Advanced

**Commands:** JSON.SET, JSON.GET

**Complexity:**
- JSON.SET: O(M+N)
- JSON.GET: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> JSON.SET doc $ '{"a":[2.1,3.9,1.0]}'
OK
> JSON.GET doc '$.a[?ceiling(@) == 3]'
"[2.1]"
> JSON.SET doc $ '{"a":[2.1,2.9,3.5]}'
OK
> JSON.GET doc '$.a[?floor(@) == 2]'
"[2.1,2.9]"
> JSON.SET doc $ '{"a":[{"n":-5},{"n":5},{"n":-3}]}'
OK
> JSON.GET doc '$.a[?abs(@.n) == 5]'
"[{\"n\":-5},{\"n\":5}]"
```

##### C#

```csharp
        bool res47 = db.JSON().Set("doc", "$", "{\"a\":[2.1,3.9,1.0]}");
        Console.WriteLine(res47);   // >>> True

        RedisResult res48 = db.JSON().Get("doc", path: "$.a[?ceiling(@) == 3]");
        Console.WriteLine(res48);   // >>> [2.1]

        bool res49 = db.JSON().Set("doc", "$", "{\"a\":[2.1,2.9,3.5]}");
        Console.WriteLine(res49);   // >>> True

        RedisResult res50 = db.JSON().Get("doc", path: "$.a[?floor(@) == 2]");
        Console.WriteLine(res50);   // >>> [2.1,2.9]

        bool res51 = db.JSON().Set("doc", "$", "{\"a\":[{\"n\":-5},{\"n\":5},{\"n\":-3}]}");
        Console.WriteLine(res51);   // >>> True

        RedisResult res52 = db.JSON().Get("doc", path: "$.a[?abs(@.n) == 5]");
        Console.WriteLine(res52);   // >>> [{"n":-5},{"n":5}]
```

##### Go

```go
	res1, err := rdb.JSONSet(ctx, "doc", "$",
		`{"a":[2.1,3.9,1.0]}`,
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // >>> OK

	res2, err := rdb.JSONGet(ctx, "doc", `$.a[?ceiling(@) == 3]`).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2) // >>> [2.1]

	res3, err := rdb.JSONSet(ctx, "doc", "$",
		`{"a":[2.1,2.9,3.5]}`,
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3) // >>> OK

	res4, err := rdb.JSONGet(ctx, "doc", `$.a[?floor(@) == 2]`).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4) // >>> [2.1,2.9]

	res5, err := rdb.JSONSet(ctx, "doc", "$",
		`{"a":[{"n":-5},{"n":5},{"n":-3}]}`,
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res5) // >>> OK

	res6, err := rdb.JSONGet(ctx, "doc", `$.a[?abs(@.n) == 5]`).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res6) // >>> [{"n":-5},{"n":5}]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> funcMathExample = asyncCommands
                    .jsonSet("doc", JsonPath.ROOT_PATH, parser.createJsonValue("{\"a\":[2.1,3.9,1.0]}"))
                    .thenCompose(res1 -> {
                        System.out.println(res1); // >>> OK
                        return asyncCommands.jsonGet("doc", JsonPath.of("$.a[?ceiling(@) == 3]"));
                    }).thenCompose(res2 -> {
                        System.out.println(res2); // >>> [[2.1]]
                        return asyncCommands.jsonSet("doc", JsonPath.ROOT_PATH,
                                parser.createJsonValue("{\"a\":[2.1,2.9,3.5]}"));
                    }).thenCompose(res3 -> {
                        System.out.println(res3); // >>> OK
                        return asyncCommands.jsonGet("doc", JsonPath.of("$.a[?floor(@) == 2]"));
                    }).thenCompose(res4 -> {
                        System.out.println(res4); // >>> [[2.1,2.9]]
                        return asyncCommands.jsonSet("doc", JsonPath.ROOT_PATH,
                                parser.createJsonValue("{\"a\":[{\"n\":-5},{\"n\":5},{\"n\":-3}]}"));
                    }).thenCompose(res5 -> {
                        System.out.println(res5); // >>> OK
                        return asyncCommands.jsonGet("doc", JsonPath.of("$.a[?abs(@.n) == 5]"));
                    }).thenAccept(res6 -> {
                        System.out.println(res6); // >>> [[{"n":-5},{"n":5}]]
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> funcMathExample = reactiveCommands
                    .jsonSet("doc", JsonPath.ROOT_PATH, parser.createJsonValue("{\"a\":[2.1,3.9,1.0]}"))
                    .doOnNext(res1 -> {
                        System.out.println(res1); // >>> OK
                    })
                    .flatMap(res1 -> reactiveCommands.jsonGet("doc", JsonPath.of("$.a[?ceiling(@) == 3]")).collectList())
                    .doOnNext(res2 -> {
                        System.out.println(res2); // >>> [[2.1]]
                    })
                    .flatMap(res2 -> reactiveCommands.jsonSet("doc", JsonPath.ROOT_PATH,
                            parser.createJsonValue("{\"a\":[2.1,2.9,3.5]}")))
                    .doOnNext(res3 -> {
                        System.out.println(res3); // >>> OK
                    })
                    .flatMap(res3 -> reactiveCommands.jsonGet("doc", JsonPath.of("$.a[?floor(@) == 2]")).collectList())
                    .doOnNext(res4 -> {
                        System.out.println(res4); // >>> [[2.1,2.9]]
                    })
                    .flatMap(res4 -> reactiveCommands.jsonSet("doc", JsonPath.ROOT_PATH,
                            parser.createJsonValue("{\"a\":[{\"n\":-5},{\"n\":5},{\"n\":-3}]}")))
                    .doOnNext(res5 -> {
                        System.out.println(res5); // >>> OK
                    })
                    .flatMap(res5 -> reactiveCommands.jsonGet("doc", JsonPath.of("$.a[?abs(@.n) == 5]")).collectList())
                    .doOnNext(res6 -> {
                        System.out.println(res6); // >>> [[{"n":-5},{"n":5}]]
                    })
                    .then();
```

##### Java (Synchronous - Jedis)

```java
        String res47 = jedis.jsonSet("doc", new Path2("$"), "{\"a\":[2.1,3.9,1.0]}");
        System.out.println(res47);    // >>> OK

        Object res48 = jedis.jsonGet("doc", new Path2("$.a[?ceiling(@) == 3]"));
        System.out.println(res48);    // >>> [2.1]

        String res49 = jedis.jsonSet("doc", new Path2("$"), "{\"a\":[2.1,2.9,3.5]}");
        System.out.println(res49);    // >>> OK

        Object res50 = jedis.jsonGet("doc", new Path2("$.a[?floor(@) == 2]"));
        System.out.println(res50);    // >>> [2.1,2.9]

        String res51 = jedis.jsonSet("doc", new Path2("$"), "{\"a\":[{\"n\":-5},{\"n\":5},{\"n\":-3}]}");
        System.out.println(res51);    // >>> OK

        Object res52 = jedis.jsonGet("doc", new Path2("$.a[?abs(@.n) == 5]"));
        System.out.println(res52);    // >>> [{"n":-5},{"n":5}]
```

##### JavaScript (Node.js)

```javascript
const res47 = await client.json.set('doc', '$', { a: [2.1, 3.9, 1.0] });
console.log(res47); // >>> OK

const res48 = await client.json.get('doc', { path: '$.a[?ceiling(@) == 3]' });
console.log(res48); // >>> [ 2.1 ]

const res49 = await client.json.set('doc', '$', { a: [2.1, 2.9, 3.5] });
console.log(res49); // >>> OK

const res50 = await client.json.get('doc', { path: '$.a[?floor(@) == 2]' });
console.log(res50); // >>> [ 2.1, 2.9 ]

const res51 = await client.json.set('doc', '$', { a: [{ n: -5 }, { n: 5 }, { n: -3 }] });
console.log(res51); // >>> OK

const res52 = await client.json.get('doc', { path: '$.a[?abs(@.n) == 5]' });
console.log(res52); // >>> [ { n: -5 }, { n: 5 } ]
```

##### PHP

```php
        $res47 = $this->redis->jsonset('doc', '$', json_encode(
            ["a" => [2.1, 3.9, 1.0]]
        ));
        echo $res47 . PHP_EOL; // >>> OK

        $res48 = $this->redis->jsonget('doc', '', '', '', '$.a[?ceiling(@) == 3]');
        echo $res48 . PHP_EOL; // >>> [2.1]

        $res49 = $this->redis->jsonset('doc', '$', json_encode(
            ["a" => [2.1, 2.9, 3.5]]
        ));
        echo $res49 . PHP_EOL; // >>> OK

        $res50 = $this->redis->jsonget('doc', '', '', '', '$.a[?floor(@) == 2]');
        echo $res50 . PHP_EOL; // >>> [2.1,2.9]

        $res51 = $this->redis->jsonset('doc', '$', json_encode(
            ["a" => [["n" => -5], ["n" => 5], ["n" => -3]]]
        ));
        echo $res51 . PHP_EOL; // >>> OK

        $res52 = $this->redis->jsonget('doc', '', '', '', '$.a[?abs(@.n) == 5]');
        echo $res52 . PHP_EOL; // >>> [{"n":-5},{"n":5}]
```

##### Python

```python
res1 = r.json().set("doc", "$", {"a": [2.1, 3.9, 1.0]})
print(res1)
# >>> True

res2 = r.json().get("doc", "$.a[?ceiling(@) == 3]")
print(res2)
# >>> [2.1]

res3 = r.json().set("doc", "$", {"a": [2.1, 2.9, 3.5]})
print(res3)
# >>> True

res4 = r.json().get("doc", "$.a[?floor(@) == 2]")
print(res4)
# >>> [2.1, 2.9]

res5 = r.json().set("doc", "$", {"a": [{"n": -5}, {"n": 5}, {"n": -3}]})
print(res5)
# >>> True

res6 = r.json().get("doc", "$.a[?abs(@.n) == 5]")
print(res6)
# >>> [{'n': -5}, {'n': 5}]
```

##### Ruby

```ruby
res1 = r.json_set('doc', '$', { 'a' => [2.1, 3.9, 1.0] })
puts res1 # >>> OK

res2 = r.json_get('doc', '$.a[?ceiling(@) == 3]')
p res2 # >>> [2.1]

res3 = r.json_set('doc', '$', { 'a' => [2.1, 2.9, 3.5] })
puts res3 # >>> OK

res4 = r.json_get('doc', '$.a[?floor(@) == 2]')
p res4 # >>> [2.1, 2.9]

res5 = r.json_set('doc', '$', { 'a' => [{ 'n' => -5 }, { 'n' => 5 }, { 'n' => -3 }] })
puts res5 # >>> OK

res6 = r.json_get('doc', '$.a[?abs(@.n) == 5]')
p res6 # >>> [{"n"=>-5}, {"n"=>5}]
```

##### Rust (Asynchronous)

```rust
        let _: bool = match r.json_set("doc", "$", &json!({"a":[2.1,3.9,1.0]})).await {
            Ok(v) => v,
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        };

        match r.json_get("doc", "$.a[?ceiling(@) == 3]").await {
            Ok(res1) => {
                let res1: String = res1;
                println!("{res1}");    // >>> [2.1]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        let _: bool = match r.json_set("doc", "$", &json!({"a":[2.1,2.9,3.5]})).await {
            Ok(v) => v,
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        };

        match r.json_get("doc", "$.a[?floor(@) == 2]").await {
            Ok(res2) => {
                let res2: String = res2;
                println!("{res2}");    // >>> [2.1,2.9]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        let _: bool = match r.json_set(
            "doc",
            "$",
            &json!({"a":[{"n":-5},{"n":5},{"n":-3}]}),
        ).await {
            Ok(v) => v,
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        };

        match r.json_get("doc", "$.a[?abs(@.n) == 5]").await {
            Ok(res3) => {
                let res3: String = res3;
                println!("{res3}");    // >>> [{"n":-5},{"n":5}]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

```

##### Rust (Synchronous)

```rust
        match r.json_set("doc", "$", &json!({"a":[2.1,3.9,1.0]})) {
            Ok(res47) => {
                let res47: bool = res47;
                println!("{}", if res47 { "OK" } else { "(nil)" });    // >>> OK
            },
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$.a[?ceiling(@) == 3]") {
            Ok(res48) => {
                let res48: String = res48;
                println!("{res48}");    // >>> [2.1]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_set("doc", "$", &json!({"a":[2.1,2.9,3.5]})) {
            Ok(res49) => {
                let res49: bool = res49;
                println!("{}", if res49 { "OK" } else { "(nil)" });    // >>> OK
            },
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$.a[?floor(@) == 2]") {
            Ok(res50) => {
                let res50: String = res50;
                println!("{res50}");    // >>> [2.1,2.9]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_set("doc", "$", &json!({"a":[{"n":-5},{"n":5},{"n":-3}]})) {
            Ok(res51) => {
                let res51: bool = res51;
                println!("{}", if res51 { "OK" } else { "(nil)" });    // >>> OK
            },
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$.a[?abs(@.n) == 5]") {
            Ok(res52) => {
                let res52: String = res52;
                println!("{res52}");    // >>> [{"n":-5},{"n":5}]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

```



#### `first()`, `last()`, and `index()`

`first(array)` and `last(array)` return the first and last element of an array. `index(array, n)` returns the element at index `n`; a negative `n` counts from the end, a fractional `n` is truncated toward zero, and an out-of-range index produces *Nothing*.

Array access functions: Use first(), last(), and index() to pick a single element out of an array before comparing it

**Difficulty:** Advanced

**Commands:** JSON.SET, JSON.GET

**Complexity:**
- JSON.SET: O(M+N)
- JSON.GET: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> JSON.SET doc $ '{"a":[{"n":[1,2]},{"n":[9,8]}]}'
OK
> JSON.GET doc '$.a[?first(@.n) == 1]'
"[{\"n\":[1,2]}]"
> JSON.GET doc '$.a[?last(@.n) == 8]'
"[{\"n\":[9,8]}]"
> JSON.GET doc '$.a[?index(@.n, -1) == 2]'
"[{\"n\":[1,2]}]"
```

##### C#

```csharp
        bool res53 = db.JSON().Set("doc", "$", "{\"a\":[{\"n\":[1,2]},{\"n\":[9,8]}]}");
        Console.WriteLine(res53);   // >>> True

        RedisResult res54 = db.JSON().Get("doc", path: "$.a[?first(@.n) == 1]");
        Console.WriteLine(res54);   // >>> [{"n":[1,2]}]

        RedisResult res55 = db.JSON().Get("doc", path: "$.a[?last(@.n) == 8]");
        Console.WriteLine(res55);   // >>> [{"n":[9,8]}]

        RedisResult res56 = db.JSON().Get("doc", path: "$.a[?index(@.n, -1) == 2]");
        Console.WriteLine(res56);   // >>> [{"n":[1,2]}]
```

##### Go

```go
	res1, err := rdb.JSONSet(ctx, "doc", "$",
		`{"a":[{"n":[1,2]},{"n":[9,8]}]}`,
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // >>> OK

	res2, err := rdb.JSONGet(ctx, "doc", `$.a[?first(@.n) == 1]`).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2) // >>> [{"n":[1,2]}]

	res3, err := rdb.JSONGet(ctx, "doc", `$.a[?last(@.n) == 8]`).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3) // >>> [{"n":[9,8]}]

	res4, err := rdb.JSONGet(ctx, "doc", `$.a[?index(@.n, -1) == 2]`).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4) // >>> [{"n":[1,2]}]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> funcArrayAccessExample = asyncCommands
                    .jsonSet("doc", JsonPath.ROOT_PATH,
                            parser.createJsonValue("{\"a\":[{\"n\":[1,2]},{\"n\":[9,8]}]}"))
                    .thenCompose(res1 -> {
                        System.out.println(res1); // >>> OK
                        return asyncCommands.jsonGet("doc", JsonPath.of("$.a[?first(@.n) == 1]"));
                    }).thenCompose(res2 -> {
                        System.out.println(res2); // >>> [[{"n":[1,2]}]]
                        return asyncCommands.jsonGet("doc", JsonPath.of("$.a[?last(@.n) == 8]"));
                    }).thenCompose(res3 -> {
                        System.out.println(res3); // >>> [[{"n":[9,8]}]]
                        return asyncCommands.jsonGet("doc", JsonPath.of("$.a[?index(@.n, -1) == 2]"));
                    }).thenAccept(res4 -> {
                        System.out.println(res4); // >>> [[{"n":[1,2]}]]
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> funcArrayAccessExample = reactiveCommands
                    .jsonSet("doc", JsonPath.ROOT_PATH, parser.createJsonValue("{\"a\":[{\"n\":[1,2]},{\"n\":[9,8]}]}"))
                    .doOnNext(res1 -> {
                        System.out.println(res1); // >>> OK
                    })
                    .flatMap(res1 -> reactiveCommands.jsonGet("doc", JsonPath.of("$.a[?first(@.n) == 1]")).collectList())
                    .doOnNext(res2 -> {
                        System.out.println(res2); // >>> [[{"n":[1,2]}]]
                    })
                    .flatMap(res2 -> reactiveCommands.jsonGet("doc", JsonPath.of("$.a[?last(@.n) == 8]")).collectList())
                    .doOnNext(res3 -> {
                        System.out.println(res3); // >>> [[{"n":[9,8]}]]
                    })
                    .flatMap(res3 -> reactiveCommands.jsonGet("doc", JsonPath.of("$.a[?index(@.n, -1) == 2]")).collectList())
                    .doOnNext(res4 -> {
                        System.out.println(res4); // >>> [[{"n":[1,2]}]]
                    })
                    .then();
```

##### Java (Synchronous - Jedis)

```java
        String res53 = jedis.jsonSet("doc", new Path2("$"), "{\"a\":[{\"n\":[1,2]},{\"n\":[9,8]}]}");
        System.out.println(res53);    // >>> OK

        Object res54 = jedis.jsonGet("doc", new Path2("$.a[?first(@.n) == 1]"));
        System.out.println(res54);    // >>> [{"n":[1,2]}]

        Object res55 = jedis.jsonGet("doc", new Path2("$.a[?last(@.n) == 8]"));
        System.out.println(res55);    // >>> [{"n":[9,8]}]

        Object res56 = jedis.jsonGet("doc", new Path2("$.a[?index(@.n, -1) == 2]"));
        System.out.println(res56);    // >>> [{"n":[1,2]}]
```

##### JavaScript (Node.js)

```javascript
const res53 = await client.json.set('doc', '$', { a: [{ n: [1, 2] }, { n: [9, 8] }] });
console.log(res53); // >>> OK

const res54 = await client.json.get('doc', { path: '$.a[?first(@.n) == 1]' });
console.log(res54); // >>> [ { n: [ 1, 2 ] } ]

const res55 = await client.json.get('doc', { path: '$.a[?last(@.n) == 8]' });
console.log(res55); // >>> [ { n: [ 9, 8 ] } ]

const res56 = await client.json.get('doc', { path: '$.a[?index(@.n, -1) == 2]' });
console.log(res56); // >>> [ { n: [ 1, 2 ] } ]
```

##### PHP

```php
        $res53 = $this->redis->jsonset('doc', '$', json_encode(
            ["a" => [["n" => [1, 2]], ["n" => [9, 8]]]]
        ));
        echo $res53 . PHP_EOL; // >>> OK

        $res54 = $this->redis->jsonget('doc', '', '', '', '$.a[?first(@.n) == 1]');
        echo $res54 . PHP_EOL; // >>> [{"n":[1,2]}]

        $res55 = $this->redis->jsonget('doc', '', '', '', '$.a[?last(@.n) == 8]');
        echo $res55 . PHP_EOL; // >>> [{"n":[9,8]}]

        $res56 = $this->redis->jsonget('doc', '', '', '', '$.a[?index(@.n, -1) == 2]');
        echo $res56 . PHP_EOL; // >>> [{"n":[1,2]}]
```

##### Python

```python
res1 = r.json().set("doc", "$", {"a": [{"n": [1, 2]}, {"n": [9, 8]}]})
print(res1)
# >>> True

res2 = r.json().get("doc", "$.a[?first(@.n) == 1]")
print(res2)
# >>> [{'n': [1, 2]}]

res3 = r.json().get("doc", "$.a[?last(@.n) == 8]")
print(res3)
# >>> [{'n': [9, 8]}]

res4 = r.json().get("doc", "$.a[?index(@.n, -1) == 2]")
print(res4)
# >>> [{'n': [1, 2]}]
```

##### Ruby

```ruby
res1 = r.json_set('doc', '$', { 'a' => [{ 'n' => [1, 2] }, { 'n' => [9, 8] }] })
puts res1 # >>> OK

res2 = r.json_get('doc', '$.a[?first(@.n) == 1]')
p res2 # >>> [{"n"=>[1, 2]}]

res3 = r.json_get('doc', '$.a[?last(@.n) == 8]')
p res3 # >>> [{"n"=>[9, 8]}]

res4 = r.json_get('doc', '$.a[?index(@.n, -1) == 2]')
p res4 # >>> [{"n"=>[1, 2]}]
```

##### Rust (Asynchronous)

```rust
        let _: bool = match r.json_set(
            "doc",
            "$",
            &json!({"a":[{"n":[1,2]},{"n":[9,8]}]}),
        ).await {
            Ok(v) => v,
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        };

        match r.json_get("doc", "$.a[?first(@.n) == 1]").await {
            Ok(res1) => {
                let res1: String = res1;
                println!("{res1}");    // >>> [{"n":[1,2]}]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$.a[?last(@.n) == 8]").await {
            Ok(res2) => {
                let res2: String = res2;
                println!("{res2}");    // >>> [{"n":[9,8]}]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$.a[?index(@.n, -1) == 2]").await {
            Ok(res3) => {
                let res3: String = res3;
                println!("{res3}");    // >>> [{"n":[1,2]}]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

```

##### Rust (Synchronous)

```rust
        match r.json_set("doc", "$", &json!({"a":[{"n":[1,2]},{"n":[9,8]}]})) {
            Ok(res53) => {
                let res53: bool = res53;
                println!("{}", if res53 { "OK" } else { "(nil)" });    // >>> OK
            },
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$.a[?first(@.n) == 1]") {
            Ok(res54) => {
                let res54: String = res54;
                println!("{res54}");    // >>> [{"n":[1,2]}]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$.a[?last(@.n) == 8]") {
            Ok(res55) => {
                let res55: String = res55;
                println!("{res55}");    // >>> [{"n":[9,8]}]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$.a[?index(@.n, -1) == 2]") {
            Ok(res56) => {
                let res56: String = res56;
                println!("{res56}");    // >>> [{"n":[1,2]}]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

```



#### `min()`, `max()`, `avg()`, `sum()`, and `stddev()`

These aggregation functions operate on an array of numbers. `stddev()` returns the *population* standard deviation (dividing by N). The functions are strict: an array that contains any non-numeric element, or an empty array, produces *Nothing* — elements are never silently skipped.

Aggregation functions: Use sum(), avg(), min(), max(), or stddev() to reduce an array of numbers to a single value in a filter

**Difficulty:** Advanced

**Commands:** JSON.SET, JSON.GET

**Complexity:**
- JSON.SET: O(M+N)
- JSON.GET: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> JSON.SET doc $ '{"a":[{"n":[3,1,2]},{"n":[5,6]}]}'
OK
> JSON.GET doc '$.a[?sum(@.n) == 6]'
"[{\"n\":[3,1,2]}]"
> JSON.GET doc '$.a[?avg(@.n) == 2]'
"[{\"n\":[3,1,2]}]"
```

##### C#

```csharp
        bool res57 = db.JSON().Set("doc", "$", "{\"a\":[{\"n\":[3,1,2]},{\"n\":[5,6]}]}");
        Console.WriteLine(res57);   // >>> True

        RedisResult res58 = db.JSON().Get("doc", path: "$.a[?sum(@.n) == 6]");
        Console.WriteLine(res58);   // >>> [{"n":[3,1,2]}]

        RedisResult res59 = db.JSON().Get("doc", path: "$.a[?avg(@.n) == 2]");
        Console.WriteLine(res59);   // >>> [{"n":[3,1,2]}]
```

##### Go

```go
	res1, err := rdb.JSONSet(ctx, "doc", "$",
		`{"a":[{"n":[3,1,2]},{"n":[5,6]}]}`,
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // >>> OK

	res2, err := rdb.JSONGet(ctx, "doc", `$.a[?sum(@.n) == 6]`).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2) // >>> [{"n":[3,1,2]}]

	res3, err := rdb.JSONGet(ctx, "doc", `$.a[?avg(@.n) == 2]`).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3) // >>> [{"n":[3,1,2]}]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> funcAggregateExample = asyncCommands
                    .jsonSet("doc", JsonPath.ROOT_PATH,
                            parser.createJsonValue("{\"a\":[{\"n\":[3,1,2]},{\"n\":[5,6]}]}"))
                    .thenCompose(res1 -> {
                        System.out.println(res1); // >>> OK
                        return asyncCommands.jsonGet("doc", JsonPath.of("$.a[?sum(@.n) == 6]"));
                    }).thenCompose(res2 -> {
                        System.out.println(res2); // >>> [[{"n":[3,1,2]}]]
                        return asyncCommands.jsonGet("doc", JsonPath.of("$.a[?avg(@.n) == 2]"));
                    }).thenAccept(res3 -> {
                        System.out.println(res3); // >>> [[{"n":[3,1,2]}]]
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> funcAggregateExample = reactiveCommands
                    .jsonSet("doc", JsonPath.ROOT_PATH,
                            parser.createJsonValue("{\"a\":[{\"n\":[3,1,2]},{\"n\":[5,6]}]}"))
                    .doOnNext(res1 -> {
                        System.out.println(res1); // >>> OK
                    })
                    .flatMap(res1 -> reactiveCommands.jsonGet("doc", JsonPath.of("$.a[?sum(@.n) == 6]")).collectList())
                    .doOnNext(res2 -> {
                        System.out.println(res2); // >>> [[{"n":[3,1,2]}]]
                    })
                    .flatMap(res2 -> reactiveCommands.jsonGet("doc", JsonPath.of("$.a[?avg(@.n) == 2]")).collectList())
                    .doOnNext(res3 -> {
                        System.out.println(res3); // >>> [[{"n":[3,1,2]}]]
                    })
                    .then();
```

##### Java (Synchronous - Jedis)

```java
        String res57 = jedis.jsonSet("doc", new Path2("$"), "{\"a\":[{\"n\":[3,1,2]},{\"n\":[5,6]}]}");
        System.out.println(res57);    // >>> OK

        Object res58 = jedis.jsonGet("doc", new Path2("$.a[?sum(@.n) == 6]"));
        System.out.println(res58);    // >>> [{"n":[3,1,2]}]

        Object res59 = jedis.jsonGet("doc", new Path2("$.a[?avg(@.n) == 2]"));
        System.out.println(res59);    // >>> [{"n":[3,1,2]}]
```

##### JavaScript (Node.js)

```javascript
const res57 = await client.json.set('doc', '$', { a: [{ n: [3, 1, 2] }, { n: [5, 6] }] });
console.log(res57); // >>> OK

const res58 = await client.json.get('doc', { path: '$.a[?sum(@.n) == 6]' });
console.log(res58); // >>> [ { n: [ 3, 1, 2 ] } ]

const res59 = await client.json.get('doc', { path: '$.a[?avg(@.n) == 2]' });
console.log(res59); // >>> [ { n: [ 3, 1, 2 ] } ]
```

##### PHP

```php
        $res57 = $this->redis->jsonset('doc', '$', json_encode(
            ["a" => [["n" => [3, 1, 2]], ["n" => [5, 6]]]]
        ));
        echo $res57 . PHP_EOL; // >>> OK

        $res58 = $this->redis->jsonget('doc', '', '', '', '$.a[?sum(@.n) == 6]');
        echo $res58 . PHP_EOL; // >>> [{"n":[3,1,2]}]

        $res59 = $this->redis->jsonget('doc', '', '', '', '$.a[?avg(@.n) == 2]');
        echo $res59 . PHP_EOL; // >>> [{"n":[3,1,2]}]
```

##### Python

```python
res1 = r.json().set("doc", "$", {"a": [{"n": [3, 1, 2]}, {"n": [5, 6]}]})
print(res1)
# >>> True

res2 = r.json().get("doc", "$.a[?sum(@.n) == 6]")
print(res2)
# >>> [{'n': [3, 1, 2]}]

res3 = r.json().get("doc", "$.a[?avg(@.n) == 2]")
print(res3)
# >>> [{'n': [3, 1, 2]}]
```

##### Ruby

```ruby
res1 = r.json_set('doc', '$', { 'a' => [{ 'n' => [3, 1, 2] }, { 'n' => [5, 6] }] })
puts res1 # >>> OK

res2 = r.json_get('doc', '$.a[?sum(@.n) == 6]')
p res2 # >>> [{"n"=>[3, 1, 2]}]

res3 = r.json_get('doc', '$.a[?avg(@.n) == 2]')
p res3 # >>> [{"n"=>[3, 1, 2]}]
```

##### Rust (Asynchronous)

```rust
        let _: bool = match r.json_set(
            "doc",
            "$",
            &json!({"a":[{"n":[3,1,2]},{"n":[5,6]}]}),
        ).await {
            Ok(v) => v,
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        };

        match r.json_get("doc", "$.a[?sum(@.n) == 6]").await {
            Ok(res1) => {
                let res1: String = res1;
                println!("{res1}");    // >>> [{"n":[3,1,2]}]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$.a[?avg(@.n) == 2]").await {
            Ok(res2) => {
                let res2: String = res2;
                println!("{res2}");    // >>> [{"n":[3,1,2]}]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

```

##### Rust (Synchronous)

```rust
        match r.json_set("doc", "$", &json!({"a":[{"n":[3,1,2]},{"n":[5,6]}]})) {
            Ok(res57) => {
                let res57: bool = res57;
                println!("{}", if res57 { "OK" } else { "(nil)" });    // >>> OK
            },
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$.a[?sum(@.n) == 6]") {
            Ok(res58) => {
                let res58: String = res58;
                println!("{res58}");    // >>> [{"n":[3,1,2]}]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$.a[?avg(@.n) == 2]") {
            Ok(res59) => {
                let res59: String = res59;
                println!("{res59}");    // >>> [{"n":[3,1,2]}]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

```



#### `append()`

`append(value, ...)` returns the matched array with the given value or values added after its elements. It is a read-only query-time projection and does not modify the stored document — to mutate an array in place, use the [`JSON.ARRAPPEND`](https://redis.io/docs/latest/commands/json.arrappend) command instead. A multiple-value argument is added as a single element (it is not spread), and a *Nothing* argument makes the whole result *Nothing*.

Append function: Use append() as a read-only, query-time projection that adds a value after an array's elements without modifying the stored document

**Difficulty:** Advanced

**Commands:** JSON.SET, JSON.GET

**Complexity:**
- JSON.SET: O(M+N)
- JSON.GET: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> JSON.SET doc $ '{"arr":[1,2,3]}'
OK
> JSON.GET doc '$.arr.append(9)'
"[1,2,3,9]"
> JSON.SET doc $ '{"books":[{"t":"a","price":30},{"t":"b","price":5}]}'
OK
> JSON.GET doc '$.books[?(@.price >= 10)].append({"t":"X"})'
"[{\"t\":\"a\",\"price\":30},{\"t\":\"X\"}]"
```

##### C#

```csharp
        bool res60 = db.JSON().Set("doc", "$", "{\"arr\":[1,2,3]}");
        Console.WriteLine(res60);   // >>> True

        RedisResult res61 = db.JSON().Get("doc", path: "$.arr.append(9)");
        Console.WriteLine(res61);   // >>> [1,2,3,9]

        bool res62 = db.JSON().Set("doc", "$", "{\"books\":[{\"t\":\"a\",\"price\":30},{\"t\":\"b\",\"price\":5}]}");
        Console.WriteLine(res62);   // >>> True

        RedisResult res63 = db.JSON().Get("doc", path: "$.books[?(@.price >= 10)].append({\"t\":\"X\"})");
        Console.WriteLine(res63);   // >>> [{"t":"a","price":30},{"t":"X"}]
```

##### Go

```go
	res1, err := rdb.JSONSet(ctx, "doc", "$",
		`{"arr":[1,2,3]}`,
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // >>> OK

	res2, err := rdb.JSONGet(ctx, "doc", `$.arr.append(9)`).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2) // >>> [1,2,3,9]

	res3, err := rdb.JSONSet(ctx, "doc", "$",
		`{"books":[{"t":"a","price":30},{"t":"b","price":5}]}`,
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3) // >>> OK

	res4, err := rdb.JSONGet(ctx, "doc", `$.books[?(@.price >= 10)].append({"t":"X"})`).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4) // >>> [{"t":"a","price":30},{"t":"X"}]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> funcAppendExample = asyncCommands
                    .jsonSet("doc", JsonPath.ROOT_PATH, parser.createJsonValue("{\"arr\":[1,2,3]}"))
                    .thenCompose(res1 -> {
                        System.out.println(res1); // >>> OK
                        return asyncCommands.jsonGet("doc", JsonPath.of("$.arr.append(9)"));
                    }).thenCompose(res2 -> {
                        System.out.println(res2); // >>> [[1,2,3,9]]
                        return asyncCommands.jsonSet("doc", JsonPath.ROOT_PATH,
                                parser.createJsonValue(
                                        "{\"books\":[{\"t\":\"a\",\"price\":30},{\"t\":\"b\",\"price\":5}]}"));
                    }).thenCompose(res3 -> {
                        System.out.println(res3); // >>> OK
                        return asyncCommands.jsonGet("doc",
                                JsonPath.of("$.books[?(@.price >= 10)].append({\"t\":\"X\"})"));
                    }).thenAccept(res4 -> {
                        System.out.println(res4); // >>> [[{"t":"a","price":30},{"t":"X"}]]
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> funcAppendExample = reactiveCommands
                    .jsonSet("doc", JsonPath.ROOT_PATH, parser.createJsonValue("{\"arr\":[1,2,3]}"))
                    .doOnNext(res1 -> {
                        System.out.println(res1); // >>> OK
                    })
                    .flatMap(res1 -> reactiveCommands.jsonGet("doc", JsonPath.of("$.arr.append(9)")).collectList())
                    .doOnNext(res2 -> {
                        System.out.println(res2); // >>> [[1,2,3,9]]
                    })
                    .flatMap(res2 -> reactiveCommands.jsonSet("doc", JsonPath.ROOT_PATH,
                            parser.createJsonValue(
                                    "{\"books\":[{\"t\":\"a\",\"price\":30},{\"t\":\"b\",\"price\":5}]}")))
                    .doOnNext(res3 -> {
                        System.out.println(res3); // >>> OK
                    })
                    .flatMap(res3 -> reactiveCommands
                            .jsonGet("doc", JsonPath.of("$.books[?(@.price >= 10)].append({\"t\":\"X\"})"))
                            .collectList())
                    .doOnNext(res4 -> {
                        System.out.println(res4); // >>> [[{"t":"a","price":30},{"t":"X"}]]
                    })
                    .then();
```

##### Java (Synchronous - Jedis)

```java
        String res60 = jedis.jsonSet("doc", new Path2("$"), "{\"arr\":[1,2,3]}");
        System.out.println(res60);    // >>> OK

        Object res61 = jedis.jsonGet("doc", new Path2("$.arr.append(9)"));
        System.out.println(res61);    // >>> [1,2,3,9]

        String res62 = jedis.jsonSet("doc", new Path2("$"), "{\"books\":[{\"t\":\"a\",\"price\":30},{\"t\":\"b\",\"price\":5}]}");
        System.out.println(res62);    // >>> OK

        Object res63 = jedis.jsonGet("doc", new Path2("$.books[?(@.price >= 10)].append({\"t\":\"X\"})"));
        System.out.println(res63);    // >>> [{"t":"a","price":30},{"t":"X"}]
```

##### JavaScript (Node.js)

```javascript
const res60 = await client.json.set('doc', '$', { arr: [1, 2, 3] });
console.log(res60); // >>> OK

const res61 = await client.json.get('doc', { path: '$.arr.append(9)' });
console.log(res61); // >>> [ 1, 2, 3, 9 ]

const res62 = await client.json.set('doc', '$', {
  books: [{ t: 'a', price: 30 }, { t: 'b', price: 5 }]
});
console.log(res62); // >>> OK

const res63 = await client.json.get('doc', { path: '$.books[?(@.price >= 10)].append({"t":"X"})' });
console.log(res63); // >>> [ { t: 'a', price: 30 }, { t: 'X' } ]
```

##### PHP

```php
        $res60 = $this->redis->jsonset('doc', '$', json_encode(
            ["arr" => [1, 2, 3]]
        ));
        echo $res60 . PHP_EOL; // >>> OK

        $res61 = $this->redis->jsonget('doc', '', '', '', '$.arr.append(9)');
        echo $res61 . PHP_EOL; // >>> [1,2,3,9]

        $res62 = $this->redis->jsonset('doc', '$', json_encode(
            ["books" => [["t" => "a", "price" => 30], ["t" => "b", "price" => 5]]]
        ));
        echo $res62 . PHP_EOL; // >>> OK

        $res63 = $this->redis->jsonget('doc', '', '', '', '$.books[?(@.price >= 10)].append({"t":"X"})');
        echo $res63 . PHP_EOL; // >>> [{"t":"a","price":30},{"t":"X"}]
```

##### Python

```python
res1 = r.json().set("doc", "$", {"arr": [1, 2, 3]})
print(res1)
# >>> True

res2 = r.json().get("doc", "$.arr.append(9)")
print(res2)
# >>> [1, 2, 3, 9]

res3 = r.json().set("doc", "$", {"books": [{"t": "a", "price": 30}, {"t": "b", "price": 5}]})
print(res3)
# >>> True

res4 = r.json().get("doc", '$.books[?(@.price >= 10)].append({"t":"X"})')
print(res4)
# >>> [{'t': 'a', 'price': 30}, {'t': 'X'}]
```

##### Ruby

```ruby
res1 = r.json_set('doc', '$', { 'arr' => [1, 2, 3] })
puts res1 # >>> OK

res2 = r.json_get('doc', '$.arr.append(9)')
p res2 # >>> [1, 2, 3, 9]

res3 = r.json_set('doc', '$', { 'books' => [{ 't' => 'a', 'price' => 30 }, { 't' => 'b', 'price' => 5 }] })
puts res3 # >>> OK

res4 = r.json_get('doc', '$.books[?(@.price >= 10)].append({"t":"X"})')
p res4 # >>> [{"t"=>"a", "price"=>30}, {"t"=>"X"}]
```

##### Rust (Asynchronous)

```rust
        let _: bool = match r.json_set("doc", "$", &json!({"arr":[1,2,3]})).await {
            Ok(v) => v,
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        };

        match r.json_get("doc", "$.arr.append(9)").await {
            Ok(res1) => {
                let res1: String = res1;
                println!("{res1}");    // >>> [1,2,3,9]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        let _: bool = match r.json_set(
            "doc",
            "$",
            &json!({"books":[{"t":"a","price":30},{"t":"b","price":5}]}),
        ).await {
            Ok(v) => v,
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        };

        match r.json_get("doc", r#"$.books[?(@.price >= 10)].append({"t":"X"})"#).await {
            Ok(res2) => {
                let res2: String = res2;
                println!("{res2}");    // >>> [{"t":"a","price":30},{"t":"X"}]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

```

##### Rust (Synchronous)

```rust
        match r.json_set("doc", "$", &json!({"arr":[1,2,3]})) {
            Ok(res60) => {
                let res60: bool = res60;
                println!("{}", if res60 { "OK" } else { "(nil)" });    // >>> OK
            },
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$.arr.append(9)") {
            Ok(res61) => {
                let res61: String = res61;
                println!("{res61}");    // >>> [1,2,3,9]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_set("doc", "$", &json!({"books":[{"t":"a","price":30},{"t":"b","price":5}]})) {
            Ok(res62) => {
                let res62: bool = res62;
                println!("{}", if res62 { "OK" } else { "(nil)" });    // >>> OK
            },
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", r#"$.books[?(@.price >= 10)].append({"t":"X"})"#) {
            Ok(res63) => {
                let res63: String = res63;
                println!("{res63}");    // >>> [{"t":"a","price":30},{"t":"X"}]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

```



### Update examples

You can also use JSONPath queries when you want to update specific sections of a JSON document.

For example, you can pass a JSONPath to the [`JSON.SET`](https://redis.io/docs/latest/commands/json.set) command to update a specific field. This example changes the price of the first item in the headphones list:

Bulk updates: Use JSONPath with JSON.NUMINCRBY to update multiple numeric values across the document when you need to apply arithmetic operations to multiple fields

**Difficulty:** Intermediate

**Builds upon:** get_bikes

**Commands:** JSON.GET, JSON.NUMINCRBY

**Complexity:**
- JSON.GET: O(N)
- JSON.NUMINCRBY: O(1)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> JSON.GET bikes:inventory $..price
"[1920,2072,3264,1475,3941]"
> JSON.NUMINCRBY bikes:inventory $..price -100
"[1820,1972,3164,1375,3841]"
> JSON.NUMINCRBY bikes:inventory $..price 100
"[1920,2072,3264,1475,3941]"
```

##### C#

```csharp
        RedisResult res42 = db.JSON().Get("bikes:inventory", path: "$..price");
        Console.WriteLine(res42);   // >>> [1920,2072,3264,1475,3941]

        double?[] res43 = db.JSON().NumIncrby("bikes:inventory", "$..price", -100);
        Console.WriteLine(string.Join(", ", res43));    // >>> 1820, 1972, 3164, 1375, 3841

        double?[] res44 = db.JSON().NumIncrby("bikes:inventory", "$..price", 100);
        Console.WriteLine(string.Join(", ", res44));    // >>> 1920, 2072, 3264, 1475, 3941
```

##### Go

```go
	res15, err := rdb.JSONGet(ctx, "bikes:inventory", "$..price").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res15) // >>> [1475,3941,1920,2072,3264]

	res16, err := rdb.JSONNumIncrBy(ctx, "bikes:inventory", "$..price", -100).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res16) // >>> [1375,3841,1820,1972,3164]

	res17, err := rdb.JSONNumIncrBy(ctx, "bikes:inventory", "$..price", 100).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res17) // >>> [1475,3941,1920,2072,3264]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> updateBikes = asyncCommands.jsonGet("bikes:inventory", JsonPath.of("$..price"))
                    .thenCompose(r -> {
                        System.out.println(r); // >>> [[1920,2072,3264,1475,3941]]

                        return asyncCommands.jsonNumincrby("bikes:inventory", JsonPath.of("$..price"), -100);
                    }).thenCompose(res23 -> {
                        System.out.println(res23); // >>> [1820, 1972, 3164, 1375, 3841]

                        return asyncCommands.jsonNumincrby("bikes:inventory", JsonPath.of("$..price"), 100);
                    })
                    .thenAccept(System.out::println)
                    // >>> [1920, 2072, 3264, 1475, 3941]
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> updateBikes = reactiveCommands.jsonGet("bikes:inventory", JsonPath.of("$..price")).collectList()
                    .doOnNext(r -> {
                        System.out.println(r); // >>> [[1920,2072,3264,1475,3941]]
                    })
                    .flatMap(
                            r -> reactiveCommands.jsonNumincrby("bikes:inventory", JsonPath.of("$..price"), -100).collectList())
                    .doOnNext(res23 -> {
                        System.out.println(res23); // >>> [1820, 1972, 3164, 1375, 3841]
                    })
                    .flatMap(res23 -> reactiveCommands.jsonNumincrby("bikes:inventory", JsonPath.of("$..price"), 100)
                            .collectList())
                    .doOnNext(System.out::println) // >>> [1920, 2072, 3264, 1475, 3941]
                    .then();
```

##### Java (Synchronous - Jedis)

```java
        Object res39 = jedis.jsonGet("bikes:inventory", new Path2("$..price"));
        System.out.println(res39);
        // >>> [1920,2072,3264,1475,3941]

        Object res40 = jedis.jsonNumIncrBy("bikes:inventory", new Path2("$..price"), -100);
        System.out.println(res40);  // >>> [1820,1972,3164,1375,3841]

        Object res41 = jedis.jsonNumIncrBy("bikes:inventory", new Path2("$..price"), 100);
        System.out.println(res41);  // >>> [1920,2072,3264,1475,3941]
```

##### JavaScript (Node.js)

```javascript
const res38 = await client.json.get("bikes:inventory", {
  path: "$..price"
});
console.log(res38);  //  [1920, 2072, 3264, 1475, 3941]

const res39 = await client.json.numIncrBy("bikes:inventory", "$..price", -100);
console.log(res39);  //  [1820, 1972, 3164, 1375, 3841]

const res40 = await client.json.numIncrBy("bikes:inventory", "$..price", 100);
console.log(res40);  //  [1920, 2072, 3264, 1475, 3941]
```

##### PHP

```php
        $res15b = $r->jsonget('bikes:inventory', '', '', '', '$..price');
        echo $res15b . PHP_EOL;
        // >>> [1920,2072,3264,1475,3941]

        $res16b = $r->jsonnumincrby('bikes:inventory', '$..price', -100);
        echo json_encode($res16b) . PHP_EOL;
        // >>> [1820,1972,3164,1375,3841]

        $res17b = $r->jsonnumincrby('bikes:inventory', '$..price', 100);
        echo json_encode($res17b) . PHP_EOL;
        // >>> [1920,2072,3264,1475,3941]
```

##### Python

```python
res15 = r.json().get("bikes:inventory", "$..price")
print(res15)  # >>> [1920, 2072, 3264, 1475, 3941]

res16 = r.json().numincrby("bikes:inventory", "$..price", -100)
print(res16)  # >>> [1820, 1972, 3164, 1375, 3841]

res17 = r.json().numincrby("bikes:inventory", "$..price", 100)
print(res17)  # >>> [1920, 2072, 3264, 1475, 3941]
```

##### Ruby

```ruby
res15 = r.json_get('bikes:inventory', '$..price')
p res15 # >>> [1920, 2072, 3264, 1475, 3941]

res16 = r.json_numincrby('bikes:inventory', '$..price', -100)
p res16 # >>> [1820, 1972, 3164, 1375, 3841]

res17 = r.json_numincrby('bikes:inventory', '$..price', 100)
p res17 # >>> [1920, 2072, 3264, 1475, 3941]
```

##### Rust (Asynchronous)

```rust
        let res40: String = r
            .json_get("bikes:inventory", "$..price")
            .await
            .expect("Failed to run JSON.GET");
        println!("{res40}"); // >>> [1920,2072,3264,1475,3941]

        let res41: String = cmd("JSON.NUMINCRBY")
            .arg("bikes:inventory")
            .arg("$..price")
            .arg(-100)
            .query_async(&mut r)
            .await
            .expect("Failed to run JSON.NUMINCRBY");
        println!("{res41}"); // >>> [1820,1972,3164,1375,3841]

        let res42: String = cmd("JSON.NUMINCRBY")
            .arg("bikes:inventory")
            .arg("$..price")
            .arg(100)
            .query_async(&mut r)
            .await
            .expect("Failed to run JSON.NUMINCRBY");
        println!("{res42}"); // >>> [1920,2072,3264,1475,3941]
```

##### Rust (Synchronous)

```rust
        let res40: String = r
            .json_get("bikes:inventory", "$..price")
            .expect("Failed to run JSON.GET");
        println!("{res40}"); // >>> [1920,2072,3264,1475,3941]

        let res41: String = cmd("JSON.NUMINCRBY")
            .arg("bikes:inventory")
            .arg("$..price")
            .arg(-100)
            .query(&mut r)
            .expect("Failed to run JSON.NUMINCRBY");
        println!("{res41}"); // >>> [1820,1972,3164,1375,3841]

        let res42: String = cmd("JSON.NUMINCRBY")
            .arg("bikes:inventory")
            .arg("$..price")
            .arg(100)
            .query(&mut r)
            .expect("Failed to run JSON.NUMINCRBY");
        println!("{res42}"); // >>> [1920,2072,3264,1475,3941]
```



You can use filter expressions to update only JSON elements that match certain conditions. The following example sets the price of any bike to 1500 if its price is already less than 2000:

Conditional updates: Use filter expressions with JSON.SET to update only elements matching specific conditions when you need selective modifications

**Difficulty:** Advanced

**Builds upon:** filter1

**Commands:** JSON.SET, JSON.GET

**Complexity:**
- JSON.SET: O(M+N)
- JSON.GET: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> JSON.SET bikes:inventory '$.inventory.*[?(@.price<2000)].price' 1500
OK
> JSON.GET bikes:inventory $..price
"[1500,2072,3264,1500,3941]"
```

##### C#

```csharp
        bool res45 = db.JSON().Set(
            "bikes:inventory",
            "$.inventory.*[?(@.price<2000)].price",
            1500
        );
        Console.WriteLine(res45);   // >>> True

        RedisResult res46 = db.JSON().Get("bikes:inventory", path: "$..price");
        Console.WriteLine(res46);   // >>> [1500,2072,3264,1500,3941]
```

##### Go

```go
	res18, err := rdb.JSONSet(ctx,
		"bikes:inventory",
		"$.inventory.*[?(@.price<2000)].price",
		1500,
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res18) // >>> OK

	res19, err := rdb.JSONGet(ctx, "bikes:inventory", "$..price").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res19) // >>> [1500,3941,1500,2072,3264]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> updateFilters1 = asyncCommands.jsonSet("bikes:inventory",
                    JsonPath.of("$.inventory.*[?(@.price<2000)].price"), parser.createJsonValue("1500")).thenCompose(r -> {
                        System.out.println(r); // >>> OK

                        return asyncCommands.jsonGet("bikes:inventory", JsonPath.of("$..price"));
                    })
                    .thenAccept(System.out::println)
                    // >>> [[1500,2072,3264,1500,3941]]
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> updateFilters1 = reactiveCommands.jsonSet("bikes:inventory",
                    JsonPath.of("$.inventory.*[?(@.price<2000)].price"), parser.createJsonValue("1500")).doOnNext(r -> {
                        System.out.println(r); // >>> OK
                    }).flatMap(r -> reactiveCommands.jsonGet("bikes:inventory", JsonPath.of("$..price")).collectList())
                    .doOnNext(System.out::println) // >>> [[1500,2072,3264,1500,3941]]
                    .then();
```

##### Java (Synchronous - Jedis)

```java
        jedis.jsonSet("bikes:inventory", new Path2("$.inventory.*[?(@.price<2000)].price"), 1500);
        Object res42 = jedis.jsonGet("bikes:inventory", new Path2("$..price"));
        System.out.println(res42);  // >>> [1500,2072,3264,1500,3941]
```

##### JavaScript (Node.js)

```javascript
const res40a = await client.json.set(
  'bikes:inventory', 
  '$.inventory.*[?(@.price<2000)].price', 
  1500
);

// Get all prices from the inventory
const res40b = await client.json.get(
  'bikes:inventory',
  { path: "$..price" }
);
console.log(res40b); // [1500, 2072, 3264, 1500, 3941]
```

##### PHP

```php
        $res18b = $r->jsonset('bikes:inventory', '$.inventory.*[?(@.price<2000)].price', '1500');
        $res19b = $r->jsonget('bikes:inventory', '', '', '', '$..price');
        echo $res19b . PHP_EOL;
        // >>> [1500,2072,3264,1500,3941]
```

##### Python

```python
res18 = r.json().set("bikes:inventory", "$.inventory.*[?(@.price<2000)].price", 1500)
res19 = r.json().get("bikes:inventory", "$..price")
print(res19)  # >>> [1500, 2072, 3264, 1500, 3941]
```

##### Ruby

```ruby
res18 = r.json_set('bikes:inventory', '$.inventory.*[?(@.price<2000)].price', 1500)
res19 = r.json_get('bikes:inventory', '$..price')
p res19 # >>> [1500, 2072, 3264, 1500, 3941]
```

##### Rust (Asynchronous)

```rust
        let _: bool = r
            .json_set(
                "bikes:inventory",
                "$.inventory.*[?(@.price<2000)].price",
                &json!(1500),
            )
            .await
            .expect("Failed to run JSON.SET");

        let res43: String = r
            .json_get("bikes:inventory", "$..price")
            .await
            .expect("Failed to run JSON.GET");
        println!("{res43}"); // >>> [1500,2072,3264,1500,3941]
```

##### Rust (Synchronous)

```rust
        let _: bool = r
            .json_set(
                "bikes:inventory",
                "$.inventory.*[?(@.price<2000)].price",
                &json!(1500),
            )
            .expect("Failed to run JSON.SET");

        let res43: String = r
            .json_get("bikes:inventory", "$..price")
            .expect("Failed to run JSON.GET");
        println!("{res43}"); // >>> [1500,2072,3264,1500,3941]
```



JSONPath queries also work with other JSON commands that accept a path as an argument. For example, you can add a new color option for a set of headphones with [`JSON.ARRAPPEND`](https://redis.io/docs/latest/commands/json.arrappend):

Array updates with filters: Use JSON.ARRAPPEND with filter expressions to add elements to arrays matching conditions when you need to modify collections selectively

**Difficulty:** Advanced

**Builds upon:** update_filters1

**Commands:** JSON.ARRAPPEND, JSON.GET

**Complexity:**
- JSON.ARRAPPEND: O(1)
- JSON.GET: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> JSON.ARRAPPEND bikes:inventory '$.inventory.*[?(@.price<2000)].colors' '"pink"'
1) (integer) 3
2) (integer) 3
> JSON.GET bikes:inventory $..[*].colors
"[[\"black\",\"silver\",\"pink\"],[\"black\",\"white\"],[\"black\",\"silver\",\"pink\"]]"
```

##### C#

```csharp
        long?[] res47 = db.JSON().ArrAppend(
            "bikes:inventory", "$.inventory.*[?(@.price<2000)].colors", "pink"
        );
        Console.WriteLine(string.Join(", ", res47));    // >>> 3, 3

        RedisResult res48 = db.JSON().Get("bikes:inventory", path: "$..[*].colors");
        Console.WriteLine(res48);   // >>> [["black","silver","pink"],["black","white"],["black","silver","pink"]]
```

##### Go

```go
	res20, err := rdb.JSONArrAppend(ctx,
		"bikes:inventory",
		"$.inventory.*[?(@.price<2000)].colors",
		"\"pink\"",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res20) // >>> [3 3]

	res21, err := rdb.JSONGet(ctx, "bikes:inventory", "$..[*].colors").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res21)
	// >>> [["black","silver","pink"],["black","silver","pink"],["black","white"]]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> updateFilters2 = asyncCommands.jsonArrappend("bikes:inventory",
                    JsonPath.of("$.inventory.*[?(@.price<2000)].colors"), parser.createJsonValue("\"pink\"")).thenCompose(r -> {
                        System.out.println(r); // >>> [3, 3]

                        return asyncCommands.jsonGet("bikes:inventory", JsonPath.of("$..[*].colors"));
                    })
                    .thenAccept(System.out::println)
                    // >>> [[["black","silver","pink"],["black","white"],["black","silver","pink"]]]
                    .toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> updateFilters2 = reactiveCommands.jsonArrappend("bikes:inventory",
                    JsonPath.of("$.inventory.*[?(@.price<2000)].colors"), parser.createJsonValue("\"pink\"")).collectList()
                    .doOnNext(r -> {
                        System.out.println(r); // >>> [3, 3]
                    }).flatMap(r -> reactiveCommands.jsonGet("bikes:inventory", JsonPath.of("$..[*].colors")).collectList())
                    .doOnNext(System.out::println) // >>>
                                                   // [[["black","silver","pink"],["black","white"],["black","silver","pink"]]]
                    .then();
```

##### Java (Synchronous - Jedis)

```java
        List<Long> res43 = jedis.jsonArrAppendWithEscape(
            "bikes:inventory", new Path2("$.inventory.*[?(@.price<2000)].colors"),
            "\"pink\""
        );
        System.out.println(res43);  // >>> [3, 3]

        Object res44 = jedis.jsonGet("bikes:inventory", new Path2("$..[*].colors"));
        System.out.println(res44);
        // >>> [["black","silver","\"pink\""],["black","white"],["black","silver","\"pink\""]]
```

##### JavaScript (Node.js)

```javascript
const res41 = await client.json.arrAppend(
    "bikes:inventory", "$.inventory.*[?(@.price<2000)].colors", "pink"
);
console.log(res41);  //  [3, 3]

const res42 = await client.json.get("bikes:inventory", {
  path: "$..[*].colors"
});
console.log(res42);  //  [['black', 'silver', 'pink'], ['black', 'white'], ['black', 'silver', 'pink']]
```

##### PHP

```php
        $res20b = $r->jsonarrappend('bikes:inventory', '$.inventory.*[?(@.price<2000)].colors', '"pink"');
        echo json_encode($res20b) . PHP_EOL;
        // >>> [3,3]

        $res21b = $r->jsonget('bikes:inventory', '', '', '', '$..[*].colors');
        echo $res21b . PHP_EOL;
        // >>> [["black","silver","pink"],["black","white"],["black","silver","pink"]]
```

##### Python

```python
res20 = r.json().arrappend(
    "bikes:inventory", "$.inventory.*[?(@.price<2000)].colors", "pink"
)
print(res20)  # >>> [3, 3]

res21 = r.json().get("bikes:inventory", "$..[*].colors")
print(
    res21
)  # >>> [['black', 'silver', 'pink'], ['black', 'white'], ['black', 'silver', 'pink']]
```

##### Ruby

```ruby
res20 = r.json_arrappend(
  'bikes:inventory', '$.inventory.*[?(@.price<2000)].colors', 'pink'
)
p res20 # >>> [3, 3]

res21 = r.json_get('bikes:inventory', '$..[*].colors')
p res21
# >>> [["black", "silver", "pink"], ["black", "white"], ["black", "silver", "pink"]]
```

##### Rust (Asynchronous)

```rust
        let res44: Value = cmd("JSON.ARRAPPEND")
            .arg("bikes:inventory")
            .arg("$.inventory.*[?(@.price<2000)].colors")
            .arg("\"pink\"")
            .query_async(&mut r)
            .await
            .expect("Failed to run JSON.ARRAPPEND");
        print_redis_value(&res44); // >>> [3,3]

        let res45: String = r
            .json_get("bikes:inventory", "$..[*].colors")
            .await
            .expect("Failed to run JSON.GET");
        println!("{res45}");
        // >>> [["black","silver","pink"],["black","white"],["black","silver","pink"]]
```

##### Rust (Synchronous)

```rust
        let res44: Value = cmd("JSON.ARRAPPEND")
            .arg("bikes:inventory")
            .arg("$.inventory.*[?(@.price<2000)].colors")
            .arg("\"pink\"")
            .query(&mut r)
            .expect("Failed to run JSON.ARRAPPEND");
        print_redis_value(&res44); // >>> [3,3]

        let res45: String = r
            .json_get("bikes:inventory", "$..[*].colors")
            .expect("Failed to run JSON.GET");
        println!("{res45}");
        // >>> [["black","silver","pink"],["black","white"],["black","silver","pink"]]
```



## Projection expressions

The top level of a JSONPath query can be an expression that *computes* a value — arithmetic, a function call, a get-keys operator, and so on — rather than only selecting nodes from the document. A query that is a plain path (for example, `$.a.b`, `$..x`, or even a fully parenthesized path such as `($.a)`) still selects nodes; anything else (for example, `$.a + 1`, `-$.a`, `$.arr.length()`, `length($.arr)`, `$.obj~`, or `$.obj.keys()`) is a projection.

A projection that evaluates to *Nothing* produces an empty reply (`[]`).

Projection expressions: Use arithmetic, a function call, or the length of a path as a top-level query that computes a value instead of only selecting nodes

**Difficulty:** Advanced

**Commands:** JSON.SET, JSON.GET

**Complexity:**
- JSON.SET: O(M+N)
- JSON.GET: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> JSON.SET doc $ '{"a":2,"b":4,"arr":[1,2,3]}'
OK
> JSON.GET doc '$.a + 1'
"[3]"
> JSON.GET doc '$.a * $.b'
"[8]"
> JSON.GET doc '($.a + $.b) / 2'
"[3.0]"
> JSON.GET doc '$.arr.length()'
"[3]"
> JSON.GET doc '$.a / 0'
"[]"
```

##### C#

```csharp
        bool res64 = db.JSON().Set("doc", "$", "{\"a\":2,\"b\":4,\"arr\":[1,2,3]}");
        Console.WriteLine(res64);   // >>> True

        RedisResult res65 = db.JSON().Get("doc", path: "$.a + 1");
        Console.WriteLine(res65);   // >>> [3]

        RedisResult res66 = db.JSON().Get("doc", path: "$.a * $.b");
        Console.WriteLine(res66);   // >>> [8]

        RedisResult res67 = db.JSON().Get("doc", path: "($.a + $.b) / 2");
        Console.WriteLine(res67);   // >>> [3.0]

        RedisResult res68 = db.JSON().Get("doc", path: "$.arr.length()");
        Console.WriteLine(res68);   // >>> [3]

        RedisResult res69 = db.JSON().Get("doc", path: "$.a / 0");
        Console.WriteLine(res69);   // >>> []
```

##### Go

```go
	res1, err := rdb.JSONSet(ctx, "doc", "$",
		`{"a":2,"b":4,"arr":[1,2,3]}`,
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // >>> OK

	res2, err := rdb.JSONGet(ctx, "doc", `$.a + 1`).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2) // >>> [3]

	res3, err := rdb.JSONGet(ctx, "doc", `$.a * $.b`).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3) // >>> [8]

	res4, err := rdb.JSONGet(ctx, "doc", `($.a + $.b) / 2`).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4) // >>> [3.0]

	res5, err := rdb.JSONGet(ctx, "doc", `$.arr.length()`).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res5) // >>> [3]

	res6, err := rdb.JSONGet(ctx, "doc", `$.a / 0`).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res6) // >>> []
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> projBasicExample = asyncCommands
                    .jsonSet("doc", JsonPath.ROOT_PATH,
                            parser.createJsonValue("{\"a\":2,\"b\":4,\"arr\":[1,2,3]}"))
                    .thenCompose(res1 -> {
                        System.out.println(res1); // >>> OK
                        return asyncCommands.jsonGet("doc", JsonPath.of("$.a + 1"));
                    }).thenCompose(res2 -> {
                        System.out.println(res2); // >>> [[3]]
                        return asyncCommands.jsonGet("doc", JsonPath.of("$.a * $.b"));
                    }).thenCompose(res3 -> {
                        System.out.println(res3); // >>> [[8]]
                        return asyncCommands.jsonGet("doc", JsonPath.of("($.a + $.b) / 2"));
                    }).thenCompose(res4 -> {
                        System.out.println(res4); // >>> [[3.0]]
                        return asyncCommands.jsonGet("doc", JsonPath.of("$.arr.length()"));
                    }).thenCompose(res5 -> {
                        System.out.println(res5); // >>> [[3]]
                        return asyncCommands.jsonGet("doc", JsonPath.of("$.a / 0"));
                    }).thenAccept(res6 -> {
                        System.out.println(res6); // >>> [[]]
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> projBasicExample = reactiveCommands
                    .jsonSet("doc", JsonPath.ROOT_PATH, parser.createJsonValue("{\"a\":2,\"b\":4,\"arr\":[1,2,3]}"))
                    .doOnNext(res1 -> {
                        System.out.println(res1); // >>> OK
                    })
                    .flatMap(res1 -> reactiveCommands.jsonGet("doc", JsonPath.of("$.a + 1")).collectList())
                    .doOnNext(res2 -> {
                        System.out.println(res2); // >>> [[3]]
                    })
                    .flatMap(res2 -> reactiveCommands.jsonGet("doc", JsonPath.of("$.a * $.b")).collectList())
                    .doOnNext(res3 -> {
                        System.out.println(res3); // >>> [[8]]
                    })
                    .flatMap(res3 -> reactiveCommands.jsonGet("doc", JsonPath.of("($.a + $.b) / 2")).collectList())
                    .doOnNext(res4 -> {
                        System.out.println(res4); // >>> [[3.0]]
                    })
                    .flatMap(res4 -> reactiveCommands.jsonGet("doc", JsonPath.of("$.arr.length()")).collectList())
                    .doOnNext(res5 -> {
                        System.out.println(res5); // >>> [[3]]
                    })
                    .flatMap(res5 -> reactiveCommands.jsonGet("doc", JsonPath.of("$.a / 0")).collectList())
                    .doOnNext(res6 -> {
                        System.out.println(res6); // >>> [[]]
                    })
                    .then();
```

##### Java (Synchronous - Jedis)

```java
        String res64 = jedis.jsonSet("doc", new Path2("$"), "{\"a\":2,\"b\":4,\"arr\":[1,2,3]}");
        System.out.println(res64);    // >>> OK

        Object res65 = jedis.jsonGet("doc", new Path2("$.a + 1"));
        System.out.println(res65);    // >>> [3]

        Object res66 = jedis.jsonGet("doc", new Path2("$.a * $.b"));
        System.out.println(res66);    // >>> [8]

        Object res67 = jedis.jsonGet("doc", new Path("($.a + $.b) / 2"));
        System.out.println(res67);    // >>> [3.0]

        Object res68 = jedis.jsonGet("doc", new Path2("$.arr.length()"));
        System.out.println(res68);    // >>> [3]

        Object res69 = jedis.jsonGet("doc", new Path2("$.a / 0"));
        System.out.println(res69);    // >>> []
```

##### JavaScript (Node.js)

```javascript
const res64 = await client.json.set('doc', '$', { a: 2, b: 4, arr: [1, 2, 3] });
console.log(res64); // >>> OK

const res65 = await client.json.get('doc', { path: '$.a + 1' });
console.log(res65); // >>> [ 3 ]

const res66 = await client.json.get('doc', { path: '$.a * $.b' });
console.log(res66); // >>> [ 8 ]

const res67 = await client.json.get('doc', { path: '($.a + $.b) / 2' });
console.log(res67); // >>> [ 3 ]

const res68 = await client.json.get('doc', { path: '$.arr.length()' });
console.log(res68); // >>> [ 3 ]

const res69 = await client.json.get('doc', { path: '$.a / 0' });
console.log(res69); // >>> []
```

##### PHP

```php
        $res64 = $this->redis->jsonset('doc', '$', json_encode(
            ["a" => 2, "b" => 4, "arr" => [1, 2, 3]]
        ));
        echo $res64 . PHP_EOL; // >>> OK

        $res65 = $this->redis->jsonget('doc', '', '', '', '$.a + 1');
        echo $res65 . PHP_EOL; // >>> [3]

        $res66 = $this->redis->jsonget('doc', '', '', '', '$.a * $.b');
        echo $res66 . PHP_EOL; // >>> [8]

        $res67 = $this->redis->jsonget('doc', '', '', '', '($.a + $.b) / 2');
        echo $res67 . PHP_EOL; // >>> [3.0]

        $res68 = $this->redis->jsonget('doc', '', '', '', '$.arr.length()');
        echo $res68 . PHP_EOL; // >>> [3]

        $res69 = $this->redis->jsonget('doc', '', '', '', '$.a / 0');
        echo $res69 . PHP_EOL; // >>> []
```

##### Python

```python
res1 = r.json().set("doc", "$", {"a": 2, "b": 4, "arr": [1, 2, 3]})
print(res1)
# >>> True

res2 = r.json().get("doc", "$.a + 1")
print(res2)
# >>> [3]

res3 = r.json().get("doc", "$.a * $.b")
print(res3)
# >>> [8]

res4 = r.json().get("doc", "($.a + $.b) / 2")
print(res4)
# >>> [3.0]

res5 = r.json().get("doc", "$.arr.length()")
print(res5)
# >>> [3]

res6 = r.json().get("doc", "$.a / 0")
print(res6)
# >>> []
```

##### Ruby

```ruby
res1 = r.json_set('doc', '$', { 'a' => 2, 'b' => 4, 'arr' => [1, 2, 3] })
puts res1 # >>> OK

res2 = r.json_get('doc', '$.a + 1')
p res2 # >>> [3]

res3 = r.json_get('doc', '$.a * $.b')
p res3 # >>> [8]

res4 = r.json_get('doc', '($.a + $.b) / 2')
p res4 # >>> [3.0]

res5 = r.json_get('doc', '$.arr.length()')
p res5 # >>> [3]

res6 = r.json_get('doc', '$.a / 0')
p res6 # >>> []
```

##### Rust (Asynchronous)

```rust
        let _: bool = match r.json_set("doc", "$", &json!({"a":2,"b":4,"arr":[1,2,3]})).await {
            Ok(v) => v,
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        };

        match r.json_get("doc", "$.a + 1").await {
            Ok(res1) => {
                let res1: String = res1;
                println!("{res1}");    // >>> [3]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$.a * $.b").await {
            Ok(res2) => {
                let res2: String = res2;
                println!("{res2}");    // >>> [8]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "($.a + $.b) / 2").await {
            Ok(res3) => {
                let res3: String = res3;
                println!("{res3}");    // >>> [3.0]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$.arr.length()").await {
            Ok(res4) => {
                let res4: String = res4;
                println!("{res4}");    // >>> [3]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$.a / 0").await {
            Ok(res5) => {
                let res5: String = res5;
                println!("{res5}");    // >>> []
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

```

##### Rust (Synchronous)

```rust
        match r.json_set("doc", "$", &json!({"a":2,"b":4,"arr":[1,2,3]})) {
            Ok(res64) => {
                let res64: bool = res64;
                println!("{}", if res64 { "OK" } else { "(nil)" });    // >>> OK
            },
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$.a + 1") {
            Ok(res65) => {
                let res65: String = res65;
                println!("{res65}");    // >>> [3]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$.a * $.b") {
            Ok(res66) => {
                let res66: String = res66;
                println!("{res66}");    // >>> [8]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "($.a + $.b) / 2") {
            Ok(res67) => {
                let res67: String = res67;
                println!("{res67}");    // >>> [3.0]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$.arr.length()") {
            Ok(res68) => {
                let res68: String = res68;
                println!("{res68}");    // >>> [3]
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

        match r.json_get("doc", "$.a / 0") {
            Ok(res69) => {
                let res69: String = res69;
                println!("{res69}");    // >>> []
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }
```



When [`JSON.GET`](https://redis.io/docs/latest/commands/json.get) is given more than one path, projections and plain paths can be mixed, and each path becomes a key in the returned object. The order of keys in that object is not guaranteed.

Multi-path queries: Pass more than one path to JSON.GET to have each path's result returned under its own key in a single reply

**Difficulty:** Advanced

**Commands:** JSON.GET

**Complexity:**
- JSON.GET: O(N)

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> JSON.GET doc '$.a + 1' '$.b'
"{\"$.a + 1\":[3],\"$.b\":[4]}"
```

##### C#

```csharp
        bool res70 = db.JSON().Set("doc", "$", "{\"a\":2,\"b\":4,\"arr\":[1,2,3]}");
        Console.WriteLine(res70);   // >>> True

        RedisResult res71 = db.JSON().Get("doc", paths: new[] { "$.a + 1", "$.b" });
        Console.WriteLine(res71);   // >>> {"$.a + 1":[3],"$.b":[4]}
```

##### Go

```go
	res1, err := rdb.JSONSet(ctx, "doc", "$",
		`{"a":2,"b":4,"arr":[1,2,3]}`,
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // >>> OK

	raw, err := rdb.JSONGet(ctx, "doc", `$.a + 1`, `$.b`).Result()

	if err != nil {
		panic(err)
	}

	// A multi-path JSON.GET reply is a JSON object whose key order is not
	// guaranteed, so decode it into a map rather than printing the raw
	// string. Go's fmt package prints map keys in sorted order, which keeps
	// this example's output deterministic regardless of the order Redis
	// returns the paths in.
	res2 := map[string]interface{}{}

	if err := json.Unmarshal([]byte(raw), &res2); err != nil {
		panic(err)
	}

	fmt.Println(res2) // >>> map[$.a + 1:[3] $.b:[4]]
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> projMultipathExample = asyncCommands
                    .jsonSet("doc", JsonPath.ROOT_PATH,
                            parser.createJsonValue("{\"a\":2,\"b\":4,\"arr\":[1,2,3]}"))
                    .thenCompose(res7 -> {
                        System.out.println(res7); // >>> OK
                        return asyncCommands.jsonGet("doc", JsonPath.of("$.a + 1"), JsonPath.of("$.b"));
                    }).thenAccept(res8 -> {
                        // The multi-path JSON.GET reply is a single JSON object keyed by path,
                        // and Redis does not guarantee key order, so look up each path rather
                        // than comparing the object's rendered string.
                        JsonObject paths = res8.get(0).asJsonObject();
                        System.out.println(paths); // >>> {"$.a + 1":[3],"$.b":[4]}
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> projMultipathExample = reactiveCommands
                    .jsonSet("doc", JsonPath.ROOT_PATH, parser.createJsonValue("{\"a\":2,\"b\":4,\"arr\":[1,2,3]}"))
                    .doOnNext(res7 -> {
                        System.out.println(res7); // >>> OK
                    })
                    .flatMap(res7 -> reactiveCommands.jsonGet("doc", JsonPath.of("$.a + 1"), JsonPath.of("$.b"))
                            .collectList())
                    .doOnNext(res8 -> {
                        System.out.println(res8); // >>> [{"$.a + 1":[3],"$.b":[4]}]
                    })
                    .then();
```

##### Java (Synchronous - Jedis)

```java
        String res70 = jedis.jsonSet("doc", new Path2("$"), "{\"a\":2,\"b\":4,\"arr\":[1,2,3]}");
        System.out.println(res70);    // >>> OK

        Object res71 = jedis.jsonGet("doc", new Path2("$.a + 1"), new Path2("$.b"));
        System.out.println(res71);    // >>> {"$.a + 1":[3],"$.b":[4]} (a JSON object; key order is not guaranteed)
```

##### JavaScript (Node.js)

```javascript
const res70 = await client.json.set('doc', '$', { a: 2, b: 4, arr: [1, 2, 3] });
console.log(res70); // >>> OK

const res71 = await client.json.get('doc', { path: ['$.a + 1', '$.b'] });
console.log(res71); // >>> { '$.a + 1': [ 3 ], '$.b': [ 4 ] }
```

##### PHP

```php
        $res70 = $this->redis->jsonset('doc', '$', json_encode(
            ["a" => 2, "b" => 4, "arr" => [1, 2, 3]]
        ));
        echo $res70 . PHP_EOL; // >>> OK

        $res71 = $this->redis->jsonget('doc', '', '', '', '$.a + 1', '$.b');
        // The reply is a JSON object keyed by path; key order is not guaranteed.
        echo $res71 . PHP_EOL; // >>> {"$.a + 1":[3],"$.b":[4]} (key order not guaranteed)
```

##### Python

```python
res7 = r.json().set("doc", "$", {"a": 2, "b": 4, "arr": [1, 2, 3]})
print(res7)
# >>> True

res8 = r.json().get("doc", "$.a + 1", "$.b")
print(res8)
# >>> {'$.a + 1': [3], '$.b': [4]}
```

##### Ruby

```ruby
res7 = r.json_set('doc', '$', { 'a' => 2, 'b' => 4, 'arr' => [1, 2, 3] })
puts res7 # >>> OK

# The reply's key order is not guaranteed, so don't rely on it.
res8 = r.json_get('doc', '$.a + 1', '$.b')
p res8
```

##### Rust (Asynchronous)

```rust
        let _: bool = match r.json_set("doc", "$", &json!({"a":2,"b":4,"arr":[1,2,3]})).await {
            Ok(v) => v,
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        };

        match r.json_get("doc", &["$.a + 1", "$.b"]).await {
            Ok(res6) => {
                let res6: String = res6;
                // The reply's key order is not guaranteed, so parse it into a
                // Value and compare that structurally rather than relying on
                // the raw string's key order.
                println!("{res6}");
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

```

##### Rust (Synchronous)

```rust
        match r.json_set("doc", "$", &json!({"a":2,"b":4,"arr":[1,2,3]})) {
            Ok(res70) => {
                let res70: bool = res70;
                println!("{}", if res70 { "OK" } else { "(nil)" });    // >>> OK
            },
            Err(e) => {
                println!("Error setting doc: {e}");
                return;
            }
        }

        // A multi-path JSON.GET replies with an object keyed by path, but Redis does not
        // guarantee the key order in that reply, so this parses the JSON and compares it
        // structurally (map equality, order-independent) instead of comparing raw strings.
        match r.json_get::<_, _, String>("doc", vec!["$.a + 1", "$.b"]) {
            Ok(res71) => {
                let parsed: serde_json::Value = serde_json::from_str(&res71).unwrap();
                // Render with sorted keys purely for a deterministic, printable example —
                // the actual reply's key order can differ from run to run.
                let sorted: std::collections::BTreeMap<String, serde_json::Value> =
                    serde_json::from_value(parsed.clone()).unwrap();
                println!("{}", serde_json::to_string(&sorted).unwrap());    // >>> {"$.a + 1":[3],"$.b":[4]}
            },
            Err(e) => {
                println!("Error getting doc: {e}");
                return;
            }
        }

```



[`JSON.MGET`](https://redis.io/docs/latest/commands/json.mget) evaluates the projection independently for each key. A missing key, or a per-key evaluation error, yields a null reply for that key rather than failing the whole request.

## Legacy path syntax

RedisJSON v1 had the following path implementation. JSON v2 still supports this legacy path in addition to JSONPath.

Paths always begin at the root of a Redis JSON value. The root is denoted by a period character (`.`). For paths that reference the root's children, it is optional to prefix the path with the root.

Redis JSON supports both dot notation and bracket notation for object key access. The following paths refer to _headphones_, which is a child of _inventory_ under the root:

*   `.inventory.headphones`
*   `inventory["headphones"]`
*   `['inventory']["headphones"]`

To access an array element, enclose its index within a pair of square brackets. The index is 0-based, with 0 being the first element of the array, 1 being the next element, and so on. You can use negative offsets to access elements starting from the end of the array. For example, -1 is the last element in the array, -2 is the second to last element, and so on.

### JSON key names and path compatibility

By definition, a JSON key can be any valid JSON string. Paths, on the other hand, are traditionally based on JavaScript's (and Java's) variable naming conventions.

Although JSON can store objects that contain arbitrary key names, you can only use a legacy path to access these keys if they conform to these naming syntax rules:

1.  Names must begin with a letter, a dollar sign (`$`), or an underscore (`_`) character
2.  Names can contain letters, digits, dollar signs, and underscores
3.  Names are case-sensitive

## Time complexity of path evaluation

The time complexity of searching (navigating to) an element in the path is calculated from:

1. Child level - every level along the path adds an additional search
2. Key search - O(N)<sup>&#8224;</sup>, where N is the number of keys in the parent object
3. Array search - O(1)

This means that the overall time complexity of searching a path is _O(N*M)_, where N is the depth and M is the number of parent object keys.

<sup>&#8224;</sup> While this is acceptable for objects where N is small, access can be optimized for larger objects.

