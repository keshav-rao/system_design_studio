# Graph configuration compatibility with Redis Software

```json metadata
{
  "schema_version": 2,
  "title": "Graph configuration compatibility with Redis Software",
  "description": "Graph configuration settings supported by Redis Software.",
  "categories": ["docs","operate","stack"],
  "tableOfContents": {"sections":[]}

,
  "codeExamples": []
}
```


You cannot use `GRAPH.CONFIG SET` to configure RedisGraph in [Redis Software](https://redis.io/docs/latest/operate/rs) or [Redis Cloud](https://redis.io/docs/latest/operate/rc). Instead, use one of the following methods.

For Redis Cloud:

- _Flexible or Annual [subscriptions](https://redis.io/docs/latest/operate/rc/subscriptions)_: contact [support](https://redis.com/company/support/) to request a configuration change.
    
- _Free or Fixed subscriptions_: you cannot change RedisGraph configuration.

For Redis Software, use either:

- [`rladmin tune db`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/tune#tune-db):

    ```sh
    $ rladmin tune db db:<ID|name> module_name graph \
        module_config_params "setting-name setting-value"
    ```

- [Configure module](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/modules/config) REST API request:

    ```sh
    POST /v1/modules/config/bdb/<ID>
    {
      "modules": [
        {
          "module_name": "graph",
          "module_args": "setting-name setting-value"
        }
      ]
    }
    ```

| Setting | Redis<br />Software | Redis<br />Cloud | Notes |
|:--------|:----------------------|:-----------------|:------|
| [CACHE_SIZE](https://github.com/RedisGraph/RedisGraph/blob/master/docs/docs/configuration.md#cache_size) | <span title="Supported">&#x2705; Supported</span><br /><span><br /></span> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Not supported"><nobr>&#x274c; Free & Fixed</nobr></span> | Default: 25 |
| [MAX_QUEUED_QUERIES](https://github.com/RedisGraph/RedisGraph/blob/master/docs/docs/configuration.md#max_queued_queries) | <span title="Supported">&#x2705; Supported</span><br /><span><br /></span> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Not supported"><nobr>&#x274c; Free & Fixed</nobr></span> | Default: 25 |
| [NODE_CREATION_BUFFER](https://github.com/RedisGraph/RedisGraph/blob/master/docs/docs/configuration.md#node_creation_buffer) | <span title="Supported">&#x2705; Supported</span><br /><span><br /></span> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Not supported"><nobr>&#x274c; Free & Fixed</nobr></span> | Default: 16384 |
| [OMP_THREAD_COUNT](https://github.com/RedisGraph/RedisGraph/blob/master/docs/docs/configuration.md#omp_thread_count) | <span title="Supported">&#x2705; Supported</span><br /><span><br /></span> | <span title="Supported">&#x2705; Flexible & Annual\*</span><br /><span title="Not supported"><nobr>&#x274c; Free & Fixed</nobr></span> | \* Updates automatically when you change your plan.<br /><br />Redis Software default: Set by plan<br /><br />Redis Cloud defaults:<br />• Flexible & Annual: Set by plan<br />• Free & Fixed: 1<br /> |
| [QUERY_MEM_CAPACITY](https://github.com/RedisGraph/RedisGraph/blob/master/docs/docs/configuration.md#query_mem_capacity) | <span title="Supported">&#x2705; Supported</span><br /><span><br /></span> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Not supported"><nobr>&#x274c; Free & Fixed</nobr></span> | Default: 100000000 |
| [RESULTSET_SIZE](https://github.com/RedisGraph/RedisGraph/blob/master/docs/docs/configuration.md#resultset_size) | <span title="Supported">&#x2705; Supported</span><br /><span><br /></span> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Not supported"><nobr>&#x274c; Free & Fixed</nobr></span> | Default: 10000 |
| [THREAD_COUNT](https://github.com/RedisGraph/RedisGraph/blob/master/docs/docs/configuration.md#thread_count) | <span title="Supported">&#x2705; Supported</span><br /><span><br /></span> | <span title="Supported">&#x2705; Flexible & Annual\*</span><br /><span title="Not supported"><nobr>&#x274c; Free & Fixed</nobr></span> | \* Updates automatically when you change your plan.<br /><br />Redis Software default: Set by plan<br /><br />Redis Cloud defaults:<br />• Flexible & Annual: Set by plan<br />• Free & Fixed: 1<br /> |
| [TIMEOUT](https://github.com/RedisGraph/RedisGraph/blob/master/docs/docs/configuration.md#timeout) | <span title="Supported">&#x2705; Supported</span><br /><span><br /></span> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Not supported"><nobr>&#x274c; Free & Fixed</nobr></span> | Default: 100 |
| [VKEY_MAX_ENTITY_COUNT](https://github.com/RedisGraph/RedisGraph/blob/master/docs/docs/configuration.md#vkey_max_entity_count) | <span title="Supported">&#x2705; Supported</span><br /><span><br /></span> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Not supported"><nobr>&#x274c; Free & Fixed</nobr></span> | Default: 100000 |

