# Redis Enterprise for Kubernetes 7.8.6 release notes

```json metadata
{
  "schema_version": 2,
  "title": "Redis Enterprise for Kubernetes 7.8.6 release notes",
  "description": "Releases with support for Redis Enterprise Software 7.8.6",
  "categories": ["docs","operate","kubernetes"],
  "tableOfContents": {"sections":[{"id":"detailed-release-notes","title":"Detailed release notes"},{"id":"breaking-changes","title":"Breaking changes"},{"id":"rhel9-based-image","title":"RHEL9-based image"},{"id":"known-limitations","title":"Known limitations"}]}

,
  "codeExamples": []
}
```


Redis Enterprise for Kubernetes 7.8.6 includes bug fixes, enhancements, and support for Redis Enterprise Software. The latest release is 7.8.6-22 with support for Redis Enterprise Software version 7.8.6-331.

## Detailed release notes


| Version (Release date) | Major changes |
| --- | --- |
| [7.8.6-22 (October 2026)](https://redis.io/docs/latest/operate/kubernetes/release-notes/7-8-6-releases/7-8-6-22-october2026/) | A maintenance release that includes support for Redis Software 7.8.6-331. |
| [7.8.6-20 (September 2026)](https://redis.io/docs/latest/operate/kubernetes/release-notes/7-8-6-releases/7-8-6-20-september2026/) | A maintenance release that includes support for Redis Software 7.8.6-315. |
| [7.8.6-19 (August 2026)](https://redis.io/docs/latest/operate/kubernetes/release-notes/7-8-6-releases/7-8-6-19-august2026/) | A maintenance release that includes support for Redis Software 7.8.6-303. |
| [7.8.6-16 (July 2026)](https://redis.io/docs/latest/operate/kubernetes/release-notes/7-8-6-releases/7-8-6-16-july2026/) | A maintenance release that includes support for Redis Software 7.8.6-286. |
| [7.8.6-15 (May 2026)](https://redis.io/docs/latest/operate/kubernetes/release-notes/7-8-6-releases/7-8-6-15-may2026/) | A maintenance release that includes support for Redis Software 7.8.6-263. |
| [7.8.6-14 (April 2026)](https://redis.io/docs/latest/operate/kubernetes/release-notes/7-8-6-releases/7-8-6-14-april2026/) | A maintenance release that includes support for Redis Software 7.8.6-260. |
| [7.8.6-13 (March 2026)](https://redis.io/docs/latest/operate/kubernetes/release-notes/7-8-6-releases/7-8-6-13-march2026/) | A maintenance release that includes support for Redis Software 7.8.6-256. |
| [7.8.6-11 (February 2026)](https://redis.io/docs/latest/operate/kubernetes/release-notes/7-8-6-releases/7-8-6-11-feb2026/) | A maintenance release that includes support for Redis Software 7.8.6-253. |
| [7.8.6-8 (October 2025)](https://redis.io/docs/latest/operate/kubernetes/release-notes/7-8-6-releases/7-8-6-8-october2025/) | A maintenance release that includes support for Redis Software 7.8.6-207. |
| [7.8.6-5 (August 2025)](https://redis.io/docs/latest/operate/kubernetes/release-notes/7-8-6-releases/7-8-6-5-august2025/) | A maintenance release that includes support for Redis Software 7.8.6-152. |
| [7.8.6-3 (June 2025)](https://redis.io/docs/latest/operate/kubernetes/release-notes/7-8-6-releases/7-8-6-3-june2025/) | A maintenance release that includes support for Redis Software 7.8.6-119. |
| [7.8.6-2 (June 2025)](https://redis.io/docs/latest/operate/kubernetes/release-notes/7-8-6-releases/7-8-6-2-june2025/) | A maintenance release that includes support for Redis Software 7.8.6-95. |
| [7.8.6-1 (May 2025)](https://redis.io/docs/latest/operate/kubernetes/release-notes/7-8-6-releases/7-8-6-1-may2025/) | A maintenance release that includes support for Redis Software 7.8.6-60. |
| [7.8.6-1 (April 2025)](https://redis.io/docs/latest/operate/kubernetes/release-notes/7-8-6-releases/7-8-6-1-april2025/) | A maintenance release that includes support for Redis Software 7.8.6-36. |
| [7.8.6-1 (March 2025)](https://redis.io/docs/latest/operate/kubernetes/release-notes/7-8-6-releases/7-8-6-1-march2025/) | Feature release including enhancements, bug fixes, platform updates, and support for Redis Software 7.8.6-13 |


## Breaking changes

Customers who use load balancers for Active-Active replication endpoints and rely on the change introduced in RED-113626 (or the workaround described in the ticket) must set the spec.externalReplicationPort field in REAADB after upgrading. Otherwise, replication will fail (RED-149374).

## RHEL9-based image

As of version 7.8.2-6, Redis Enterprise images are based on Red Hat Enterprise Linux 9 (RHEL9). This means upgrades require:

- [Cluster version of 7.4.2-2 or later](https://redis.io/docs/latest/operate/kubernetes/7.4.6/upgrade/).
- Database version 7.2 or later.
- RHEL9 compatible binaries for any modules you need.

For detailed steps, see the relevant upgrade page:

- [OpenShift CLI](https://redis.io/docs/latest/operate/kubernetes/upgrade/openshift-cli)
- [OpenShift OperatorHub](https://redis.io/docs/latest/operate/kubernetes/upgrade/upgrade-olm)
- [Kubernetes](https://redis.io/docs/latest/operate/kubernetes/upgrade/upgrade-redis-cluster)

## Known limitations

- **Only upgrades from 7.4.2-2 and later are supported.** If you are using an earlier version, install 7.4.2-2 before upgrading to 7.8.2-6 or later.

- **When changing the REDB field `spec.modulesList`, version might be upgraded to latest, even if a different version is specified.** To prevent the upgrade to latest, set  `spec.upgradeSpec.setModuleToLatest` to `false` before upgrading to 7.8.2-6.

- **Missing endpoint for admission endpoint (rare) (RED-119469)** Restart the operator pod.

- **The REDB "redisVersion" field can’t be used for memcached databases(RED-119152)**

- **When modifying the database suffix for an Active-Active database, while the service-rigger is in a terminating state, the services-rigger will delete and create the ingress or route resources in a loop (RED-107687)** Wait until the services rigger pod has finished to terminate it.

- **REAADB changes might fail with "gateway timeout" errors, mostly on OpenShift (RED-103048)** Retry the operation.

- **Creating two databases with the same name directly on Redis Enterprise software will cause the service to be deleted and the database will not be available (RED-99997)** Avoid duplicating database names. Database creation via K8s has validation in place to prevent this.

- **Installing the operator bundle produces warning: `Warning: would violate PodSecurity "restricted: v1.24"` (RED-97381)** Ignore the warning. This issue is documented as benign on official Red Hat documentation.

- **RERC resources must have a unique name (RED-96302)** The string "rec-name"/"rec-namespace" must be different from all other participating clusters in the Active-Active database.

- **Admission is not blocking REAADB with `shardCount` which exceeds license quota (RED-96301)** Fix the problems with the REAADB and reapply.

- **Active-Active controller only supports global database options. Configuration specific to location is not supported (RED-86490)**

- **Active-Active setup removal might keep services or routes undeleted (RED-77752)** Delete services or routes manually if you encounter this problem.

- **`autoUpgrade` set to `true` can cause unexpected bdb upgrades when `redisUpgradePolicy` is set to `true` (RED-72351)** Contact support if your deployment is impacted.

- **Following the previous quick start guide version causes issues with creating an REDB due to unrecognized memory field name (RED-69515)** The workaround is to use the newer (current) revision of Deploy Redis Enterprise Software for Kubernetes.

- **PVC size issues when using decimal value in spec (RED-62132)** Make sure you use integer values for the PVC size.

- **REC might report error states on initial startup (RED-61707)** There is no workaround at this time except to ignore the errors.

- **Hashicorp Vault integration - no support for Gesher (RED-55080)** There is no workaround for this issue. Gesher support has been deprecated.

- **REC clusters fail to start on Kubernetes clusters with unsynchronized clocks (RED-47254)** When REC clusters are deployed on Kubernetes clusters without synchronized clocks, the REC cluster does not start correctly. The fix is to use NTP to synchronize the underlying K8s nodes.

- **Deleting an OpenShift project with an REC deployed may hang (RED-47192)** When an REC cluster is deployed in a project (namespace) and has REDB resources, the REDB resources must be deleted first before the REC can be deleted. Therefore, until the REDB resources are deleted, the project deletion will hang. The fix is to delete the REDB resources first and the REC second. Then, you can delete the project.

- **Clusters must be named 'rec' in OLM-based deployments (RED-39825)** In OLM-deployed operators, the deployment of the cluster will fail if the name is not "rec". When the operator is deployed via the OLM, the security context constraints (scc) are bound to a specific service account name (namely, "rec"). The workaround is to name the cluster "rec".

- **Readiness probe incorrect on failures (RED-39300)** STS Readiness probe does not mark a node as "not ready" when running `rladmin status` on node failure.

- **Internal DNS and Kubernetes DNS may have conflicts (RED-37462)** DNS conflicts are possible between the cluster `mdns_server` and the K8s DNS. This only impacts DNS resolution from within cluster nodes for Kubernetes DNS names.

- **K8s-based 5.4.10 clusters seem to negatively affect existing 5.4.6 clusters (RED-37233)** Upgrade clusters to latest version.

- **Node CPU usage is reported instead of pod CPU usage (RED-36884)** In Kubernetes, the reported node CPU usage is the usage of the Kubernetes worker node hosting the REC pod.

- **An unreachable cluster has status running (RED-32805)** When a cluster is in an unreachable state, the state remains `running` instead of triggering an error.

- **Long cluster names cause routes to be rejected  (RED-25871)** A cluster name longer than 20 characters will result in a rejected route configuration because the host part of the domain name exceeds 63 characters. The workaround is to limit the cluster name to 20 characters or fewer.

- **Cluster CR (REC) errors are not reported after invalid updates (RED-25542)** A cluster CR specification error is not reported if two or more invalid CR resources are updated in sequence.

