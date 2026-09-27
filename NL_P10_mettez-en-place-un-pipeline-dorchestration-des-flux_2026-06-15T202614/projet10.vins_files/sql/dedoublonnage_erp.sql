CREATE OR REPLACE TABLE erp_clean AS
SELECT
    product_id,
    onsale_web,
    price,
    stock_quantity,
    stock_status
FROM (
    SELECT
        *,
        ROW_NUMBER() OVER (
            PARTITION BY product_id
            ORDER BY product_id
        ) AS numero_ligne
    FROM erp
    WHERE product_id IS NOT NULL
      AND price IS NOT NULL
)
WHERE numero_ligne = 1;
