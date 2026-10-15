# rladmin cluster change_password_hashing_algorithm

```json metadata
{
  "schema_version": 2,
  "title": "rladmin cluster change_password_hashing_algorithm",
  "description": "Changes the password hashing algorithm.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[]}

,
  "codeExamples": []
}
```


Changes the password hashing algorithm for the entire cluster. When you change the hashing algorithm, it rehashes the administrator password and passwords for all users, including default users.

```sh
rladmin cluster change_password_hashing_algorithm <algorithm>
```

### Parameters

| Parameter | Type/Value | Description |
|-----------|------------|-------------|
| algorithm | SHA-256<br />PBKDF2 | Change to the specified hashing algorithm. The default hashing algorithm is `SHA-256`. |

### Returns

Reports whether the algorithm change succeeded or an error occurred.

### Example

```sh
$ rladmin cluster change_password_hashing_algorithm PBKDF2
Please confirm changing the password hashing algorithm
Please confirm [Y/N]: y
Algorithm changed
```

