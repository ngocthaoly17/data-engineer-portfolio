# Projet 9 — Modélisez une infrastructure dans le cloud

## Contexte

InduTechData dispose d’un système d’information on-premise comprenant notamment un cluster SQL Server de **40 To**, un SAN de **10 To**, Active Directory et plusieurs applications métier.

La croissance des flux IoT impose de moderniser cette infrastructure sans abandonner les systèmes existants. Le projet consiste donc à concevoir une **architecture hybride on-premise / AWS**, capable de gérer à la fois les traitements batch et les flux temps réel.

## Architecture proposée

### Données batch

**SQL Server → AWS DMS → Amazon S3 → Amazon Redshift**

AWS DMS permet d’effectuer la réplication initiale puis les mises à jour incrémentales grâce au CDC.

### Données temps réel

**Sources IoT → Redpanda → Amazon S3 → Amazon Redshift**

Redpanda fournit une couche de streaming compatible avec l’écosystème Kafka.

### Fichiers du SAN

**SAN → AWS DataSync → Amazon S3**

### Identités

**Active Directory on-premise → AWS Directory Service**

### Réseau

Le réseau de l’entreprise est relié au VPC AWS via un **Site-to-Site VPN IPsec**, avec une évolution possible vers Direct Connect.

## Outils et technologies

- Amazon Web Services
- Amazon S3
- Amazon Redshift
- AWS DMS
- AWS DataSync
- AWS Directory Service
- AWS IAM
- AWS KMS
- AWS Site-to-Site VPN
- AWS Direct Connect
- CloudWatch / CloudTrail
- Redpanda
- Docker
- Apache Spark
- Python

## Prototype streaming

Un prototype permet de valider une partie de la chaîne temps réel avec :

- un producteur Python ;
- Redpanda ;
- des topics compatibles Kafka ;
- un consommateur / traitement Spark ;
- Docker Compose pour reproduire l’environnement.

## Sécurité

L’architecture applique notamment :

- le principe du moindre privilège avec IAM ;
- le chiffrement des données au repos ;
- AWS KMS pour la gestion des clés ;
- TLS et IPsec pour les données en transit ;
- une séparation réseau via le VPC ;
- des mécanismes d’audit et de supervision.

## Scalabilité

Chaque couche peut évoluer indépendamment :

- S3 adapte automatiquement sa capacité ;
- DMS peut augmenter sa capacité de réplication ;
- Redshift peut évoluer en capacité ou fonctionner en Serverless ;
- Redpanda peut augmenter brokers et partitions ;
- la liaison hybride peut évoluer du VPN vers Direct Connect.

## Résultats obtenus

- Conception d’une architecture hybride conservant le SI historique.
- Séparation claire des flux batch et temps réel.
- Intégration d’un mécanisme CDC pour SQL Server.
- Proposition d’une stratégie de stockage et d’analyse AWS.
- Intégration des contraintes de sécurité et de gestion des identités.
- Prototype de streaming Redpanda / Spark conteneurisé.

## Compétences démontrées

- Architecture cloud hybride.
- AWS.
- Streaming événementiel.
- Kafka / Redpanda.
- Spark.
- CDC et réplication.
- Sécurité cloud.
- IAM et gestion des identités.
- Scalabilité et haute disponibilité.

## Valeur ajoutée

Ce projet démontre la capacité à concevoir une architecture cloud réaliste en tenant compte d’un **SI existant**, des contraintes de migration, de sécurité et de performance, plutôt que de proposer une architecture cloud isolée du contexte de l’entreprise.
