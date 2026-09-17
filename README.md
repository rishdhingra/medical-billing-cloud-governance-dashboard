# MediBill Cloud Cost & Governance Dashboard

## Overview

MediBill Cloud Cost & Governance Dashboard is a cloud analytics project that simulates how a medical billing company could analyze AWS cloud spend, identify governance issues, and recommend cost optimization actions.

The project uses synthetic AWS cost data only. No real patient data, billing data, or PHI is used.

This project demonstrates a practical AWS workflow using:

- Python
- Amazon S3
- AWS Glue
- Amazon Athena
- Amazon EC2
- IAM
- AWS CLI
- Terraform
- Static HTML dashboarding

## Business Problem

A simulated medical billing company uses AWS for claim storage, reporting, analytics, dashboards, and backend systems.

Leadership needs answers to questions such as:

- Which AWS services cost the most?
- Which departments are driving cloud spend?
- Which resources are missing ownership or cost-center tags?
- Which resources create the largest savings opportunities?
- What recommendations should be made to improve cloud governance?

## Architecture

```text
Synthetic AWS Cost Data Generator
        ↓
Local CSV Dataset
        ↓
Python Cost Analyzer
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
Static Dashboard / Reporting Layer

Additional Cloud Engineering Lab:

Amazon EC2 Linux Instance
        ↓
IAM Role-Based S3 Access
        ↓
Download CSV from S3
        ↓
Run Python Analyzer on EC2
        ↓
Upload Report Back to S3
