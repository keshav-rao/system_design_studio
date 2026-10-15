# Redis Cloud changelog (December 2023)

```json metadata
{
  "schema_version": 2,
  "title": "Redis Cloud changelog (December 2023)",
  "description": "New features, enhancements, and other changes added to Redis Cloud during December 2023.",
  "categories": ["docs","operate","rc"],
  "tableOfContents": {"sections":[{"children":[{"id":"active-active-json-support","title":"Active-Active JSON support"},{"id":"mutual-tls-enhancements","title":"Mutual TLS enhancements"}],"id":"new-features","title":"New features"}]}

,
  "codeExamples": []
}
```


## New features

### Active-Active JSON support

[Active-Active databases](https://redis.io/docs/latest/operate/rc/databases/active-active) on Redis Cloud now support the [JSON](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/json) data type.

See [Create an Active-Active subscription](https://redis.io/docs/latest/operate/rc/databases/active-active/create-active-active-database) to learn how to create an Active-Active subscription.

### Mutual TLS enhancements

Databases that support [Transport layer security (TLS)](https://redis.io/docs/latest/operate/rc/security/database-security/tls-ssl) now support multiple client certificates for use with mutual TLS. This makes it easier to rotate client certificates outside of a maintenance window. In addition, you can now provide a client Certificate Authority chain to trust any leaf certificate it signed for more flexibility.

See [Transport layer security (TLS)](https://redis.io/docs/latest/operate/rc/security/database-security/tls-ssl) to learn how to enable TLS. 


