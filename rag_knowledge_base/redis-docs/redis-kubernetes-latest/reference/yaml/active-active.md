# Active-Active examples

```json metadata
{
  "schema_version": 2,
  "title": "Active-Active examples",
  "description": "YAML examples for Active-Active Redis Enterprise databases across multiple Kubernetes clusters.",
  "categories": ["docs","operate","kubernetes"],
  "tableOfContents": {"sections":[{"id":"applying-the-configuration","title":"Applying the configuration"},{"id":"namespace-examples","title":"Namespace examples"},{"id":"rec-examples","title":"REC examples"},{"children":[{"id":"rerc-configuration","title":"RERC configuration"}],"id":"rerc-examples","title":"RERC examples"},{"children":[{"id":"reaadb-configuration","title":"REAADB configuration"}],"id":"active-active-database-examples","title":"Active-Active database examples"},{"id":"related-documentation","title":"Related documentation"}]}

,
  "codeExamples": []
}
```


This page provides YAML examples for deploying Active-Active Redis Enterprise databases across multiple Kubernetes clusters. Active-Active databases provide multi-master replication with conflict resolution, enabling global distribution and local read/write access.

For complete deployment instructions, see [Active-Active databases](https://redis.io/docs/latest/operate/kubernetes/active-active).

## Applying the configuration

To deploy Active-Active databases using these YAML files, follow [Create Active-Active database (REAADB)](https://redis.io/docs/latest/operate/kubernetes/active-active/create-reaadb), which provides detailed instructions for preparing clusters, creating RERC resources, and deploying REAADB configurations.

## Namespace examples

A namespace is an abstraction used by Kubernetes to support multiple virtual clusters on the same physical cluster.

`ns-illinois.yaml` is used in [Create Active-Active database](https://redis.io/docs/latest/operate/kubernetes/active-active/create-reaadb#example-values).



`ns-virginia.yaml` is used in [Create Active-Active database](https://redis.io/docs/latest/operate/kubernetes/active-active/create-reaadb#example-values).



## REC examples

A Redis Enterprise cluster is a collection of Redis Enterprise nodes that pools system resources across nodes and supports multi-tenant database instances.

`rec-chicago.yaml` is used in [Create Active-Active database](https://redis.io/docs/latest/operate/kubernetes/active-active/create-reaadb#prerequisites) and [Create RERC](https://redis.io/docs/latest/operate/kubernetes/active-active/create-reaadb#create-rerc).



`rec-arlington.yaml` is used in [Create Active-Active database](https://redis.io/docs/latest/operate/kubernetes/active-active/create-reaadb#prerequisites) and [Create RERC](https://redis.io/docs/latest/operate/kubernetes/active-active/create-reaadb#create-rerc).



## RERC examples

RedisEnterpriseRemoteCluster represents a remote participating cluster.

`rerc-ohare.yaml` is used in the [Create RERC](https://redis.io/docs/latest/operate/kubernetes/active-active/create-reaadb#create-rerc) section.



`rerc-raegan.yaml` is used in the [Create RERC](https://redis.io/docs/latest/operate/kubernetes/active-active/create-reaadb#create-rerc) section.



### RERC configuration

- [metadata.name](https://redis.io/docs/latest/operate/kubernetes/reference/api/redis_enterprise_remote_cluster_api#appredislabscomv1alpha1): Unique name for this remote cluster reference
- [spec.recName](https://redis.io/docs/latest/operate/kubernetes/reference/api/redis_enterprise_remote_cluster_api#spec): Name of the remote REC
- [spec.recNamespace](https://redis.io/docs/latest/operate/kubernetes/reference/api/redis_enterprise_remote_cluster_api#spec): Namespace of the remote REC
- [spec.apiFqdnUrl](https://redis.io/docs/latest/operate/kubernetes/reference/api/redis_enterprise_remote_cluster_api#spec): API endpoint URL for the remote cluster
- [spec.dbFqdnSuffix](https://redis.io/docs/latest/operate/kubernetes/reference/api/redis_enterprise_remote_cluster_api#spec): Database hostname suffix for the remote cluster
- [spec.secretName](https://redis.io/docs/latest/operate/kubernetes/reference/api/redis_enterprise_remote_cluster_api#spec): Secret containing authentication credentials

Edit the values in the downloaded YAML file for your specific setup, updating the remote cluster details, API endpoints, and secret names to match your actual environment.

## Active-Active database examples

Active-Active databases are geo-distributed databases that span multiple Redis Enterprise clusters and use multi-primary replication and conflict-free replicated data types (CRDTs).

`reaadb-boeing.yaml` is used in the [Create Active-Active database](https://redis.io/docs/latest/operate/kubernetes/active-active/create-reaadb#create-reaadb) section.



### REAADB configuration

- [metadata.name](https://redis.io/docs/latest/operate/kubernetes/reference/api/redis_enterprise_active_active_database_api#appredislabscomv1alpha1): Active-Active database name
- [spec.participatingClusters](https://redis.io/docs/latest/operate/kubernetes/reference/api/redis_enterprise_active_active_database_api#specparticipatingclusters): List of RERC names that participate in this database
- [spec.globalConfigurations](https://redis.io/docs/latest/operate/kubernetes/reference/api/redis_enterprise_active_active_database_api#specglobalconfigurations): Database settings applied to all participating clusters

Edit the downloaded YAML file to add global database settings such as memory allocation, shard count, replication settings, database secrets, Redis modules, and database-specific Redis configuration.

## Related documentation

- [Active-Active databases (index)](https://redis.io/docs/latest/operate/kubernetes/active-active)
- [Prepare participating clusters](https://redis.io/docs/latest/operate/kubernetes/active-active/prepare-clusters)
- [Create Active-Active database (REAADB)](https://redis.io/docs/latest/operate/kubernetes/active-active/create-reaadb)
- [Edit global configuration](https://redis.io/docs/latest/operate/kubernetes/active-active/global-config)
- [Sync global database secret](https://redis.io/docs/latest/operate/kubernetes/active-active/global-db-secret)
- [RERC API reference](https://redis.io/docs/latest/operate/kubernetes/reference/api/redis_enterprise_remote_cluster_api)
- [REAADB API reference](https://redis.io/docs/latest/operate/kubernetes/reference/api/redis_enterprise_active_active_database_api)
- [Networking configuration](https://redis.io/docs/latest/operate/kubernetes/networking)

