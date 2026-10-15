# Consolidated health report

```json metadata
{
  "schema_version": 2,
  "title": "Consolidated health report",
  "description": "View the consolidated health report to get a read-only snapshot of a Redis Software cluster's current system health.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"children":[{"id":"cluster-info","title":"Cluster info"},{"id":"cluster-storage","title":"Cluster storage"},{"id":"nodes","title":"Nodes"},{"id":"databases","title":"Databases"},{"id":"certificates","title":"Certificates"},{"id":"actions","title":"Actions"},{"id":"alerts-and-services","title":"Alerts and services"}],"id":"view-health-overview","title":"View health overview"},{"children":[{"id":"verify-nodes","title":"Verify nodes"},{"id":"node-storage","title":"Node storage"},{"id":"services","title":"Services"},{"id":"shards","title":"Shards"}],"id":"view-node-health","title":"View node health"},{"children":[{"id":"cluster-health-report-requests","title":"Cluster health report requests"},{"id":"database-health-report-requests","title":"Database health report requests"}],"id":"health-rest-api-requests","title":"Health report REST API requests"}]}

,
  "codeExamples": []
}
```


The consolidated health report is a read-only, consolidated snapshot of a cluster's current system health, including:

- License and certificate status

- Nodes and services health

- Node memory breakdown, including free and provisioned memory

- Running actions status

- Active alerts

- Basic database status and version

- High availability health

The consolidated health report consolidates cluster and database health information that was previously scattered across multiple APIs and CLI commands, such as [`rladmin status extra all`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/status) and required SSH access to view.

As of Redis Software version 8.0.16, you can access the cluster and database health reports using the [Cluster manager UI](#view-health-overview) or [REST API requests](#health-rest-api-requests).

## View health overview {#view-health-overview}

You can access the cluster and database health reports using the **Overview** screen in the Cluster Manager UI.

You can view node health

![The health report screen.](https://redis.io/docs/latest/images/rs/screenshots/overview/health-report-overview.png)

### Cluster info

The **Cluster Info** section provides basic cluster details, including:

- Overall cluster status

- Redis Software cluster version

- License usage and expiration date

### Cluster storage

The **Cluster Storage** section provides memory usage details, including used memory, free memory, and total memory for RAM, flash, persistent storage, and ephemeral storage on the cluster.

### Nodes

The **Nodes** section shows the status of nodes in the cluster and indicates which node is the leader or primary node.

### Databases

In the **Databases** section, you can check each database's status and Redis version. You can click the number listed by each field to display the relevant database names and click on the database links to view database details.

![Active database names and links are displayed.](https://redis.io/docs/latest/images/rs/screenshots/overview/db-status-hover.png)

### Certificates

The **Certificates** section shows whether the cluster's certificates are still valid. If a certificate appears as no longer valid, you can click the **Certificates** link to update the certificate.

![The certificates section shows an alert that the SSO service certificate expires soon.](https://redis.io/docs/latest/images/rs/screenshots/overview/cert-expires-soon.png)

### Actions

In the **Actions** section, you can view currently running actions.

![The Actions section shows a database upgrade is in progress.](https://redis.io/docs/latest/images/rs/screenshots/overview/running-actions.png)

### Alerts and services

If a configured alert threshold is reached or a running service stops, an alert will appear in the **Alerts & Services** section.

![Active alerts are displayed ephemeral and persistent storage have reached 90% capacity.](https://redis.io/docs/latest/images/rs/screenshots/overview/active-alerts.png)

## View node health {#view-node-health}

On the **Nodes** screen of the Cluster Manager UI, you can click on a node to go to its **Node configuration** tab and view node health details.

![Node configuration screen.](https://redis.io/docs/latest/images/rs/screenshots/nodes/node-config-screen.png)

### Verify nodes

You can check if nodes are functioning properly using one of the following methods:

**Verify all nodes:**

On the **Nodes** screen, click **Verify all nodes**.

**Verify specific node:**

1. On the **Nodes** screen, find the node you want verify in the list and click the **More actions** button (**&vellip;**).
    
1. Select **Verify node** from the list.

![Click the more actions button for a node to access node actions.](https://redis.io/docs/latest/images/rs/screenshots/nodes/primary-node-more-actions-8-0.png)



### Node storage

The **Node storage** section of the **Node configuration** tab provides memory usage details, including used memory, free memory, and total memory for RAM, flash, persistent storage, and ephemeral storage on the node.

### Services

In the **Services** section **Node configuration** tab, you can view the list of services running on the node and the most recent status of each.

![The services section shows most services running and one stopped service.](https://redis.io/docs/latest/images/rs/screenshots/nodes/node-stopped-service.png)

### Shards

When viewing a node's configuration, you can click the **Shards** tab to view a list of database shards running on the node and related details such as each shard's ID, current status, role, and slot range.

![A list of database shards on the node.](https://redis.io/docs/latest/images/rs/screenshots/nodes/node-shards.png)

## Health report REST API requests {#health-rest-api-requests}

### Cluster health report requests

[Cluster health report](https://redis.io/docs/latest/operate/rs/references/rest-api/api-reference#tag/Cluster/operation/cluster_cluster_health_report) REST API requests provide overall health information for a cluster:

```sh
GET https://<host>:<port>/v4/cluster/health
```

### Database health report requests

[Database health report](https://redis.io/docs/latest/operate/rs/references/rest-api/api-reference#tag/Database/operation/cluster_database_health_report) REST API requests provide detailed health information for a specific database:

```sh
GET https://<host>:<port>/v4/bdb/<database_id>/health
```

