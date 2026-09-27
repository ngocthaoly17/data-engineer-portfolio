CREATE OR REPLACE TABLE donnees_fusionnees AS
SELECT
    e.product_id,
    l.id_web,
    w.sku,
    w.post_title AS nom_produit,
    e.price AS prix,
    w.total_sales,
    e.stock_quantity,
    e.stock_status
FROM erp_clean e
INNER JOIN liaison_clean l
    ON e.product_id = l.product_id
INNER JOIN web_clean w
    ON l.id_web = w.sku;
