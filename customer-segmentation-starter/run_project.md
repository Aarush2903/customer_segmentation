# Running the Customer Segmentation Project

This guide explains how to run the customer segmentation and market basket analysis project from setup to final dashboard. The workflow uses notebooks for development, reusable Python modules in `src/`, tests from the project root, and a Streamlit app for the final demo layer .

## Project workflow

Run the project in this order:

1. Create and activate a virtual environment .
2. Install dependencies from `requirements.txt` .
3. Place the raw Online Retail dataset inside `data/raw/` .
4. Run the notebooks in sequence so each step produces inputs for the next one .
5. Run tests from the repository root with `pytest` .
6. Launch the Streamlit app with `streamlit run app/streamlit_app.py` .

## Folder assumptions

The guide assumes this project structure:

```text
customer-segmentation-starter/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── src/
├── app/
├── tests/
├── requirements.txt
└── README.md
```

The notebooks depend on a cleaned dataset produced during preprocessing, and the app depends on the reusable logic stored in `src/` .

## Setup

Open a terminal in the project root and run:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows PowerShell, activate the environment with:

```bash
.venv\Scripts\Activate.ps1
```

After installation, copy the Kaggle dataset file into `data/raw/`. The starter notebooks were written to search that folder for a CSV or Excel file before they run .

## Notebook order

Run the notebooks in this sequence:

1. `01_eda.ipynb` — schema checks, null analysis, revenue sanity checks, and quick business understanding .
2. `02_preprocessing.ipynb` — cleans the dataset and saves `data/processed/online_retail_clean.csv` .
3. `03_rfm_segmentation.ipynb` — builds recency, frequency, and monetary features, then creates customer segments .
4. `04_cohort_analysis.ipynb` — creates monthly cohort retention tables and a heatmap .
5. `05_market_basket.ipynb` — builds the basket matrix and association rules .
6. `06_dashboard_prep.ipynb` — exports dashboard-ready CSV files for the app layer .

A convenient way to start notebooks is:

```bash
jupyter notebook
```

Launch Jupyter from the project root so imports from `src/` and relative paths are easier to manage in a standard repository workflow .

## Testing

Run tests from the project root:

```bash
pytest
```

This follows the typical Python testing workflow where `pytest` discovers tests in the `tests/` directory and executes them from the repository root .

## Streamlit app

After preprocessing or dashboard preparation is complete, start the app with:

```bash
streamlit run app/streamlit_app.py
```

Streamlit runs the script locally and serves the interface in a browser tab as part of its standard development workflow . In this project, the app is the demo layer for uploading data, previewing cleaned output, viewing RFM segments, and checking cohort results through the logic stored in `src/` .

## Typical daily workflow

A normal development cycle looks like this:

- Add or update the raw dataset in `data/raw/` .
- Run `02_preprocessing.ipynb` to refresh the cleaned dataset .
- Run segmentation, cohort, and basket notebooks to regenerate analysis outputs .
- Run `06_dashboard_prep.ipynb` to save dashboard CSV files .
- Run `pytest` to validate core logic .
- Launch Streamlit for the final demo .

## Troubleshooting

| Problem | Likely cause | Fix |
|---|---|---|
| `FileNotFoundError` for dataset | No raw file in `data/raw/` | Copy the Kaggle file into `data/raw/`  |
| `Run 02_preprocessing.ipynb first` | Cleaned dataset not created yet | Execute notebook 2 before later notebooks  |
| `ModuleNotFoundError: src` | Jupyter launched from the wrong folder | Start Jupyter from the project root  |
| Streamlit app shows no data | No file uploaded in the app | Upload the Online Retail file in the Streamlit interface  |
| Tests not discovered | Running from the wrong directory | Run `pytest` from the repository root  |

## Minimum command list

If the goal is just to get the project working end to end, these are the minimum commands:

```bash
cd customer-segmentation-starter
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```

Then run the notebooks in order, and finally:

```bash
streamlit run app/streamlit_app.py
```
