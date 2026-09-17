resource "aws_s3_bucket" "cost_data" {
  bucket = var.bucket_name

  tags = {
    Project     = var.project_name
    Environment = "student-lab"
    ManagedBy   = "terraform-blueprint"
  }
}

resource "aws_s3_bucket_public_access_block" "cost_data" {
  bucket = aws_s3_bucket.cost_data.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

data "aws_iam_policy_document" "ec2_assume_role" {
  statement {
    actions = ["sts:AssumeRole"]

    principals {
      type        = "Service"
      identifiers = ["ec2.amazonaws.com"]
    }
  }
}

resource "aws_iam_role" "ec2_s3_role" {
  name               = "medibill-ec2-s3-role-terraform-example"
  assume_role_policy = data.aws_iam_policy_document.ec2_assume_role.json

  tags = {
    Project   = var.project_name
    ManagedBy = "terraform-blueprint"
  }
}

data "aws_iam_policy_document" "medibill_s3_access" {
  statement {
    sid     = "AllowListProjectBucket"
    effect  = "Allow"
    actions = ["s3:ListBucket"]

    resources = [
      aws_s3_bucket.cost_data.arn
    ]
  }

  statement {
    sid    = "AllowReadWriteProjectObjects"
    effect = "Allow"

    actions = [
      "s3:GetObject",
      "s3:PutObject"
    ]

    resources = [
      "${aws_s3_bucket.cost_data.arn}/*"
    ]
  }
}

resource "aws_iam_policy" "medibill_s3_access" {
  name        = "medibill-s3-access-terraform-example"
  description = "Least-privilege S3 access for the MediBill EC2 Linux lab."
  policy      = data.aws_iam_policy_document.medibill_s3_access.json
}

resource "aws_iam_role_policy_attachment" "ec2_s3_access" {
  role       = aws_iam_role.ec2_s3_role.name
  policy_arn = aws_iam_policy.medibill_s3_access.arn
}

resource "aws_iam_instance_profile" "ec2_profile" {
  name = "medibill-ec2-instance-profile-terraform-example"
  role = aws_iam_role.ec2_s3_role.name
}
