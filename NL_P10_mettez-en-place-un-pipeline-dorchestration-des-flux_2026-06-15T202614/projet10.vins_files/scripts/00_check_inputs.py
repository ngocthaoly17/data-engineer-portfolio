from pathlib import Path

INPUT_DIR = Path("data/input")

FILES = [
    "Fichier_erp.xlsx",
    "fichier_liaison.xlsx",
    "Fichier_web.xlsx",
]

for filename in FILES:
    path = INPUT_DIR / filename
    print(f"Vérification : {path}")

    if not path.exists():
        raise FileNotFoundError(f"Fichier source manquant : {path}")

print("OK - les 3 fichiers sources sont présents")