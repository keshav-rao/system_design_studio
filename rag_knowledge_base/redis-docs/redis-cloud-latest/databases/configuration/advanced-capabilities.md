# Advanced capabilities

```json metadata
{
  "schema_version": 2,
  "title": "Advanced capabilities",
  "description": "Describes Redis Cloud Advanced capability options.",
  "categories": ["docs","operate","rc"],
  "tableOfContents": {"sections":[{"id":"essentials","title":"Redis Cloud Essentials"},{"children":[{"id":"search-and-query-sizing","title":"Search and query sizing"}],"id":"pro","title":"Redis Cloud Pro"}]}

,
  "codeExamples": []
}
```


Advanced capabilities extend Redis database functionality by adding new features and data types.  

Available options depend on your database plan and **Type**.

## Redis Cloud Essentials {#essentials}

All Redis Cloud Essentials databases with versions prior to Redis 8.0 support [Redis Stack](https://redis.io/docs/latest/operate/oss_and_stack), which enables the most frequently used capabilities.

![For Essentials, the Type setting in the General section includes an option for Redis.](https://redis.io/docs/latest/images/rc/new-database-general-type-free-stack.png)

When the database **Type** is set to _Redis_, the Advanced capabilities section of the database details page displays the advanced capabilities included with the database and their versions.

![For Essentials, the Database details page lists the capabilities and versions added by Redis Stack.](https://redis.io/docs/latest/images/rc/database-details-modules-stack-free.png)

Starting with Redis 8.0, all advanced capabilities provided by Redis Stack are included in Redis by default.

Redis Cloud is updated on a regular basis, which includes the advanced capabilities supported by the service. Versions displayed by the Redis Cloud console may vary from those shown above.  For the latest details of any capability, see [Redis Stack and Redis Software](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise). For more information about Redis Cloud version management, see [Redis version management](https://redis.io/docs/latest/operate/rc/databases/version-management).

## Redis Cloud Pro {#pro}

By default, Redis Cloud Pro databases load all supported advanced capabilities. For versions prior to Redis 8.0, you can choose to load specific capabilities when you create your database. To choose which capabilities to load for your Pro database, [create it with custom settings](https://redis.io/docs/latest/operate/rc/databases/create-database/create-pro-database-new) and select **More options** when adding your database in the **Sizing tab** to view advanced capability settings.

![For Pro databases, you can select the capabilities included in your database.](https://redis.io/docs/latest/images/rc/database-details-redis-module-select-flexible.png)

You can select more than one advanced capability for a database, though there are limits:

- The following advanced capabilities can be combined in Pro databases:

    - Search and query
    - JSON
    - Time series
    - Probabilistic

- [Active-Active databases](https://redis.io/docs/latest/operate/rc/databases/active-active/create-active-active-database) only support JSON and Search and query.

To remove a selected capability, clear its checkbox.

Starting with Redis 8.0, all advanced capabilities provided by Redis Stack are included in Redis by default. 

To learn more, see [Redis Stack](https://redis.io/docs/latest/develop/get-started) and [Redis Stack and Redis Software](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise). For more information about Redis Cloud version management, see [Redis version management](https://redis.io/docs/latest/operate/rc/databases/version-management).

### Search and query sizing

When you create a Pro database with [Search and Query](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/search), you must consider the sizing and throughput requirements for search and query when you define the dataset size and throughput for your database. 

Use the [Search and query sizing calculator](https://redis.io/redisearch-sizing-calculator/) to estimate your index size and throughput requirements.

- **Dataset Size**: Add the estimated index size from the Sizing calculator to your expected dataset size.
- **Throughput**: Enter the total estimated throughput from the Sizing calculator when you enter your throughput.
- **Query performance factor**: The query performance factor adds extra power specifically for search and query. Select a factor to increase your queries per second by that amount.

#### Query performance factor

The query performance factor adds extra compute power specifically for search and query. When you create a Pro database with search and query, you can increase your search queries per second by the selected factor.

![For Pro databases, you can select the query performance factor for your database.](https://redis.io/docs/latest/images/rc/database-details-query-performance-factor-pro.png)

We recommend testing your application with a test database to see your baseline queries per second and determine how much you want to boost your query performance. After you have determined your queries per second and your desired performance factor, [create a new database](https://redis.io/docs/latest/operate/rc/databases/create-database) with the desired performance factor and [migrate data](https://redis.io/docs/latest/operate/rc/databases/migrate-databases) from the test database to your new database.

For more info on how to use scalable search, see [Best practices for scalable Redis Search](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/search/scalable-query-best-practices).

The query performance factor is available for Redis Cloud Pro databases on Redis 7.2 and later.
