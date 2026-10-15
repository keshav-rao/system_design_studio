# Redis Cloud changelog (October 2023)

```json metadata
{
  "schema_version": 2,
  "title": "Redis Cloud changelog (October 2023)",
  "description": "New features, enhancements, and other changes added to Redis Cloud during October 2023.",
  "categories": ["docs","operate","rc"],
  "tableOfContents": {"sections":[{"children":[{"id":"cost-report-csv-download","title":"Cost report CSV download"},{"id":"saml-account-linking-tokens","title":"SAML account linking tokens"}],"id":"new-features","title":"New features"}]}

,
  "codeExamples": []
}
```


## New features

### Cost report CSV download

You can now download shard cost reports in CSV format from the [**Billing and Payments**](https://redis.io/docs/latest/operate/rc/billing-and-payments) and [**Usage Reports**](https://redis.io/docs/latest/operate/rc/logs-reports/usage-reports) pages.

Select the **Cost report** button to download a report of all shard costs in CSV format.

![The cost report download button.](https://redis.io/docs/latest/images/rc/button-cost-report-download.png)

The report gives a breakdown of all your Redis billing unit costs, per subscription and database, by month. Subscriptions under the minimum subscription price are broken down into actual billing unit prices and the difference from minimum price.
### SAML account linking tokens

The process for [linking new Redis accounts](https://redis.io/docs/latest/operate/rc/security/access-control/saml-sso#link-other-accounts) to your [SAML single sign-on](https://redis.io/docs/latest/operate/rc/security/access-control/saml-sso) configuration has changed to enhance security. Now, both accounts must use a token to ensure that the connection is legitimate.

