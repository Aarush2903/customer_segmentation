import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def plot_cohort_heatmap(retention: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.heatmap(retention, annot=False, cmap="Blues", ax=ax)
    ax.set_title("Cohort Retention Heatmap")
    ax.set_xlabel("Cohort Index")
    ax.set_ylabel("Cohort Month")
    return fig


def plot_segment_counts(df: pd.DataFrame, segment_col: str = "Segment"):
    fig, ax = plt.subplots(figsize=(10, 5))
    df[segment_col].value_counts().plot(kind="bar", ax=ax)
    ax.set_title("Customer Segment Distribution")
    ax.set_xlabel("Segment")
    ax.set_ylabel("Customer Count")
    return fig
