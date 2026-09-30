# Projet 4 — Auditez un environnement de données

## Contexte

SuperSmartMarket utilise un entrepôt OLAP et Power BI pour piloter ses activités. Des incohérences ont été observées dans le chiffre d’affaires : une même journée peut afficher des montants différents selon le moment où le reporting est consulté.

Un exemple identifié concerne le 14 août, dont le chiffre d’affaires est passé de **275 186,59 € à 284 243,88 €** sans justification opérationnelle évidente.

## Objectif

Auditer l’environnement de données afin de comprendre l’origine des écarts, reconstruire une base fiable et proposer des mécanismes permettant d’améliorer la traçabilité.

## Travail réalisé

- Analyse de l’architecture et des données existantes.
- Reconstruction d’un prototype local sous PostgreSQL.
- Création d’un schéma relationnel.
- Création d’un dictionnaire de données.
- Import et harmonisation des données.
- Recalcul d’indicateurs de chiffre d’affaires.
- Comparaison des résultats avec le reporting Power BI.
- Analyse des causes possibles des variations historiques.
- Proposition de mesures correctives.

## Outils et technologies

- PostgreSQL
- SQL
- Power BI
- Modélisation relationnelle
- Triggers
- Journalisation / audit logs
- Versioning des données

## Résultats obtenus

L’audit a mis en évidence plusieurs risques :

- données historiques susceptibles d’être modifiées ;
- absence de documentation suffisante ;
- manque de traçabilité des transformations ;
- écarts entre les résultats reconstruits localement et les indicateurs du reporting.

Le prototype propose notamment :

- des **triggers et logs d’audit** enregistrant ancienne valeur, nouvelle valeur, auteur et date de modification ;
- une table d’historique `sales_history` permettant de rejouer l’état des ventes à une date donnée ;
- des procédures centralisant les règles de calcul des indicateurs.

## Compétences démontrées

- Audit d’un environnement data.
- Investigation d’anomalies.
- Data Quality.
- SQL et PostgreSQL.
- Modélisation et documentation.
- Traçabilité et historisation.
- Analyse des risques liés aux données.

## Valeur ajoutée

Le projet ne se limite pas à constater une anomalie : il propose une architecture de contrôle permettant de comprendre les modifications rétroactives, de reproduire les calculs et d’améliorer la confiance dans les reportings.
