"""
Tests unitaires du POC RAG Puls-Events.

Les tests vérifient la qualité du dataset nettoyé, le périmètre géographique,
la contrainte temporelle demandée par la mission, le jeu d'évaluation et la
présence de l'index vectoriel FAISS. Ils ne font aucun appel réseau.
"""

from __future__ import annotations

import os
from pathlib import Path

import pandas as pd


DATA_PATH = Path("data/events_versailles.csv")
EVALUATION_PATH = Path("data/evaluation_dataset.csv")
VECTORSTORE_PATH = Path("vectorstore/faiss_versailles")

reference_date_value = os.getenv("PROJECT_REFERENCE_DATE")
REFERENCE_DATE = (
    pd.Timestamp(reference_date_value, tz="UTC")
    if reference_date_value
    else pd.Timestamp.now(tz="UTC")
)


def load_dataset() -> pd.DataFrame:
    """Charge le dataset nettoyé des événements."""
    return pd.read_csv(DATA_PATH)


def test_events_file_exists() -> None:
    """Le fichier CSV nettoyé doit exister."""
    assert DATA_PATH.exists(), f"Missing dataset: {DATA_PATH}"


def test_events_dataset_is_not_empty() -> None:
    """Le dataset nettoyé ne doit pas être vide."""
    df = load_dataset()
    assert len(df) > 0, "The events dataset is empty."


def test_required_columns_exist() -> None:
    """Le dataset doit contenir les colonnes nécessaires au RAG."""
    df = load_dataset()
    required_columns = {"title", "description", "city", "date", "begin_date", "url"}
    missing_columns = required_columns - set(df.columns)
    assert not missing_columns, f"Missing columns: {missing_columns}"


def test_all_events_are_in_versailles() -> None:
    """Tous les événements doivent respecter le périmètre Versailles."""
    df = load_dataset()
    invalid_rows = df[df["city"].str.lower().str.strip() != "versailles"]
    assert invalid_rows.empty, "Some events are not located in Versailles."


def test_events_are_recent_or_upcoming() -> None:
    """Tous les événements doivent dater de moins d'un an ou être à venir."""
    df = load_dataset()
    begin_dates = pd.to_datetime(df["begin_date"], utc=True, errors="coerce")
    assert begin_dates.notna().all(), "Some begin_date values are invalid."

    one_year_ago = REFERENCE_DATE - pd.Timedelta(days=365)
    old_events = df[begin_dates < one_year_ago]
    assert old_events.empty, "Some events are older than one year."


def test_no_duplicates() -> None:
    """Les doublons métier doivent être absents du dataset."""
    df = load_dataset()
    duplicates = df.duplicated(subset=["title", "begin_date", "city"]).sum()
    assert duplicates == 0, f"{duplicates} duplicates found in the dataset."


def test_no_missing_required_fields() -> None:
    """Les champs principaux utilisés par le RAG ne doivent pas être vides."""
    df = load_dataset()

    for column in ["title", "description", "city"]:
        assert df[column].notna().all(), f"Some events have no {column}."
        assert (df[column].astype(str).str.strip() != "").all(), (
            f"Some {column} values are empty."
        )


def test_evaluation_dataset_exists_and_is_valid() -> None:
    """Le jeu d'évaluation annoté doit être présent et exploitable."""
    assert EVALUATION_PATH.exists(), f"Missing evaluation dataset: {EVALUATION_PATH}"

    df = pd.read_csv(EVALUATION_PATH)
    required_columns = {"question", "expected_answer"}
    missing_columns = required_columns - set(df.columns)

    assert not missing_columns, f"Missing evaluation columns: {missing_columns}"
    assert not df.empty, "The evaluation dataset is empty."
    assert df["question"].notna().all(), "Some evaluation questions are missing."
    assert df["expected_answer"].notna().all(), (
        "Some expected answers are missing."
    )


def test_vectorstore_files_exist() -> None:
    """L'index FAISS local doit être présent après la vectorisation."""
    assert (VECTORSTORE_PATH / "index.faiss").exists(), "Missing index.faiss file."
    assert (VECTORSTORE_PATH / "index.pkl").exists(), "Missing index.pkl file."
