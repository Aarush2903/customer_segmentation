import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


def label_segments(rfm: pd.DataFrame) -> pd.DataFrame:
    df = rfm.copy()
    r = df["R_Score"].astype(int)
    f = df["F_Score"].astype(int)
    m = df["M_Score"].astype(int)

    conditions = [
        (r >= 4) & (f >= 4) & (m >= 4),
        (r >= 3) & (f >= 3),
        (r <= 2) & (f >= 3),
        (r <= 2) & (f <= 2),
    ]
    labels = ["Champions", "Loyal Customers", "At Risk", "Hibernating"]
    df["Segment"] = np.select(conditions, labels, default="Potential Loyalist")
    return df


def run_kmeans_segmentation(rfm: pd.DataFrame, n_clusters: int = 4) -> tuple[pd.DataFrame, KMeans]:
    df = rfm.copy()
    x = np.log1p(df[["Recency", "Frequency", "Monetary"]])
    x_scaled = StandardScaler().fit_transform(x)
    model = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    df["Cluster"] = model.fit_predict(x_scaled)
    return df, model
