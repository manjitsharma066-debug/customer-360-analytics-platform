from google.cloud import bigquery

PROJECT_ID = "gcp-data-engineering-manjit"
DATASET = "customer360_dw"

client = bigquery.Client(project=PROJECT_ID)

print("=" * 70)
print(" CUSTOMER 360 ETL PIPELINE VALIDATION")
print("=" * 70)


def run_scalar_query(query):
    result = client.query(query).result()
    for row in result:
        return list(row.values())[0]


def validate_row_count(table, expected):
    query = f"""
    SELECT COUNT(*) AS row_count
    FROM `{PROJECT_ID}.{DATASET}.{table}`
    """
    actual = run_scalar_query(query)

    status = "PASS" if actual == expected else "FAIL"

    print(f"{table:<20} Expected={expected:<8} Actual={actual:<8} {status}")

    return status == "PASS"


print("\nROW COUNT VALIDATION")
print("-" * 70)

checks = []

checks.append(validate_row_count("bronze_customers", 5000))
checks.append(validate_row_count("silver_customers", 5000))
checks.append(validate_row_count("dim_customer", 5000))

checks.append(validate_row_count("bronze_products", 500))
checks.append(validate_row_count("silver_products", 500))
checks.append(validate_row_count("dim_product", 500))

checks.append(validate_row_count("bronze_orders", 100000))
checks.append(validate_row_count("silver_orders", 100000))
checks.append(validate_row_count("fact_sales", 100000))


print("\nREFERENTIAL INTEGRITY")
print("-" * 70)

queries = {
    "Missing Customers": """
        SELECT COUNT(*)
        FROM `gcp-data-engineering-manjit.customer360_dw.fact_sales` f
        LEFT JOIN `gcp-data-engineering-manjit.customer360_dw.dim_customer` c
        ON f.customer_id = c.customer_id
        WHERE c.customer_id IS NULL
    """,

    "Missing Products": """
        SELECT COUNT(*)
        FROM `gcp-data-engineering-manjit.customer360_dw.fact_sales` f
        LEFT JOIN `gcp-data-engineering-manjit.customer360_dw.dim_product` p
        ON f.product_id = p.product_id
        WHERE p.product_id IS NULL
    """,

    "Missing Stores": """
        SELECT COUNT(*)
        FROM `gcp-data-engineering-manjit.customer360_dw.fact_sales` f
        LEFT JOIN `gcp-data-engineering-manjit.customer360_dw.dim_store` s
        ON f.store_id = s.store_id
        WHERE s.store_id IS NULL
    """,

    "Missing Dates": """
        SELECT COUNT(*)
        FROM `gcp-data-engineering-manjit.customer360_dw.fact_sales` f
        LEFT JOIN `gcp-data-engineering-manjit.customer360_dw.dim_date` d
        ON f.order_date = d.order_date
        WHERE d.order_date IS NULL
    """
}

for name, query in queries.items():
    value = run_scalar_query(query)
    status = "PASS" if value == 0 else "FAIL"
    print(f"{name:<25} {value:<5} {status}")
    checks.append(value == 0)


print("\n" + "=" * 70)

if all(checks):
    print("FINAL RESULT : ETL PIPELINE VALIDATION PASSED")
else:
    print("FINAL RESULT : ETL PIPELINE VALIDATION FAILED")

print("=" * 70)