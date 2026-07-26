"""
=====================================================
Customer 360 Analytics Platform
End-to-End ETL Pipeline
=====================================================
"""

from logger import setup_logger

import generate_customers
import generate_products
import generate_stores
import generate_orders
import upload_to_gcs
import load_bigquery
import run_sql

logger = setup_logger(__name__)


def run_pipeline():

    logger.info("=" * 60)
    logger.info("Starting Customer 360 ETL Pipeline")
    logger.info("=" * 60)

    # -------------------------------------------------
    # Generate Data
    # -------------------------------------------------

    logger.info("Generating Customers...")
    generate_customers.generate_customers()

    logger.info("Generating Products...")
    generate_products.generate_products()

    logger.info("Generating Stores...")
    generate_stores.generate_stores()

    logger.info("Generating Orders...")
    generate_orders.generate_orders()

    # -------------------------------------------------
    # Upload to Google Cloud Storage
    # -------------------------------------------------

    logger.info("Uploading CSV files to GCS...")
    upload_to_gcs.upload_folder()

    # -------------------------------------------------
    # Load Bronze Tables
    # -------------------------------------------------

    logger.info("Loading Bronze Tables...")
    load_bigquery.load_bigquery_tables()

    # -------------------------------------------------
    # Build Silver & Gold Layer
    # -------------------------------------------------

    logger.info("Executing SQL Scripts...")
    run_sql.run_all_sql()

    logger.info("=" * 60)
    logger.info("Customer 360 ETL Pipeline Completed Successfully")
    logger.info("=" * 60)


def main():
    run_pipeline()


if __name__ == "__main__":
    main()