# Redis Search configuration compatibility with Redis Software

```json metadata
{
  "schema_version": 2,
  "title": "Redis Search configuration compatibility with Redis Software",
  "description": "Redis Search configuration settings supported by Redis Software and Redis Cloud.",
  "categories": ["docs","operate","stack"],
  "tableOfContents": {"sections":[{"id":"configure-search-in-redis-cloud","title":"Configure search in Redis Cloud"},{"id":"configure-search-in-redis-software","title":"Configure search in Redis Software"},{"id":"configuration-settings","title":"Configuration settings"}]}

,
  "codeExamples": []
}
```


To configure Redis Search in [Redis Software](https://redis.io/docs/latest/operate/rs) or [Redis Cloud](https://redis.io/docs/latest/operate/rc), use one of the following methods instead of [`FT.CONFIG SET`](https://redis.io/docs/latest/commands/ft.config-set).

## Configure search in Redis Cloud

For Redis Cloud:

- _Flexible or Annual [subscriptions](https://redis.io/docs/latest/operate/rc/subscriptions)_: contact [support](https://redis.com/company/support/) to request a configuration change.
    
- _Free or Fixed subscriptions_: you cannot change Redis Search configuration.

## Configure search in Redis Software

For Redis Software, use one of the following methods:

- Cluster Manager UI:

  1. From the **Databases** list, select the database, then click **Configuration**.

  1. Select the **Edit** button.

  1. In the **Capabilities** section, click **Parameters**.

  1. Enter the setting name and setting value in the **RediSearch** box.
  
      In the **Query Performance Factor** section, you can configure settings to improve query performance. See [Configure the query performance factor for Redis Search in Redis Software](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/search/query-performance-factor) for more information.

      ![The Parameters dialog includes sections to edit RediSearch settings and the Query Performance Factor settings.](https://redis.io/docs/latest/images/rs/screenshots/databases/rs-config-search-params.png)

  1. After you finish editing the module's configuration parameters, click **Done** to close the parameter editor.

  1. Click **Save**.

- [`rladmin tune db`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/tune#tune-db):

    ```sh
    $ rladmin tune db db:<ID|name> module_name search \
        module_config_params "setting-name setting-value"
    ```

- [Configure module](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/modules/config) REST API request:

    ```sh
    POST /v1/modules/config/bdb/<ID>
    {
      "modules": [
        {
          "module_name": "search",
          "module_args": "setting-name setting-value"
        }
      ]
    }
    ```

## Configuration settings

See [configuration parameters](https://redis.io/docs/latest/develop/ai/search-and-query/administration/configuration) in the Develop section for parameter details and compatibility with Redis Software and Redis Cloud.

