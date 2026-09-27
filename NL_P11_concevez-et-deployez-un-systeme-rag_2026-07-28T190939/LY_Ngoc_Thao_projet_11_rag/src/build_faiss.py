"""
Construction de la base vectorielle FAISS pour le POC RAG Puls-Events.

Le script lit le dataset nettoyé, transforme chaque événement en Document
LangChain, génère les embeddings avec Mistral et sauvegarde l'index FAISS.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_mistralai import MistralAIEmbeddings


load_dotenv()

DATA_PATH = Path("data/events_versailles.csv")
VECTORSTORE_PATH = Path("vectorstore/faiss_versailles")


def load_events() -> pd.DataFrame:
    """Charge le fichier CSV nettoyé et supprime les lignes incomplètes."""
    df = pd.read_csv(DATA_PATH)
    df = df.dropna(subset=["title", "description", "city", "begin_date"])
    return df


def create_documents(df: pd.DataFrame) -> list[Document]:
    """
    Transforme les événements en Documents LangChain.

    Stratégie de chunking : un événement OpenAgenda correspond à un document
    LangChain et donc à un chunk unique.
    """
    documents = []

    for _, row in df.iterrows():
        content = f"""
Titre : {row['title']}
Ville : {row['city']}
Date : {row['date']}
Description : {row['description']}
URL : {row.get('url', '')}
""".strip()

        metadata = {
            "title": row["title"],
            "city": row["city"],
            "date": row["date"],
            "begin_date": row["begin_date"],
            "url": row.get("url", ""),
        }

        documents.append(Document(page_content=content, metadata=metadata))

    return documents


def build_vectorstore(documents: list[Document]) -> FAISS:
    """Génère les embeddings Mistral et construit l'index FAISS local."""
    embeddings = MistralAIEmbeddings(model="mistral-embed")

    vectorstore = FAISS.from_documents(
        documents=documents,
        embedding=embeddings,
    )

    VECTORSTORE_PATH.parent.mkdir(exist_ok=True)
    vectorstore.save_local(str(VECTORSTORE_PATH))

    return vectorstore


def test_search(vectorstore: FAISS) -> None:
    """Exécute une recherche sémantique simple pour contrôler l'index."""
    query = "Je cherche un concert à Versailles"
    results = vectorstore.similarity_search(query, k=3)

    print("\nRésultats de test :")
    for index, doc in enumerate(results, start=1):
        print(f"\n--- Résultat {index} ---")
        print("Titre :", doc.metadata.get("title"))
        print("Date :", doc.metadata.get("date"))
        print("Ville :", doc.metadata.get("city"))
        print("Description :", doc.page_content[:300])


def main() -> None:
    """Construit la base FAISS complète à partir du dataset nettoyé."""
    df = load_events()
    print(f"{len(df)} événements chargés depuis {DATA_PATH}")

    documents = create_documents(df)
    print(f"{len(documents)} documents créés")

    vectorstore = build_vectorstore(documents)
    print(f"Base FAISS sauvegardée dans {VECTORSTORE_PATH}")

    test_search(vectorstore)


if __name__ == "__main__":
    main()
