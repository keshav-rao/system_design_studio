# Create a Flex database

```json metadata
{
  "schema_version": 2,
  "title": "Create a Flex database",
  "description": "Shows how to create a Flex database on Redis Cloud and describes the best use cases for Flex.",
  "categories": ["docs","operate","rc"],
  "tableOfContents": {"sections":[{"id":"when-to-use-flex","title":"When to use Flex"},{"children":[{"id":"redis-search-on-flex-beta","title":"Redis Search on Flex (Beta)"},{"id":"ram-percentage","title":"RAM percentage"},{"id":"key-and-value-sizes","title":"Key and value sizes"}],"id":"best-practices-and-limitations","title":"Best practices and limitations"},{"children":[{"id":"redis-cloud-essentials","title":"Redis Cloud Essentials"},{"id":"redis-cloud-pro","title":"Redis Cloud Pro"}],"id":"create-a-flex-database","title":"Create a Flex database"},{"id":"troubleshooting","title":"Troubleshooting"}]}

,
  "codeExamples": []
}
```


Flex allows your dataset to span both high-performance RAM and cost-efficient dedicated Flash memory. Flex automatically manages data placement between the two tiers, keeping frequently accessed (“hot”) data in RAM for sub-millisecond latency, while moving less active (“warm”) data to Flash to optimize capacity and cost. This dual memory architecture delivers predictable performance at scale, enabling larger datasets without compromising speed or operational simplicity.

