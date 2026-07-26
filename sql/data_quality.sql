-- =====================================================
-- Customer 360 Analytics Platform
-- Data Quality Validation Report
-- Author : Manjit Kumar Sharma
-- =====================================================

-- =====================================================
-- CHECK 1 : Duplicate Order IDs
-- =====================================================

SELECT

    'Duplicate Order IDs' AS check_name,

    COUNT(*) AS issue_count

FROM (

    SELECT

        order_id

    FROM `customer360_dw.fact_sales`

    GROUP BY order_id

    HAVING COUNT(*) > 1

);



-- =====================================================
-- CHECK 2 : NULL Customer IDs
-- =====================================================

SELECT

    'NULL Customer IDs' AS check_name,

    COUNT(*) AS issue_count

FROM `customer360_dw.fact_sales`

WHERE customer_id IS NULL;



-- =====================================================
-- CHECK 3 : NULL Product IDs
-- =====================================================

SELECT

    'NULL Product IDs' AS check_name,

    COUNT(*) AS issue_count

FROM `customer360_dw.fact_sales`

WHERE product_id IS NULL;



-- =====================================================
-- CHECK 4 : NULL Store IDs
-- =====================================================

SELECT

    'NULL Store IDs' AS check_name,

    COUNT(*) AS issue_count

FROM `customer360_dw.fact_sales`

WHERE store_id IS NULL;



-- =====================================================
-- CHECK 5 : Invalid Quantity
-- =====================================================

SELECT

    'Invalid Quantity' AS check_name,

    COUNT(*) AS issue_count

FROM `customer360_dw.fact_sales`

WHERE quantity <= 0;



-- =====================================================
-- CHECK 6 : Invalid Unit Price
-- =====================================================

SELECT

    'Invalid Unit Price' AS check_name,

    COUNT(*) AS issue_count

FROM `customer360_dw.fact_sales`

WHERE unit_price <= 0;



-- =====================================================
-- CHECK 7 : Invalid Total Amount
-- =====================================================

SELECT

    'Invalid Total Amount' AS check_name,

    COUNT(*) AS issue_count

FROM `customer360_dw.fact_sales`

WHERE total_amount <> quantity * unit_price;



-- =====================================================
-- CHECK 8 : Invalid Order Status
-- =====================================================

SELECT

    'Invalid Order Status' AS check_name,

    COUNT(*) AS issue_count

FROM `customer360_dw.fact_sales`

WHERE order_status NOT IN (

    'Delivered',
    'Cancelled',
    'Returned'

);



-- =====================================================
-- CHECK 9 : Future Order Dates
-- =====================================================

SELECT

    'Future Order Dates' AS check_name,

    COUNT(*) AS issue_count

FROM `customer360_dw.fact_sales`

WHERE order_date > CURRENT_DATE();



-- =====================================================
-- CHECK 10 : Duplicate Customers
-- =====================================================

SELECT

    'Duplicate Customers' AS check_name,

    COUNT(*) AS issue_count

FROM (

    SELECT

        customer_id

    FROM `customer360_dw.dim_customer`

    GROUP BY customer_id

    HAVING COUNT(*) > 1

);