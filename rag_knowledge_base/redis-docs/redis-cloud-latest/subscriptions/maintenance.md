# Subscription and database maintenance

```json metadata
{
  "schema_version": 2,
  "title": "Subscription and database maintenance",
  "description": "Describes maintenance that Redis performs on a Redis Cloud subscription.",
  "categories": ["docs","operate","rc"],
  "tableOfContents": {"sections":[{"children":[{"id":"redis-cloud-pro","title":"Redis Cloud Pro"},{"id":"redis-cloud-essentials","title":"Redis Cloud Essentials"}],"id":"maintenance-windows","title":"Maintenance windows"},{"children":[{"id":"urgent-maintenance","title":"Urgent maintenance"},{"id":"major-upgrades","title":"Major upgrades"}],"id":"maintenance-activities","title":"Maintenance activities"},{"id":"notifications","title":"Notifications"}]}

,
  "codeExamples": []
}
```


Redis will maintain your Redis Cloud subscriptions and databases as needed to ensure your databases are running the most stable and up-to-date version of Redis.

## Maintenance windows

Maintenance windows define when Redis can perform maintenance on your subscriptions and databases. Maintenance window options depend on your subscription type.

### Redis Cloud Pro

For Redis Cloud Pro plans, Redis will perform maintenance automatically while limiting service disruption as much as possible. If you want to control when we can perform maintenance for a Redis Cloud Pro subscription, you can [set manual maintenance windows](https://redis.io/docs/latest/operate/rc/subscriptions/maintenance/set-maintenance-windows#set-manual-maintenance-windows).

### Redis Cloud Essentials

Redis Cloud Essentials databases have a set maintenance window based on the cloud provider region. The maintenance window for Redis Cloud Essentials databases is **daily from 12 AM to 6 AM** in the region's local time zone. We won't use more than one maintenance window per week unless we need to do [urgent maintenance](https://redis.io/docs/latest/operate/rc/subscriptions/maintenance#urgent-maintenance), and we won't perform any maintenance that introduces breaking changes during these maintenance windows.

## Maintenance activities

During maintenance, Redis ensures the stability of your subscriptions and databases. 

This includes, but is not limited to:

- Upgrading Redis or an advanced capability to the latest version
- Cluster optimization
- Replacing a cluster node
- Adding more memory to a node
- Applying security patches

Redis will notify users by email when maintenance starts and ends. For more details, see [Notifications](#notifications).

During maintenance, your database will be operational, but you may notice some latency when connecting to your databases.

Your application may also disconnect from your database for a few seconds. Most Redis clients are set to refresh their DNS address when they reconnect to the database, and you will not be required to perform any further action. If you encounter connectivity problems for more than a minute during maintenance, please refresh your DNS entries.

> [!TIP]
> To make sure your applications are set to reconnect after maintenance activity, see [Develop highly available and resilient apps with Redis Cloud](https://redis.io/docs/latest/operate/rc/resilient-apps).

### Urgent maintenance

Urgent maintenance refers to any activity that could affect service and cannot wait for scheduling. This includes applying urgent security patches.

Redis can perform urgent maintenance at any time, even if you have set a manual maintenance window or have temporarily [skipped maintenance](https://redis.io/docs/latest/operate/rc/subscriptions/maintenance/set-maintenance-windows#skip-maintenance-temporarily). Redis will notify you by email when urgent maintenance starts and ends.

### Major upgrades

We won't schedule major upgrades or upgrades that might include breaking changes until you opt-in to those changes. You can control your Redis major version on the [subscription page](https://redis.io/docs/latest/operate/rc/subscriptions/view-pro-subscription).

## Notifications

Redis will notify you by email when maintenance starts and ends. If Redis needs an action from you to start maintenance, we will notify you with a reasonable amount of time before planned maintenance.

If you want to receive advance maintenance notifications, you must [set manual maintenance windows](https://redis.io/docs/latest/operate/rc/subscriptions/maintenance/set-maintenance-windows#set-manual-maintenance-windows) and [contact support](https://redis.io/support/) to request advance maintenance notifications.

To receive maintenance notifications by email:
 
1. Go to [Access Management](https://redis.io/docs/latest/operate/rc/security/access-control/access-management) and select your account in the list.

1. Select the Edit button.

    ![Use the Edit button change details for a team member.](https://redis.io/docs/latest/images/rc/icon-edit.png)

1. Select **Operational emails** if it is not already turned on.

    ![Use the Edit User dialog to change the details for a user](https://redis.io/docs/latest/images/rc/access-mgmt-edit-user-dialog.png)

1. Select **Save user** to save your changes.
