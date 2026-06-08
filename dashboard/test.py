import pandas as pd

df = pd.read_parquet(
    "data/revenue_by_category"
)

print(df.head())
