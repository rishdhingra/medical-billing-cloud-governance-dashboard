# AWS S3 Setup

## Purpose

This phase moves the synthetic AWS cost data from my local machine into Amazon S3.

S3 is used as the cloud storage layer for the MediBill cost and governance dataset.

## What I did

1. Created an S3 bucket for the project.
2. Blocked public access on the bucket.
3. Uploaded the synthetic AWS cost CSV file to the `raw/` folder.
4. Verified the file upload using the AWS CLI.

## S3 structure

```text
s3://<bucket-name>/raw/synthetic_aws_cost_data.csv
