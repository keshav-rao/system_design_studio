# Multi-namespace examples

```json metadata
{
  "schema_version": 2,
  "title": "Multi-namespace examples",
  "description": "YAML examples for deploying Redis Enterprise across multiple Kubernetes namespaces.",
  "categories": ["docs","operate","kubernetes"],
  "tableOfContents": {"sections":[{"id":"operator-service-account","title":"Operator service account"},{"id":"operator-cluster-role","title":"Operator cluster role"},{"id":"operator-cluster-role-binding","title":"Operator cluster role binding"},{"id":"consumer-role","title":"Consumer role"},{"id":"consumer-role-binding","title":"Consumer role binding"},{"id":"next-steps","title":"Next steps"},{"id":"related-documentation","title":"Related documentation"}]}

,
  "codeExamples": []
}
```


Multi-namespace deployment lets a single Redis Enterprise operator manage clusters and databases in different namespaces, providing better resource isolation and organization.

Multi-namespace deployment enables:
- Namespace isolation: Separate Redis Enterprise resources by team, environment, or application
- Centralized management: Single operator manages multiple namespaces
- Resource sharing: Efficient use of cluster resources across namespaces
- Flexible RBAC: Fine-grained permissions per namespace

This example shows:
- Operator namespace: `redis-enterprise-operator` (where the operator and REC run)
- Consumer namespaces: `app-production`, `app-staging` (where REDB resources are created)

For complete deployment instructions, see [Manage databases in multiple namespaces](https://redis.io/docs/latest/operate/kubernetes/re-clusters/multi-namespace).

## Operator service account

Deploy these resources in the namespace where the Redis Enterprise operator runs.



## Operator cluster role

Grant the operator cluster-wide permissions to manage resources across namespaces.



## Operator cluster role binding



## Consumer role



## Consumer role binding



Consumer namespace configuration:

- `subjects.name`: Must match the operator service account name
- `subjects.namespace`: Must be the operator namespace, not the consumer namespace
- `roleRef.name`: Must match the consumer role name

## Next steps

- [Configure networking across namespaces](https://redis.io/docs/latest/operate/kubernetes/networking)
- [Set up monitoring for multi-namespace deployment](https://redis.io/docs/latest/operate/kubernetes/re-clusters/connect-prometheus-operator)
- [Learn about resource management](https://redis.io/docs/latest/operate/kubernetes/recommendations)

## Related documentation

- [Manage databases in multiple namespaces](https://redis.io/docs/latest/operate/kubernetes/re-clusters/multi-namespace)
- [RBAC configuration](https://redis.io/docs/latest/operate/kubernetes/security)
- [Kubernetes namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/)

