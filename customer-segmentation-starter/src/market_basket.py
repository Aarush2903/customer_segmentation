import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules


def build_basket_matrix(df: pd.DataFrame, country: str | None = None) -> pd.DataFrame:
    data = df.copy()
    if country:
        data = data[data["Country"] == country]
    basket = (
        data.groupby(["InvoiceNo", "Description"])["Quantity"]
        .sum()
        .unstack()
        .fillna(0)
    )
    basket = basket.map(lambda x: 1 if x > 0 else 0)
    return basket


def generate_association_rules(basket: pd.DataFrame, min_support: float = 0.02, metric: str = "lift", min_threshold: float = 1.0) -> pd.DataFrame:
    frequent_itemsets = apriori(basket, min_support=min_support, use_colnames=True)
    if frequent_itemsets.empty:
        return frequent_itemsets
    rules = association_rules(frequent_itemsets, metric=metric, min_threshold=min_threshold)
    return rules.sort_values([metric, "confidence"], ascending=False)
