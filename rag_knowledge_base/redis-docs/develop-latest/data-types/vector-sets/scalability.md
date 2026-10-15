# Scalability

```json metadata
{
  "schema_version": 2,
  "title": "Scalability",
  "description": "Scale Redis vector sets to handle larger data sets and workloads",
  "categories": ["docs","develop","stack","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"children":[{"id":"example-strategy","title":"Example strategy"}],"id":"multi-instance-scalability","title":"Multi-instance scalability"},{"id":"key-properties","title":"Key properties"},{"id":"availability-benefits","title":"Availability benefits"},{"id":"latency-considerations","title":"Latency considerations"},{"id":"summary","title":"Summary"},{"id":"see-also","title":"See also"}]}

,
  "codeExamples": []
}
```


## Multi-instance scalability

Vector sets can scale horizontally by sharding your data across multiple Redis instances. This is done by partitioning the dataset manually across keys and nodes.

### Example strategy

You can shard data using a consistent hash:

```python
key_index = crc32(item) % 3
key = f"vset:{key_index}"
```

Then add elements into different keys:

```bash
VADD vset:0 VALUES 3 0.1 0.2 0.3 item1
VADD vset:1 VALUES 3 0.4 0.5 0.6 item2
```

To run a similarity search across all shards, send [`VSIM`](https://redis.io/docs/latest/commands/vsim) commands to each key and then merge the results client-side:

```bash
VSIM vset:0 VALUES ... WITHSCORES
VSIM vset:1 VALUES ... WITHSCORES
VSIM vset:2 VALUES ... WITHSCORES
```

Then combine and sort the results by score.

## Key properties

- Write operations ([`VADD`](https://redis.io/docs/latest/commands/vadd), [`VREM`](https://redis.io/docs/latest/commands/vrem)) scale linearly—you can insert in parallel across instances.
- Read operations ([`VSIM`](https://redis.io/docs/latest/commands/vsim)) do not scale linearly—you must query all shards for a full result set.
- Smaller vector sets yield faster queries, so distributing them helps reduce query time per node.
- Merging results client-side keeps logic simple and doesn't add server-side overhead.

## Availability benefits

This sharding model also improves fault tolerance:

- If one instance is down, you can still retrieve partial results from others.
- Use timeouts and partial fallbacks to increase resilience.

## Latency considerations

To avoid additive latency across N instances:

- Send queries to all shards in parallel.
- Wait for the slowest response.

This makes total latency close to the worst-case shard time, not the sum of all times.

## Summary

| Goal                      | Approach                                          |
|---------------------------|---------------------------------------------------|
| Scale inserts             | Split data across keys and instances              |
| Scale reads               | Query all shards and merge results                |
| High availability         | Accept partial results when some shards fail      |
| Maintain performance      | Use smaller shards for faster per-node traversal  |

## See also

- [Performance](https://redis.io/docs/latest/develop/data-types/vector-sets/performance)
- [Filtered search](https://redis.io/docs/latest/develop/data-types/vector-sets/filtered-search)
- [Memory usage](https://redis.io/docs/latest/develop/data-types/vector-sets/memory)

