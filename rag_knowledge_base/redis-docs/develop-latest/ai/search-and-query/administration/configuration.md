# Configuration parameters

```json metadata
{
  "schema_version": 2,
  "title": "Configuration parameters",
  "description": "Redis Search can be tuned through multiple configuration parameters. Some of these parameters can only be set at load-time, while other parameters can be set either at load-time or at run-time.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"children":[{"id":"search-bg-index-sleep-gap","title":"search-bg-index-sleep-gap"},{"id":"search-bg-index-sleep-duration-us","title":"search-bg-index-sleep-duration-us"},{"id":"search-conn-per-shard","title":"search-conn-per-shard"},{"id":"search-cursor-max-idle","title":"search-cursor-max-idle"},{"id":"search-cursor-reply-threshold","title":"search-cursor-reply-threshold"},{"id":"search-default-dialect","title":"search-default-dialect"},{"id":"search-ext-load","title":"search-ext-load"},{"id":"search-fork-gc-clean-numeric-empty-nodes","title":"search-fork-gc-clean-numeric-empty-nodes"},{"id":"search-fork-gc-clean-threshold","title":"search-fork-gc-clean-threshold"},{"id":"search-fork-gc-retry-interval","title":"search-fork-gc-retry-interval"},{"id":"search-fork-gc-run-interval","title":"search-fork-gc-run-interval"},{"id":"search-fork-gc-sleep-before-exit","title":"search-fork-gc-sleep-before-exit"},{"id":"search-friso-ini","title":"search-friso-ini"},{"id":"gc_policy","title":"GC_POLICY"},{"id":"search-gc-scan-size","title":"search-gc-scan-size"},{"id":"search-index-cursor-limit","title":"search-index-cursor-limit"},{"id":"search-max-aggregate-results","title":"search-max-aggregate-results"},{"id":"search-max-doctablesize","title":"search-max-doctablesize"},{"id":"search-max-expansions","title":"search-max-expansions"},{"id":"search-max-prefix-expansions","title":"search-max-prefix-expansions"},{"id":"search-max-search-results","title":"search-max-search-results"},{"id":"search-_max-foreground-timeout-limit","title":"search-_max-foreground-timeout-limit"},{"id":"search-min-operation-workers","title":"search-min-operation-workers"},{"id":"search-min-phonetic-term-len","title":"search-min-phonetic-term-len"},{"id":"search-min-prefix","title":"search-min-prefix"},{"id":"search-min-stem-len","title":"search-min-stem-len"},{"id":"search-multi-text-slop","title":"search-multi-text-slop"},{"id":"search-no-mem-pools","title":"search-no-mem-pools"},{"id":"search-no-gc","title":"search-no-gc"},{"id":"search-on-timeout","title":"search-on-timeout"},{"id":"search-partial-indexed-docs","title":"search-partial-indexed-docs"},{"id":"partitions","title":"PARTITIONS"},{"id":"search-raw-docid-encoding","title":"search-raw-docid-encoding"},{"id":"search-threads","title":"search-threads"},{"id":"search-io-threads","title":"search-io-threads"},{"id":"search-tiered-hnsw-buffer-limit","title":"search-tiered-hnsw-buffer-limit"},{"id":"search-timeout","title":"search-timeout"},{"id":"search-topology-validation-timeout","title":"search-topology-validation-timeout"},{"id":"search-union-iterator-heap","title":"search-union-iterator-heap"},{"id":"upgrade_index","title":"UPGRADE_INDEX"},{"id":"search-vss-max-resize","title":"search-vss-max-resize"},{"id":"search-workers-priority-bias-threshold","title":"search-workers-priority-bias-threshold"},{"id":"search-workers","title":"search-workers"},{"id":"search-on-oom","title":"search-on-oom"}],"id":"redis-search-configuration-parameters","title":"Redis Search configuration parameters"},{"id":"set-configuration-parameters-at-module-load-time-deprecated","title":"Set configuration parameters at module load-time (deprecated)"},{"id":"set-configuration-parameters-at-run-time-for-supported-parameters-deprecated","title":"Set configuration parameters at run-time (for supported parameters, deprecated)"}]}

,
  "codeExamples": []
}
```

