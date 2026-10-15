# Enable TLS

```json metadata
{
  "schema_version": 2,
  "title": "Enable TLS",
  "description": "Shows how to enable TLS.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"children":[{"id":"enable-mutual-tls","title":"Enable mutual TLS"},{"id":"validate-client-certificate-expiration","title":"Validate client certificate expiration"},{"id":"connect-over-tls","title":"Connect over TLS"}],"id":"client","title":"Enable TLS for client connections"},{"children":[{"id":"enable-tls-during-database-creation","title":"Enable TLS during database creation"},{"id":"enable-tls-after-database-creation","title":"Enable TLS after database creation"}],"id":"enable-tls-for-active-active-cluster-connections","title":"Enable TLS for Active-Active cluster connections"},{"id":"enable-tls-for-replica-of-cluster-connections","title":"Enable TLS for Replica Of cluster connections"}]}

,
  "codeExamples": []
}
```


You can use TLS authentication for one or more of the following types of communication:

- Communication from clients (applications) to your database
- Communication from your database to other clusters for replication using [Replica Of](https://redis.io/docs/latest/operate/rs/databases/import-export/replica-of)
- Communication to and from your database to other clusters for synchronization using [Active-Active](https://redis.io/docs/latest/operate/rs/databases/active-active)

> [!NOTE]
> When you enable or turn off TLS, the change applies to new connections but does not affect existing connections. You must update TLS parameters in the client's connection configuration, then clients must close existing connections and reconnect to apply the change.

## Enable TLS for client connections {#client}

**Cluster Manager UI:**

To enable TLS for client connections using the Cluster Manager UI:

1. From your database's **Security** tab, select **Edit**.

1. Expand the **TLS - Transport Layer Security for secure connections** section, then select **On**.

1. In the **Apply TLS for** section, select **Clients and databases + Between databases**.

1. Select **Save**.

**REST API:**

You can also enable TLS for client connections using the REST API.

To enable TLS for client connections during database creation, include `"tls_mode": "enabled"` when you [create a database](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/bdbs#post-bdbs-v1):

```sh
POST https://<host>:<port>/v1/bdbs
{
  "tls_mode": "enabled",
  // Additional fields
}
```

For additional database configuration fields, see the [BDB object](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/bdb) reference.

To enable TLS for client connections after database creation, you can use an [update database configuration](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/bdbs#put-bdbs) REST API request:

```sh
PUT https://<host>:<port>/v1/bdbs/<database_id>
{
  "tls_mode": "enabled"
}
```



### Enable mutual TLS

Optionally, you can enable mutual TLS for client connections.

**Cluster Manager UI:**

To enable mutual TLS using the Cluster Manager UI:

1. Select **Mutual TLS (Client authentication)**.

    ![Mutual TLS authentication configuration.](https://redis.io/docs/latest/images/rs/screenshots/databases/security-mtls-clients-7-8-2.png)

1. For all clients, upload a client certificate, an intermediary certificate, or a trusted client CA certificate.

    1. Click **+ Add certificate**.

    1. Paste or upload the client certificate, intermediary certificate, or trusted client CA certificate.

    1. Click **Done**.

    If your database uses Replica Of, you also need to add the syncer certificates for the participating clusters. See [Enable TLS for Replica Of cluster connections](#enable-tls-for-replica-of-cluster-connections) for instructions.

1. You can configure **Additional certificate validations** to further limit connections to clients with valid certificates.

    Additional certificate validations occur only when loading a [certificate chain](https://en.wikipedia.org/wiki/Chain_of_trust#Computer_security) that includes the [root certificate](https://en.wikipedia.org/wiki/Root_certificate) and intermediate [CA](https://en.wikipedia.org/wiki/Certificate_authority) certificate but does not include a leaf (end-entity) certificate. If you include a leaf certificate, mutual client authentication skips any additional certificate validations.

    1. Select a certificate validation option.

        | Validation option | Description |
        |-------------------|-------------|
        | _No validation_ | Authenticates clients with valid certificates. No additional validations are enforced. |
        | _By Subject Alternative Name_ | A client certificate is valid only if its Subject Alternative Name (SAN) DNS entries or Common Name (CN) match an entry in the list of valid subjects. Ignores other [`Subject`](https://datatracker.ietf.org/doc/html/rfc5280#section-4.1.2.6) attributes. |
        | _By full Subject Name_ | A client certificate is valid only if its [`Subject`](https://datatracker.ietf.org/doc/html/rfc5280#section-4.1.2.6) attributes match an entry in the list of valid subjects. |

    1. If you selected **No validation**, you can skip this step. Otherwise, select **+ Add validation** to create a new entry and then enter valid [`Subject`](https://datatracker.ietf.org/doc/html/rfc5280#section-4.1.2.6) attributes for your client certificates. All `Subject` attributes are case-sensitive.

        | Subject attribute<br />(case-sensitive) | Description |
        |-------------------|-------------|
        | _Common Name (CN)_ | Name of the client authenticated by the certificate (_required_) |
        | _Organization (O)_ | The client's organization or company name |
        | <nobr>_Organizational Unit (OU)_</nobr> | Name of the unit or department within the organization |
        | _Locality (L)_ | The organization's city |
        | _State / Province (ST)_ | The organization's state or province |
        | _Country (C)_ | 2-letter code that represents the organization's country |

        You can only enter a single value for each field, except for the _Organizational Unit (OU)_ field. If your client certificate has a `Subject` with multiple  _Organizational Unit (OU)_ values, press the `Enter` or `Return` key after entering each value to add multiple Organizational Units.

        ![An example that shows adding a certificate validation with multiple organizational units.](https://redis.io/docs/latest/images/rs/screenshots/databases/security-mtls-add-cert-validation-multi-ou.png)

        **Breaking change:** If you use the [REST API](https://redis.io/docs/latest/operate/rs/references/rest-api) instead of the Cluster Manager UI to configure additional certificate validations, note that `authorized_names` is deprecated as of Redis Software v6.4.2. Use `authorized_subjects` instead. See the [BDB object reference](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/bdb) for more details.

1. Select **Save**.

**REST API:**

You can also enable mutual TLS using the REST API.

To enable mutual TLS during database creation, include the following fields when you [create a database](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/bdbs#post-bdbs-v1):

```sh
POST https://<host>:<port>/v1/bdbs
{
  "authorized_subjects": [{
    "CN": <string>,
    "O": <string>,
    "OU": [<array of strings>],
    "L": <string>,
    "ST": <string>,
    "C": <string>
  }],
  "authentication_ssl_client_certs": [{
    "client_cert": "-----BEGIN CERTIFICATE-----\n...\n-----END CERTIFICATE-----\n"
  }],
  "client_cert_subject_validation_type": <"disabled" | "san_cn" | "full_subject">,
  "enforce_client_authentication": "enabled",
  "tls_mode": "enabled",
  // Additional fields
}
```

For additional database configuration fields, see the [BDB object](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/bdb) reference.

To enable mutual TLS after database creation, you can use an [update database configuration](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/bdbs#put-bdbs) REST API request:

```sh
PUT https://<host>:<port>/v1/bdbs/<database_id>
{
  "authorized_subjects": [{
    "CN": <string>,
    "O": <string>,
    "OU": [<array of strings>],
    "L": <string>,
    "ST": <string>,
    "C": <string>
  }],
  "authentication_ssl_client_certs": [{
    "client_cert": "-----BEGIN CERTIFICATE-----\n...\n-----END CERTIFICATE-----\n"
  }],
  "client_cert_subject_validation_type": <"disabled" | "san_cn" | "full_subject">,
  "enforce_client_authentication": "enabled",
  "tls_mode": "enabled"
}
```



### Validate client certificate expiration

By default, Redis Software validates client certificate expiration dates.  You can use [`rladmin tune db`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/tune#tune-db) to turn off this behavior.

```sh
rladmin tune db < db:id | name > mtls_allow_outdated_certs { enabled | disabled }
```

### Connect over TLS

To connect to a Redis Software database over TLS using [`redis-cli`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/redis-cli):

1. Download or copy the server (or proxy) certificate from the Cluster Manager UI (**Cluster > Security > Certificates > Server authentication**) or from a cluster node (`/etc/opt/redislabs/proxy_cert.pem`).

1. Copy the certificate to each client machine.

1. If your database doesn't require client authentication with mutual TLS, provide the server certificate when you connect:

    ```sh
    redis-cli -h <endpoint> -p <port> --tls --cacert proxy_cert.pem
    ```

1. If your database requires client authentication with mutual TLS, provide your client's private and public keys along with the Redis Software server certificate when you connect:

    ```sh
    redis-cli -h <endpoint> -p <port> --tls --cacert proxy_cert.pem \
        --cert redis_user.crt --key redis_user_private.key
    ```

## Enable TLS for Active-Active cluster connections

You can enable TLS for Active-Active cluster connections when you create a database using the Cluster Manager UI, [`crdb-cli`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/crdb-cli), or the [REST API](https://redis.io/docs/latest/operate/rs/references/rest-api).

If you need to enable or turn off TLS after the Active-Active database is created, you must use [`crdb-cli`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/crdb-cli) or the [REST API](https://redis.io/docs/latest/operate/rs/references/rest-api).

### Enable TLS during database creation

To enable TLS for Active-Active cluster connections using the Cluster Manager UI:

1. During [database creation](https://redis.io/docs/latest/operate/rs/databases/active-active/create), expand the **TLS** configuration section.

1. Select **On** to enable TLS.

    ![TLS is enabled on the Cluster Manager UI screen.](https://redis.io/docs/latest/images/rs/screenshots/databases/active-active-databases/enable-tls-for-active-active-db.png)

1. Click **Create**.

If you also want to require TLS for client connections during creation, you can use the [create an Active-Active database](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/crdbs#post-crdb) REST API request to create an Active-Active database with TLS enabled for client connections.
You should configure the client certificates individually for each instance instead of using the default database configuration, even if the same certificate is used across all instances.
This allows you to rotate the certificates independently for each instance and to avoid outages in case of certificate expiration.

```json
POST https://<host>:9443/v1/crdb
{
  "name": "crdb-mtls",
  "default_db_config": {
    "name": "crdb-mtls",
    "bigstore": false,
    "memory_size": 4294967296
  },
  "encryption": true,
  "instances": [
    {
      "cluster": {
        "name": "<cluster1_host>",
        "url": "https://<cluster1_host>:9443",
        "credentials": {
          "username": "<username>",
          "password": "<password>"
        }
      },
      "db_config": {
        "tls_mode": "enabled",
        "enforce_client_authentication": "enabled",
        "authentication_ssl_client_certs": [
          {
            "client_cert": "-----BEGIN CERTIFICATE-----\n...\n-----END CERTIFICATE-----\n"
          }
        ]
      }
    },
    {
      "cluster": {
        "name": "<cluster2_host>",
        "url": "https://<cluster2_host>:9443",
        "credentials": {
          "username": "<username>",
          "password": "<password>"
        }
      },
      "db_config": {
        "tls_mode": "enabled",
        "enforce_client_authentication": "enabled",
        "authentication_ssl_client_certs": [
          {
            "client_cert": "-----BEGIN CERTIFICATE-----\n...\n-----END CERTIFICATE-----\n"
          }
        ]
      }
    }
  ],
  "causal_consistency": false
}
```

### Enable TLS after database creation

You can enable TLS for an existing Active-Active database using either `crdb-cli` or the REST API.

**CLI:**

Run the following [`crdb-cli crdb update`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/crdb-cli/crdb/update) command:

```sh
crdb-cli crdb update --crdb-guid <guid> --encryption true
```

Replace `<guid>` with your Active-Active database's globally unique identifier.

**REST API:**

You can use an [update database configuration](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/bdbs#put-bdbs) request to enable TLS.

To enable TLS for Active-Active database communications only:

```sh
PUT https://<host>:9443/v1/bdbs/<database-id>
{
  "enforce_client_authentication": "disabled",
  "tls_mode": "replica_ssl"
}
```

To enable TLS for all communications:

```sh
PUT https://<host>:9443/v1/bdbs/<database-id>
{
  "enforce_client_authentication": "disabled",
  "tls_mode": "enabled"
}
```



## Enable TLS for Replica Of cluster connections

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

