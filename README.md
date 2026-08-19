# Customer Segmentation and Cohort Analytics

A portfolio project that segments customers based on behavior and lifecycle features, then tracks retention patterns across cohorts to identify high-value and high-risk groups.

## Problem statement

Most businesses know overall churn or revenue numbers, but they often do not know which customer groups behave differently over time. This project answers two questions:
- Which customer segments are most valuable or most at risk?
- How does retention change across acquisition cohorts?

The output is intended for product, marketing, retention, and customer success decision-making.

## Objectives

- Build a clean customer-level analytical dataset.
- Engineer lifecycle and behavioral features.
- Segment customers using clustering or business-rule-based grouping.
- Perform cohort retention analysis.
- Deliver findings in a dashboard or shareable report.

## Dataset

Suggested inputs:
- Ecommerce or online retail transactions.
- Telecom churn dataset.
- Bank customer churn dataset.
- SaaS subscription dataset.

Minimum required columns:
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
- Audit missing values, duplicates, and invalid IDs.
- Standardize dates and category labels.
- Create a customer-level analytical base table.

### 2. Feature engineering
Create features such as:
- Tenure.
- Recency.
- Frequency.
- Monetary value.
- Product breadth.
- Complaint or inactivity indicators.

### 3. Segmentation
Possible approaches:
- RFM scoring.
- KMeans clustering.
- Hierarchical clustering.
- Rule-based business segmentation.

### 4. Cohort analysis
- Group customers by signup month or first purchase month.
- Measure retention by cohort age.
- Compare revenue and churn across cohorts.

### 5. Communication layer
- Build a Streamlit dashboard or BI report.
- Add segment-level business recommendations.

## Expected outputs

- Segment definitions with business interpretation.
- Cohort retention heatmap.
- Revenue and churn breakdown by segment.
- Dashboard screenshots or interactive app.

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

## Portfolio value

This project demonstrates:
- Customer analytics.
- Feature engineering.
- Clustering.
- Cohort retention analysis.
- Business storytelling.

## Resume bullet

Built a customer segmentation and cohort analytics pipeline using Python, SQL, and clustering to identify high-value and high-risk customer groups and surface retention opportunities.

## Next improvements

- Add uplift-style retention experiments.
- Compare unsupervised and rule-based segmentation.
- Add automated segment refresh pipeline.
