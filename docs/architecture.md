# Architecture

## MediBill Cloud Cost & Governance Dashboard

This project simulates a cloud cost and governance workflow for a fake medical billing company.

## Architecture Flow

```text
Synthetic AWS Cost Data Generator
        ↓
Local CSV Dataset
        ↓
Python Cost Analyzer
        ↓
Local Cost Summary Report
        ↓
Amazon S3 Raw Data Bucket
        ↓
AWS Glue Crawler
        ↓
AWS Glue Data Catalog Table
        ↓
Amazon Athena SQL Queries
        ↓
Athena Result CSVs
        ↓
Stakeholder Dashboard / Reporting Layer
