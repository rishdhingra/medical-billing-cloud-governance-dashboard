# Athena Query Results Summary

## Purpose

This document summarizes the Athena SQL analysis performed on the synthetic AWS cost data stored in Amazon S3.

The goal was to answer cloud cost and governance questions for the simulated medical billing company, MediBill Cloud Solutions.

## Data Flow

Synthetic AWS cost CSV  
→ Amazon S3 raw folder  
→ AWS Glue Crawler  
→ AWS Glue Data Catalog table  
→ Amazon Athena SQL queries  
→ Athena result CSVs

## Questions Answered

### 1. Which AWS services cost the most?

Result file:

`reports/athena_results/cost_by_service.csv`

This helps identify the largest service-level cost drivers.

### 2. Which departments spend the most?

Result file:

`reports/athena_results/cost_by_department.csv`

This helps leadership understand which internal teams are driving cloud spend.

### 3. Where are the untagged resources?

Result file:

`reports/athena_results/untagged_resources.csv`

This helps identify governance issues where resources are missing ownership or cost-center metadata.

### 4. What are the top 10 savings opportunities?

Result file:

`reports/athena_results/top_10_savings_opportunities.csv`

This helps stakeholders prioritize the highest-impact optimization actions.

## Why This Matters

This phase shows how Athena can query cost and governance data directly from S3 using SQL.

Instead of only analyzing data locally with Python, the project now uses an AWS-native analytics workflow with S3, Glue, and Athena.
