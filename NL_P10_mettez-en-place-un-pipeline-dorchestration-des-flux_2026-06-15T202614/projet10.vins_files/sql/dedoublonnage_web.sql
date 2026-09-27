CREATE OR REPLACE TABLE web_clean AS
SELECT
    sku,
    post_title,
    total_sales,
    post_type,
    post_modified
FROM (
    SELECT
        sku,
        post_title,
        total_sales,
        post_type,
        post_modified,
        ROW_NUMBER() OVER (
            PARTITION BY sku
            ORDER BY post_modified DESC NULLS LAST
        ) AS numero_ligne
    FROM web
    WHERE sku IS NOT NULL
      AND total_sales IS NOT NULL
      AND post_type = 'product'
)
WHERE numero_ligne = 1;
