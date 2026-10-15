# RedisJSON 2.2 release notes

```json metadata
{
  "schema_version": 2,
  "title": "RedisJSON 2.2 release notes",
  "description": "Preview of Active-Active support for JSON.",
  "categories": ["docs","operate","stack"],
  "tableOfContents": {"sections":[{"id":"requirements","title":"Requirements"},{"children":[{"id":"headlines","title":"Headlines"},{"id":"details","title":"Details"}],"id":"v220-july-2022","title":"v2.2.0 (July 2022)"}]}

,
  "codeExamples": []
}
```

## Requirements

RedisJSON v2.2.0 requires:

- Minimum Redis compatibility version (database): 6.0.0
- Minimum Redis Enterprise Software version (cluster): 6.2.18

## v2.2.0 (July 2022)

A preview of RedisJSON 2.2 is available for Free and Fixed subscription plans in Redis Cloud.

### Headlines

This release adds support for the JSON data structure as a CRDT (Conflict-free Replicated Data Type) when used with Redis Enterprise [Active-Active databases](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/json/active-active).

Active-Active JSON requires Redis Enterprise Software v6.2.12. Contact your account manager or support to access the preview of RedisJSON 2.2. 

### Details

- Enhancements:

  - [#758](https://github.com/RedisJSON/RedisJSON/pull/758) Add support for [`COPY`](https://redis.io/docs/latest/commands/copy)

