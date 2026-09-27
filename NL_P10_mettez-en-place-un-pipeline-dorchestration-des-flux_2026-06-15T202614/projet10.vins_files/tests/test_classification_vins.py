import sys
from pathlib import Path
import pandas as pd

sys.path.append(str(Path("scripts").resolve()))

from utils import WORK_DIR

fusion = pd.read_csv(WORK_DIR / "donnees_fusionnees.csv")
premium = pd.read_csv(WORK_DIR / "vins_premium.csv")
ordinaires = pd.read_csv(WORK_DIR / "vins_ordinaires.csv")

moyenne = fusion["prix"].mean()
ecart_type = fusion["prix"].std()

if ecart_type == 0:
    nb_premium_recalcule = 0
else:
    z_score_recalcule = (fusion["prix"] - moyenne) / ecart_type
    nb_premium_recalcule = int((z_score_recalcule > 2).sum())

assert len(premium) + len(ordinaires) == len(fusion), \
    "Total premium + ordinaires différent du total fusion"

assert nb_premium_recalcule == 30, \
    f"Nombre de vins premium attendu : 30, obtenu {nb_premium_recalcule}"

assert len(premium) == nb_premium_recalcule, \
    "Le fichier premium ne correspond pas au z-score recalculé"

assert premium.empty or (premium["z_score"] > 2).all(), \
    "Un vin premium ne respecte pas z_score > 2"

assert ordinaires.empty or (ordinaires["z_score"] <= 2).all(), \
    "Un vin ordinaire ne respecte pas z_score <= 2"

print("OK - classification premium / ordinaire recalculée et cohérente")