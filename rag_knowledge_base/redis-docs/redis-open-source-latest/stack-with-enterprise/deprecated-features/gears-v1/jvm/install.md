# Install RedisGears and the JVM plugin

```json metadata
{
  "schema_version": 2,
  "title": "Install RedisGears and the JVM plugin",
  "description": "",
  "categories": ["docs","operate","stack"],
  "tableOfContents": {"sections":[{"id":"prerequisites","title":"Prerequisites"},{"id":"enable-redisgears-for-a-database","title":"Enable RedisGears for a database"},{"id":"verify-the-install","title":"Verify the install"}]}

,
  "codeExamples": []
}
```


Before you can use RedisGears with the JVM, you need to install the RedisGears module and JVM plugin on your Redis Software cluster and enable them for a database.

## Prerequisites

1. Redis Software v6.0.12 or later

1. [Created a Redis Software cluster](https://redis.io/docs/latest/operate/rs/clusters/new-cluster-setup)

1. [Added nodes to the cluster](https://redis.io/docs/latest/operate/rs/clusters/add-node)

1. [Installed RedisGears and the JVM plugin](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/installing-redisgears#install-redisgears)

## Enable RedisGears for a database

1. From the Redis Software admin console's **databases** page, select the **Add** button to create a new database:

    ![The Add icon](https://redis.io/docs/latest/images/rs/icon_add.png)

1. Confirm that you want to create a new Redis database with the **Next** button.

1. On the **create database** page, give your database a name.

1. For **Redis Modules**, select the **Add** button and choose RedisGears from the **Module** dropdown list.

1. Select **Add Configuration**, enter `Plugin gears_jvm` in the box, then select the **OK** button:

    ![The Save icon](https://redis.io/docs/latest/images/rs/icon_save.png)

    > [!NOTE]
    > You can configure additional JVM options in this box. For example:<br></br>
    > `Plugin gears_jvm JvmOptions `<nobr>`'-Dproperty1=value1`</nobr> <nobr>`-Dproperty2=value2'`</nobr>
    >     

1. Select the **Activate** button.

## Verify the install

Run the `RG.JSTATS` command from a database shard to view statistics and verify that you set up RedisGears and the JVM plugin correctly:

```sh
$ shard-cli 3
172.16.0.1:12345> RG.JSTATS
```