> [!NOTE]
> As of Redis 8 in Redis Open Source (Redis 8), configuration parameters for Redis Search are now set in the following ways:
> * At load time via your `redis.conf` file.
> * At run time (where applicable) using the [`CONFIG SET`](https://redis.io/docs/latest/commands/config-set) command.
>
> Also, Redis 8 persists Redis Search configuration parameters just like any other configuration parameters (e.g., using the [`CONFIG REWRITE`](https://redis.io/docs/latest/commands/config-rewrite) command).

## Redis Search configuration parameters

The following table summarizes which configuration parameters can be set at run-time, the versions in which each parameter is available, and compatibility with Redis Software and Redis Cloud.

The version columns indicate availability per Redis Query Engine module version (2.6, 2.8, and 2.10) and per Redis Open Source version (8.0, 8.2, 8.4, and 8.10). In those columns, &#x2705; means the parameter is available, &#x274c; means it is not available, and :warning: means it is deprecated (but still accepted) in that version.

#### Table part 1 of 2, rows 1-10

| Parameter name<br />(version < 8.0) | Parameter name<br />(version &#8805; 8.0) | 2.6 | 2.8 | 2.10 | 8.0 | 8.2 |
| :------- | :------- | :----: | :----: | :----: | :----: | :----: |
| BG_INDEX_SLEEP_GAP | [search-bg-index-sleep-gap](#search-bg-index-sleep-gap) | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| BG_INDEX_SLEEP_DURATION_US | [search-bg-index-sleep-duration-us](#search-bg-index-sleep-duration-us) | <span title="Not available">&#x274c;</span> | <span title="Not available">&#x274c;</span> | <span title="Not available">&#x274c;</span> | <span title="Not available">&#x274c;</span> | <span title="Supported">&#x2705;</span> |
| CONCURRENT_WRITE_MODE | Removed in v2.10. | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Not available">&#x274c;</span> | <span title="Not available">&#x274c;</span> | <span title="Not available">&#x274c;</span> |
| CONN_PER_SHARD | [search-conn-per-shard](#search-conn-per-shard) | <span title="Not available">&#x274c;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| CURSOR_MAX_IDLE | [search-cursor-max-idle](#search-cursor-max-idle) | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| CURSOR_REPLY_THRESHOLD | [search-cursor-reply-threshold](#search-cursor-reply-threshold) | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| DEFAULT_DIALECT | [search-default-dialect](#search-default-dialect) | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| EXTLOAD | [search-ext-load](#search-ext-load) | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| FORK_GC_CLEAN_THRESHOLD | [search-fork-gc-clean-threshold](#search-fork-gc-clean-threshold) | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| FORK_GC_RETRY_INTERVAL | [search-fork-gc-retry-interval](#search-fork-gc-retry-interval) | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |

#### Table part 1 of 2, rows 11-20

| Parameter name<br />(version < 8.0) | Parameter name<br />(version &#8805; 8.0) | 2.6 | 2.8 | 2.10 | 8.0 | 8.2 |
| :------- | :------- | :----: | :----: | :----: | :----: | :----: |
| FORK_GC_RUN_INTERVAL | [search-fork-gc-run-interval](#search-fork-gc-run-interval) | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| FORKGC_SLEEP_BEFORE_EXIT | [search-fork-gc-sleep-before-exit](#search-fork-gc-sleep-before-exit) | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| FRISOINI | [search-friso-ini](#search-friso-ini) | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| [GC_POLICY](#gc_policy) | There is no matching `CONFIG` parameter. | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| GCSCANSIZE | [search-gc-scan-size](#search-gc-scan-size) | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| INDEX_CURSOR_LIMIT | [search-index-cursor-limit](#search-index-cursor-limit) | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| INDEX_THREADS | Removed in v2.10. | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Not available">&#x274c;</span> | <span title="Not available">&#x274c;</span> | <span title="Not available">&#x274c;</span> |
| MAXAGGREGATERESULTS | [search-max-aggregate-results](#search-max-aggregate-results) | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| MAXDOCTABLESIZE | [search-max-doctablesize](#search-max-doctablesize) | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| MAXEXPANSIONS | [search-max-expansions](#search-max-expansions) | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |

#### Table part 1 of 2, rows 21-30

| Parameter name<br />(version < 8.0) | Parameter name<br />(version &#8805; 8.0) | 2.6 | 2.8 | 2.10 | 8.0 | 8.2 |
| :------- | :------- | :----: | :----: | :----: | :----: | :----: |
| MAXPREFIXEXPANSIONS | [search-max-prefix-expansions](#search-max-prefix-expansions) | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| MAXSEARCHRESULTS | [search-max-search-results](#search-max-search-results) | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| _MAX_FOREGROUND_TIMEOUT_LIMIT | [search-_max-foreground-timeout-limit](#search-_max-foreground-timeout-limit) | <span title="Not available">&#x274c;</span> | <span title="Not available">&#x274c;</span> | <span title="Not available">&#x274c;</span> | <span title="Not available">&#x274c;</span> | <span title="Not available">&#x274c;</span> |
| MIN_OPERATION_WORKERS | [search-min-operation-workers](#search-min-operation-workers) | <span title="Not available">&#x274c;</span> | <span title="Not available">&#x274c;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| MIN_PHONETIC_TERM_LEN | [search-min-phonetic-term-len](#search-min-phonetic-term-len) | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| MINPREFIX | [search-min-prefix](#search-min-prefix) | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| MINSTEMLEN | [search-min-stem-len](#search-min-stem-len) | <span title="Not available">&#x274c;</span> | <span title="Not available">&#x274c;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| MULTI_TEXT_SLOP | [search-multi-text-slop](#search-multi-text-slop) | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| NO_MEM_POOLS | [search-no-mem-pools](#search-no-mem-pools) | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| NOGC | [search-no-gc](#search-no-gc) | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |

#### Table part 1 of 2, rows 31-40

| Parameter name<br />(version < 8.0) | Parameter name<br />(version &#8805; 8.0) | 2.6 | 2.8 | 2.10 | 8.0 | 8.2 |
| :------- | :------- | :----: | :----: | :----: | :----: | :----: |
| ON_TIMEOUT | [search-on-timeout](#search-on-timeout) | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| PARTIAL_INDEXED_DOCS | [search-partial-indexed-docs](#search-partial-indexed-docs) | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| [PARTITIONS](#partitions) | There is no matching `CONFIG` parameter. | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| RAW_DOCID_ENCODING | [search-raw-docid-encoding](#search-raw-docid-encoding) | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| SEARCH_THREADS | [search-threads](#search-threads) | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| SEARCH_IO_THREADS | [search-io-threads](#search-io-threads) | <span title="Not available">&#x274c;</span> | <span title="Not available">&#x274c;</span> | <span title="Not available">&#x274c;</span> | <span title="Not available">&#x274c;</span> | <span title="Not available">&#x274c;</span> |
| TIERED_HNSW_BUFFER_LIMIT | [search-tiered-hnsw-buffer-limit](#search-tiered-hnsw-buffer-limit) | <span title="Not available">&#x274c;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| TIMEOUT | [search-timeout](#search-timeout) | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| TOPOLOGY_VALIDATION_TIMEOUT | [search-topology-validation-timeout](#search-topology-validation-timeout) | <span title="Not available">&#x274c;</span> | <span title="Not available">&#x274c;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| UNION_ITERATOR_HEAP | [search-union-iterator-heap](#search-union-iterator-heap) | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |

#### Table part 1 of 2, rows 41-50

| Parameter name<br />(version < 8.0) | Parameter name<br />(version &#8805; 8.0) | 2.6 | 2.8 | 2.10 | 8.0 | 8.2 |
| :------- | :------- | :----: | :----: | :----: | :----: | :----: |
| [UPGRADE_INDEX](#upgrade_index) | There is no matching `CONFIG` parameter. | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| VSS_MAX_RESIZE | [search-vss-max-resize](#search-vss-max-resize) | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| WORKERS_PRIORITY_BIAS_THRESHOLD | [search-workers-priority-bias-threshold](#search-workers-priority-bias-threshold) | <span title="Not available">&#x274c;</span> | <span title="Not available">&#x274c;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| WORKERS | [search-workers](#search-workers) | <span title="Not available">&#x274c;</span> | <span title="Not available">&#x274c;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| OSS_GLOBAL_PASSWORD | Deprecated in v8.0.0. Replace with the `masterauth` password. | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Deprecated" class="font-serif">:warning:</span> | <span title="Deprecated" class="font-serif">:warning:</span> |
| MT_MODE | Deprecated in v8.0.0. Use search-workers. | <span title="Not available">&#x274c;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Deprecated" class="font-serif">:warning:</span> | <span title="Deprecated" class="font-serif">:warning:</span> |
| PRIVILEGED_THREADS_NUM | Deprecated in v8.0.0. Use search-workers-priority-bias-threshold. | <span title="Not available">&#x274c;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Deprecated" class="font-serif">:warning:</span> | <span title="Deprecated" class="font-serif">:warning:</span> |
| WORKER_THREADS | Deprecated in v8.0.0. Use search-min-operation-workers. | <span title="Not available">&#x274c;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Deprecated" class="font-serif">:warning:</span> | <span title="Deprecated" class="font-serif">:warning:</span> |
| SAFEMODE | Deprecated in v1.6.0. This is now the default setting. | <span title="Deprecated" class="font-serif">:warning:</span> | <span title="Deprecated" class="font-serif">:warning:</span> | <span title="Not available">&#x274c;</span> | <span title="Not available">&#x274c;</span> | <span title="Not available">&#x274c;</span> |
| FORK_GC_CLEAN_NUMERIC_EMPTY_NODES | Deprecated in v8.0.0. | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Deprecated" class="font-serif">:warning:</span> | <span title="Deprecated" class="font-serif">:warning:</span> |

#### Table part 2 of 2, rows 1-10

| Parameter name<br />(version < 8.0) | 8.4 | 8.10 | Run-time | Redis<br />Software | Redis<br />Cloud |
| :------- | :----: | :----: | :------- | :------- | :------- |
| BG_INDEX_SLEEP_GAP | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | :white_large_square: | <span title="Supported">&#x2705; Supported</span><br /><span><br /></span> | <span title="Not supported"><nobr>&#x274c; Flexible & Annual</span><br /><span title="Not supported"><nobr>&#x274c; Free & Fixed</nobr></span> |
| BG_INDEX_SLEEP_DURATION_US | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | :white_large_square: |  |  |
| CONCURRENT_WRITE_MODE | <span title="Not available">&#x274c;</span> | <span title="Not available">&#x274c;</span> |  |  |  |
| CONN_PER_SHARD | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | :white_check_mark: |  |  |
| CURSOR_MAX_IDLE | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | :white_check_mark: | <span title="Supported">&#x2705; Supported</span><br /><span><br /></span> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Not supported"><nobr>&#x274c; Free & Fixed</nobr></span> |
| CURSOR_REPLY_THRESHOLD | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | :white_check_mark: |  |  |
| DEFAULT_DIALECT | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | :white_check_mark: | <span title="Supported">&#x2705; Supported</span><br /><span><br /></span> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Not supported"><nobr>&#x274c; Free & Fixed</nobr></span> |
| EXTLOAD | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | :white_large_square: | <span title="Supported">&#x2705; Supported</span><br /><span><br /></span> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Not supported"><nobr>&#x274c; Free & Fixed</nobr></span> |
| FORK_GC_CLEAN_THRESHOLD | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | :white_check_mark: | <span title="Supported">&#x2705; Supported</span><br /><span><br /></span> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Not supported"><nobr>&#x274c; Free & Fixed</nobr></span> |
| FORK_GC_RETRY_INTERVAL | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | :white_check_mark: | <span title="Supported">&#x2705; Supported</span><br /><span><br /></span> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Not supported"><nobr>&#x274c; Free & Fixed</nobr></span> |

#### Table part 2 of 2, rows 11-20

| Parameter name<br />(version < 8.0) | 8.4 | 8.10 | Run-time | Redis<br />Software | Redis<br />Cloud |
| :------- | :----: | :----: | :------- | :------- | :------- |
| FORK_GC_RUN_INTERVAL | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | :white_check_mark: | <span title="Supported">&#x2705; Supported</span><br /><span><br /></span> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Not supported"><nobr>&#x274c; Free & Fixed</nobr></span> |
| FORKGC_SLEEP_BEFORE_EXIT | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | :white_check_mark: |  |  |
| FRISOINI | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | :white_large_square: | <span title="Supported">&#x2705; Supported</span><br /><span><br /></span> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Not supported"><nobr>&#x274c; Free & Fixed</nobr></span> |
| [GC_POLICY](#gc_policy) | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | :white_large_square: | <span title="Supported">&#x2705; Supported</span><br /><span><br /></span> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Not supported"><nobr>&#x274c; Free & Fixed</nobr></span> |
| GCSCANSIZE | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | :white_large_square: | <span title="Supported">&#x2705; Supported</span><br /><span><br /></span> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Not supported"><nobr>&#x274c; Free & Fixed</nobr></span> |
| INDEX_CURSOR_LIMIT | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | :white_large_square: |  |  |
| INDEX_THREADS | <span title="Not available">&#x274c;</span> | <span title="Not available">&#x274c;</span> |  |  |  |
| MAXAGGREGATERESULTS | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | :white_check_mark: | <span title="Supported">&#x2705; Supported</span><br /><span><br /></span> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Not supported"><nobr>&#x274c; Free & Fixed</nobr></span> |
| MAXDOCTABLESIZE | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | :white_large_square: | <span title="Supported">&#x2705; Supported</span><br /><span><br /></span> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Not supported"><nobr>&#x274c; Free & Fixed</nobr></span> |
| MAXEXPANSIONS | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | :white_check_mark: |  |  |

#### Table part 2 of 2, rows 21-30

| Parameter name<br />(version < 8.0) | 8.4 | 8.10 | Run-time | Redis<br />Software | Redis<br />Cloud |
| :------- | :----: | :----: | :------- | :------- | :------- |
| MAXPREFIXEXPANSIONS | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | :white_check_mark: | <span title="Supported">&#x2705; Supported</span><br /><span><br /></span> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Not supported"><nobr>&#x274c; Free & Fixed</nobr></span> |
| MAXSEARCHRESULTS | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | :white_check_mark: | <span title="Supported">&#x2705; Supported</span><br /><span><br /></span> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Not supported"><nobr>&#x274c; Free & Fixed</nobr></span> |
| _MAX_FOREGROUND_TIMEOUT_LIMIT | <span title="Not available">&#x274c;</span> | <span title="Supported">&#x2705;</span> | :white_check_mark: |  |  |
| MIN_OPERATION_WORKERS | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | :white_check_mark: |  |  |
| MIN_PHONETIC_TERM_LEN | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | :white_check_mark: |  |  |
| MINPREFIX | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | :white_check_mark: | <span title="Supported">&#x2705; Supported</span><br /><span><br /></span> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Not supported"><nobr>&#x274c; Free & Fixed</nobr></span> |
| MINSTEMLEN | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | :white_check_mark: | <span title="Supported">&#x2705; Supported</span><br /><span><br /></span> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Not supported"><nobr>&#x274c; Free & Fixed</nobr></span> |
| MULTI_TEXT_SLOP | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | :white_large_square: |  |  |
| NO_MEM_POOLS | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | :white_large_square: |  |  |
| NOGC | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | :white_large_square: | <span title="Supported">&#x2705; Supported</span><br /><span><br /></span> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Not supported"><nobr>&#x274c; Free & Fixed</nobr></span> |

#### Table part 2 of 2, rows 31-40

| Parameter name<br />(version < 8.0) | 8.4 | 8.10 | Run-time | Redis<br />Software | Redis<br />Cloud |
| :------- | :----: | :----: | :------- | :------- | :------- |
| ON_TIMEOUT | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | :white_check_mark: | <span title="Supported">&#x2705; Supported</span><br /><span><br /></span> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Not supported"><nobr>&#x274c; Free & Fixed</nobr></span> |
| PARTIAL_INDEXED_DOCS | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | :white_large_square: | <span title="Supported">&#x2705; Supported</span><br /><span><br /></span> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Not supported"><nobr>&#x274c; Free & Fixed</nobr></span> |
| [PARTITIONS](#partitions) | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | :white_large_square: | <span title="Supported">&#x2705; Supported</span><br /><span><br /></span> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Not supported"><nobr>&#x274c; Free & Fixed</nobr></span> |
| RAW_DOCID_ENCODING | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | :white_large_square: |  |  |
| SEARCH_THREADS | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | :white_large_square: |  |  |
| SEARCH_IO_THREADS | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | :white_large_square: |  |  |
| TIERED_HNSW_BUFFER_LIMIT | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | :white_large_square: |  |  |
| TIMEOUT | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | :white_check_mark: | <span title="Supported">&#x2705; Supported</span><br /><span><br /></span> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Not supported"><nobr>&#x274c; Free & Fixed</nobr></span> |
| TOPOLOGY_VALIDATION_TIMEOUT | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | :white_check_mark: |  |  |
| UNION_ITERATOR_HEAP | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | :white_check_mark: | <span title="Supported">&#x2705; Supported</span><br /><span><br /></span> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Not supported"><nobr>&#x274c; Free & Fixed</nobr></span> |

#### Table part 2 of 2, rows 41-50

| Parameter name<br />(version < 8.0) | 8.4 | 8.10 | Run-time | Redis<br />Software | Redis<br />Cloud |
| :------- | :----: | :----: | :------- | :------- | :------- |
| [UPGRADE_INDEX](#upgrade_index) | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | :white_large_square: | <span title="Supported">&#x2705; Supported</span><br /><span><br /></span> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Not supported"><nobr>&#x274c; Free & Fixed</nobr></span> |
| VSS_MAX_RESIZE | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | :white_check_mark: |  |  |
| WORKERS_PRIORITY_BIAS_THRESHOLD | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | :white_large_square: |  |  |
| WORKERS | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | :white_check_mark: |  |  |
| OSS_GLOBAL_PASSWORD | <span title="Deprecated" class="font-serif">:warning:</span> | <span title="Deprecated" class="font-serif">:warning:</span> | :white_large_square: | <span title="Supported">&#x2705; Supported</span><br /><span><br /></span> | <span title="Not supported"><nobr>&#x274c; Flexible & Annual</span><br /><span title="Not supported"><nobr>&#x274c; Free & Fixed</nobr></span> |
| MT_MODE | <span title="Deprecated" class="font-serif">:warning:</span> | <span title="Deprecated" class="font-serif">:warning:</span> | :white_large_square: |  |  |
| PRIVILEGED_THREADS_NUM | <span title="Deprecated" class="font-serif">:warning:</span> | <span title="Deprecated" class="font-serif">:warning:</span> | :white_large_square: |  |  |
| WORKER_THREADS | <span title="Deprecated" class="font-serif">:warning:</span> | <span title="Deprecated" class="font-serif">:warning:</span> | :white_large_square: |  |  |
| SAFEMODE | <span title="Not available">&#x274c;</span> | <span title="Not available">&#x274c;</span> | :white_large_square: |  |  |
| FORK_GC_CLEAN_NUMERIC_EMPTY_NODES | <span title="Deprecated" class="font-serif">:warning:</span> | <span title="Deprecated" class="font-serif">:warning:</span> | :white_large_square: |  |  |



> [!NOTE]
> Parameter names for Redis Open Source versions < 8.0, while deprecated, will still be supported in Redis 8.

---

### search-bg-index-sleep-gap

The number of iterations to run while performing background indexing before `usleep(1)` (sleep for 1 microsecond) is called, ensuring that Redis can process other commands.

Type: integer

Valid range: `[1 .. 4294967295]`

Default: `100`

### search-bg-index-sleep-duration-us

Added in the 8.2 maintenance line (v8.2.12) and the 8.4 maintenance line (v8.4.9). Not available in Redis Open Source 8.0, and not present in the initial 8.2.0 or 8.4.0 releases.

The sleep duration (in microseconds) used during background indexing. During background indexing (triggered by `FT.CREATE` on existing keys), Redis periodically sleeps to allow the main thread to process commands. This parameter controls how long each sleep lasts. Works in conjunction with [`search-bg-index-sleep-gap`](#search-bg-index-sleep-gap), which controls how many iterations occur between sleeps.

Type: integer

Valid range: `[1 .. 999999]`

Default: `1`

### search-conn-per-shard

The number of connections to each shard in a cluster.
If `0`, the number of connections is set to `search-workers` + 1.

Type: integer

Valid range: `[0 .. 9,223,372,036,854,775,807]`

Default: `0`

### search-cursor-max-idle

The maximum idle time (in ms) that can be set to the [cursor api](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/aggregations#cursor-api).

Type: integer

Valid range: `[0 .. 9,223,372,036,854,775,807]`

Default: `300000`

### search-cursor-reply-threshold

The maximum number of replies to accumulate before triggering `_FT.CURSOR READ` on the shards.

Type: integer

Valid range: `[1 .. 9,223,372,036,854,775,807]`

Default: `1`

### search-default-dialect

The default
[DIALECT](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/dialects)
to be used by [`FT.CREATE`](https://redis.io/docs/latest/commands/ft.create), [`FT.AGGREGATE`](https://redis.io/docs/latest/commands/ft.aggregate), [`FT.EXPLAIN`](https://redis.io/docs/latest/commands/ft.explain), [`FT.EXPLAINCLI`](https://redis.io/docs/latest/commands/ft.explaincli), and [`FT.SPELLCHECK`](https://redis.io/docs/latest/commands/ft.spellcheck).
See [Query dialects](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/dialects)
for more information.

Default: `1`

### search-ext-load

If present, Redis will try to load an extension dynamic library from the specified file path.
See [Extensions](https://redis.io/docs/latest/develop/ai/search-and-query/administration/extensions) for details.

Type: string

Default: not set

### search-fork-gc-clean-numeric-empty-nodes

Clean empty nodes from numeric tree.

Type: boolean

Default: `TRUE`

### search-fork-gc-clean-threshold

The fork GC will only start to clean when the number of uncleaned documents exceeds this threshold, otherwise it will skip this run.

Type: integer

Valid range: `[1 .. 9,223,372,036,854,775,807]`

Default: `100`

### search-fork-gc-retry-interval

Interval (in seconds) in which Redis will retry to run fork GC in case of a failure.
This setting can only be combined with the [`search-gc-policy`](#search-gc-policy) `FORK` setting.

Type: integer

Valid range: `[1 .. 9,223,372,036,854,775,807]`

Default: `5`

### search-fork-gc-run-interval

Interval (in seconds) between two consecutive fork GC runs.
This setting can only be combined with the [`search-gc-policy`](#search-gc-policy) `FORK` setting.

Type: integer

Valid range: `[1 .. 9,223,372,036,854,775,807]`

Default: `30`

### search-fork-gc-sleep-before-exit

The number of seconds for the fork GC to sleep before exit. This value should always be set to 0 except when testing.

Type: integer

Valid range: `[1 .. 9,223,372,036,854,775,807]`

Default: `0`

### search-friso-ini

If present, load the custom Chinese dictionary from the specified path. See [Using custom dictionaries](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/chinese#using-custom-dictionaries) for more details.

Type: string

Default: not set

### GC_POLICY

The garbage collection policy. The two supported policies are:
* FORK: uses a forked thread for garbage collection (v1.4.1 and above). This is the default GC policy since v1.6.1 and is ideal for general purpose workloads.
* LEGACY: uses a synchronous, in-process fork. This is ideal for read-heavy and append-heavy workloads with very few updates/deletes. Deprecated in v2.6.0.

Note: When `GC_POLICY` is set to `FORK`, it can be combined with the `search-fork-gc-run-interval` and `search-fork-gc-retry-interval` settings. 

Type: string

Valid values: `FORK` or `DEFAULT`

Default: `FORK`

### search-gc-scan-size

The bulk size of the internal GC used for cleaning up indexes.

Type: integer

Valid range: `[1 .. 9,223,372,036,854,775,807]`

Redis Open Source default: `100`

Redis Software default: `-1` (unlimited)

Redis Cloud defaults:
- Flexible & Annual: `-1` (unlimited)
- Free & Fixed: `10000`

### search-index-cursor-limit

Available in Redis Query Engine v2.6.24, v2.8.21, and v2.10.9 and their later maintenance releases, and in Redis Open Source 8.0 and later.

The maximum number of cursors that can be opened, per shard, at any given time. Cursors can be opened by the user via [`FT.AGGREGATE WITHCURSOR`](https://redis.io/docs/latest/commands/ft.aggregate). Cursors are also opened internally by  Redis Search for long-running queries. Once `INDEX_CURSOR_LIMIT` is reached, any further attempts to open a cursor will result in an error.

> [!NOTE] Notes
> * Caution should be used in modifying this parameter.  Every open cursor results in additional memory usage.
> * Cursor usage should be regulated first by use of [`FT.CURSOR DEL`](https://redis.io/docs/latest/commands/ft.cursor-del) and/or [`MAXIDLE`](https://redis.io/docs/latest/commands/ft.aggregate) prior to modifying `INDEX_CURSOR_LIMIT`
> * See [Cursor API](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/aggregations#cursor-api) for more details.

Type: integer

Default: `128`

### search-max-aggregate-results

The maximum number of results to be returned by the `FT.AGGREGATE` command if `LIMIT` is used.

Type: integer

Valid range: `[1 .. 9,223,372,036,854,775,807]`

Redis Open Source default: `-1` (unlimited)

Redis Software default: `-1` (unlimited)

Redis Cloud defaults:
- Flexible & Annual: `-1` (unlimited)
- Free & Fixed: `10000`

### search-max-doctablesize

The maximum size of the internal hash table used for storing documents. 
Note: this configuration option doesn't limit the number of documents that can be stored. It only affects the hash table internal array maximum size.
Decreasing this property can decrease the memory overhead in cases where the index holds a small number of documents that are constantly updated.

Type: integer

Valid range: `[1 .. 18,446,744,073,709,551,615]`

Default: `1000000`

### search-max-expansions

This parameter is an alias for [search-max-prefix-expansions](#search-max-prefix-expansions).

### search-max-prefix-expansions

The maximum number of expansions allowed for query prefixes.
The maximum number of expansions allowed for query prefixes. Setting it too high can cause performance issues. If `search-max-prefix-expansions` is reached, the query will continue with the first acquired results. The configuration is applicable for all affix queries including prefix, suffix, and infix (contains) queries.

Type: integer

Valid range: `[1 .. 9,223,372,036,854,775,807]`

Default: `200`

### search-max-search-results

The maximum number of results to be returned by the `FT.SEARCH` command if `LIMIT` is used. Set it to `-1` to remove the limit.

Type: integer

Valid range: `[1 .. 9,223,372,036,854,775,807]`

Redis Open Source default: `1000000`

Redis Software default: `1000000`

Redis Cloud defaults:
- Flexible & Annual: `1000000`
- Free & Fixed: `10000`

### search-_max-foreground-timeout-limit

Available in Redis Search 8.10 and later.

Sets the hard upper bound, in milliseconds, for the effective query timeout when
[`search-workers`](#search-workers) is `0`. The effective timeout is either a query's
`TIMEOUT` value or, when the query doesn't specify one, the value inherited from
[`search-timeout`](#search-timeout).

If the effective timeout exceeds this limit, Redis caps it instead of rejecting the query.
This also applies to `TIMEOUT 0`, which normally means unlimited. RESP3 clients receive a
`MaxTimeoutCapped` warning when the timeout is capped. The limit applies to
[`FT.SEARCH`](https://redis.io/docs/latest/commands/ft.search),
[`FT.AGGREGATE`](https://redis.io/docs/latest/commands/ft.aggregate),
[`FT.CURSOR READ`](https://redis.io/docs/latest/commands/ft.cursor-read), and
[`FT.HYBRID`](https://redis.io/docs/latest/commands/ft.hybrid).

Set this parameter to `0` to disable the limit. The limit is also inactive when
`search-workers` is greater than `0`.

Changes to this parameter, `search-timeout`, and `search-workers` are accepted and logged
at notice level regardless of their current combination. Redis evaluates the settings and
applies the limit when each query runs.

The legacy `FT.CONFIG` name is `_MAX_FOREGROUND_TIMEOUT_LIMIT`.

Type: integer

Valid range: `[0 .. 9,223,372,036,854,775,807]`

Default: `60000`

### search-min-operation-workers

The number of worker threads to use for background tasks when the server is in an operation event.

Type: integer

Valid range: `[0 .. 8192]`

Default: `4`

### search-min-phonetic-term-len

The minimum length of term to be considered for phonetic matching.

Type: integer

Valid range: `[1 .. 9,223,372,036,854,775,807]`

Default: `3`

### search-min-prefix

The minimum number of characters allowed for prefix queries (for example, hel*). Setting it to `1` can reduce performance.

Type: integer

Valid range: `[1 .. 9,223,372,036,854,775,807]`

Default: `2`

### search-min-stem-len

The minimum word length to stem. Setting it lower than `4` can reduce performance.

Type: integer

Valid range: `[2 .. 4,294,967,295]`

Redis Open Source default: `4`

Redis Software and Redis Cloud default: `2`

### search-multi-text-slop

Set the delta that is used to increase positional offsets between array slots for multi text values.
This will allow you to control the level of separation between phrases in different array slots; related to the `SLOP` parameter of `FT.SEARCH` command.

Type: integer

Valid range: `[0 .. 4,294,967,295]`

Default: `100`

### search-no-mem-pools

Set Redis Search to run without memory pools.

Type: boolean

Default: `FALSE`

### search-no-gc

If set to `TRUE`, garbage collection is disabled for all indexes.

Type: boolean

Default: `FALSE`

### search-on-timeout

The response policy for queries that exceed their effective timeout can be one of the following:

* `RETURN`: this policy will return the top results accumulated by the query until it timed out.
* `RETURN_STRICT`: like `RETURN`, returns the partial results accumulated when a query exceeds the timeout instead of failing, but strictly enforces the configured timeout as a hard deadline. This matters most in clustered deployments: with `RETURN`, the first shard to time out aborts the whole query early; with `RETURN_STRICT`, the coordinator keeps gathering results from all shards up to the deadline and then returns whatever accumulated at that point. Available in Redis Query Engine 8.10 and later.
* `FAIL`: will return an error when the query exceeds the timeout value.

Type: string

Valid values: `RETURN`, `RETURN_STRICT`, `FAIL`

Default: `RETURN`

### search-partial-indexed-docs

Available in Redis Query Engine 2.0 and later.

Enable/disable the Redis command filter. The filter optimizes partial updates of hashes
and may avoid re-indexing the hash if changed fields are not part of the schema. 

The Redis command filter will be executed upon each Redis command.  Though the filter is
optimized, this will introduce a small increase in latency on all commands.  
This configuration is best used with partially indexed documents where the non-indexed fields are updated frequently.

Type: integer

Valid values: `0` (false), `1` (true)

Default: `0`

### PARTITIONS

The number of coordinator partitions to use in a clustered deployment (Redis Software,
Redis Cloud, or Redis Open Source in cluster mode). This parameter is deprecated and
immutable: any value passed to it is ignored, and the number of partitions is always
determined automatically.

Type: string

Valid values: `AUTO`

Default: `AUTO`

### search-raw-docid-encoding

Disable compression for DocID inverted indexes to boost CPU performance.

Type: boolean

Default: `FALSE`

### search-threads

Sets the number of search threads in the coordinator thread pool.

Type: integer

### search-io-threads

Sets the number of threads used in the coordinator to run I/O tasks with other shards.

Type: integer

Valid range: `[1 .. 256]`

Default: 1

### search-tiered-hnsw-buffer-limit

Used for setting the buffer limit threshold for vector tiered HNSW indexes. If Redis is using `WORKERS` for indexing, and the number of vectors waiting in the buffer to be indexed exceeds this limit, new vectors are inserted directly into HNSW.

Type: integer

Valid range: `[0 .. 9,223,372,036,854,775,807]`

Default: `1024`

### search-timeout

The default amount of time in milliseconds that a search query is allowed to run when the query doesn't specify its own `TIMEOUT`. A query-specific `TIMEOUT` overrides this value, so `search-timeout` is a default, not a ceiling. When [`search-_max-foreground-timeout-limit`](#search-_max-foreground-timeout-limit) is active, it provides the ceiling for the effective timeout.

If the effective timeout is exceeded, Redis returns the top results accumulated so far, or an error depending on the policy set with [`search-on-timeout`](#search-on-timeout). The timeout can be disabled by setting it to `0`.

> [!NOTE] Notes
> * `search-timeout` refers to query time only.
> * Parsing the query is not counted towards `search-timeout`.
> * If `search-timeout` was not reached during the search, finalizing operations such as loading document content or reducers continue.

Type: integer

Value range: `[1 .. 9,223,372,036,854,775,807]`

Redis Open Source default: `500`

Redis Software default: `500`

Redis Cloud defaults:
- Flexible & Annual: `500`
- Free & Fixed: `100`

### search-topology-validation-timeout

Sets the timeout in milliseconds for topology validation. After this timeout, any pending requests will be processed, even if the topology is not fully connected. A value of `0` means no timeout.

Type: integer

Valid range: `[1 .. 9,223,372,036,854,775,807]`

Default: `30000`

### search-union-iterator-heap

The minimum number of iterators in a union at which the iterator will switch to a heap based implementation.

Type: integer

Valid range: `[1 .. 9,223,372,036,854,775,807]`

Default: `20`

### UPGRADE_INDEX

There is no matching `CONFIG` parameter for `UPGRADE_INDEX`; it is available only as an `FT.CONFIG` parameter or as a module load-time argument.

Relevant only when loading an v1.x RDB file. Specify the argument for upgrading the index.
This configuration setting is a special configuration option introduced to upgrade indexes from v1.x Redis Search versions, otherwise known as legacy indexes. This configuration option needs to be given for each legacy index, followed by the index name and all valid options for the index description (also referred to as the `ON` arguments for following hashes) as described on [FT.CREATE](https://redis.io/docs/latest/commands/ft.create) command page. 

Type: string

Default: there is no default for index name, and the other arguments have the same defaults as with the [`FT.CREATE`](https://redis.io/docs/latest/commands/ft.create) command.

**Example**

```
UPGRADE_INDEX idx PREFIX 1 tt LANGUAGE french LANGUAGE_FIELD MyLang SCORE 0.5 SCORE_FIELD MyScore
    PAYLOAD_FIELD MyPayload UPGRADE_INDEX idx1
```

> [!NOTE] Notes
> * If the RDB file does not contain a legacy index that's specified in the configuration, a warning message will be added to the log file, and loading will continue.
> * If the RDB file contains a legacy index that wasn't specified in the configuration, loading will fail and the server won't start.

### search-vss-max-resize

Available in Redis Query Engine 2.4.8 and later.

The maximum memory resize (in bytes) for vector indexes.
The maximum memory resize (in bytes) for vector indexes. This value will override default memory limits if you need to allow for a large [`BLOCK_SIZE`](https://redis.io/docs/latest/develop/ai/search-and-query/vectors#create-a-vector-index).

Type: integer

Valid range: `[0 .. 4,294,967,295]`

Default: `0`

### search-workers-priority-bias-threshold

The number of high priority tasks to be executed at any given time by the worker thread pool before executing low priority tasks. After this number of high priority tasks are being executed, the worker thread pool will execute high and low priority tasks alternately.

Type: integer

Valid range: `[1 .. 9,223,372,036,854,775,807]`

Default: `1`

### search-workers

The number of worker threads to use for query processing and background tasks.

Type: integer

Valid range: `[0 .. 8192]`

Default: `0`

### search-on-oom

Specifies the response policy for queries when the server's current memory usage exceeds the configured [maxmemory](https://redis.io/docs/latest/develop/reference/eviction/#maxmem) limit.

* `IGNORE`: Execute the query regardless of current memory usage.
* `RETURN`: In cluster mode, the query returns partial results from shards that did not exceed the memory limit. Shards that exceed the limit will not contribute results.
* `FAIL`: Will return an error if memory usage exceeds the memory limit.

Type: string

Valid values: `IGNORE`, `RETURN`, `FAIL`

Default: `IGNORE`

> [!NOTE] Notes
> To prevent potential out-of-memory conditions, it is recommended that you set this parameter to FAIL or RETURN rather than IGNORE.

## Set configuration parameters at module load-time (deprecated)

These methods are deprecated beginning with Redis 8.

Setting configuration parameters at load-time is done by appending arguments after the `--loadmodule` argument when starting a server from the command line, or after the `loadmodule` directive in a Redis config file. For example:

In [redis.conf](https://redis.io/docs/latest/operate/oss_and_stack/management/config):

```
loadmodule ./redisearch.so [OPT VAL]...
```

From the [Redis CLI](https://redis.io/docs/latest/develop/tools/cli), using the [MODULE LOAD](https://redis.io/docs/latest/commands/module-load) command:

```
127.0.0.6379> MODULE LOAD redisearch.so [OPT VAL]...
```

From the command line:

```
$ redis-server --loadmodule ./redisearch.so [OPT VAL]...
```

## Set configuration parameters at run-time (for supported parameters, deprecated)

These methods are deprecated beginning with Redis 8.

Redis Search exposes the `FT.CONFIG` endpoint to allow for the setting and retrieval of configuration parameters at run-time.

To set the value of a configuration parameter at run-time (for supported parameters), simply run:

```sh
FT.CONFIG SET OPT1 VAL1
```

Similarly, you can retrieve current configuration parameter values using:

```sh
FT.CONFIG GET OPT1
FT.CONFIG GET *
```

Values set using [`FT.CONFIG SET`](https://redis.io/docs/latest/commands/ft.config-set) are not persisted after server restart.

