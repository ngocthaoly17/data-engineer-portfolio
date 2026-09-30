# Projet 7 — Concevez et analysez une base de données NoSQL

## Contexte

L’association **NosCités** analyse les locations de courte durée à Paris et Lyon afin d’évaluer leur impact sur l’offre de logements. Après un incident ayant provoqué la perte de la base parisienne, le projet consiste à restaurer les données, vérifier leur intégrité et rendre l’architecture MongoDB plus résiliente.

## Travail réalisé

- Restauration et import des données de locations.
- Exploration de documents MongoDB semi-structurés.
- Réalisation de requêtes analytiques sur les logements et les hôtes.
- Analyses complémentaires avec Polars.
- Utilisation de MongoDB Atlas et Data Federation.
- Connexion des données à Power BI.
- Mise en place et test d’un **Replica Set MongoDB** en local.
- Simulation d’un PRIMARY, d’un SECONDARY et d’un arbitre.
- Vérification de la réplication après insertion de données.
- Mise en place d’une architecture de **sharding**.
- Répartition des données de Paris et Lyon sur des shards distincts.
- Analyse du routage des requêtes avec `explain("executionStats")`.

## Outils et technologies

- MongoDB
- MongoDB Atlas
- MongoDB Data Federation
- MongoDB Replica Sets
- MongoDB Sharding
- Python
- Polars
- Power BI
- Mongo Shell / mongosh

## Analyses réalisées

Le projet permet notamment d’étudier :

- le nombre d’annonces par type de location ;
- les annonces possédant le plus d’évaluations ;
- le nombre d’hôtes distincts ;
- la proportion de logements réservables instantanément ;
- les hôtes possédant plus de 100 annonces ;
- la proportion de super-hôtes ;
- le taux de réservation moyen par mois et par type de logement ;
- la densité de logements par quartier ;
- les quartiers présentant les taux de réservation les plus élevés.

## Résultats obtenus

- Base MongoDB restaurée et vérifiée.
- Architecture de réplication testée avec succès.
- Mise en œuvre d’un cluster shardé permettant de répartir les données selon leur localisation.
- Validation de la distribution des requêtes entre Paris et Lyon.
- Connexion de la base à un outil de BI.
- Recommandations pour automatiser les sauvegardes, surveiller le balancer et créer des index adaptés aux requêtes métier.

## Compétences démontrées

- Modélisation et interrogation d’une base NoSQL.
- Administration MongoDB.
- Analyse de données semi-structurées.
- Haute disponibilité avec Replica Sets.
- Scalabilité horizontale avec le sharding.
- Analyse de performance des requêtes.
- Intégration MongoDB / Power BI.

## Valeur ajoutée

Ce projet démontre la capacité à aller au-delà de l’utilisation fonctionnelle d’une base NoSQL en intégrant des problématiques de **résilience, réplication, disponibilité et scalabilité**, essentielles pour exploiter MongoDB dans un environnement de production.
