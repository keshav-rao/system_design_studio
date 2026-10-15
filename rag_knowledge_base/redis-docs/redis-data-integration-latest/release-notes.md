# Release notes

```json metadata
{
  "schema_version": 2,
  "title": "Release notes",
  "description": "",
  "categories": ["docs","integrate","rs","rdi"],
  "group": "di",
  "tableOfContents": {"sections":[]}

,
  "codeExamples": []
}
```


Here's what changed recently in Redis Data Integration (RDI):


| Version (Release date) | Major changes |
| --- | --- |
| [2.0.0 (September 2026)](https://redis.io/docs/latest/integrate/redis-data-integration/release-notes/rdi-2-0-0/) | Multiple sources in one pipeline, Flink as the default processor, and simpler source mTLS configuration. Database-scoped secrets, per-source reset and cleanup, expanded API diagnostics, and security updates. |
| [1.19.1 (August 2026)](https://redis.io/docs/latest/integrate/redis-data-integration/release-notes/rdi-1-19-1/) | Improved Flink processor recovery, logging, and security. |
| [1.19.0 (July 2026)](https://redis.io/docs/latest/integrate/redis-data-integration/release-notes/rdi-1-19-0/) | New redis-di CLI for VM, Kubernetes, and Redis Cloud installations. New Redis sorted set and stream outputs for the Flink processor, expanded Snowflake configuration, and Flink processor support for offline VM installations. Improved pipeline status, secret updates, support packages, and error handling. |
| [1.18.1 (May 2026)](https://redis.io/docs/latest/integrate/redis-data-integration/release-notes/rdi-1-18-1/) | Debezium 3.5.0 upgrade with default collector image updates, Oracle connector compatibility updates, and Microsoft Entra ID authentication support. |
| [1.18.0 (April 2026)](https://redis.io/docs/latest/integrate/redis-data-integration/release-notes/rdi-1-18-0/) | New Flink-based stream processor for Kubernetes deployments (Preview), with horizontal scaling, Flink checkpointing, and significantly higher throughput. Preview for Snowflake source support for Helm installations, including multi-schema capture and system truststore support. New API v2 endpoints for DLQ inspection, flushing the target database, and CDC-readiness validation. Better deployment reliability, new validation and resource controls, and security refreshes across core images. |
| [1.16.2 (March 2026)](https://redis.io/docs/latest/integrate/redis-data-integration/release-notes/rdi-1-16-2/) | Maintenance release focusing on allowing the use of RDI with Redis Enterprise databases that have AOF disabled. |
| [1.16.1 (February 2026)](https://redis.io/docs/latest/integrate/redis-data-integration/release-notes/rdi-1-16-1/) | Maintenance release focusing on TLS certificate handling fixes and API v2 pipeline patching. Includes security hardening for the collector API through dependency upgrades (Spring Boot, Netty, Kafka clients, MySQL connector, Logback, Jetty, Spring Security, Spring Framework). |
| [1.16.0 (January 2026)](https://redis.io/docs/latest/integrate/redis-data-integration/release-notes/rdi-1-16-0/) | Enhanced disaster recovery for Cloud Spanner with Redis Active-Active, plus better performance and resilience in the Spanner collector. New RDI API v2 dry-run, info, and metrics endpoints for safer rollouts and improved observability. Improved deployment, installation, and troubleshooting, including disk space preflight checks, and broader stability fixes. |
| [1.15.1 (November 2025)](https://redis.io/docs/latest/integrate/redis-data-integration/release-notes/rdi-1-15-1/) | Fixes support package generation and masking to simplify troubleshooting and log collection. Improves processor throughput during initial sync via parallel processing and new stream tuning parameters. Adds an advanced configuration option to pass custom Java options to the Debezium collector. |
| [1.15.0 (October 2025)](https://redis.io/docs/latest/integrate/redis-data-integration/release-notes/rdi-1-15-0/) | Flink collector for Spanner enabled by default for improved user experience. Enhanced high availability with configurable leader election and standby mode. Support for sharded RDI Redis databases. Improved configuration validation and monitoring capabilities. Better resource management and security enhancements. |
| [1.14.1 (August 2025)](https://redis.io/docs/latest/integrate/redis-data-integration/release-notes/rdi-1-14-1/) | New RDI API v2 with enhanced pipeline management. Improved Oracle RAC support with configuration scaffolding. Enhanced metrics and monitoring capabilities. Better TLS/mTLS support across components. |
| [1.14.0 (August 2025)](https://redis.io/docs/latest/integrate/redis-data-integration/release-notes/rdi-1-14-0/) | New RDI API v2 with enhanced pipeline management. Improved Oracle RAC support with configuration scaffolding. Enhanced metrics and monitoring capabilities. Better TLS/mTLS support across components. |
| [1.12.3 (July 2025)](https://redis.io/docs/latest/integrate/redis-data-integration/release-notes/rdi-1-12-3/) | Fixed operator excessive CPU usage and log flooding. Fixed reset jobs not being able to pull images from private registries. |
| [1.12.2 (July 2025)](https://redis.io/docs/latest/integrate/redis-data-integration/release-notes/rdi-1-12-2/) | RDI Collector API now properly supports MariaDB. Extend adding custom labels and annotations to all resources in the RDI Helm chart. |
| [1.12.1 (June 2025)](https://redis.io/docs/latest/integrate/redis-data-integration/release-notes/rdi-1-12-1/) | Update documentation on pipelines endpoint. Fix deploy pipeline validation issues. /tables API can now group tables by schema. Fix mongo tables endpoint. Fix Oracle /metadata and /columns filters being case sensitive. |
| [1.12.0 (June 2025)](https://redis.io/docs/latest/integrate/redis-data-integration/release-notes/rdi-1-12-0/) | Enhanced CLI command for HA topology information. Automatic DLQ routing for key errors. Enhanced transformation job validation in the PATCH and POST /api/v1/pipelines endpoints. Added `xml_to_dict` transformation function. |
| [1.10.0 (May 2025)](https://redis.io/docs/latest/integrate/redis-data-integration/release-notes/rdi-1-10-0/) | Added support for MongoDB as a source, with a scaffold template and enhanced configuration validation. Implemented automatic deletion of pods affected by secret rotation. |
| [1.8.0 (May 2025)](https://redis.io/docs/latest/integrate/redis-data-integration/release-notes/rdi-1-8-0/) | Enhanced RDI operator for better pipeline orchestration, resiliency, observability and flexibility; External collector support; Labels and annotations to RDI data plane pods; Custom Debezium image; Calculated TTL for target database. |
| [1.6.7 (May 2025)](https://redis.io/docs/latest/integrate/redis-data-integration/release-notes/rdi-1-6-7/) | Installation on Kubernetes with a Helm chart. Improvements for installation on VMs. |
| [1.6.6 (April 2025)](https://redis.io/docs/latest/integrate/redis-data-integration/release-notes/rdi-1-6-6/) | Installation on Kubernetes with a Helm chart. Improvements for installation on VMs. |
| [1.6.5 (April 2025)](https://redis.io/docs/latest/integrate/redis-data-integration/release-notes/rdi-1-6-5/) | Installation on Kubernetes with a Helm chart. Improvements for installation on VMs. |
| [1.6.4 (April 2025)](https://redis.io/docs/latest/integrate/redis-data-integration/release-notes/rdi-1-6-4/) | Installation on Kubernetes with a Helm chart. Improvements for installation on VMs. |
| [1.6.3 (March 2025)](https://redis.io/docs/latest/integrate/redis-data-integration/release-notes/rdi-1-6-3/) | Installation on Kubernetes with a Helm chart. Improvements for installation on VMs. |
| [1.6.2 (March 2025)](https://redis.io/docs/latest/integrate/redis-data-integration/release-notes/rdi-1-6-2/) | Installation on Kubernetes with a Helm chart. Improvements for installation on VMs. |
| [1.6.1 (March 2025)](https://redis.io/docs/latest/integrate/redis-data-integration/release-notes/rdi-1-6-1/) | Installation on Kubernetes with a Helm chart. Improvements for installation on VMs. |
| [1.6.0 (February 2025)](https://redis.io/docs/latest/integrate/redis-data-integration/release-notes/rdi-1-6-0/) | Installation on Kubernetes with a Helm chart. Improvements for installation on VMs. |
| [1.4.4 (January 2025)](https://redis.io/docs/latest/integrate/redis-data-integration/release-notes/rdi-1-4-4/) | Installation on Kubernetes with a Helm chart. Improvements for installation on VMs. |
| [1.4.3 (December 2024)](https://redis.io/docs/latest/integrate/redis-data-integration/release-notes/rdi-1-4-3/) | Installation on Kubernetes with a Helm chart. Improvements for installation on VMs. |
| [1.4.2 (November 2024)](https://redis.io/docs/latest/integrate/redis-data-integration/release-notes/rdi-1-4-2/) | Installation on Kubernetes with a Helm chart. Improvements for installation on VMs. |
| [1.4.1 (November 2024)](https://redis.io/docs/latest/integrate/redis-data-integration/release-notes/rdi-1-4-1/) | Installation on Kubernetes with a Helm chart. Improvements for installation on VMs. |
| [1.4.0 (October 2024)](https://redis.io/docs/latest/integrate/redis-data-integration/release-notes/rdi-1-4-0/) | Installation on Kubernetes with a Helm chart. Improvements for installation on VMs. |
| [1.2.8 (August 2024)](https://redis.io/docs/latest/integrate/redis-data-integration/release-notes/rdi-1-2-8/) | API server with a set of APIs to support Redis Insight with creating, testing, deploying & monitoring RDI pipelines. RDI Installer verifies all components are running at the end of installation. |
| [1.2 (June 2024)](https://redis.io/docs/latest/integrate/redis-data-integration/release-notes/rdi-1-2/) | API server with a set of APIs to support Redis Insight with creating, testing, deploying & monitoring RDI pipelines. RDI Installer verifies all components are running at the end of installation. |
| [1.0 (June 2024)](https://redis.io/docs/latest/integrate/redis-data-integration/release-notes/rdi-1-0/) | Changes to the processing mode. Simple installation. Silent installation. Pipeline orchestration. Logging. Monitoring. High availability mechanism. |


