# Customer Segmentation and Cohort Analytics

A Streamlit dashboard that segments customers based on RFM (Recency, Frequency, Monetary) behavior and tracks retention patterns across acquisition cohorts to identify high-value and high-risk customer groups.

**Live app:** `localhost:8501` (run locally via `streamlit run app/streamlit_app.py`)

## Problem statement

Most businesses know overall churn or revenue numbers, but they often do not know which customer groups behave differently over time. This project answers two questions:
- Which customer segments are most valuable or most at risk?
- How does retention change across acquisition cohorts?

The output is intended for product, marketing, retention, and customer success decision-making.

## Objectives

- Build a clean customer-level analytical dataset.
- Engineer lifecycle and behavioral features.
- Segment customers using RFM scoring.
- Perform cohort retention analysis.
- Deliver findings in an interactive Streamlit dashboard.

## Dataset

**Used:** Online Retail dataset (`Online Retail.xlsx`, ~22.6MB) — UK-based online retailer transactions, uploaded directly through the dashboard.

Columns: `InvoiceNo`, `StockCode`, `Description`, `Quantity`, `InvoiceDate`, `UnitPrice`, `CustomerID`, `Country`.

Other datasets this pipeline generalizes to:
- Telecom churn dataset.
- Bank customer churn dataset.
- SaaS subscription dataset.

Minimum required columns for any dataset used with this app:
- `customer_id`
- `transaction_date` or `signup_date`
- `amount` or revenue proxy
- `product/service` features
- optional demographic or region fields

## Project structure

```text
customer-segmentation-cohort/
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_feature_engineering.ipynb
│   └── 03_segmentation.ipynb
├── src/
│   ├── features.py
│   ├── clustering.py
│   └── cohort.py
├── app/
│   └── streamlit_app.py
├── models/
├── reports/
│   └── figures/
└── tests/
```

## Methodology

### 1. Data preparation
- Upload the raw Online Retail workbook directly in the app.
- Clean the transaction table and derive a `SalesLineTotal` column (`Quantity × UnitPrice`).
- Standardize dates and drop invalid/duplicate rows.

### 2. Feature engineering
- Recency — days since each customer's last purchase.
- Frequency — number of distinct purchases per customer.
- Monetary — total spend per customer.

### 3. Segmentation (RFM scoring)
- Score each customer 1–4 on Recency, Frequency, and Monetary (`R_Score`, `F_Score`, `M_Score`), combined into an `RFM_Score`.
- Map scores to named segments: **Champions**, **Loyal Customers**, **Potential Loyalist**, **At Risk**, **Hibernating**.
- Display segment counts as a bar chart for a quick distribution view.

### 4. Cohort analysis
- Group customers into cohorts by first purchase month (`CohortMonth`).
- Track retention rate by cohort age (months 1–13+) in a cohort retention table.
- Compare retention decay across cohorts to spot patterns (e.g. the Dec 2010 cohort retains far better than later cohorts).

### 5. Communication layer
- Interactive Streamlit dashboard: upload → cleaned transactions → RFM table → segment counts → cohort retention, all in one flow.

## Dashboard walkthrough

1. **Upload & preview** — upload the Online Retail workbook; the app previews raw rows and shows the cleaned transaction table with `SalesLineTotal` computed.

   ![Upload and cleaned transaction preview](reports/figures/01_upload_preview.png)

2. **RFM table & segment counts** — per-customer Recency, Frequency, Monetary values, their R/F/M scores, the resulting segment label, and a bar chart of customer counts across the five segments (Hibernating and Loyal Customers are typically the largest groups in this dataset).

   ![RFM table and segment counts](reports/figures/02_rfm_segments.png)

3. **Cohort retention** — a month-by-cohort-age retention matrix showing what fraction of each signup cohort is still active in subsequent months.

   ![Cohort retention table](reports/figures/03_cohort_retention.png)

## Expected outputs

- Segment definitions with business interpretation.
- Cohort retention heatmap/table.
- Revenue and churn breakdown by segment.
- Interactive dashboard (screenshots below).

## Evaluation

This project is evaluated more by interpretability and business usefulness than by predictive accuracy. Good outcomes include:
- Clearly distinct segments.
- Cohorts with visible retention differences.
- Actionable recommendations for retention or growth.

## Tools and libraries

- Python
- pandas, numpy
- scikit-learn
- matplotlib, seaborn, plotly
- SQL
- Streamlit

## How to run

```bash
pip install -r requirements.txt
jupyter notebook
```

To run the app:

```bash
streamlit run app/streamlit_app.py
```

Then open `localhost:8501` and upload your transactions file.

## Portfolio value

This project demonstrates:
- Customer analytics.
- Feature engineering.
- RFM-based segmentation.
- Cohort retention analysis.
- Interactive dashboard building and business storytelling.

## Resume bullet

Built a customer segmentation and cohort analytics dashboard using Python and Streamlit, applying RFM scoring to segment customers into five behavioral groups and cohort retention analysis to surface retention opportunities from 500K+ transaction records.

## Next improvements

- Add clustering-based segmentation (KMeans/hierarchical) alongside RFM scoring, for comparison.
- Add revenue and churn breakdown per segment.
- Add uplift-style retention experiments.
- Add automated segment refresh pipeline.
- Deploy the app (Streamlit Community Cloud or similar) instead of running locally only.
