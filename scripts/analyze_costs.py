import csv
from collections import defaultdict

file_path = "data/synthetic_aws_cost_data.csv"
report_path = "reports/cost_summary_report.txt"

total_cost = 0
total_savings = 0
untagged_count = 0

cost_by_service = defaultdict(float)
cost_by_department = defaultdict(float)
savings_by_waste_category = defaultdict(float)

top_savings_opportunities = []

with open(file_path, newline="") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        cost = float(row["monthly_cost"])
        savings = float(row["estimated_savings"])

        total_cost += cost
        total_savings += savings

        cost_by_service[row["aws_service"]] += cost
        cost_by_department[row["department"]] += cost
        savings_by_waste_category[row["waste_category"]] += savings

        if row["tag_status"] == "untagged":
            untagged_count += 1

        if savings > 0:
            top_savings_opportunities.append({
                "resource_id": row["resource_id"],
                "department": row["department"],
                "aws_service": row["aws_service"],
                "environment": row["environment"],
                "waste_category": row["waste_category"],
                "recommendation": row["recommendation"],
                "estimated_savings": savings
            })

top_savings_opportunities.sort(
    key=lambda item: item["estimated_savings"],
    reverse=True
)

report_lines = []

report_lines.append("=== MediBill Cloud Cost Summary ===")
report_lines.append(f"Total monthly AWS cost: ${total_cost:,.2f}")
report_lines.append(f"Estimated monthly savings: ${total_savings:,.2f}")
report_lines.append(f"Untagged resources: {untagged_count}")

report_lines.append("\n=== Cost by AWS Service ===")
for service, cost in cost_by_service.items():
    report_lines.append(f"{service}: ${cost:,.2f}")

report_lines.append("\n=== Cost by Department ===")
for department, cost in cost_by_department.items():
    report_lines.append(f"{department}: ${cost:,.2f}")

report_lines.append("\n=== Savings by Waste Category ===")
for category, savings in savings_by_waste_category.items():
    report_lines.append(f"{category}: ${savings:,.2f}")

report_lines.append("\n=== Top 10 Savings Opportunities ===")
for item in top_savings_opportunities[:10]:
    report_lines.append(
        f"{item['resource_id']} | "
        f"{item['department']} | "
        f"{item['aws_service']} | "
        f"{item['environment']} | "
        f"{item['waste_category']} | "
        f"Save ${item['estimated_savings']:,.2f} | "
        f"{item['recommendation']}"
    )

for line in report_lines:
    print(line)

with open(report_path, "w") as report_file:
    for line in report_lines:
        report_file.write(line + "\n")

print(f"\nReport saved to: {report_path}")