Flex databases are currently compatible with most existing Redis applications, except for applications that use Time Series. [Redis Search](https://redis.io/docs/latest/develop/ai/search-and-query) is available on Flex databases on Redis Cloud Pro as a beta feature; see [Redis Search on Flex](#redis-search-on-flex-beta).

Flex is available on both Redis Cloud Essentials and Redis Cloud Pro.

## When to use Flex

Flex is ideal for workloads that demand large-scale, low-latency data access with the flexibility to optimize cost and performance.

Consider Flex when you need to:

- Run Redis at terabyte scale while maintaining high throughput and sub-10 ms latency.
- Power real-time feature stores for machine learning applications such as fraud detection, recommendation systems, and personalization engines.
- Operate large distributed caches that require elastic scaling and consistent performance under heavy load.
- Optimize infrastructure cost by combining high-speed RAM with cost-efficient Flash storage through Flex's automatic data tiering.

Flex is **not** a durable data store. It is designed for performance, elasticity, and scalability, not for long-term data persistence. While Flex can temporarily retain data in memory or Flash, it should not be used as a primary system of record or persistent storage layer.

For workloads that require durability and recovery across restarts or failures, use Redis Cloud's [Data persistence](https://redis.io/docs/latest/operate/rc/databases/configuration/data-persistence) features.

## Best practices and limitations

### Redis Search on Flex (Beta)

[Redis Search](https://redis.io/docs/latest/develop/ai/search-and-query) on Flex databases is available as a beta feature on Redis Cloud Pro. It isn't available on Redis Cloud Essentials.

To use it, enable the beta flag for Redis Search on Flex in the Redis Cloud console for your Redis Cloud Pro subscription, then create a Flex database with a Redis Search index on tiered storage.

The beta supports:

- HASH documents
- `TEXT` fields, including prefix, infix, suffix, wildcard, and fuzzy matching
- `TAG` fields
- `VECTOR` fields with `HNSW` and `FLAT` indexes
- Loading fields from the keyspace with `SORTBY` and `RETURN`
- High availability, persistence, backup, and upgrades

JSON documents, `NUMERIC` and `GEO` fields, `FT.AGGREGATE`, `FT.HYBRID`, and background indexing aren't yet available for Redis Search on Flex, even though they're available for Redis Search on Redis Software today. As a beta feature, the supported feature set will continue to expand ahead of general availability.

Terraform support for Redis Search on Flex is available at Preview level.

### RAM percentage

On Redis Cloud Essentials, the RAM percentage for Flex plans is fixed at 10% and can't be changed. On Redis Cloud Pro, you can select a RAM percentage between 10% and 50% when you create your database. See [Choosing the right RAM ratio](https://support.redislabs.com/hc/en-us/articles/36437338181522-Redis-Flex-V2-Choosing-the-Right-RAM-Ratio-and-Troubleshooting-Performance) for guidance on selecting a RAM percentage.

### Key and value sizes

Similar to best practices for in-memory Redis, we recommend storing relatively small keys and values in Flex. If possible, avoid large objects (>10 KB).

Depending on your application's traffic pattern, using large objects might decrease performance, since the entire value is moved from RAM to Flash storage and vice versa.

Flex databases cannot store keys or values larger than 4 GB in Flash storage. Keys or values larger than 4 GB are stored in RAM only, and will generate warnings like the following in the Redis logs:

```
# WARNING: key too big for disk driver, size: 4703717276, key: subactinfo:htable
```

## Create a Flex database 

### Redis Cloud Essentials

Before creating a Redis Cloud database, you need to [create an account](https://redis.io/docs/latest/operate/rc/rc-quickstart).

To create a database in your Redis Cloud account:

1. Sign in to the [Redis Cloud console](https://cloud.redis.io).

2. Select the **New database** button.

    ![The New Database button creates a new database.](https://redis.io/docs/latest/images/rc/button-database-new.png)

    This displays the **Create database** screen. 

3. Select the type of [subscription](https://redis.io/docs/latest/operate/rc/subscriptions) you need. For this guide, select **Essentials**.

    ![The Subscription selection panel with Essentials selected.](https://redis.io/docs/latest/images/rc/create-database-subscription-essentials.png)

    After you select **Essentials**, the rest of the database details will appear. Select **Flex (RAM + SSD)** to use Flex.

    ![The database name, cloud vendor, version, region, type, and durability settings.](https://redis.io/docs/latest/images/rc/create-database-essentials-cloud-vendor.png)

1. Redis will generate a database name for you. If you want to change it, you can do so in the **Database name** field.  

1. Choose a **Region** on Amazon Web Services for your database. See [Supported regions](https://redis.io/docs/latest/operate/rc/supported-regions) for a list of supported regions by cloud vendor.

1. Select the **Database version** you want to use.

1. Select your desired memory limit. 

    ![Available Flex plans.](https://redis.io/docs/latest/images/rc/subscription-new-flex-tiers.png)

    For a comparison of available plans, see [Redis Cloud Essentials plans](https://redis.io/docs/latest/operate/rc/subscriptions/view-essentials-subscription/essentials-plan-details).

    All Flex plans on Redis Cloud Essentials have a default RAM percentage of 10%. 

1. Choose your **High availability (replication)** settings from the list. 

    Redis Cloud supports the following high availability settings with Flex:

    - **None**: You will have a single copy of your database without replication.
    - **Single-Zone**: Your database will have a primary and a replica located in the same cloud zone. If anything happens to the primary, the replica takes over and becomes the new primary.

    See [High availability](https://redis.io/docs/latest/operate/rc/databases/configuration/high-availability) for more information about these settings.

1. Choose your **Data persistence** settings from the list.

    Redis Cloud supports the following data persistence options:

    - An **Append-Only File** maintains a record (sometimes called a _redo log_ or _journal_) of write operations.  This allows the data to be restored by using the record to reconstruct the database up to the point of failure. For Essentials databases, Redis updates the Append-Only file every second.

    - A **Snapshot** is a copy of the in-memory database, taken at periodic intervals (one, six, or twelve hours). You can restore data to the snapshot's point in time. 
    
    See [Data persistence](https://redis.io/docs/latest/operate/rc/databases/configuration/data-persistence) for more information about these settings.

1. Select the **Database version** you want to use.

1.  Enter your payment details.

    If you haven't previously entered a payment method, use the **Add Credit Card** button to add one.

    ![The Add credit card icon.](https://redis.io/docs/latest/images/rc/icon-add.png)

    If you have not already added a business address to your account, you must enter one. Redis uses your business address for communication, invoicing, and tax purposes.

![The Add credit card screen before a business address has already been added.](https://redis.io/docs/latest/images/rc/billing-add-first-card.png)

If you already have a business address, you don't need to enter one here. See [Account settings](https://redis.io/docs/latest/operate/rc/accounts/account-settings) to learn how to update your business address.

![The Add credit card screen after a business address has already been added.](https://redis.io/docs/latest/images/rc/billing-add-credit-card.png)

If the card's billing address is the same as your account's business address, select **Same as business address** to fill the billing address with your business address details.

1. Select **Confirm & pay** to create your database.

![Select Confirm & Pay to create your new database.](https://redis.io/docs/latest/images/rc/button-create-db-confirm-pay.png)

When you create your database, there's a brief pause while your request is processed and then the **Database details** page appears.

### Redis Cloud Pro

To create a Flex database on Redis Cloud Pro, [create a new Pro database with custom settings](https://redis.io/docs/latest/operate/rc/databases/create-database/create-pro-database-new#custom-settings). 

In the **Advanced options** of the **Setup** tab, select **Redis Flex**.

![The Flex setting selected.](https://redis.io/docs/latest/images/rc/pro-flex-on.png)

During the **Sizing** step, when you are provisioning your databases, you can select the RAM percentage for your database. The default is 20%, but you can select a percentage between 10% and 50%. Lower RAM percentages reduce cost but may increase latency, while higher RAM percentages improve throughput and latency at higher cost. See [Choosing the right RAM ratio](https://support.redislabs.com/hc/en-us/articles/36437338181522-Redis-Flex-V2-Choosing-the-Right-RAM-Ratio-and-Troubleshooting-Performance) to choose the right RAM percentage for your database.

![The RAM percentage setting.](https://redis.io/docs/latest/images/rc/pro-flex-ram-percentage.png)

Continue with the instructions to [create your database](https://redis.io/docs/latest/operate/rc/databases/create-database/create-pro-database-new#custom-settings).

## Troubleshooting

See [Troubleshooting Redis Flex performance questions](https://support.redislabs.com/hc/en-us/articles/36437338181522-Redis-Flex-V2-Choosing-the-Right-RAM-Ratio-and-Troubleshooting-Performance#h_01KV6F382KNM8N0W00DFEHPY3S) on the Redis Support knowledge base to learn how to troubleshoot Redis Flex databases.
