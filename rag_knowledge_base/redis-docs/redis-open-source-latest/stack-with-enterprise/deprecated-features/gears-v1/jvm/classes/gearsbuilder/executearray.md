# ExecuteArray

```json metadata
{
  "schema_version": 2,
  "title": "ExecuteArray",
  "description": "Runs a Redis command.",
  "categories": ["docs","operate","stack"],
  "tableOfContents": {"sections":[{"id":"parameters","title":"Parameters"},{"id":"returns","title":"Returns"},{"id":"example","title":"Example"}]}

,
  "codeExamples": []
}
```


```java
public static native java.lang.Object executeArray(
    java.lang.String[] command)
```

Runs a Redis command. It accepts an array of strings, which represents the command to execute.

## Parameters

| Name | Type | Description |
|------|------|-------------|
| command | array of strings | A Redis command |

## Returns

Returns the command result. It could be a string or an array of strings, depending on the command.

## Example

```java
GearsBuilder.executeArray(new String[]{"SET", "age:maximum", "100"});
```
