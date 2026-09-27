import sys
from pathlib import Path

sys.path.append(str(Path("scripts").resolve()))

from utils import read_csv_work

df = read_csv_work("donnees_fusionnees.csv")

assert df["product_id"].duplicated().sum() == 0, "Doublons product_id détectés"
assert df["sku"].duplicated().sum() == 0, "Doublons sku détectés"

print("OK - absence de doublons")