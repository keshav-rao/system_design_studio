# Add a node

```json metadata
{
  "schema_version": 2,
  "title": "Add a node",
  "description": "Add a node to your existing Redis Software cluster.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"id":"prerequisites","title":"Prerequisites"},{"id":"add-node","title":"Add node"},{"id":"verify-node","title":"Verify node"}]}

,
  "codeExamples": []
}
```

When you install Redis Software on the first node of a cluster, you create the new cluster.
After you install the first node, you can add more nodes to the cluster.

## Prerequisites

Before you add a node to the cluster:

- The clocks on all nodes must always be [synchronized](https://redis.io/docs/latest/operate/rs/clusters/configure/sync-clocks).

    If the clock in the node you are trying to join to the cluster is not synchronized with the nodes already in the cluster,
    the action fails and an error message is shown indicating that you must synchronize the clocks first.

- You must [update the DNS records](https://redis.io/docs/latest/operate/rs/networking/cluster-dns)
    each time a node is added or replaced.

- We recommend that you add nodes one after the other rather than in parallel
    to avoid errors that occur because the connection to the other nodes in the cluster cannot be verified.

## Add node

To add a node to an existing cluster:

1. [Install the Redis Software installation package](https://redis.io/docs/latest/operate/rs/installing-upgrading) on a clean installation
    of a [supported operating system](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/plan-deployment/supported-platforms).

1. To connect to the Cluster Manager UI of the new Redis Software installation, go to: <https://URL or IP address:8443>

    For example, if you installed Redis Software on a machine with IP address 10.0.1.34, go to `https://10.0.1.34:8443`.

    > [!TIP]
    > The management UI uses TLS encryption with a default certificate.
    > You can also [replace the TLS certificate](https://redis.io/docs/latest/operate/rs/security/certificates/updating-certificates)
    > with a custom certificate.

1. Select **Join cluster**.

1. For **Cluster identification**, enter the internal IP address or DNS name of a node that is a cluster member.

    If the node only has one IP address, enter that IP address.

1. For **Cluster sign in**, enter the credentials of the cluster administrator.

    The cluster administrator is the user account that you create when you configure the first node in the cluster.

1. Click **Next**.

1. Configure storage and network settings:

    1. Enter a path for [*Ephemeral storage*](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/plan-deployment/persistent-ephemeral-storage), or leave the default path.

    1. Enter a path for [*Persistent storage*](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/plan-deployment/persistent-ephemeral-storage),
        or leave the default path.

    1. To enable [*Redis Flex or Auto Tiering*](https://redis.io/docs/latest/operate/rs/databases/flash),
        select **Enable flash storage** and enter the path to the flash storage.

    1. If the cluster is configured to support [rack-zone awareness](https://redis.io/docs/latest/operate/rs/clusters/configure/rack-zone-awareness), set the **Rack-zone ID** for the new node.

    1. If your machine has multiple IP addresses, assign a single IPv4 type address for **Node-to-node communication (internal traffic)** and multiple IPv4/IPv6 type addresses for **External traffic**.

1. Select **Join cluster**.

The node is added to the cluster.
You can see it in the list of nodes in the cluster.

If you see an error when you add the node, try adding the node again.

## Verify node

We recommend that you verify the node is functioning properly using one of the following methods:

- Cluster Manager UI method:

    1. On the **Nodes** screen, click ![More actions button](https://redis.io/docs/latest/images/rs/buttons/button-toggle-actions-vertical.png#no-click) for the node you want to verify.
    
    1. Select **Verify node** from the list.

    ![Click the more actions button for a node to access node actions.](https://redis.io/docs/latest/images/rs/screenshots/nodes/secondary-nodes-more-actions.png)

- Command-line method:

    Run the [`rlcheck`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rlcheck) utility from the node's command line.

