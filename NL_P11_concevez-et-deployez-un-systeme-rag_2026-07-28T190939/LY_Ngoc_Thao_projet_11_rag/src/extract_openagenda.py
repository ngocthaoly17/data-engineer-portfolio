"""
Extraction et nettoyage des événements OpenAgenda pour le POC RAG Puls-Events.

Le script récupère les événements de l'agenda public Culture Versailles,
filtre les événements localisés à Versailles et conserve uniquement les
données récentes de moins d'un an ou à venir.
"""

from __future__ import annotations

import os
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd
import requests
from dotenv import load_dotenv


load_dotenv()

AGENDA_UID = "60871835"
OUTPUT_PATH = Path("data/events_versailles.csv")


def clean_text_key(value) -> str:
    """Retourne une chaîne nettoyée à partir d'une valeur potentiellement vide."""
    if pd.isna(value):
        return ""
    return str(value).strip()


def fetch_events() -> dict:
    """Récupère les événements depuis l'API OpenAgenda."""
    api_key = os.getenv("OPENAGENDA_API_KEY")

    if not api_key:
        raise ValueError(
            "La variable OPENAGENDA_API_KEY est absente du fichier .env."
        )

    url = f"https://api.openagenda.com/v2/agendas/{AGENDA_UID}/events"

    params = {
        "key": api_key,
        "size": 100,
    }

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()

    return response.json()


def clean_events(raw_data: dict) -> pd.DataFrame:
    """
    Nettoie les événements OpenAgenda.

    Les règles appliquées sont :
    - ville égale à Versailles ;
    - date de début inférieure à un an ou à venir ;
    - titre, description, ville et date de début non vides ;
    - suppression des doublons sur title, begin_date et city.
    """
    events = raw_data.get("events", [])
    rows = []

    for event in events:
        title = event.get("title", {}).get("fr", "")
        description = event.get("description", {}).get("fr", "")
        location = event.get("location", {})
        city = location.get("city", "")
        url = event.get("canonicalUrl", "")
        readable_date = event.get("dateRange", {}).get("fr", "")
        begin_raw = event.get("firstTiming", {}).get("begin")

        city_clean = clean_text_key(city)

        if city_clean.lower() != "versailles":
            continue

        if not begin_raw:
            continue

        begin_date = datetime.fromisoformat(begin_raw)
        one_year_ago = datetime.now(begin_date.tzinfo) - timedelta(days=365)

        if begin_date < one_year_ago:
            continue

        rows.append(
            {
                "title": title,
                "description": description,
                "city": city_clean,
                "date": readable_date,
                "begin_date": begin_raw,
                "url": url,
            }
        )

    df = pd.DataFrame(rows)

    if df.empty:
        return df

    for column in ["title", "description", "city", "date", "url"]:
        df[column] = df[column].apply(clean_text_key)

    df = df.dropna(subset=["title", "description", "city", "begin_date"])

    df = df[
        (df["title"] != "")
        & (df["description"] != "")
        & (df["city"] != "")
        & (df["begin_date"] != "")
    ]

    df = df.drop_duplicates(subset=["title", "begin_date", "city"])

    return df


def main() -> None:
    """Exécute l'extraction et sauvegarde le dataset nettoyé."""
    OUTPUT_PATH.parent.mkdir(exist_ok=True)

    raw_data = fetch_events()
    df = clean_events(raw_data)

    if df.empty:
        print("Aucun événement trouvé.")
        return

    df.to_csv(OUTPUT_PATH, index=False, encoding="utf-8")
    print(f"{len(df)} événements sauvegardés dans {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
