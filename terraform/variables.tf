variable "aws_region" {
  description = "AWS region used for the MediBill project."
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project name used for tags."
  type        = string
  default     = "medibill-cloud-cost-governance"
}

variable "bucket_name" {
  description = "S3 bucket used for synthetic AWS cost data."
  type        = string
  default     = "medibill-synthetic-cost-data-example"
}
