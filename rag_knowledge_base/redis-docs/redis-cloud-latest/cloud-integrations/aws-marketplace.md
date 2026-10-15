# Sign up for Redis Cloud with AWS Marketplace

```json metadata
{
  "schema_version": 2,
  "title": "Sign up for Redis Cloud with AWS Marketplace",
  "description": "Shows how to subscribe to Redis Cloud using AWS Marketplace",
  "categories": ["docs","operate","rc"],
  "tableOfContents": {"sections":[{"id":"subscribe-to-redis-cloud-with-aws-marketplace","title":"Subscribe to Redis Cloud with AWS Marketplace"},{"id":"add-additional-redis-accounts-to-aws-marketplace","title":"Add additional Redis accounts to AWS Marketplace"},{"id":"switch-from-annual-to-pay-as-you-go","title":"Switch from Annual to Pay as You Go"},{"id":"disconnect-aws-marketplace-account","title":"Disconnect AWS Marketplace account"}]}

,
  "codeExamples": []
}
```


You can use AWS Marketplace to subscribe to Redis Cloud through AWS Marketplace.  This lets you provision according to your needs and pay using your AWS account.

## Subscribe to Redis Cloud with AWS Marketplace

Here's how to subscribe to Redis Cloud with AWS Marketplace:

1.  Sign in to the [AWS console](https://console.aws.amazon.com/).

1.  Search AWS Marketplace for [Redis Cloud: Real-Time Data Layer for AI Apps & Agents](https://aws.amazon.com/marketplace/pp/prodview-mwscixe4ujhkq) and subscribe to the listing.

    ![The Redis Cloud listing on AWS Marketplace](https://redis.io/docs/latest/images/rc/aws-marketplace-rc-listing.png)

    Or, click on the URL provided by your Redis seller for a private offer for [Redis Cloud - Annual Commits](https://aws.amazon.com/marketplace/pp/prodview-e6y7ork67pjwg?sr=0-3&ref_=beagle&applicationId=AWSMPContessa) and accept the private offer.

1.  Locate the **Set Up Your Account button**, and then select it to begin mapping your Redis Cloud account with your AWS Marketplace account.

    ![Use the Set Up Your Account button after subscribing to Redis Cloud with your AWS Marketplace account.](https://redis.io/docs/latest/images/rc/aws-marketplace-account-setup-button.png)

1.  Sign in to the [Redis Cloud console](https://cloud.redis.io). If you do not yet have an account, you will need to create one. You must have the **Account Owner** role.

1.  Select the Redis Cloud account(s) to be mapped to your AWS Marketplace account and confirm that your Marketplace account will pay for your Redis Cloud resources going forward.

    ![Use the AWS Marketplace dialog to map your Redis Cloud account to your AWS Marketplace account.](https://redis.io/docs/latest/images/rc/aws-marketplace-map-account-dialog.png)

1.  Use the **Connect account** button to confirm your choice.

    > [!NOTE]
    > You must complete this step to bill your Redis Cloud resources to your AWS Marketplace account.

1.  Once your Redis account is mapped to your AWS Marketplace account, your AWS Marketplace account will be charged for all your Redis Cloud resources going forward.

At this point, you can create a new database using the [standard workflow](https://redis.io/docs/latest/operate/rc/databases/create-database), with one important change. You don't need to enter a payment method, as it's automatically assigned to your AWS Marketplace account.

To confirm this, review the payment method associated with your subscription.

If your AWS Marketplace account is deactivated or otherwise unavailable, you won't be able to use your databases until the billing method is updated.  For help, [contact support](https://redis.io/support/).

## Add additional Redis accounts to AWS Marketplace

If you are the owner of more than one Redis Cloud account and have already associated your AWS marketplace account with one or more of your Redis accounts, you can add your AWS marketplace account to your other Redis Cloud accounts.

To do this:

1. In the [Redis Cloud console](https://cloud.redis.io/), sign in to the account you would like to associate with your marketplace account. 

1. Select **Billing & Payments > Payment Methods**.

1. Select **Add Marketplace account**.

    ![The Add marketplace account button.](https://redis.io/docs/latest/images/rc/add-marketplace-account.png)

1. Select the marketplace account you want to connect and confirm that it will pay for your Redis Cloud resources going forward.

1. Select **Connect account**.

    ![The Connect account button.](https://redis.io/docs/latest/images/rc/button-connect-account.png)

Your marketplace account is now connected to your Redis Cloud account. If you would like to disconnect your marketplace account from your Redis Cloud account, select **Disconnect**.

## Switch from Annual to Pay as You Go

If you have an Annual private offer and want to switch to a Pay as You Go subscription, you can do so by subscribing to the [Redis Cloud: Real-Time Data Layer for AI Apps & Agents](https://aws.amazon.com/marketplace/pp/prodview-mwscixe4ujhkq) listing. Both existing and future resources will continue to be billed under the Annual offer until it expires, after which they will be billed under the Pay as You Go offer.

## Disconnect AWS Marketplace account

See [Disconnect AWS Marketplace account](https://support.redislabs.com/hc/en-us/articles/29215779949074-Disconnect-Redis-Cloud-from-AWS-Marketplace) on the Redis knowledge base for help disconnecting your AWS Marketplace account from your Redis Cloud account.

