# Create a Pro database with a new subscription

```json metadata
{
  "schema_version": 2,
  "title": "Create a Pro database with a new subscription",
  "description": "Shows how to create a Pro database with a new subscription",
  "categories": ["docs","operate","rc"],
  "tableOfContents": {"sections":[{"id":"easy-create","title":"Create database with Easy create"},{"children":[{"id":"set-up-deployment-details","title":"Set up deployment details"},{"id":"sizing-tab","title":"Sizing tab"},{"id":"review-and-create-tab","title":"Review and Create tab"}],"id":"custom-settings","title":"Create database with Custom settings"},{"id":"billing-unit-types","title":"Billing unit types"}]}

,
  "codeExamples": []
}
```


Redis Cloud Pro supports more databases, larger databases, greater throughput, and unlimited connections compared to Redis Cloud Essentials. Redis Cloud Pro databases are perfect for teams building mission-critical systems in the cloud.

Before creating a Redis Cloud database, you need to [create an account](https://redis.io/docs/latest/operate/rc/rc-quickstart).

To create a database in your Redis Cloud account:

1. Sign in to the [Redis Cloud console](https://cloud.redis.io).

2. Select the **New database** button.

    ![The New Database button creates a new database.](https://redis.io/docs/latest/images/rc/button-database-new.png)

    This displays the **Create database** screen.

3. Select the type of [subscription](https://redis.io/docs/latest/operate/rc/subscriptions) you need. For this guide, select **Pro**. 

    ![The Subscription selection panel with Pro selected.](https://redis.io/docs/latest/images/rc/create-database-subscription-pro-new.png)

    > [!NOTE]
    > This guide shows how to create a Pro database with a new subscription.
    > - If you already have a Pro subscription and want to add a database to it, see [Create a Pro database in an existing subscription](https://redis.io/docs/latest/operate/rc/databases/create-database/create-pro-database-existing).
    > - If you'd rather create an Essentials database, see [Create an Essentials database](https://redis.io/docs/latest/operate/rc/databases/create-database/create-essentials-database).
    >
    

After you select **Pro**, the **Database settings** section will appear.

![The database settings section.](https://redis.io/docs/latest/images/rc/create-pro-db-settings.png)

You can choose to create your database in one of two ways:

- [**Easy create**](#easy-create) selects the optimal settings for you to get started faster.
- [**Custom settings**](#custom-settings) lets you select all of the configuration options for your new database.

## Create database with Easy create {#easy-create}

If you choose to create your database with Easy create:

![The database name, cloud vendor and region settings.](https://redis.io/docs/latest/images/rc/pro-easy-create-vendor.png)

1. Choose a **Cloud Provider** and a **Region**.

1. Enter the following settings for your database:

    ![The Dataset size, throughput, and High availability settings.](https://redis.io/docs/latest/images/rc/pro-easy-create-size-throughput.png)

    | Database&nbsp;setting | Description |
    |:---------|:-----------|
    | **Name** | The name for your database. Redis will generate a database name for you, but you can change it at any time.  |
    | **Dataset size (GB)** | The amount of data for your dataset. See [Dataset size](https://redis.io/docs/latest/operate/rc/databases/configuration/sizing#dataset-size) for sizing considerations. <br/> Databases with Search and query have specific sizing requirements, see [Search and query sizing](https://redis.io/docs/latest/operate/rc/databases/configuration/advanced-capabilities#search-and-query-sizing) for more information. |
    | **Throughput** | Identifies maximum throughput for the database, which is specified in terms of operations per second (**Ops/sec**). See [Throughput](https://redis.io/docs/latest/operate/rc/databases/configuration/sizing#throughput) for more information. <br/> Databases with Search and query have specific throughput requirements, see [Search and query sizing](https://redis.io/docs/latest/operate/rc/databases/configuration/advanced-capabilities#search-and-query-sizing) for more information. |
    | **High Availability** | Indicates whether a replica copy of the database is maintained in case the primary database becomes unavailable.  (Warning: doubles memory consumption). See [High Availability](https://redis.io/docs/latest/operate/rc/databases/configuration/high-availability).  |

1. Select **View all settings** to review the database settings that we selected for you.

    ![The optimal database settings.](https://redis.io/docs/latest/images/rc/pro-easy-create-optimal-settings.png)

    If you want to change these settings, select [**Switch to custom settings**](#custom-settings).

1. Enter your payment details.

    If you haven't previously entered a payment method, use the **Add Credit Card** button to add one.

    ![The Add credit card icon.](https://redis.io/docs/latest/images/rc/icon-add.png)

    If you have not already added a business address to your account, you must enter one. Redis uses your business address for communication, invoicing, and tax purposes.

![The Add credit card screen before a business address has already been added.](https://redis.io/docs/latest/images/rc/billing-add-first-card.png)

If you already have a business address, you don't need to enter one here. See [Account settings](https://redis.io/docs/latest/operate/rc/accounts/account-settings) to learn how to update your business address.

![The Add credit card screen after a business address has already been added.](https://redis.io/docs/latest/images/rc/billing-add-credit-card.png)

If the card's billing address is the same as your account's business address, select **Same as business address** to fill the billing address with your business address details.

 Select **Confirm & pay** to create your database.

![Select Confirm & Pay to create your new database.](https://redis.io/docs/latest/images/rc/button-create-db-confirm-pay.png)

Note that databases are created in the background.  While they are provisioning, you aren't allowed to make changes. This process generally takes 10-15 minutes.

Use the **Database list** to check the status of your databases.

## Create database with Custom settings {#custom-settings}

![The database settings section, with custom settings selected.](https://redis.io/docs/latest/images/rc/create-pro-db-settings-custom.png)

If you choose to create your database with custom settings, you need to:

1. Set up the deployment options, including cloud vendor details, high availability settings, and advanced options.

2. Define the database size requirements.

3. Review your choices, provide payment details, and then create your databases.

The following sections provide more information.

### Set up deployment details

The **Setup** tab specifies general settings for your Redis deployment.

![The Setup tab of the new Pro Database process.](https://redis.io/docs/latest/images/rc/subscription-new-flexible-tabs-setup.png)

There are two sections on this tab:

- [General settings](#general-settings) include the cloud provider details and specific configuration options.
- [Advanced options](#advanced-options) define settings for high availability and security. Configurable settings vary according to cloud provider.

#### General settings {#general-settings}

![The General settings of the Setup tab.](https://redis.io/docs/latest/images/rc/subscription-new-flexible-setup-general.png)

In the General settings of the **Setup** tab, you need to:

1. Select the public **Cloud vendor** to deploy your databases.

1. Select the **Region** where you want to deploy your database. 

    > [!NOTE]
    > This guide is for single region database deployment. If you want to create a multi-region Active-Active database, see [Create an Active-Active database](https://redis.io/docs/latest/operate/rc/databases/active-active/create-active-active-database) for specific steps and configuration options exclusive to Active-Active.
    >

#### Advanced options {#advanced-options}

![The Advanced settings of the Setup tab.](https://redis.io/docs/latest/images/rc/subscription-new-flexible-setup-advanced.png)

The following settings are defined in the **Advanced options** of the **Setup** tab:

| Advanced option | Description |
|---|---|
| **Redis Flex** | Determines if your databases are stored only in memory (RAM) or are split between memory and Flash storage (RAM+Flash).  See [Redis Flex](https://redis.io/docs/latest/operate/rc/databases/create-database/create-flex-database) for more information. |
| **BYOC account** | To deploy these databases to an existing cloud account, select it here.  Use the **Add** button to add a new cloud account.<br/><br/>(Available only if [Redis Cloud Bring your own Cloud](https://redis.io/docs/latest/operate/rc/subscriptions/bring-your-own-cloud) is enabled) |
| **AWS Resource tags** | Applies resource tags to the infrastructure deployed to your BYOC account. See [Resource tags](https://redis.io/docs/latest/operate/rc/subscriptions/bring-your-own-cloud/resource-tags) for more information.<br/><br/>(Available only if [Redis Cloud Bring your own Cloud](https://redis.io/docs/latest/operate/rc/subscriptions/bring-your-own-cloud) is enabled) |
| **Multi-AZ** | Determines if replication spans multiple Availability Zones, which provides automatic failover when problems occur. See [High Availability](https://redis.io/docs/latest/operate/rc/databases/configuration/high-availability). |
| **VPC configuration** | Select **In a new VPC** to deploy to a new [virtual private cloud](https://en.wikipedia.org/wiki/Virtual_private_cloud) (VPC).<br/><br/>To deploy these databases to an existing virtual private cloud, select **In existing VPC** and then set VPC ID to the appropriate ID value.<br/><br/>(Available only if [Redis Cloud Bring your own Cloud](https://redis.io/docs/latest/operate/rc/subscriptions/bring-your-own-cloud) is enabled and you have selected an existing BYOC account) |
| **Allowed Availability Zones** | The availability zones for your selected region.<br/><br/>If you choose **Manual selection**, you must select at least one zone ID from the **Zone IDs** list.  For more information, see [Availability zones](https://redis.io/docs/latest/operate/rc/databases/configuration/high-availability#availability-zones). |
| **Deployment CIDR** | The [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) range of IP addresses for your deployment. Redis creates a new [subnet](https://en.wikipedia.org/wiki/Subnetwork) for the **Deployment CIDR** in your [virtual private cloud](https://en.wikipedia.org/wiki/Virtual_private_cloud) (VPC). It cannot overlap with the CIDR ranges of other subnets used by your account.<br/><br/>For deployments in an existing VPC, the **Deployment CIDR** must be within your VPC's **primary** CIDR range (secondary CIDRs are not supported). |
| **Public endpoint access** | Select whether or not to [block public endpoints](https://redis.io/docs/latest/operate/rc/security/database-security/block-public-endpoints) for all databases in the subscription.  |
| **Persistent storage encryption** | Select whether to encrypt persistent storage with a Cloud-provider managed key or a [self-managed encryption key](https://redis.io/docs/latest/operate/rc/security/manage-encryption-keys). If you select **Customer managed key**, you'll get clear instructions to provide access to your self-managed key after you set up your database(s). See [Grant key permissions](https://redis.io/docs/latest/operate/rc/security/manage-encryption-keys#grant-key-permissions) for more information. |
| **Maintenance windows** | Determines when Redis can perform [maintenance](https://redis.io/docs/latest/operate/rc/subscriptions/maintenance) on your databases. Select **Manual** if you want to set [manual maintenance windows](https://redis.io/docs/latest/operate/rc/subscriptions/maintenance/set-maintenance-windows). |

When finished, choose **Continue** to determine your size requirements.

![Select the Continue button to continue to the next step.](https://redis.io/docs/latest/images/rc/button-subscription-continue.png)

### Sizing tab

The **Sizing** tab helps you specify the database, memory, and throughput requirements for your subscription.

![The Sizing tab when creating a new Pro subscription.](https://redis.io/docs/latest/images/rc/subscription-new-flexible-sizing-tab.png)

When you first visit the **Sizing** tab, there are no databases defined.  Select the **Add** button to create one.

![Use the Add button to define a new database for your subscription.](https://redis.io/docs/latest/images/rc/icon-add.png)

This opens the **Database configurations** dialog, which lets you define the requirements for your new database.

![The Database configurations dialog with basic settings.](https://redis.io/docs/latest/images/rc/flexible-add-database-basic.png)

By default, you're shown basic settings, which include:

| Database&nbsp;setting | Description |
|:---------|:-----------|
| **Name** | Redis Cloud generates a database name for you, but you can change it at any time. |
| **Version** | The Redis version for your database. We recommend you choose the latest available version. See [Redis version management](https://redis.io/docs/latest/operate/rc/databases/version-management) for more information. |
| **Dataset size (GB)** | The amount of data for your dataset. Specify small sizes as decimals of 1.0&nbsp;GB; example: `0.1` GB (minimum). We calculate the total memory limit for you based on the other settings you choose for your database. <br/> Databases with Search and query have specific sizing requirements, see [Search and query sizing](https://redis.io/docs/latest/operate/rc/databases/configuration/advanced-capabilities#search-and-query-sizing) for more information. |
| **High Availability** | Indicates whether a replica copy of the database is maintained in case the primary database becomes unavailable.  (Warning: Doubles memory consumption). See [High Availability](https://redis.io/docs/latest/operate/rc/databases/configuration/high-availability).  |
| **Throughput** | Identifies maximum throughput for the database, which is specified in terms of operations per second (**Ops/sec**). See [Throughput](https://redis.io/docs/latest/operate/rc/databases/configuration/sizing#throughput) for more information. <br/> Databases with Search and query have specific throughput requirements. See [Search and query sizing](https://redis.io/docs/latest/operate/rc/databases/configuration/advanced-capabilities#search-and-query-sizing) for more information. |
| **Hashing policy** | Determines how data is distributed across multiple Redis processes of a database. Available options depend on your account creation date. See [Clustering](https://redis.io/docs/latest/operate/rc/databases/configuration/clustering#manage-the-hashing-policy) for more information.  |
| **Query performance factor** | *(Search and query databases on Redis 7.2 or later only)* Adds additional compute power to process your query and vector search workloads and boost your queries per second. See [Search and query sizing](https://redis.io/docs/latest/operate/rc/databases/configuration/advanced-capabilities#search-and-query-sizing) for more information. |
| **Data Persistence** | Defines the data persistence policy, if any. See [Data persistence](https://redis.io/docs/latest/operate/rc/databases/configuration/data-persistence). |

Select **More options** to specify values for the following settings.

![The Database configurations dialog with advanced settings.](https://redis.io/docs/latest/images/rc/flexible-add-database-advanced.png)

| Database&nbsp;option | Description                                                                                                                                                     |
|:---------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Advanced Capabilities** | [Advanced features and data types](https://redis.io/docs/latest/operate/rc/databases/configuration/advanced-capabilities) used by the database. Starting with Redis 8.0, all advanced capabilities are included in Redis by default. |
| **OSS Cluster API** | Enable to use the [OSS Cluster API](https://redis.io/docs/latest/operate/rc/databases/configuration/clustering#oss-cluster-api).                                                                                                                |
| **Type** | Set to **Redis**, otherwise **Memcached** database for legacy database support.                                                                                     |
| **Supported Protocol(s)** | Choose between RESP2 and RESP3 _(Redis 7.2 and later only)_. See [Redis serialization protocol](https://redis.io/docs/latest/develop/reference/protocol-spec#resp-versions) for details |
| **Quantity** | Number of databases to create with these settings.                                                                                                              |

When finished, select **Save configuration** to save your database configuration.

![Select the Save configuration button to define your new database.](https://redis.io/docs/latest/images/rc/button-configuration-save.png)

Use the **Add database** button to define additional databases or select the **Continue button** to display the **Review and create** tab.

Hover over a database to see the **Edit** and **Delete** icons. You can use the **Edit** icon to change a database or the **Delete** icon to remove a database from the list.

![Use the Edit button to change database settings.](https://redis.io/docs/latest/images/rc/icon-edit.png#no-click)&nbsp;![Use the Delete button to remove a database.](https://redis.io/docs/latest/images/rc/icon-delete-lb.png#no-click)


### Review and Create tab

The **Review & Create** tab provides a cost estimate for your Redis Cloud Pro plan:

![The Review & Create tab of the New Flexible subscription screen.](https://redis.io/docs/latest/images/rc/subscription-new-flexible-review.png)

Redis breaks down your databases to Redis Billing Units (RBUs), each with their own size and throughput requirements. For more info, see [Billing unit types](#billing-unit-types).

The **Payment methods** section of this tab shows which payment method you're using for this database. Select the arrow on the top right of this section to view all available payment methods.

![The payment method list.](https://redis.io/docs/latest/images/rc/subscription-new-flexible-cardlist.png)

If you have not added a payment method or want to add a new payment method, select **Add credit card** to add a new credit card.

If you have not already added a business address to your account, you must enter one. Redis uses your business address for communication, invoicing, and tax purposes.

![The Add credit card screen before a business address has already been added.](https://redis.io/docs/latest/images/rc/billing-add-first-card.png)

If you already have a business address, you don't need to enter one here. See [Account settings](https://redis.io/docs/latest/operate/rc/accounts/account-settings) to learn how to update your business address.

![The Add credit card screen after a business address has already been added.](https://redis.io/docs/latest/images/rc/billing-add-credit-card.png)

If the card's billing address is the same as your account's business address, select **Same as business address** to fill the billing address with your business address details.

Select **Back to Sizing** to make changes or **Confirm & Pay** to create your databases.

![Select Confirm & pay to create your database.](https://redis.io/docs/latest/images/rc/button-create-db-confirm-pay.png)

Note that databases are created in the background.  While they are provisioning, you aren't allowed to make changes. This process generally takes 10-15 minutes.

Use the **Database list** to check the status of your databases.


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



