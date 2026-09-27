import sys
from pathlib import Path

sys.path.append(str(Path("scripts").resolve()))

import pandas as pd
from utils import read_csv_work, OUTPUT_DIR

fusion = read_csv_work("donnees_fusionnees.csv")

ca_recalcule = round(
    float((fusion["prix"] * fusion["total_sales"]).sum()),
    2
)

ca_global_sheet = pd.read_excel(
    OUTPUT_DIR / "rapport_ca.xlsx",
    sheet_name="CA global"
)

ca_global_exporte = round(
    float(ca_global_sheet.loc[0, "valeur"]),
    2
)

assert ca_recalcule == ca_global_exporte, (
    f"CA global incohérent : recalculé={ca_recalcule}, exporté={ca_global_exporte}"
)

assert ca_recalcule == 70568.60, (
    f"CA global attendu 70568.60, obtenu {ca_recalcule}"
)

print("OK - cohérence du chiffre d'affaires")