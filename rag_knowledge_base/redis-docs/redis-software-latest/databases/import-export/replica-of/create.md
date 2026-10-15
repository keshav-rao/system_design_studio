# Create a database with Replica Of

```json metadata
{
  "schema_version": 2,
  "title": "Create a database with Replica Of",
  "description": "Create Replica Of database",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"children":[{"id":"same-cluster","title":"Same Redis Software cluster"},{"id":"different-cluster","title":"Different Redis Software cluster"},{"id":"source-available-cluster","title":"Redis Open Source cluster"},{"id":"enforce-read-only-access","title":"Enforce read-only access"}],"id":"configure-replica-of","title":"Configure Replica Of"},{"children":[{"id":"encrypt-source-database-traffic","title":"Encrypt source database traffic"},{"id":"encrypt-replica-database-traffic","title":"Encrypt replica database traffic"}],"id":"configure-tls-for-replica-of","title":"Configure TLS for Replica Of"}]}

,
  "codeExamples": []
}
```

Replica databases copy data from source databases (previously known as _master_), which enable read-only connections from apps and clients located in different geographic locations.

To create a replica connection, you define a database as a replica of a source database.  Replica Of databases (also known as _Active-Passive databases_) synchronize in the background.

Sources databases can be:

- Located in the same Redis Software cluster
- Located in a different Redis Software cluster
- Hosted by a different deployment, e.g. Redis Cloud
- Redis Open Source databases

Your apps can connect to the source database to read and write data; they can also use any replica for read-only access.

Replica Of can model a variety of data relationships, including:

- One-to-many relationships, where multiple replicas copy a single source database.
- Many-to-one relationships, where a single replica collects data from multiple source databases.

When you change the replica status of a database by adding, removing, or changing sources, the replica database is synchronized to the new sources.  

## Configure Replica Of

You can configure a database as a Replica Of, where the source database is in one of the following clusters:

