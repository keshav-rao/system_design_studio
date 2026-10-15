# Triggers and functions

```json metadata
{
  "schema_version": 2,
  "title": "Triggers and functions",
  "description": "Trigger and execute JavaScript functions in the Redis process",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"quick-links","title":"Quick links"},{"id":"primary-features","title":"Primary features"},{"id":"cluster-support","title":"Cluster support"},{"children":[{"id":"blog-posts","title":"Blog posts"}],"id":"references","title":"References"},{"id":"overview","title":"Overview"}]}

,
  "codeExamples": []
}
```


[![discord](https://img.shields.io/discord/697882427875393627?style=flat-square)](https://discord.gg/xTbqgTB)
[![Github](https://img.shields.io/static/v1?label=&message=repository&color=5961FF&logo=github)](https://github.com/RedisGears/RedisGears/)

The triggers and functions feature of Redis Stack allows running JavaScript functions inside Redis. These functions can be executed on-demand, by an event-driven trigger, or by a stream processing trigger.

## Quick links
* [Command documentation](https://github.com/RedisGears/RedisGears/tree/master/docs/commands)
* [Source code](https://github.com/RedisGears/RedisGears)
* [Latest release](https://github.com/RedisGears/RedisGears/releases)
* [Docker image](https://hub.docker.com/r/redis/redis-stack-server/)

## Primary features

* JavaScript engine for functions
* On-demand functions
* Keyspace triggers
* Stream triggers
* Async handling of functions
* Read data from across the cluster

## Cluster support

Triggers and functions support deployment and execution of functions across a cluster. Functions are executed on the correct shard based on the key that is changed or read functions can be executed on all to return a correct view of the data.

## References

### Blog posts

- [Expanding the Database Trigger Features in Redis](https://redis.com/blog/database-trigger-features/)

## Overview

