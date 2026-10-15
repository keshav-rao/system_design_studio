# Create a free database

```json metadata
{
  "schema_version": 2,
  "title": "Create a free database",
  "description": "Shows how to create a free database.",
  "categories": ["docs","operate","rc"],
  "tableOfContents": {"sections":[]}

,
  "codeExamples": []
}
```


Free databases are perfect for learning and exploring Redis. You get 30 MB of space for you to learn Redis concepts and develop application prototypes.

> [!NOTE]
> You can only have one free database per account. If you already have a free database, you can [delete it](https://redis.io/docs/latest/operate/rc/databases/delete-database) or [upgrade it to a paid Essentials plan](https://redis.io/docs/latest/operate/rc/subscriptions/view-essentials-subscription#upgrade-plan) before creating a new one.

Before creating a Redis Cloud database, you need to [create an account](https://redis.io/docs/latest/operate/rc/rc-quickstart).

To create a database in your Redis Cloud account:

1. Sign in to the [Redis Cloud console](https://cloud.redis.io).

2. Select the **New database** button.

    ![The New Database button creates a new database.](https://redis.io/docs/latest/images/rc/button-database-new.png)

    This displays the **Create database** screen. 

3. Select the type of [subscription](https://redis.io/docs/latest/operate/rc/subscriptions) you need. For this guide, select **Try 30 MB for free**.

    ![The Subscription selection panel with Free selected.](https://redis.io/docs/latest/images/rc/create-database-subscription-free.png)

    The rest of the database settings will appear.

    ![The database name, cloud vendor, and region settings.](https://redis.io/docs/latest/images/rc/create-database-free-settings.png)

4. Redis will generate a database name for you. If you want to change it, you can do so in the **Database name** field. 

1. Select the **Database version** you want to use.

1. Choose your **Cloud vendor** and **Region**. You can choose between **Amazon Web Services (AWS)**, **Google Cloud**, and **Microsoft Azure** for the Cloud Vendor. 

    ![The list of available cloud vendors.](https://redis.io/docs/latest/images/rc/create-database-essentials-cloud-vendor-list.png)

    See [Supported regions](https://redis.io/docs/latest/operate/rc/supported-regions) for a list of supported regions by cloud vendor.

6. Select **Create database**.

    ![Select the Create database button to create your new database.](https://redis.io/docs/latest/images/rc/button-create-db.png)

    When you create your database, there's a brief pause while your request is processed and then the **Database details** page appears.

You can now [connect to your database](https://redis.io/docs/latest/operate/rc/databases/connect) and start working with Redis. Once your app is ready to scale up, you can [upgrade to a paid Essentials plan](https://redis.io/docs/latest/operate/rc/subscriptions/view-essentials-subscription#upgrade-plan) at any time.
