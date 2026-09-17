import csv
from pathlib import Path
from html import escape

BASE_DIR = Path(__file__).resolve().parent.parent
RESULTS_DIR = BASE_DIR / "reports" / "athena_results"
DASHBOARD_DIR = BASE_DIR / "dashboard"
OUTPUT_FILE = DASHBOARD_DIR / "medibill_dashboard.html"

DASHBOARD_DIR.mkdir(exist_ok=True)


def read_csv(filename):
    path = RESULTS_DIR / filename
    with open(path, newline="", encoding="utf-8-sig") as file:
        return list(csv.DictReader(file))


def money(value):
    try:
        return f"${float(value):,.2f}"
    except (ValueError, TypeError):
        return value


def number(value):
    try:
        return f"{float(value):,.0f}"
    except (ValueError, TypeError):
        return value


def bar_chart(title, rows, label_key, value_key, value_format="money"):
    if not rows:
        return f"<section><h2>{escape(title)}</h2><p>No data available.</p></section>"

    values = []
    for row in rows:
        try:
            values.append(float(row[value_key]))
        except (ValueError, KeyError):
            values.append(0)

    max_value = max(values) if values else 1
    html = f"<section><h2>{escape(title)}</h2>"

    for row, value in zip(rows, values):
        label = escape(row.get(label_key, "Unknown"))
        width = 0 if max_value == 0 else (value / max_value) * 100
        display_value = money(value) if value_format == "money" else number(value)

        html += f"""
        <div class="bar-row">
            <div class="bar-label">{label}</div>
            <div class="bar-container">
                <div class="bar" style="width:{width:.1f}%"></div>
            </div>
            <div class="bar-value">{display_value}</div>
        </div>
        """

    html += "</section>"
    return html


def table(title, rows, columns, money_columns=None, number_columns=None):
    money_columns = money_columns or []
    number_columns = number_columns or []

    html = f"<section><h2>{escape(title)}</h2><table><thead><tr>"

    for column in columns:
        html += f"<th>{escape(column.replace('_', ' ').title())}</th>"

    html += "</tr></thead><tbody>"

    for row in rows:
        html += "<tr>"
        for column in columns:
            value = row.get(column, "")

            if column in money_columns:
                value = money(value)
            elif column in number_columns:
                value = number(value)

            html += f"<td>{escape(str(value))}</td>"
        html += "</tr>"

    html += "</tbody></table></section>"
    return html


cost_by_service = read_csv("cost_by_service.csv")
cost_by_department = read_csv("cost_by_department.csv")
untagged_resources = read_csv("untagged_resources.csv")
top_savings = read_csv("top_10_savings_opportunities.csv")

total_cost = sum(float(row["total_cost"]) for row in cost_by_service)
total_top_savings = sum(float(row["estimated_savings"]) for row in top_savings)
total_untagged = sum(float(row["untagged_resource_count"]) for row in untagged_resources)

html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>MediBill Cloud Cost & Governance Dashboard</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 40px;
            background: #f6f7f9;
            color: #1f2937;
        }}

        header {{
            background: white;
            padding: 28px;
            border-radius: 14px;
            margin-bottom: 24px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }}

        h1 {{
            margin-bottom: 8px;
        }}

        .subtitle {{
            color: #6b7280;
            font-size: 16px;
        }}

        .cards {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 16px;
            margin-bottom: 24px;
        }}

        .card {{
            background: white;
            padding: 22px;
            border-radius: 14px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }}

        .card-title {{
            color: #6b7280;
            font-size: 14px;
            margin-bottom: 8px;
        }}

        .card-value {{
            font-size: 30px;
            font-weight: bold;
        }}

        section {{
            background: white;
            padding: 24px;
            border-radius: 14px;
            margin-bottom: 24px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }}

        .bar-row {{
            display: grid;
            grid-template-columns: 220px 1fr 120px;
            gap: 14px;
            align-items: center;
            margin: 12px 0;
        }}

        .bar-label {{
            font-weight: 600;
        }}

        .bar-container {{
            background: #e5e7eb;
            height: 22px;
            border-radius: 999px;
            overflow: hidden;
        }}

        .bar {{
            height: 100%;
            background: #2563eb;
            border-radius: 999px;
        }}

        .bar-value {{
            text-align: right;
            font-weight: 600;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 14px;
        }}

        th, td {{
            padding: 10px;
            border-bottom: 1px solid #e5e7eb;
            text-align: left;
            vertical-align: top;
        }}

        th {{
            background: #f3f4f6;
        }}

        footer {{
            color: #6b7280;
            font-size: 13px;
            margin-top: 24px;
        }}
    </style>
</head>
<body>

<header>
    <h1>MediBill Cloud Cost & Governance Dashboard</h1>
    <div class="subtitle">
        Stakeholder-facing dashboard built from Athena query results for a simulated medical billing cloud environment.
    </div>
</header>

<div class="cards">
    <div class="card">
        <div class="card-title">Total Monthly Cloud Cost</div>
        <div class="card-value">{money(total_cost)}</div>
    </div>

    <div class="card">
        <div class="card-title">Top 10 Estimated Savings</div>
        <div class="card-value">{money(total_top_savings)}</div>
    </div>

    <div class="card">
        <div class="card-title">Untagged Resources Found</div>
        <div class="card-value">{number(total_untagged)}</div>
    </div>
</div>

{bar_chart("Monthly Cost by AWS Service", cost_by_service, "aws_service", "total_cost")}
{bar_chart("Monthly Cost by Department", cost_by_department, "department", "total_cost")}

{table(
    "Untagged Resources",
    untagged_resources,
    ["department", "aws_service", "environment", "untagged_resource_count"],
    number_columns=["untagged_resource_count"]
)}

{table(
    "Top 10 Savings Opportunities",
    top_savings,
    ["resource_id", "department", "aws_service", "environment", "waste_category", "recommendation", "estimated_savings"],
    money_columns=["estimated_savings"]
)}

<footer>
    Data source: Athena result CSVs generated from AWS S3 data cataloged by AWS Glue.
</footer>

</body>
</html>
"""

OUTPUT_FILE.write_text(html, encoding="utf-8")
print(f"Dashboard created: {OUTPUT_FILE}")
