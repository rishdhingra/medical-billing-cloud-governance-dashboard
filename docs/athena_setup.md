# Amazon Athena Setup

## Purpose

This phase connects the synthetic AWS cost dataset stored in Amazon S3 to Amazon Athena so the data can be queried using SQL.

Athena allows the project to analyze cloud cost, waste, savings opportunities, and governance issues directly from S3.

## Data source

The CSV file is stored in Amazon S3:

```text
s3://<bucket-name>/raw/synthetic_aws_cost_data.csv
