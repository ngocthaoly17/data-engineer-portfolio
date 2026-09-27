import sys
from pathlib import Path

sys.path.append(str(Path("scripts").resolve()))

from utils import read_csv_work, write_csv_work, run_sql

liaison = read_csv_work("liaison_normalise.csv",)
liaison_clean = run_sql("dedoublonnage_liaison.sql", {"liaison": liaison}, "liaison_clean")
write_csv_work(liaison_clean, "liaison_clean.csv")
print(f"OK - Liaison nettoyée et dédoublonnée : {len(liaison_clean)} lignes")