- [Same Redis Software cluster](#same-cluster)

- [Different Redis Software cluster](#different-cluster)

- [Redis Open Source cluster](#source-available-cluster)

The order of the multiple Replica Of sources has no material impact on replication.

For best results when using the [Multicast DNS](https://en.wikipedia.org/wiki/Multicast_DNS) (mDNS) protocol to resolve the fully-qualified domain name (FQDN) of the cluster, verify that your client connections meet the [client mDNS prerequisites](https://redis.io/docs/latest/operate/rs/networking/mdns).

> [!NOTE]
> As long as Replica Of is enabled, data in the target database will not expire and will not be evicted regardless of the set [data eviction policy](https://redis.io/docs/latest/operate/rs/databases/memory-performance/eviction-policy).

### Same Redis Software cluster {#same-cluster}

To configure a Replica Of database in the same Redis Software cluster as the source database:

1. [Create a new database](https://redis.io/docs/latest/operate/rs/databases/create) or select an existing database from the **Databases** screen.

1. For an existing database, select **Edit** from the **Configuration** tab.

1. Expand the **Replica Of** section.

1. Select **+ Add source database**.

1. In the **Connect a Replica Of source database** dialog, select **Current cluster**.

1. Select the source database from the list.

1. Select **Add source**.

1. Select **Save**.

### Different Redis Software cluster {#different-cluster}

To configure a Replica Of database in a different Redis Software cluster from the source database:

1. Ensure the source database's port is allowed through firewalls between the clusters and can be accessed by the destination cluster's nodes.

    > [!NOTE]
    > Ports 10000-19999 are reserved for database traffic. See [Network port configurations](https://redis.io/docs/latest/operate/rs/networking/port-configurations) for more information about ports.
    >

1. Sign in to the Cluster Manager UI of the cluster hosting the source database.

    1. In **Databases**, select the source database and then select the **Configuration** tab.

    1. In the **Replica Of** section, select **Use this database as a source for another database**.

    1. Copy the Replica Of source URL.

        ![Copy the Replica Of source URL from the Connection link to destination dialog.](https://redis.io/docs/latest/images/rs/screenshots/databases/config-replica-of-copy-source-url.png)

        To change the internal password, select **Regenerate password**.

        If you regenerate the password, replication to existing destinations fails until their credentials are updated with the new password.

1. Sign in to the Cluster Manager UI of the destination database's cluster.

1. [Create a new database](https://redis.io/docs/latest/operate/rs/databases/create) or select an existing database from the **Databases** screen.

1. For an existing database, select **Edit** from the **Configuration** tab.

1. Expand the **Replica Of** section.

1. Select **+ Add source database**.

1. In the **Connect a Replica Of source database** dialog, select **External**.

1. Enter the URL of the source database endpoint.

1. Select **Add source**.

1. Select **Save**.

For source databases on different clusters, you can [compress replication data](https://redis.io/docs/latest/operate/rs/databases/import-export/replica-of#data-compression-for-replica-of) to save bandwidth.
        
### Redis Open Source cluster {#source-available-cluster}

To use a database from a Redis Open Source cluster as a Replica Of source:

1. [Create a new database](https://redis.io/docs/latest/operate/rs/databases/create) or select an existing database from the **Databases** screen.

1. For an existing database, select **Edit** from the **Configuration** tab.

1. Expand the **Replica Of** section.

1. Select **+ Add source database**.

1. In the **Connect a Replica Of source database** dialog, select **External**.

1. Enter the URL of the source endpoint in one of the following formats:

    - For databases with passwords:

        ```sh
        redis://:<password>@<host>:<port>
        ```

        Where the password is the Redis password represented with URL encoding escape characters.

    - For databases without passwords:

        ```sh
        redis://<host>:<port>
        ```

1. Select **Add source**.

1. Select **Save**.

### Enforce read-only access

Writing directly to a Replica Of destination database is not supported and can result in replication errors, data inconsistencies, or data loss.

As of Redis Software version 7.22.0-95, you can set `replica_read_only` to `true` when you [create a Replica Of database](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/bdbs#post-bdbs-v2) using the REST API. When enabled, the destination database rejects all write operations to prevent accidental writes. Replication remains one-way from source to destination. You cannot change `replica_read_only` after database creation.

To enforce read-only access when you create a Replica Of destination database:

```sh
POST https://<host>:<port>/v2/bdbs
{
  "name": "readonly-replica-db",
  "memory_size": 1073741824,
  "replica_sources": [
    {
      "uri": "redis://admin:<password>@<source-host>:<port>"
    }
  ],
  "replica_read_only": true,
  // Additional fields
}
```

For additional database configuration fields, see the [BDB object](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/bdb) reference.

For Redis Software versions earlier than 7.22.0-95, there is no product-level enforcement preventing writes to the destination database, so you should configure your application to direct all write operations exclusively to the source database.

## Configure TLS for Replica Of

When you enable TLS for Replica Of, the Replica Of synchronization traffic uses TLS certificates to authenticate the communication between the source and destination clusters.

To encrypt Replica Of synchronization traffic, configure encryption for the [source database](#encrypt-source-database-traffic) and the destination [replica database](#encrypt-replica-database-traffic).

### Encrypt source database traffic

To enable TLS for Replica Of cluster connections:

1. For each cluster hosting a replica:

    1. Go to **Cluster > Security > Certificates**.

    1. Expand the **Replica Of and Active-Active authentication (Syncer certificate)** section.

        ![Syncer certificate for Replica Of and Active-Active authentication.](https://redis.io/docs/latest/images/rs/screenshots/cluster/security-syncer-cert.png)
    
    1. Download or copy the syncer certificate.

1. From the **Security** tab of the Replica Of source database, select **Edit**.

1. In the **TLS - Transport Layer Security for secure connections** section, make sure the checkbox is selected.

1. In the **Apply TLS for** section, select **Between databases only**.

1. Select **Mutual TLS (Client authentication)**.

    ![Replica Of TLS authentication configuration.](https://redis.io/docs/latest/images/rs/screenshots/databases/security-tls-replica-of.png)

1. Select **+ Add certificate**, paste or upload the syncer certificate, then select **Done**.

    Repeat this process, adding the syncer certificate for each cluster hosting a replica of this database.

1. _(Optional)_ To require TLS for client connections, change **Apply TLS for** to **Clients and databases + Between databases** and add client certificates.

1. Select **Save**.

### Encrypt replica database traffic

To enable TLS for Replica Of in the destination database:

1. From the Cluster Manager UI of the cluster hosting the source database:

    1. Go to **Cluster > Security > Certificates**.

    1. Expand the **Server authentication (Proxy certificate)** section.

        ![Proxy certificate for server authentication.](https://redis.io/docs/latest/images/rs/screenshots/cluster/security-proxy-cert.png)

     1. Download or copy the proxy certificate.

1. From the **Configuration** tab of the Replica Of destination database, select **Edit**.

1. Expand the **Replica Of** section.

1. Point to the source database entry and select ![The Edit button](https://redis.io/docs/latest/images/rs/buttons/edit-button.png#no-click) to edit it.

1. Paste or upload the source proxy certificate, then select **Done**.

1. Select **Save**.

