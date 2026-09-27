import sys
from pathlib import Path

sys.path.append(str(Path("scripts").resolve()))
from utils import read_csv_work, write_csv_work, run_sql

web = read_csv_work("web_normalise.csv")
web_clean = run_sql("dedoublonnage_web.sql", {"web": web}, "web_clean")
write_csv_work(web_clean, "web_clean.csv")
print(f"OK - Web nettoyé et dédoublonné : {len(web_clean)} lignes")
