# ShardsIDReader

```json metadata
{
  "schema_version": 2,
  "title": "ShardsIDReader",
  "description": "Gets the shard ID for each shard in a database.",
  "categories": ["docs","operate","stack"],
  "tableOfContents": {"sections":[{"id":"parameters","title":"Parameters"},{"id":"output-records","title":"Output records"},{"id":"example","title":"Example"}]}

,
  "codeExamples": []
}
```


The `ShardsIDReader` creates a single record on each shard that represents the current shard's ID.
 
Use this reader when you want to run an operation on each shard in the database.

## Parameters

None

## Output records

Creates a record for each shard with the shard's cluster identifier.

## Example

```java
ShardsIDReader reader = new ShardsIDReader();
```
