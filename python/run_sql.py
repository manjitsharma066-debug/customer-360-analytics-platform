"""
=====================================================
Customer 360 Analytics Platform
Execute SQL Scripts in BigQuery
=====================================================
"""

from pathlib import Path
from google.cloud import bigquery

from config import PROJECT_ID, SQL_DIR
from logger import setup_logger

logger = setup_logger(__name__)


def execute_sql_file(sql_file):
    """
    Execute an entire SQL script in BigQuery.
    """

    sql_path = Path(SQL_DIR) / sql_file

    if not sql_path.exists():
        logger.error(f"SQL file not found: {sql_path}")
        return

    logger.info(f"Running SQL Script: {sql_file}")

    with open(sql_path, "r", encoding="utf-8") as f:
        sql_script = f.read()

    client = bigquery.Client(project=PROJECT_ID)

    job_config = bigquery.QueryJobConfig()

    query_job = client.query(
        sql_script,
        job_config=job_config
    )

    query_job.result()

    logger.info(f"Completed : {sql_file}")


def run_all_sql():

    sql_files = [
        "bronze_to_silver.sql",
        "silver_to_gold.sql",
        "data_quality.sql"
    ]

    logger.info("=" * 60)
    logger.info("Starting SQL Execution")
    logger.info("=" * 60)

    for sql_file in sql_files:
        execute_sql_file(sql_file)

    logger.info("=" * 60)
    logger.info("All SQL Scripts Executed Successfully")
    logger.info("=" * 60)


def main():
    run_all_sql()


if __name__ == "__main__":
    main()