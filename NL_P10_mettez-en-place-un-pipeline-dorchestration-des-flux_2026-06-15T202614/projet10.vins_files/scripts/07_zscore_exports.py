import sys
from pathlib import Path

sys.path.append(str(Path("scripts").resolve()))
import pandas as pd
from utils import read_csv_work, write_csv_work, write_csv_output, OUTPUT_DIR

fusion = read_csv_work("ca_produit.csv")

moyenne = fusion["prix"].mean()
ecart_type = fusion["prix"].std()

if ecart_type == 0:
    fusion["z_score"] = 0.0
else:
    fusion["z_score"] = (fusion["prix"] - moyenne) / ecart_type

fusion["categorie_vin"] = fusion["z_score"].apply(
    lambda z: "premium_millesime" if z > 2 else "ordinaire"
)

vins_premium = fusion[fusion["z_score"] > 2].copy()
vins_ordinaires = fusion[fusion["z_score"] <= 2].copy()

# P11 — Le chiffre d’affaires est regroupé par nom et non par produit
rapport_ca = (
    fusion.groupby(["product_id", "sku", "nom_produit"], as_index=False)
    .agg(
        chiffre_affaires=("chiffre_affaires", "sum"),
        total_ventes=("total_sales", "sum"),
        prix_moyen=("prix", "mean"),
    )
    .sort_values("chiffre_affaires", ascending=False)
)

ca_global = round(float((fusion["prix"] * fusion["total_sales"]).sum()), 2)

with pd.ExcelWriter(OUTPUT_DIR / "rapport_ca.xlsx", engine="openpyxl") as writer:
    rapport_ca.to_excel(writer, sheet_name="CA par produit", index=False)
    pd.DataFrame({
        "indicateur": [
            "Chiffre d'affaires global",
            "Nombre de produits fusionnes",
            "Nombre de vins premium",
            "Nombre de vins ordinaires",
        ],
        "valeur": [
            ca_global,
            len(fusion),
            len(vins_premium),
            len(vins_ordinaires),
        ],
    }).to_excel(writer, sheet_name="CA global", index=False)

write_csv_output(fusion, "donnees_fusionnees.csv")
write_csv_output(vins_premium, "vins_premium.csv")
write_csv_output(vins_ordinaires, "vins_ordinaires.csv")

write_csv_work(fusion, "donnees_fusionnees.csv")
write_csv_work(vins_premium, "vins_premium.csv")
write_csv_work(vins_ordinaires, "vins_ordinaires.csv")

print("OK - z-score, classification et exports terminés")
print(f"Produits fusionnés : {len(fusion)}")
print(f"Vins premium : {len(vins_premium)}")
print(f"Vins ordinaires : {len(vins_ordinaires)}")
print(f"CA global : {ca_global}")
