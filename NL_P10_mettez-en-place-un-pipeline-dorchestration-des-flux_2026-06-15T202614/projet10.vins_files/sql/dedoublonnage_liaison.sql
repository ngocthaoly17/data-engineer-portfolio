CREATE OR REPLACE TABLE liaison_clean AS
SELECT
    product_id,
    id_web
FROM (
    SELECT
        product_id,
        id_web,
        ROW_NUMBER() OVER (
            PARTITION BY product_id
            ORDER BY id_web
        ) AS numero_ligne
    FROM liaison
    WHERE product_id IS NOT NULL
      AND id_web IS NOT NULL
)
WHERE numero_ligne = 1;
