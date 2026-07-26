-- =====================================================
-- PRODUCT TABLE
-- =====================================================

CREATE OR REPLACE TABLE `customer360_dw.silver_products` AS

SELECT DISTINCT

    product_id,

    TRIM(product_name) AS product_name,

    INITCAP(TRIM(category)) AS category,

    INITCAP(TRIM(brand)) AS brand,

    unit_price

FROM `customer360_dw.bronze_products`

WHERE unit_price > 0;