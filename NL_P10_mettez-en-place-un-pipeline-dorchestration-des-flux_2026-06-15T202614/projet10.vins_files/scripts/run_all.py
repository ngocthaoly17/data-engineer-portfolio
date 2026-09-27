import sys
from pathlib import Path

sys.path.append(str(Path("scripts").resolve()))
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = [
    "00_check_inputs.py",
    "01_ingestion_normalisation.py",
    "02_clean_erp.py",
    "03_clean_liaison.py",
    "04_clean_web.py",
    "05_fusion_systemes.py",
    "06_calcul_ca.py",
    "07_zscore_exports.py",
]
TESTS = [
    "test_absence_doublons.py",
    "test_valeurs_manquantes.py",
    "test_coherence_jointure.py",
    "test_coherence_ca.py",
    "test_classification_vins.py",
]

for script in SCRIPTS:
    print(f"\n=== Exécution {script} ===")
    runpy.run_path(str(ROOT / "scripts" / script), run_name="__main__")

for test in TESTS:
    print(f"\n=== Test {test} ===")
    runpy.run_path(str(ROOT / "tests" / test), run_name="__main__")

print("\n=== PIPELINE TERMINÉ AVEC SUCCÈS ===")
