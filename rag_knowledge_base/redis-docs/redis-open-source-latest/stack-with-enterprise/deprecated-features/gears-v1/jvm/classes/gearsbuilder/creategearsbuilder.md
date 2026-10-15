# CreateGearsBuilder

```json metadata
{
  "schema_version": 2,
  "title": "CreateGearsBuilder",
  "description": "Creates a new GearsBuilder object.",
  "categories": ["docs","operate","stack"],
  "tableOfContents": {"sections":[{"id":"parameters","title":"Parameters"},{"id":"returns","title":"Returns"},{"id":"example","title":"Example"}]}

,
  "codeExamples": []
}
```


```java
public static <I extends java.io.Serializable> GearsBuilder<I> CreateGearsBuilder​(
    gears.readers.BaseReader<I> reader)

public static <I extends java.io.Serializable> GearsBuilder<I> CreateGearsBuilder​(
    gears.readers.BaseReader<I> reader, 
    java.lang.String desc)
```

Creates a new `GearsBuilder` object. Use this function instead of a `GearsBuilder` constructor to avoid type warnings.

## Parameters

Type Parameters:

| Name | Description |
|------|-------------|
| I | The template type of the returned builder. The reader determines the type. |

Parameters:

| Name | Type | Description |
|------|------|-------------|
| desc | string | The description |
| reader | BaseReader<I> | The pipe reader |

## Returns

Returns a new GearsBuilder object.

## Example

```java
GearsBuilder.CreateGearsBuilder(reader);
```
