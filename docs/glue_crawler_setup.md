# AWS Glue Crawler Setup

## Purpose

This phase uses AWS Glue to scan the synthetic AWS cost data stored in Amazon S3 and create a table in the AWS Glue Data Catalog.

The Glue-created table can then be queried in Amazon Athena.

## Crawler name

medibill-cost-crawler

## Data source

s3://<bucket-name>/raw/

## IAM role

AWSGlueServiceRole-example-glue-role

## Target database

medibill_finops

## Schedule

On demand only.

## Tables created

The Glue crawler created the table:

raw

The project also includes a manually created Athena table:

synthetic_aws_cost_data

## Why this matters

This adds a real AWS data catalog layer to the project. Instead of only manually defining Athena tables, AWS Glue can scan the S3 dataset and create metadata that Athena can query.
