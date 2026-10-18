import pandas as pd

df = pd.read_csv("dataset.csv", index_col="row_id")

print(df.head())
print(df.describe())
print(df.info())


print("==========")
print(df[['kota', 'order_id']].head())

print("==========")
print(df[df['penjualan'] > 100000]['kota'].head())


print("======")

print(df.loc[df['kuantitas'] > 10, ['nama_produk', 'kota']].head())

print("========")

print(df.loc[df['kuantitas'] > 10, 'kota'].head())
