-- =====================================================
-- Customer 360 Analytics Platform
-- Silver → Gold Layer (Star Schema)
-- Author : Manjit Kumar Sharma
-- =====================================================

-- =====================================================
-- DIMENSION : CUSTOMER
-- =====================================================

CREATE OR REPLACE TABLE `customer360_dw.dim_customer` AS

SELECT DISTINCT

    customer_id,
    customer_name,
    gender,
    age,
    city,
    state,
    join_date

FROM `customer360_dw.silver_customers`;



-- =====================================================
-- DIMENSION : PRODUCT
-- =====================================================

CREATE OR REPLACE TABLE `customer360_dw.dim_product` AS

SELECT DISTINCT

    product_id,
    product_name,
    category,
    brand,
    unit_price

FROM `customer360_dw.silver_products`;



-- =====================================================
-- DIMENSION : STORE
-- =====================================================

CREATE OR REPLACE TABLE `customer360_dw.dim_store` AS

SELECT DISTINCT

    store_id,
    store_name,
    city,
    state,
    region

FROM `customer360_dw.silver_stores`;



-- =====================================================
-- DIMENSION : DATE
-- =====================================================

CREATE OR REPLACE TABLE `customer360_dw.dim_date` AS

SELECT DISTINCT

    order_date,

    EXTRACT(YEAR FROM order_date) AS year,

    EXTRACT(QUARTER FROM order_date) AS quarter,

    EXTRACT(MONTH FROM order_date) AS month,

    FORMAT_DATE('%B', order_date) AS month_name,

    EXTRACT(DAY FROM order_date) AS day,

    FORMAT_DATE('%A', order_date) AS day_name,

    EXTRACT(WEEK FROM order_date) AS week_number

FROM `customer360_dw.silver_orders`;



-- =====================================================
-- FACT : SALES
-- =====================================================

CREATE OR REPLACE TABLE `customer360_dw.fact_sales` AS

SELECT

    order_id,

    customer_id,

    product_id,

    store_id,

    order_date,

    quantity,

    unit_price,

    total_amount,

    payment_method,

    order_status

FROM `customer360_dw.silver_orders`;