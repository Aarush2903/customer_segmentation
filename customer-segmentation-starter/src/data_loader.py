from pathlib import Path
import pandas as pd


def load_retail_data(path: str | Path) -> pd.DataFrame:
    path = Path(path)
    if path.suffix.lower() in {".xlsx", ".xls"}:
        return pd.read_excel(path)
    if path.suffix.lower() == ".csv":
        return pd.read_csv(path, encoding="ISO-8859-1")
    raise ValueError(f"Unsupported file type: {path.suffix}")
