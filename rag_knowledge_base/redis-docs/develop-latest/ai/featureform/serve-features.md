# Serve features

```json metadata
{
  "schema_version": 2,
  "title": "Serve features",
  "description": "Read materialized features from a Redis Feature Form feature view at inference time.",
  "categories": null,
  "tableOfContents": {"sections":[{"id":"verify-the-feature-view-exists","title":"Verify the feature view exists"},{"id":"minimal-python-workflow","title":"Minimal Python workflow"},{"id":"if-serving-fails","title":"If serving fails"}]}

,
  "codeExamples": []
}
```


Read materialized features from a feature view by calling `ff.Client.serve(...)`. This page assumes the feature view exists and the online store is ready — the [Quickstart](https://redis.io/docs/latest/develop/ai/featureform/quickstart)'s `demo_customer_feature_view` is the canonical example.

The examples use `<workspace-id>` as the workspace UUID. Get yours with `ff workspace list`. See [Manage workspaces](https://redis.io/docs/latest/develop/ai/featureform/manage-workspace) for the full workspace lifecycle.

## Verify the feature view exists

```bash
ff graph feature-view get demo_customer_feature_view --workspace <workspace-id>
```

## Minimal Python workflow

```python
import featureform as ff

client = ff.Client(host="127.0.0.1:9090", insecure=True, workspace="<workspace-id>")
features = client.serve("demo_customer_feature_view", entity="C1001")
print(features)
```

The example connects to a local server with TLS off. For a deployed server, change `host` and set `insecure=False`.

## If serving fails

- The feature view isn't ready. Confirm with `ff graph feature-view get` and re-check after materialization completes.
- The online provider is unavailable or not registered. Confirm with `ff provider list --workspace <workspace-id>`.
- The caller lacks the required RBAC permission. Serving values and reading serving metadata are governed by separate permissions; see the [Permissions table](https://redis.io/docs/latest/develop/ai/featureform/reference#permissions).

