"""
Load Raw CSV Files from Google Cloud Storage to BigQuery
Author : Manjit Kumar Sharma
Project : Customer 360 Analytics Platform
"""

from google.cloud import bigquery

from config import (
    PROJECT_ID,
    DATASET_ID,
    RAW_GCS,
    TABLES
)

client = bigquery.Client(project=PROJECT_ID)


# -----------------------------
# Explicit Schemas
# -----------------------------

SCHEMAS = {

    "bronze_customers": [
    bigquery.SchemaField("customer_id", "STRING"),
    bigquery.SchemaField("customer_name", "STRING"),
    bigquery.SchemaField("gender", "STRING"),
    bigquery.SchemaField("age", "INTEGER"),
    bigquery.SchemaField("city", "STRING"),
    bigquery.SchemaField("state", "STRING"),
    bigquery.SchemaField("join_date", "DATE"),
    ],

    "bronze_products": [
        bigquery.SchemaField("product_id", "STRING"),
        bigquery.SchemaField("product_name", "STRING"),
        bigquery.SchemaField("category", "STRING"),
        bigquery.SchemaField("brand", "STRING"),
        bigquery.SchemaField("unit_price", "FLOAT"),
    ],

    "bronze_stores": [
        bigquery.SchemaField("store_id", "STRING"),
        bigquery.SchemaField("store_name", "STRING"),
        bigquery.SchemaField("city", "STRING"),
        bigquery.SchemaField("state", "STRING"),
        bigquery.SchemaField("region", "STRING"),
    ],

    "bronze_orders": [
        bigquery.SchemaField("order_id", "STRING"),
        bigquery.SchemaField("customer_id", "STRING"),
        bigquery.SchemaField("product_id", "STRING"),
        bigquery.SchemaField("store_id", "STRING"),
        bigquery.SchemaField("order_date", "DATE"),
        bigquery.SchemaField("quantity", "INTEGER"),
        bigquery.SchemaField("unit_price", "FLOAT"),
        bigquery.SchemaField("total_amount", "FLOAT"),
        bigquery.SchemaField("payment_method", "STRING"),
        bigquery.SchemaField("order_status", "STRING"),
    ],
}


def load_bigquery_tables():

    loaded_tables = 0

    for file_name, table_name in TABLES.items():

        uri = f"{RAW_GCS}/{file_name}.csv"
        table_id = f"{PROJECT_ID}.{DATASET_ID}.{table_name}"

        job_config = bigquery.LoadJobConfig(
            source_format=bigquery.SourceFormat.CSV,
            skip_leading_rows=1,
            schema=SCHEMAS[table_name],
            write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
        )

        try:

            load_job = client.load_table_from_uri(
                uri,
                table_id,
                job_config=job_config,
            )

            load_job.result()

            table = client.get_table(table_id)

            print(f"✅ {table_name} loaded successfully ({table.num_rows:,} rows)")

            loaded_tables += 1

        except Exception as e:

            print(f"❌ Failed to load {table_name}")
            print(e)

    print("=" * 60)
    print("BigQuery Load Completed")
    print("=" * 60)
    print(f"Tables Loaded : {loaded_tables}")
    print("=" * 60)


def main():
    load_bigquery_tables()


if __name__ == "__main__":
    main()