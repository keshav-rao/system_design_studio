# API reference

```json metadata
{
  "schema_version": 2,
  "title": "API reference",
  "description": "Reference documentation for Redis Enterprise operator APIs",
  "categories": ["docs","operate","kubernetes"],
  "tableOfContents": {"sections":[{"id":"api-versions-and-stability","title":"API versions and stability"},{"id":"custom-resources","title":"Custom resources"},{"children":[{"id":"using-kubectl","title":"Using kubectl"},{"id":"resource-relationships","title":"Resource relationships"}],"id":"working-with-the-apis","title":"Working with the APIs"}]}

,
  "codeExamples": []
}
```


The Redis Enterprise operator provides Kubernetes custom resource definitions (CRDs) that let you manage Redis Enterprise clusters and databases declaratively. This section contains the complete API reference for all operator resources.

## API versions and stability

The operator uses different API versions to indicate stability and feature maturity:

- **`app.redislabs.com/v1`** - Stable APIs for production use
- **`app.redislabs.com/v1alpha1`** - Alpha APIs that may change in future releases

## Custom resources

| Resource | API Version | Purpose |
|----------|-------------|---------|
| [RedisEnterpriseCluster (REC)](redis_enterprise_cluster_api) | `v1` | Manages Redis Enterprise cluster deployments |
| [RedisEnterpriseDatabase (REDB)](redis_enterprise_database_api) | `v1alpha1` | Creates and configures Redis databases |
| [RedisEnterpriseActiveActiveDatabase (REAADB)](redis_enterprise_active_active_database_api) | `v1alpha1` | Sets up active-active databases across clusters |
| [RedisEnterpriseRemoteCluster (RERC)](redis_enterprise_remote_cluster_api) | `v1alpha1` | Defines remote cluster connections for active-active |
| [RedisEnterpriseUser (REUSER)](redis_enterprise_user_api) | `v1alpha1` | Defines users for cluster access control |
| [RedisEnterpriseRole (REROLE)](redis_enterprise_role_api) | `v1alpha1` | Defines a role scoped to selected databases |
| [RedisEnterpriseRoleBinding (REROLEBINDING)](redis_enterprise_role_binding_api) | `v1alpha1` | Binds users to a RedisEnterpriseRole |
| [RedisEnterpriseClusterRole (RECROLE)](redis_enterprise_cluster_role_api) | `v1alpha1` | Defines a cluster-scoped role |
| [RedisEnterpriseClusterRoleBinding (RECROLEBINDING)](redis_enterprise_cluster_role_binding_api) | `v1alpha1` | Binds users to a RedisEnterpriseClusterRole |
| [RedisEnterpriseACL (REACL)](redis_enterprise_acl_api) | `v1alpha1` | Defines an access control list (ACL) for a database |

## Working with the APIs

### Using kubectl

Manage all resources using standard `kubectl` commands:

```bash
# List all Redis Enterprise clusters
kubectl get rec

# Get detailed information about a specific database
kubectl describe redb my-database

# Apply a configuration from a YAML file
kubectl apply -f my-redis-config.yaml
```

### Resource relationships

- Create a `RedisEnterpriseCluster` (REC) first to provide the Redis Enterprise infrastructure
- Create `RedisEnterpriseDatabase` (REDB) resources within a cluster to provision individual databases
- Use `RedisEnterpriseActiveActiveDatabase` (REAADB) with `RedisEnterpriseRemoteCluster (RERC)` resources to define participating clusters

For complete YAML configuration examples, see the [YAML examples](https://redis.io/docs/latest/operate/kubernetes/reference/yaml) section.

