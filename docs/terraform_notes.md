# Terraform Notes

## Purpose

This folder contains a Terraform infrastructure-as-code blueprint for the MediBill Cloud Cost & Governance project.

The Terraform files define the type of AWS infrastructure used in the project:

- S3 bucket for synthetic AWS cost data
- S3 public access blocking
- EC2 IAM role
- Least-privilege S3 IAM policy
- IAM instance profile for EC2

## Why This Matters

The project was first built manually with the AWS Console and AWS CLI to understand each service step-by-step.

Terraform was then added to show how the same infrastructure could be represented as code.

## Safety Note

The Terraform configuration is currently a blueprint.

The project bucket and IAM role were already created manually during the lab. Because of that, `terraform apply` was not run yet to avoid modifying or duplicating existing AWS resources.

## Security Improvement

During the EC2 lab, the temporary IAM role used broad S3 permissions.

The Terraform blueprint improves this by defining a more limited policy that only allows:

- Listing the project S3 bucket
- Reading objects from the project bucket
- Writing objects to the project bucket

This follows a better least-privilege access pattern.
