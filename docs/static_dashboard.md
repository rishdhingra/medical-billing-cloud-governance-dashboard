# Static Dashboard

## Purpose

This dashboard provides a stakeholder-facing view of the MediBill cloud cost and governance analysis.

It was built from Athena-exported CSV results.

## Dashboard File

`dashboard/medibill_dashboard.html`

## Data Sources

The dashboard uses the following Athena result files:

- `reports/athena_results/cost_by_service.csv`
- `reports/athena_results/cost_by_department.csv`
- `reports/athena_results/untagged_resources.csv`
- `reports/athena_results/top_10_savings_opportunities.csv`

## Visuals Included

- Total monthly cloud cost
- Top 10 estimated savings
- Untagged resources found
- Monthly cost by AWS service
- Monthly cost by department
- Untagged resources table
- Top savings opportunities table

## Why This Matters

This turns the Athena SQL analysis into a business-facing dashboard that non-technical stakeholders can understand.

QuickSight can be added later as an AWS-native dashboard layer.
