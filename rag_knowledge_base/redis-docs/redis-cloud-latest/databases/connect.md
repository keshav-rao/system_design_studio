# Connect to a Redis Cloud database

```json metadata
{
  "schema_version": 2,
  "title": "Connect to a Redis Cloud database",
  "description": "",
  "categories": ["docs","operate","rc"],
  "tableOfContents": {"sections":[{"children":[{"id":"database-endpoints","title":"Database endpoints"},{"id":"database-username-and-password","title":"Database username and password"}],"id":"get-connection-information","title":"Get connection information"},{"children":[{"id":"using-redisinsight","title":"Redis Insight"},{"id":"using-redis-client","title":"Redis client"}],"id":"connect-to-your-database-with-connection-wizard","title":"Connect to your database with connection wizard"},{"id":"more-info","title":"More info"}]}

,
  "codeExamples": []
}
```


After you [create your database](https://redis.io/docs/latest/operate/rc/databases/create-database), you can connect to it using the public or private endpoint.

## Get connection information

To connect to the database, you need the following information:
- The database endpoint
- Your database username and password

### Database endpoints

The database endpoints are listed in the **Configuration** tab for your database: in the **Access** section for Essentials databases, or the **General** section for Pro databases.

![The General section of the Configuration tab of the Pro database details page.](https://redis.io/docs/latest/images/rc/databases-configuration-general-endpoints.png)

![The Access section for an Essentials database.](https://redis.io/docs/latest/images/rc/database-details-configuration-tab-access-essentials.png)

Redis Cloud Pro and Redis Cloud Essentials databases have a public endpoint, which you can access from the public internet. Redis Cloud Pro databases also have a private endpoint. You can connect to the private endpoint from a private network. Before you can connect to the private endpoint, you must set up a private connectivity method, such as:
- [VPC peering](https://redis.io/docs/latest/operate/rc/security/vpc-peering)
- [Google Cloud Private Service Connect](https://redis.io/docs/latest/operate/rc/security/private-service-connect) (Google Cloud only)
- [AWS Transit Gateway](https://redis.io/docs/latest/operate/rc/security/aws-transit-gateway) or [AWS PrivateLink](https://redis.io/docs/latest/operate/rc/security/aws-privatelink) (AWS only)

Redis Cloud Pro users can block the public endpoint for their databases. For more information, see [Block public endpoints](https://redis.io/docs/latest/operate/rc/security/database-security/block-public-endpoints).

#### Static and dynamic endpoints

Static endpoints on Redis Cloud start with `redis-<port>.c<number>` (or `redis-<port>.internal.c<number>` for the private endpoint). For example, a static endpoint might look like this:

```text
redis-12345.c12345.us-east-1-mz.ec2.cloud.rlrcp.com
```

Dynamic endpoints on Redis Cloud always contain three words and a random number, and end in `db.redis.io`. For example, a dynamic endpoint might look like this:

```text
horse-battery-staple-12345.db.redis.io
```

You can see the Dynamic endpoints for databases with both static and dynamic endpoints by expanding the **Dynamic endpoints** section in the **General** section of the **Configuration** tab. 

![The Static and dynamic endpoints for a database with both kinds of endpoints.](https://redis.io/docs/latest/images/rc/databases-configuration-general-endpoints-legacy.png)

You can redirect the dynamic endpoints to a different database at any time, but you cannot redirect the static endpoints. We recommend using the dynamic endpoints for your application so that you can migrate your database endpoints to a different database in the future without any code changes. See [Redirect dynamic endpoints](https://redis.io/docs/latest/operate/rc/databases/redirect-endpoints) for more information.

### Database username and password

By default, your database is protected by a [**Default user**](https://redis.io/docs/latest/operate/rc/security/access-control/data-access-control/default-user) with the username `default` and a masked **Default user password**. For Essentials databases, select **Default user > Configure** and then select the eye icon to view your password. 

For Pro databases, you can see the default user password in the **Security** section of the **Configuration** details for your database. Select the eye icon to show or hide the password.    

If you've turned on [Role-based access control](https://redis.io/docs/latest/operate/rc/security/access-control/data-access-control/role-based-access-control) for your database and [turned off the default User](https://redis.io/docs/latest/operate/rc/security/access-control/data-access-control/default-user#turn-off-default-user), use the username and password for your data access role.

## Connect to your database with connection wizard

Select **Connect** to open the connection wizard.

![Connect button.](https://redis.io/docs/latest/images/rc/button-connect.png#no-click)

> [!NOTE]
> For [Active-Active databases](https://redis.io/docs/latest/operate/rc/databases/active-active), you connect to one of the database instances. Choose the region you want to connect to from the region selection to access the connection information for that instance.

The connection wizard provides the following database connection methods:

- [Redis Insight](#using-redisinsight)

- [`redis-cli`](#using-rediscli) utility

- [Redis client](#using-redis-client) for your preferred programming language

![The connection wizard.](https://redis.io/docs/latest/images/rc/connection-wizard.png)

### Redis Insight {#using-redisinsight}

[Redis Insight](https://redis.io/docs/latest/develop/tools/insight) is a free Redis GUI that lets you visualize your Redis data and learn more about Redis.

You can connect to your database with Redis Insight in two ways:

1. [Open your database in Redis Insight in your browser](#ri-browser).

1. [Download and Install Redis Insight](#ri-app) on Windows, macOS, and Linux.

#### Open in your browser {#ri-browser}

> [!NOTE]
> Opening your database with Redis Insight in your browser is only available for Essentials databases. For all other databases, [Download and install Redis Insight](#ri-app) on your computer.

If Redis Insight on Redis Cloud is available for your database, select **Launch Redis Insight web** from the connection wizard to open it.

![Launch Redis Insight web from the Connection Wizard.](https://redis.io/docs/latest/images/rc/rc-ri-wizard-launch.png)

You can also select **Launch** from the database page under **View and manage data with Redis Insight** to open Redis Insight in your browser.

![Launch Redis Insight web from the database page.](https://redis.io/docs/latest/images/rc/rc-ri-open.png)

Redis Insight will open in a new tab. 

This browser-based version of Redis Insight has a subset of the features of Redis Insight. For more information, see [Open with Redis Insight on Redis Cloud](https://redis.io/docs/latest/operate/rc/databases/connect/insight-cloud).

#### Install and open on your computer {#ri-app}

1. If you haven't downloaded Redis Insight, select **Download** under **Redis Insight** in the Connection wizard to download it. 

1. [Install Redis Insight](https://redis.io/docs/latest/develop/tools/insight).

1. Once installed, select **Open with Redis Insight**.

1. A pop-up asks if you wish to open the link with Redis Insight. Select **Open Redis Insight** to connect to your database with Redis Insight.

If you get an error when connecting with Redis Insight, [manually connect to your database](https://redis.io/docs/latest/develop/tools/insight) from Redis Insight.

You can use Redis Insight to view your data, run Redis commands, and analyze database performance. See the [Redis Insight docs](https://redis.io/docs/latest/develop/tools/insight) for more info.

### Redis client {#using-redis-client}

A Redis client is a software library or tool that enables applications to interact with a Redis server. Each client has its own syntax and installation process. For help with a specific client, see the client's documentation.

The connection wizard provides code snippets to connect to your database with the following programming languages:

- .NET using [StackExchange.Redis/NRedisStack](https://redis.io/docs/latest/develop/clients/dotnet)
- node.js using [node-redis](https://redis.io/docs/latest/develop/clients/nodejs)
- Python using [redis-py](https://redis.io/docs/latest/develop/clients/redis-py)
- Java using [Jedis](https://redis.io/docs/latest/develop/clients/jedis) and [Lettuce](https://redis.io/docs/latest/develop/clients/lettuce)
- Go using [go-redis](https://redis.io/docs/latest/develop/clients/go)
- PHP using [Predis](https://redis.io/docs/latest/develop/clients/php)

![The connection wizard clients.](https://redis.io/docs/latest/images/rc/connection-wizard-clients.png)

If the username and password are not already filled in, replace `<username>` and `<password>` with your username and password.

See [Clients](https://redis.io/docs/latest/develop/clients) to learn how to connect with the official Redis clients.

> [!NOTE]
> We recommend using the [dynamic endpoints](#static-and-dynamic-endpoints) for your application so that you can migrate your database endpoints to a different database in the future without any code changes.  See [Redirect dynamic endpoints](https://redis.io/docs/latest/operate/rc/databases/redirect-endpoints) for more information.

#### redis-cli {#using-rediscli}

The [`redis-cli`](https://redis.io/docs/latest/develop/tools/cli) utility is installed when you install Redis.  It provides a command-line interface that lets you work with your database using core [Redis commands](/content/commands).

To run `redis-cli`, [install Redis](https://redis.io/docs/latest/operate/oss_and_stack/install/install-stack) on your machine. After it's installed, copy the `redis-cli` command under **Redis CLI** in the connection wizard and enter it into your terminal. If the username and password are not already filled in, replace `<username>` and `<password>` with your username and password.

If you only need the Redis CLI (`redis-cli`) and not the full Redis Open Source distribution, you can [install the standalone `redis-cli` binary](https://redis.io/docs/latest/operate/oss_and_stack/install/install-stack/install-redis-cli) on Linux or macOS.

See [Redis CLI](https://redis.io/docs/latest/develop/tools/cli) to learn how to use `redis-cli`.

## More info

- [Connect your application](https://redis.io/docs/latest/develop/clients)
- [Connect with TLS](https://redis.io/docs/latest/operate/rc/security/database-security/tls-ssl#connect-over-tls)
- [Default user](https://redis.io/docs/latest/operate/rc/security/access-control/data-access-control/default-user)
- [Role-based access control](https://redis.io/docs/latest/operate/rc/security/access-control/data-access-control/role-based-access-control)
