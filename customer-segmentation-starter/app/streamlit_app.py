import sys
import tempfile
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import streamlit as st
from src.data_loader import load_retail_data
from src.preprocess import clean_retail_data
from src.rfm import build_rfm, add_rfm_scores
from src.segmentation import label_segments
from src.cohort import build_cohort_retention
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


st.set_page_config(page_title="Customer Segmentation Dashboard", layout="wide")
st.title("Customer Segmentation and Cohort Dashboard")

uploaded_file = st.file_uploader("Upload Online Retail dataset", type=["csv", "xlsx", "xls"])

if uploaded_file is not None:
    temp_path = Path("tmp") / "Online Retail.xlsx"
    temp_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(temp_path)
    else:
        df = pd.read_excel(temp_path)

    st.write("Preview")
    st.dataframe(df.head())

    raw = load_retail_data(temp_path)
    clean = clean_retail_data(raw)
    rfm = build_rfm(clean)
    rfm = add_rfm_scores(rfm)
    segmented = label_segments(rfm)
    retention = build_cohort_retention(clean)

    st.subheader("Cleaned transactions")
    st.dataframe(clean.head())

    st.subheader("RFM table")
    st.dataframe(segmented.head())

    st.subheader("Segment counts")
    st.bar_chart(segmented["Segment"].value_counts())

    st.subheader("Cohort retention")
    st.dataframe(retention)
else:
    st.info("Upload the raw Online Retail dataset to begin analysis.")
