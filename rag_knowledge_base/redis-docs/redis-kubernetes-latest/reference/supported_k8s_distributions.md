# Supported Kubernetes distributions

```json metadata
{
  "schema_version": 2,
  "title": "Supported Kubernetes distributions",
  "description": "Support matrix for the current Redis Software for Kubernetes operator",
  "categories": ["docs","operate","kubernetes"],
  "tableOfContents": {"sections":[{"children":[{"id":"latest-release","title":"Latest release"},{"id":"version-history","title":"Version history"}],"id":"kubernetes-version-support","title":"Kubernetes version support"}]}

,
  "codeExamples": []
}
```


## Kubernetes version support

Redis Software for Kubernetes is compatible with [CNCF-conformant](https://www.cncf.io/training/certification/software-conformance/) Kubernetes platforms. The operator follows standard Kubernetes APIs and practices and is designed to run consistently across certified Kubernetes environments.

Redis tests Redis Software for Kubernetes on the following platforms:

- Red Hat OpenShift
- Google Kubernetes Engine (GKE)
- Rancher Kubernetes Engine (RKE)
- Azure Kubernetes Service (AKS)
- Amazon Elastic Kubernetes Service (EKS)

Redis also supports other CNCF-conformant distributions that run a supported Kubernetes version, even without explicit testing.

The tables below use the following status icons:

<span title="Check mark icon">&#x2705;</span> Supported – This Kubernetes version is supported for this operator version.

<span title="Deprecation warning">&#x26a0;&#xfe0f;</span> Deprecated – Support for this Kubernetes version will be removed in a future release.

<span title="X icon">&#x274c;</span> End of life – No longer supported.

### Latest release

Operator release **8.2.0-12** supports the following Kubernetes and OpenShift versions.

| OpenShift | Kubernetes | Support status |
|---|---|---|
| &mdash; | 1.36 | <span title="Supported">&#x2705;</span> Supported |
| 4.22 | 1.35 | <span title="Supported">&#x2705;</span> Supported |
| 4.21 | 1.34 | <span title="Supported">&#x2705;</span> Supported |
| 4.20 | 1.33 | <span title="Supported">&#x2705;</span> Supported |
| 4.19 | 1.32 | <span title="Deprecation warning">&#x26a0;&#xfe0f;</span> Deprecated |

### Version history

The following table lists the Kubernetes versions supported by every operator version. Operator versions run from newest (left) to oldest (right).

#### Table part 1 of 6, rows 1-10

|  | Redis operator | **<nobr>8.2.0-12</nobr>** | **<nobr>8.0.20-21</nobr>** | **<nobr>8.0.18-11</nobr>** | **<nobr>8.0.10-15</nobr>** | **<nobr>8.0.6-6</nobr>** |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | July 2026 | May 2026 | March 2026 | Jan 2026 | Dec 2025 |
| OpenShift | Kubernetes |  |  |  |  |  |
| &mdash; | 1.36 | <span title="Supported">&#x2705;</span> |  |  |  |  |
| 4.22 | 1.35 | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |  |
| 4.21 | 1.34 | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| 4.20 | 1.33 | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| 4.19 | 1.32 | <span title="Deprecation warning">&#x26a0;&#xfe0f;</span> | <span title="Deprecation warning">&#x26a0;&#xfe0f;</span> | <span title="Deprecation warning">&#x26a0;&#xfe0f;</span> | <span title="Deprecation warning">&#x26a0;&#xfe0f;</span> | <span title="Deprecation warning">&#x26a0;&#xfe0f;</span> |
| 4.18 | 1.31 | <span title="X icon">&#x274c;</span> | <span title="Deprecation warning">&#x26a0;&#xfe0f;</span> | <span title="Deprecation warning">&#x26a0;&#xfe0f;</span> | <span title="Deprecation warning">&#x26a0;&#xfe0f;</span> | <span title="Deprecation warning">&#x26a0;&#xfe0f;</span> |
| 4.17 | 1.30 |  |  |  |  |  |
| 4.16 | 1.29 |  |  |  |  |  |

#### Table part 1 of 6, rows 11-20

|  | Redis operator | **<nobr>8.2.0-12</nobr>** | **<nobr>8.0.20-21</nobr>** | **<nobr>8.0.18-11</nobr>** | **<nobr>8.0.10-15</nobr>** | **<nobr>8.0.6-6</nobr>** |
| --- | --- | --- | --- | --- | --- | --- |
| 4.15 | 1.28 |  |  |  |  |  |
| 4.14 | 1.27 |  |  |  |  |  |
| 4.13 | 1.26 |  |  |  |  |  |
| 4.12 | 1.25 |  |  |  |  |  |
| 4.11 | 1.24 |  |  |  |  |  |
| 4.10 | 1.23 |  |  |  |  |  |
| 4.09 | 1.22 |  |  |  |  |  |
| 4.08 | 1.21 |  |  |  |  |  |
| 4.07 | 1.20 |  |  |  |  |  |
| 4.06 | 1.19 |  |  |  |  |  |

#### Table part 1 of 6, rows 21-23

|  | Redis operator | **<nobr>8.2.0-12</nobr>** | **<nobr>8.0.20-21</nobr>** | **<nobr>8.0.18-11</nobr>** | **<nobr>8.0.10-15</nobr>** | **<nobr>8.0.6-6</nobr>** |
| --- | --- | --- | --- | --- | --- | --- |
| 4.05 | 1.18 |  |  |  |  |  |
| 4.04 | 1.17 |  |  |  |  |  |
| 4.03 | 1.16 |  |  |  |  |  |

#### Table part 2 of 6, rows 1-10

|  | **<nobr>8.0.2-2</nobr>** | **<nobr>7.22.2-21</nobr>** | **<nobr>7.22.0-15</nobr>** | **<nobr>7.22.0-7</nobr>** | **<nobr>7.8.6-1</nobr>** | **<nobr>7.8.4-9</nobr>** |
| --- | --- | --- | --- | --- | --- | --- |
|  | Oct 2025 | Oct 2025 | July 2025 | April 2025 | March 2025 | March 2025 |
| OpenShift |  |  |  |  |  |  |
| &mdash; |  |  |  |  |  |  |
| 4.22 |  |  |  |  |  |  |
| 4.21 | <span title="Supported">&#x2705;</span> |  |  |  |  |  |
| 4.20 | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |  |  |  |
| 4.19 | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |  |
| 4.18 | <span title="Deprecation warning">&#x26a0;&#xfe0f;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| 4.17 | <span title="X icon">&#x274c;</span> | <span title="Deprecation warning">&#x26a0;&#xfe0f;</span> | <span title="Deprecation warning">&#x26a0;&#xfe0f;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| 4.16 |  |  |  | <span title="X icon">&#x274c;</span> | <span title="Deprecation warning">&#x26a0;&#xfe0f;</span> | <span title="Supported">&#x2705;</span> |

#### Table part 2 of 6, rows 11-20

|  | **<nobr>8.0.2-2</nobr>** | **<nobr>7.22.2-21</nobr>** | **<nobr>7.22.0-15</nobr>** | **<nobr>7.22.0-7</nobr>** | **<nobr>7.8.6-1</nobr>** | **<nobr>7.8.4-9</nobr>** |
| --- | --- | --- | --- | --- | --- | --- |
| 4.15 |  |  |  | <span title="X icon">&#x274c;</span> | <span title="Deprecation warning">&#x26a0;&#xfe0f;</span> | <span title="Supported">&#x2705;</span> |
| 4.14 |  |  |  |  |  | <span title="X icon">&#x274c;</span> |
| 4.13 |  |  |  |  |  |  |
| 4.12 |  |  |  |  |  |  |
| 4.11 |  |  |  |  |  |  |
| 4.10 |  |  |  |  |  |  |
| 4.09 |  |  |  |  |  |  |
| 4.08 |  |  |  |  |  |  |
| 4.07 |  |  |  |  |  |  |
| 4.06 |  |  |  |  |  |  |

#### Table part 2 of 6, rows 21-23

|  | **<nobr>8.0.2-2</nobr>** | **<nobr>7.22.2-21</nobr>** | **<nobr>7.22.0-15</nobr>** | **<nobr>7.22.0-7</nobr>** | **<nobr>7.8.6-1</nobr>** | **<nobr>7.8.4-9</nobr>** |
| --- | --- | --- | --- | --- | --- | --- |
| 4.05 |  |  |  |  |  |  |
| 4.04 |  |  |  |  |  |  |
| 4.03 |  |  |  |  |  |  |

#### Table part 3 of 6, rows 1-10

|  | **<nobr>7.8.4-8</nobr>** | **<nobr>7.8.2-6</nobr>** | **<nobr>7.4.6-2</nobr>** | **<nobr>7.4.2-12</nobr>** | **<nobr>7.4.2-2</nobr>** | **<nobr>7.2.4-12</nobr>** |
| --- | --- | --- | --- | --- | --- | --- |
|  | Feb 2025 | Nov 2024 | July 2024 | May 2024 | March 2024 | Dec 2023 |
| OpenShift |  |  |  |  |  |  |
| &mdash; |  |  |  |  |  |  |
| 4.22 |  |  |  |  |  |  |
| 4.21 |  |  |  |  |  |  |
| 4.20 |  |  |  |  |  |  |
| 4.19 |  |  |  |  |  |  |
| 4.18 | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |  |  |  |  |
| 4.17 | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |  |  |  |
| 4.16 | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |  |

#### Table part 3 of 6, rows 11-20

|  | **<nobr>7.8.4-8</nobr>** | **<nobr>7.8.2-6</nobr>** | **<nobr>7.4.6-2</nobr>** | **<nobr>7.4.2-12</nobr>** | **<nobr>7.4.2-2</nobr>** | **<nobr>7.2.4-12</nobr>** |
| --- | --- | --- | --- | --- | --- | --- |
| 4.15 | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| 4.14 | <span title="X icon">&#x274c;</span> | <span title="X icon">&#x274c;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| 4.13 |  |  | <span title="Deprecation warning">&#x26a0;&#xfe0f;</span> | <span title="Deprecation warning">&#x26a0;&#xfe0f;</span> | <span title="Deprecation warning">&#x26a0;&#xfe0f;</span> | <span title="Supported">&#x2705;</span> |
| 4.12 |  |  |  |  | <span title="X icon">&#x274c;</span> | <span title="Supported">&#x2705;</span> |
| 4.11 |  |  |  |  | <span title="X icon">&#x274c;</span> | <span title="Supported">&#x2705;</span> |
| 4.10 |  |  |  |  |  |  |
| 4.09 |  |  |  |  |  |  |
| 4.08 |  |  |  |  |  |  |
| 4.07 |  |  |  |  |  |  |
| 4.06 |  |  |  |  |  |  |

#### Table part 3 of 6, rows 21-23

|  | **<nobr>7.8.4-8</nobr>** | **<nobr>7.8.2-6</nobr>** | **<nobr>7.4.6-2</nobr>** | **<nobr>7.4.2-12</nobr>** | **<nobr>7.4.2-2</nobr>** | **<nobr>7.2.4-12</nobr>** |
| --- | --- | --- | --- | --- | --- | --- |
| 4.05 |  |  |  |  |  |  |
| 4.04 |  |  |  |  |  |  |
| 4.03 |  |  |  |  |  |  |

#### Table part 4 of 6, rows 1-10

|  | **<nobr>7.2.4-7</nobr>** | **<nobr>7.2.4-2</nobr>** | **<nobr>6.4.2-8</nobr>** | **<nobr>6.4.2-6</nobr>** | **<nobr>6.4.2-5</nobr>** | **<nobr>6.4.2-4</nobr>** |
| --- | --- | --- | --- | --- | --- | --- |
|  | Oct 2023 | Aug 2023 | July 2023 | June 2023 | April 2023 | March 2023 |
| OpenShift |  |  |  |  |  |  |
| &mdash; |  |  |  |  |  |  |
| 4.22 |  |  |  |  |  |  |
| 4.21 |  |  |  |  |  |  |
| 4.20 |  |  |  |  |  |  |
| 4.19 |  |  |  |  |  |  |
| 4.18 |  |  |  |  |  |  |
| 4.17 |  |  |  |  |  |  |
| 4.16 |  |  |  |  |  |  |

#### Table part 4 of 6, rows 11-20

|  | **<nobr>7.2.4-7</nobr>** | **<nobr>7.2.4-2</nobr>** | **<nobr>6.4.2-8</nobr>** | **<nobr>6.4.2-6</nobr>** | **<nobr>6.4.2-5</nobr>** | **<nobr>6.4.2-4</nobr>** |
| --- | --- | --- | --- | --- | --- | --- |
| 4.15 |  |  |  |  |  |  |
| 4.14 | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |  |  |
| 4.13 | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| 4.12 | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| 4.11 | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| 4.10 |  | <span title="X icon">&#x274c;</span> | <span title="Deprecation warning">&#x26a0;&#xfe0f;</span> | <span title="Deprecation warning">&#x26a0;&#xfe0f;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| 4.09 |  |  |  | <span title="X icon">&#x274c;</span> | <span title="Deprecation warning">&#x26a0;&#xfe0f;</span> | <span title="Deprecation warning">&#x26a0;&#xfe0f;</span> |
| 4.08 |  |  |  |  |  |  |
| 4.07 |  |  |  |  |  |  |
| 4.06 |  |  |  |  |  |  |

#### Table part 4 of 6, rows 21-23

|  | **<nobr>7.2.4-7</nobr>** | **<nobr>7.2.4-2</nobr>** | **<nobr>6.4.2-8</nobr>** | **<nobr>6.4.2-6</nobr>** | **<nobr>6.4.2-5</nobr>** | **<nobr>6.4.2-4</nobr>** |
| --- | --- | --- | --- | --- | --- | --- |
| 4.05 |  |  |  |  |  |  |
| 4.04 |  |  |  |  |  |  |
| 4.03 |  |  |  |  |  |  |

#### Table part 5 of 6, rows 1-10

|  | **<nobr>6.2.18-41</nobr>** | **<nobr>6.2.18-3</nobr>** | **<nobr>6.2.12-1</nobr>** | **<nobr>6.2.10-45</nobr>** | **<nobr>6.2.10-34</nobr>** | **<nobr>6.2.10-4</nobr>** |
| --- | --- | --- | --- | --- | --- | --- |
|  | Jan 2023 | Nov 2022 | Sept 2022 | July 2022 | May 2022 | March 2022 |
| OpenShift |  |  |  |  |  |  |
| &mdash; |  |  |  |  |  |  |
| 4.22 |  |  |  |  |  |  |
| 4.21 |  |  |  |  |  |  |
| 4.20 |  |  |  |  |  |  |
| 4.19 |  |  |  |  |  |  |
| 4.18 |  |  |  |  |  |  |
| 4.17 |  |  |  |  |  |  |
| 4.16 |  |  |  |  |  |  |

#### Table part 5 of 6, rows 11-20

|  | **<nobr>6.2.18-41</nobr>** | **<nobr>6.2.18-3</nobr>** | **<nobr>6.2.12-1</nobr>** | **<nobr>6.2.10-45</nobr>** | **<nobr>6.2.10-34</nobr>** | **<nobr>6.2.10-4</nobr>** |
| --- | --- | --- | --- | --- | --- | --- |
| 4.15 |  |  |  |  |  |  |
| 4.14 |  |  |  |  |  |  |
| 4.13 |  |  |  |  |  |  |
| 4.12 | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |  |  |  |  |
| 4.11 | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |  |  |
| 4.10 | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |  |
| 4.09 | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| 4.08 |  |  | <span title="X icon">&#x274c;</span> | <span title="Deprecation warning">&#x26a0;&#xfe0f;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| 4.07 |  |  |  | <span title="X icon">&#x274c;</span> | <span title="Deprecation warning">&#x26a0;&#xfe0f;</span> | <span title="Supported">&#x2705;</span> |
| 4.06 |  |  |  | <span title="X icon">&#x274c;</span> | <span title="Deprecation warning">&#x26a0;&#xfe0f;</span> | <span title="Supported">&#x2705;</span> |

#### Table part 5 of 6, rows 21-23

|  | **<nobr>6.2.18-41</nobr>** | **<nobr>6.2.18-3</nobr>** | **<nobr>6.2.12-1</nobr>** | **<nobr>6.2.10-45</nobr>** | **<nobr>6.2.10-34</nobr>** | **<nobr>6.2.10-4</nobr>** |
| --- | --- | --- | --- | --- | --- | --- |
| 4.05 |  |  |  |  |  | <span title="Supported">&#x2705;</span> |
| 4.04 |  |  |  |  |  |  |
| 4.03 |  |  |  |  |  |  |

#### Table part 6 of 6, rows 1-10

|  | **<nobr>6.2.8-15</nobr>** | **<nobr>6.2.8-11</nobr>** | **<nobr>6.2.8-2</nobr>** | **<nobr>6.2.4-1</nobr>** |
| --- | --- | --- | --- | --- |
|  | Jan 2022 | Jan 2022 | Nov 2021 | Sept 2021 |
| OpenShift |  |  |  |  |
| &mdash; |  |  |  |  |
| 4.22 |  |  |  |  |
| 4.21 |  |  |  |  |
| 4.20 |  |  |  |  |
| 4.19 |  |  |  |  |
| 4.18 |  |  |  |  |
| 4.17 |  |  |  |  |
| 4.16 |  |  |  |  |

#### Table part 6 of 6, rows 11-20

|  | **<nobr>6.2.8-15</nobr>** | **<nobr>6.2.8-11</nobr>** | **<nobr>6.2.8-2</nobr>** | **<nobr>6.2.4-1</nobr>** |
| --- | --- | --- | --- | --- |
| 4.15 |  |  |  |  |
| 4.14 |  |  |  |  |
| 4.13 |  |  |  |  |
| 4.12 |  |  |  |  |
| 4.11 |  |  |  |  |
| 4.10 |  |  |  |  |
| 4.09 | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |  |  |
| 4.08 | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| 4.07 | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| 4.06 | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |

#### Table part 6 of 6, rows 21-23

|  | **<nobr>6.2.8-15</nobr>** | **<nobr>6.2.8-11</nobr>** | **<nobr>6.2.8-2</nobr>** | **<nobr>6.2.4-1</nobr>** |
| --- | --- | --- | --- | --- |
| 4.05 | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| 4.04 |  |  | <span title="X icon">&#x274c;</span> | <span title="Deprecation warning">&#x26a0;&#xfe0f;</span> |
| 4.03 |  |  | <span title="X icon">&#x274c;</span> | <span title="Deprecation warning">&#x26a0;&#xfe0f;</span> |



