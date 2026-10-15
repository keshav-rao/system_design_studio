# GearsFuture

```json metadata
{
  "schema_version": 2,
  "title": "GearsFuture",
  "description": "Allows asynchronous processing of records.",
  "categories": ["docs","operate","stack"],
  "tableOfContents": {"sections":[{"id":"functions","title":"Functions"}]}

,
  "codeExamples": []
}
```


The `GearsFuture` class allows asynchronous processing of records in another thread.

You can use a `GearsFuture` object with the following [`GearsBuilder`](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder) functions:

- [`asyncFilter`](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/asyncfilter)
- [`asyncForeach`](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/asyncforeach)
- [`asyncMap`](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/asyncmap)

## Functions


| Function | Description |
| --- | --- |
| [setError](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsfuture/seterror/) | Sets an error message. |
| [setResult](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsfuture/setresult/) | Sets a computation to run asynchronously. |

