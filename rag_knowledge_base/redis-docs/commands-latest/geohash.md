# GEOHASH

```json metadata
{
  "schema_version": 2,
  "title": "GEOHASH",
  "description": "Returns members from a geospatial index as geohash strings.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"},{"display_text":"member","multiple":true,"name":"member","optional":true,"type":"string"}],
  "syntax_fmt": "GEOHASH key [member [member ...]]",
  "complexity": "O(1) for each member requested.",
  "group": "geo",
  "command_flags": ["readonly"],
  "acl_categories": ["@read","@geo","@slow"],
  "since": "3.2.0",
  "arity": -2,
  "key_specs": [{"RO":true,"access":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"children":[{"id":"geohash-string-properties","title":"Geohash string properties"}],"id":"details","title":"Details"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Return valid [Geohash](https://en.wikipedia.org/wiki/Geohash) strings representing the position of one or more elements in a sorted set value representing a geospatial index (where elements were added using [`GEOADD`](https://redis.io/docs/latest/commands/geoadd)).

Normally Redis represents positions of elements using a variation of the Geohash
technique where positions are encoded using 52-bit integers. The encoding is
also different compared to the standard because the initial minimum and maximum
coordinates used during the encoding and decoding process are different. This
command returns a standard Geohash in the form of a string as
described in the [Wikipedia article](https://en.wikipedia.org/wiki/Geohash).

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key that holds the geospatial index (a sorted set).

</details>

<details open><summary><code>member [member ...]</code></summary>

One or more members whose Geohash strings to return.

</details>

## Details

### Geohash string properties

The command returns 11 character Geohash strings, so no precision is lost
compared to the Redis internal 52-bit representation. The returned Geohashes
have the following properties:

1. They can be shortened by removing characters from the right. They will lose precision but will still point to the same area.
2. Strings with a similar prefix are nearby, but the contrary is not true, it is possible that strings with different prefixes are nearby too.

## Examples


redis> GEOADD Sicily 13.361389 38.115556 "Palermo" 15.087269 37.502669 "Catania"
(integer) 2
redis> GEOHASH Sicily Palermo Catania
1) "sqc8b49rny0"
2) "sqdtr74hyu0"


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Array reply](../../develop/reference/protocol-spec#arrays): an array where each element is the Geohash corresponding to each member name passed as an argument to the command.

**RESP3:**

[Array reply](../../develop/reference/protocol-spec#arrays): An array where each element is the Geohash corresponding to each member name passed as an argument to the command.



