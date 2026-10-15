# Create an Active-Active database

```json metadata
{
  "schema_version": 2,
  "title": "Create an Active-Active database",
  "description": "Shows how to create an Active-Active database",
  "categories": ["docs","operate","rc"],
  "tableOfContents": {"sections":[{"children":[{"id":"set-up-deployment-details","title":"Set up deployment details"},{"id":"sizing-tab","title":"Sizing tab"},{"id":"review-and-create-tab","title":"Review and Create tab"}],"id":"create-an-active-active-database","title":"Create an Active-Active database"},{"id":"more-info","title":"More info"}]}

,
  "codeExamples": []
}
```


Active-Active databases store data across multiple regions and availability zones.  This improves scalability, performance, and availability, especially when compared to standalone databases. See [Active-Active Redis](https://redis.io/docs/latest/operate/rc/databases/active-active) for more information.

To deploy Active-Active databases in Redis Cloud, you need a Redis Cloud Pro plan that enables Active-Active Redis and defines the regions for each copy of your databases.

Active-Active databases consist of multiple copies (also called _instances_) deployed to different regions throughout the world.

This reduces latency for local users and improves availability should a region fail.

Redis Cloud maintains consistency among instances in the background; that is, each copy eventually includes updates from every region.  As a result, memory limit and throughput increase.

## Create an Active-Active database

Before creating a Redis Cloud database, you need to [create an account](https://redis.io/docs/latest/operate/rc/rc-quickstart).

To create a database in your Redis Cloud account:

1. Sign in to the [Redis Cloud console](https://cloud.redis.io).

2. Select the **New database** button.

    ![The New Database button creates a new database.](https://redis.io/docs/latest/images/rc/button-database-new.png)

    This displays the **Create database** screen.

3. Select the type of [subscription](https://redis.io/docs/latest/operate/rc/subscriptions) you need. For this guide, select **Pro**. 

    ![The Subscription selection panel with Pro selected.](https://redis.io/docs/latest/images/rc/create-database-subscription-pro-new.png)

    > [!NOTE]
    > This guide shows how to create an Active-Active database with a new Pro subscription. If you already have an Active-Active subscription and want to add a database to it, see [Create a Pro database in an existing subscription](https://redis.io/docs/latest/operate/rc/databases/create-database/create-pro-database-existing). Active-Active subscriptions can host a maximum of 10 databases.
    >
    

After you select **Pro**, the **Database settings** section will appear.

![The database settings section, with custom settings selected.](https://redis.io/docs/latest/images/rc/create-pro-db-settings-custom.png)

For this guide, select **Custom settings**. For an Active-Active database, you will need to: 

1. Set up the deployment options, including cloud vendor and region details for each instance.

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

Select **Active-Active (Multi-region)** to turn on Active-Active. 

![The general settings of the setup tab with Active-Active selected.](https://redis.io/docs/latest/images/rc/create-flexible-sub-active-active-on.png)

When you enable Active-Active Redis, two regions are selected by default. Select the drop-down arrow to display a list of provider regions that support Active-Active databases.

![Use the Region drop-down to select the regions for your Active-Active database.](https://redis.io/docs/latest/images/rc/create-sub-active-active-regions.png)

> [!NOTE]
> Active-Active subscriptions on Redis Cloud are limited to a maximum of 10 regions.

Use the checkboxes in the list to select or remove regions.  The Search box lets you locate specific regions.

You can use a region's Remove button to remove it from the list.

![Select the Delete button to remove a region from the list.](https://redis.io/docs/latest/images/rc/icon-region-delete.png)

#### Advanced options {#advanced-options}

![Each region needs a unique CIDR address block to communicate securely with other instances.](https://redis.io/docs/latest/images/rc/create-sub-active-active-cidr.png)

In the **Advanced options** section, you can:

- Choose to deploy your Active-Active database to an existing Cloud Account, if [Redis Cloud Bring your own Cloud](https://redis.io/docs/latest/operate/rc/subscriptions/bring-your-own-cloud) is enabled.
    
- Define CIDR addresses for each region in the **VPC configuration** section.

    Every CIDR should be unique to properly route network traffic between each Active-Active database instance and your consumer VPCs. The CIDR block regions should _not_ overlap between the Redis server and your app consumer VPCs. In addition, CIDR blocks should not overlap between cluster instances. 

When all **Deployment CIDR** regions display a green checkmark, you're ready to continue.  

![Green checkmarks indicate valid CIDR address values.](https://redis.io/docs/latest/images/rc/icon-cidr-address-ok.png)

Red exclamation marks indicate error conditions; the tooltip provides additional details.

![Red exclamation points indicate CIDR address problems.](https://redis.io/docs/latest/images/rc/icon-cidr-address-error.png)
    
    If you chose to deploy your Active-Active database to an existing [Bring your own Cloud](https://redis.io/docs/latest/operate/rc/subscriptions/bring-your-own-cloud) account, you can also define the VPC ID for each region. Select **In existing VPC** and the set the VPC ID for each selected region.
    
- Set your [maintenance](https://redis.io/docs/latest/operate/rc/subscriptions/maintenance) settings in the **Maintenance windows** section. Select **Manual** if you want to set [manual maintenance windows](https://redis.io/docs/latest/operate/rc/subscriptions/maintenance/set-maintenance-windows).

> [!NOTE]
> Multi-AZ replication is required for all Active-Active databases.
>
> Regions with fewer than three availability zones are not available in the Redis Cloud console. To create an Active-Active database that includes one of these regions, use the REST API to [create a Pro subscription](https://redis.io/docs/latest/operate/rc/api/examples/manage-subscriptions#create-a-pro-subscription). You'll be able to manage these subscriptions and databases using the Redis Cloud console after they're created. Active-Active databases in these regions use single-zone replication and provide 99.99% (four-nines) availability instead of 99.999%. For more information, see [Active-Active Redis](https://redis.io/docs/latest/operate/rc/databases/active-active#multi-zone).

When finished, choose **Continue** to determine your size requirements.

![Select the Continue button to continue to the next step.](https://redis.io/docs/latest/images/rc/button-subscription-continue.png)

### Sizing tab

The **Sizing** tab helps you specify the database, memory, and throughput requirements for your subscription.

![The Sizing tab when creating a new Pro subscription.](https://redis.io/docs/latest/images/rc/subscription-new-flexible-sizing-tab.png)

When you first visit the **Sizing** tab, there are no databases defined.  Select the **Add** button to create one.

![Use the Add button to define a new database for your subscription.](https://redis.io/docs/latest/images/rc/icon-add.png)

This opens the **Database configurations** dialog, which lets you define the requirements for your new database.

![New database dialog for Active-Active database.](https://redis.io/docs/latest/images/rc/create-database-active-active.png)

By default, you're shown basic settings, which include:

- **Name**: A custom name for your database.
- **Version**: The Redis version for your database. We recommend you choose the latest available version. 
- **Advanced Capabilities**: Advanced data types or features used by the database. Active-Active databases support the [JSON](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/json) data type and [Search and query](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/search) features.

    ![When you create an Active-Active database, you can select the JSON and Search and query advanced capabilities.](https://redis.io/docs/latest/images/rc/active-active-json-detail.png)

    For Redis versions prior to 8.0, we select both capabilities for you automatically. You can remove a capability by clicking on it while selected. Selected capabilities will be available in all regions, including those added in the future.

    Starting with Redis 8.0, JSON and Search and query are included by default.

    See [Search and query Active-Active databases](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/search/search-active-active) to learn how to use Search and query on Active-Active databases.

- **Dataset size**: The amount of data needed for your dataset in GB. 

    For Search and query databases, use the [Sizing calculator](https://redis.io/redisearch-sizing-calculator/) to estimate your index size and throughput requirements. When you're entering the dataset size for your database, add the estimated index size from the Sizing calculator to your expected dataset size.

- **Hashing policy**: Determines how data is distributed across multiple Redis processes of a database. Available options depend on your account creation date. See [Clustering](https://redis.io/docs/latest/operate/rc/databases/configuration/clustering#manage-the-hashing-policy) for more information.

- **Throughput**: When you create an Active-Active database, you define the throughput for each instance. The total operations per second combines the total read ops/sec and applies the write ops/sec for each region across every region. 

    ![When you create an Active-Active database, you define throughput for each region.](https://redis.io/docs/latest/images/rc/active-active-throughput-detail.png)

    The total ops/sec for each region is calculated as follows:

    ```sh
    Region ops/sec = Local read ops/sec + 
                    Sum of write ops/sec from all regions
    ```

    The total ops/sec for the database is the sum of the ops/sec for each region.
    
    Because each instance needs the ability to write to every other instance, write operations significantly affect the total number of ops/sec. 

    Select a tab to see examples of throughput calculations for different Active-Active configurations.

    **Two regions, balanced between regions:**

For this database, we have two regions where read and write operations are balanced between the regions, as described in the table below:

| Region | Local read ops/sec | Local write ops/sec | 
|:------:|:------------------:|:-------------------:|
| Region 1 | 2000 | 1000 |
| Region 2 | 2000 | 1000 |

The total ops/sec for this database is calculated as follows:

```text
Region 1 ops/sec = 2000 (local read) + 
                   1000 (local write) + 
                   1000 (write from Region 2) = 4000 ops/sec

Region 2 ops/sec = 2000 (local read) + 
                   1000 (local write) + 
                   1000 (write from Region 1) = 4000 ops/sec

Total ops/sec = 4000 (Region 1) + 4000 (Region 2) 
              = 8000 ops/sec
```

**Two regions, read/write heavy in one region:**

For this database, we have two regions where one region has more read and write operations than the other region, as described in the table below:

| Region | Local read ops/sec | Local write ops/sec | 
|:------:|:------------------:|:-------------------:|
| Region 1 | 2000 | 1000 |
| Region 2 | 4000 | 2000 |

The total ops/sec for this database is calculated as follows:

```text
Region 1 ops/sec = 2000 (local read) + 
                   1000 (local write) + 
                   2000 (write from Region 2) = 5000 ops/sec

Region 2 ops/sec = 4000 (local read) + 
                   2000 (local write) + 
                   1000 (write from Region 1) = 7000 ops/sec

Total ops/sec = 5000 (Region 1) + 7000 (Region 2) 
              = 12000 ops/sec
```

**Three regions, balanced between regions:**

For this database, we have three regions where read and write operations are balanced between the regions, as described in the table below:

| Region | Local read ops/sec | Local write ops/sec | 
|:------:|:------------------:|:-------------------:|
| Region 1 | 2000 | 1000 |
| Region 2 | 2000 | 1000 |
| Region 3 | 2000 | 1000 |

The total ops/sec for this database is calculated as follows:

```text
Region 1 ops/sec = 2000 (local read) + 
                   1000 (local write) + 
                   1000 (write from Region 2) +
                   1000 (write from Region 3) = 5000 ops/sec

Region 2 ops/sec = 2000 (local read) + 
                   1000 (local write) + 
                   1000 (write from Region 1) +
                   1000 (write from Region 3) = 5000 ops/sec

Region 3 ops/sec = 2000 (local read) + 
                   1000 (local write) + 
                   1000 (write from Region 1) +
                   1000 (write from Region 2) = 5000 ops/sec

Total ops/sec = 5000 (Region 1) + 5000 (Region 2) + 5000 (Region 3) 
              = 15000 ops/sec
```

**Three regions, different read/write in each region:**

For this database, we have three regions where read and write operations are different between the regions, as described in the table below:

| Region | Local read ops/sec | Local write ops/sec | 
|:------:|:------------------:|:-------------------:|
| Region 1 | 3000 | 1000 |
| Region 2 | 4000 | 3000 |
| Region 3 | 1000 | 2000 |

The total ops/sec for this database is calculated as follows:

```text
Region 1 ops/sec = 3000 (local read) + 
                   1000 (local write) + 
                   3000 (write from Region 2) +
                   2000 (write from Region 3) = 9000 ops/sec

Region 2 ops/sec = 4000 (local read) + 
                   3000 (local write) + 
                   1000 (write from Region 1) +
                   2000 (write from Region 3) = 10000 ops/sec

Region 3 ops/sec = 1000 (local read) + 
                   2000 (local write) + 
                   1000 (write from Region 1) +
                   3000 (write from Region 2) = 7000 ops/sec

Total ops/sec = 9000 (Region 1) + 10000 (Region 2) + 7000 (Region 3) 
              = 26000 ops/sec
```



    For Search and query databases, the estimated throughput from the [Sizing calculator](https://redis.io/redisearch-sizing-calculator/) is the total amount of throughput you need. When setting throughput for your Active-Active database, use the total amount for each region and divide it depending on your read (query) and write (update) needs for each region. For example, if the total amount of throughput needed is 50000 ops/sec, you could set each region to have 20000 ops/sec for reads (queries) and 30000 ops/sec for writes (updates).

- **Data Persistence**: Defines the data persistence policy, if any. See [Database persistence](https://redis.io/docs/latest/operate/rs/databases/configure/database-persistence).
- **Supported Protocol(s)**: Choose between RESP2 and RESP3 _(Redis 7.2 or later)_. See [Redis serialization protocol](https://redis.io/docs/latest/develop/reference/protocol-spec#resp-versions) for details.
- **Quantity**: Number of databases to create with these settings. 

When finished, select **Save configuration** to save your database configuration.

![Select the Save configuration button to define your new database.](https://redis.io/docs/latest/images/rc/button-configuration-save.png)

Use the **Add database** button to define additional databases or select the **Continue button** to display the **Review and create** tab.

Hover over a database to see the **Edit** and **Delete** icons. You can use the **Edit** icon to change a database or the **Delete** icon to remove a database from the list.

![Use the Edit button to change database settings.](https://redis.io/docs/latest/images/rc/icon-edit.png#no-click)&nbsp;![Use the Delete button to remove a database.](https://redis.io/docs/latest/images/rc/icon-delete-lb.png#no-click)


### Review and Create tab

The **Review and Create** tab provides a cost estimate for your Redis Cloud Pro plan:

![The Review & Create tab of the New Active-Active subscription screen.](https://redis.io/docs/latest/images/rc/create-pro-aa-review.png)

Redis breaks down your databases to Redis Billing Units (RBUs), each with their own size and throughput requirements. For more info, see [Billing unit types](https://redis.io/docs/latest/operate/rc/databases/create-database/create-pro-database-new#billing-unit-types).

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

## More info

- [Create a Pro database with a new subscription](https://redis.io/docs/latest/operate/rc/databases/create-database/create-pro-database-new)
- [Active-Active Redis](https://redis.io/docs/latest/operate/rc/databases/active-active)
- [Develop applications with Active-Active databases](https://redis.io/docs/latest/operate/rc/databases/active-active/develop)
- Database [memory limit](https://redis.io/docs/latest/operate/rc/databases/configuration/sizing#dataset-size)
- Redis Cloud [subscription plans](https://redis.io/docs/latest/operate/rc/subscriptions)
- [Redis Cloud pricing](https://redis.io/pricing/#monthly)


