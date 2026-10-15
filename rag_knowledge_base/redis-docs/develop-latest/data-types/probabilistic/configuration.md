# Configuration Parameters

```json metadata
{
  "schema_version": 2,
  "title": "Configuration Parameters",
  "description": "Redis probabilistic data structures support multiple configuration parameters.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"redis-probabilistic-data-structure-configuration-parameters","title":"Redis probabilistic data structure configuration parameters"},{"children":[{"id":"bf-error-rate","title":"bf-error-rate"},{"id":"bf-expansion-factor","title":"bf-expansion-factor"},{"id":"bf-initial-size","title":"bf-initial-size"}],"id":"default-parameters-for-bloom-filters","title":"Default parameters for Bloom filters"},{"children":[{"id":"cf-bucket-size","title":"cf-bucket-size"},{"id":"cf-initial-size","title":"cf-initial-size"},{"id":"cf-expansion-factor","title":"cf-expansion-factor"},{"id":"cf-max-expansions","title":"cf-max-expansions"},{"id":"cf-max-iterations","title":"cf-max-iterations"}],"id":"default-parameters-for-cuckoo-filters","title":"Default parameters for Cuckoo filters"},{"id":"setting-configuration-parameters-on-module-load-deprecated","title":"Setting configuration parameters on module load (deprecated)"}]}

,
  "codeExamples": []
}
```

> [!NOTE]
> As of Redis 8 in Redis Open Source (Redis 8), configuration parameters for the probabilistic data structures are now set in the following ways:
> * At load time via your `redis.conf` file.
> * At run time (where applicable) using the [`CONFIG SET`](https://redis.io/docs/latest/commands/config-set) command.
>
> Also, Redis 8 persists probabilistic configuration parameters just like any other configuration parameters (e.g., using the [`CONFIG REWRITE`](https://redis.io/docs/latest/commands/config-rewrite) command).


## Redis probabilistic data structure configuration parameters

The following table summarizes which Bloom filter configuration parameters can be set at run-time, and compatibility with Redis Software and Redis Cloud.

| Parameter name<br />(version < 8.0) | Parameter name<br />(version &#8805; 8.0) | Run-time | Redis<br />Software | Redis<br />Cloud |
| :------- | :------- | :------- | :------- | :------- |
| ERROR_RATE         | [bf-error-rate](#bf-error-rate)             | :white_check_mark: | <span title="Supported">&#x2705; Supported</span><br /><span><br /></span> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Not supported"><nobr>&#x274c; Free & Fixed</nobr></span> |
|                    | [bf-expansion-factor](#bf-expansion-factor) | :white_check_mark: |||
| INITIAL_SIZE       | [bf-initial-size](#bf-initial-size)         | :white_check_mark: | <span title="Supported">&#x2705; Supported</span><br /><span><br /></span> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Not supported"><nobr>&#x274c; Free & Fixed</nobr></span> |

The following table summarizes which Cuckoo filter configuration parameters can be set at run-time, and compatibility with Redis Software and Redis Cloud.

| Parameter name<br />(version < 8.0) | Parameter name<br />(version &#8805; 8.0) | Run-time | Redis<br />Software | Redis<br />Cloud |
| :------- | :------- | :------- | :------- | :------- |
|                    | [cf-bucket-size](#cf-bucket-size)           | :white_check_mark: |||
|                    | [cf-initial-size](#cf-initial-size)         | :white_check_mark: |||
|                    | [cf-expansion-factor](#cf-expansion-factor) | :white_check_mark: |||
| CF_MAX_EXPANSIONS  | [cf-max-expansions](#cf-max-expansions)     | :white_check_mark: | <span title="Supported">&#x2705; Supported</span><br /><span><br /></span> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Not supported"><nobr>&#x274c; Free & Fixed</nobr></span> |
|                    | [cf-max-iterations](#cf-max-iterations)     | :white_check_mark: |||

> [!NOTE]
> Parameter names for Redis Open Source versions < 8.0, while deprecated, will still be supported in Redis 8.

See also [Redis configuration](https://redis.io/docs/latest/operate/oss_and_stack/management/config).

---

> [!WARNING]
> A filter should always be sized for the expected capacity and the desired error rate.
> Using the `INSERT` family commands with the default values should be used in cases where many small filters exist and the expectation is most will remain at around the default sizes.
> Not optimizing a filter for its intended use will result in degradation of performance and memory efficiency.

## Default parameters for Bloom filters

### bf-error-rate

Default false positive rate for Bloom filters.

Type: double

Valid range: `(0 .. 1)`. Though the valid range is `(0 .. 1)` (corresponding to `> 0%` to `< 100%` false positive rate), any value greater than `0.25` is treated as `0.25`.

Default: `0.01`

### bf-expansion-factor

Added in v8.0.0.

Expansion factor for Bloom filters.

Type: integer

Valid range: `[0 .. 32768]`.

Default: `2`

### bf-initial-size

Initial capacity for Bloom filters.

Type: integer

Valid range: `[1 .. 1048576]`

Default: `100`

## Default parameters for Cuckoo filters

### cf-bucket-size

Added in v8.0.0.

The number of items in each Cuckoo filter bucket.

Type: integer

Valid range: `[1 .. 255]`

Default: `2`

### cf-initial-size

Added in v8.0.0.

Cuckoo filter initial capacity.

Type: integer

Valid range: `[2*cf-bucket-size .. 1048576]`

Default: `1024`

### cf-expansion-factor

Added in v8.0.0.

Expansion factor for Cuckoo filters.

Type: integer

Valid range: `[0 .. 32768]`

Default: `1`

### cf-max-expansions

The maximum number of expansions for Cuckoo filters.

Type: integer

Valid range: `[1 .. 65535]`

Default: `32`

### cf-max-iterations

Added in v8.0.0

The maximum number of iterations for Cuckoo filters.

Type: integer

Valid range: `[1 .. 65535]`

Default: `20`

## Setting configuration parameters on module load (deprecated)

These methods are deprecated beginning with Redis 8.

Setting configuration parameters at load-time is done by appending arguments after the `--loadmodule` argument when starting a server from the command line or after the `loadmodule` directive in a Redis config file. For example:

In [redis.conf](https://redis.io/docs/latest/operate/oss_and_stack/management/config):

```sh
loadmodule ./redisbloom.so [OPT VAL]...
```

From the [Redis CLI](https://redis.io/docs/latest/develop/tools/cli), using the [MODULE LOAD](https://redis.io/docs/latest/commands/module-load) command:

```
127.0.0.6379> MODULE LOAD redisbloom.so [OPT VAL]...
```

From the command line:

```sh
$ redis-server --loadmodule ./redisbloom.so [OPT VAL]...
```
