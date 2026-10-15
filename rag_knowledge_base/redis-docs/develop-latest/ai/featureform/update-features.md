# Update features

```json metadata
{
  "schema_version": 2,
  "title": "Update features",
  "description": "Iterate on a Redis Feature Form definitions file with plan, merge, and re-apply workflows.",
  "categories": null,
  "tableOfContents": {"sections":[{"id":"typical-cycle","title":"Typical cycle"},{"id":"when-to-use---merge","title":"When to use --merge"},{"id":"verify-the-outcome","title":"Verify the outcome"}]}

,
  "codeExamples": []
}
```


After the first `ff apply`, most changes will be iterative: edit the definitions file, preview the delta, apply, and verify. For the full apply mechanics and failure modes, see [Define and deploy features](https://redis.io/docs/latest/develop/ai/featureform/define-and-deploy-features).

## Typical cycle

1. Change a resource definition.
2. Run a plan.
3. Apply the change.
4. Verify the resulting graph or catalog state.

Preview the change first:

```bash
ff apply \
  --workspace <workspace-id> \
  --file examples/featureform/docs/resources.py \
  --plan
```

Then apply:

```bash
ff apply \
  --workspace <workspace-id> \
  --file examples/featureform/docs/resources.py \
  --wait \
  --wait-for finished
```

## When to use `--merge`

Use `--merge` when your file is intentionally partial and omitted resources should not be treated as deletions.

## Verify the outcome

```bash
ff graph workspace stats --workspace <workspace-id>
ff catalog list --workspace <workspace-id>
```

