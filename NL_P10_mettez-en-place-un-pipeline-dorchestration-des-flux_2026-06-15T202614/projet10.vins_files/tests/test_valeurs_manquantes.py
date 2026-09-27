import sys
from pathlib import Path

sys.path.append(str(Path("scripts").resolve()))

from utils import read_csv_work

df = read_csv_work("donnees_fusionnees.csv")

colonnes_obligatoires = [
    "product_id",
    "sku",
    "prix",
    "total_sales",
    "chiffre_affaires",
]

colonnes_absentes = [
    col for col in colonnes_obligatoires
    if col not in df.columns
]

assert not colonnes_absentes, (
    f"Colonnes obligatoires absentes : {colonnes_absentes}"
)

assert df[colonnes_obligatoires].isna().sum().sum() == 0, (
    "Valeurs manquantes détectées"
)

print("OK - absence de valeurs manquantes")