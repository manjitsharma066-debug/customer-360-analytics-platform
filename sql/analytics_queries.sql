-- =====================================================
-- Customer 360 Analytics Platform
-- Business Analytics Queries
-- Author : Manjit Kumar Sharma
-- =====================================================

-- =====================================================
-- KPI 1 : Total Revenue
-- =====================================================

SELECT

    SUM(total_amount) AS total_revenue

FROM `customer360_dw.fact_sales`;



-- =====================================================
-- KPI 2 : Total Orders
-- =====================================================

SELECT

    COUNT(order_id) AS total_orders

FROM `customer360_dw.fact_sales`;



-- =====================================================
-- KPI 3 : Average Order Value
-- =====================================================

SELECT

    ROUND(AVG(total_amount), 2) AS average_order_value

FROM `customer360_dw.fact_sales`;



-- =====================================================
-- KPI 4 : Top 10 Customers by Revenue
-- =====================================================

SELECT

    customer_id,

    SUM(total_amount) AS total_revenue

FROM `customer360_dw.fact_sales`

GROUP BY customer_id

ORDER BY total_revenue DESC

LIMIT 10;



-- =====================================================
-- KPI 5 : Top 10 Products by Revenue
-- =====================================================

SELECT

    p.product_name,

    SUM(f.total_amount) AS total_revenue

FROM `customer360_dw.fact_sales` AS f

INNER JOIN `customer360_dw.dim_product` AS p

ON f.product_id = p.product_id

GROUP BY p.product_name

ORDER BY total_revenue DESC

LIMIT 10;



-- =====================================================
-- KPI 6 : Revenue by State
-- =====================================================

SELECT

    c.state,

    SUM(f.total_amount) AS total_revenue

FROM `customer360_dw.fact_sales` AS f

INNER JOIN `customer360_dw.dim_customer` AS c

ON f.customer_id = c.customer_id

GROUP BY c.state

ORDER BY total_revenue DESC;



-- =====================================================
-- KPI 7 : Revenue by Region
-- =====================================================

SELECT

    s.region,

    SUM(f.total_amount) AS total_revenue

FROM `customer360_dw.fact_sales` AS f

INNER JOIN `customer360_dw.dim_store` AS s

ON f.store_id = s.store_id

GROUP BY s.region

ORDER BY total_revenue DESC;



-- =====================================================
-- KPI 8 : Monthly Sales Trend
-- =====================================================

SELECT

    d.year,

    d.month,

    d.month_name,

    SUM(f.total_amount) AS total_revenue

FROM `customer360_dw.fact_sales` AS f

INNER JOIN `customer360_dw.dim_date` AS d

ON f.order_date = d.order_date

GROUP BY

    d.year,
    d.month,
    d.month_name

ORDER BY

    d.year,
    d.month;



-- =====================================================
-- KPI 9 : Category-wise Revenue
-- =====================================================

SELECT

    p.category,

    SUM(f.total_amount) AS total_revenue

FROM `customer360_dw.fact_sales` AS f

INNER JOIN `customer360_dw.dim_product` AS p

ON f.product_id = p.product_id

GROUP BY p.category

ORDER BY total_revenue DESC;



-- =====================================================
-- KPI 10 : Order Status Analysis
-- =====================================================

SELECT

    order_status,

    COUNT(order_id) AS total_orders,

    ROUND(SUM(total_amount), 2) AS total_revenue

FROM `customer360_dw.fact_sales`

GROUP BY order_status

ORDER BY total_orders DESC;