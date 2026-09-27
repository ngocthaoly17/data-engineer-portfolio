"""
Évaluation automatique simplifiée du RAG Puls-Events.

Le script lit data/evaluation_dataset.csv, interroge le RAG pour chaque
question, calcule deux métriques de qualité et exporte les résultats dans
 data/evaluation_results.csv :
- semantic_similarity : proximité entre réponse générée et réponse attendue ;
- faithfulness : fidélité de la réponse au contexte récupéré dans FAISS.
"""

from __future__ import annotations

import json

import numpy as np
import pandas as pd
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI, MistralAIEmbeddings


load_dotenv()

embeddings = MistralAIEmbeddings(model="mistral-embed")
llm = ChatMistralAI(model="mistral-small-latest", temperature=0.2)

vectorstore = FAISS.load_local(
    "vectorstore/faiss_versailles",
    embeddings,
    allow_dangerous_deserialization=True,
)


def generate_answer(question: str, context: str) -> str:
    """Génère une réponse à partir de la question et du contexte FAISS."""
    prompt = ChatPromptTemplate.from_template(
        """
Réponds uniquement à partir du contexte fourni.

Contexte :
{context}

Question :
{question}

Réponse :
"""
    )

    response = (prompt | llm).invoke({"context": context, "question": question})
    return str(response.content)


def semantic_similarity(answer: str, expected_answer: str) -> float:
    """Compare le sens de la réponse générée avec la réponse attendue."""
    vectors = embeddings.embed_documents([str(answer), str(expected_answer)])

    vector_a = np.array(vectors[0])
    vector_b = np.array(vectors[1])

    denominator = np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
    if denominator == 0:
        return 0.0

    return float(np.dot(vector_a, vector_b) / denominator)


def faithfulness(answer: str, context: str) -> float:
    """Évalue si la réponse reste fidèle aux informations du contexte."""
    prompt = ChatPromptTemplate.from_template(
        """
Évalue si la réponse est fidèle au contexte fourni.

Donne un score entre 0 et 1.
Retourne uniquement un JSON valide :
{{"score": 0.0}}

Contexte :
{context}

Réponse :
{answer}
"""
    )

    response = (prompt | llm).invoke({"context": context, "answer": answer})
    cleaned_response = str(response.content).strip()
    cleaned_response = cleaned_response.replace("```json", "").replace("```", "")
    cleaned_response = cleaned_response.strip()

    return float(json.loads(cleaned_response)["score"])


def main() -> None:
    """Lance l'évaluation du RAG sur le jeu de questions annoté."""
    evaluation_df = pd.read_csv("data/evaluation_dataset.csv")
    evaluation_df = evaluation_df.dropna(subset=["question", "expected_answer"])

    results = []

    for index, row in evaluation_df.iterrows():
        question = str(row["question"])
        expected_answer = str(row["expected_answer"])

        print(f"[{index + 1}/{len(evaluation_df)}] {question}")

        documents = vectorstore.similarity_search(question, k=4)
        context = "\n\n".join(str(doc.page_content) for doc in documents)

        answer = generate_answer(question, context)
        similarity = semantic_similarity(answer, expected_answer)
        faithfulness_score = faithfulness(answer, context)

        results.append(
            {
                "question": question,
                "expected_answer": expected_answer,
                "generated_answer": answer,
                "semantic_similarity": similarity,
                "faithfulness": faithfulness_score,
                "retrieved_documents": " | ".join(
                    str(doc.metadata.get("title", "")) for doc in documents
                ),
            }
        )

    results_df = pd.DataFrame(results)

    if results_df.empty:
        print("Aucune question n'a été évaluée.")
        return

    results_df.to_csv(
        "data/evaluation_results.csv",
        index=False,
        sep=";",
        encoding="utf-8-sig",
    )

    print("\nRÉSULTATS MOYENS")
    print("Similarité sémantique :", round(results_df["semantic_similarity"].mean(), 3))
    print("Faithfulness :", round(results_df["faithfulness"].mean(), 3))
    print("\nRésultats sauvegardés dans data/evaluation_results.csv")


if __name__ == "__main__":
    main()
