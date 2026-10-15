# GEOPOS

```json metadata
{
  "schema_version": 2,
  "title": "GEOPOS",
  "description": "Returns the longitude and latitude of members from a geospatial index.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"},{"display_text":"member","multiple":true,"name":"member","optional":true,"type":"string"}],
  "syntax_fmt": "GEOPOS key [member [member ...]]",
  "complexity": "O(1) for each member requested.",
  "group": "geo",
  "command_flags": ["readonly"],
  "acl_categories": ["@read","@geo","@slow"],
  "since": "3.2.0",
  "arity": -2,
  "key_specs": [{"RO":true,"access":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Return the positions (longitude,latitude) of all the specified members of the geospatial index represented by the sorted set at *key*.

Given a sorted set representing a geospatial index, populated using the [`GEOADD`](https://redis.io/docs/latest/commands/geoadd) command, it is often useful to obtain back the coordinates of specified members. When the geospatial index is populated via [`GEOADD`](https://redis.io/docs/latest/commands/geoadd) the coordinates are converted into a 52 bit geohash, so the coordinates returned may not be exactly the ones used in order to add the elements, but small errors may be introduced.

The command can accept a variable number of arguments so it always returns an array of positions even when a single element is specified.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key that holds the geospatial index (a sorted set).

</details>

<details open><summary><code>member [member ...]</code></summary>

One or more members whose longitude and latitude to return.

</details>

## Examples


redis> GEOADD Sicily 13.361389 38.115556 "Palermo" 15.087269 37.502669 "Catania"
(integer) 2
redis> GEOPOS Sicily Palermo Catania NonExisting
1) 1) "13.361389338970184"
   2) "38.1155563954963"
2) 1) "15.087267458438873"
   2) "37.50266842333162"
3) (nil)


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Array reply](../../develop/reference/protocol-spec#arrays): An array where each element is a two elements array representing longitude and latitude (x,y) of each member name passed as argument to the command. Non-existing elements are reported as [Nil reply](../../develop/reference/protocol-spec#bulk-strings) elements of the array.

**RESP3:**

[Array reply](../../develop/reference/protocol-spec#arrays): An array where each element is a two elements array representing longitude and latitude (x,y) of each member name passed as argument to the command. Non-existing elements are reported as [Null reply](../../develop/reference/protocol-spec#nulls) elements of the array.



