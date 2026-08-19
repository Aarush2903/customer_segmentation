import pandas as pd
from src.preprocess import clean_retail_data


def test_clean_retail_data_removes_invalid_rows():
    df = pd.DataFrame({
        "InvoiceNo": ["10001", "C10002"],
        "StockCode": ["A", "B"],
        "Description": ["Item A", "Item B"],
        "Quantity": [2, 1],
        "InvoiceDate": ["2011-01-01", "2011-01-02"],
        "UnitPrice": [3.0, 4.0],
        "CustomerID": [12345, 12346],
        "Country": ["UK", "UK"],
    })
    out = clean_retail_data(df)
    assert len(out) == 1
    assert "SalesLineTotal" in out.columns
