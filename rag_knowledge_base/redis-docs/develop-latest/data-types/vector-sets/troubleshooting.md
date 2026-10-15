# Troubleshooting

```json metadata
{
  "schema_version": 2,
  "title": "Troubleshooting",
  "description": "Diagnose and debug issues when working with Redis vector sets",
  "categories": ["docs","develop","stack","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"common-challenges","title":"Common challenges"},{"id":"low-recall-or-missing-results","title":"Low recall or missing results"},{"id":"filtering-issues","title":"Filtering issues"},{"id":"unexpected-memory-usage","title":"Unexpected memory usage"},{"id":"inspecting-the-graph","title":"Inspecting the graph"},{"id":"deletion-spikes","title":"Deletion spikes"},{"id":"replication-quirks","title":"Replication quirks"},{"id":"summary","title":"Summary"},{"id":"see-also","title":"See also"}]}

,
  "codeExamples": []
}
```


## Common challenges

Vector sets are approximate by design. That makes debugging trickier than with exact match queries. This section helps you understand issues with recall, filtering, and graph structure.

## Low recall or missing results

If [`VSIM`](https://redis.io/docs/latest/commands/vsim) doesn't return expected items:

- Increase the `EF` parameter:

  ```bash
  VSIM myset VALUES 3 ... COUNT 10 EF 1000
  ```

- Check quantization mode. Binary quantization (`BIN`) trades accuracy for speed.
- Use `TRUTH` to compare results against a linear scan:

  ```bash
  VSIM myset VALUES 3 ... COUNT 10 TRUTH
  ```

  This gives you the most accurate results for validation, but it's slow.

## Filtering issues

Filters silently exclude items if:

- A field is missing from the element’s attributes
- The JSON is invalid
- A type doesn’t match the expression (for example, `.rating > 8` when `.rating` is a string)

Try retrieving the attributes with [`VGETATTR`](https://redis.io/docs/latest/commands/vgetattr):

```bash
VGETATTR myset myelement
```

Double-check field names, JSON validity, and value types.

## Unexpected memory usage

Memory issues may arise from:

- Large vectors (use `REDUCE` to project down)
- High `M` values inflating link graphs
- Large or deeply nested JSON attributes
- Storing raw `FP32` vectors (`NOQUANT`)

Use default `Q8` quantization and compact attributes to save space.

## Inspecting the graph

Use [`VLINKS`](https://redis.io/docs/latest/commands/vlinks) to examine a node’s connections:

```bash
VLINKS myset myelement WITHSCORES
```

- Helps you verify whether isolated or weakly connected nodes exist.
- Useful for explaining poor recall.

## Deletion spikes

Large sets deleted using the `DEL` command can briefly spike latency as Redis reclaims memory and rebuilds HNSW linkages.

## Replication quirks

- `VADD` with `REDUCE` does not replicate the random projection matrix.
- Replicas will produce different projected vectors for the same inputs.

This doesn't affect similarity searches but does affect [`VEMB`](https://redis.io/docs/latest/commands/vemb) output.

## Summary

| Symptom                          | Try this                                                  |
|----------------------------------|-----------------------------------------------------------|
| Poor recall                      | Use higher `EF`, check quantization, use `TRUTH`          |
| Filters exclude too much         | Validate attributes with `VGETATTR`, simplify expressions |
| Memory spikes                    | Use `REDUCE`, `Q8`, smaller `M`, compact JSON             |
| Replication mismatch with REDUCE | Avoid relying on projected vectors from replicas          |

## See also

- [Filtered Search](https://redis.io/docs/latest/develop/data-types/vector-sets/filtered-search)
- [Memory Usage](https://redis.io/docs/latest/develop/data-types/vector-sets/memory)
- [Performance](https://redis.io/docs/latest/develop/data-types/vector-sets/performance)

