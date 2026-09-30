# Projet 5 — Maintenez et documentez un système de stockage sécurisé et performant

## Contexte

DataSoluTech doit faire évoluer le stockage d’un jeu de données médicales contenant des informations patients. Le projet étudie la migration depuis un stockage relationnel vers MongoDB, avec un objectif de performance, de portabilité, de sécurité et de scalabilité.

## Travail réalisé

- Analyse du dataset médical.
- Définition d’un modèle documentaire MongoDB.
- Nettoyage des données avant migration.
- Développement d’un script Python de migration.
- Insertion automatisée des documents dans MongoDB.
- Conteneurisation de MongoDB et du processus de migration.
- Mise en place d’utilisateurs et de rôles.
- Création d’index.
- Documentation et versioning du projet.
- Étude de plusieurs options de déploiement AWS.

## Outils et technologies

- MongoDB
- Python
- Pandas
- Docker
- Docker Compose
- Git / GitHub
- AWS : DocumentDB, EC2, ECS/EKS, S3

## Traitements réalisés

Le nettoyage comprend notamment :

- suppression des doublons ;
- gestion des valeurs manquantes ;
- uniformisation des noms ;
- conversion des âges en entiers ;
- conversion des montants en nombres décimaux.

La migration transforme ensuite les lignes nettoyées en documents et utilise une insertion en masse avec `insert_many()`.

## Sécurité

Trois profils sont documentés :

- **admin** : administration globale ;
- **data_engineer** : lecture/écriture sur la base métier ;
- **analyst** : accès en lecture seule.

Des index sont également prévus sur des champs utilisés pour les recherches.

## Résultats obtenus

- Migration automatisée de données médicales vers MongoDB.
- Environnement reproductible avec Docker Compose.
- Données nettoyées avant insertion.
- Gestion des droits selon les responsabilités.
- Documentation des commandes d’exploitation.
- Comparaison de solutions AWS pour préparer un futur déploiement cloud.

## Compétences démontrées

- Modélisation NoSQL.
- Administration MongoDB.
- Migration de données.
- Python et Pandas.
- Conteneurisation.
- Sécurisation des accès.
- Indexation.
- Analyse d’options cloud.

## Valeur ajoutée

Le projet démontre la capacité à faire évoluer un système de stockage vers une architecture NoSQL tout en intégrant dès la conception les problématiques de qualité des données, sécurité, automatisation, documentation et déploiement.
