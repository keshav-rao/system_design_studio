# Run

```json metadata
{
  "schema_version": 2,
  "title": "Run",
  "description": "Runs the pipeline of functions immediately.",
  "categories": ["docs","operate","stack"],
  "tableOfContents": {"sections":[{"id":"parameters","title":"Parameters"},{"id":"returns","title":"Returns"},{"id":"example","title":"Example"}]}

,
  "codeExamples": []
}
```


```java
public void run()

public void run​(boolean jsonSerialize, boolean collect)
```

Runs the pipeline of functions immediately upon execution. It will only run once.

## Parameters

| Name | Type | Description |
|------|------|-------------|
| collect | boolean | Whether or not to collect the results from the entire cluster before returning them |
| jsonSerialize | boolean | Whether or not to serialize the results to JSON before returning them |

## Returns

None

## Example

```java
GearsBuilder.CreateGearsBuilder(reader).run();
```
