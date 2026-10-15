# Upgrade a Redis Software cluster

```json metadata
{
  "schema_version": 2,
  "title": "Upgrade a Redis Software cluster",
  "description": "Upgrade a cluster to a later version of Redis Software.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"id":"supported-upgrade-paths","title":"Supported upgrade paths"},{"id":"upgrade-prerequisites","title":"Upgrade prerequisites"},{"id":"in-place-upgrade","title":"In-place upgrade"},{"children":[{"id":"extra-node-upgrade","title":"Extra node upgrade method"},{"id":"replace-node-upgrade","title":"Replace node upgrade method"}],"id":"rolling-upgrade","title":"Rolling upgrade"},{"id":"after-cluster-upgrade","title":"After cluster upgrade"}]}

,
  "codeExamples": []
}
```


Before you upgrade a cluster to a later Redis Software version, review the [supported upgrade paths](#supported-upgrade-paths) and [prerequisites](#upgrade-prerequisites).

To upgrade a cluster's Redis Software version, use one of the following methods:

- [In-place upgrade](#in-place-upgrade) - Directly upgrade Redis Software on each node in the cluster. Although this method is simpler than the rolling upgrade method, it might cause brief service interruptions as each node is upgraded.

- [Rolling upgrade](#rolling-upgrade) - Minimize downtime by adding new nodes with an updated Redis Software version to the cluster, one at a time, while keeping the rest of the cluster operational. This method is recommended for production environments that require continuous availability.

## Supported upgrade paths

<span title="Check mark icon">&#x2705;</span> Supported – You can upgrade directly from the current Redis Software cluster version.

<span title="X icon">:x:</span> Not supported – You cannot upgrade directly from the current Redis Software cluster version. You must first upgrade to a supported intermediate version.

| Current Redis Software cluster version | Upgrade to Redis Software 7.2.x | Upgrade to Redis Software 7.4.x |  Upgrade to Redis Software 7.8.x | Upgrade to Redis Software 7.22.x | Upgrade to Redis Software 8.0.2-8.0.10 | Upgrade to Redis Software 8.0.16-8.0.20 | Upgrade to Redis Software 8.2.x |
|:-----------------------:|:----------------:|:----------------:|:----------------:|:----------------:|:----------------:|:----------------:|:----------------:|
| 6.0.x | <span title="Supported">&#x2705;</span> | <span title="Not supported">:x:</span> | <span title="Not supported">:x:</span> | <span title="Not supported">:x:</span> | <span title="Not supported">:x:</span> | <span title="Not supported">:x:</span> | <span title="Not supported">:x:</span> |
| 6.2.4<br />6.2.8 | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Not supported">:x:</span> | <span title="Not supported">:x:</span> | <span title="Not supported">:x:</span> | <span title="Not supported">:x:</span> | <span title="Not supported">:x:</span> |
| 6.2.10<br />6.2.12<br />6.2.18 | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Not supported">:x:</span> | <span title="Not supported">:x:</span> | <span title="Not supported">:x:</span> | <span title="Not supported">:x:</span> |
| 6.4.x | <span title="Supported">&#x2705;</span> |  <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Not supported">:x:</span> | <span title="Not supported">:x:</span> |
| 7.2.x | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| 7.4.x | – | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| 7.8.x | – | – | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| 7.22.x | – | – | – | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| 8.0.2<br />8.0.6<br />8.0.10 | – | – | – | – | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| 8.0.16<br />8.0.18<br />8.0.20 | – | – | – | – | - | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| 8.2.x | – | – | – | – | – | – | <span title="Supported">&#x2705;</span> |


See the [Redis Software product lifecycle](https://redis.io/docs/latest/operate/rs/installing-upgrading/product-lifecycle) for more information about release numbers and the end-of-life schedule.

> [!NOTE]
> Redis Enterprise for Kubernetes has its own support lifecycle, which accounts for the Kubernetes distribution lifecycle. For details, see [Supported Kubernetes distributions](https://redis.io/docs/latest/operate/kubernetes/reference/supported_k8s_distributions).

## Upgrade prerequisites

Before upgrading a cluster:

- Verify access to [rlcheck](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rlcheck) and [rladmin](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin#use-the-rladmin-shell) commands.

- Run [rlcheck](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rlcheck) on each node and verify there are no issues:

    ```sh
    rlcheck
    ```

- Verify [maintenance mode](https://redis.io/docs/latest/operate/rs/clusters/maintenance-mode) is not enabled:

    1. On a node in the cluster, run [`rladmin status`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/status):
    
        ```sh
        rladmin status
        ``` 
        
    1. Review each node's `SHARDS` field. If the value is yellow, the node is in maintenance mode.

        ![](https://redis.io/docs/latest/images/rs/maintenance_mode.png)

    1. To deactivate maintenance mode on a node, run the following [`rladmin node maintenance_mode off`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/node/maintenance-mode#node-maintenance_mode-off) command. See [Deactivate maintenance mode](https://redis.io/docs/latest/operate/rs/clusters/maintenance-mode#deactivate-maintenance-mode) for additional details.

        ```sh
        rladmin node <node_id> maintenance_mode off
        ```

- Verify that you meet the upgrade path requirements for the target cluster version and review the relevant [release notes](https://redis.io/docs/latest/operate/rs/release-notes) for any preparation instructions.

- Before you upgrade a cluster from Redis Software version 6.2.x to 7.8.x, you must follow these steps if the cluster has any databases with Redis version 6.0:

    1. Set the Redis upgrade policy to `latest`:

        ```sh
        rladmin tune cluster redis_upgrade_policy latest
        ```

    1. [Upgrade Redis 6.0 databases](https://redis.io/docs/latest/operate/rs/installing-upgrading/upgrading/upgrade-database) to Redis 6.2.

- [Upgrade your databases](https://redis.io/docs/latest/operate/rs/installing-upgrading/upgrading/upgrade-database) to a version that is supported by the target Redis Software version before upgrading the cluster. We recommend you upgrade the databases to the latest supported version if possible. Make sure to test the upgrade in a non-production environment to determine any impact.

- Avoid changing the database configuration or performing other cluster management operations during the cluster upgrade process, as this might cause unexpected results.

- Upgrade the cluster's primary (master) node first. To identify the primary node, use one of the following methods:

    - **Nodes** screen in the new Cluster Manager UI (only available for Redis Software versions 7.2 and later)

    - [`rladmin status nodes`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/status#status-nodes) command
    
    - [`GET /nodes/status`](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/nodes/status#get-all-nodes-status) REST API request

## In-place upgrade

Starting with the primary node, follow these steps for every node in the cluster. To ensure cluster availability, upgrade each node separately.

1. Complete all [prerequisites](#upgrade-prerequisites) before starting the upgrade.

1.  Verify node operation with the following commands:

    ``` shell
    $ rlcheck
    $ rladmin status extra all
    ```

    > [!WARNING]
    > Do not proceed if any shard, node, or endpoint is not `OK`.

1.  Download the Redis Software installation package to the machine running the node from the Download Center on [https://cloud.redis.io](https://cloud.redis.io).  

1.  Extract the installation package:

    ```sh
    tar vxf <tarfile name>
    ```

    > [!NOTE]
    > You cannot change the installation path or the user during the upgrade.

1.  Run the install command. See [installation script options](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/install-script) for a list of command-line options you can add to the following command. You cannot use options marked as "new installs only" during an in-place upgrade.

    ``` shell
    sudo ./install.sh
    ```

    The installation script automatically recognizes the upgrade and responds accordingly.

    The upgrade replaces all node processes, which might briefly interrupt any active connections.

1.  Verify the node was upgraded to the new version and is still operational:

    ``` shell
    $ rlcheck
    $ rladmin status extra all
    ```

1.  Visit the Cluster Manager UI.

    If the Cluster Manager UI was open in a web browser during the upgrade, refresh the browser to reload the console.

## Rolling upgrade

To perform a rolling upgrade of the cluster, use one of the following methods:

- [Extra node method](#extra-node-upgrade) - recommended if you have additional resources available

- [Replace node method](#replace-node-upgrade) - recommended if you cannot temporarily allocate additional resources

### Extra node upgrade method {#extra-node-upgrade}

1. Complete all [prerequisites](#upgrade-prerequisites) before starting the rolling upgrade.

1. [Install a later version of Redis Software](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/install-on-linux) on a new node.

1. [Add the new node](https://redis.io/docs/latest/operate/rs/clusters/add-node) to the cluster.

1. If the [cluster uses DNS](https://redis.io/docs/latest/operate/rs/networking/cluster-dns), add the new node’s IP address to the DNS records.

1. [Promote the first new node](https://redis.io/docs/latest/operate/rs/clusters/change-node-role#promote-secondary-node) to become the primary node.

1. [Remove one node](https://redis.io/docs/latest/operate/rs/clusters/remove-node#remove-a-node) running the earlier Redis Software version from the cluster.

1. Repeat the previous steps until all nodes with the earlier Redis Software version are removed. If the final node to remove from the cluster is the primary node, [demote it](https://redis.io/docs/latest/operate/rs/clusters/change-node-role#demote-primary-node) to a secondary node before you remove it.

### Replace node upgrade method {#replace-node-upgrade}

1. Complete all [prerequisites](#upgrade-prerequisites) before starting the rolling upgrade.

1. [Remove a node](https://redis.io/docs/latest/operate/rs/clusters/remove-node#remove-a-node) with the earlier Redis Software version from the cluster.

1. Uninstall Redis Software from the removed node:

    ```sh
    sudo ./rl_uninstall.sh
    ```

1. [Install a later version of Redis Software](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/install-on-linux) on the removed node or a new node.

1. [Add the new node](https://redis.io/docs/latest/operate/rs/clusters/add-node) to the cluster.

    If you want to reuse the removed node's ID when you add the node to the cluster, run [`rladmin cluster join`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/cluster/join) with the `replace_node` flag:

    ```sh
    rladmin cluster join nodes <cluster_member_ip_address> username <username> password <password> replace_node <node_id>
    ```

1. If the [cluster uses DNS](https://redis.io/docs/latest/operate/rs/networking/cluster-dns), add the new node’s IP address to the DNS records.

1. [Promote the first new node](https://redis.io/docs/latest/operate/rs/clusters/change-node-role#promote-secondary-node) to become the primary node.

1. Verify node health:

    1. Run `rlcheck` on all nodes:

        ```sh
        rlcheck
        ```

        The output lists the result of each verification test:

        ```sh
        ##### Welcome to Redis Software Cluster settings verification utility ####
        Running test: verify_bootstrap_status
		                PASS
        ...
        Running test: verify_encrypted_gossip
		                PASS
        Summary:
        -------
        ALL TESTS PASSED.
        ```

        For healthy nodes, the expected output is `ALL TESTS PASSED`.

    1. Run [`rladmin status`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/status) on the new node:

        ```sh
        rladmin status extra all
        ```

        The expected output is the `OK` status for the cluster, nodes, endpoints, and shards:

        ```sh
        CLUSTER:
        OK. Cluster master: 2 (<IP.address>)
        Cluster health: OK, [0, 0.0, 0.0]
        failures/minute - avg1 0.00, avg15 0.00, avg60 0.00.
        ...
        ```

1. Repeat the previous steps until all nodes with the earlier Redis Software version are replaced. If the final node to remove from the cluster is the primary node, [demote it](https://redis.io/docs/latest/operate/rs/clusters/change-node-role#demote-primary-node) to a secondary node before you remove it.

## After cluster upgrade

After all nodes are upgraded, the cluster is fully upgraded. Certain features introduced in the new version of Redis Software only become available after upgrading the entire cluster.

```sh
supervisorctl restart cnm_exec
```

