# Projet 8 — Construisez et testez une infrastructure de données

## Contexte

Dans le cadre du projet **Forecast 2.0**, GreenAndCoop souhaite améliorer ses modèles de prévision de demande électrique grâce à de nouvelles données météorologiques.

L’objectif Data Engineering est de fournir quotidiennement aux Data Scientists des données météo fiables issues de plusieurs sources et formats, dans une infrastructure AWS accessible aux futurs traitements Machine Learning.

## Architecture réalisée

Le pipeline suit le flux principal :

**Sources météo → Amazon S3 → AWS Lambda → MongoDB sur ECS**

L’arrivée d’un fichier dans S3 déclenche automatiquement une fonction Lambda chargée de parser, valider, transformer et charger les données dans MongoDB.

CloudWatch centralise les logs et les métriques.

## Outils et technologies

- AWS S3
- AWS Lambda
- AWS ECS
- Amazon ECR
- Amazon CloudWatch
- MongoDB
- Docker
- Python
- CSV / XLSX / Parquet

## Modèle de données

Plusieurs collections MongoDB permettent de séparer les usages :

- `infoclimat_raw` : données brutes conservées ;
- `wu_observations` : observations Weather Underground normalisées ;
- `infoclimat_hourly` : données agrégées à l’heure ;
- `data_quality_reports` : résultats des contrôles qualité.

## Qualité des données

Des contrôles sont appliqués sur les observations :

- validité des timestamps ;
- détection des doublons ;
- détection des valeurs aberrantes ;
- cohérence des températures ;
- cohérence des pressions.

Les rapports permettent d’identifier les règles en échec et les stations concernées.

## Tests de performance

Les requêtes sont exécutées plusieurs fois afin de mesurer :

- moyenne ;
- médiane / p50 ;
- p95 ;
- minimum ;
- maximum.

Cette approche permet d’évaluer l’accessibilité réelle des données pour les consommateurs du pipeline.

## Résultats obtenus

- Pipeline événementiel déclenché à l’arrivée des fichiers sur S3.
- Ingestion automatisée de données météo hétérogènes.
- Stockage MongoDB conteneurisé sur AWS ECS.
- Conservation des données brutes et création de données agrégées prêtes pour l’analyse.
- Mise en place de contrôles Data Quality.
- Centralisation des logs dans CloudWatch.
- Mesure des performances d’accès aux données.
- Proposition d’une table de rejets afin d’isoler les données ne respectant pas les règles qualité.

## Compétences démontrées

- Conception d’une architecture data cloud.
- AWS S3, Lambda, ECS, ECR et CloudWatch.
- Architecture événementielle.
- Conteneurisation Docker.
- MongoDB.
- Data Quality.
- Monitoring et mesure de performance.
- Préparation de données destinées au Machine Learning.

## Valeur ajoutée

Le projet démontre la capacité à construire une chaîne de données cloud complète, de l’arrivée du fichier jusqu’à sa mise à disposition pour les Data Scientists, avec **automatisation, contrôle qualité, observabilité et mesure de performance**.
