# View and Upgrade Redis Cloud Essentials plan

```json metadata
{
  "schema_version": 2,
  "title": "View and Upgrade Redis Cloud Essentials plan",
  "description": "",
  "categories": ["docs","operate","rc"],
  "tableOfContents": {"sections":[{"children":[{"id":"change-high-availability-and-persistence","title":"Change high availability and persistence"},{"id":"change-subscription-plan","title":"Change subscription plan"},{"id":"change-payment-method","title":"Change payment method"},{"id":"save-changes","title":"Save changes"}],"id":"upgrade-plan","title":"Upgrade plan"},{"id":"subscription-overview","title":"Subscription overview"}]}

,
  "codeExamples": []
}
```

To view the details of a Redis Cloud Essentials subscription:

1.  Sign in to the [Redis Cloud console](https://cloud.redis.io/) and select the **Subscriptions** list.

1.  Select the target subscription from the subscription list.

    ![The Subscription list shows your current subscriptions.](https://redis.io/docs/latest/images/rc/subscription-list-select.png)

1.  Your subscription details appear, along with a summary of your database details.

    ![The Databases tab of the subscription details page is the default view.](https://redis.io/docs/latest/images/rc/subscription-details-fixed-databases-tab.png)

From here, you can:

- Select the **Plan upgrade** button to update your subscription plan, high availability settings, or payment method.

    ![Select the Upgrade plan button to update your subscription settings.](https://redis.io/docs/latest/images/rc/button-subscription-upgrade-plan.png)

- Select the **Overview** tab to view and edit subscription details.

The following sections provide more details.

## Upgrade plan

Use the **Plan upgrade** button to update your Redis Cloud Essentials plan, your high availability settings, or your payment method. Upgrading your database between Redis Cloud Essentials plans does not impact database availability during the update.

![Use the Plan upgrade button to change selected Redis Cloud Essentials subscription detils.](https://redis.io/docs/latest/images/rc/button-subscription-upgrade-plan.png)

For information on how to upgrade to Redis Cloud Pro, see [upgrade subscription plan from Essentials to Pro](https://redis.io/docs/latest/operate/rc/subscriptions/upgrade-essentials-pro).

### Change high availability and persistence

To change your plan's [high availability](https://redis.io/docs/latest/operate/rc/databases/configuration/high-availability) and [data persistence](https://redis.io/docs/latest/operate/rc/databases/configuration/data-persistence) settings, change them in the **Configure your settings** panel.

![Use the Configure your settings panel to set Essentials subscription settings.](https://redis.io/docs/latest/images/rc/subscription-fixed-high-availability-panel.png)

You can switch between **No replication** and **Single-zone replication** at any time, but you cannot choose **Multi-zone replication** after your subscription is created. You also cannot switch from **Multi-zone replication** to another high availability option.

### Change subscription plan

To change your subscription plan, select the desired plan from the list and select the **Upgrade plan** button:

![Select the desired subscription plan from the ones shown.](https://redis.io/docs/latest/images/rc/subscription-change-fixed-tiers.png)

Each Redis Cloud Essentials plan provides a variety of benefits, including increased memory and number of connections.
For a comparison of available plans, see [Redis Cloud Essentials plans](https://redis.io/docs/latest/operate/rc/subscriptions/view-essentials-subscription/essentials-plan-details).

When you change your plan, your data and endpoints are not disrupted.  

If you upgrade a free plan to a paid plan, you need to add a payment method.

If you change your subscription to a lower plan, make sure your data fits within the limits of the new plan; otherwise, the change attempt will fail.

> [!NOTE]
> As of January 2024, new and upgraded Redis Cloud Essentials subscriptions are limited to one database per subscription. If you have a Redis Cloud Essentials subscription created before January 2024, you can add databases up to the previous plan limit. If you choose to upgrade your plan, you can keep your databases, but you will need to create a new subscription to add another database.

### Change payment method

To change your subscription payment method, update the **Payment method** settings.  You can select a known payment method from the drop-down list or use the **Add** button to add a new one.

![Use the Credit card drop-down to set your subscription payment method.](https://redis.io/docs/latest/images/rc/subscription-change-credit-card.png)

Payment method changes require the Owner or Billing Admin roles. To verify your role, select **Access Management** from the admin menu and then locate your credentials in the **Team** tab.

### Save changes

Use the **Update Database** button to save changes.

![Use the Upgrade plan button to save your subscription plan changes.](https://redis.io/docs/latest/images/rc/button-subscription-upgrade-plan-blue.png)

## Subscription overview

The **Overview** tab summarizes your Redis Cloud Essentials subscription details using a series of panels:

![The Overview tab displays the details of your Fixed subscription.](https://redis.io/docs/latest/images/rc/subscription-details-fixed-overview-tab.png)

The following details are displayed:

| Detail | Description |
|:---------|:--------------|
| **Subscription description** | Brief summary of subscription, including the plan type, cloud provider, region, and data size limit |
| **Cloud vendor** | Your database's cloud vendor |
| **Availability** | Describes high availability settings |
| **Region** | The region your subscription is deployed to |
| **Plan** | The maximum database size of your Essentials plan. Also displays the cost for paid plans. |
| **Databases** | Maximum number of databases for your plan |
| **Connections** | Maximum number of concurrent connections |
| **CIDR allow rules** | Maximum number of authorization rules |
| **Data persistence** | Indicates whether persistence is supported for your subscription |
| **Daily & instant backups** | Indicates whether backups are supported for your subscription |
| **Replication** | Indicates whether replication is supported for your subscription |
| **Clustering** | Indicates whether clustering is supported for your subscription |

The **Delete Database** button lets you [delete your database](https://redis.io/docs/latest/operate/rc/databases/delete-database).

![Use the Delete subscription button to delete your subscription plan.](https://redis.io/docs/latest/images/rc/button-delete-database-essentials-overview.png)

