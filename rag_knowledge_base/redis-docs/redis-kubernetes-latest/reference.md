# Reference

```json metadata
{
  "schema_version": 2,
  "title": "Reference",
  "description": "Resources to help you manage Redis Enterprise custom resources on Kubernetes.",
  "categories": ["docs","operate","kubernetes"],
  "tableOfContents": {"sections":[{"children":[{"id":"create-custom-resources","title":"Create custom resources"},{"id":"view-custom-resources","title":"View custom resources"},{"id":"modify-custom-resources","title":"Modify custom resources"}],"id":"work-with-custom-resources","title":"Work with custom resources"},{"children":[{"id":"example-categories","title":"Example categories"}],"id":"yaml-examples","title":"YAML examples"},{"children":[{"id":"core-resources","title":"Core resources"},{"id":"active-active-resources","title":"Active-Active resources"},{"id":"access-control-resources","title":"Access control resources"}],"id":"api-reference","title":"API reference"},{"id":"compatibility","title":"Compatibility"},{"id":"best-practices","title":"Best practices"}]}

,
  "codeExamples": []
}
```


This reference documentation covers Redis Enterprise custom resources, API specifications, and practical instructions for creating, configuring, and managing Redis Enterprise deployments on Kubernetes.

## Work with custom resources

Redis Enterprise for Kubernetes uses custom resources to manage clusters and databases. Use standard Kubernetes tools to create, modify, and delete these resources.

### Create custom resources

Use `kubectl apply` with YAML manifests to create custom resources:

```bash
kubectl apply -f my-redis-cluster.yaml
kubectl apply -f my-redis-database.yaml
```

### View custom resources

Use these commands to list and inspect existing custom resources:

```bash
# List Redis Enterprise clusters
kubectl get rec

# List Redis Enterprise databases
kubectl get redb

# List Active-Active databases
kubectl get reaadb

# List remote clusters
kubectl get rerc

# Get detailed information about a specific resource
kubectl describe rec my-cluster
kubectl describe redb my-database
```

### Modify custom resources

Edit the YAML manifest and reapply to update custom resources:

```bash
# Edit and apply updated manifest
kubectl apply -f updated-redis-cluster.yaml

# Or edit directly (not recommended for production)
kubectl edit rec my-cluster
kubectl edit redb my-database
```

## YAML examples

Find complete YAML examples for common deployment scenarios:

- [YAML examples](https://redis.io/docs/latest/operate/kubernetes/reference/yaml) - Ready-to-use YAML configurations for different deployment types

### Example categories

- [Basic deployment](https://redis.io/docs/latest/operate/kubernetes/reference/yaml/basic-deployment) - Essential YAML files for simple Redis Enterprise deployment
- [Rack awareness](https://redis.io/docs/latest/operate/kubernetes/reference/yaml/rack-awareness) - YAML examples for rack-aware deployments across availability zones
- [Active-Active](https://redis.io/docs/latest/operate/kubernetes/reference/yaml/active-active) - YAML examples for Active-Active databases across multiple clusters
- [Multi-namespace](https://redis.io/docs/latest/operate/kubernetes/reference/yaml/multi-namespace) - YAML examples for deploying across multiple namespaces

## API reference

Review complete API specifications for all Redis Enterprise custom resources:

### Core resources

- [Redis Enterprise cluster API (REC)](https://redis.io/docs/latest/operate/kubernetes/reference/api/redis_enterprise_cluster_api) - Manage Redis Enterprise clusters
- [Redis Enterprise database API (REDB)](https://redis.io/docs/latest/operate/kubernetes/reference/api/redis_enterprise_database_api) - Manage Redis databases

### Active-Active resources

- [Active-Active database API (REAADB)](https://redis.io/docs/latest/operate/kubernetes/reference/api/redis_enterprise_active_active_database_api) - Manage Active-Active databases
- [Remote cluster API (RERC)](https://redis.io/docs/latest/operate/kubernetes/reference/api/redis_enterprise_remote_cluster_api) - Configure remote cluster connections

### Access control resources

- [RedisEnterpriseUser API (REUSER)](https://redis.io/docs/latest/operate/kubernetes/reference/api/redis_enterprise_user_api) - Manage users for access control
- [RedisEnterpriseRole API (REROLE)](https://redis.io/docs/latest/operate/kubernetes/reference/api/redis_enterprise_role_api) - Define roles scoped to selected databases
- [RedisEnterpriseRoleBinding API (REROLEBINDING)](https://redis.io/docs/latest/operate/kubernetes/reference/api/redis_enterprise_role_binding_api) - Bind users to a scoped role
- [RedisEnterpriseClusterRole API (RECROLE)](https://redis.io/docs/latest/operate/kubernetes/reference/api/redis_enterprise_cluster_role_api) - Define cluster-scoped roles
- [RedisEnterpriseClusterRoleBinding API (RECROLEBINDING)](https://redis.io/docs/latest/operate/kubernetes/reference/api/redis_enterprise_cluster_role_binding_api) - Bind users to a cluster-scoped role
- [RedisEnterpriseACL API (REACL)](https://redis.io/docs/latest/operate/kubernetes/reference/api/redis_enterprise_acl_api) - Define access control lists

## Compatibility

Check supported Kubernetes distributions and versions:

- [Supported Kubernetes distributions](https://redis.io/docs/latest/operate/kubernetes/reference/supported_k8s_distributions) - Compatible Kubernetes platforms and versions

## Best practices

Follow these best practices when working with custom resources:

- **Use version control**: Store your YAML manifests in version control systems
- **Validate before applying**: Use `kubectl apply --dry-run=client` to validate changes
- **Monitor resource status**: Check resource status after you apply changes
- **Follow naming conventions**: Use consistent naming for easier management
- **Document configurations**: Add annotations and labels to describe resource purpose
