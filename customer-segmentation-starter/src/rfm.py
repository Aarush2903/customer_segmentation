import pandas as pd


def build_rfm(df: pd.DataFrame, snapshot_date: pd.Timestamp | None = None) -> pd.DataFrame:
    if snapshot_date is None:
        snapshot_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)
    rfm = df.groupby("CustomerID").agg(
        Recency=("InvoiceDate", lambda x: (snapshot_date - x.max()).days),
        Frequency=("InvoiceNo", "nunique"),
        Monetary=("SalesLineTotal", "sum"),
    ).reset_index()
    return rfm


def add_rfm_scores(rfm: pd.DataFrame) -> pd.DataFrame:
    out = rfm.copy()
    out["R_Score"] = pd.qcut(out["Recency"], 4, labels=[4, 3, 2, 1], duplicates="drop")
    out["F_Score"] = pd.qcut(out["Frequency"].rank(method="first"), 4, labels=[1, 2, 3, 4], duplicates="drop")
    out["M_Score"] = pd.qcut(out["Monetary"].rank(method="first"), 4, labels=[1, 2, 3, 4], duplicates="drop")
    out["RFM_Score"] = out[["R_Score", "F_Score", "M_Score"]].astype(str).agg("".join, axis=1)
    return out
