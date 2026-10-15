# Client-side caching compatibility with Redis Software and Redis Cloud

```json metadata
{
  "schema_version": 2,
  "title": "Client-side caching compatibility with Redis Software and Redis Cloud",
  "description": "Redis Software and Redis Cloud compatibility with client-side caching.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"id":"required-database-versions","title":"Required database versions"},{"id":"supported-resp-versions","title":"Supported RESP versions"},{"id":"two-connections-mode-with-redirect-not-supported","title":"Two connections mode with REDIRECT not supported"},{"id":"change-tracking_table_max_keys-for-a-database","title":"Change tracking_table_max_keys for a database"},{"id":"change-default-tracking_table_max_keys","title":"Change default tracking_table_max_keys"}]}

,
  "codeExamples": []
}
```


Redis Software and Redis Cloud support [client-side caching](https://redis.io/docs/latest/develop/clients/client-side-caching) for databases with Redis versions 7.4 or later.

## Required database versions

Client-side caching in Redis Software and Redis Cloud requires Redis database versions 7.4 or later.

The following table shows the differences in client-side caching support by product:

| Redis product           | Client-side caching support |
|-------------------------|-----------------------------|
| Redis Open Source       | Redis v6.0 and later |
| Redis Cloud             | Redis database v7.4 and later |
| Redis Software          | Redis database v7.4 and later |

## Supported RESP versions

Client-side caching in Redis Software and Redis Cloud requires [RESP3](https://redis.io/docs/latest/develop/reference/protocol-spec#resp-versions).

The following table shows the differences in client-side caching support for RESP by product:

| Redis product with client-side caching  | RESP2 | RESP3 |
|-------------------------|-------|-------|
| Redis Open Source       | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| Redis Cloud             | <span title="Not supported">&#x274c;</span> | <span title="Supported">&#x2705;</span> |
| Redis Software          | <span title="Not supported">&#x274c;</span> | <span title="Supported">&#x2705;</span> |

## Two connections mode with REDIRECT not supported

Unlike Redis Open Source, Redis Software and Redis Cloud do not support [two connections mode](https://redis.io/docs/latest/develop/reference/client-side-caching#two-connections-mode) or the `REDIRECT` option for [`CLIENT TRACKING`](https://redis.io/docs/latest/commands/client-tracking).

## Change tracking_table_max_keys for a database

When client-side caching is enabled, Redis uses an invalidation table to track which keys are cached by each connected client.

The configuration setting `tracking-table-max-keys` determines the maximum number of keys stored in the invalidation table and is set to `1000000` keys by default. Redis Software does not support using `CONFIG SET` to change this value, but you can use the REST API or rladmin instead.

To change `tracking_table_max_keys` for a database in a Redis Software cluster:

- [`rladmin tune db`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/tune#tune-db):

    ```sh
    rladmin tune db db:<ID> tracking_table_max_keys 2000000
    ```

    You can use the database name in place of `db:<ID>` in the preceding command.

- [Update database configuration](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/bdbs#put-bdbs) REST API request:

    ```sh
    PUT /v1/bdbs/<uid> 
    { "tracking_table_max_keys": 2000000 }
    ```

## Change default tracking_table_max_keys

The cluster-wide option `default_tracking_table_max_keys_policy` determines the default value of `tracking_table_max_keys` for new databases in a Redis Software cluster. `default_tracking_table_max_keys_policy` is set to `1000000` keys by default.

To change `default_tracking_table_max_keys_policy`, use one of the following methods:

- [`rladmin tune cluster`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/tune#tune-cluster)

    ```sh
    rladmin tune cluster default_tracking_table_max_keys_policy 2000000
    ```

- [Update cluster policy](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/cluster/policy#put-cluster-policy) REST API request:

    ```sh
    PUT /v1/cluster/policy 
    { "default_tracking_table_max_keys_policy": 2000000 }
    ```

