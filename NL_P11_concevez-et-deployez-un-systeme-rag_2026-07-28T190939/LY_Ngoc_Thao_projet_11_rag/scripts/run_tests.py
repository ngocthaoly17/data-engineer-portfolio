"""Pipeline local de validation Pytest."""

from __future__ import annotations

import subprocess
import sys


def main() -> int:
    """Exécute la suite de tests unitaires du projet."""
    return subprocess.call([sys.executable, "-m", "pytest", "-v"])


if __name__ == "__main__":
    raise SystemExit(main())
