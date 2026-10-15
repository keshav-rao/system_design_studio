# Search commands in MULTI/EXEC transactions and Lua scripts

```json metadata
{
  "schema_version": 2,
  "title": "Search commands in MULTI/EXEC transactions and Lua scripts",
  "description": "How Redis Search commands behave inside MULTI/EXEC transactions and Lua scripts",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"standalone-and-single-shard-deployments","title":"Standalone and single-shard deployments"},{"id":"multi-shard-deployments-oss-cluster-and-redis-software-with-multiple-shards","title":"Multi-shard deployments (OSS Cluster and Redis Software with multiple shards)"},{"id":"related-commands","title":"Related commands"}]}

,
  "codeExamples": []
}
```


Redis Search commands ([`FT.SEARCH`](https://redis.io/docs/latest/commands/ft.search),
[`FT.AGGREGATE`](https://redis.io/docs/latest/commands/ft.aggregate),
[`FT.HYBRID`](https://redis.io/docs/latest/commands/ft.hybrid),
[`FT.PROFILE`](https://redis.io/docs/latest/commands/ft.profile), and
[`FT.CURSOR READ`](https://redis.io/docs/latest/commands/ft.cursor-read))
can be used inside [`MULTI`](https://redis.io/docs/latest/commands/multi)/[`EXEC`](https://redis.io/docs/latest/commands/exec)
transactions and [Lua scripts](https://redis.io/docs/latest/develop/programmability/lua-api),
but the behavior differs depending on your deployment topology.

## Standalone and single-shard deployments

Query commands inside a `MULTI`/`EXEC` block or Lua script (including when issued
through a client pipeline that wraps commands in a transaction) execute synchronously
on the main Redis thread, regardless of the
[`search-workers`](https://redis.io/docs/latest/develop/ai/search-and-query/administration/configuration#search-workers)
setting.

The worker thread pool is bypassed in this context because Redis transactions
require all commands to complete sequentially without yielding to other clients.
As a result, queries inside transactions do not benefit from the parallelism
provided by `search-workers > 0`, but they execute correctly and return results
as expected.

## Multi-shard deployments (OSS Cluster and Redis Software with multiple shards)

Redis Search commands inside a `MULTI`/`EXEC` block or a Lua script are rejected with
the following error:

```
Cannot perform FT.SEARCH: Cannot block
```

This is because the coordinator must fan out the query to multiple shards and
collect results asynchronously, which is incompatible with the sequential
execution model of transactions. This limitation applies regardless of the
`search-workers` setting.

## Related commands

- [`FT.SEARCH`](https://redis.io/docs/latest/commands/ft.search)
- [`FT.AGGREGATE`](https://redis.io/docs/latest/commands/ft.aggregate)
- [`FT.HYBRID`](https://redis.io/docs/latest/commands/ft.hybrid)
- [`FT.PROFILE`](https://redis.io/docs/latest/commands/ft.profile)
- [`FT.CURSOR READ`](https://redis.io/docs/latest/commands/ft.cursor-read)
- [`MULTI`](https://redis.io/docs/latest/commands/multi)
- [`EXEC`](https://redis.io/docs/latest/commands/exec)

