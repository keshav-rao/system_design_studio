# Prepare source databases

```json metadata
{
  "schema_version": 2,
  "title": "Prepare source databases",
  "description": "Enable CDC features in your source databases",
  "categories": ["docs","integrate","rs","rdi"],
  "group": "di",
  "tableOfContents": {"sections":[]}

,
  "codeExamples": []
}
```


Each database uses a different mechanism to track changes to its data and
generally, these mechanisms are not switched on by default.
RDI's Debezium collector uses these mechanisms for change data capture (CDC),
so you must prepare each source database before you can use it with RDI.

A pipeline can capture from more than one source database, and you must prepare each of them
separately. Follow the page for each source's database type. See
[Multiple sources in one pipeline](https://redis.io/docs/latest/integrate/redis-data-integration/data-pipelines/multiple-sources)
to learn how to configure several sources in one pipeline.

RDI supports the following source databases:

| Database | Versions | AWS RDS  Versions | GCP SQL Versions |
| :-- | :-- | :-- | :-- |
| Oracle | 19c, 21c, 23ai (LogMiner only) | 19c, 21c | - |
| MariaDB | 10.5, 11.4.x, 11.7.x | 10.4 to 10.11 | - |
| MongoDB | 6.0, 7.0, 8.0 | - | - |
| MySQL | 5.7, 8.0.x, 8.4.x, 9.0, 9.1 | 8.0.x | 8.0 |
| PostgreSQL | 10, 11, 12, 13, 14, 15, 16, 17, 18 | 11, 12, 13, 14, 15, 16, 17, 18 | 15 |
| Supabase (uses PostgreSQL) | 10, 11, 12, 13, 14, 15, 16, 17  | - | - |
| SQL Server | 2017, 2019, 2022 | 2016, 2017, 2019, 2022 | 2019 |
| Spanner | - | - | All versions |
| AlloyDB for PostgreSQL | 14.2, 15.7 | - | 14.2, 15.7 |
| AWS Aurora/PostgreSQL | 15 | 15 | - |
| Neon | 14, 15, 16, 17 | - | - |
| Snowflake (preview) | - | - | - |


The pages in this section give detailed instructions to get your source
database ready for Debezium to use:

