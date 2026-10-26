import pandas as pd

df = pd.read_csv("dataset.csv", index_col="row_id")

print(df.head())
# 1. selection

print(df.loc[7981, ['row_id']])
