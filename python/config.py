# =====================================================
# Customer 360 Analytics Platform Configuration
# =====================================================
from pathlib import Path
# ==============================
# Project Paths
# ==============================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

LOG_DIR = BASE_DIR / "logs"

SQL_DIR = BASE_DIR / "sql"

DOCS_DIR = BASE_DIR / "docs"

RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)

PROJECT_ID = "gcp-data-engineering-manjit"

BUCKET_NAME = "customer360-de-manjit"

DATASET_ID = "customer360_dw"

LOCATION = "asia-south1"

RAW_GCS = f"gs://{BUCKET_NAME}/raw"

PROCESSED_GCS = f"gs://{BUCKET_NAME}/processed"

TABLES = {
    "customers": "bronze_customers",
    "products": "bronze_products",
    "stores": "bronze_stores",
    "orders": "bronze_orders"
}