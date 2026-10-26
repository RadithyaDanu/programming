import pandas as pd
# No.	Tugas	Petunjuk
# 1	Import Pandas	Gunakan alias pd
# 2	Baca file CSV	Gunakan pd.read_csv()
# 3	Tampilkan 5 baris pertama	Gunakan .head()
# 4	Tampilkan jumlah baris dan kolom	Gunakan .shape
# 5	Periksa tipe data setiap kolom	Gunakan .dtypes


df = pd.read_csv('data.csv')

df['revenue'] = df['price'] * df['quantity'] * (1 - df['discount'])
# print(df['revenue'])

print(df[(df['quantity'] >= 15) & (df['discount'] >= 0)].head())

print("\ndata null : ")
print(df.isnull().sum())

aggregation = df.groupby('product')
print(aggregation['revenue'].sum())

aggregation2 = df.groupby('')

print("\n quantity perjualan terbanyak")
print(aggregation['quantity'].max())

print("\npenjualan tertinggi")
print(aggregation['revenue'].max())


# # proses date jd datetime
# juni = (df['date'] >= '2026-06-01') & (df['date'] <= '2026-06-30')
# juli = (df['date'] >= '2026-07-01') & (df['date'] <= '2026-07-31')
# agustus = (df['date'] >= '2026-08-01') & (df['date'] <= '2026-08-30')
# # filter = df[juni]

# print(filter)

# print(df[df[juni], df['revenue']])
