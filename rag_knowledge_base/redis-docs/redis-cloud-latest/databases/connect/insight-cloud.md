# Use Redis Insight on Redis Cloud

```json metadata
{
  "schema_version": 2,
  "title": "Use Redis Insight on Redis Cloud",
  "description": "Shows how to open your database in a browser-based version of Redis Insight and lists the features that are available.",
  "categories": ["docs","operate","rc","redisinsight"],
  "tableOfContents": {"sections":[{"id":"browse","title":"Browse"},{"id":"cli-and-command-helper","title":"CLI and Command Helper"},{"id":"workbench","title":"Workbench"},{"id":"insights","title":"Insights"}]}

,
  "codeExamples": []
}
```


[Redis Insight](https://redis.io/docs/latest/develop/tools/insight) is a free Redis GUI that lets you visualize your Redis data and learn more about Redis.

You can either [install Redis Insight](https://redis.io/docs/latest/develop/tools/insight) on your computer, or you can open your database in Redis Insight directly on Redis Cloud.

> [!NOTE]
> Opening your database with Redis Insight in your browser is only available for Essentials databases. For all other databases, [install Redis Insight](https://redis.io/docs/latest/develop/tools/insight) on your computer and [open Redis Insight](https://redis.io/docs/latest/operate/rc/databases/connect#ri-app) from the database page.

To open your database with Redis Insight on Redis Cloud, select **Open with Redis Insight** on the [database screen](https://redis.io/docs/latest/operate/rc/databases/view-edit-database).

![Open with Redis Insight](https://redis.io/docs/latest/images/rc/rc-ri-open.png)

Redis Insight will open in a new tab. 

This browser-based version of Redis Insight has a subset of the features of Redis Insight. For other Redis Insight features, [install Redis Insight](https://redis.io/docs/latest/develop/tools/insight) on your computer and [open Redis Insight](https://redis.io/docs/latest/operate/rc/databases/connect#ri-app) from the database page.

## Browse

The **Browse** tab lets you browse, filter, and visualize your Redis data structures.

- Create, read, update, and delete lists, hashes, strings, sets, sorted sets, streams, and [JSON](https://redis.io/docs/latest/develop/data-types/json)
- Filter keys by key name or pattern, and by key type
- Group keys according to their namespaces

    ![Keys in a database grouped by namespace.](https://redis.io/docs/latest/images/rc/rc-ri-browser-group.png)

- View, validate, and manage your key values in a human-readable format using formatters that prettify and highlight data in different formats (for example, Unicode, JSON, MessagePack, HEX, and ASCII)

    ![Human-readable view of a hash key.](https://redis.io/docs/latest/images/rc/rc-ri-browser-view.png)

- Search by key values using your [search indexes](https://redis.io/docs/latest/develop/ai/search-and-query)

    ![Search for keys using a search index.](https://redis.io/docs/latest/images/rc/rc-ri-browser-search.png)

If you don't have any Redis data yet, you can select **Load sample data** to add sample data into your database.

![Load Sample Data button](https://redis.io/docs/latest/images/rc/rc-ri-load-data.png)

## CLI and Command Helper

The **CLI** lets you run Redis commands directly. 

![The CLI and command helper](https://redis.io/docs/latest/images/rc/rc-ri-cli.png)

The CLI integrates with a **Command Helper** that lets you search and read information about Redis commands.

## Workbench

The **Workbench** is an advanced command line interface with intelligent command auto-complete and complex data visualization support.

![The Workbench](https://redis.io/docs/latest/images/rc/rc-ri-workbench.png)

## Insights

The **Insights** panel provides interactive tutorials and recommendations to help you optimize your database performance and memory usage.

![The Insights panel](https://redis.io/docs/latest/images/rc/rc-ri-insights.png)

From the **Workbench** of an empty database, select **Explore** to view the **Insights** panel.

![The Explore button](https://redis.io/docs/latest/images/rc/rc-ri-explore-button.png)

You can also select the **Insights** button in the top-right corner to view the **Insights** panel.

![The Insights button](https://redis.io/docs/latest/images/rc/rc-ri-insights-button.png)


