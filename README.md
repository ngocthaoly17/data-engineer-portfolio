# 👋 Portfolio Data Engineer — Ngoc Thao LY

Bienvenue sur mon portfolio de projets **Data Engineering**.

Ce repository regroupe plusieurs projets réalisés au cours de ma formation et de mon parcours professionnel. Ils illustrent différentes problématiques liées à la **collecte, la transformation, la qualité, le stockage et l'exploitation des données**, ainsi qu'à la conception d'architectures data.

---

## 👩‍💻 À propos de moi

Je suis **Data Engineer**, avec plusieurs années d'expérience dans le domaine de la Data, notamment en **Data Quality**.

J'ai travaillé sur des environnements manipulant d'importants volumes de données et sur des problématiques de :

- Data Engineering
- Data Quality
- pipelines de données
- SQL et bases de données
- architectures event-driven
- visualisation et exploitation des données

Ce portfolio présente des projets permettant de mettre en pratique ces compétences sur différentes architectures et problématiques métier.

---

## 🚀 Projets

### 1. Sport Data Solution — Architecture Event-Driven

Conception d'une architecture permettant de traiter des données d'activités sportives en temps réel.

Le projet met notamment en œuvre :

**PostgreSQL → Debezium → Redpanda/Kafka → Spark → Delta Lake → MinIO → Power BI**

Il comprend également :

- capture des changements de données avec le **CDC**
- traitement des événements en temps réel
- architecture **Bronze / Silver**
- règles métier liées aux avantages collaborateurs
- validation de trajets domicile-travail
- contrôles de qualité des données
- notifications Slack
- gestion de référentiels

**Technologies :** Python, PostgreSQL, Redpanda, Kafka, Debezium, Spark, Delta Lake, MinIO, Docker, Power BI.

---

### 2. Projet RAG — Recommandation d'événements culturels

Développement d'un **Proof of Concept utilisant une architecture RAG (Retrieval-Augmented Generation)** pour rechercher et recommander des événements culturels.

Le système combine :

- récupération de données événementielles
- génération d'embeddings
- recherche vectorielle
- récupération des événements les plus pertinents
- génération d'une réponse avec un LLM

**Technologies :** Python, FAISS, Mistral AI, embeddings, API, RAG.

Une réflexion sur le passage du **POC vers une architecture MVP scalable** a également été menée, notamment autour de PostgreSQL, pgvector, de l'indexation ANN, de la résilience et du découplage de l'ingestion.

---

### 3. Pipelines et traitement de données

Projets consacrés à la construction de pipelines permettant de :

- collecter des données depuis différentes sources
- nettoyer et transformer les données
- automatiser les traitements
- contrôler leur qualité
- préparer les données pour leur exploitation analytique

Ces projets mettent en pratique différents concepts fondamentaux du Data Engineering : **ETL/ELT, orchestration, transformation et monitoring**.

---

### 4. Data Quality

Travaux autour de la fiabilité et du contrôle des données.

Les problématiques abordées comprennent notamment :

- définition de règles de qualité
- détection d'anomalies
- contrôles de cohérence
- suivi d'indicateurs
- analyse des erreurs
- amélioration de la fiabilité des données

---

### 5. Analyse et visualisation de données

Projets orientés exploitation et restitution de données afin de transformer des données brutes en informations compréhensibles et exploitables.

**Technologies utilisées :** SQL, Python et Power BI.

---

### 6. Autres projets

Le portfolio contient également différents projets permettant d'explorer d'autres problématiques Data et de mettre en pratique les compétences acquises au cours de ma formation.

Chaque dossier contient son propre **README** présentant :

- le contexte du projet
- les objectifs
- l'architecture
- les technologies utilisées
- les principales étapes de réalisation
- les résultats obtenus

---

## 🛠️ Stack technique

### Data Engineering

`Python` • `SQL` • `PostgreSQL` • `Spark` • `Kafka` • `Redpanda` • `Debezium`

### Data Lake & stockage

`Delta Lake` • `MinIO` • `PostgreSQL`

### Data & BI

`Power BI` • `Snowflake`

### IA & recherche vectorielle

`RAG` • `FAISS` • `Mistral AI` • `Embeddings` • `Vector Search`

### DevOps & environnement

`Docker` • `Docker Compose` • `Git` • `GitHub`

---

## 🏗️ Compétences mises en pratique

À travers ces projets, j'ai notamment travaillé sur :

- conception d'architectures Data
- développement de pipelines ETL/ELT
- traitement batch et streaming
- architectures event-driven
- Change Data Capture (CDC)
- traitement distribué avec Spark
- stockage Data Lake / Lakehouse
- qualité et validation des données
- SQL et modélisation de données
- APIs et intégration de services externes
- recherche vectorielle et RAG
- containerisation avec Docker
- visualisation et restitution des données

---

## 📂 Organisation du repository

Chaque projet est disponible dans un dossier dédié.

```text
portfolio/
│
├── projet-1/
│   └── README.md
│
├── projet-2/
│   └── README.md
│
├── projet-3/
│   └── README.md
│
├── projet-4/
│   └── README.md
│
├── projet-5/
│   └── README.md
│
├── projet-6/
│   └── README.md
│
└── README.md
```

Les README individuels détaillent l'objectif, l'architecture et les choix techniques de chaque projet.

---

## 🎯 Objectif du portfolio

Ce portfolio permet de présenter concrètement ma capacité à intervenir sur différentes étapes du cycle de vie de la donnée :

**Collecter → Stocker → Transformer → Contrôler → Exposer → Valoriser**

Il reflète également ma progression vers des problématiques plus avancées de **Data Engineering**, notamment les architectures distribuées, le streaming, les architectures event-driven et l'intégration de solutions d'IA dans les systèmes Data.
