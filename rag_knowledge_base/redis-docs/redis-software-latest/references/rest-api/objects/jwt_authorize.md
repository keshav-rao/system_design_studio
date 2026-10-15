# JWT authorize object

```json metadata
{
  "schema_version": 2,
  "title": "JWT authorize object",
  "description": "An object for user authentication or a JW token refresh request",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[]}

,
  "codeExamples": []
}
```


An API object for user authentication or a JW token refresh request.

| Name | Type/Value | Description |
|------|------------|-------------|
| password | string | The user’s password (required) |
| ttl | integer (range: 1-86400) (default: 300) | Time to live - The amount of time in seconds the token will be valid |
| username | string | The user’s username (required) |

