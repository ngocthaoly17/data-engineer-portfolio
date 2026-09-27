import sys
from pathlib import Path

sys.path.append(str(Path("scripts").resolve()))
from utils import read_csv_work, write_csv_work, run_sql

fusion = read_csv_work("donnees_fusionnees_sans_ca.csv")
ca_produit = run_sql("calcul_ca.sql", {"donnees_fusionnees": fusion}, "ca_produit")
write_csv_work(ca_produit, "ca_produit.csv")
print(f"OK - chiffre d'affaires calculé : {len(ca_produit)} produits")
