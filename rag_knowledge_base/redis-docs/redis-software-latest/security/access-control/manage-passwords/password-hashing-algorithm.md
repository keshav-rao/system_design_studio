# Change the password hashing algorithm

```json metadata
{
  "schema_version": 2,
  "title": "Change the password hashing algorithm",
  "description": "Change the password hashing algorithm for user passwords in a Redis Software cluster.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"id":"command-line-method","title":"Command-line method"},{"id":"rest-api-method","title":"REST API method"}]}

,
  "codeExamples": []
}
```


Redis Software securely stores all user passwords using a cryptographic hash function. The default password hashing algorithm is `SHA-256`, but `PBKDF2` is also supported as of Redis Software version 7.8.6-13.

You can change the password hashing algorithm using [`rladmin`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin) or the [REST API](https://redis.io/docs/latest/operate/rs/references/rest-api). When you change the password hashing algorithm, the cluster rehashes the administrator password and passwords for all users, including default users.

## Command-line method

To change the password hashing algorithm from the command line, run [`rladmin cluster change_password_hashing_algorithm`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/cluster/change_password_hashing_algorithm):

```sh
rladmin cluster change_password_hashing_algorithm PBKDF2
```

## REST API method

You can [change the password hashing algorithm](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/cluster/change_password_hashing_algorithm#patch-change-password-hashing-algorithm) using a REST API request:

```sh
PATCH /v1/cluster/change_password_hashing_algorithm
{ "algorithm": "PBKDF2" }
```

