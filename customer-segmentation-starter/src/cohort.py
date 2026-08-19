import pandas as pd


def _month_start(ts: pd.Timestamp) -> pd.Timestamp:
    return pd.Timestamp(ts.year, ts.month, 1)


def build_cohort_retention(df: pd.DataFrame) -> pd.DataFrame:
    data = df.copy()
    data["InvoiceMonth"] = data["InvoiceDate"].apply(_month_start)
    data["CohortMonth"] = data.groupby("CustomerID")["InvoiceDate"].transform("min").apply(_month_start)
    year_diff = data["InvoiceMonth"].dt.year - data["CohortMonth"].dt.year
    month_diff = data["InvoiceMonth"].dt.month - data["CohortMonth"].dt.month
    data["CohortIndex"] = year_diff * 12 + month_diff + 1
    grouped = data.groupby(["CohortMonth", "CohortIndex"])["CustomerID"].nunique().reset_index()
    cohort_counts = grouped.pivot(index="CohortMonth", columns="CohortIndex", values="CustomerID")
    retention = cohort_counts.divide(cohort_counts.iloc[:, 0], axis=0)
    return retention
