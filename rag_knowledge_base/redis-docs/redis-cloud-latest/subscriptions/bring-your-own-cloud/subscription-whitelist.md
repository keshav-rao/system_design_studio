# Configure subscription CIDR allow list

```json metadata
{
  "schema_version": 2,
  "title": "Configure subscription CIDR allow list",
  "description": "The CIDR allow list permits traffic between a range of IP addresses and the Redis Cloud VPC.",
  "categories": ["docs","operate","rc"],
  "tableOfContents": {"sections":[{"id":"allow-ip-address-or-security-group","title":"Allow IP address or security group"}]}

,
  "codeExamples": []
}
```


The [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) [allow list](https://en.wikipedia.org/wiki/Whitelist) lets you restrict traffic to your Redis Cloud database. When you configure an allow list, only the [IP addresses](https://en.wikipedia.org/wiki/IP_address) defined in the list can connect to the database. Traffic from all other IP addresses is blocked.

If you use [Redis Cloud Bring your Own Cloud](https://redis.io/docs/latest/operate/rc/subscriptions/bring-your-own-cloud) to host your Redis Cloud deployment, you can configure a subscription-wide allow list
to restrict traffic to all databases associated with the subscription.

The subscription CIDR allow list defines a range of IP addresses and [AWS security groups](https://docs.aws.amazon.com/managedservices/latest/userguide/about-security-groups.html) that control inbound and outbound traffic to the Redis Cloud [VPC](https://en.wikipedia.org/wiki/Virtual_private_cloud). When you add security groups to the allow list, you can also use the same security groups to manage access to your application.

> [!NOTE]
> The subscription-level allow list is available for Redis Cloud Bring your Own Cloud. If you don't have Redis Cloud Bring your Own Cloud, you can configure a [CIDR allow list](https://redis.io/docs/latest/operate/rc/security/cidr-whitelist) for each database.

## Allow IP address or security group

To add IP addresses or [AWS security groups](https://docs.aws.amazon.com/managedservices/latest/userguide/about-security-groups.html) to a subscription's allow list:

1. From the [Redis Cloud console](https://cloud.redis.io/) menu, select **Subscriptions** and then select your subscription from the list.

1. Select **Connectivity > Allow List**.

1. If the allow list is empty, select **Add allow list**.

    ![Use the Add allow list button to create an allow list.](https://redis.io/docs/latest/images/rc/button-subscription-allow-list-add.png)

1. Select an entry **Type** from the list:

    ![Select the type of entry to add to the allow list from the Type list. You can choose between IP address and AWS security group.](https://redis.io/docs/latest/images/rc/subscription-connectivity-allow-list-type-dropdown.png)

1. In the **Value** box, enter one of these options:

    - An IP address in CIDR format

    - The AWS security group ID

1. Select the check to add the entry to the allow list.

1. To allow additional IP addresses or security groups:

    1. Select **Add** to add a new entry.

    ![The Add button adds new entries to the allow list.](https://redis.io/docs/latest/images/rc/icon-add.png)

    1. Select the new entry's **Type**, enter the **Value**, and select the check to add it to the allow list.

        ![Define the new entry and select the Submit entry button to add it to the allow list.](https://redis.io/docs/latest/images/rc/subscription-connectivity-allow-list-add-entry.png)
    
    You can also select the **Edit** button to change an entry or the **Delete** button to remove it.

    ![The Edit button updates an entry in the allow list.](https://redis.io/docs/latest/images/rc/icon-edit.png#no-click)&nbsp;![The Delete button removes an entry from the allow list.](https://redis.io/docs/latest/images/rc/icon-delete-lb.png#no-click)
    
1. Select **Apply all changes** to apply the allow list updates.

    ![The Apply all changes button saves your allow list changes.](https://redis.io/docs/latest/images/rc/button-subscription-allow-list-apply-all.png)
