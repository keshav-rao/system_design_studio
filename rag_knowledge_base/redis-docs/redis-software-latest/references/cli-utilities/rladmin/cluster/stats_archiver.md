# rladmin cluster stats_archiver

```json metadata
{
  "schema_version": 2,
  "title": "rladmin cluster stats_archiver",
  "description": "Enables/deactivates the stats archiver.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[]}

,
  "codeExamples": []
}
```


Enables or deactivates the stats archiver, which logs statistics in CSV (comma-separated values) format.

```sh
rladmin cluster stats_archiver { enabled | disabled }
```

### Parameters

| Parameter | Description |
|-----------|-------------|
| enabled | Turn on the stats archiver |
| disabled | Turn off the stats archiver |

### Returns

Returns the updated status of the stats archiver. 

### Example

```sh
$ rladmin cluster stats_archiver enabled 
Status: enabled
```
