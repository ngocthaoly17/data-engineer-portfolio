CREATE OR REPLACE TABLE ca_produit AS
SELECT
    *,
    CAST(prix * total_sales AS DOUBLE) AS chiffre_affaires
FROM donnees_fusionnees;

CREATE OR REPLACE TABLE ca_global AS
SELECT
    ROUND(SUM(chiffre_affaires), 2) AS chiffre_affaires_global,
    COUNT(*) AS nombre_produits
FROM ca_produit;
