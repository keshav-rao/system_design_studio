# View and edit databases

```json metadata
{
  "schema_version": 2,
  "title": "View and edit databases",
  "description": "",
  "categories": ["docs","operate","rc"],
  "tableOfContents": {"sections":[{"children":[{"id":"performance--availability","title":"Performance \u0026 availability"},{"id":"access","title":"Access"},{"id":"data","title":"Data"},{"id":"security","title":"Security"},{"id":"database-info","title":"Database info"},{"id":"general-settings","title":"General settings"},{"id":"performance-section","title":"Performance section"},{"id":"durability-section","title":"Durability section"},{"id":"security-section","title":"Security section"},{"id":"alerts-section","title":"Alerts section"},{"id":"danger-zone","title":"Danger zone"}],"id":"configuration-tab","title":"Configuration tab"},{"id":"other-actions-and-info","title":"Other actions and info"},{"id":"edit-database-details","title":"Edit database details"},{"id":"manage-the-database-list","title":"Manage the database list"}]}

,
  "codeExamples": []
}
```


Use the **Databases** menu of the Redis Cloud console to manage your databases.

To view the details of a database:

1. Sign in to the [Redis Cloud console](https://cloud.redis.io/).  (Create an account if you don't already have one.)

2. Select the **Databases** menu to display a [searchable list of all databases](#manage-the-database-list).
 
3. Locate the database in the list.

4. Select the database name to open the **Database** page.

The **Database** screen lets you review:
- Configuration details of a database
- Graphs showing performance metrics
- Recent activity via a "[slowlog](https://redis.io/docs/latest/commands/slowlog)," which lists queries that exceed a certain execution time.

For help changing database settings, see [Edit database details](#edit-database-details).

## Configuration tab

The **Configuration** screen is divided into sections, each dedicated to a specific category.  Note that not every section or setting is available to every [subscription plan](https://redis.io/docs/latest/operate/rc/subscriptions).

The Configuration tab is organized differently for Essentials and Pro databases. Select your plan type below.

**Essentials:**

### Performance & availability

The **Performance & availability** section defines the plan and backup settings of your database.

<img src="../../../../images/rc/database-details-configuration-tab-performance-availability-essentials.png" alt="The Performance & availability section for an Essentials database.">

| Setting name | Editable | Description |
|---|---|---|
| **Plan** | <span title="Yes">&#x2705; Yes</span> | The plan for your database. <br><br/>Your Essentials plan determines the size of your database and other limits. For a comparison of available plans, see [Redis Cloud Essentials plans](https://redis.io/docs/latest/operate/rc/subscriptions/view-essentials-subscription/essentials-plan-details). |
| **High Availability** | <span title="Yes">&#x2705; Yes</span> | Whether and how your data replicates across multiple nodes; see [available options](https://redis.io/docs/latest/operate/rc/databases/configuration/high-availability) |
| **Data persistence** | <span title="Yes">&#x2705; Yes</span> | Defines whether (and how) data is saved to disk; see [available options](https://redis.io/docs/latest/operate/rc/databases/configuration/data-persistence)  |
| **Remote backup**  | <span title="Yes">&#x2705; Yes</span> | When enabled, identifies a location and interval for [data backups](https://redis.io/docs/latest/operate/rc/databases/back-up-data). |
| **Data eviction policy** | <span title="Yes">&#x2705; Yes</span> | Configures which [policy](https://redis.io/docs/latest/operate/rc/databases/configuration/data-eviction-policies) is applied when your database reaches its memory limit |

### Access

The **Access** section shows the connection information for your database.

<img src="../../../../images/rc/database-details-configuration-tab-access-essentials.png" alt="The Access section for an Essentials database." width=50%>

Here, you can: 
- View the number of active connections to your database.
- View the Public endpoint of your database.
- Select **Connect** to [connect to your database](https://redis.io/docs/latest/operate/rc/databases/connect)

### Data

In the **Data** section, you can:

<img src="../../../../images/rc/database-details-configuration-tab-data-essentials.png" alt="The Data section for an Essentials database." width=40%>

- [Import data](https://redis.io/docs/latest/operate/rc/databases/import-data) into your database
- Open [Redis Insight](https://redis.io/docs/latest/operate/rc/databases/connect/insight-cloud) to explore your data.

### Security

The **Security** section helps you control access to your database.

<img src="../../../../images/rc/database-details-configuration-tab-security-essentials.png" alt="The Security section for an Essentials database.">

| Setting name | Editable | Description |
|---|---|---|
| **Default user** | <span title="Yes">&#x2705; Yes</span> | When **On**, permits access using the `default` username with a simple password. Select **Configure** to turn off the default user or change the password. See [Default user](https://redis.io/docs/latest/operate/rc/security/access-control/data-access-control/default-user) for more information. |
| **CIDR allow list** | <span title="Yes">&#x2705; Yes</span> | [Allow list](https://redis.io/docs/latest/operate/rc/security/cidr-whitelist) of IP addresses/security groups permitted to access the database. Select **Configure** to edit the CIDR allow list. |
| **Transport layer security (TLS)** | <span title="Yes">&#x2705; Yes</span> | Select **Configure** to turn on [transport layer security](https://redis.io/docs/latest/operate/rc/security/database-security/tls-ssl) (TLS) encryption for database access. |

### Database info

The **Database info** section defines basic properties about your database.

<img src="../../../../images/rc/database-details-configuration-tab-database-info-essentials.png" alt="The Database info section for an Essentials database.">

| Setting name | Editable | Description |
|---|---|---|
| **Name** | <span title="Yes">&#x2705; Yes</span> | The name given to your database |
| **ID** | <span title="No">&#x274c; No</span> | The database's numeric ID |
| **Creation** | <span title="No">&#x274c; No</span> | Date the database was created |
| **Last changed** | <span title="No">&#x274c; No</span> | Date of last update |
| **Advanced Capabilities** | <span title="No">&#x274c; No</span> | This setting appears when an [advanced capability](https://redis.io/docs/latest/operate/rc/databases/configuration/advanced-capabilities) is enabled for a database |
| **Architecture** | <span title="No">&#x274c; No</span> | Shows whether the database runs in **RAM** or is a [**Flex**](https://redis.io/docs/latest/operate/rc/databases/create-database/create-flex-database) database |
| **Version** | <span title="Yes">&#x2705; Yes</span> | The Redis version your database uses |
| **Protocol** | <span title="Yes">&#x2705; Yes</span> | Shows which version of RESP the database uses. See [Redis serialization protocol](https://redis.io/docs/latest/develop/reference/protocol-spec#resp-versions) for details |

**Pro:**

### General settings

The **General** section defines basic properties about your database.

<img src="../../../../images/rc/database-details-configuration-tab-general-flexible.png" alt="The Configuration tab of the Database details screen.">

The available settings vary according to your cloud provider and design choices. 

| Setting name              | Editable | Description |
|:--------------------------|:---------|:------------|
| **Database Name**         | <span title="Yes">&#x2705; Yes</span> | The name given to your database                                                                                                                             |
| **Subscription Name**     | <span title="No">&#x274c; No</span> | The name for the subscription your database is a part of                                                                                                    |
| **Public endpoint**       | <span title="No">&#x274c; No</span> | Public URI used by any application or client to access the database. You can [block the public endpoint](https://redis.io/docs/latest/operate/rc/security/database-security/block-public-endpoints).                                                  |
| **Private endpoint**      | <span title="No">&#x274c; No</span> | Private endpoint URI available to approved clients; use CIDR allow list, VPC peering, or other connectivity options to enable access. |
| **Tags**                  | <span title="Yes">&#x2705; Yes</span> | A list of the [tags](https://redis.io/docs/latest/operate/rc/databases/tag-database) associated with the database. Select [Manage tags](https://redis.io/docs/latest/operate/rc/databases/tag-database#configuration-tab) to manage the database tags. |
| **Vendor**                | <span title="No">&#x274c; No</span> | The Cloud vendor hosting your database: AWS, Google Cloud, or Azure.                                                   |
| **Region**                | <span title="No">&#x274c; No</span> | The Cloud vendor region hosting your database                                                  |
| **Type**                  | <span title="No">&#x274c; No</span> | Displays 'Redis', 'Redis Stack' or 'memcached' based on the value selected when the database was created                                                    |
| **Redis version**         | <span title="No">&#x274c; No</span> | Redis version of the database                                                                                                                  |
| **Auto Tiering**          | <span title="No">&#x274c; No</span> | Checked when the subscription supports Auto Tiering                                                               |
| **Active-Active Redis**   | <span title="No">&#x274c; No</span> | Checked when the database is part of an [Active-Active](https://redis.io/docs/latest/operate/rc/databases/active-active) relationship                                                                                         |
| **Creation time**         | <span title="No">&#x274c; No</span> | Date and time the database was created                                                                                                                      |
| **Last changed**          | <span title="No">&#x274c; No</span> | Date and time of last update                                                                                                                                |
| **Supported Protocol(s)** | <span title="Yes">&#x2705; Yes</span> | Shows which version of RESP the database uses. See [Redis serialization protocol](https://redis.io/docs/latest/develop/reference/protocol-spec#resp-versions) for details |
| **Advanced Capabilities**  | <span title="No">&#x274c; No</span> | This setting appears when an [advanced capability](https://redis.io/docs/latest/operate/rc/databases/configuration/advanced-capabilities) is enabled for a database                                                  |

### Performance section

The **Performance** section describes the memory size, throughput, and hashing policy for a database.

<img src="../../../../images/rc/database-details-configuration-tab-scalability-flexible.png" alt="Use the Performance section to control the size, throughput, and hashing policy for a database.">

| Setting name          | Editable | Description |
|:----------------------|:---------|:------------|
| **Dataset size** | <span title="Yes">&#x2705; Yes</span> | Maximum size (in GB) for your dataset. See [Dataset size](https://redis.io/docs/latest/operate/rc/databases/configuration/sizing#dataset-size).  |
| **Throughput**        | <span title="Yes">&#x2705; Yes</span> | Defines [throughput](https://redis.io/docs/latest/operate/rc/databases/configuration/sizing#throughput) in terms of maximum operations per second for the database. |
| **Memory used**       | <span title="No">&#x274c; No</span> | Memory currently used for your database.  |
| **High availability**    | <span title="Yes">&#x2705; Yes</span> | Replicates your data across multiple nodes; see [available options](https://redis.io/docs/latest/operate/rc/databases/configuration/high-availability)  |
| **Hashing policy**    | <span title="Yes">&#x2705; Yes</span> | Defines the [hashing policy](https://redis.io/docs/latest/operate/rc/databases/configuration/clustering#manage-the-hashing-policy).  |
| **OSS Cluster API**       | <span title="Yes">&#x2705; Yes</span> | Enables the [Cluster API](https://redis.io/docs/latest/operate/rc/databases/configuration/clustering#oss-cluster-api) for a database.<br/><br/>When this option is enabled, you cannot define a custom hashing policy.|

To learn more about these settings and when to use them, see [Sizing](https://redis.io/docs/latest/operate/rc/databases/configuration/sizing) and [Database clustering](https://redis.io/docs/latest/operate/rc/databases/configuration/clustering).

### Durability section

The Durability section helps protect your data when problems occur.  These settings define replication, persistence, backup, and eviction policies.

<img src="../../../../images/rc/database-details-configuration-tab-durability-flexible.png" alt="Use the Durability section to protect your data from unexpected problems.">

| Setting name             | Editable | Description |
|:-------------------------|:---------|:------------|
| **Data persistence**     | <span title="Yes">&#x2705; Yes</span> | Defines whether (and how) data is saved to disk; see [available options](https://redis.io/docs/latest/operate/rc/databases/configuration/data-persistence) |
| **Data eviction policy** | <span title="Yes">&#x2705; Yes</span> | Configures which [policy](https://redis.io/docs/latest/operate/rc/databases/configuration/data-eviction-policies) is applied when your database reaches its memory limit        |
| **Remote backup**        | <span title="Yes">&#x2705; Yes</span> | When enabled, identifies a location and interval for [data backups](https://redis.io/docs/latest/operate/rc/databases/back-up-data).                |
| **Active-Passive Redis** | <span title="Yes">&#x2705; Yes</span> | When enabled, identifies a path to the [linked database](https://redis.io/docs/latest/operate/rc/databases/migrate-databases#sync-using-active-passive).                                                               |

### Security section

The **Security** section helps you control access to your database.

<img src="../../../../images/rc/database-details-configuration-tab-security-flexible.png" alt="Use the Security settings to control access to your database.">

|Setting name| Editable | Description |
|:-----------|:---------|:------------|
| **Default user** | <span title="Yes">&#x2705; Yes</span> | When enabled, permits access using a simple password                                                                                                                           |
| **Default user password** | <span title="Yes">&#x2705; Yes</span> | Password for default user. A default password is assigned to the database on creation and may be updated. If you [block the public endpoint](https://redis.io/docs/latest/operate/rc/security/database-security/block-public-endpoints), you can also turn on passwordless authentication for the default user here.  |
| **CIDR allow list** | <span title="Yes">&#x2705; Yes</span> | [Allow list](https://redis.io/docs/latest/operate/rc/security/cidr-whitelist) of IP addresses/security groups permitted to access the database.                    |
| **Transport layer security (TLS)** | <span title="Yes">&#x2705; Yes</span> | Enables [transport layer security](https://redis.io/docs/latest/operate/rc/security/database-security/tls-ssl) (TLS) encryption for database access.  |

### Alerts section


The **Alerts** section defines notification emails sent to your account and the conditions that trigger them.

<img src="../../../../images/rc/database-details-configuration-tab-alerts-flexible.png" alt="The Alerts section defines the notification emails and their triggering conditions.">

The available alerts vary according to the plan type. See [Configure alerts](https://redis.io/docs/latest/operate/rc/databases/monitor-performance#configure-metric-alerts) for more information.

### Danger zone

Actions in the **Danger Zone** are permanent and should not be taken lightly.

<img src="../../../../images/rc/database-details-configuration-tab-danger-flexible.png" alt="The Danger Zone includes activities that impact data, such as deleting a database.  Use with care.">

Here, you can:

- Delete the database. Databases must be active before they can be deleted.  To learn more, see [Delete a database](https://redis.io/docs/latest/operate/rc/databases/delete-database).
- Flush the database (_Active-Active databases only_).

For best results, we recommend [backing up data](https://redis.io/docs/latest/operate/rc/databases/back-up-data) before any danger zone actions.



## Other actions and info

The **View Database** screen also has tabs that let you view:

- **Metrics**: a series of graphs showing database performance over time.  See [Monitor performance](https://redis.io/docs/latest/operate/rc/databases/monitor-performance) for more information.

- **Slowlog**: a log showing recent [slow queries](https://redis.io/docs/latest/commands/slowlog) run against your database.  The log displays when the action started, the duration, the complexity of the operation, and any parameters passed to the operation.

- **Alerts** (_Essentials databases only_): the notification emails sent to your account and the conditions that trigger them.  See [Configure alerts](https://redis.io/docs/latest/operate/rc/databases/monitor-performance#configure-metric-alerts) for more information.


## Edit database details

Editing your database depends on your plan type. Select your plan type to learn more.

**Essentials:**

You can make direct changes to your database on the database page. Any changes you make won't be saved until you review and confirm them.

After you've made changes to your database, select **Review changes** to review your changes. If your changes result in any cost changes, you'll see the cost change there.

<img src="../../../../images/rc/database-essentials-review-changes.png" alt="The Review changes button lets you review your changes and save them." width="50%">

From there, select **Confirm** or **Confirm & pay** to save your changes.

**Pro:**

Use the **Edit** button to edit database details.

<img src="../../../../images/rc/button-database-edit.png" alt="The Edit button lets you change selected database properties." width="100px">

Choose **Save database** to save your changes.

<img src="../../../../images/rc/button-database-save.png" alt="Use the Save database button to save database changes." width="150px">



Because databases exist within the context of a deployment, certain fields cannot be updated, especially those that might lead to data loss. Refer to the tables in the previous sections for your plan to learn which settings are editable.

If you need to change other details, create a new database and then migrate existing data.

## Manage the database list

The **Databases** list summarizes the status of all databases associated with your account.  

You can:

- Search by typing into the search box located above the database list.

    ![Use the search bar to filter the list.](https://redis.io/docs/latest/images/rc/database-list-search.png)

- Filter by selecting a filter type and then selecting the checkbox next to the options you want to include from the dropdown.  Select the Filter toggle, located on the right of the search bar, if the filter types are hidden.

    ![Use the filter toggle to display filter options.](https://redis.io/docs/latest/images/rc/database-list-filter.png)

    You can filter the list on **Status**, **Subscription**, **Subscription Type**, **Capabilities**, **Options**, **Tags**, and **Version**.  

    A list of selected filters appears below the filter types.

    To remove a filter click the **x** to the right of the name of that filter.  To remove all filters, select **Clear all**.

    ![Use the filter toggle to display filter options.](https://redis.io/docs/latest/images/rc/database-list-filter-selected.png)

- Select **Columns** to change what information is displayed on the list.

    ![Use the columns toggle to display column options.](https://redis.io/docs/latest/images/rc/database-list-columns.png)

- Select the **Export** button to export the current view as a CSV file.

    ![The Export button exports the current list view to CSV.](https://redis.io/docs/latest/images/rc/icon-export-to-csv.png)

- Sort the list in descending or ascending order using the arrow displayed to right of the field name in the header.  Supported fields include **Subscription**, **Database name**, **Memory usage**, and **Version**.

    ![Use the arrows in the list header to sort the list.](https://redis.io/docs/latest/images/rc/icon-list-sort-asc.png#no-click) ![The direction of the arrow corresponds to the direction of the sort.](https://redis.io/docs/latest/images/rc/icon-list-sort-desc.png#no-click)

    Select the arrow icon to change the sort order.  One sort order can be active at any given time.

- Use the controls in the list footer to change the number of items displayed in the list or to navigate.

Sort orders and filter expressions are not saved between console sessions.

