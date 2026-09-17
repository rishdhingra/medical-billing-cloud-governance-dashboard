-- Query 1: Cost by AWS service
SELECT 
  aws_service,
  ROUND(SUM(monthly_cost), 2) AS total_cost
FROM medibill_finops.synthetic_aws_cost_data
GROUP BY aws_service
ORDER BY total_cost DESC;


-- Query 2: Cost by department
SELECT 
  department,
  ROUND(SUM(monthly_cost), 2) AS total_cost
FROM medibill_finops.synthetic_aws_cost_data
GROUP BY department
ORDER BY total_cost DESC;


-- Query 3: Untagged resources by department, service, and environment
SELECT 
  department,
  aws_service,
  environment,
  COUNT(*) AS untagged_resource_count
FROM medibill_finops.synthetic_aws_cost_data
WHERE tag_status = 'untagged'
GROUP BY department, aws_service, environment
ORDER BY untagged_resource_count DESC;


-- Query 4: Top 10 savings opportunities
SELECT 
  resource_id,
  department,
  aws_service,
  environment,
  waste_category,
  recommendation,
  estimated_savings
FROM medibill_finops.synthetic_aws_cost_data
WHERE estimated_savings > 0
ORDER BY estimated_savings DESC
LIMIT 10;
