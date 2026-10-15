# Alerts

```json metadata
{
  "schema_version": 2,
  "title": "Alerts",
  "description": "Documents the alerts that are tracked with Redis Software.",
  "categories": ["docs","operate","rs","rc"],
  "tableOfContents": {"sections":[{"id":"cluster-alerts","title":"Cluster alerts"},{"id":"database-alerts","title":"Database alerts"},{"id":"send-alerts-by-email","title":"Send alerts by email"}]}

,
  "codeExamples": []
}
```


Cluster alerts are triggered based on thresholds applied to these stored metrics.

## Cluster alerts

In **Cluster > Alert Settings**, you can enable alerts for node or cluster events, such as high memory usage or throughput.

Configured alerts are shown:

- As a notification on the status icon (  ) for the node and cluster
- In the **log**
- In email notifications, if you configure [email alerts](#send-alerts-by-email)

> [!NOTE]
> If you enable alerts for "Node joined" or "Node removed" actions,
> you must also enable "Receive email alerts" so that the notifications are sent.

To enable alerts for a cluster:

1. In **Cluster > Alert Settings**, click **Edit**. 
1. Select the alerts that you want to show for the cluster and click **Save**.

## Database alerts

For each database, you can enable alerts for database events, such as high memory usage or throughput.

Configured alerts are shown:

- As a notification on the status icon (  ) for the database
- In the **log**
- In emails, if you configure [email alerts](#send-alerts-by-email)

To enable alerts for a database:

1. In **Configuration** for the database, click **Edit**.
1. Select the **Alerts** section to open it.
1. Select the alerts that you want to show for the database and click **Save**.

## Send alerts by email

To send cluster and database alerts by email:

1. In **Cluster > Alert Settings**, click **Edit**.
1. Select **Set an email** to configure the [email server settings](https://redis.io/docs/latest/operate/rs/clusters/configure/cluster-settings#configure-email-server-settings).
1. In **Configuration** for the database, click **Edit**.
1. Select the **Alerts** section to open it.
1. Select **Receive email alerts** and click **Save**.
1. In **Access Control**, select the [database and cluster alerts](https://redis.io/docs/latest/operate/rs/security/access-control/create-users#add-users) that you want each user to receive.

