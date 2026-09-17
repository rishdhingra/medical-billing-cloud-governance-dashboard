import csv
import random

output_file = "data/synthetic_aws_cost_data.csv"

months = ["2026-06", "2026-07", "2026-08"]

departments = [
    "Claims Processing",
    "Billing Operations",
    "Reporting Analytics",
    "Engineering",
    "Admin"
]

services = ["EC2", "S3", "RDS", "Lambda", "CloudWatch", "QuickSight", "Glue", "Athena"]

environments = ["dev", "test", "prod"]

owners = {
    "Claims Processing": "claims-team",
    "Billing Operations": "billing-team",
    "Reporting Analytics": "reports-team",
    "Engineering": "engineering-team",
    "Admin": "admin-team"
}

waste_categories = ["none", "idle", "overprovisioned", "untagged", "storage_tier", "log_retention"]

recommendations = {
    "none": "No action needed",
    "idle": "Schedule shutdown after business hours",
    "overprovisioned": "Review sizing and downsize resource",
    "untagged": "Add owner and cost-center tags",
    "storage_tier": "Move older files to cheaper S3 storage class",
    "log_retention": "Reduce log retention for non-production environment"
}

with open(output_file, "w", newline="") as csvfile:
    fieldnames = [
        "month",
        "department",
        "aws_service",
        "environment",
        "resource_id",
        "owner",
        "monthly_cost",
        "tag_status",
        "usage_level",
        "waste_category",
        "recommendation",
        "estimated_savings"
    ]

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(150):
        month = random.choice(months)
        department = random.choice(departments)
        service = random.choice(services)
        environment = random.choice(environments)

        waste_category = random.choice(waste_categories)

        if waste_category == "untagged":
            tag_status = "untagged"
            owner = "unknown"
        else:
            tag_status = "tagged"
            owner = owners[department]

        if service == "RDS":
            cost = random.randint(300, 1200)
        elif service == "EC2":
            cost = random.randint(100, 900)
        elif service == "S3":
            cost = random.randint(40, 500)
        elif service == "QuickSight":
            cost = random.randint(80, 400)
        elif service == "CloudWatch":
            cost = random.randint(30, 250)
        elif service == "Glue":
            cost = random.randint(50, 600)
        elif service == "Athena":
            cost = random.randint(20, 200)
        else:
            cost = random.randint(10, 150)

        if waste_category == "none":
            estimated_savings = 0
        else:
            estimated_savings = int(cost * random.uniform(0.15, 0.45))

        resource_id = f"{service.lower()}-{department.lower().replace(' ', '-')}-{environment}-{i}"

        writer.writerow({
            "month": month,
            "department": department,
            "aws_service": service,
            "environment": environment,
            "resource_id": resource_id,
            "owner": owner,
            "monthly_cost": cost,
            "tag_status": tag_status,
            "usage_level": random.choice(["low", "normal", "high"]),
            "waste_category": waste_category,
            "recommendation": recommendations[waste_category],
            "estimated_savings": estimated_savings
        })

print(f"Generated 150 fake AWS cost records in {output_file}")
