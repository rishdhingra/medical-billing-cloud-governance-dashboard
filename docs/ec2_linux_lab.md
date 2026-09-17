# EC2 Linux Cloud Support Lab

## Purpose

This lab demonstrates how the MediBill cloud cost analysis workflow can run from an AWS EC2 Linux instance instead of only from a local machine.

The goal was to practice cloud support and cloud engineering skills:

- Launching an EC2 Linux instance
- Connecting with SSH
- Using Linux commands
- Using IAM roles instead of hardcoded AWS keys
- Accessing S3 from EC2
- Running Python scripts on a cloud server
- Uploading generated reports back to S3
- Terminating cloud resources after use

## AWS Services Used

- Amazon EC2
- Amazon S3
- IAM
- AWS CLI

## EC2 Configuration

- Instance name: medibill-linux-lab
- AMI: Amazon Linux 2023
- Instance type: t3.micro
- IAM role: example-ec2-s3-role
- Security group: SSH allowed from My IP only

## IAM Role Validation

The EC2 instance used an IAM role instead of local AWS access keys.

The role was confirmed with this command:

    aws sts get-caller-identity

The output showed the EC2 instance assuming this role:

    assumed-role/example-ec2-s3-role

## S3 Download Test

The synthetic AWS cost dataset was downloaded from S3 to the EC2 instance:

    aws s3 cp s3://<bucket-name>/raw/synthetic_aws_cost_data.csv data/synthetic_aws_cost_data.csv

## EC2 Python Analysis

A Python analyzer was run on the EC2 instance to calculate:

- Total monthly AWS cost
- Estimated savings
- Untagged resources
- Cost by AWS service
- Cost by department
- Savings by waste category
- Top 10 savings opportunities

## S3 Upload Test

The EC2-generated report was uploaded back to S3:

    aws s3 cp reports/ec2_cost_summary_report.txt s3://<bucket-name>/reports/ec2_cost_summary_report.txt

## Output

The EC2-generated report is saved locally here:

    reports/ec2_cost_summary_report.txt

It was also uploaded to the S3 reports folder.

## Security Notes

- No AWS access keys were stored on the EC2 instance.
- S3 access was provided through an IAM role.
- SSH access was restricted to My IP only.
- The EC2 instance was terminated after the lab to avoid unnecessary cost.
