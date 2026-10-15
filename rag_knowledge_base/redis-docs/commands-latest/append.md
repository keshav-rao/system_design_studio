# APPEND

```json metadata
{
  "schema_version": 2,
  "title": "APPEND",
  "description": "Appends a string to the value of a key. Creates the key if it doesn't exist.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"},{"display_text":"value","name":"value","type":"string"}],
  "syntax_fmt": "APPEND key value",
  "complexity": "O(1). The amortized time complexity is O(1) assuming the appended value is small and the already present value is of any size, since the dynamic string library used by Redis will double the free space available on every reallocation.",
  "group": "string",
  "command_flags": ["write","denyoom","fast"],
  "acl_categories": ["@write","@string","@fast"],
  "since": "2.0.0",
  "arity": 3,
  "key_specs": [{"RW":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"},"insert":true}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"children":[{"id":"pattern-time-series","title":"Pattern: time series"}],"id":"details","title":"Details"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Appends a value to the string stored at `key`. If `key` does not exist, it is created with an empty string, so in that case, `APPEND` behaves like [`SET`](https://redis.io/docs/latest/commands/set).

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key.

</details>

<details open><summary><code>value</code></summary>

The string to append to the existing value.

</details>

## Examples


redis> EXISTS mykey
(integer) 0
redis> APPEND mykey "Hello"
(integer) 5
redis> APPEND mykey " World"
(integer) 11
redis> GET mykey
"Hello World"


## Details

### Pattern: time series

The `APPEND` command can be used to create a very compact representation of a
list of fixed-size samples, usually referred as _time series_.
Every time a new sample arrives we can store it using the command

```
APPEND timeseries "fixed-size sample"
```

Accessing individual elements in the time series is not hard:

* [`STRLEN`](https://redis.io/docs/latest/commands/strlen) can be used in order to obtain the number of samples.
* [`GETRANGE`](https://redis.io/docs/latest/commands/getrange) allows for random access of elements.
  If our time series have associated time information we can easily implement
  a binary search to get range combining [`GETRANGE`](https://redis.io/docs/latest/commands/getrange) with the Lua scripting
  engine available in Redis 2.6.
* [`SETRANGE`](https://redis.io/docs/latest/commands/setrange) can be used to overwrite an existing time series.

The limitation of this pattern is that we are forced into an append-only mode
of operation, there is no way to cut the time series to a given size easily
because Redis currently lacks a command able to trim string objects.
However the space efficiency of time series stored in this way is remarkable.

Hint: it is possible to switch to a different key based on the current Unix
time, in this way it is possible to have just a relatively small amount of
samples per key, to avoid dealing with very big keys, and to make this pattern
more friendly to be distributed across many Redis instances.

An example sampling the temperature of a sensor using fixed-size strings (using
a binary format is better in real implementations).


redis> APPEND ts "0043"
(integer) 4
redis> APPEND ts "0035"
(integer) 8
redis> GETRANGE ts 0 3
"0043"
redis> GETRANGE ts 4 7
"0035"


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Integer reply](../../develop/reference/protocol-spec#integers): the length of the string after the append operation.

**RESP3:**

[Integer reply](../../develop/reference/protocol-spec#integers): the length of the string after the append operation.



