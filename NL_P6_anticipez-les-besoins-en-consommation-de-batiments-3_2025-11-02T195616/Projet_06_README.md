# Projet 6 — Anticipez les besoins en consommation de bâtiments

## Contexte

La ville de Seattle vise la neutralité carbone à l’horizon 2050. Les relevés énergétiques détaillés étant coûteux, le projet cherche à prédire la consommation d’énergie et les émissions de CO₂ de bâtiments non résidentiels à partir de leurs caractéristiques.

Le jeu de données utilisé contient **3 376 lignes et 31 variables**.

## Travail réalisé

- Analyse exploratoire des données.
- Nettoyage et préparation des variables.
- Suppression des variables non pertinentes.
- Traitement des valeurs extrêmes.
- Suppression de variables fortement corrélées.
- Encodage des variables catégorielles.
- Imputation des valeurs manquantes.
- Feature engineering.
- Comparaison de plusieurs modèles supervisés.
- Évaluation avec R², MAE et RMSE.
- Analyse de l’importance des variables.
- Préparation du modèle pour un déploiement sous forme de service.

## Feature engineering

Plusieurs variables ont été créées, notamment :

- `AvgGFA_perFloor`
- `AvgGFA_perBuilding`
- `GHG_per_sqft`
- `DecadeBuilt`
- `IsCertified`

## Outils et technologies

- Python
- Pandas
- NumPy
- scikit-learn
- Jupyter Notebook
- BentoML
- Docker
- Google Cloud Run

## Résultats obtenus

Le modèle retenu dans la présentation est un modèle de type **Random Forest Regressor**, avec un **R² de test de 0,887**.

L’analyse de l’importance des variables montre que les émissions de GES sont notamment liées :

- à la consommation d’électricité ;
- à l’intensité des émissions par surface ;
- à la surface totale du bâtiment.

Le modèle a ensuite été préparé comme service avec **BentoML** et déployé sur **Google Cloud Run**.

## Compétences démontrées

- Préparation de données pour le Machine Learning.
- Analyse exploratoire.
- Feature engineering.
- Régression supervisée.
- Comparaison et évaluation de modèles.
- Optimisation et interprétation d’un modèle.
- Packaging d’un modèle ML.
- Déploiement d’un service de prédiction dans le cloud.

## Valeur ajoutée

Ce projet couvre le cycle complet d’un cas d’usage Machine Learning : compréhension du besoin, préparation des données, modélisation, évaluation, interprétation puis mise à disposition du modèle sous forme de service déployable.
