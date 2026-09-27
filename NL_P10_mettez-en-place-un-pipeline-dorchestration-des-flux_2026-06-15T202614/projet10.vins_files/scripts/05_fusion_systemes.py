import sys
from pathlib import Path

sys.path.append(str(Path("scripts").resolve()))
from utils import read_csv_work, write_csv_work, run_sql

# P03 — La fusion utilise les tables brutes et non les tables nettoyées
erp_clean = read_csv_work("erp_clean.csv")
liaison_clean = read_csv_work("liaison_clean.csv")
web_clean = read_csv_work("web_clean.csv")

fusion = run_sql(
    "fusion_systemes.sql",
    {"erp_clean": erp_clean, "liaison_clean": liaison_clean, "web_clean": web_clean},
    "donnees_fusionnees",
)
write_csv_work(fusion, "donnees_fusionnees_sans_ca.csv")
print(f"OK - fusion terminée : {len(fusion)} lignes")
