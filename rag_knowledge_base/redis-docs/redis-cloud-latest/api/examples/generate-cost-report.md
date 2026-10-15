# Generate FOCUS-compliant cost report

```json metadata
{
  "schema_version": 2,
  "title": "Generate FOCUS-compliant cost report",
  "description": "Shows how to generate and download a cost report in FOCUS format using the Redis Cloud REST API.",
  "categories": ["docs","operate","rc"],
  "tableOfContents": {"sections":[{"id":"generate-a-cost-report","title":"Generate a cost report"},{"id":"get-cost-report-status","title":"Get cost report status"},{"children":[{"id":"cost-report-fields","title":"Cost report fields"}],"id":"download-cost-report","title":"Download cost report"}]}

,
  "codeExamples": []
}
```


You can use the Redis Cloud REST API to generate and download a cost report in a [FinOps Open Cost and Usage Specification (FOCUS)](https://focus.finops.org/) compatible format. The report includes detailed information about your Redis Cloud subscription usage and associated charges.

To get the cost report using the REST API:

1. Use [`POST /cost-report`](https://redis.io/docs/latest/operate/rc/api/api-reference#tag/Account/operation/createCostReport) to generate a cost report, with the request body containing the `startDate` and `endDate` for the report as well as any optional filters. Your account must have the **Owner**, **Viewer**, or **Billing admin** role to generate a cost report through this endpoint.

    The response includes a `taskId` that you can use to track the status of the report generation.

1. Use [`GET /tasks/{taskId}`](https://redis.io/docs/latest/operate/rc/api/api-reference#tag/Tasks/operation/getTaskById) to check report generation status. The report is ready when the `status` is `processing-completed` and the `response` field contains a `costReportId`.
1. Use [`GET /cost-report/{costReportId}`](https://redis.io/docs/latest/operate/rc/api/api-reference#tag/Account/operation/getCostReport) to download the generated cost report.

The following sections provide examples for each step.

## Generate a cost report

To generate a cost report, use [`POST /cost-report`](https://redis.io/docs/latest/operate/rc/api/api-reference#tag/Account/operation/createCostReport). Your account must have the **Owner**, **Billing admin**, or **Viewer** role to generate a cost report through this endpoint.

Include `startDate` and `endDate` in your request body using `YYYY-MM-DD` format. You can specify a date range up to 40 days.

```json
{
  "startDate": "2025-01-01",
  "endDate": "2025-01-31"
}
```

More options and filters can be added to the request body to filter the report data.

| Option name | Type | Description |
|-------------|--------|-------------|
| `format` | Enum: `csv`, `json` | The format for the report file. Default is `csv`. |
| `subscriptionIds` | Array of integers | Filters the report to only include the specified subscriptions. |
| `databaseIds` | Array of integers | Filters the report to only include the specified databases. |
| `subscriptionType` | Enum: `essentials`, `pro` | Filters the report to only include subscriptions of the specified type. |
| `regions` | Array of strings | Filters the report to only include subscriptions in the specified regions. |
| `tags` | Array of key-value pairs | Filters the report to only include databases with the specified [tags](https://redis.io/docs/latest/operate/rc/databases/tag-database). Both `key` and `value` are required for each tag. |

For example, the following request body generates a CSV report for all databases in the `us-east-1` region that have the `team:marketing` tag in January 2025:

```json
{
  "startDate": "2025-01-01",
  "endDate": "2025-01-31",
  "format": "csv",
  "regions": ["us-east-1"],
  "tags": [
    {
      "key": "team",
      "value": "marketing"
    }
  ]
}
```

The response body is a [task object](https://redis.io/docs/latest/operate/rc/api/get-started/manage-tasks#task-information) that contains the `taskId` for the task that generates the cost report:

```json
{
  "taskId": "7ba51acc-cd1d-44c7-8453-281730d214ce",
  "commandType": "costReportCreateRequest",
  "status": "received",
  "description": "Task request received and is being queued for processing.",
  "timestamp": "2025-11-07T15:44:29.811142433Z",
  "links": [
    {
      "href": "https://api.redislabs.com/v1/tasks/7ba51acc-cd1d-44c7-8453-281730d214ce",
      "type": "GET",
      "rel": "task"
    }
  ]
}
```

## Get cost report status

To get the status of the cost report generation, use [`GET /tasks/{taskId}`](https://redis.io/docs/latest/operate/rc/api/api-reference#tag/Tasks/operation/getTaskById) with the `taskId` from the previous step.

When the report is ready, the `status` is `processing-completed` and the `response` field contains a `costReportId`:

```json
{
  "taskId": "7ba51acc-cd1d-44c7-8453-281730d214ce",
  "commandType": "costReportCreateRequest",
  "status": "processing-completed",
  "description": "Request processing completed successfully and its resources are now being provisioned / de-provisioned.",
  "timestamp": "2025-11-07T15:44:31.168900133Z",
  "response": {
    "resource": {
      "costReportId": "a07524cf-6d4d-47ec-a1b7-810d1cbafcf7.json"
    }
  },
  "links": [
    {
      "href": "https://api.redislabs.com/v1/tasks/7ba51acc-cd1d-44c7-8453-281730d214ce",
      "type": "GET",
      "rel": "self"
    }
  ]
}
```

## Download cost report

To get the cost report, use [`GET /cost-report/{costReportId}`](https://redis.io/docs/latest/operate/rc/api/api-reference#tag/Account/operation/getCostReport) with the `costReportId` from the previous step.

You can use this cost report with any FOCUS-compatible cost reporting tool to analyze and visualize your costs.

### Cost report fields

The cost report returned from the Redis Cloud REST API contains fields from the [FOCUS column library](https://focus.finops.org/focus-columns/). The Redis Cloud-specific implementation is described in the following sections.

#### Billing account and publisher fields

| Field | Type | Description |
|---|---|---|
| `BillingAccountId` | String | Redis Cloud account ID. |
| `BillingAccountName` | String | Display name of the Redis Cloud account. |
| `BillingAccountType` | String | Type of billing account structure. Always set to `Redis Cloud`. |
| `PublisherName` | String | Publisher/vendor of the service, which is Redis. Always `redis.io`. |

#### Pricing fields

| Field | Type | Description |
|---|---|---|
| `PricingCategory` | String | Pricing model category. Always `Standard`. |
| `PricingCurrency` | String | The currency used for pricing. Always `USD`. |
| `PricingQuantity` | BigDecimal | Quantity of units being priced. For hourly services like Redis Cloud Pro, this is the number of hours. For monthly services like Redis Cloud Essentials and network costs, this is typically one month. |
| `PricingUnit` | String | The unit of measure for pricing. Can be `Hours` (Pro), `Months` (Essentials), or `Network`. |

#### Period fields

| Field | Type | Description |
|---|---|---|
| `BillingPeriodStart` | Instant (ISO 8601 DateTime) | Start of the billing period (inclusive). |
| `BillingPeriodEnd` | Instant (ISO 8601 DateTime) | End of the billing period (exclusive). |
| `ChargePeriodStart` | Instant (ISO 8601 DateTime) | Start of the specific charge period (inclusive). May differ from billing period if the resource was created mid-period. |
| `ChargePeriodEnd` | Instant (ISO 8601 DateTime) | End of the specific charge period (exclusive). May differ from billing period if the resource was deleted mid-period. |

#### Cost fields

| Field | Type | Description |
|---|---|---|
| `BilledCost` | BigDecimal | Cost that Redis will invoice you for. |
| `BillingCurrency` | String (ISO 4217) | Currency code for all billing amounts. Always `USD`. |
| `ConsumedQuantity` | BigDecimal | Actual amount of resources used. May be null for fixed-price plans. |
| `ConsumedUnit` | String | Unit for `ConsumedQuantity`. Can be `Hours` or `Network`. |
| `ContractedCost` | BigDecimal | Cost after applying contractual discounts but before credits. |
| `ContractedUnitPrice` | BigDecimal | Per-unit price after applying your negotiated discounts. |
| `EffectiveCost` | BigDecimal | True cost after all discounts, credits, and adjustments. |
| `ListCost` | BigDecimal | Cost at Redis's published list prices before any discounts. |
| `ListUnitPrice` | BigDecimal | Redis's published price per unit at list rates. |

#### Location, Resource, and SKU fields

| Field | Type | Description |
|---|---|---|
| `RegionId` | String | Cloud vendor region identifier. |
| `RegionName` | String | Display name of the region. |
| `ResourceId` | String | Identifier of the resource being charged. |
| `ResourceName` | String | Display name you gave to the resource in the Redis Cloud console. |
| `ResourceType` | String | Whether the charge is for a specific database or a subscription-level service. |
| `Tags` | JSON Map<String, String> | User-defined tags on resources. |
| `SkuPriceDetails` | JSON Map<String, Object> | Redis-specific technical details about the database configuration, such as RBUs, memory limit, and throughput. |

#### Charge fields

| Field | Type | Description |
|---|---|---|
| `ChargeCategory` | String | Category of the charge: `Usage`, `Purchase`, `Tax`, or `Adjustment`. |
| `ChargeDescription` | String | A clear description of what you're being charged for, combining service type and resource details. |
| `ChargeFrequency` | String | How often the charge occurs - always `Recurring`. |

#### Service fields

| Field | Type | Description |
|---|---|---|
| `ServiceCategory` | String | The high-level category of service - always `Databases`. |
| `ServiceName` | String | The Redis Cloud service tier - `Redis Cloud Pro` or `Redis Cloud Essentials`. |
| `ServiceSubcategory` | String | The specific type of database service - always `Caching`. |


