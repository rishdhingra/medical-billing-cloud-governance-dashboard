output "bucket_name" {
  description = "S3 bucket used for MediBill cost data."
  value       = aws_s3_bucket.cost_data.bucket
}

output "ec2_role_name" {
  description = "IAM role intended for EC2 S3 access."
  value       = aws_iam_role.ec2_s3_role.name
}

output "instance_profile_name" {
  description = "Instance profile that can be attached to EC2."
  value       = aws_iam_instance_profile.ec2_profile.name
}
