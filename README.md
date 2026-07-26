<p align="center">
  <img src="assets/banner/banner.png" alt="Customer 360 Analytics Platform Banner" width="100%">
</p>

<h1 align="center">Customer 360 Analytics Platform</h1>

<p align="center">
Enterprise End-to-End Data Engineering Pipeline on Google Cloud Platform
</p>

# Customer 360 Analytics Platform using Google Cloud Platform

## Project Overview

The Customer 360 Analytics Platform is a batch ETL and Data Warehouse solution built on Google Cloud Platform (GCP). It processes retail customer, product, store, and order data through a multi-layered architecture (Bronze, Silver, and Gold) to provide clean, analytics-ready data for business reporting.

The project demonstrates an end-to-end Data Engineering workflow, including data generation, ingestion, transformation, validation, and business analytics.

---

## Architecture

```
CSV Files
    │
    ▼
Google Cloud Storage (GCS)
    │
    ▼
Bronze Layer (Raw Data)
    │
    ▼
Silver Layer (Cleaned Data)
    │
    ▼
Gold Layer (Star Schema)
    │
    ▼
Business Analytics
```

---

## Technology Stack

- Google Cloud Platform (GCP)
- Google BigQuery
- Google Cloud Storage (GCS)
- Python
- SQL
- Pandas
- Git & GitHub

---

## Project Structure

```
customer-360-analytics-platform/
│
├── architecture/
├── config/
├── dashboard/
├── data/
│   ├── raw/
│   └── processed/
├── docs/
├── logs/
├── python/
├── screenshots/
├── sql/
├── README.md
├── requirements.txt
└── .gitignore
```

---

## ETL Workflow

### Step 1 – Data Generation

Synthetic retail datasets were generated for:

- Customers
- Products
- Stores
- Orders

---

### Step 2 – Data Upload

CSV files were uploaded to Google Cloud Storage.

---

### Step 3 – Bronze Layer

Raw data was loaded into BigQuery without modification.

Tables:

- bronze_customers
- bronze_products
- bronze_stores
- bronze_orders

---

### Step 4 – Silver Layer

Data cleaning and standardisation included:

- Remove invalid records
- Trim spaces
- Standardise text
- Convert data types
- Basic data quality checks

---

### Step 5 – Gold Layer

A Star Schema was created with:

Dimension Tables

- dim_customer
- dim_product
- dim_store
- dim_date

Fact Table

- fact_sales

---

## Data Validation

The project includes validation for:

- Row count verification
- Referential integrity
- Data quality checks
- Business KPI validation

---

## Analytics

Example business insights include:

- Total Revenue
- Total Orders
- Average Order Value
- Top Customers
- Top Products
- Revenue by State
- Revenue by Region
- Monthly Sales Trend
- Revenue by Product Category
- Order Status Analysis

---

## How to Run

### Upload data

```bash
python python/upload_to_gcs.py
```

### Load Bronze tables

```bash
python python/load_bigquery.py
```

### Execute ETL

```bash
python python/run_sql.py
```

### Validate Pipeline

```bash
python python/validate_pipeline.py
```

### Run Analytics

```bash
python python/run_analytics.py
```

---

## Results

- Successfully processed 100,000 sales records
- Built a Star Schema in BigQuery
- Automated ETL validation
- Generated business analytics dashboards and KPIs

---

## Future Enhancements

- Cloud Composer orchestration
- Incremental loading
- CI/CD pipeline
- Unit testing
- Monitoring and alerting
- Dashboard integration with Looker Studio or Power BI

---

## Author

**Manjit Kumar Sharma**

Data Analytics | Data Engineering | Google Cloud | SQL | Python | Power BI