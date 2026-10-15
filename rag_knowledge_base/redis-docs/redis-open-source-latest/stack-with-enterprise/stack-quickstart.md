# Redis Open Source quick start

```json metadata
{
  "schema_version": 2,
  "title": "Redis Open Source quick start",
  "description": "",
  "categories": ["docs","operate","stack"],
  "tableOfContents": {"sections":[{"children":[{"id":"create-a-subscription","title":"Create a subscription"},{"id":"create-a-redis-stack-database","title":"Create a Redis Stack database"},{"id":"connect-to-the-database","title":"Connect to the database"}],"id":"set-up-a-redis-cloud-database","title":"Set up a Redis Cloud database"},{"id":"try-redis-open-source-features","title":"Try Redis Open Source features"}]}

,
  "codeExamples": []
}
```

To quickly set up a database with Redis Stack (Redis Open Source) features,
you can sign up for a free [Redis Cloud](https://cloud.redis.io/#/sign-up) subscription and create a Redis Stack database.

Alternatively, you can use one of these methods:

- [Redis Software](https://redis.io/docs/latest/operate/rs/installing-upgrading/quickstarts/redis-enterprise-software-quickstart)
- Redis Software in a [Docker container](https://redis.io/docs/latest/operate/rs/installing-upgrading/quickstarts/docker-quickstart)
- [Other platforms](https://redis.io/docs/latest/operate/kubernetes) for Redis Software

## Set up a Redis Cloud database

To set up a Redis Cloud database with Redis Stack features, follow these steps:

1. [Create a new Redis Cloud subscription](#create-a-subscription).

1. [Create a Redis Stack database](#create-a-redis-stack-database).

1. [Connect to the database](#connect-to-the-database).

For more details, see the Redis Cloud [quick start](https://redis.io/docs/latest/operate/rc/rc-quickstart).

### Create a subscription

To create a new subscription:

1. Sign in to the Redis Cloud [admin console](http://cloud.redis.io) or create a new account.

1. Select the **New subscription** button:

    ![The New subscriptions button in the admin console menu.](https://redis.io/docs/latest/images/rc/button-subscription-new.png)

1. Configure your subscription:

    1. Select **Fixed plans**.
    1. For the cloud vendor, select **Amazon Web Services** (AWS), **Google Cloud** (GCP), or **Microsoft Azure**.
    1. Select a region to deploy the subscription to.
    1. From the dataset size list, select the Free tier (30MB).
    1. Enter a name for the subscription.

1. Select the **Create subscription** button:

    ![The Create Subscription button.](https://redis.io/docs/latest/images/rc/button-subscription-create.png)

### Create a Redis Stack database

After you create a subscription, follow these steps to create a Redis Stack database:

1. Select the **New database** button:

    ![The New Database button creates a new database for your subscription.](https://redis.io/docs/latest/images/rc/button-database-new.png)

1. In **General** settings, enter a **Database name**.

1. For database **Type**, select **Redis Stack**.

1. Select the **Activate database** button:

    ![Use the Activate database button to create and activate your database.](https://redis.io/docs/latest/images/rc/button-database-activate.png)

### Connect to the database

After creating the database, you can view its **Configuration** settings. You will need the following information to connect to your new database:

- **Public endpoint**: The host address of the database
- **Redis password**/**Default user password**: The password used to authenticate with the database

With this information, you can connect to your database with the [`redis-cli`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/redis-cli) command-line tool, an application, or [Redis Insight](https://redislabs.com/redisinsight/).

## Try Redis Open Source features

To try out Redis Open Source features, follow the examples provided by the corresponding guides:

- [Redis Search quick start](https://redis.io/docs/latest/develop/get-started/search-tutorial)
- [JSON quick start](https://redis.io/docs/latest/develop/data-types/json#use-redisjson)
- [Time series quick start](https://redis.io/docs/latest/develop/data-types/timeseries)
- [Probabilistic data structures quick start](https://redis.io/docs/latest/develop/data-types/probabilistic)

