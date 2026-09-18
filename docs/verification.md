# MediBill verification

The local workflow was rerun against the checked-in dataset on September 18, 2026.

Commands:

```bash
python3 scripts/analyze_costs.py
python3 scripts/build_static_dashboard.py
```

The analyzer completed successfully and reproduced the saved report totals:

- 150 synthetic records are present in `data/synthetic_aws_cost_data.csv`.
- Modeled monthly cost: `$43,265.00`.
- Estimated monthly savings: `$10,773.00`.
- Untagged resources: `28`.
- The dashboard was regenerated from the four CSV files in `reports/athena_results/`.

The AWS setup documents describe the earlier S3, Glue, Athena, and EC2 lab workflow. Terraform remains an unapplied blueprint by design; no new AWS resources were created during this verification.
