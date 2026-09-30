# Projet 10 — Mettez en place un pipeline d’orchestration des flux

## Contexte

BottleNeck exploite plusieurs sources de données pour suivre ses produits et ses ventes : un système ERP, un site e-commerce et un fichier de liaison entre les deux systèmes.

Les traitements étaient initialement manuels, avec des risques d’erreurs et une perte de productivité. Le projet consiste à industrialiser ce processus grâce à un pipeline automatisé et orchestré.

## Architecture

Le pipeline repose sur trois composants principaux :

- **Kestra** pour l’orchestration, la planification, les triggers et la supervision du workflow ;
- **Python** pour le nettoyage, le dédoublonnage et les traitements métier ;
- **DuckDB** pour les opérations SQL de fusion et de calcul.

## Étapes du pipeline

1. Vérification de la présence des trois fichiers sources.
2. Ingestion et normalisation.
3. Nettoyage des données ERP.
4. Nettoyage du fichier de liaison.
5. Nettoyage des données web.
6. Dédoublonnage des trois sources.
7. Exécution des tests qualité.
8. Fusion des données avec DuckDB.
9. Contrôle de cohérence de la fusion.
10. Calcul du chiffre d’affaires.
11. Contrôle du chiffre d’affaires.
12. Calcul du Z-score des prix.
13. Classification des vins.
14. Export des résultats.

Le workflow s’arrête automatiquement lorsqu’un contrôle critique échoue.

## Outils et technologies

- Kestra
- Python
- DuckDB
- SQL
- Docker
- Pytest
- YAML
- Cron

## Qualité des données

Le pipeline applique notamment :

- dédoublonnage sur `product_id` pour l’ERP ;
- dédoublonnage sur `sku` pour les données web ;
- suppression des lignes incomplètes sur les clés et champs métier essentiels ;
- contrôle des valeurs manquantes ;
- contrôle de la cohérence des jointures ;
- contrôle du chiffre d’affaires ;
- contrôle de la classification finale.

## Détection des vins premium

Les vins premium sont identifiés grâce au **Z-score** appliqué au prix.

Un vin est considéré comme premium lorsque :

`z > 2.0`

Cette méthode permet d’identifier statistiquement les prix significativement supérieurs à la moyenne du catalogue.

## Résultats obtenus

- **714 produits analysés**
- **30 vins premium détectés**
- **Pipeline 100 % automatisé**

Exports produits :

- `vins_premium.csv`
- `vins_ordinaires.csv`
- `rapport_ca.xlsx`
- `donnees_fusionnees.csv`

## Tests automatisés

Le workflow intègre plusieurs contrôles :

- absence de doublons ;
- absence de valeurs manquantes critiques ;
- cohérence du chiffre d’affaires ;
- cohérence de la classification premium / ordinaire ;
- cohérence de la fusion des sources.

## Orchestration

Le pipeline est planifié automatiquement avec l’expression Cron :

`0 9 15 * *`

Il s’exécute donc **le 15 de chaque mois à 9 h**.

## Compétences démontrées

- Orchestration de workflows data.
- Automatisation de pipelines.
- Kestra.
- Python et SQL.
- DuckDB.
- Data Quality.
- Tests automatisés.
- Gestion des erreurs.
- Planification Cron.
- Industrialisation d’un traitement manuel.

## Valeur ajoutée

Le projet transforme une analyse manuelle en **pipeline industrialisé, testable et reproductible**. Les équipes métier disposent automatiquement de données fusionnées, du chiffre d’affaires et d’une classification des produits, tandis que les contrôles intégrés réduisent le risque de diffuser des résultats incohérents.
