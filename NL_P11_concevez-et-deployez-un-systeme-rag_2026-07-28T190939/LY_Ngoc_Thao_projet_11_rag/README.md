# Projet 11 - Système RAG pour la recommandation d'événements culturels

## Contexte

Ce projet OpenClassrooms consiste à développer un Proof of Concept (POC) d'assistant conversationnel pour recommander des événements culturels. Le système s'appuie sur une architecture RAG (Retrieval-Augmented Generation) afin de répondre à partir de données réelles issues d'OpenAgenda.

Le périmètre retenu est l'agenda public **Culture Versailles** :

- Source : OpenAgenda
- Agenda UID : `60871835`
- Ville : Versailles
- Dataset final : 98 événements

## Architecture

```text
OpenAgenda API
    -> extraction et nettoyage
    -> data/events_versailles.csv
    -> documents LangChain
    -> embeddings Mistral
    -> index FAISS
    -> chatbot RAG
    -> interface Streamlit
```

## Structure du projet

```text
projet_11_rag_openclassrooms/
├── app.py
├── evaluate_rag.py
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── pytest.ini
├── architecture_rag_puls_events.drawio
├── POC_RAG_Puls-Events_Versailles.pptx
├── data/
│   ├── events_versailles.csv
│   ├── evaluation_dataset.csv
│   └── evaluation_results.csv
├── docs/
│   ├── rapport_technique_p11_rag.docx
│   └── rapport_technique_p11_rag.pdf
├── scripts/
│   └── run_tests.py
├── src/
│   ├── build_faiss.py
│   └── extract_openagenda.py
├── tests/
│   └── test_events.py
└── vectorstore/
    └── faiss_versailles/
        ├── index.faiss
        └── index.pkl
```

## Installation

### 1. Créer et activer l'environnement virtuel

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 2. Installer les dépendances

```powershell
python -m pip install -r requirements.txt
```

## Configuration

Créer un fichier `.env` à partir de `.env.example` :

```text
OPENAGENDA_API_KEY=your_openagenda_api_key
MISTRAL_API_KEY=your_mistral_api_key
```

Le fichier `.env` n'est pas livré afin de ne pas exposer les clés API.

## Extraction des événements

```powershell
python src/extract_openagenda.py
```

Ce script récupère les événements depuis OpenAgenda, filtre sur Versailles, conserve les événements de moins d'un an ou à venir, nettoie les champs principaux et supprime les doublons.

## Construction de l'index FAISS

```powershell
python src/build_faiss.py
```

Cette étape transforme les événements en Documents LangChain, génère les embeddings avec Mistral, puis sauvegarde l'index FAISS dans `vectorstore/faiss_versailles/`.

## Lancement de l'application Streamlit

```powershell
python -m streamlit run app.py
```

Exemples de questions :

- Je cherche un concert à Versailles
- Quels événements pour enfants sont disponibles ?
- Y a-t-il des expositions actuellement à Versailles ?

## Tests unitaires et pipeline

### Méthode directe

```powershell
python -m pytest
```

### Pipeline local

```powershell
python scripts/run_tests.py
```

Les tests vérifient notamment :

- l'existence du dataset nettoyé ;
- la présence des colonnes obligatoires ;
- le périmètre géographique Versailles ;
- la contrainte temporelle de moins d'un an ou à venir ;
- l'absence de champs obligatoires vides ;
- l'absence de doublons ;
- l'existence du jeu de test annoté ;
- l'existence de l'index FAISS.

## Évaluation du RAG

Le fichier `data/evaluation_dataset.csv` contient un jeu de questions/réponses attendues. Le script suivant exécute le RAG sur ce jeu d'évaluation :

```powershell
python evaluate_rag.py
```

Il produit `data/evaluation_results.csv` avec deux métriques :

- `semantic_similarity` : proximité sémantique entre la réponse générée et la réponse attendue ;
- `faithfulness` : fidélité de la réponse au contexte récupéré par FAISS.

## Livrables

- Code du système RAG
- Interface Streamlit
- Dataset OpenAgenda nettoyé
- Base vectorielle FAISS
- Tests unitaires intégrés sous forme de pipeline
- Jeu de test annoté et résultats d'évaluation
- Rapport technique dans `docs/`
- Présentation PowerPoint
- Architecture Draw.io
