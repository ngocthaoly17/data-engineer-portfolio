import sys
from pathlib import Path

sys.path.append(str(Path("scripts").resolve()))

from utils import read_csv_work, write_csv_work, run_sql

erp = read_csv_work("erp_normalise.csv")

if erp.empty:
    raise ValueError("erp_normalise.csv est vide")

erp_clean = run_sql(
    "dedoublonnage_erp.sql",
    {"erp": erp},
    "erp_clean"
)

write_csv_work(erp_clean, "erp_clean.csv")

print(f"OK - ERP nettoyé et dédoublonné : {len(erp_clean)} lignes")