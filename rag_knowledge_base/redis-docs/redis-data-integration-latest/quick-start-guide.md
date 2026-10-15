# Quickstart

```json metadata
{
  "schema_version": 2,
  "title": "Quickstart",
  "description": "Get started with a simple pipeline example",
  "categories": ["redis-di"],
  "tableOfContents": {"sections":[{"id":"prerequisites","title":"Prerequisites"},{"children":[{"id":"install-postgresql","title":"Install PostgreSQL"},{"id":"install-rdi","title":"Install RDI"},{"id":"prepare-the-pipeline","title":"Prepare the pipeline"},{"id":"create-context","title":"Create a context (optional)"},{"id":"deploy-the-pipeline","title":"Deploy the pipeline"},{"id":"view-rdis-response-to-data-changes","title":"View RDI's response to data changes"}],"id":"overview","title":"Overview"}]}

,
  "codeExamples": []
}
```


In this tutorial you will learn how to install RDI and set up a pipeline to ingest live data from a [PostgreSQL](https://www.postgresql.org/) database into a Redis database.

## Prerequisites

- A Redis Enterprise database that will serve as the pipeline target. The dataset that will be ingested is
  quite small in size, so a single shard database should be enough. RDI also needs to maintain its
  own database on the cluster to store state information. *This requires Redis Enterprise v6.4 or greater*.
- [Redis Insight](https://redis.io/docs/latest/develop/tools/insight)
  to edit your pipeline
- A virtual machine (VM) with one of the following operating systems:  
  * RHEL 8 or 9
* Ubuntu 20.04, 22.04, or 24.04

## Overview

The following diagram shows the structure of the pipeline we will create (see
the [architecture overview](https://redis.io/docs/latest/integrate/redis-data-integration/architecture#overview) to learn how the pipeline works):

![](https://redis.io/docs/latest/images/rdi/ingest/ingest-qsg.webp)

Here, the RDI *collector* tracks changes in PostgreSQL and writes them to streams in the 
RDI database in Redis. The *stream processor* then reads data records from the RDI
database streams, processes them, and writes them to the target.

### Install PostgreSQL

We provide a [Docker](https://www.docker.com/) image for an example PostgreSQL
database that we will use for the tutorial. Follow the
[instructions on our Github page](https://github.com/Redislabs-Solution-Architects/rdi-quickstart-postgres/tree/main)
to download the image and start serving the database. The database, which is
called `chinook`, has the [schema and data](https://www.kaggle.com/datasets/samaxtech/chinook-music-store-data?select=schema_diagram.png) for an imaginary online music store
and is already set up for the RDI collector to use.

### Install RDI

Install RDI using the instructions in the
[VM installation guide](https://redis.io/docs/latest/integrate/redis-data-integration/installation/install-vm).

RDI will create the pipeline template for your chosen source database type at
`/opt/rdi/config`. You will need this pathname later when you prepare the pipeline for deployment
(see [Prepare the pipeline](#prepare-the-pipeline) below).

At the end of the installation, RDI CLI will prompt you to set the access secrets
for both the source PostgreSQL database and the target Redis database. RDI needs these to
run the pipeline.

Use the Redis Enterprise Cluster Manager UI to create the RDI database with the following requirements:

* Redis Enterprise v6.4 or greater for the cluster.
* For production, 250MB RAM with one primary and one replica is recommended, but for the
  quickstart or for development, 125MB and a single shard is sufficient.
* If you are deploying RDI for a production environment then secure this database with a password
  and TLS.
* Set the database's
  [eviction policy](https://redis.io/docs/latest/operate/rs/databases/memory-performance/eviction-policy) to `noeviction`. Note that you can't set this using
  [`rladmin`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin),
  so you must either do it using the admin UI or with the following
  [REST API](https://redis.io/docs/latest/operate/rs/references/rest-api)
  command:

  ```bash
  curl -v -k -d '{"eviction_policy": "noeviction"}' \
    -u '<USERNAME>:<PASSWORD>' \
    -H "Content-Type: application/json" \
    -X PUT https://<CLUSTER_FQDN>:9443/v1/bdbs/<BDB_UID>
  ```
* Set the database's
  [data persistence](https://redis.io/docs/latest/operate/rs/databases/configure/database-persistence)
  to AOF - fsync every 1 sec. Note that you can't set this using
  [`rladmin`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin),
  so you must either do it using the admin UI or with the following
  [REST API](https://redis.io/docs/latest/operate/rs/references/rest-api)
  commands:

  ```bash
  curl -v -k -d '{"data_persistence":"aof"}' \
    -u '<USERNAME>:<PASSWORD>' \
    -H "Content-Type: application/json" 
    -X PUT https://<CLUSTER_FQDN>:9443/v1/bdbs/<BDB_UID>
  curl -v -k -d '{"aof_policy":"appendfsync-every-sec"}' \
    -u '<USERNAME>:<PASSWORD>' \
    -H "Content-Type: application/json" \
    -X PUT https://<CLUSTER_FQDN>:9443/v1/bdbs/<BDB_UID>
  ```
 If you don't have permissions to use AOF persistence, please check the [Using RDI without persistence](https://redis.io/docs/latest/integrate/redis-data-integration/faq#can-i-use-rdi-without-persistence-enabled) section in the FAQ.

* **Ensure that the RDI database is not clustered.** RDI will not work correctly if the
  RDI database is clustered (but note that the target database *can* be clustered without
  any problems).

  When you create the RDI database, expand the **Clustering** section and make sure the
  **Sharding** option is *unchecked* (as shown below).

  ![The Sharding option is unchecked in the Clustering section of the create database form.](https://redis.io/docs/latest/images/rdi/ingest/RDIClusterSetting.webp)

  You can check if your RDI database is clustered from its **Configuration** tab in the
  Cluster Manager UI. In the **Clustering** section, **Sharding** should be set to **Disabled**,
  as shown in the following screenshot:

  ![The Clustering section of the database Configuration tab shows Sharding: Disabled.](https://redis.io/docs/latest/images/rdi/ingest/RDICheckUnclustered.webp)

  If you find the database has been clustered by mistake, you must create a new database with
  sharding disabled before continuing with the RDI installation.


### Prepare the pipeline

During the installation, RDI placed the pipeline templates at `/opt/rdi/config`.
If you go to that folder and run the `ll` command, you will see the pipeline
configuration file, `config.yaml`, and the `jobs` folder (see the page about
[Pipelines](https://redis.io/docs/latest/integrate/redis-data-integration/data-pipelines) for more information). Use Redis Insight to open
the `config.yaml` file and then edit the following settings:

- Set the `host` to `localhost` and the `port` to 5432.
- Under `tables`, specify the `Track` table from the source database.
- Add the details of your target database to the `target` section.

At this point, the pipeline is ready to deploy.

This tutorial uses one source database, but a pipeline can capture from several source databases
into the same Redis target. See
[Multiple sources in one pipeline](https://redis.io/docs/latest/integrate/redis-data-integration/data-pipelines/multiple-sources) for more information.

### Create a context (optional) {#create-context}

To manage and inspect RDI, you can use the
[`redis-di`](https://redis.io/docs/latest/integrate/redis-data-integration/reference/cli)
CLI tool, which has several commands for different purposes. Most of these commands connect to
the RDI API, which you specify with the `--api-url` option. You can avoid typing this and the other
connection options repeatedly by saving them in a *context*.

When you activate a context, its saved connection options are used automatically whenever
you use `redis-di`. If you have more than one RDI installation, you can create a context
for each of them and select the one you want to be active using its unique name.

To create a context, use the
[`redis-di set-context`](https://redis.io/docs/latest/integrate/redis-data-integration/reference/cli/redis-di-set-context)
command. For a VM installation, the API has the same hostname or IP address as your RDI VM and uses
the default HTTPS port 443:

```bash
redis-di set-context <unique-context-name> --api-url https://<host> --user <user>
```

You can save a few other options, such as a CA certificate (`--cacert`) if the API uses a private
certificate (see the
[reference page](https://redis.io/docs/latest/integrate/redis-data-integration/reference/cli/redis-di-set-context)
for details). When you have created a context, use
[`redis-di use-context`](https://redis.io/docs/latest/integrate/redis-data-integration/reference/cli/redis-di-use-context)
to activate it:

```bash
redis-di use-context <context name>
```

There are also subcommands to
[list](https://redis.io/docs/latest/integrate/redis-data-integration/reference/cli/redis-di-list-contexts)
and [delete](https://redis.io/docs/latest/integrate/redis-data-integration/reference/cli/redis-di-delete-context)
contexts.

### Deploy the pipeline

You can deploy the pipeline with the following command:

```bash
redis-di deploy --dir <path to pipeline folder>
```

where the path is the one you supplied earlier during the installation. (You may also need
to supply the `--api-url` option if you are not using a
[context](#create-context) as described above.) RDI first
validates your pipeline and then deploys it if the configuration is correct.

You can also use [Redis Insight](https://redis.io/docs/latest/develop/tools/insight/rdi-connector)
to deploy the pipeline, by adding a connection to the RDI API
endpoint (which has the same hostname or IP address as your RDI VM and uses the default HTTPS port 443) and then clicking the **Deploy** button.

Once the pipeline is running, you can use Redis Insight to view the data flow using the
pipeline metrics. You can also connect to your target database to see the keys that RDI has written there.

See [Deploy a pipeline](https://redis.io/docs/latest/integrate/redis-data-integration/data-pipelines/deploy)
for more information about deployment settings.

### View RDI's response to data changes

Once the pipeline has loaded a *snapshot* of all the existing data from the source,
it enters *change data capture (CDC)* mode (see the
[architecture overview](https://redis.io/docs/latest/integrate/redis-data-integration/architecture#overview)
and the
[ingest pipeline lifecycle](https://redis.io/docs/latest/integrate/redis-data-integration/data-pipelines#pipeline-lifecycle)
for more information
).

To see the RDI pipeline working in CDC mode:
 
- Create a simulated load on the source database
  (see [Generating load on the database](https://github.com/Redislabs-Solution-Architects/rdi-quickstart-postgres?tab=readme-ov-file#generating-load-on-the-database)
  to learn how to do this).
- Run
  [`redis-di describe`](https://redis.io/docs/latest/integrate/redis-data-integration/reference/cli/redis-di-describe)
  to see the flow of records. To watch it update live, pair the command with `watch`, for example
  `watch -n 1 redis-di describe`.
- Use [Redis Insight](https://redis.io/docs/latest/develop/tools/insight) to look at the data in the target database.

