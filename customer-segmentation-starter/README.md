# Customer Segmentation and Market Basket Analysis

A recruiter-friendly end-to-end analytics project built on the Online Retail dataset. The project focuses on customer segmentation using RFM features, cohort retention analysis, and optional market basket analysis.

## Project goals

- Clean and validate retail transaction data.
- Build customer-level RFM features.
- Segment customers using rules and clustering.
- Analyze cohort retention behavior.
- Extract product association patterns using market basket analysis.
- Deliver results through a Streamlit dashboard.

## Suggested workflow

1. Load and clean the raw dataset.
2. Perform exploratory data analysis.
3. Build RFM features.
4. Create customer segments.
5. Build cohort retention tables.
6. Run market basket analysis.
7. Publish visual outputs and dashboard.

## Folder structure

```text
customer-segmentation-starter/
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_rfm_segmentation.ipynb
│   ├── 04_cohort_analysis.ipynb
│   ├── 05_market_basket.ipynb
│   └── 06_dashboard_prep.ipynb
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── preprocess.py
│   ├── rfm.py
│   ├── segmentation.py
│   ├── cohort.py
│   ├── market_basket.py
│   └── visualize.py
├── app/
│   └── streamlit_app.py
├── models/
├── reports/
│   └── figures/
└── tests/
    └── test_preprocess.py
```

## Dataset expectations

Expected columns:
- `InvoiceNo`
- `StockCode`
- `Description`
- `Quantity`
- `InvoiceDate`
- `UnitPrice`
- `CustomerID`
- `Country`

Place the raw CSV or XLSX file inside `data/raw/`.

## Run locally

```bash
pip install -r requirements.txt
jupyter notebook
```

To run the dashboard:

```bash
streamlit run app/streamlit_app.py
```
