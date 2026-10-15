# Foreach

```json metadata
{
  "schema_version": 2,
  "title": "Foreach",
  "description": "For each record in the pipe, runs some operations.",
  "categories": ["docs","operate","stack"],
  "tableOfContents": {"sections":[{"id":"parameters","title":"Parameters"},{"id":"returns","title":"Returns"},{"id":"example","title":"Example"}]}

,
  "codeExamples": []
}
```


```java
public GearsBuilder<T> foreach​(
    gears.operations.ForeachOperation<T> foreach)
```

Defines a set of operations to run for each record in the pipe.

## Parameters

| Name | Type | Description |
|------|------|-------------|
| foreach | ForeachOperation<T> | The set of operations to run for each record |

## Returns

Returns a GearsBuilder object with a new template type.

## Example

For each person hash, add a new full_name field that combines their first and last names:

```java
GearsBuilder.CreateGearsBuilder(reader).foreach(r->{
    String firstName = r.getHashVal().get("first_name");
    String lastName = r.getHashVal().get("last_name");
   	r.getHashVal().put("full_name", firstName + lastName);
}); 
```
