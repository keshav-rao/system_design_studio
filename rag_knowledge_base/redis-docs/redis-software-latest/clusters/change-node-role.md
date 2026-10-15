# Change node roles

```json metadata
{
  "schema_version": 2,
  "title": "Change node roles",
  "description": "Change node roles to demote the primary node to a secondary node or promote a secondary node to become the primary node.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"id":"demote-primary-node","title":"Demote primary node"},{"id":"promote-secondary-node","title":"Promote secondary node"}]}

,
  "codeExamples": []
}
```


A Redis Software cluster contains a primary node, which coordinates cluster-wide management operations, and multiple secondary nodes. Nodes with either role can host database shards.

## Demote primary node

**Cluster Manager UI:**

To demote the primary node to a secondary node using the Cluster Manager UI:

1. On the **Nodes** screen, click the **More actions** button (**&vellip;**) for the primary node you want to demote.

    ![Click the more actions button for a node to access node actions.](https://redis.io/docs/latest/images/rs/screenshots/nodes/primary-node-more-actions.png)

1. Select **Set as a secondary node** from the list.

1. Select one of the options to determine the new primary node:

    - **Automatically**: The cluster decides which node becomes the new primary node.

    - **Choose specific node**: You can manually select which node becomes the new primary node.

    ![The Set as a secondary node dialog has two options to select the new primary node, either automatically or manually.](https://redis.io/docs/latest/images/rs/screenshots/nodes/primary-node-set-as-secondary-dialog.png)

1. Click **Confirm**.

**rladmin:**

To demote the primary node to a secondary node using `rladmin`:

1. Identify the primary node's ID with [`rladmin cluster master`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/cluster/master):

    ```sh
    $ rladmin cluster master
    Node <primary-node-id> is the cluster master node
    ```

1. Run [`rladmin node enslave`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/node/enslave#node-enslave) with the `demote_node` option:

    ```sh
    rladmin node <primary-node-ID> enslave demote_node
    ```

    Replace `<primary-node-ID>` with the ID returned by `rladmin cluster master`.



## Promote secondary node

**Cluster Manager UI:**

To promote a secondary node to become the primary node using the Cluster Manager UI:

1. On the **Nodes** screen, click the **More actions** button (**&vellip;**) for the secondary node you want to promote.

    ![Click the more actions button for a node to access node actions.](https://redis.io/docs/latest/images/rs/screenshots/nodes/secondary-nodes-more-actions.png)

1. Select **Set as the primary node** from the list.

1. Click **Confirm**.

**rladmin:**

To promote a secondary node to become the primary node using `rladmin`:

1. To find the IDs of secondary nodes, run [`rladmin status nodes`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/status#status-nodes):

    ```sh
    $ rladmin status nodes
    CLUSTER NODES:
    NODE:ID     ROLE       ADDRESS          EXTERNAL_ADDRESS          HOSTNAME            SHARDS     CORES          FREE_RAM                 PROVISIONAL_RAM          VERSION        STATUS   
    node:1      master     198.51.100.2                                 3d99db1fdf4b        4/100      6              14.74GB/19.54GB          10.73GB/16.02GB          7.22.0-250     OK       
    *node:3     slave      198.51.100.4                                 b87cc06c830f        0/100      6              14.74GB/19.54GB          11.22GB/16.02GB          7.22.0-250     OK       
    node:2      slave      198.51.100.3                                 fc7a3d332458        0/100      6              14.74GB/19.54GB          11.22GB/16.02GB          7.22.0-250     OK       
    ```

    Nodes with the `slave` role are secondary nodes.

1. Run [`rladmin cluster master set`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/cluster/master):

    ```sh
    rladmin cluster master set <secondary-node-ID>
    ```

    Replace `<secondary-node-ID>` with the ID of the secondary node you want to promote.



After this node becomes the primary node, all cluster management traffic is directed to it.

