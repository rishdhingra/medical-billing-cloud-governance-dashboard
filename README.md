# MediBill Cloud Cost & Governance Dashboard

MediBill is a portfolio project that analyzes synthetic AWS cost and governance data for a simulated medical billing company. It shows how a FinOps workflow can move from raw data to recommendations and a stakeholder-friendly dashboard.

No real patient, billing, or protected health information is used.

## What it demonstrates

- Python data generation and cost analysis
- Amazon S3, AWS Glue, and Amazon Athena workflow design
- Governance checks for ownership and cost-center tags
- Savings recommendations for idle, oversized, and poorly tiered resources
- A static HTML dashboard generated from Athena-style result CSVs
- IAM role-based access for an EC2 Linux support lab
- Terraform infrastructure-as-code for the S3 and EC2 IAM foundation

## Architecture

```text
Synthetic cost data → S3 raw/ → Glue crawler/catalog → Athena SQL
                                                        ↓
                                          reports/athena_results/
                                                        ↓
                                      static MediBill dashboard

EC2 Linux lab → IAM role → S3 download → Python analysis → S3 report upload
```

The Terraform directory is a safe blueprint. It describes an S3 bucket, public-access block, EC2 role, least-privilege S3 policy, and instance profile. It was not applied from this repository because the original lab resources were created manually.

## Verified local results

The current checked-in synthetic dataset contains 150 records. Running the analyzer produces:

| Measure | Result |
| --- | ---: |
| Monthly AWS cost modeled | $43,265.00 |
| Estimated monthly savings | $10,773.00 |
| Untagged resources | 28 |
| Largest service cost | EC2 ($10,716.00) |
| Largest department cost | Billing Operations ($12,863.00) |

The full report is in `reports/cost_summary_report.txt`, and the dashboard is `dashboard/medibill_dashboard.html`.

## Run locally

From the project directory:

```bash
python3 scripts/analyze_costs.py
python3 scripts/build_static_dashboard.py
open dashboard/medibill_dashboard.html
```

The analyzer reads `data/synthetic_aws_cost_data.csv` and refreshes `reports/cost_summary_report.txt`. The dashboard reads the CSV result files in `reports/athena_results/`.

To generate a new synthetic dataset first, run `python3 scripts/generate_fake_cost_data.py`, then rerun the analyzer and dashboard. Because generation is intentionally random, the displayed totals will change.

## AWS workflow documentation

- `docs/aws_s3_setup.md` — S3 upload and security setup
- `docs/glue_crawler_setup.md` — Glue catalog workflow
- `docs/athena_setup.md` — Athena setup
- `docs/athena_query_results_summary.md` — query outputs and business questions
- `docs/ec2_linux_lab.md` — EC2 role-based analysis lab
- `docs/static_dashboard.md` — dashboard inputs and visuals
- `docs/terraform_notes.md` — Terraform scope and safety notes
- `queries/athena_finops_queries.sql` — FinOps queries

## Scope and security

This is a portfolio demonstration using synthetic data. It is not a production medical billing system and does not claim HIPAA compliance. The dashboard is static, has no authentication, and should be treated as a local artifact unless it is placed behind an appropriate access-controlled hosting layer.
