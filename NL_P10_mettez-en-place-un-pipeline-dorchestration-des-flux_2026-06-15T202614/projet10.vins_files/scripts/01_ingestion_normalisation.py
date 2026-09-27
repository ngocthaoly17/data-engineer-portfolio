import sys
from pathlib import Path

sys.path.append(str(Path("scripts").resolve()))

import pandas as pd
from utils import INPUT_DIR, normalize_columns, clean_text_key, write_csv_work


erp = normalize_columns(pd.read_excel(INPUT_DIR / "Fichier_erp.xlsx"))
liaison = normalize_columns(pd.read_excel(INPUT_DIR / "fichier_liaison.xlsx"))
web = normalize_columns(pd.read_excel(INPUT_DIR / "Fichier_web.xlsx"))

erp["product_id"] = pd.to_numeric(erp["product_id"], errors="coerce")
liaison["product_id"] = pd.to_numeric(liaison["product_id"], errors="coerce")

# P05 — pn retire les fillna(0) pour ne pas biaisé les statistiques.
erp["price"] = pd.to_numeric(erp["price"], errors="coerce")
erp["stock_quantity"] = pd.to_numeric(erp["stock_quantity"], errors="coerce")
web["total_sales"] = pd.to_numeric(web["total_sales"], errors="coerce")


# P04 — Les valeurs manquantes deviennent le texte "nan"
# Cette fois je fais le dropna avant de mettre en texte.
liaison = liaison.dropna(subset=["product_id", "id_web"])
web = web.dropna(subset=["sku"])

liaison["id_web"] = clean_text_key(liaison["id_web"])
web["sku"] = clean_text_key(web["sku"])

erp = erp.dropna(subset=["product_id", "price"])
web = web.dropna(subset=["sku", "total_sales", "post_type"])

write_csv_work(erp, "erp_normalise.csv")
write_csv_work(liaison, "liaison_normalise.csv")
write_csv_work(web, "web_normalise.csv")

print("OK - ingestion et normalisation terminées")
print(f"ERP normalisé : {len(erp)} lignes")
print(f"Liaison normalisée : {len(liaison)} lignes")
print(f"Web normalisé : {len(web)} lignes")
