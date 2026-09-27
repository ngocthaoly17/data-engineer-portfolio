from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
INPUT_DIR = ROOT / "data" / "input"
WORK_DIR = ROOT / "data" / "work"
OUTPUT_DIR = ROOT / "data" / "output"
SQL_DIR = ROOT / "sql"

WORK_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = df.columns.str.strip().str.lower()
    return df


def clean_text_key(series: pd.Series) -> pd.Series:
    return series.astype("string").str.strip()


def read_csv_work(name: str) -> pd.DataFrame:
    return pd.read_csv(WORK_DIR / name)


def write_csv_work(df: pd.DataFrame, name: str) -> None:
    df.to_csv(WORK_DIR / name, index=False, encoding="utf-8-sig")


def write_csv_output(df: pd.DataFrame, name: str) -> None:
    df.to_csv(OUTPUT_DIR / name, index=False, encoding="utf-8-sig")


def run_sql(sql_name: str, registrations: dict[str, pd.DataFrame], table_name: str) -> pd.DataFrame:
    import duckdb
    con = duckdb.connect(database=":memory:")
    for name, df in registrations.items():
        con.register(name, df)
    sql = (SQL_DIR / sql_name).read_text(encoding="utf-8")
    con.execute(sql)
    return con.execute(f"SELECT * FROM {table_name}").fetchdf()
