# Collect

```json metadata
{
  "schema_version": 2,
  "title": "Collect",
  "description": "Collects all records to the origin shard.",
  "categories": ["docs","operate","stack"],
  "tableOfContents": {"sections":[{"id":"parameters","title":"Parameters"},{"id":"returns","title":"Returns"},{"id":"example","title":"Example"}]}

,
  "codeExamples": []
}
```


```java
public GearsBuilder<T> collect()
```

Collects all of the records to the shard where the RedisGears job started.

## Parameters
 
None

## Returns

Returns a GearsBuilder object with the same template type as the input builder.

## Example

```java
GearsBuilder.CreateGearsBuilder(reader).collect();
```
