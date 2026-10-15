# Block public endpoints

```json metadata
{
  "schema_version": 2,
  "title": "Block public endpoints",
  "description": "Learn how to block the public endpoints of your databases.",
  "categories": ["docs","operate","rc"],
  "tableOfContents": {"sections":[{"children":[{"id":"new-subscription","title":"New subscription"},{"id":"existing-subscription","title":"Existing subscription"}],"id":"block-public-endpoints","title":"Block public endpoints"},{"id":"turn-on-passwordless-authentication-for-the-default-user","title":"Turn on passwordless authentication for the default user"},{"id":"private-connectivity-methods","title":"Private connectivity methods"}]}

,
  "codeExamples": []
}
```


By default, you can connect to Redis Cloud databases through the database's public endpoint, or through the database's private endpoint with a private connectivity method. 

Public endpoints are accessible from the public internet and don't require a private connectivity method. While this makes Redis Cloud databases convenient to use, it also exposes the databases to potential unauthorized access or brute force attacks, even with a database password in place. Some organizations may want to block public access to their databases to comply with security policies or to better meet stringent compliance standards.

Users with Redis Cloud Pro databases can choose to block public endpoints for all databases in their subscription.

> [!NOTE]
> After you block your database's public endpoint, any connection from an IP address that is not part of the private address space defined in [RFC 1918](https://datatracker.ietf.org/doc/html/rfc1918#section-3) will be rejected. Ensure that all connections to your database are made through a private connectivity method before blocking the public endpoint.

## Block public endpoints

You can block public endpoints for a [new subscription](#new-subscription) or an [existing subscription](#existing-subscription).

### New subscription

To block the public endpoints when you [create a new Pro subscription](https://redis.io/docs/latest/operate/rc/databases/create-database/create-pro-database-new):

1. Follow the instructions to [create a Pro database with custom settings](https://redis.io/docs/latest/operate/rc/databases/create-database/create-pro-database-new#custom-settings). 
1. On the **Setup** tab, go to **Advanced options > Security** to select persistent storage encryption options. 
1. Select **Block public endpoint** to block the public endpoint for all databases on the subscription. 
1. Select **Continue** to go to the [Sizing tab](https://redis.io/docs/latest/operate/rc/databases/create-database/create-pro-database-new#sizing-tab). Follow the instructions to provision your database(s).

After you block the public endpoints for a new subscription, you will need to set up a [private connectivity method](#private-connectivity-methods) to connect to your databases. 

### Existing subscription

For existing subscriptions, we recommend setting up a [private connectivity method](#private-connectivity-methods) to connect to your databases before blocking the private endpoint and migrating all connections to the private endpoint. 

To block the public endpoints of an existing Pro subscription:

1. From the [Redis Cloud console](https://cloud.redis.io/), select the **Subscriptions** menu and then select your subscription from the list. 
1. Open the **Security** tab to view security settings.
1. In the **Endpoint** section, select **Edit**.
1. Select **Block public endpoint**.
1. Select **Save** to save your changes.
1. A window will appear asking you to confirm that blocking the public endpoint will reject clients connecting to the public endpoint. Select **I understand** and then **Block** to confirm.

After your changes are saved, any incoming connections to the public endpoint of your database will be rejected, and only connections through a private connectivity method will be allowed.

## Turn on passwordless authentication for the default user

If you have blocked the public endpoint for your Redis Cloud Pro subscription, you can turn on passwordless authentication for the [default user](https://redis.io/docs/latest/operate/rc/security/access-control/data-access-control/default-user) for any database in that subscription.

To turn on passwordless authentication:

1. From the database **Configuration** tab, select **Edit**.
1. In the **Security** section, select **Use passwordless auth** to turn on passwordless authentication.

    ![Turn on passwordless authentication for the default user.](https://redis.io/docs/latest/images/rc/database-configuration-security-passwordless.png)

1. Select **Save database** to save your changes.

## Private connectivity methods

Redis Cloud supports the following private connectivity options:
- [VPC peering](https://redis.io/docs/latest/operate/rc/security/vpc-peering)
- [Google Cloud Private Service Connect](https://redis.io/docs/latest/operate/rc/security/private-service-connect) _(Google Cloud only)_
- [AWS Transit Gateway](https://redis.io/docs/latest/operate/rc/security/aws-transit-gateway) or [AWS PrivateLink](https://redis.io/docs/latest/operate/rc/security/aws-privatelink) _(AWS only)_
