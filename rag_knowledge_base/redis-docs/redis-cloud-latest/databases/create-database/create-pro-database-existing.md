# Create a Pro database in an existing subscription

```json metadata
{
  "schema_version": 2,
  "title": "Create a Pro database in an existing subscription",
  "description": "Shows how to create a Pro database in an existing subscription",
  "categories": ["docs","operate","rc"],
  "tableOfContents": {"sections":[{"id":"general-section","title":"General section"},{"id":"performance-section","title":"Performance section"},{"id":"durability-section","title":"Durability section"},{"id":"tags-section","title":"Tags section"},{"id":"security-section","title":"Security section"},{"id":"alerts-section","title":"Alerts section"},{"id":"billing-unit-types","title":"Billing unit types"}]}

,
  "codeExamples": []
}
```


> [!NOTE]
> This guide shows how to create a Pro database in an existing subscription.
> - If you don't yet have a Pro subscription, see [Create a Pro database with a new subscription](https://redis.io/docs/latest/operate/rc/databases/create-database/create-pro-database-new).
> - If you'd rather create an Essentials database, see [Create an Essentials database](https://redis.io/docs/latest/operate/rc/databases/create-database/create-essentials-database).

To create a database in an already existing Pro subscription: 

1. Sign in to the [Redis Cloud console](https://cloud.redis.io).

2. Select the **New database** button.

    ![The New Database button creates a new database.](https://redis.io/docs/latest/images/rc/button-database-new.png)

    This displays the **Create database** screen.

1. Select the type of [subscription](https://redis.io/docs/latest/operate/rc/subscriptions) you need. For this guide, select **Existing subscription**, and then select your existing Pro subscription from the list.

    ![The Subscription selection panel with Pro selected and an existing subscription selected.](https://redis.io/docs/latest/images/rc/create-database-subscription-pro-existing.png)

After you select your existing subscription from the list, select **Continue** to go to the **New database** page.

You can also select your subscription from the [subscription list](https://redis.io/docs/latest/operate/rc/subscriptions/view-pro-subscription) and select **Create database in this subscription**.

![The Create database in this subscription button.](https://redis.io/docs/latest/images/rc/button-add-new-to-pro.png)

The **New database** page is divided into sections, each dedicated to a specific category of settings. The following sections provide more details.

When you've configured your new database, click the **Activate database** button to create and activate it.

![Use the Activate database button to create and activate your database.](https://redis.io/docs/latest/images/rc/button-database-activate.png)

## General section

The **General** section defines basic properties about your database.

![The general section of the New Database screen.](https://redis.io/docs/latest/images/rc/database-new-flexible.png)

The available settings vary according to your subscription plan:

| Setting name              | Description                                                                                                                                                                                                                                                                                                       |
|:--------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Subscription**          | Read-only description of your Pro subscription, including cloud provider and region                                                                                                                                                                                                                              |
| **Database name**         | A name for your database (_required_)                                                                                                                                                                                                                                                                             |
| **Database port**         | Automatically or manually assigns a database port (range: 10000-19999).  You cannot assign a port that is reserved or already in use.                                                                                                                                                                                      |
| **Database version**         | The Redis version of your database. We recommend you choose the latest available version.                                                                                                                                                                                      |
| **Type**                  | Controls advanced database capabilities and protocol.  Supported values include _Redis_ and _Memcached_                                                                       |
| **Advanced capabilities** | [Advanced features and data types](https://redis.io/docs/latest/operate/rc/databases/configuration/advanced-capabilities) used by the database. Starting with Redis 8.0, all advanced capabilities are included in Redis by default. |
| **Query performance factor** | *(Search and query databases on Redis 7.2 or later only)* Adds additional compute power to process your query and vector search workloads and boost your queries per second. See [Search and query sizing](https://redis.io/docs/latest/operate/rc/databases/configuration/advanced-capabilities#search-and-query-sizing) for more information. |
| **Supported Protocol(s)** | Choose between RESP2 and RESP3 _(Redis 7.2 only)_. See [Redis serialization protocol](https://redis.io/docs/latest/develop/reference/protocol-spec#resp-versions) for details                                                                                                                                                   |

## Performance section

The **Performance** section lets you manage the maximum size, throughput, and hashing policy for a database.

![Use the Performance section to control the size, throughput, and hashing policy for a database.](https://redis.io/docs/latest/images/rc/database-new-flexible-scalability.png)

| Setting name        | Description                                                                                                                                                                                                                                                                                                                                   |
|:--------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Dataset size**    | Maximum size (in GB) for your dataset. See [Dataset size](https://redis.io/docs/latest/operate/rc/databases/configuration/sizing#dataset-size) for sizing considerations. <br/> Databases with Search and query have specific size requirements, see [Search and query sizing](https://redis.io/docs/latest/operate/rc/databases/configuration/advanced-capabilities#search-and-query-sizing) for more information. |
| **Throughput**      | Defines throughput in terms of maximum operations per second for the database. See [Throughput](https://redis.io/docs/latest/operate/rc/databases/configuration/sizing#throughput) for more info. <br/> Databases with Search and query have specific throughput requirements, see [Search and query sizing](https://redis.io/docs/latest/operate/rc/databases/configuration/advanced-capabilities#search-and-query-sizing) for more information. |
| **High availability**    | Indicates whether a replica copy of the database is maintained in case the primary database becomes unavailable. See [High availability](https://redis.io/docs/latest/operate/rc/databases/configuration/high-availability) for more info|
| **Query performance factor** | *(Search and query databases on Redis 7.2 or later)* Adds additional compute power to process your query and vector search workloads and boost your queries per second. See [Search and query sizing](https://redis.io/docs/latest/operate/rc/databases/configuration/advanced-capabilities#search-and-query-sizing) for more information. |
| **Hashing policy**  | Defines the [hashing policy](https://redis.io/docs/latest/operate/rc/databases/configuration/clustering#manage-the-hashing-policy).  |
| **OSS Cluster API** | Activates the [OSS Cluster API](https://redis.io/docs/latest/operate/rc/databases/configuration/clustering#oss-cluster-api) for a database.<br/> After you select OSS Cluster API, you can select **Use external endpoint** if you want to use the external endpoint for the database. Selecting **Use external endpoint** will block the private endpoint for this database. |

## Durability section

The **Durability** section helps you keep your database (and your data) available when problems occur.

![Use the Durability settings to keep your database (and data) available when problems occur.](https://redis.io/docs/latest/images/rc/database-new-flexible-durability.png)


| Setting name             | Description                                                                                                                                                                |
|:-------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Data persistence**     | Defines the data persistence policy, if any. See [Data persistence](https://redis.io/docs/latest/operate/rc/databases/configuration/data-persistence).            |
| **Data eviction policy** | Configures which [policy](https://redis.io/docs/latest/operate/rc/databases/configuration/data-eviction-policies) is applied when your database reaches its memory limit.              |
| **Remote backup**        | When enabled, identifies a location and interval for [data backups](https://redis.io/docs/latest/operate/rc/databases/back-up-data). |
| **Active-Passive Redis** | When enabled, identifies a path to the linked database. See [Migrate data](https://redis.io/docs/latest/operate/rc/databases/migrate-databases) for more information.           |

## Tags section

The **Tags** section lets you add [tags](https://redis.io/docs/latest/operate/rc/databases/tag-database) to the database.

![Use the Tag settings to add tags to the database.](https://redis.io/docs/latest/images/rc/database-new-tags.png)

Select **Add tag** to add a tag.

![The Add tag button.](https://redis.io/docs/latest/images/rc/tags-button-add-tag.png)

You can select the tag's **Key** and **Value** from the suggestions, or you can enter your own.

![The New tag fields.](https://redis.io/docs/latest/images/rc/tags-new-tag.png)

A valid tag must follow these guidelines:
- Tag keys must be between 1 and 64 characters long, and values must be at least 1 character long.
- Tags can only have lowercase letters, numbers, spaces, and these special characters: `-`, `_`, `.`, `+`, `@`, and `:`.

After you add your first tag, you can:

- Select the **Key** or **Value** field of an existing tag and enter new text to edit it.

- Select **Delete** next to a tag to delete it.

    ![Delete button.](https://redis.io/docs/latest/images/rc/icon-delete-lb.png)

- Select **Add additional tag** to add another tag.

    ![The Add additional tag button.](https://redis.io/docs/latest/images/rc/tags-button-add-additional-tag.png)

## Security section

The **Security** section helps you control access to your database.

![Use the Security settings to control access to your database.](https://redis.io/docs/latest/images/rc/database-new-flexible-security.png)


| Setting name                       | Description                                                                                                                                                                           |
|:-----------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Default user**                   | When enabled, permits access using the `default` username and a simple password (see [Default User](https://redis.io/docs/latest/operate/rc/security/access-control/data-access-control/default-user)). Turn on [Role-based access control](https://redis.io/docs/latest/operate/rc/security/access-control/data-access-control/role-based-access-control) to turn off this setting.              |
| **Default user password**                 | Password assigned to the database when created.                                                                                                                                        |  
| **CIDR allow list**                | [Allow list](https://redis.io/docs/latest/operate/rc/security/cidr-whitelist) of IP addresses/security groups permitted to access the database |
| **Transport layer security (TLS)** | Enables [transport layer security](https://redis.io/docs/latest/operate/rc/security/database-security/tls-ssl) (TLS) encryption for database access.          |


## Alerts section

The **Alerts** section defines notification emails sent to your account and the conditions that trigger them.

![The Alerts section defines the notification emails and their triggering conditions.](https://redis.io/docs/latest/images/rc/database-new-flexible-alerts.png)

The available alerts vary according to the plan type. See [Configure alerts](https://redis.io/docs/latest/operate/rc/databases/monitor-performance#configure-metric-alerts) for more information.

## Billing unit types

The Redis Billing Unit types associated with your Pro subscription depend on your database memory size and throughput requirements.

| Billing unit type | Capacity (Memory/Throughput) |
|:------------|:----------|
| Pico | 100MB / 100 ops/sec |
| Nano | 500MB / 500 ops/sec |
| Micro | 1GB / 1K ops/sec |
| High-throughput | 2.5GB / 25K ops/sec |
| Small | 12.5GB / 12.5K ops/sec |
| Large | 25GB  / 25K ops/sec |
| Very large<sup>[1](#table-note-1)</sup> | 50GB / 5K ops/sec |
| XLarge<sup>[2](#table-note-2)</sup> | 50GB / 10K ops/sec |
| Flex-10<sup>[3](#table-note-3)</sup> | 50GB / 5K ops/sec |
| Flex-20<sup>[3](#table-note-3)</sup> | 50GB / 10K ops/sec |
| Flex-30<sup>[3](#table-note-3)</sup> | 50GB / 15K ops/sec |
| Flex-40<sup>[3](#table-note-3)</sup> | 50GB / 20K ops/sec |
| Flex-50<sup>[3](#table-note-3)</sup> | 50GB / 25K ops/sec |

1. <a name="table-note-1" style="display: block; height: 80px; margin-top: -80px;"></a>Used for databases with Auto Tiering before Redis 7.2.

2. <a name="table-note-2" style="display: block; height: 80px; margin-top: -80px;"></a>Used for hosted databases with Auto Tiering between Redis 7.2 and Redis 8.2. 

3. <a name="table-note-3" style="display: block; height: 80px; margin-top: -80px;"></a>Used for Redis Flex databases for Redis 8.2 or later. Available Flex billing units depend on the RAM percentage you set for your database.

Prices vary according to the cloud provider and region.  Minimum prices apply.
