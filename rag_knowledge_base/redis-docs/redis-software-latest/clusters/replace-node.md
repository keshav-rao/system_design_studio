# Replace a cluster node

```json metadata
{
  "schema_version": 2,
  "title": "Replace a cluster node",
  "description": "Replace a node in your cluster that is down.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[]}

,
  "codeExamples": []
}
```

A failed node will appear as `Down` (![Node down icon](https://redis.io/docs/latest/images/rs/icons/node-down-icon.png#no-click)) in the **Nodes** list.

To replace a failed node: 

1. Prepare a new node identical to the old one.

1.  Install and
    configure Redis Software on the node. See [Install and setup](https://redis.io/docs/latest/operate/rs/installing-upgrading) for more information.

    > [!NOTE]
    > If you are using [Redis Flex or Auto Tiering](https://redis.io/docs/latest/operate/rs/databases/flash), make sure the required flash storage is set up on this new node.

1. [Add the node](https://redis.io/docs/latest/operate/rs/clusters/add-node) to the cluster. Make sure the new node has as much available memory as the faulty
    node.

    If the new node does not have enough memory, you will be prompted to add a node with enough memory.

1. A message will appear informing you that the cluster has a faulty node
    and that the new node will replace the faulty node.

    > [!NOTE]
    > - If there is a faulty node in the cluster to which you are adding a node, Redis Software will use the new node to replace the faulty one.
    > - Any existing [DNS records](https://redis.io/docs/latest/operate/rs/networking/cluster-dns) must be updated
    > each time a node is added or replaced.

