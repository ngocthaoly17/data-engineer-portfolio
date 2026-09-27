import sys
from pathlib import Path

sys.path.append(str(Path("scripts").resolve()))

from utils import read_csv_work

df = read_csv_work("donnees_fusionnees.csv")

if len(df) != 714:
    raise ValueError(f"Erreur jointure : attendu 714 lignes, obtenu {len(df)}")

if df.empty:
    raise ValueError("Erreur jointure : fichier fusionné vide")

print("OK - cohérence de la jointure")