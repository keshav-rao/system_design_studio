# Set up Redis for Bedrock

```json metadata
{
  "schema_version": 2,
  "title": "Set up Redis for Bedrock",
  "description": "Shows how to set up your Redis database for Amazon Bedrock.",
  "categories": ["docs","integrate","oss","rs","rc"],
  "group": "cloud-service",
  "tableOfContents": {"sections":[{"children":[{"id":"sign-up","title":"Sign up for Redis Cloud using AWS Marketplace"},{"id":"create-sub","title":"Create a database"}],"id":"sign-up-create-subscription","title":"Sign up and create a database"},{"id":"get-certs","title":"Enable TLS and get certificates"},{"id":"store-secret","title":"Store database credentials in AWS secrets manager"},{"children":[{"id":"redis-insight","title":"Redis Insight"},{"id":"redis-cli","title":"redis-cli"}],"id":"create-vector-index","title":"Create a vector index in your database"},{"id":"next-steps","title":"Next steps"}]}

,
  "codeExamples": []
}
```


You need to set up your Redis Cloud database before you can set it as the vector database in Amazon Bedrock. To do this, you need to:

1. [Sign up for Redis Cloud and create a database](#sign-up-create-subscription)
1. [Enable Transport Layer Security (TLS) for the database and save the certificates](#get-certs)
1. [Store database credentials in AWS secrets manager](#store-secret)
1. [Create a vector index in your database](#create-vector-index) for Bedrock to use

After you set up the database, you can use the database information to set it as your knowledge base database when you [create a knowledge base](https://redis.io/docs/latest/integrate/amazon-bedrock/create-knowledge-base).

## Sign up and create a database  {#sign-up-create-subscription}

To set up a Redis Cloud instance for Bedrock, you need to:

1. [Sign up for Redis Cloud](#sign-up) if you do not already have an account.
1. [Create a database](#create-sub) to use for your Bedrock knowledge base.

### Sign up for Redis Cloud using AWS Marketplace {#sign-up}

1.  Select the [Redis Cloud](https://aws.amazon.com/marketplace/pp/prodview-mwscixe4ujhkq?sr=0-1&ref_=beagle&applicationId=AWSMPContessa) AWS marketplace link from Bedrock to be taken to the Redis Cloud plan listing.

    ![The Redis Cloud listing on AWS Marketplace](https://redis.io/docs/latest/images/rc/aws-marketplace-rc-listing.png)

1.  Subscribe to Redis Cloud listing, locate the **Set Up Your Account** button, and then select it to begin mapping your Redis Cloud account with your AWS Marketplace account.

    ![Use the Set Up Your Account button after subscribing to Redis Cloud with your AWS Marketplace account.](https://redis.io/docs/latest/images/rc/aws-marketplace-account-setup-button.png)

1.  Sign in to the [Redis Cloud console](https://cloud.redis.io).

1.  Select the Redis account to be mapped to your AWS Marketplace account and confirm that your payment method will change and that the connection cannot be undone.

    ![Use the AWS Marketplace dialog to map your Redis Cloud account to your AWS Marketplace account.](https://redis.io/docs/latest/images/rc/aws-marketplace-map-account-dialog.png)

1.  Use the **Map account** button to confirm your choice.

1.  Once your Redis account is mapped to your AWS Marketplace account, a message appears in the upper, left corner of the account panel.

    ![The AWS Marketplace badge appears when your Redis Cloud account is mapped to an AWS Marketplace account.](https://redis.io/docs/latest/images/rc/aws-marketplace-billing-badge.png)

    In addition, AWS Marketplace is reported as the selected payment method.

### Create a database {#create-sub} 

1. In the [Redis Cloud console](https://cloud.redis.io/), select **New database**. 

    ![The New Database button creates a new database.](https://redis.io/docs/latest/images/rc/button-database-new.png)

1. When the **New database** page appears, select **Pro** to create a Pro plan.

    ![The Subscription selection panel with Pro selected.](https://redis.io/docs/latest/images/rc/create-database-subscription-pro-new.png)

1. After you select **Pro**, the **Database settings** section will appear. For this guide, continue with **Easy create** to get started faster.

    ![The database settings section.](https://redis.io/docs/latest/images/rc/create-pro-db-settings.png)

    If you'd like to select all of the configuration options yourself, select **Custom settings**. See [Create a Redis Cloud Pro database](https://redis.io/docs/latest/operate/rc/databases/create-database/create-pro-database-new#custom-settings) for more details.

1. Redis will generate a database name for you. If you want to change it, you can do so in the **Database name** field.

    ![The database name, cloud vendor and region settings.](https://redis.io/docs/latest/images/rc/pro-easy-create-vendor.png)

1. Select **Amazon Web Services** as the cloud vendor and select a region.

1. In the **Database Sizing** section:

    ![The Dataset size, throughput, and High availability settings.](https://redis.io/docs/latest/images/rc/pro-easy-create-size-throughput.png)
 
    - Select [**High availability**](https://redis.io/docs/latest/operate/rc/databases/configuration/high-availability) if it is not already selected.
    - Set the Dataset size of your database based on the amount of data that Bedrock will pull from your Simple Storage Service (S3) [bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-buckets-s3.html). See [Find out the size of your S3 buckets](https://aws.amazon.com/blogs/storage/find-out-the-size-of-your-amazon-s3-buckets/) to find out how much knowledge base data is stored in your S3 bucket and pick the closest size, rounded up, from the table below. 

        | Total Size of Documents in S3 | Database size without replication | Database size with replication |
|-------------------------------|-----------------------------------|--------------------------------|
| 10,000 kb                     | 135 Mb                             | 270 Mb                         |
| 100,000 kb                    | 1.35 Gb                            | 2.7 Gb                         |
| 1,000,000 kb                  | 13.5 Gb                              | 27 Gb                          |
| 10,000,000 kb                 | 135 Gb                             | 270 Gb                         |

        For more information on sizing, see the [Bedrock integration blog post](https://redis.io/blog/amazon-bedrock-integration-with-redis-enterprise/#right-size-your-database-for-amazon-bedrock).

1. Select **View all settings** to review the database settings that we selected for you.

    ![The optimal database settings.](https://redis.io/docs/latest/images/rc/pro-easy-create-optimal-settings.png)

    If you want to change these settings, select [**Switch to custom settings**](https://redis.io/docs/latest/operate/rc/databases/create-database/create-pro-database-new#custom-settings).

1. You will not need to enter a payment method, as it's automatically assigned to your AWS Marketplace account. Select **Confirm & pay** to create your new database.

    ![Select Confirm & pay to create your new database.](https://redis.io/docs/latest/images/rc/button-create-db-confirm-pay.png)

    Note that databases are created in the background.  While they are provisioning, you aren't allowed to make changes.  (The process generally takes 10-15 minutes.)

    Use the **Databases list** to check the status of your subscription.  You will also receive an email when your database is ready to use.

## Enable TLS and get certificates {#get-certs}

For your database to be fully secure, you must enable [Transport Layer Security (TLS)](https://redis.io/docs/latest/operate/rc/security/database-security/tls-ssl#enable-tls) for your database with client authentication.

1. Select **Databases** from the [Redis Cloud console](https://cloud.redis.io/) menu and then select your database from the list.

1. From the database's **Configuration** screen, select the **Edit** button:

    ![The Edit database button lets you change selected database properties.](https://redis.io/docs/latest/images/rc/button-database-edit.png)

1. In the **Security** section, use the **Transport layer security (TLS)** toggle to enable TLS:

    ![Use the Transport Layer Security toggle to enable TLS.](https://redis.io/docs/latest/images/rc/database-details-configuration-tab-security-tls-toggle.png)

1. Select **Download server certificate** to download the Redis Cloud certificate bundle `redis_ca.pem`:

    ![Use the Download server certificate button to download the Redis Cloud CA certificates.](https://redis.io/docs/latest/images/rc/button-database-config-security-server-ca-download.png)

1. Select the **Mutual TLS (require client authentication)** checkbox to require client authentication.

1. Select **Add client certificate** to add a certificate.

    ![The Add client certificate button.](https://redis.io/docs/latest/images/rc/mtls-add-client-certificate.png)

1. Either provide an [X.509 client certificate](https://en.wikipedia.org/wiki/X.509) or chain in PEM format for your client or select **Generate** to create one:

    ![Provide or generate a certificate for Mutual TLS.](https://redis.io/docs/latest/images/rc/database-details-configuration-tab-security-tls-client-auth-certificate.png)

    - If you generate your certificate from the Redis Cloud console, a **Download certificate** button will appear after it is generated. Select it to download the certificate. 

        ![The Download certificate button.](https://redis.io/docs/latest/images/rc/mtls-download-certificate.png)
        
        The download contains:

        - `redis-db-<database_id>.crt` – the certificate's public key.

        - `redis-db-<database_id>.key` – the certificate's private key.

        > [!NOTE]
        > You must download the certificate using the button at this point.  After your changes have been applied, the full bundle of public and private keys will no longer be available for download.
    
    - If you provide a client certificate, you will see the certificate details before you save your changes.

        ![The Download certificate button.](https://redis.io/docs/latest/images/rc/mtls-certificate-details.png)

1. To apply your changes and enable TLS, select the **Save database** button:

    ![Use the Save database button to save database changes.](https://redis.io/docs/latest/images/rc/button-database-save.png)

## Store database credentials in AWS secrets manager {#store-secret}

In the [AWS Management Console](https://console.aws.amazon.com/), use the **Services** menu to locate and select **Security, Identity, and Compliance** > **Secrets Manager**. [Create a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html) of type **Other type of secret** with the following key/value fields:

- `username`: Database username
- `password`: Database password
- `serverCertificate`: Contents of the [server certificate](https://redis.io/docs/latest/operate/rc/security/database-security/tls-ssl#download-certificates) (`redis_ca.pem`)
- `clientCertificate`: Contents of the client certificate (`redis_user.crt`)
- `clientPrivateKey`: Contents of the client private key (`redis_user_private.key`)

After you store this secret, you can view and copy the [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#iam-resources) of your secret on the secret details page. 

## Create a vector index in your database {#create-vector-index}

After your Redis Cloud database is set up, create a search index with a vector field using [FT.CREATE](https://redis.io/docs/latest/commands/ft.create) as your knowledge base for Amazon Bedrock. You can accomplish this using **Redis Insight** or `redis-cli`.

### Redis Insight

[Redis Insight](https://redis.io/docs/latest/develop/tools/insight) is a free Redis GUI that allows you to visualize and optimize your data in Redis. 

To create your vector index in Redis Insight:

1. [Download and install Redis Insight](https://redis.io/insight/) if you don't have it already.

1. In the [Redis Cloud console](https://cloud.redis.io/), in your database's **Configuration** tab, select the **Connect** button next to your database to open the connection wizard.

    ![Connect button.](https://redis.io/docs/latest/images/rc/button-connect.png#no-click)

1. In the connection wizard, under **Redis Insight Desktop**, select **Public Endpoint**. Select **Open with Redis Insight** to connect to the database with Redis Insight.

1. Select **Use TLS**. In the **CA Certificate** section, select **Add new CA certificate**. Give the certificate a name in the **Name** field, and enter the contents of `redis_ca.pem` into the **Certificate** field.

    ![The Redis Insight Add CA Certificate section.](https://redis.io/docs/latest/images/rc/ri-bedrock-add-ca-cert.png)

1. Select **Requires TLS Client Authentication**. In the **Client Certificate** section, select **Add new certificate**. Give the certificate a name in the **Name** field. Enter the contents of `redis_user.crt` into the **Certificate** field, and the contents of `redis_user_private.key` into the **Private Key** field.

    ![The Redis Insight Add Client Certificate section.](https://redis.io/docs/latest/images/rc/ri-bedrock-add-client-cert.png)

1. Select **Add Redis Database** to connect to the database.

1. Select your database alias to connect to your database. Select the **Workbench** icon to go to the workbench.

    ![The Redis Insight workbench icon.](https://redis.io/docs/latest/images/rc/ri-bedrock-workbench.png)

1. Enter the [FT.CREATE](https://redis.io/docs/latest/commands/ft.create) command to create an index. 

    ```text
    FT.CREATE <index_name>                    
        ON HASH                
        SCHEMA
            "<text_field>" TEXT
            "<metadata_field>" TEXT                   
            "<vector_field>"  VECTOR FLAT     
                6                          
                "TYPE" "FLOAT32"            
                "DIM" 1536                   
                "DISTANCE_METRIC" "COSINE"  
    ```

    Replace the following fields:

    - `<index_name>` with the vector index name
    - `<text_field>` with the text field name
    - `<metadata_field>` with the metadata field name
    - `<vector_field>` with the vector field name

1. Select **Run** to create the index.

    ![The Redis Insight run button.](https://redis.io/docs/latest/images/rc/ri-bedrock-run-button.png)

### `redis-cli`

The [`redis-cli`](https://redis.io/docs/latest/develop/tools/cli) command-line utility lets you connect and run Redis commands directly from the command line. To use `redis-cli`, you can [install Redis](https://redis.io/docs/latest/operate/rs/installing-upgrading/modules).

Public endpoint and port details are available from the **Databases** list or the database's **Configuration** screen. Select **Connect** to view how to connect to your database with `redis-cli`.

```sh
redis-cli -h <endpoint> -p <port> --tls --cacert redis_ca.pem \
    --cert redis_user.crt --key redis_user_private.key
```

After you are connected with `redis-cli`, create an index using [FT.CREATE](https://redis.io/docs/latest/commands/ft.create). 

```text
FT.CREATE <index_name>                    
    ON HASH                
    SCHEMA
        "<text_field>" TEXT
        "<metadata_field>" TEXT                   
        "<vector_field>"  VECTOR FLAT     
            6                          
            "TYPE" "FLOAT32"            
            "DIM" 1536                   
            "DISTANCE_METRIC" "COSINE"  
```

Replace the following fields:
- `<index_name>` with the vector index name
- `<text_field>` with the text field name
- `<metadata_field>` with the metadata field name
- `<vector_field>` with the vector field name

## Next steps

After your Redis database is set up, you can use it to [create a knowledge base](https://redis.io/docs/latest/integrate/amazon-bedrock/create-knowledge-base) in Amazon Bedrock.
